Title: 细说uWSGI的优雅重启
Date: 2025-09-29 20:20
Modified: 2025-09-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T7
Authors: nJcx
Summary: 细说uWSGI的优雅重启 ~

#### 介绍

uWSGI 是一个功能强大的应用服务器,主要用于部署 Python Web 应用。它充当 Web 服务器(如 Nginx、Apache)和 Python Web 应用之间的桥梁。它的名字来源于 WSGI 协议,但功能远不止于此。uWSGI 用 C 语言编写,性能优异,支持多进程、多线程和异步模式,能够处理大量并发请求。在生产环境中,通常的架构是:浏览器 → Nginx(反向代理) → uWSGI(应用服务器) → Django/Flask(Web框架)。Nginx 负责处理静态文件和反向代理,uWSGI 负责运行 Python 应用,两者通过 uwsgi 协议或 HTTP 协议通信。



####  核心工作流程

uWSGI 的核心是一个事件驱动的应用容器,主要包含以下几个关键组件:

1. 主进程(Master Process)
主进程负责:

	- 管理工作进程的生命周期
	
	- 监控进程状态,自动重启崩溃的进程
	
	- 处理信号(如平滑重启)
	
	- 加载配置文件

```
#简化的主进程逻辑, 伪代码
while True:
    # 检查工作进程状态
    for worker in workers:
        if worker.is_dead():
            worker.respawn()
    
    # 处理信号
    if received_reload_signal:
        graceful_reload()
```

2. 工作进程(Worker Process)
每个工作进程独立处理请求:

```
# Worker 的基本结构, 伪代码
def worker_loop():
    while True:
        # 1. 接收请求(从 socket)
        request = accept_connection()
        
        # 2. 解析请求(uwsgi/http 协议)
        env = parse_request(request)
        
        # 3. 调用 WSGI 应用
        response = wsgi_app(env, start_response)
        
        # 4. 返回响应
        send_response(response)
        
```

####  uWSGI 是怎么调用Python的Web应用的？

uWSGI 使用 Python C API 来嵌入 Python 解释器并调用 Python 代码。下面以一个Python  Flask 应用为例。


1， 初始化 Python 解释器

```bash

#include <Python.h>

// uWSGI 启动时初始化 Python
void init_python() {
    // 初始化 Python 解释器
    Py_Initialize();
    
    // 设置 Python 路径
    PySys_SetPath(L"/usr/lib/python3.9:/path/to/your/app");
}


```

2， 加载 Flask 应用

```bash

// 加载 Python 模块和应用对象
PyObject *load_wsgi_application(const char *module_name, const char *app_name) {
    PyObject *pModule, *pApp;
    
    // 导入模块 (例如: "myapp")
    // 相当于 Python 的: import myapp
    pModule = PyImport_ImportModule(module_name);
    if (pModule == NULL) {
        PyErr_Print();
        return NULL;
    }
    
    // 获取应用对象 (例如: app = myapp.application)
    // 相当于 Python 的: app = myapp.application
    pApp = PyObject_GetAttrString(pModule, app_name);
    if (pApp == NULL || !PyCallable_Check(pApp)) {
        PyErr_Print();
        Py_DECREF(pModule);
        return NULL;
    }
    
    return pApp;
}


```


3， 构造 WSGI environ 字典

```bash
// 将 HTTP 请求转换为 Python 字典
PyObject *build_environ(struct http_request *req) {
    PyObject *environ = PyDict_New();
    
    // 添加请求方法
    // environ['REQUEST_METHOD'] = 'GET'
    PyDict_SetItemString(environ, "REQUEST_METHOD", 
                        PyUnicode_FromString(req->method));
    
    // 添加路径
    // environ['PATH_INFO'] = '/hello'
    PyDict_SetItemString(environ, "PATH_INFO", 
                        PyUnicode_FromString(req->path));
    
    // 添加查询字符串
    // environ['QUERY_STRING'] = 'id=123'
    PyDict_SetItemString(environ, "QUERY_STRING", 
                        PyUnicode_FromString(req->query));
    
    // 添加 HTTP 头
    // environ['HTTP_HOST'] = 'example.com'
    for (int i = 0; i < req->header_count; i++) {
        char key[256];
        snprintf(key, sizeof(key), "HTTP_%s", req->headers[i].name);
        PyDict_SetItemString(environ, key, 
                            PyUnicode_FromString(req->headers[i].value));
    }
    
    // 添加 WSGI 必需的变量
    PyDict_SetItemString(environ, "wsgi.version", 
                        Py_BuildValue("(ii)", 1, 0));
    
    PyDict_SetItemString(environ, "wsgi.url_scheme", 
                        PyUnicode_FromString(req->is_https ? "https" : "http"));
    
    // 添加请求体输入流
    PyDict_SetItemString(environ, "wsgi.input", 
                        create_input_stream(req->body, req->body_len));
    
    // 添加错误流
    PyDict_SetItemString(environ, "wsgi.errors", PySys_GetObject("stderr"));
    
    PyDict_SetItemString(environ, "wsgi.multithread", Py_True);
    PyDict_SetItemString(environ, "wsgi.multiprocess", Py_True);
    PyDict_SetItemString(environ, "wsgi.run_once", Py_False);
    
    return environ;
}

```

