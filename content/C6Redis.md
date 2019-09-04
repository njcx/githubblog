Title:Redis学习笔记总结(A)
Date: 2018-06-02 22:20
Modified: 2018-06-02 22:20
Category: 数据库
Tags: Redis
Slug: C6
Authors: nJcx
Summary: Redis学习笔记
Status: draft

####介绍
Redis是很火的一个Key-Value数据库,它以优异的性能得到了广泛的应用.Redis是一个内存数据库，但在磁盘数据库上是持久的，它有5种数据类型，string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)，它所有的操作都是原子类型的,可以应对复杂的生产环境,可用于多种用例，如：缓存，消息队列，应用程序中短期数据。
####安装
Redis 可以编译安装,也可以apt-get /yum安装,一般编译安装的版本比较新一些

```bash
centos/rhce : yum install redis -y

```

```bash
debian/ubuntu : sudo apt-get install redis-server -y

```

编译安装,

```bash

wget http://download.redis.io/releases/redis-3.2.9.tar.gz && tar -xzvf redis-3.2.9.tar.gz && cd redis-3.2.9

make && make PREFIX=/usr/local/redis install && mkdir /usr/local/redis/etc/

cp redis.conf /usr/local/redis/etc/ && cd /usr/local/redis/bin/ && cp redis-benchmark redis-cli redis-server /usr/bin/

```
####使用
先通过读取配置文件启动服务端,我通过apt-get 安装的,默认配置文件在 /etc/redis/redis.conf,先启动服务端

```bash

redis-server /etc/redis/redis.conf

```

再启动客服端

```bash

redis-cli

```

####命令

Redis的命令主要围绕着:配置,以及相关数据类型的操作的.

- 配置

查看配置

```bash

127.0.0.1:6379> CONFIG GET *

127.0.0.1:6379> CONFIG GET loglevel  

```

更改配置

```bash
127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE

127.0.0.1:6379> CONFIG SET loglevel "notice" 

```

- Redis 键命令

```bash

127.0.0.1:6379>　DEL key　　             // 删除key
127.0.0.1:6379> DUMP key                // 返回存储在指定键的值的序列化版本。
127.0.0.1:6379> EXISTS key              // 检查键是否存在
127.0.0.1:6379> EXPIRE key seconds         //	设置键在指定时间秒数之后到期/过期。
127.0.0.1:6379> EXPIRE key timestamp        // 设置在指定时间戳之后键到期/过期。这里的时间是Unix时间戳格式。
127.0.0.1:6379> PEXPIRE key milliseconds     // 设置键的到期时间(以毫秒为单位)。1000毫秒等于1秒
127.0.0.1:6379> PEXPIREAT key milliseconds-timestamp // 以Unix时间戳形式来设置键的到期时间(以毫秒为单位)。
127.0.0.1:6379> KEYS pattern                // 查找与指定模式匹配的所有键。
127.0.0.1:6379> MOVE key db                // 将键移动到另一个数据库
127.0.0.1:6379> PERSIST key                // 删除指定键的过期时间
127.0.0.1:6379> PTTL key                     // 获取键的剩余到期时间
127.0.0.1:6379> RANDOMKEY                  // 随机获取一个key
127.0.0.1:6379> RENAME key newkey        // 重命名一个key
127.0.0.1:6379> RENAMENX key newkey         // 如果新键不存在，重命名键
127.0.0.1:6379> TYPE key                   // 返回key的数据类型


```

- Redis 字符串命令

