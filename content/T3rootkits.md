Title: Linux Rootkit检测思路
Date: 2022-10-29 20:20
Modified: 2022-10-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T2
Authors: nJcx
Summary: linux rootkit检测思路 ~

#### 介绍
Linux rootkit 是一种特别设计用来隐藏其存在并提供未经授权的系统访问权限的恶意软件。它们对系统的危害很大，通常非常难以检测，因为它们能够修改操作系统的核心组件或关键文件，使得标准的安全检查工具无法发现它们的存在。 主要分为内核态rootkit和用户态rootkit。
无论是用户态rootkit还是内核的rootkit，都会把隐藏自己，作为核心功能存在，只是实现的方法，各有不同。本文的前置知识，建议先阅读：  https://www.njcx.bid/posts/O4.html



#### Linux 用户态 rootkit检测


Linux 用户态 rootkit 主要通过以下几种方法来实现隐藏和操控系统的行为：

- 动态链接库（LD_PRELOAD）注入：通过设置环境变量 LD_PRELOAD 来加载恶意的共享库。这种方法可以拦截并修改标准库函数的行为，例如文件操作、网络通信等，从而隐蔽地执行某些操作。
- ptrace系统调用：利用 ptrace 系统调用来跟踪或操控另一个进程。攻击者可以使用这种方法来操纵其他进程的内存或寄存器值，比如篡改程序的返回值或者隐藏特定进程。
- /etc/ld.so.preload 植入：在 /etc/ld.so.preload 文件中指定一个共享库，这样每次动态链接器加载程序时都会首先加载这个库。这使得攻击者能够在几乎所有的用户态进程中运行自己的代码。
- 替换关键系统工具和二进制文件：通过替换常用的系统命令如 ls, ps, netstat 等，使得这些命令在被执行时隐藏特定的信息，例如隐藏特定的文件、进程或网络连接。
- 劫持环境变量：改变诸如 PATH 这样的环境变量，使得命令行输入的命令指向恶意版本而非原版系统命令。


LD_PRELOAD 是 Linux 环境下的一个环境变量，它允许用户指定在执行程序之前优先加载的共享库。这种机制原本是为开发者提供了一种方式来覆盖或扩展标准库函数的功能，比如用于调试、性能监控等。然而，这一特性也可能被恶意利用，特别是通过所谓的 LD_PRELOAD rootkit 来实现未经授权的行为。LD_PRELOAD rootkit 主要通过预加载特定编写的共享库到目标进程的地址空间，从而覆盖或拦截原生系统调用。例如，可以替换文件操作相关的函数（如 open, read, readdir），以便隐藏文件、目录或进程。如果要检测LD_PRELOAD HOOK， 则关注 ld.so.preload 配置文件是不是存在与里面是不是包含so 文件路径地址，以及LD_PRELOAD 环境变量是否存在。

这段代码包含两个函数，用于检查LD_PRELOAD环境变量和配置文件。

- checkLDPreloadEnv：检查环境变量LD_PRELOAD是否设置。
- checkLDPreloadConfig：检查/etc/ld.so.preload文件和/etc/ld.so.conf.d/目录下的配置文件是否包含LD_PRELOAD。


```bash

func checkLDPreloadEnv() (bool, string) {
	ldPreload := os.Getenv("LD_PRELOAD")
	if ldPreload != "" {
		return true, ldPreload
	}
	return false, ""
}

func checkLDPreloadConfig() (bool, []string) {
	suspiciousFiles := []string{}

	// Check /etc/ld.so.preload
	if _, err := os.Stat("/etc/ld.so.preload"); err == nil {
		content, err := ioutil.ReadFile("/etc/ld.so.preload")
		if err == nil && len(content) > 0 {
			suspiciousFiles = append(suspiciousFiles, "/etc/ld.so.preload")
		}
	}

	// Check /etc/ld.so.conf.d/ directory
	files, err := filepath.Glob("/etc/ld.so.conf.d/*.conf")
	if err == nil {
		for _, file := range files {
			content, err := ioutil.ReadFile(file)
			if err == nil && strings.Contains(string(content), "LD_PRELOAD") {
				suspiciousFiles = append(suspiciousFiles, file)
			}
		}
	}

	return len(suspiciousFiles) > 0, suspiciousFiles
}

```




替换关键系统工具和二进制文件：通过替换常用的系统命令如 ls, ps, netstat 等，使得这些命令在被执行时隐藏特定的信息，例如隐藏特定的文件、进程或网络连接。 这个是一个bash 包装的ps 命令， 可以过滤掉指定进程， 只要把原ps 重命令ps1（可以是其他的字符，只要一致就行）即可。

