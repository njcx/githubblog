Title: 常见服务端口对照表
Date: 2017-04-14 11:20 
Modified: 2017-04-14 11:20 
Category: 杂项
Tags: 端口
Slug: J10
Authors: nJcx
Summary: 常见服务端口对照表
Status: draft


```bash
计算机常用端口

HTTP:80：HTTP。

DHCP：服务器端的端口号是67

DHCP：客户机端的端口号是68

POP3：POP3仅仅是接收协议，POP3客户端使用SMTP向服务器发送邮件。POP3所用的端口号是110。

SMTP：端口号是25。SMTP真正关心的不是邮件如何被传送，而只关心邮件是否能顺利到达目的地。SMTP具有健壮的邮件处

理特性，这种特性允许邮件依据一定标准自动路由，SMTP具有当邮件地址不存在时立即通知用户的能力，并且具有在一定

时间内将不可传输的邮件返回发送方的特点。

Telnet：端口号是23。Telnet是一种最老的Internet应用，起源于ARPNET。它的名字是“电信网络协议

（Telecommunication Network Protocol）”的缩写。

FTP：FTP使用的端口有20和21。20端口用于数据传输，21端口用于控制信令的传输，控制信息和数据能够同时传输，这是

FTP的特殊这处。FTP采用的是TCP连接。

TFTP：端口号69，使用的是UDP的连接。

DNS:53，名称服务

NetBIOS:137,138,139,其中137、138是UDP端口，当通过网上邻居传输文件时用这个端口。而139端口：通过这个端口进入

的连接试图获得NetBIOS/SMB服务。这个协议被用于windows文件和打印机共享和 SAMBA。还有WINS Regisrtation也用它。

NNTP 网络新闻传输协议:119

SNMP（简单网络管理协议）:161端口

RPC（远程过程调用）服务:135端口

QQ:使用8000(服务端)和4000端口（客户端）

21 端口：21 端口主要用于FTP（File Transfer Protocol，文件传输协议）服务。

23 端口：23 端口主要用于Telnet（远程登录）服务，是Internet上普遍采用的登录和仿真程序。

25 端口：25 端口为SMTP（Simple Mail Transfer Protocol，简单邮件传输协议）服务器所开放，主要用于发送邮件，如

今绝大多数邮件服务器都使用该协议。

53 端口：53 端口为DNS（Domain Name Server，域名服务器）服务器所开放，主要用于域名解析，DNS 服务在NT 系统中

使用的最为广泛。

67、68 端口：67、68 端口分别是为Bootp 服务的Bootstrap Protocol Server（引导程序协议服务端）和Bootstrap 

Protocol Client（引导程序协议客户端）开放的端口。

69 端口：TFTP 是Cisco 公司开发的一个简单文件传输协议，类似于FTP。

79 端口：79 端口是为Finger 服务开放的，主要用于查询远程主机在线用户、操作系统类型以及是否缓冲区溢出等用户的

详细信息。

80 端口：80 端口是为HTTP（HyperText Transport Protocol，超文本传输协议）开放的，这是上网冲浪使用最多的协议

，主要用于在WWW（World Wide Web，万维网）服务上传输信息的协议。

99 端口：99 端口是用于一个名为“Metagram Relay”（亚对策延时）的服务该服务比较少见，一般是用不到的。

109、110 端口：109 端口是为POP2（Post Office Protocol Version2，邮局协议2）服务开放的，110 端口是为POP3（邮

件协议3）服务开放的，POP2、POP3 都是主要用于接收邮件的。

111 端口：111 端口是SUN 公司的RPC（Remote Procedure Call，远程过程调用）服务所开放的端口，主要用于分布式系

统中不同计算机的内部进程通信，RPC 在多种网络服务中都是很重要的组件。

113 端口：113 端口主要用于Windows 的“Authentication Service”（验证服务）。

119 端口：119 端口是为“Network News Transfer Protocol”（网络新闻组传输协议，简称NNTP）开放的。

135 端口：135 端口主要用于使用RPC（Remote Procedure Call，远程过程调用）协议并提供DCOM（分布式组件对象模型

）服务。

137 端口：137 端口主要用于“NetBIOS Name Service”（NetBIOS名称服务）。

139 端口：139 端口是为“NetBIOS Session Service”提供的，主要用于提供Windows 文件和打印机共享以及Unix 中的

Samba 服务。

143 端口：143 端口主要是用于“Internet Message Access Protocol”v2（Internet 消息访问协议，简称IMAP）。

161 端口：161 端口是用于“Simple Network Management Protocol”（简单网络管理协议，简称SNMP）。

443 端口：443 端口即网页浏览端口，主要是用于HTTPS 服务，是提供加密和通过安全端口传输的另一种HTTP。

554 端口：554 端口默认情况下用于“Real Time Streaming Protocol”（实时流协议，简称RTSP）。

1024 端口：1024 端口一般不固定分配给某个服务，在英文中的解释是“Reserved”（保留）。

1080 端口：1080 端口是Socks 代理服务使用的端口，大家平时上网使用的WWW 服务使用的是HTTP 协议的代理服务。

1755 端口：1755 端口默认情况下用于“Microsoft Media Server”（微软媒体服务器，简称MMS）。

1433 端口： SQL Server 数据库

1521 端口： Oracle 数据库

3306端口 ： MySQL 数据库

3389端口： 远程桌面 rdp

6379端口： Redis 端口

9092 端口： DB2

11211端口： memcached 端口

27017端口： mongodb 数据库

9200端口： ElasticSearch 数据库

5601端口： Kibana

5044端口： Logstash

大数据常见端口汇总：
Hadoop：    
    50070：HDFS WEB UI端口
    8020 ： 高可用的HDFS RPC端口
    9000 ： 非高可用的HDFS RPC端口
    8088 ： Yarn 的WEB UI 接口
    8485 ： JournalNode 的RPC端口
    8019 ： ZKFC端口
Zookeeper:
    2181 ： 客户端连接zookeeper的端口
    2888 ： zookeeper集群内通讯使用，Leader监听此端口
    3888 ： zookeeper端口 用于选举leader
Hbase:
    60010：Hbase的master的WEB UI端口
    60030：Hbase的regionServer的WEB UI 管理端口    
Hive:
    9083  :  metastore服务默认监听端口
    10000：Hive 的JDBC端口
Spark：
    7077 ： spark 的master与worker进行通讯的端口  standalone集群提交Application的端口
    8080 ： master的WEB UI端口  资源调度
    8081 ： worker的WEB UI 端口  资源调度
    4040 ： Driver的WEB UI 端口  任务调度
    18080：Spark History Server的WEB UI 端口
Kafka：
    9092： Kafka集群节点之间通信的RPC端口
CDH：
    7180： Cloudera Manager WebUI端口
    7182： Cloudera Manager Server 与 Agent 通讯端口
HUE：
    8888： Hue WebUI 端口




以下为搜索到的可用端口详细对应表
TCP端口（静态端口）
TCP 0= Reserved
TCP 1=TCP Port Service Multiplexer
TCP 2=Death
TCP 5=Remote Job Entry,yoyo
TCP 7=Echo
TCP 11=Skun
TCP 12=Bomber
TCP 16=Skun
TCP 17=Skun
TCP 18=消息传输协议，skun
TCP 19=Skun
TCP 20=FTP Data,Amanda
TCP 21=文件传输,Back Construction,Blade Runner,Doly Trojan,Fore,FTP trojan,Invisible FTP,Larva,WebEx,WinCrash
TCP 22=远程登录协议
TCP 23=远程登录（Telnet),Tiny Telnet Server (= TTS)
TCP 25=电子邮件(SMTP),Ajan,Antigen,Email Password Sender,Happy 99,Kuang2,ProMail trojan,Shtrilitz,Stealth,Tapiras,Terminator,WinPC,WinSpy,Haebu Coceda
TCP 27=Assasin
TCP 28=Amanda
TCP 29=MSG ICP
TCP 30=Agent 40421
TCP 31=Agent 31,Hackers Paradise,Masters Paradise,Agent 40421
TCP 37=Time,ADM worm
TCP 39=SubSARI
TCP 41=DeepThroat,Foreplay
TCP 42=Host Name Server
TCP 43=WHOIS
TCP 44=Arctic
TCP 48=DRAT
TCP 49=主机登录协议
TCP 50=DRAT
TCP 51=IMP Logical Address Maintenance,Fuck Lamers Backdoor
TCP 52=MuSka52,Skun
TCP 53=DNS,Bonk (DOS Exploit)
TCP 54=MuSka52
TCP 58=DMSetup
TCP 59=DMSetup
TCP 63=whois++
TCP 64=Communications Integrator
TCP 65=TACACS-Database Service
TCP 66=Oracle SQL*NET,AL-Bareki
TCP 67=Bootstrap Protocol Server
TCP 68=Bootstrap Protocol Client
TCP 69=TFTP,W32.Evala.Worm,BackGate Kit,Nimda,Pasana,Storm,Storm worm,Theef,Worm.Cycle.a
TCP 70=Gopher服务，ADM worm
TCP 79=用户查询（Finger),Firehotcker,ADM worm
TCP 80=超文本服务器（Http),Executor,RingZero
TCP 81=Chubo,Worm.Bbeagle.q
TCP 82=Netsky-Z
TCP 88=Kerberos krb5服务
TCP 99=Hidden Port
TCP 102=消息传输代理
TCP 108=SNA网关访问服务器
TCP 109=Pop2
TCP 110=电子邮件（Pop3),ProMail
TCP 113=Kazimas,Auther Idnet
TCP 115=简单文件传输协议
TCP 118=SQL Services,Infector 1.4.2
TCP 119=新闻组传输协议（Newsgroup(Nntp)),Happy 99
TCP 121=JammerKiller,Bo jammerkillah
TCP 123=网络时间协议(NTP),Net Controller
TCP 129=Password Generator Protocol
TCP 133=Infector 1.x
TCP 135=微软DCE RPC end-point mapper服务
TCP 137=微软Netbios Name服务（网上邻居传输文件使用）
TCP 138=微软Netbios Name服务（网上邻居传输文件使用）
TCP 139=微软Netbios Name服务（用于文件及打印机共享）
TCP 142=NetTaxi
TCP 143=Internet 邮件访问协议版本 4（IMAP4)
TCP 146=FC Infector,Infector
TCP 150=NetBIOS Session Service
TCP 156=SQL服务器
TCP 161=Snmp
TCP 162=Snmp-Trap
TCP 170=A-Trojan
TCP 177=X Display管理控制协议
TCP 179=Border网关协议（BGP)
TCP 190=网关访问控制协议（GACP)
TCP 194=Irc
TCP 197=目录定位服务（DLS)
TCP 220=Internet 邮件访问协议版本 3（IMAP3)
TCP 256=Nirvana
TCP 315=The Invasor
TCP 371=ClearCase版本管理软件
TCP 389=Lightweight Directory Access Protocol (LDAP)
TCP 396=Novell Netware over IP
TCP 420=Breach
TCP 421=TCP Wrappers
TCP 443=安全服务（HTTPS）
TCP 444=Simple Network Paging Protocol(SNPP)
TCP 445=Microsoft-DS
TCP 455=Fatal Connections
TCP 456=Hackers paradise,FuseSpark
TCP 458=苹果公司QuickTime
TCP 513=Grlogin
TCP 514=RPC Backdoor
UDP 520=Rip
TCP 531=Rasmin,Net666
TCP 544=kerberos kshell
TCP 546=DHCP Client
TCP 547=DHCP Server
TCP 548=Macintosh文件服务
TCP 555=Ini-Killer,Phase Zero,Stealth Spy
TCP 569=MSN
TCP 605=SecretService
TCP 606=Noknok8
TCP 660=DeepThroat
TCP 661=Noknok8
TCP 666=Attack FTP,Satanz Backdoor,Back Construction,Dark Connection Inside 1.2
TCP 667=Noknok7.2
TCP 668=Noknok6
TCP 669=DP trojan
TCP 692=GayOL
TCP 707=Welchia,nachi
TCP 777=AIM Spy
TCP 808=RemoteControl,WinHole
TCP 815=Everyone Darling
TCP 901=Backdoor.Devil
TCP 911=Dark Shadow
TCP 990=ssl加密
TCP 993=IMAP
TCP 999=DeepThroat
TCP 1000=Der Spaeher
TCP 1001=Silencer,WebEx,Der Spaeher
TCP 1003=BackDoor
TCP 1010=Doly
TCP 1011=Doly
TCP 1012=Doly
TCP 1015=Doly
TCP 1016=Doly
TCP 1020=Vampire
TCP 1023=Worm.Sasser.e
TCP端口（动态端口）
TCP 1024=NetSpy.698(YAI)
TCP 1025=NetSpy.698,Unused Windows Services Block
TCP 1026=Unused Windows Services Block
TCP 1027=Unused Windows Services Block
TCP 1028=Unused Windows Services Block
TCP 1029=Unused Windows Services Block
TCP 1030=Unused Windows Services Block
TCP 1033=Netspy
TCP 1035=Multidropper
TCP 1042=Bla
TCP 1045=Rasmin
TCP 1047=GateCrasher
TCP 1050=MiniCommand
TCP 1059=nimreg
TCP 1069=Backdoor.TheefServer.202
TCP 1070=Voice,Psyber Stream Server,Streaming Audio Trojan
TCP 1080=Wingate,Worm.BugBear.B,Worm.Novarg.B
TCP 1090=Xtreme,VDOLive
TCP 1092=LoveGate
TCP 1095=Rat
TCP 1097=Rat
TCP 1098=Rat
TCP 1099=Rat
TCP 1110=nfsd-keepalive
TCP 1111=Backdoor.AIMVision
TCP 1155=Network File Access
TCP 1170=Psyber Stream Server,Streaming Audio trojan,Voice
TCP 1200=NoBackO
TCP 1201=NoBackO
TCP 1207=Softwar
TCP 1212=Nirvana,Visul Killer
TCP 1234=Ultors
TCP 1243=BackDoor-G,SubSeven,SubSeven Apocalypse
TCP 1245=VooDoo Doll
TCP 1269=Mavericks Matrix
TCP 1313=Nirvana
TCP 1349=BioNet
TCP 1433=Microsoft SQL服务
TCP 1441=Remote Storm
TCP 1492=FTP99CMP(BackOriffice.FTP)
TCP 1503=NetMeeting T.120
TCP 1509=Psyber Streaming Server
TCP 1600=Shivka-Burka
TCP 1688=Key Management Service(密钥管理服务)
TCP 1703=Exloiter 1.1
TCP 1720=NetMeeting H.233 call Setup
TCP 1723=VPN 网关（PPTP）
TCP 1731=NetMeeting音频调用控制
TCP 1807=SpySender
TCP 1966=Fake FTP 2000
TCP 1976=Custom port
TCP 1981=Shockrave
TCP 1990=stun-p1 cisco STUN Priority 1 port
TCP 1990=stun-p1 cisco STUN Priority 1 port
TCP 1991=stun-p2 cisco STUN Priority 2 port
TCP 1992=stun-p3 cisco STUN Priority 3 port,ipsendmsg IPsendmsg
TCP 1993=snmp-tcp-port cisco SNMP TCP port
TCP 1994=stun-port cisco serial tunnel port
TCP 1995=perf-port cisco perf port
TCP 1996=tr-rsrb-port cisco Remote SRB port
TCP 1997=gdp-port cisco Gateway Discovery Protocol
TCP 1998=x25-svc-port cisco X.25 service (XOT)
TCP 1999=BackDoor,TransScout
TCP 2000=Der Spaeher,INsane Network
TCP 2002=W32. Beagle .AX @mm
TCP 2001=Transmisson scout
TCP 2002=Transmisson scout
TCP 2003=Transmisson scout
TCP 2004=Transmisson scout
TCP 2005=TTransmisson scout
TCP 2011=cypress
TCP 2015=raid-cs
TCP 2023=Ripper,Pass Ripper,Hack City Ripper Pro
TCP 2049=NFS
TCP 2115=Bugs
TCP 2121=Nirvana
TCP 2140=Deep Throat,The Invasor
TCP 2155=Nirvana
TCP 2208=RuX
TCP 2255=Illusion Mailer
TCP 2283=HVL Rat5
TCP 2300=PC Explorer
TCP 2311=Studio54
TCP 2556=Worm.Bbeagle.q
TCP 2565=Striker
TCP 2583=WinCrash
TCP 2600=Digital RootBeer
TCP 2716=Prayer Trojan
TCP 2745=Worm.BBeagle.k
TCP 2773=Backdoor,SubSeven
TCP 2774=SubSeven2.1&2.2
TCP 2801=Phineas Phucker
TCP 2989=Rat
TCP 3024=WinCrash trojan
TCP 3127=Worm.Novarg
TCP 3128=RingZero,Worm.Novarg.B
TCP 3129=Masters Paradise
TCP 3150=Deep Throat,The Invasor
TCP 3198=Worm.Novarg
TCP 3210=SchoolBus
TCP 3332=Worm.Cycle.a
TCP 3333=Prosiak
TCP 3389=超级终端（远程桌面）
TCP 3456=Terror
TCP 3459=Eclipse 2000
TCP 3700=Portal of Doom
TCP 3791=Eclypse
TCP 3801=Eclypse
TCP 3996=Portal of Doom,RemoteAnything
TCP 4000=腾讯QQ客户端
TCP 4060=Portal of Doom,RemoteAnything
TCP 4092=WinCrash
TCP 4242=VHM
TCP 4267=SubSeven2.1&2.2
TCP 4321=BoBo
TCP 4444=Prosiak,Swift remote
TCP 4500=W32.HLLW.Tufas
TCP 4567=File Nail
TCP 4590=ICQTrojan
TCP 4899=Remote Administrator服务器
TCP 4950=ICQTrojan
TCP 5000=WindowsXP服务器，Blazer 5,Bubbel,Back Door Setup,Sockets de Troie
TCP 5001=Back Door Setup,Sockets de Troie
TCP 5002=cd00r,Shaft
TCP 5011=One of the Last Trojans (OOTLT)
TCP 5025=WM Remote KeyLogger
TCP 5031=Firehotcker,Metropolitan,NetMetro
TCP 5032=Metropolitan
TCP 5190=ICQ Query
TCP 5321=Firehotcker
TCP 5333=Backage Trojan Box 3
TCP 5343=WCrat
TCP 5400=Blade Runner,BackConstruction1.2
TCP 5401=Blade Runner,Back Construction
TCP 5402=Blade Runner,Back Construction
TCP 5471=WinCrash
TCP 5512=Illusion Mailer
TCP 5521=Illusion Mailer
TCP 5550=Xtcp,INsane Network
TCP 5554=Worm.Sasser
TCP 5555=ServeMe
TCP 5556=BO Facil
TCP 5557=BO Facil
TCP 5569=Robo-Hack
TCP 5598=BackDoor 2.03
TCP 5631=PCAnyWhere data
TCP 5632=PCAnyWhere
TCP 5637=PC Crasher
TCP 5638=PC Crasher
TCP 5698=BackDoor
TCP 5714=Wincrash3
TCP 5741=WinCrash3
TCP 5742=WinCrash
TCP 5760=Portmap Remote Root Linux Exploit
TCP 5880=Y3K RAT
TCP 5881=Y3K RAT
TCP 5882=Y3K RAT
TCP 5888=Y3K RAT
TCP 5889=Y3K RAT
TCP 5900=WinVnc
TCP 6000=Backdoor.AB
TCP 6006=Noknok8
TCP 6129=Dameware Nt Utilities服务器
TCP 6272=SecretService
TCP 6267=广外女生
TCP 6400=Backdoor.AB,The Thing
TCP 6500=Devil 1.03
TCP 6661=Teman
TCP 6666=TCPshell.c
TCP 6667=NT Remote Control,Wise 播放器接收端口
TCP 6668=Wise Video广播端口
TCP 6669=Vampyre
TCP 6670=DeepThroat,iPhone
TCP 6671=Deep Throat 3.0
TCP 6711=SubSeven
TCP 6712=SubSeven1.x
TCP 6713=SubSeven
TCP 6723=Mstream
TCP 6767=NT Remote Control
TCP 6771=DeepThroat
TCP 6776=BackDoor-G,SubSeven,2000 Cracks
TCP 6777=Worm.BBeagle
TCP 6789=Doly Trojan
TCP 6838=Mstream
TCP 6883=DeltaSource
TCP 6912=Shit Heep
TCP 6939=Indoctrination
TCP 6969=GateCrasher,Priority,IRC 3
TCP 6970=RealAudio,GateCrasher
TCP 7000=Remote Grab,NetMonitor,SubSeven1.x
TCP 7001=Freak88
TCP 7201=NetMonitor
TCP 7215=BackDoor-G,SubSeven
TCP 7001=Freak88,Freak2k
TCP 7300=NetMonitor
TCP 7301=NetMonitor
TCP 7306=NetMonitor,NetSpy 1.0
TCP 7307=NetMonitor,ProcSpy
TCP 7308=NetMonitor,X Spy
TCP 7323=Sygate服务器端
TCP 7424=Host Control
TCP 7511=聪明基因
TCP 7597=Qaz
TCP 7609=Snid X2
TCP 7626=冰河
TCP 7777=The Thing
TCP 7789=Back Door Setup,ICQKiller
TCP 7983=Mstream
TCP 8000=腾讯OICQ服务器端，XDMA
TCP 8010=Wingate,Logfile
TCP 8011=WAY2.4
TCP 8080=WWW 代理，Ring Zero,Chubo,Worm.Novarg.B
TCP 8102=网络神偷
TCP
8181=W32.Erkez.D@mm
TCP 8520=W32.Socay.Worm
TCP 8594=I-Worm/Bozori.a
TCP 8787=BackOfrice 2000
TCP 8888=Winvnc
TCP 8897=Hack Office,Armageddon
TCP 8989=Recon
TCP 9000=Netministrator
TCP 9325=Mstream
TCP 9400=InCommand 1.0
TCP 9401=InCommand 1.0
TCP 9402=InCommand 1.0
TCP 9872=Portal of Doom
TCP 9873=Portal of Doom
TCP 9874=Portal of Doom
TCP 9875=Portal of Doom
TCP 9876=Cyber Attacker
TCP 9878=TransScout
TCP 9989=Ini-Killer
TCP 9898=Worm.Win32.Dabber.a
TCP 9999=Prayer Trojan
TCP 10067=Portal of Doom
TCP 10080=Worm.Novarg.B
TCP 10084=Syphillis
TCP 10085=Syphillis
TCP 10086=Syphillis
TCP 10101=BrainSpy
TCP 10167=Portal Of Doom
TCP 10168=Worm.Supnot.78858.c,Worm.LovGate.T
TCP 10520=Acid Shivers
TCP 10607=Coma trojan
TCP 10666=Ambush
TCP 11000=Senna Spy
TCP 11050=Host Control
TCP 11051=Host Control
TCP 11223=Progenic,Hack ’99KeyLogger
TCP 11831=TROJ_LATINUS.SVR
TCP 12076=Gjamer,MSH.104b
TCP 12223=Hack’99 KeyLogger
TCP 12345=GabanBus,NetBus 1.6/1.7,Pie Bill Gates,X-bill
TCP 12346=GabanBus,NetBus 1.6/1.7,X-bill
TCP 12349=BioNet
TCP 12361=Whack-a-mole
TCP 12362=Whack-a-mole
TCP 12363=Whack-a-mole
TCP12378=W32/Gibe@MM
TCP 12456=NetBus
TCP 12623=DUN Control
TCP 12624=Buttman
TCP 12631=WhackJob,WhackJob.NB1.7
TCP 12701=Eclipse2000
TCP 12754=Mstream
TCP 13000=Senna Spy
TCP 13010=Hacker Brazil
TCP 13013=Psychward
TCP 13223=Tribal Voice的聊天程序PowWow
TCP 13700=Kuang2 The Virus
TCP 14456=Solero
TCP 14500=PC Invader
TCP 14501=PC Invader
TCP 14502=PC Invader
TCP 14503=PC Invader
TCP 15000=NetDaemon 1.0
TCP 15092=Host Control
TCP 15104=Mstream
TCP 16484=Mosucker
TCP 16660=Stacheldraht (DDoS)
TCP 16772=ICQ Revenge
TCP 16959=Priority
TCP 16969=Priority
TCP 17027=提供广告服务的Conducent"adbot"共享软件
TCP 17166=Mosaic
TCP 17300=Kuang2 The Virus
TCP 17490=CrazyNet
TCP 17500=CrazyNet
TCP 17569=Infector 1.4.x + 1.6.x
TCP 17777=Nephron
TCP 18753=Shaft (DDoS)
TCP 19191=蓝色火焰
TCP 19864=ICQ Revenge
TCP 20000=Millennium II (GrilFriend)
TCP 20001=Millennium II (GrilFriend)
TCP 20002=AcidkoR
TCP 20034=NetBus 2 Pro
TCP 20168=Lovgate
TCP 20203=Logged,Chupacabra
TCP 20331=Bla
TCP 20432=Shaft (DDoS)
TCP 20808=Worm.LovGate.v.QQ
TCP 213 35=Tribal Flood Network,Trinoo
TCP 21544=Schwindler 1.82,GirlFriend
TCP 21554=Schwindler 1.82,GirlFriend,Exloiter 1.0.1.2
TCP 22222=Prosiak,RuXUploader2.0
TCP 22784=Backdoor.Intruzzo
TCP 23432=Asylum 0.1.3
TCP 23444=网络公牛
TCP 23456=Evil FTP,Ugly FTP,WhackJob
TCP 23476=Donald Dick
TCP 23477=Donald Dick
TCP 23777=INet Spy
TCP 26274=Delta
TCP 26681=Spy Voice
TCP 27374=Sub Seven 2.0+,Backdoor.Baste
TCP 27444=Tribal Flood Network,Trinoo
TCP 27665=Tribal Flood Network,Trinoo
TCP 29431=Hack Attack
TCP 29432=Hack Attack
TCP 29104=Host Control
TCP 29559=TROJ_LATINUS.SVR
TCP 29891=The Unexplained
TCP 30001=Terr0r32
TCP 30003=Death,Lamers Death
TCP 30029=AOL trojan
TCP 30100=NetSphere 1.27a,NetSphere 1.31
TCP 30101=NetSphere 1.31,NetSphere 1.27a
TCP 30102=NetSphere 1.27a,NetSphere 1.31
TCP 30103=NetSphere 1.31
TCP 30303=Sockets de Troie
TCP 30722=W32.Esbot.A
TCP 30947=Intruse
TCP 30999=Kuang2
TCP 31336=Bo Whack
TCP 31337=Baron Night,BO client,BO2,Bo Facil,BackFire,Back Orifice,DeepBO,Freak2k,NetSpy
TCP 31338=NetSpy,Back Orifice,DeepBO
TCP 31339=NetSpy DK
TCP 31554=Schwindler
TCP 31666=BOWhack
TCP 31778=Hack Attack
TCP 31785=Hack Attack
TCP 31787=Hack Attack
TCP 31789=Hack Attack
TCP 31791=Hack Attack
TCP 31792=Hack Attack
TCP 32100=PeanutBrittle
TCP 32418=Acid Battery
TCP 33333=Prosiak,Blakharaz 1.0
TCP 33577=Son Of Psychward
TCP 33777=Son Of Psychward
TCP 33911=Spirit 2001a
TCP 34324=BigGluck,TN,Tiny Telnet Server
TCP 34555=Trin00 (Windows) (DDoS)
TCP 35555=Trin00 (Windows) (DDoS)
TCP 36794=Worm.Bugbear-A
TCP 37651=YAT
TCP 40412=The Spy
TCP 40421=Agent 40421,Masters Paradise.96
TCP 40422=Masters Paradise
TCP 40423=Masters Paradise.97
TCP 40425=Masters Paradise
TCP 40426=Masters Paradise 3.x
TCP 41666=Remote Boot
TCP 43210=Schoolbus 1.6/2.0
TCP 44444=Delta Source
TCP 44445=Happypig
TCP 45576=未知代理
TCP 47252=Prosiak
TCP 47262=Delta
TCP 47878=BirdSpy2
TCP 49301=Online Keylogger
TCP 50505=Sockets de Troie
TCP 50766=Fore,Schwindler
TCP 51966=CafeIni
TCP 53001=Remote Windows Shutdown
TCP 53217=Acid Battery 2000
TCP 54283=Back Door-G,Sub7
TCP 54320=Back Orifice 2000,Sheep
TCP 54321=School Bus .69-1.11,Sheep,BO2K
TCP 57341=NetRaider
TCP 58008=BackDoor.Tron
TCP 58009=BackDoor.Tron
TCP 58339=ButtFunnel
TCP 59211=BackDoor.DuckToy
TCP 60000=Deep Throat
TCP 60068=Xzip 6000068
TCP 60411=Connection
TCP 60606=TROJ_BCKDOR.G2.A
TCP 61466=Telecommando
TCP 61603=Bunker-kill
TCP 63485=Bunker-kill
TCP 65000=Devil,DDoS
TCP 65432=Th3tr41t0r,The Traitor
TCP 65530=TROJ_WINMITE.10
TCP 65535=RC,Adore Worm/Linux
UDP端口（静态端口）
UDP 1=Sockets des Troie
UDP 9=Chargen
UDP 19=Chargen
UDP 69=Pasana
UDP 80=Penrox
UDP 371=ClearCase版本管理软件
UDP 445=公共Internet文件系统（CIFS)
UDP 500=Internet密钥交换（IP安全性 ,IKE)
UDP端口（动态端口）
UDP 1025=Maverick’s Matrix 1.2 - 2.0
UDP 1026=Remote Explorer 2000
UDP 1027=UC聊天软件，Trojan.Huigezi.e
UDP 1028=3721上网助手（用途不明，建议用户警惕！），KiLo,SubSARI
UDP 1029=SubSARI
UDP 1031=Xot
UDP 1032=Akosch4
UDP 1104=RexxRave
UDP 1111=Daodan
UDP 1116=Lurker
UDP 1122=Last 2000,Singularity
UDP 1183=Cyn,SweetHeart
UDP 1200=NoBackO
UDP 1201=NoBackO
UDP 1342=BLA trojan
UDP 1344=Ptakks
UDP 1349=BO dll
UDP 1561=MuSka52
UDP 1701=VPN网关（L2TP）
UDP 1772=NetControle
UDP 1978=Slapper
UDP 1985=Black Diver
UDP 2000=A-trojan,Fear,Force,GOTHIC Intruder,Last 2000,Real 2000
UDP 2001=Scalper
UDP 2002=Slapper
UDP 2015=raid-cs
UDP 2018=rellpack
UDP 2130=Mini BackLash
UDP 2140=Deep Throat,Foreplay,The Invasor
UDP 2222=SweetHeart,Way
UDP 2339=Voice Spy
UDP 2702=Black Diver
UDP 2989=RAT
UDP 3150=Deep Throat
UDP 3215=XHX
UDP 3333=Daodan
UDP 3801=Eclypse
UDP 3996=Remote Anything
UDP 4128=RedShad
UDP 4156=Slapper
UDP 4500=sae-urn/ (IP安全性，IKE NAT遍历）
UDP 5419=DarkSky
UDP 5503=Remote Shell Trojan
UDP 5555=Daodan
UDP 5882=Y3K RAT
UDP 5888=Y3K RAT
UDP 6112=Battle .net Game
UDP 6666=KiLo
UDP 6667=KiLo
UDP 6766=KiLo
UDP 6767=KiLo,UandMe
UDP 6838=Mstream Agent-handler
UDP 7028=未知木马
UDP 7424=Host Control
UDP 7788=Singularity
UDP 7983=MStream handler-agent
UDP 8012=Ptakks
UDP 8090=Aphex’s Remote Packet Sniffer
UDP 8127=9_119,Chonker
UDP 8488=KiLo
UDP 8489=KiLo
UDP 8787=BackOrifice 2000
UDP 8879=BackOrifice 2000
UDP 9325=MStream Agent-handler
UDP 10000=XHX
UDP 10067=Portal of Doom
UDP 10084=Syphillis
UDP 10100=Slapper
UDP 10167=Portal of Doom
UDP 10498=Mstream
UDP 10666=Ambush
UDP 11225=Cyn
UDP 12321=Protoss
UDP 12345=BlueIce 2000
UDP12378=W32/Gibe@MM
UDP 12623=ButtMan,DUN Control
UDP 15210=UDP remote shell backdoor server
UDP 15486=KiLo
UDP 16514=KiLo
UDP 16515=KiLo
UDP 18753=Shaft handler to Agent
UDP 20433=Shaft
UDP 21554=GirlFriend
UDP 22784=Backdoor.Intruzzo
UDP 23476=Donald Dick
UDP 25123=MOTD
UDP 26274=Delta Source
UDP 26374=Sub-7 2.1
UDP 26444=Trin00/TFN2K
UDP 26573=Sub-7 2.1
UDP 27184=Alvgus trojan 2000
UDP 27444=Trinoo
UDP 29589=KiLo
UDP 29891=The Unexplained
UDP 30103=NetSphere
UDP 31320=Little Witch
UDP 31335=Trin00 DoS Attack
UDP 31337=Baron Night,BO client,BO2,Bo Facil,BackFire,Back Orifice,DeepBO
UDP 31338=Back Orifice,NetSpy DK,DeepBO
UDP 31339=Little Witch
UDP 31340=Little Witch
UDP 31416=Lithium
UDP 31787=Hack aTack
UDP 31789=Hack aTack
UDP 31790=Hack aTack
UDP 31791=Hack aTack
UDP 33390=未知木马
UDP 34555=Trinoo
UDP 35555=Trinoo
UDP 43720=KiLo
UDP 44014=Iani
UDP 44767=School Bus
UDP 46666=Taskman
UDP 47262=Delta Source
UDP 47785=KiLo
UDP 49301=OnLine keyLogger
UDP 49683=Fenster
UDP 49698=KiLo
UDP 52901=Omega
UDP 54320=Back Orifice
UDP 54321=Back Orifice 2000
UDP 54341=NetRaider Trojan
UDP 61746=KiLO
UDP 61747=KiLO
UDP 61748=KiLO
UDP 65432=The Traitor

```



