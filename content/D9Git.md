Title: Git简明教程
Date: 2017-04-14 10:20
Modified: 2017-04-14 10:20
Category: 杂项
Tags: Git
Slug: D9
Authors: nJcx
Summary: Git简明教程
- 介绍

git是 Linus，也就是Linux kernel 的作者所写的分布式版本控制系统。下面介绍一下git是怎么使用的：

# 1

先安装git
```bash
sudo apt-get install git git-core

```
然后我们先设置Git的user name和email：

```bash
>git config --global user.name "nJcx"
>git config --global user.email "njcx86@gmail.com"
```
然后我们再生成Git SSH Key,一直回车就行了，然后我们打开当前用户目录下即～/.ssh/id_rsa.pub这个文件，把里面的东西添加到github、码云、coding上，就可以用了

```bash
>ssh-keygen -t rsa -C “njcx86@gmail.com”
```

我们先建个目录，并且在目录里面初始化git所需的相关文件，里面会有一个.git 的隐藏文件夹
```bash

> mkdir git 
>cd git && git init
>echo "# git_" >> README.md

```
我们在里面加了一个README.md文件

```bash

> git add .
> git commit -m "add more" 
>git remote add origin git@github.com:njcx/git_.git
>git push -u origin master

//第一步,用命令 git add 告诉Git,把文件添加到仓库
//用命令 git commit （-m 就是加注释的意思）告诉Git,把文件提交到仓库:
//第三步，添加远程仓库
//第四步，把本地文件变动提交远程仓库
```
查看本地是否有变动或者状态
```bash
>git status

```
查看差异或者修改的内容
```bash
>git diff
```
查看提交的tag

```bash

>git log

```

# 2

既然是版本控制系统，我们肯定可以回退到历史上某个文件状态，我们先用 git log 看一下有哪些历史commit tag

```bash

commit 5b42df0cfd1b5d6cdfc7d5b251ea770ca35cbec1
Author: nJcx <njcx86@gmail.com>
Date:   Thu Jun 8 18:16:57 2017 +0800

    add more

commit d171df385fb3af5b092c65bfea5011316de936d0
Author: nJcx <njcx86@gmail.com>
Date:   Thu Jun 8 17:53:49 2017 +0800

    first commit
```
就像这样,前面介绍了，在工作区里面有.git目录，这个是git版本库，我们的相关操作都会在这个目录产生记录。我们在工作区里面通过 git add xxx 把相关文件的改动提交到暂存区index,我们又通过git commit 把文件状态改动提交到默认的主分支master上，也就是说，我们会经过两个状态，一个是提交到暂存区index，另一个就是提交到分支上。

我们再创建一个README2.md 文件

```bash

> echo "# git_" >> README2.md

```
然后 git status 一下

```bash
未跟踪的文件:
  （使用 "git add <文件>..." 以包含要提交的内容）

	README2.md

提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）

```
我们先把它加入跟踪状态，

```bash

> git add README2.md && git commit -m "add file README2.MD

```
现在我们编辑它

```bash

> echo "by nJcx" >> README2.md

```
下面，我们就会存在3种状态：

- 1，就是文件在工作区被修改了，没有git add 到暂存区
- 2，文件被 git add 到暂存区了，但是没有提交到分支上
- 3，文件的修改被git commit 分支上了

第一种状态
```bash
> git checkout -- README2.md
```

第二种
```bash
> git reset HEAD README2.md
> git checkout -- README2.md
// HEAD,表示最新的版本。
```
第三种

```bash
> git reset --hard HEAD^ 
//这里也可以用 commit_id,通过git log 或者 git reflog 查看
// HEAD^表示上一个版本，上上一个版本就是 HEAD^^
```
第三种有一个缺点，如果一次commit 多个文件，回退版本的时候会把其他正常的文件也回退了，所以有的时候，我们可以把不想回退的文件单独commit一下

如果，我们回退的时候，又后悔了，又想回到某个最新的版本，那该怎么办？

```bash
> git reflog
> git reset --hard commit_id
```

# 3
讲版本控制系统就不能不讲分支，我们用 git branch 查看当前有哪些分支以及所在分支
```bash

njcx@njcx:~/桌面/git$ git branch
* master

```
我们创建一个dev 分支,并切换分支

```bash
njcx@njcx:~/桌面/git$  git checkout -b dev
njcx@njcx:~/桌面/git$  git branch
* dev
  master
//创建分支:git branch <name>
//切换分支: git checkout <name>
//创建+切换分支: git checkout ‐b <name>
//删除分支: git branch ‐d <name>
```



 
