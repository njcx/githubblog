Title: Docker 常用命令记录
Date: 2017-02-16 10:20
Modified: 2017-02-16 10:20
Category: Linux
Tags: docker
Slug: B4
Authors: nJcx
Summary: 介绍一下Docker常用命令，记录一下学习过程
Status: draft


#### 查看docker信息（version、info）

- 查看docker版本  

docker version 

- 显示docker系统的信息  

docker info  

#### 对image的操作（search、pull、images、rmi、history）

- 检索image  

docker search image_name  
  
-  下载image 

 docker pull image_name  
  
- 列出镜像列表; -a, --all=false Show all images; --no-trunc=false Don't truncate output; -q, --quiet=false Only show numeric IDs  

docker images  
  
- 删除一个或者多个镜像; -f, --force=false Force; --no-prune=false Do not delete untagged parents  

docker rmi image_name  
  
- 显示一个镜像的历史; --no-trunc=false Don't truncate output; -q, --quiet=false Only show numeric IDs  

docker history image_name 


####启动容器（run）

Docker容器可以理解为在沙盒中运行的进程。这个沙盒包含了该进程运行所必须的资源，包括文件系统、系统类库、shell 环境等等。但这个沙盒默认是不会运行任何程序的。你需要在沙盒中运行一个进程来启动某一个容器。这个进程是该容器的唯一进程，所以当该进程结束的时候，容器也会完全的停止。

- 在容器中运行"echo"命令，输出"hello word"  

docker run image_name echo "hello word"  
  
- 交互式进入容器中 
 
docker run -i -t image_name /bin/bash  
  
  
- 在容器中安装新的程序  

docker run image_name apt-get install -y app_name  

Note：  在执行apt-get 命令的时候，要带上-y参数。如果不指定-y参数的话，apt-get命令会进入交互模式，需要用户输入命令来进行确认，但在docker环境中是无法响应这种交互的。apt-get 命令执行完毕之后，容器就会停止，但对容器的改动不会丢失。

####查看容器（ps）

- 列出当前所有正在运行的container  

docker ps  

- 列出所有的container  

docker ps -a  

- 列出最近一次启动的container 

docker ps -l  

####保存对容器的修改（commit）

当你对某一个容器做了修改之后（通过在容器中运行某一个命令），可以把对容器的修改保存下来，这样下次可以从保存后的最新状态运行该容器。

- 保存对容器的修改; -a, --author="" Author; -m, --message="" Commit message  

docker commit ID new_image_name  

Note：  image相当于类，Container相当于实例，不过可以动态给实例安装新软件，然后把这个container用commit命令固化成一个image。

#### 对容器的操作（rm、stop、start、kill、logs、diff、top、cp、restart、attach）

- 删除所有容器  

docker rm `docker ps -a -q`  
  
删除单个容器; -f, --force=false; -l, --link=false Remove the specified link and not the underlying container; -v, --volumes=false Remove the volumes associated to the container 
 
docker rm Name/ID  
  
- 停止、启动、杀死一个容器  

docker stop Name/ID  

docker start Name/ID  

docker kill Name/ID  
  
- 从一个容器中取日志; -f, --follow=false Follow log output; -t, --timestamps=false Show timestamps  

docker logs Name/ID  
  
- 列出一个容器里面被改变的文件或者目录，list列表会显示出三种事件，A 增加的，D 删除的，C 被改变的  

docker diff Name/ID  
  
- 显示一个运行的容器里面的进程信息  

docker top Name/ID  
  
- 从容器里面拷贝文件/目录到本地一个路径  

docker cp Name:/container_path to_path  

docker cp ID:/container_path to_path  
  
- 重启一个正在运行的容器; -t, --time=10 Number of seconds to try to stop for before killing the container, Default=10  

docker restart Name/ID  
  
- 附加到一个运行的容器上面; --no-stdin=false Do not attach stdin; --sig-proxy=true Proxify all received signal to the process  

docker attach ID  

Note： attach命令允许你查看或者影响一个运行的容器。你可以在同一时间attach同一个容器。你也可以从一个容器中脱离出来，是从CTRL-C。

#### 保存和加载镜像（save、load）

当需要把一台机器上的镜像迁移到另一台机器的时候，需要保存镜像与加载镜像。

- 保存镜像到一个tar包; -o, --output="" Write to an file 

docker save image_name -o file_path  

- 加载一个tar包格式的镜像; -i, --input="" Read from a tar archive file  

docker load -i file_path  
  
- 机器a  

docker save image_name > /home/save.tar  

使用scp将save.tar拷到机器b上，然后：  

docker load < /home/save.tar  

#### 登录registry server（login）

登陆registry server; -e, --email="" Email; -p, --password="" Password; -u, --username="" Username  

docker login  

#### 发布image（push）

- 发布docker镜像  

docker push new_image_name  

####根据Dockerfile 构建出一个容器

- build  

      --no-cache=false Do not use cache when building the image  
      
      -q, --quiet=false Suppress the verbose output generated by the containers  
      
      --rm=true Remove intermediate containers after a successful build  
      
      -t, --tag="" Repository name (and optionally a tag) to be applied to the resulting image in case of success  

docker build -t image_name Dockerfile_path  

