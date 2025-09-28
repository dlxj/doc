```

因为Alpine Linux默认使用的是国外的源，使用国外的服务器，网速特别慢，更换成国内阿里云、中科大、清华的源都可以。

https://mirrors.aliyun.com/alpine/v3.22/community/aarch64/git-lfs-3.6.0-r7.apk

vi /etc/apk/repositories
在最上面添加这两行：

# 阿里云源
https://mirrors.aliyun.com/alpine/v3.22/main
https://mirrors.aliyun.com/alpine/v3.22/community
# 中科大源
https://mirrors.ustc.edu.cn/alpine/v3.22/main
https://mirrors.ustc.edu.cn/alpine/v3.22/community
这两行，注意v后面的版本号，对应原来文件中的版本号。

保存退出，使用下面的语句更新源列表，就可以愉快地安装软件了。

（更新：如果apk not found，那么请移至文末，安装apk）


apk add <package_name>: 安装软件包

apk del <package_name>: 卸载软件包

apk upgrade: 升级所有已安装的软件包

apk search <keyword>: 搜索软件包

apk info: 列出已安装的软件包或显示某个包的详细信息

	
apk fix
	如果安装后遇到依赖问题，可以尝试修复。

下载单个包及其所有依赖：使用 -R选项。

apk fetch -R nginx
	这会将 nginx包及其所有依赖下载到当前工作目录


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



# ish

```


#!/bin/bash

# 遍历当前目录下的所有软链接
for symlink in *; do
    # 检查是否为软链接
    if [ -L "$symlink" ]; then
        # 获取软链接指向的真实文件路径
        target=$(readlink "$symlink")
        
        # 检查目标文件是否存在
        if [ -f "$target" ]; then
            echo "处理软链接: $symlink -> $target"
            
            # 删除软链接
            rm "$symlink"
            
            # 将目标文件移动到软链接的位置（重命名）
            mv "$target" "$symlink"
            
            echo "已完成: $symlink"
        else
            echo "警告: 软链接 $symlink 指向的文件 $target 不存在，跳过处理"
        fi
    fi
done

echo "所有软链接处理完成"


pip install hf_xet

pip install huggingface_hub && \
git config --global credential.helper store && \
huggingface-cli login

echo https://dl-cdn.alpinelinux.org/alpine/v3.13/main >> /etc/apk/repositories
echo https://dl-cdn.alpinelinux.org/alpine/v3.13/community >> /etc/apk/repositories
apk update
apk del --rdepends python3 # removes everything using python3.9
apk add python3\<3.9 py3-numpy\<1.20 py3-pip 
python3 -m ensurepip
the client ip is 10.0.2.15 host is 10.0.2.2
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet static
        address 172.21.123.73
        netmask 255.255.0.0
        gateway 172.21.127.253
阿里57的配置
iface eth0 inet dhcp
dhclient eth0 
/etc/network/interfaces
lsblk
partprobe /dev/sda
parted /dev/sda resizepart 3 100%
hf download dlxjj/bookread --repo-type dataset
https://huggingface.co/docs/huggingface_hub/guides/cli
apk add python3 py3-pip
modprobe 9pnet_virtio  # 针对 Virtio 传输
modprobe 9p
modprobe 9pnet
lsmod
https://ivonblog.com/posts/ios-utm-alpine-linux-vm/
https://pokelink.xn--4gsvmh74cwxi.cn/api/v1/client/subscribe?token=13dbb1bd2634dc38b473c69aff59bedd
https://love.52pokemon.cc/
https://www.wsj.com/opinion 观点
https://cn.wsj.com  https://jp.wsj.com/

https://qemu.weilnetz.de/w64/qemu-w64-setup-20250826.exe

vi /etc/apk/repositories
community 那一行默认是注释了的

apk update
apk add git
apk add git-lfs
git lfs install

poweroff
	# 这样关机

rc-service sshd status