4，创建 start_response 回调

```bash

// 用于存储响应状态和头部
struct response_data {
    char *status;
    PyObject *headers;
};

// start_response 的 C 实现
static PyObject *start_response_callback(PyObject *self, PyObject *args) {
    struct response_data *resp = (struct response_data *)PyCapsule_GetPointer(self, NULL);
    PyObject *status_obj, *headers_obj, *exc_info = NULL;
    
    // 解析参数: start_response(status, response_headers, exc_info=None)
    if (!PyArg_ParseTuple(args, "OO|O:start_response", 
                         &status_obj, &headers_obj, &exc_info)) {
        return NULL;
    }
    
    // 保存状态码 "200 OK"
    const char *status = PyUnicode_AsUTF8(status_obj);
    resp->status = strdup(status);
    
    // 保存响应头 [('Content-Type', 'text/html'), ...]
    resp->headers = headers_obj;
    Py_INCREF(headers_obj);
    
    // 返回一个写入函数(通常不用)
    Py_RETURN_NONE;
}

// 创建 start_response 可调用对象
PyObject *create_start_response(struct response_data *resp) {
    // 将 C 指针封装到 Python 对象
    PyObject *capsule = PyCapsule_New(resp, NULL, NULL);
    
    // 创建方法对象
    static PyMethodDef method_def = {
        "start_response", start_response_callback, METH_VARARGS, NULL
    };
    
    return PyCFunction_New(&method_def, capsule);
}

```


5, 调用 Flask 应用

```bash

// 完整的请求处理流程
void handle_wsgi_request(PyObject *app, struct http_request *req, 
                        struct http_response *resp) {
    // 1. 构造 environ 字典
    PyObject *environ = build_environ(req);
    
    // 2. 创建 start_response 回调
    struct response_data response_data = {0};
    PyObject *start_response = create_start_response(&response_data);
    
    // 3. 调用 WSGI 应用
    // 相当于: response_body = app(environ, start_response)
    PyObject *args = PyTuple_Pack(2, environ, start_response);
    PyObject *result = PyObject_CallObject(app, args);
    
    if (result == NULL) {
        PyErr_Print();
        goto cleanup;
    }
    
    // 4. 处理响应状态和头部
    resp->status = response_data.status;  // "200 OK"
    
    // 解析响应头
    Py_ssize_t header_count = PyList_Size(response_data.headers);
    for (Py_ssize_t i = 0; i < header_count; i++) {
        PyObject *header_tuple = PyList_GetItem(response_data.headers, i);
        PyObject *name = PyTuple_GetItem(header_tuple, 0);
        PyObject *value = PyTuple_GetItem(header_tuple, 1);
        
        const char *header_name = PyUnicode_AsUTF8(name);
        const char *header_value = PyUnicode_AsUTF8(value);
        
        // 添加到响应头
        add_response_header(resp, header_name, header_value);
    }
    
    // 5. 处理响应体(迭代器)
    // Flask 返回的是一个可迭代对象
    PyObject *iterator = PyObject_GetIter(result);
    if (iterator == NULL) {
        PyErr_Print();
        goto cleanup;
    }
    
    PyObject *item;
    while ((item = PyIter_Next(iterator))) {
        // 获取字节数据
        Py_ssize_t size;
        char *data;
        
        if (PyBytes_Check(item)) {
            PyBytes_AsStringAndSize(item, &data, &size);
        } else if (PyUnicode_Check(item)) {
            data = (char *)PyUnicode_AsUTF8AndSize(item, &size);
        }
        
        // 发送响应体数据
        send_response_chunk(resp, data, size);
        
        Py_DECREF(item);
    }
    
    Py_DECREF(iterator);
    
cleanup:
    Py_DECREF(environ);
    Py_DECREF(start_response);
    Py_DECREF(args);
    if (result) Py_DECREF(result);
}


```