```bash

#!/bin/bash

# Default list of processes to exclude (you can add more process names here)
EXCLUDE_PROCESSES=("sshd" "xmr" "miner")

# Parse options and arguments
PS_ARGS=()
EXCLUDE_FLAG=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --exclude)
            EXCLUDE_FLAG=true
            shift # Skip the --exclude argument
            ;;
        *)
            PS_ARGS+=("$1") # Collect all other arguments
            shift
            ;;
    esac
done

# If no arguments are passed, default to 'aux'
if [ ${#PS_ARGS[@]} -eq 0 ]; then
    PS_ARGS=("aux")
fi

# Execute the ps command and pipe its output to grep
ps1 "${PS_ARGS[@]}" | {
    if [ "$EXCLUDE_FLAG" = true ]; then
        # Build the grep exclusion pattern
        exclude_pattern=$(printf "|%s" "${EXCLUDE_PROCESSES[@]}")
        exclude_pattern=${exclude_pattern:1} # Remove the leading '|'

        # Use grep to exclude specific process names
        grep -vE "$exclude_pattern"
    else
        # Directly output the ps result
        cat
    fi
}
```


检测 ps 命令有没有被替换, 遍历proc 和 ps 执行结果对比， 代码如下 ：


```bash

func getProcProcesses(minAge time.Duration) (*ProcessMap, error) {
	procMap := NewProcessMap()
	files, err := ioutil.ReadDir("/proc")
	if err != nil {
		return nil, fmt.Errorf("error reading /proc: %v", err)
	}

	now := time.Now().Unix()

	for _, f := range files {
		if !f.IsDir() {
			continue
		}

		pid, err := strconv.Atoi(f.Name())
		if err != nil {
			continue
		}

		startTime, err := getProcessStartTime(pid)
		if err != nil {
			continue
		}

		// Skip processes running for less than minAge
		if now-startTime < int64(minAge.Seconds()) {
			continue
		}

		statusFile := filepath.Join("/proc", f.Name(), "status")
		content, err := ioutil.ReadFile(statusFile)
		if err != nil {
			continue
		}

		info := &ProcessInfo{
			PID:       pid,
			StartTime: startTime,
			CmdLine:   getCmdLine(pid),
		}

		lines := strings.Split(string(content), "\n")
		for _, line := range lines {
			switch {
			case strings.HasPrefix(line, "Name:"):
				info.Name = strings.TrimSpace(strings.TrimPrefix(line, "Name:"))
			case strings.HasPrefix(line, "PPid:"):
				info.PPID, _ = strconv.Atoi(strings.TrimSpace(strings.TrimPrefix(line, "PPid:")))
			case strings.HasPrefix(line, "Uid:"):
				uidFields := strings.Fields(strings.TrimPrefix(line, "Uid:"))
				if len(uidFields) > 0 {
					info.UID, _ = strconv.Atoi(uidFields[0])
				}
			case strings.HasPrefix(line, "State:"):
				stateParts := strings.Fields(strings.TrimPrefix(line, "State:"))
				if len(stateParts) > 0 {
					info.State = string(stateParts[0][0])
				}
			}
		}

		procMap.Add(pid, info)
	}

	return procMap, nil
}

// getPsProcesses retrieves process information from the ps command
func getPsProcesses(minAge time.Duration) (*ProcessMap, error) {
	procMap := NewProcessMap()

	// Use ps command to get more detailed information, including start time
	cmd := exec.Command("ps", "ax", "-o", "pid,ppid,uid,stat,lstart,comm")
	output, err := cmd.Output()
	if err != nil {
		return nil, fmt.Errorf("error executing ps command: %v", err)
	}

	now := time.Now()
	scanner := bufio.NewScanner(strings.NewReader(string(output)))
	scanner.Scan() // Skip header line

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		if len(fields) < 6 {
			continue
		}

		pid, err := strconv.Atoi(fields[0])
		if err != nil {
			continue
		}

		// Parse start time
		timeStr := strings.Join(fields[4:9], " ")
		startTime, err := time.Parse("Mon Jan 2 15:04:05 2006", timeStr)
		if err != nil {
			continue
		}

		// Skip processes running for less than minAge
		if now.Sub(startTime) < minAge {
			continue
		}

		ppid, _ := strconv.Atoi(fields[1])
		uid, _ := strconv.Atoi(fields[2])

		info := &ProcessInfo{
			PID:       pid,
			PPID:      ppid,
			UID:       uid,
			State:     string(fields[3][0]),
			StartTime: startTime.Unix(),
			Name:      fields[len(fields)-1],
			CmdLine:   getCmdLine(pid),
		}

		procMap.Add(pid, info)
	}

	return procMap, nil
}


```



#### Linux 内核态rootkit检测



Linux 内核态 rootkit 通过编写自定义的内核模块并将其加载到运行中的内核中，rootkit 可以获得更高的权限和更大的灵活性 。这类 rootkit 通常比用户态的更难检测和移除，因为它们在系统层次上运作，能够绕过大多数用户空间的安全机制。内核态 rootkit主要是修改内核的数据结构或者进行系统函数HOOK来实现隐藏和操控系统的行为, 那么我们就聚焦关注两个点：修改哪些数据结构， 怎么HOOK与HOOK哪些函数。
