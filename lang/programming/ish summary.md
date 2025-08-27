
# git-lfs
```

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