nmap -p 22 --unprivileged 10.0.2.15
	# windows 测试 alpine 22 是通的

qemu-img create -f qcow2  alpine.qcow2 20G  创建虚拟磁盘
qemu-system-x86_64 -m 1024 -hda alpine.qcow2 -cdrom alpine-standard-3.22.1-x86_64.iso -boot d -netdev user,id=net0 -device e1000,netdev=net0
lsblk
qemu-system-x86_64 -m 1024 -hda alpine.qcow2  -boot c -netdev user,id=net0,hostfwd=tcp::127.0.0.1:2112-:22 -device e1000,netdev=net0 装完后启动
    # 端口转发 2112 -> 22
qemu-system-x86_64 -hda alpine.qcow2 -boot d -net nic,model=virtio -net user,hostfwd=tcp::10022-:22  1022 -> 22 端口转发
qemu-system-x86_64 -hda alpine.qcow2 -boot d -vnc :1 VNC客户端中连接到localhost:5901（默认VNC端口为5900+显示号）
qemu-img snapshot -c my_snapshot alpine.qcow2
qemu-img convert -f qcow2 -O qcow2 alpine.qcow2 cloned_image.qcow2
qemu-system-x86_64 -hda your_image.qcow2 -boot d -smp 4  CPU数量4


https://josephcz.xyz/technology/linux/install-alpine-on-aliyun  aliyun install
https://qemu.weilnetz.de/w64/qemu-w64-setup-20250826.exe
https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/x86_64/alpine-standard-3.22.1-x86_64.iso
https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/aarch64/alpine-standard-3.22.1-aarch64.iso
https://ivonblog.com/posts/ios-utm-alpine-linux-vm/
https://apps.apple.com/us/app/utm-se-retro-pc-emulator/id1564628856
https://blog.zdawn.net/archives/obisidian-sync-to-syncthing 
https://apps.apple.com/us/app/working-copy-git-client/id896694807

https://huggingface.co/datasets/dlxjj/bookread

python3 -m ensurepip
apk add py3-pip
https://github.com/ish-app/ish/wiki/Running-in-background
apk add python3 python3-dev python3-pip

因为Alpine Linux默认使用的是国外的源，使用国外的服务器，网速特别慢，更换成国内阿里云、中科大、清华的源都可以。

https://mirrors.aliyun.com/alpine/v3.22/community/aarch64/git-lfs-3.6.0-r7.apk

vi /etc/apk/repositories
在最上面添加这两行：

# 阿里云源
https://mirrors.aliyun.com/alpine/v3.22/main
https://mirrors.aliyun.com/alpine/v3.22/community
# 中科大源
https://mirrors.ustc.edu.cn/alpine/v3.22/main
https://mirrors.ustc.edu.cn/alpine/v3.22/community
这两行，注意v后面的版本号，对应原来文件中的版本号。

保存退出，使用下面的语句更新源列表，就可以愉快地安装软件了。

（更新：如果apk not found，那么请移至文末，安装apk）


apk add <package_name>: 安装软件包

apk del <package_name>: 卸载软件包

apk upgrade: 升级所有已安装的软件包

apk search <keyword>: 搜索软件包

apk info: 列出已安装的软件包或显示某个包的详细信息

	
apk fix
	如果安装后遇到依赖问题，可以尝试修复。

下载单个包及其所有依赖：使用 -R选项。

apk fetch -R nginx
	这会将 nginx包及其所有依赖下载到当前工作目录




alpine v3.20 x84_x64 正常显示中文
Almalinux 9 docker 里的 alpine 3.20 x84_x64 正常显示中文


yum install -y yum-utils device-mapper-persistent-data lvm2 \
  && yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
  && yum install docker-ce \
  && systemctl start docker \
  && systemctl enable docker \
  && docker version \
  && docker ps \
  && docker images
  
  
#docker login
#docker pull alpine