假设有这样一个 Flask 应用:

```bash

# myapp.py
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

# WSGI 入口
application = app


```

uWSGI 的 C 代码调用流程:

```bash


int main() {
    // 1. 初始化 Python
    Py_Initialize();
    
    // 2. 加载 Flask 应用
    // import myapp
    // app = myapp.application
    PyObject *flask_app = load_wsgi_application("myapp", "application");
    
    // 3. 接收 HTTP 请求
    struct http_request req = {
        .method = "GET",
        .path = "/hello",
        .query = "",
        // ...
    };
    
    // 4. 调用 Flask 处理请求
    struct http_response resp = {0};
    handle_wsgi_request(flask_app, &req, &resp);
    
    // 5. 发送响应给客户端
    printf("HTTP/1.1 %s\r\n", resp.status);
    for (int i = 0; i < resp.header_count; i++) {
        printf("%s: %s\r\n", resp.headers[i].name, resp.headers[i].value);
    }
    printf("\r\n%s", resp.body);
    
    // 6. 清理
    Py_DECREF(flask_app);
    Py_Finalize();
    
    return 0;
}

```



#### 所以， uWSGI 是如何重启，而不丢请求的？


平滑重启的关键是：新旧进程共存期间的请求转移，确保：

 - 旧进程处理完手头的请求才退出
 - 新进程提前启动接管新请求
 - Socket 连接不中断



1. 初始状态

```bash
	Master Process (PID: 1000)
	├── Worker 1 (PID: 1001) - 处理请求中
	├── Worker 2 (PID: 1002) - 空闲
	├── Worker 3 (PID: 1003) - 处理请求中
	└── Worker 4 (PID: 1004) - 空闲

	监听 Socket: /tmp/uwsgi.sock (由 Master 持有)
```


2, 接收重启信号

```bash

// Master 进程接收信号
void signal_handler(int signum) {
    if (signum == SIGHUP) {  // kill -HUP <master_pid>
        graceful_reload = 1;
    }
}

// 主循环
while (1) {
    if (graceful_reload) {
        do_graceful_reload();
        graceful_reload = 0;
    }
    // 其他工作...
}

```

3, 创建新 Worker（关键步骤）


```bash
void do_graceful_reload() {
    // 步骤 1: 标记旧进程
    for (int i = 0; i < num_workers; i++) {
        workers[i].mark_as_old = 1;  // 标记为"待退役"
        workers[i].accepting = 0;     // 停止接受新请求
    }
    
    // 步骤 2: 重新加载代码（Master 进程中）
    reload_application_code();
    
    // 步骤 3: 启动新 Worker
    for (int i = 0; i < num_workers; i++) {
        pid_t new_pid = fork();
        
        if (new_pid == 0) {
            // 子进程：新 Worker
            // 重新加载 Python 应用
            load_python_application();
            
            // 开始接受请求
            worker_loop();
            exit(0);
        } else {
            // Master 进程
            new_workers[i].pid = new_pid;
            new_workers[i].accepting = 1;  // 新进程立即接受请求
        }
    }
}

```

此时状态：


```bash
Master Process (PID: 1000)

旧 Workers (正在停止):
├── Worker 1 (PID: 1001) [OLD] - 继续处理当前请求，不接受新请求
├── Worker 2 (PID: 1002) [OLD] - 不接受新请求
├── Worker 3 (PID: 1003) [OLD] - 继续处理当前请求，不接受新请求
└── Worker 4 (PID: 1004) [OLD] - 不接受新请求

新 Workers (已启动):
├── Worker 1' (PID: 2001) [NEW] - 接受新请求 ✓
├── Worker 2' (PID: 2002) [NEW] - 接受新请求 ✓
├── Worker 3' (PID: 2003) [NEW] - 接受新请求 ✓
└── Worker 4' (PID: 2004) [NEW] - 接受新请求 ✓

监听 Socket: /tmp/uwsgi.sock (新旧进程都可以 accept)


```


4， Socket 继承机制（核心技术）

关键点：Socket 文件描述符通过 fork() 继承给子进程！

