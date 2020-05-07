Title: Go绑定yara静态编译无依赖恶意代码扫描工具
Date: 2018-07-24 20:20
Modified: 2018-07-24 20:20
Category: 安全
Tags: Yara
Slug: N10
Authors: nJcx
Summary:  Go绑定yara静态编译无依赖恶意代码扫描工具~

#### 安装


方法1

```bash
yum install -y glibc-static libstdc++-static  autoconf automake libtool


wget https://codeload.github.com/VirusTotal/yara/tar.gz/v3.11.0

tar -zxvf v3.11.0 
 cd yara-3.11.0/
./bootstrap.sh 
./configure --disable-shared --enable-static --without-crypto
make && make install
cp /usr/local/lib/pkgconfig/yara.pc   /usr/lib64/pkgconfig 

export YARA_SRC=~/go/src/yara-3.11.0
export CGO_CFLAGS="-I${YARA_SRC}/libyara/include"
export CGO_LDFLAGS="-L${YARA_SRC}/libyara/.libs -lyara -lm"

go get github.com/hillu/go-yara
cd go-yara/
git checkout v3.x

```

```go

package main

import (
        "github.com/hillu/go-yara"

        "errors"
        "flag"
        "log"
        "os"
        "strconv"
        "strings"
)

type rule struct{ namespace, filename string }
type rules []rule

func (r *rules) Set(arg string) error {
        if len(arg) == 0 {
                return errors.New("empty rule specification")
        }
        a := strings.SplitN(arg, ":", 2)
        switch len(a) {
        case 1:
                *r = append(*r, rule{filename: a[0]})
        case 2:
                *r = append(*r, rule{namespace: a[0], filename: a[1]})
        }
        return nil
}

func (r *rules) String() string {
        var s string
        for _, rule := range *r {
                if len(s) > 0 {
                        s += " "
                }
                if rule.namespace != "" {
                        s += rule.namespace + ":"
                }
                s += rule.filename
        }
        return s
}

func printMatches(m []yara.MatchRule, err error) {
        if err == nil {
                if len(m) > 0 {
                        for _, match := range m {
                                log.Printf("- [%s] %s ", match.Namespace, match.Rule)
                        }
                } else {
                        log.Print("no matches.")
                }
        } else {
                log.Printf("error: %s.", err)
        }
}

func main() {
        var (
                rules       rules
                processScan bool
                pids        []int
        )
        flag.BoolVar(&processScan, "processes", false, "scan processes instead of files")
        flag.Var(&rules, "rule", "add rule")
        flag.Parse()

        if len(rules) == 0 {
                log.Fatal("no rules specified")
        }

        args := flag.Args()
        if len(args) == 0 {
                log.Fatal("no files or processes specified")
        }

        if processScan {
                for _, arg := range args {
                        if pid, err := strconv.Atoi(arg); err != nil {
                                log.Fatalf("Could not parse %s ad number", arg)
                        } else {
                                pids = append(pids, pid)
                        }
                }
        }

        c, err := yara.NewCompiler()
        if err != nil {
                log.Fatalf("Failed to initialize YARA compiler: %s", err)
        }
        for _, rule := range rules {
                f, err := os.Open(rule.filename)
                if err != nil {
                        log.Fatalf("Could not open rule file %s: %s", rule.filename, err)
                }
                err = c.AddFile(f, rule.namespace)
                f.Close()
                if err != nil {
                        log.Fatalf("Could not parse rule file %s: %s", rule.filename, err)
                }
        }
        r, err := c.GetRules()
        if err != nil {
                log.Fatalf("Failed to compile rules: %s", err)
        }

        if processScan {
                for _, pid := range pids {
                        log.Printf("Scanning process %d...", pid)
                        m, err := r.ScanProc(pid, 0, 0)
                        printMatches(m, err)
                }
        } else {
                for _, filename := range args {
                        log.Printf("Scanning file %s... ", filename)
                        m, err := r.ScanFile(filename, 0, 0)
                        printMatches(m, err)
                }
        }
}

```

```bash

go build --ldflags '-extldflags "-static -lm"' test.go  

```



方法2 

```bash

https://github.com/Velocidex/go-yara

go build --ldflags '-extldflags "-static -lm"' test.go  

```