docker pull ghcr.io/linuxcontainers/alpine:latest
    # docker pull ghcr.io/linuxcontainers/alpine:3.20


vi Dockerfile
         
FROM ghcr.io/linuxcontainers/alpine:latest
RUN apk update && apk upgrade
RUN apk --no-cache add ca-certificates
RUN apk add bash bash-doc bash-completion
RUN apk add vim wget curl net-tools
RUN rm -rf /var/cache/apk/*
RUN /bin/bash
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-bin-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-i18n-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-dev-2.35-r1.apk
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub


docker build -t alpine_zh .


docker network create --subnet=172.20.0.0/16 customnetwork


docker stop alpine_zh_ENV \
  && docker rm alpine_zh_ENV


docker run -tid --name alpine_zh_ENV --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true alpine_zh /bin/bash
    # 成功运行


docker exec -it alpine_zh_ENV bash
    # 进入 docker


apk del gcompat libc6-compat
    # alpine/v3.20 它是这个版本
    # 并没有装 gcompat 和 libc6-compat


apk add glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-dev-2.35-r1.apk glibc-i18n-2.35-r1.apk --allow-untrust --force-overwrite


/usr/glibc-compat/bin/localedef -i zh_CN -f UTF-8 zh_CN.UTF-8


vi /etc/profile
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8


source /etc/profile


/usr/glibc-compat/bin/localedef --help 
    # 实测到这里在 awslightsail 已经正常显示中文了


apk add fonts-noto-core fonts-noto-cjk ttf-dejavu fontconfig \
  && mkfontscale && mkfontdir && fc-cache --force
  UTM SE 共享目录
 「https://blog.csdn.net/m0_45378777/article/details/145263854」- https://blog.csdn.net/m0_45378777/article/details/145263854 


mkdir /mnt/mp
mount -t 9p -o trans=virtio share /mnt/mp -oversion=9p2000.L
    # 共享目录就挂载到了/mnt/mp里
    
配置 /etc/fstab 文件 ，例如
share [mount point] virtiofs rw,nofail 0 0
    # 永久生效




```





# QEMU

```

https://qemu.weilnetz.de/w64/qemu-w64-setup-20250826.exe

vi /etc/apk/repositories
community 那一行默认是注释了的

apk update
apk add git
apk add git-lfs
git lfs install

poweroff
	# 这样关机

rc-service sshd status

nmap -p 22 --unprivileged 10.0.2.15
	# windows 测试 alpine 22 是通的

-netdev user,id=net0,hostfwd=tcp::2112-:22

qemu-img create -f qcow2  alpine.qcow2 20G  创建虚拟磁盘
qemu-system-x86_64 -m 1024 -hda alpine.qcow2 -cdrom alpine-standard-3.22.1-x86_64.iso -boot d -netdev user,id=net0 -device e1000,netdev=net0
lsblk
qemu-system-x86_64 -m 1024 -hda alpine.qcow2  -boot c -netdev user,id=net0,hostfwd=tcp::127.0.0.1:2112-:22 -device e1000,netdev=net0 装完以后这样启动
  # 端口转发 2112 -> 22
qemu-system-x86_64 -hda alpine.qcow2 -boot d -vnc :1 VNC客户端中连接到localhost:5901（默认VNC端口为5900+显示号）
qemu-img snapshot -c my_snapshot alpine.qcow2
qemu-img convert -f qcow2 -O qcow2 alpine.qcow2 cloned_image.qcow2
qemu-system-x86_64 -hda your_image.qcow2 -boot d -smp 4  CPU数量4


https://qemu.weilnetz.de/w64/qemu-w64-setup-20250826.exe
https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/x86_64/alpine-standard-3.22.1-x86_64.iso
https://dl-cdn.alpinelinux.org/alpine/v3.22/releases/aarch64/alpine-standard-3.22.1-aarch64.iso
https://ivonblog.com/posts/ios-utm-alpine-linux-vm/
https://apps.apple.com/us/app/utm-se-retro-pc-emulator/id1564628856
https://blog.zdawn.net/archives/obisidian-sync-to-syncthing 
https://apps.apple.com/us/app/working-copy-git-client/id896694807

https://huggingface.co/datasets/dlxjj/bookread

python3 -m ensurepip
apk add py3-pip
https://github.com/ish-app/ish/wiki/Running-in-background
apk add python3 python3-dev python3-pip

因为Alpine Linux默认使用的是国外的源，使用国外的服务器，网速特别慢，更换成国内阿里云、中科大、清华的源都可以。

https://mirrors.aliyun.com/alpine/v3.22/community/aarch64/git-lfs-3.6.0-r7.apk

vi /etc/apk/repositories
在最上面添加这两行：

# 阿里云源
https://mirrors.aliyun.com/alpine/v3.22/main
https://mirrors.aliyun.com/alpine/v3.22/community
# 中科大源
https://mirrors.ustc.edu.cn/alpine/v3.22/main
https://mirrors.ustc.edu.cn/alpine/v3.22/community
这两行，注意v后面的版本号，对应原来文件中的版本号。

保存退出，使用下面的语句更新源列表，就可以愉快地安装软件了。

（更新：如果apk not found，那么请移至文末，安装apk）


apk add <package_name>: 安装软件包

apk del <package_name>: 卸载软件包

apk upgrade: 升级所有已安装的软件包

apk search <keyword>: 搜索软件包

apk info: 列出已安装的软件包或显示某个包的详细信息

	
apk fix
	如果安装后遇到依赖问题，可以尝试修复。

下载单个包及其所有依赖：使用 -R选项。

apk fetch -R nginx
	这会将 nginx包及其所有依赖下载到当前工作目录

```



# alpine v3.20 x84_x64 正常显示中文

```
Almalinux 9 docker 里的 alpine 3.20 x84_x64 正常显示中文

yum install -y yum-utils device-mapper-persistent-data lvm2 \
  && yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
  && yum install docker-ce \
  && systemctl start docker \
  && systemctl enable docker \
  && docker version \
  && docker ps \
  && docker images
  
  
#docker login
#docker pull alpine


docker pull ghcr.io/linuxcontainers/alpine:latest
	# docker pull ghcr.io/linuxcontainers/alpine:3.20

vi Dockerfile
         
FROM ghcr.io/linuxcontainers/alpine:latest
RUN apk update && apk upgrade
RUN apk --no-cache add ca-certificates
RUN apk add bash bash-doc bash-completion
RUN apk add vim wget curl net-tools
RUN rm -rf /var/cache/apk/*
RUN /bin/bash
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-bin-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-i18n-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-dev-2.35-r1.apk
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub

docker build -t alpine_zh .

docker network create --subnet=172.20.0.0/16 customnetwork

docker stop alpine_zh_ENV \
  && docker rm alpine_zh_ENV

docker run -tid --name alpine_zh_ENV --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true alpine_zh /bin/bash
	# 成功运行

docker exec -it alpine_zh_ENV bash
	# 进入 docker

apk del gcompat libc6-compat
	# alpine/v3.20 它是这个版本
	# 并没有装 gcompat 和 libc6-compat

apk add glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-dev-2.35-r1.apk glibc-i18n-2.35-r1.apk --allow-untrust --force-overwrite


/usr/glibc-compat/bin/localedef -i zh_CN -f UTF-8 zh_CN.UTF-8

vi /etc/profile
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

source /etc/profile

/usr/glibc-compat/bin/localedef --help 
	# 实测到这里在 awslightsail 已经正常显示中文了
	# 其实是 xshell 连上去显示中文，在那上面原生显示不了的


apk add fonts-noto-core fonts-noto-cjk ttf-dejavu fontconfig \
  && mkfontscale && mkfontdir && fc-cache --force
  
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