```bash
// Master 进程启动时创建 Socket
int listen_fd;

void master_init() {
    // 创建监听 Socket
    listen_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    bind(listen_fd, "/tmp/uwsgi.sock", ...);
    listen(listen_fd, 100);  // backlog = 100
    
    // 设置为非阻塞
    fcntl(listen_fd, F_SETFL, O_NONBLOCK);
}

// Worker 进程的事件循环
void worker_loop() {
    while (1) {
        if (!accepting) {
            // 旧 Worker：不再调用 accept()
            sleep(1);
            if (active_requests == 0) {
                exit(0);  // 没有活跃请求了，退出
            }
            continue;
        }
        
        // 新 Worker：正常接受连接
        // 多个进程同时 accept 同一个 Socket（惊群效应由内核处理）
        int client_fd = accept(listen_fd, ...);
        
        if (client_fd > 0) {
            active_requests++;
            handle_request(client_fd);
            active_requests--;
            close(client_fd);
        }
    }
}

```


5, 请求分配机制

Linux 内核的 SO_REUSEPORT 或传统的 accept 锁机制：


```bash
// 方式 1: SO_REUSEPORT (现代 Linux)
void master_init() {
    int reuse = 1;
    setsockopt(listen_fd, SOL_SOCKET, SO_REUSEPORT, &reuse, sizeof(reuse));
    // 每个 Worker 的 accept 会被内核负载均衡
}

// 方式 2: accept 锁 (传统方式)
pthread_mutex_t accept_mutex;

void worker_loop() {
    while (1) {
        // 竞争锁
        pthread_mutex_lock(&accept_mutex);
        int client_fd = accept(listen_fd, ...);
        pthread_mutex_unlock(&accept_mutex);
        
        if (client_fd > 0) {
            handle_request(client_fd);
        }
    }
}

```


6, 旧进程优雅退出


```bash
// 旧 Worker 的退出逻辑
void old_worker_shutdown() {
    // 1. 停止接受新请求
    accepting = 0;
    
    // 2. 设置超时时间（防止挂起的请求）
    alarm(60);  // 60 秒后强制退出
    
    // 3. 等待当前请求完成
    while (active_requests > 0) {
        // 继续处理已接受的请求
        if (current_request) {
            continue_processing(current_request);
        }
        usleep(100000);  // 100ms
    }
    
    // 4. 清理资源
    cleanup_python_interpreter();
    close_database_connections();
    
    // 5. 退出
    exit(0);
}

// Master 监控旧进程
void monitor_old_workers() {
    for (int i = 0; i < num_workers; i++) {
        if (workers[i].mark_as_old) {
            time_t now = time(NULL);
            
            // 超过 60 秒还没退出，强制杀死
            if (now - workers[i].shutdown_start > 60) {
                kill(workers[i].pid, SIGKILL);
                fprintf(stderr, "Force killed worker %d\n", workers[i].pid);
            }
            
            // 检查进程是否已退出
            int status;
            pid_t result = waitpid(workers[i].pid, &status, WNOHANG);
            if (result > 0) {
                fprintf(stderr, "Old worker %d exited gracefully\n", workers[i].pid);
                workers[i].mark_as_old = 0;
            }
        }
    }
}
```

时间线演示

```bash
时间 | 事件
-----|-----------------------------------------------------
T0   | Master 收到 SIGHUP 信号
     | 旧 Workers: [1001✓, 1002✓, 1003✓, 1004✓] 接受请求
     |
T1   | 创建新 Workers [2001, 2002, 2003, 2004]
     | 旧 Workers: [1001(req1), 1002, 1003(req2), 1004] 停止接受新请求
     | 新 Workers: [2001✓, 2002✓, 2003✓, 2004✓] 开始接受请求
     |
T2   | 新请求 → 由新 Workers 处理
     | 旧 Workers: 
     |   - 1001 还在处理 req1...
     |   - 1002 空闲，退出 ✓
     |   - 1003 还在处理 req2...
     |   - 1004 空闲，退出 ✓
     |
T3   | req1 完成，Worker 1001 退出 ✓
     | req2 完成，Worker 1003 退出 ✓
     |
T4   | 所有旧 Workers 已退出
     | 只剩新 Workers: [2001✓, 2002✓, 2003✓, 2004✓]
     | 重启完成！

```


总结

平滑重启不丢请求的核心机制：

