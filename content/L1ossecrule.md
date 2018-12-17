Title: ossec的rootkit_trojans.txt的理解
Date: 2017-05-27 12:21
Modified: 2017-05-27 12:21
Category: 安全
Tags: ossec
Slug: L1
Authors: nJcx
Summary: 记录一下学习ossec 心路~

#### 安装

[点这里](https://www.njcx.bid/posts/H14.html)

#### rootkit_trojans.txt内容

```bash

# Released under the same license as OSSEC.
# More details at the LICENSE file included with OSSEC or online
# at: https://github.com/ossec/ossec-hids/blob/master/LICENSE
#
# Blank lines and lines starting with '#' are ignored.
#
# Each line must be in the following format:
# file_name !string_to_search!Description
#通用可执行文件和常见的木马

# Common binaries and public trojan entries
ls          !bash|^/bin/sh|dev/[^clu]|\.tmp/lsfile|duarawkz|/prof|/security|file\.h!
env         !bash|^/bin/sh|file\.h|proc\.h|/dev/|^/bin/.*sh!
echo        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
chown       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
chmod       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
chgrp       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
cat         !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
bash        !proc\.h|/dev/[0-9]|/dev/[hijkz]!
sh          !proc\.h|/dev/[0-9]|/dev/[hijkz]!
uname       !bash|^/bin/sh|file\.h|proc\.h|^/bin/.*sh!
date        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cln]|^/bin/.*sh!
du          !w0rm|/prof|file\.h!
df          !bash|^/bin/sh|file\.h|proc\.h|/dev/[^clurdv]|^/bin/.*sh!
login       !elite|SucKIT|xlogin|vejeta|porcao|lets_log|sukasuk!
passwd      !bash|file\.h|proc\.h|/dev/ttyo|/dev/[A-Z]|/dev/[b-s,uvxz]!
mingetty    !bash|Dimensioni|pacchetto!
chfn        !bash|file\.h|proc\.h|/dev/ttyo|/dev/[A-Z]|/dev/[a-s,uvxz]!
chsh        !bash|file\.h|proc\.h|/dev/ttyo|/dev/[A-Z]|/dev/[a-s,uvxz]!
mail        !bash|file\.h|proc\.h|/dev/[^nu]!
su          !/dev/[d-s,abuvxz]|/dev/[A-D]|/dev/[F-Z]|/dev/[0-9]|satori|vejeta|conf\.inv!
sudo        !satori|vejeta|conf\.inv!
crond       !/dev/[^nt]|bash!
gpm         !bash|mingetty!
ifconfig    !bash|^/bin/sh|/dev/tux|session.null|/dev/[^cludisopt]!
diff        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^n]|^/bin/.*sh!
md5sum      !bash|^/bin/sh|file\.h|proc\.h|/dev/|^/bin/.*sh!
hdparm      !bash|/dev/ida!
ldd         !/dev/[^n]|proc\.h|libshow.so|libproc.a!

## 应急常用的工具

# Trojan entries for troubleshooting binaries
grep        !bash|givemer!
egrep       !bash|^/bin/sh|file\.h|proc\.h|/dev/|^/bin/.*sh!
find        !bash|/dev/[^tnlcs]|/prof|/home/virus|file\.h!
lsof        !/prof|/dev/[^apcmnfk]|proc\.h|bash|^/bin/sh|/dev/ttyo|/dev/ttyp!
netstat     !bash|^/bin/sh|/dev/[^aik]|/prof|grep|addr\.h!
top         !/dev/[^npi3st%]|proc\.h|/prof/!
ps          !/dev/ttyo|\.1proc|proc\.h|bash|^/bin/sh!
tcpdump     !bash|^/bin/sh|file\.h|proc\.h|/dev/[^bu]|^/bin/.*sh!
pidof       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^f]|^/bin/.*sh!
fuser       !bash|^/bin/sh|file\.h|proc\.h|/dev/[a-dtz]|^/bin/.*sh!
w           !uname -a|proc\.h|bash!

#被感染的守护进程

# Trojan entries for common daemons
sendmail    !bash|fuck!
named       !bash|blah|/dev/[0-9]|^/bin/sh!
inetd       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^un%]|^/bin/.*sh!
apachectl   !bash|^/bin/sh|file\.h|proc\.h|/dev/[^n]|^/bin/.*sh!
sshd        !check_global_passwd|panasonic|satori|vejeta|\.ark|/hash\.zk|bash|/dev[a-s]|/dev[A-Z]/!
syslogd     !bash|/usr/lib/pt07|/dev/[^cln]]|syslogs\.h|proc\.h!
xinetd      !bash|file\.h|proc\.h!
in.telnetd  !cterm100|vt350|VT100|ansi-term|bash|^/bin/sh|/dev[A-R]|/dev/[a-z]/!
in.fingerd  !bash|^/bin/sh|cterm100|/dev/!
identd      !bash|^/bin/sh|file\.h|proc\.h|/dev/[^n]|^/bin/.*sh!
init        !bash|/dev/h
tcpd        !bash|proc\.h|p1r0c4|hack|/dev/[^n]!
rlogin      !p1r0c4|r00t|bash|/dev/[^nt]!

#查杀木马

# Kill trojan
killall     !/dev/[^t%]|proc\.h|bash|tmp!
kill        !/dev/[ab,d-k,m-z]|/dev/[F-Z]|/dev/[A-D]|/dev/[0-9]|proc\.h|bash|tmp!

# rootkit 项

# Rootkit entries
/etc/rc.d/rc.sysinit    !enyelkmHIDE! enye-sec Rootkit

# ZK rootkit

# ZK rootkit (http://honeyblog.org/junkyard/reports/redhat-compromise2.pdf)
/etc/sysconfig/console/load.zk   !/bin/sh! ZK rootkit
/etc/sysconfig/console/load.zk   !usr/bin/run! ZK rootkit

# Modified /etc/hosts entries
# Idea taken from:
# http://blog.tenablesecurity.com/2006/12/detecting_compr.html
# http://www.sophos.com/security/analyses/trojbagledll.html
# http://www.f-secure.com/v-descs/fantibag_b.shtml
/etc/hosts  !^[^#]*avp.ch!Anti-virus site on the hosts file
/etc/hosts  !^[^#]*avp.ru!Anti-virus site on the hosts file
/etc/hosts  !^[^#]*awaps.net! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*ca.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*mcafee.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*microsoft.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*f-secure.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*sophos.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*symantec.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*my-etrust.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*nai.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*networkassociates.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*viruslist.ru! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*kaspersky! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*symantecliveupdate.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*grisoft.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*clamav.net! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*bitdefender.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*antivirus.com! Anti-virus site on the hosts file
/etc/hosts  !^[^#]*sans.org! Security site on the hosts file

```



#### check_rc_trojans.c

```c
/* Copyright (C) 2009 Trend Micro Inc.
 * All right reserved.
 *
 * This program is a free software; you can redistribute it
 * and/or modify it under the terms of the GNU General Public
 * License (version 2) as published by the FSF - Free Software
 * Foundation
 */

#include "shared.h"
#include "rootcheck.h"


/* Read the file pointer specified (rootkit_trojans)
 * and check if any trojan entry is in the configured files
 */
void check_rc_trojans(const char *basedir, FILE *fp)
{
    int i = 0, _errors = 0, _total = 0;
    char buf[OS_SIZE_1024 + 1];
    char file_path[OS_SIZE_1024 + 1];
    char *file;
    char *string_to_look;

#ifndef WIN32
    const char *(all_paths[]) = {"bin", "sbin", "usr/bin", "usr/sbin", NULL};
#else
    const char *(all_paths[]) = {"C:\\Windows\\", "D:\\Windows\\", NULL};
#endif

    debug1("%s: DEBUG: Starting on check_rc_trojans", ARGV0);

    while (fgets(buf, OS_SIZE_1024, fp) != NULL) {
        char *nbuf;
        char *message = NULL;

        i = 0;
        /* Remove end of line */
        nbuf = strchr(buf, '\n');
        if (nbuf) {
            *nbuf = '\0';
        }

        nbuf = normalize_string(buf);

        if (*nbuf == '\0' || *nbuf == '#') {
            continue;
        }

        /* File now may be valid */
        file = nbuf;

        string_to_look = strchr(file, '!');
        if (!string_to_look) {
            continue;
        }

        *string_to_look = '\0';
        string_to_look++;

        message = strchr(string_to_look, '!');
        if (!message) {
            continue;
        }
        *message = '\0';
        message++;

        string_to_look = normalize_string(string_to_look);
        file = normalize_string(file);
        message = normalize_string(message);

        if (*file == '\0' || *string_to_look == '\0') {
            continue;
        }

        _total++;

        /* Try with all possible paths */
        while (all_paths[i] != NULL) {
            if (*file != '/') {
                snprintf(file_path, OS_SIZE_1024, "%s/%s/%s", basedir,
                         all_paths[i],
                         file);
            } else {
                strncpy(file_path, file, OS_SIZE_1024);
                file_path[OS_SIZE_1024 - 1] = '\0';
            }

            /* Check if entry is found */
            if (is_file(file_path) && os_string(file_path, string_to_look)) {
                char op_msg[OS_SIZE_1024 + 1];
                _errors = 1;

                snprintf(op_msg, OS_SIZE_1024, "Trojaned version of file "
                         "'%s' detected. Signature used: '%s' (%s).",
                         file_path,
                         string_to_look,
                         *message == '\0' ?
                         "Generic" : message);

                notify_rk(ALERT_ROOTKIT_FOUND, op_msg);
            }

            if (*file == '/') {
                break;
            }
            i++;
        }
        continue;
    }

    if (_errors == 0) {
        char op_msg[OS_SIZE_1024 + 1];
        snprintf(op_msg, OS_SIZE_1024, "No binaries with any trojan detected. "
                 "Analyzed %d files.", _total);
        notify_rk(ALERT_OK, op_msg);
    }
}

```


```bash 

#!/bin/sh

for arg in "$*";do

ips $arg|grep -v "589a2ec0c1"|grep -v "4b74cd2dba"|grep -v "ips"|grep -v "grep"

done;exit

```