```bash

127.0.0.1:6379> SET key value                  // 此命令设置指定键的值。
127.0.0.1:6379> GET key                        // 得到键的值
127.0.0.1:6379> GETRANGE key start end         // 得到key 上字符串的子串(索引)
127.0.0.1:6379> GETSET key value                // 先得到旧值,再设置新值
127.0.0.1:6379> GETBIT key offset              // 返回在键处存储的字符串值中偏移处的位值
127.0.0.1:6379> MGET key[key1]                //	获取所有给定键的值
127.0.0.1:6379> SETBIT key offset value        // 存储在键上的字符串值中设置或清除偏移处的位
127.0.0.1:6379> SETEX key seconds value            // 	使用键和到期时间来设置值(同时把两个都设置了)
127.0.0.1:6379> SETNX key value                 // 设置键的值，仅当键不存在时
127.0.0.1:6379> SETRANGE key offset value       // 在指定偏移处开始的键处覆盖字符串的一部分
127.0.0.1:6379> STRLEN key                        // 获取key中值的长度
127.0.0.1:6379> MSET key value [key value …]       // 为多个key 设置 值
127.0.0.1:6379> MSETNX key value [key value …]        // 为多个键分别设置它们的值，仅当键不存在时
127.0.0.1:6379> PSETEX key milliseconds value       // 设置键的值和到期时间(以毫秒为单位)
127.0.0.1:6379> INCR key                        // 将键的整数值增加1
127.0.0.1:6379> INCRBY key  increment             //  将键的整数值按给定的数值增加
127.0.0.1:6379> INCRBYFLOAT key increment          // 将键的整数值按给定的数值增加
127.0.0.1:6379> DECR key                           //  将键的整数值减1
127.0.0.1:6379> DECRBY key decrement              //  按给定数值减少键的整数值
127.0.0.1:6379> APPEND key value                 // 	将指定值附加到键


```

- Redis 哈希命令


```bash

127.0.0.1:6379> HMGET key field1 [field2]                      // 获取所有给定哈希字段的值
127.0.0.1:6379> HMSET key field1 value1 [field2 value2 ]       // 为多个哈希字段分别设置它们的值
127.0.0.1:6379> HSET key field value                         // 设置散列字段的字符串值
127.0.0.1:6379> HSETNX key field value                         // 	仅当字段不存在时，才设置散列字段的值
127.0.0.1:6379> HLEN key                                      // 获取散列中的字段数量
127.0.0.1:6379> HKEYS key                                   // 获取哈希中的所有字段
127.0.0.1:6379> HINCRBY key field increment                  // 	将哈希字段的整数值按给定数字增加
127.0.0.1:6379> HINCRBYFLOAT key field increment               // 将哈希字段的浮点值按给定数值增加
127.0.0.1:6379> HGETALL key                                   // 获取存储在指定键的哈希中的所有字段和值
127.0.0.1:6379> HGET key field                             	// 获取存储在指定键的哈希字段的值
127.0.0.1:6379> HEXISTS key field                            // 判断是否存在散列字段
127.0.0.1:6379> HDEL key field2 [field2]                       // 删除一个或多个哈希字段
127.0.0.1:6379> HVALS key                                   // 获取哈希中的所有值

```
- Redis 列表命令

```bash

127.0.0.1:6379> BLPOP key1 [key2 ] timeout          // 删除并获取列表中的第一个元素，或阻塞，直到有一个元素可用
127.0.0.1:6379> BRPOP key1 [key2 ] timeout           // 	删除并获取列表中的最后一个元素，或阻塞，直到有一个元素可用
127.0.0.1:6379> LINDEX key index                 // 通过其索引从列表获取元素
127.0.0.1:6379> LLEN key                           //	获取列表的长度
127.0.0.1:6379> LINSERT key BEFORE/AFTER pivot value  // 在列表中的另一个元素之前或之后插入元素
127.0.0.1:6379> LPOP key                           // 删除并获取列表中的第一个元素
127.0.0.1:6379> LPUSH key value1 [value2]            //将一个或多个值添加到列表
127.0.0.1:6379> BRPOPLPUSH source destination timeout   // 从列表中弹出值，将其推送到另一个列表并返回它; 或阻塞，直到一个可用
127.0.0.1:6379> RPOP key                             // 删除并获取列表中的最后一个元素
127.0.0.1:6379> RPUSH key value1 [value2]           //将一个或多个值附加到列表
127.0.0.1:6379> RPUSHX key value                     //仅当列表存在时才将值附加到列表
127.0.0.1:6379> RPOPLPUSH source destination        // 删除列表中的最后一个元素，将其附加到另一个列表并返回
127.0.0.1:6379> LREM key count value                 // 	从列表中删除元素
127.0.0.1:6379> LSET key index value            // 通过索引在列表中设置元素的值
127.0.0.1:6379> LTRIM key start stop             // 修剪列表的指定范围
127.0.0.1:6379> LPUSHX key value                  //仅当列表存在时，才向列表添加值
127.0.0.1:6379> LRANGE key start stop          // 从列表中获取一系列元素

```