- Socket 继承：新旧进程共享同一个监听 Socket
- 双进程并存：新进程启动后，旧进程才停止接受新请求
- 优雅退出：旧进程等待活跃请求完成
- 内核缓冲：Socket backlog 保证短暂的连接队列,listen(listen_fd, 100), backlog = 100, 即使所有 Worker 都忙，新连接也会在内核队列中等待, 不会被拒绝，直到队列满
- 超时保护：防止挂起的请求阻塞重启

这个设计让 uWSGI 可以在生产环境中实现零停机部署，非常优雅。



#### 如何避免多个子进程(多个Worker)同时处理同一个请求（惊群问题）

问题场景

```bash
// 多个 Worker 同时监听同一个 Socket
Master Process (listen_fd = 3)
├── Worker 1: accept(fd=3)  ← 都在等待
├── Worker 2: accept(fd=3)  ← 都在等待
├── Worker 3: accept(fd=3)  ← 都在等待
└── Worker 4: accept(fd=3)  ← 都在等待

// 当一个新连接到来时，会发生什么？

```


历史问题：惊群效应 (Thundering Herd)


老版本 Linux (2.6 之前)


```bash
// 所有进程在 accept() 上阻塞
Worker 1: accept(listen_fd) → 阻塞中...
Worker 2: accept(listen_fd) → 阻塞中...
Worker 3: accept(listen_fd) → 阻塞中...
Worker 4: accept(listen_fd) → 阻塞中...

// 新连接到达
[新连接来了！]

// 内核唤醒所有进程！（惊群）
Worker 1: 被唤醒，尝试 accept() → 成功获得连接 ✓
Worker 2: 被唤醒，尝试 accept() → 返回 EAGAIN ✗
Worker 3: 被唤醒，尝试 accept() → 返回 EAGAIN ✗
Worker 4: 被唤醒，尝试 accept() → 返回 EAGAIN ✗

// 问题：3 个进程被无谓唤醒，浪费 CPU

```


现代解决方案

方案 1: 内核级解决 (Linux 2.6+)

Linux accept() 的原子性保证

```bash
// 现代 Linux 内核已经解决了 accept 惊群
// 只会唤醒一个进程

// 内核实现伪代码
int sys_accept(int sockfd) {
    // 1. 获取 socket 的等待队列
    wait_queue_head_t *wq = &sock->wq;
    
    // 2. 只唤醒一个等待的进程 (exclusive wake)
    wake_up_exclusive(wq);  // 关键：exclusive
    
    // 3. 被唤醒的进程获取连接
    return new_connection;
}

// Worker 进程的 accept 调用
void worker_loop() {
    while (1) {
        // 多个进程可以同时调用，但只有一个会成功
        int client_fd = accept(listen_fd, NULL, NULL);
        
        if (client_fd > 0) {
            handle_request(client_fd);
            close(client_fd);
        }
    }
}

```

方案 2: SO_REUSEPORT (Linux 3.9+)

更高级的负载均衡

```bash
// 每个 Worker 创建自己的 Socket，但绑定到同一个端口
void worker_process() {
    // 每个 Worker 独立创建 Socket
    int listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    // 关键：设置 SO_REUSEPORT
    int reuse = 1;
    setsockopt(listen_fd, SOL_SOCKET, SO_REUSEPORT, &reuse, sizeof(reuse));
    
    // 多个进程可以绑定到同一个端口
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };
    bind(listen_fd, (struct sockaddr*)&addr, sizeof(addr));
    listen(listen_fd, 128);
    
    // 各自 accept，内核自动负载均衡
    while (1) {
        int client = accept(listen_fd, NULL, NULL);
        handle_request(client);
        close(client);
    }
}

// Master 启动多个 Worker
int main() {
    for (int i = 0; i < 4; i++) {
        if (fork() == 0) {
            worker_process();
            exit(0);
        }
    }
    wait(NULL);
}

```


内核如何分配连接？

```bash
// Linux 内核实现（简化）
// net/ipv4/inet_hashtables.c

struct sock *inet_lookup_listener(struct net *net, ...) {
    struct sock *sk;
    struct hlist_head *head;
    
    // 1. 查找监听该端口的所有 Socket
    head = &hashinfo->listening_hash[hash];
    
    // 2. 使用哈希算法选择一个 Socket (负载均衡)
    // 基于源 IP、源端口的哈希
    unsigned int hash = jhash_3words(saddr, sport, daddr);
    sk = choose_socket_from_hash(head, hash);
    
    return sk;
}

// 结果：连接被均匀分配到不同 Worker
// Worker 1: 处理连接 1, 5, 9, 13...
// Worker 2: 处理连接 2, 6, 10, 14...
// Worker 3: 处理连接 3, 7, 11, 15...
// Worker 4: 处理连接 4, 8, 12, 16...

```


