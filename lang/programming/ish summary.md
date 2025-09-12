```
iSH Shell最近上架 App Store 。上架版本由于限制，和 TestFlight 版本有些不同。我总结了一下要点：

下载须知
在国区 App Store 需要搜索“iSH Shell”，外区搜索"iSH"即可。

获取 apk
App Store 版本默认未装 apk 。安装过程参见这个官方 wiki 页面，步骤如下：

运行cd /
运行wget -qO- http://dl-cdn.alpinelinux.org/alpine/v3.12/main/x86/apk-tools-static-2.10.5-r1.apk | tar -xz sbin/apk.static && ./sbin/apk.static add apk-tools && rm sbin/apk.static
变更默认 shell
iSH Shell 的默认 shell
iSH Shell 使用 Alpine Linux，它的默认 shell 是 busybox ash 。
ash 不会 source.bashrc，而是会 source.profile。
一般的 bash 脚本无法在这里运行，需要使用/bin/sh来运行经典 shell 脚本。这当然很不方便，我们喜欢用 bash 或者 zsh 。
以 bash 为例，运行apk add bash安装 bash，然后在 iSH terminal 输入bash使用 bash 。
使用 bash 作为默认 shell
参见这个官方 issue，有两种改变默认 shell 的方式：

编辑/etc/passwd。iSH Shell 的用户是 root，所以编辑第一行，把/bin/ash改为/bin/bash。
安装 shadow：apk add shadow，然后使用其中的 chsh 命令修改默认 shell：chsh -s bash 我个人觉得前者更加方便。把默认 shell 改成 bash 之后，再次进入 iSH Shell 就会默认 source.bashrc，方便 git pull 使用自己的 dotfiles 。
杂项
App 图标可以设置
大部分用法能在官方 wiki里面找到，比如如何使用ssh，vnc，python，ruby，php或者r，以及目前的局限是什么。
```





# git-lfs

```


https://dl-cdn.alpinelinux.org/alpine/v3.22/community/aarch64/git-lfs-3.6.0-r7.apk

https://dl-cdn.alpinelinux.org/alpine/v3.22/main/aarch64/git-2.49.1-r0.apk

试试最新的包



After more trial-and-error, I found that using v3.15's git-lfs (3.0.2-r0) can work around this issue.

vi -c "%s/v3.14/v3.15/g" -c wq /etc/apk/repositories # or edit the file manually
apk add git-lfs
git-lfs --version # now this should be done instantly
I'm closing this issue as there are workarounds.


curl -O https://github.com/git-lfs/git-lfs/releases/download/v3.5.1/git-lfs-linux-amd64-v3.5.1.tar.gz
tar -xzf git-lfs-*.tar.gz
cd git-lfs-*
./install.sh
```



# mount

```
https://ish.app

1. 挂载文件夹
mount -t ios . /mnt
会弹出文件夹选择框，选择你要挂载的目录，比如下载目录，确定后即挂载到 /mnt 目录中

2. 剪贴板操作
读取剪贴板：

cat /dev/clipboard
复制到剪贴板：

echo im3x > /dev/clipboard
提示：如果剪贴板没内容，读取会报错

最近在折腾 iPhone 上安装 code-server，目前还没成功
如果大家还有其他好玩的技巧，可以在帖子里留言讨论

 剪贴 ish clipboard dev2 条回复  •  2020-10-27 23:53:53 +08:00
im3x		    1
im3x   
OP
   2020-10-27 23:47:42 +08:00
[x] 成功跑上 sqlmap
[ ] 安装 weevely3 失败
[ ] vscode 远程连接失败
[ ] npm install -g code-server 失败，正在尝试 yarn global add code-server 中，已经卡了一个多小时了
im3x		    2
im3x   
OP
   2020-10-27 23:53:53 +08:00
nmap 安装成功，测试扫描使用失败
zsh 安装成功，oh-my-zsh 成功
```