- Redis 集合命令

```bash

127.0.0.1:6379>  SADD key member1 [member2]         //将一个或多个成员添加到集合
127.0.0.1:6379>  SCARD key                           // 获取集合中的成员数
127.0.0.1:6379>  SDIFF key1 [key2]                    // 	减去多个集合
127.0.0.1:6379>  SDIFFSTORE destination key1 [key2]    // 减去多个集并将结果集存储在键中
127.0.0.1:6379>  SINTER key1 [key2]                    // 集合相交
127.0.0.1:6379>  SINTERSTORE destination key1 [key2]   // 交叉多个集合并将结果集存储在键中
127.0.0.1:6379>  SISMEMBER key member                  // 判断确定给定值是否是集合的成员
127.0.0.1:6379>  SMOVE source destination member        //将成员从一个集合移动到另一个集合
127.0.0.1:6379>  SPOP key	                            // 从集合中删除并返回随机成员
127.0.0.1:6379>  SRANDMEMBER key [count]                //	从集合中获取一个或多个随机成员
127.0.0.1:6379>  SREM key member1 [member2]             // 从集合中删除一个或多个成员
127.0.0.1:6379>  SUNION key1 [key2]                  //	添加多个集合
127.0.0.1:6379>  SUNIONSTORE destination key1 [key2]   // 添加多个集并将结果集存储在键中
127.0.0.1:6379>  SSCAN key cursor [MATCH pattern] [COUNT count]  // 	递增地迭代集合中的元素

```

- Redis 有序集合(sorted set)

```bash

127.0.0.1:6379> ZADD key score1 member1 [score2 member2]       //向有序集合添加一个或多个成员，或者更新已存在成员的分数
127.0.0.1:6379> ZCARD key                                      // 获取有序集合的成员数
127.0.0.1:6379> ZCOUNT key min max                             //计算在有序集合中指定区间分数的成员数
127.0.0.1:6379> ZINCRBY key increment member                   //有序集合中对指定成员的分数加上增量 increment
127.0.0.1:6379> ZINTERSTORE destination numkeys key [key ...]  //计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 key 中
127.0.0.1:6379> ZLEXCOUNT key min max                          //在有序集合中计算指定字典区间内成员数量
127.0.0.1:6379> ZRANGE key start stop [WITHSCORES]             //通过索引区间返回有序集合成指定区间内的成员
127.0.0.1:6379> ZRANGEBYLEX key min max [LIMIT offset count]  //通过字典区间返回有序集合的成员
127.0.0.1:6379> ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT]  //通过分数返回有序集合指定区间内的成员
127.0.0.1:6379> ZRANK key member                               // 返回有序集合中指定成员的索引
127.0.0.1:6379> ZREM key member [member ...]                  //移除有序集合中的一个或多个成员
127.0.0.1:6379> ZREMRANGEBYLEX key min max                     //移除有序集合中给定的字典区间的所有成员
127.0.0.1:6379> ZREMRANGEBYRANK key start stop                 //移除有序集合中给定的排名区间的所有成员
127.0.0.1:6379> ZREMRANGEBYSCORE key min max                  //移除有序集合中给定的分数区间的所有成员
127.0.0.1:6379> ZREVRANGE key start stop [WITHSCORES]         //返回有序集中指定区间内的成员，通过索引，分数从高到底
127.0.0.1:6379> ZREVRANGEBYSCORE key max min [WITHSCORES]     //返回有序集中指定分数区间内的成员，分数从高到低排序
127.0.0.1:6379> ZREVRANK key member                           // 返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序
127.0.0.1:6379> ZSCORE key member                               //返回有序集中，成员的分数值
127.0.0.1:6379> ZUNIONSTORE destination numkeys key [key ...]   //计算给定的一个或多个有序集的并集，并存储在新的 key 中
127.0.0.1:6379> ZSCAN key cursor [MATCH pattern] [COUNT count]   //迭代有序集合中的元素（包括元素成员和元素分值）

```