方案 3: Accept 互斥锁 (uWSGI 传统模式)

用户态加锁控制


```bash
// uWSGI 的锁实现
struct uwsgi_lock {
    pthread_mutex_t lock;
    // 或者用文件锁、信号量等
};

struct uwsgi_lock accept_lock;

void worker_init() {
    // 初始化共享锁（在 Master 进程中创建，fork 后共享）
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_setpshared(&attr, PTHREAD_PROCESS_SHARED);
    pthread_mutex_init(&accept_lock.lock, &attr);
}

void worker_loop() {
    while (1) {
        // 1. 竞争锁
        pthread_mutex_lock(&accept_lock.lock);
        
        // 2. 只有获得锁的进程可以 accept
        int client_fd = accept(listen_fd, NULL, NULL);
        
        // 3. 立即释放锁，让其他进程可以 accept
        pthread_mutex_unlock(&accept_lock.lock);
        
        // 4. 处理请求（不持有锁）
        if (client_fd > 0) {
            handle_request(client_fd);
            close(client_fd);
        }
    }
}

```

方案 4: epoll + EPOLLEXCLUSIVE (Linux 4.5+)

事件驱动模式

```bash
// 使用 epoll 监听同一个 listen_fd
void worker_loop() {
    int epfd = epoll_create1(0);
    
    struct epoll_event ev;
    ev.events = EPOLLIN | EPOLLEXCLUSIVE;  // 关键：EPOLLEXCLUSIVE
    ev.data.fd = listen_fd;
    epoll_ctl(epfd, EPOLL_CTL_ADD, listen_fd, &ev);
    
    struct epoll_event events[10];
    while (1) {
        // 只有一个 Worker 会被唤醒
        int n = epoll_wait(epfd, events, 10, -1);
        
        for (int i = 0; i < n; i++) {
            if (events[i].data.fd == listen_fd) {
                // 可以安全 accept
                int client = accept(listen_fd, NULL, NULL);
                handle_request(client);
                close(client);
            }
        }
    }
}


```


uWSGI 实际实现

```bash
// uwsgi.c (简化)

void uwsgi_accept_loop() {
    // 检测内核特性
    #ifdef SO_REUSEPORT
        if (uwsgi.reuse_port) {
            // 使用 SO_REUSEPORT 模式
            setup_reuseport_socket();
            simple_accept_loop();
            return;
        }
    #endif
    
    #ifdef EPOLLEXCLUSIVE
        if (kernel_version >= KERNEL_VERSION(4, 5, 0)) {
            // 使用 epoll exclusive 模式
            epoll_exclusive_loop();
            return;
        }
    #endif
    
    // 降级到加锁模式
    if (uwsgi.lock_engine) {
        locked_accept_loop();
        return;
    }
    
    // 最后：依赖内核的 accept 原子性
    simple_accept_loop();
}

// 简单 accept 模式（现代 Linux 默认）
void simple_accept_loop() {
    while (1) {
        // 直接 accept，内核保证原子性
        int client = accept(uwsgi.shared->worker_sockets[0], NULL, NULL);
        if (client < 0) continue;
        
        handle_wsgi_request(client);
        close(client);
    }
}

// 加锁模式（老系统或配置要求）
void locked_accept_loop() {
    while (1) {
        // 获取共享锁
        uwsgi_lock(uwsgi.accept_lock);
        
        // accept 连接
        int client = accept(uwsgi.shared->worker_sockets[0], NULL, NULL);
        
        // 立即释放锁
        uwsgi_unlock(uwsgi.accept_lock);
        
        if (client < 0) continue;
        
        // 处理请求（不持有锁）
        handle_wsgi_request(client);
        close(client);
    }
}

```


总结

保证请求不被重复处理的机制：

- 现代 Linux (2.6+)：内核的 accept() 已经是原子的，只唤醒一个进程

- SO_REUSEPORT：内核层面的连接分发，最优负载均衡
- 用户态锁：兼容老系统，通过互斥锁保证互斥
- EPOLLEXCLUSIVE：epoll 的独占唤醒模式

uWSGI 默认依赖内核的 accept 原子性，在现代 Linux 上完全不需要担心重复处理问题！