- Redis HyperLogLog

HyperLogLog 是做基数统计的算法

```bash

127.0.0.1:6379> PFADD key element [element ...]               //添加指定元素到 HyperLogLog 中。
127.0.0.1:6379> PFCOUNT key [key ...].                        //返回给定 HyperLogLog 的基数估算值。
127.0.0.1:6379> PFMERGE destkey sourcekey [sourcekey ...]     //将多个 HyperLogLog 合并为一个 HyperLogLog

```

- Redis 发布订阅

```bash


127.0.0.1:6379> PSUBSCRIBE pattern [pattern ...]               //订阅一个或多个符合给定模式的频道。
127.0.0.1:6379> PUBSUB subcommand [argument [argument ...]]    //查看订阅与发布系统状态。
127.0.0.1:6379> PUBLISH channel message                         //将信息发送到指定的频道。
127.0.0.1:6379> PUNSUBSCRIBE [pattern [pattern ...]]            //退订所有给定模式的频道。
127.0.0.1:6379> SUBSCRIBE channel [channel ...]                //订阅给定的一个或多个频道的信息。
127.0.0.1:6379> UNSUBSCRIBE [channel [channel ...]]            //指退订给定的频道。

```


- Redis 事务

```bash

127.0.0.1:6379>  DISCARD                //取消事务，放弃执行事务块内的所有命令。
127.0.0.1:6379>  EXEC                   //执行所有事务块内的命令。
127.0.0.1:6379>  MULTI                  //标记一个事务块的开始。
127.0.0.1:6379>  UNWATCH                //取消 WATCH 命令对所有 key 的监视。
127.0.0.1:6379>  WATCH key [key ...]    // 监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断

```
样例

```bash
127.0.0.1:6379> MULTI
OK

127.0.0.1:6379> SET book-name "Mastering C++ in 21 days"
QUEUED

127.0.0.1:6379> GET book-name
QUEUED

127.0.0.1:6379> SADD tag "C++" "Programming" "Mastering Series"
QUEUED

127.0.0.1:6379> SMEMBERS tag
QUEUED

127.0.0.1:6379> EXEC
1) OK
2) "Mastering C++ in 21 days"
3) (integer) 3
4) 1) "Mastering Series"
   2) "C++"
   3) "Programming"
   
```


- Redis脚本

```bash

127.0.0.1:6379>  EVAL script numkeys key [key ...] arg [arg ...]    //执行 Lua 脚本。
127.0.0.1:6379> 	EVALSHA sha1 numkeys key [key ...] arg [arg ...]   //执行 Lua 脚本。
127.0.0.1:6379> 	SCRIPT EXISTS script [script ...] 查看指定的脚本是否已经被保存在缓存当中。
127.0.0.1:6379> 	SCRIPT FLUSH 从脚本缓存中移除所有脚本。
127.0.0.1:6379> 	SCRIPT KILL 杀死当前正在运行的 Lua 脚本。
127.0.0.1:6379> 	SCRIPT LOAD script    将脚本 script 添加到脚本缓存中，但并不立即执行这个脚本。
```