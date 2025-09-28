

# install alpine

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

qemu-system-x86_64 -m 1024 -hda alpine.qcow2  -boot c -netdev user,id=net0 -device e1000,netdev=net0 -fsdev local,security_model=passthrough,id=fsdev0,path=f:\shared -device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=hostshare
	# 共享目录


qemu-img create -f qcow2  alpine.qcow2 20G  创建虚拟磁盘
qemu-system-x86_64 -m 1024 -hda alpine.qcow2 -cdrom alpine-standard-3.22.1-x86_64.iso -boot d -netdev user,id=net0 -device e1000,netdev=net0
lsblk
qemu-system-x86_64 -m 1024 -hda alpine.qcow2  -boot c -netdev user,id=net0,hostfwd=tcp::127.0.0.1:2112-:22 -device e1000,netdev=net0 装完以后这样启动
  # 端口转发 2112 -> 22
qemu-system-x86_64 -hda alpine.qcow2 -boot d -net nic,model=virtio -net user,hostfwd=tcp::10022-:22  1022 -> 22 端口转发
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



## ish

```

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


apk add font-noto-core font-noto-cjk ttf-dejavu fontconfig \
  && mkfontscale && mkfontdir && fc-cache --force
  
```



# UTM SE 共享目录

https://blog.csdn.net/m0_45378777/article/details/145263854

```

mkdir /mnt/mp
sudo mount -t 9p -o trans=virtio share /mnt/mp -oversion=9p2000.L
	# 共享目录就挂载到了/mnt/mp里
	
配置 /etc/fstab 文件 ，例如
share [mount point] virtiofs rw,nofail 0 0
	# 永久生效

```







# Hyper-V 虚拟机

https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/get-started/install-hyper-v?tabs=powershell&pivots=windows

```
# see QEMU Summary.md

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All



```







# 阿里云安装 alpine

https://josephcz.xyz/technology/linux/install-alpine-on-aliyun/

https://luotianyi.vc/8445.html

- ```
  
  从 HyperV 中创建一个1024M的动态扩展.vhd文件
  
  HyperV 新建一个代次为Gen1的虚拟机，然后挂载.vhd的磁盘和 alpine-standard x64 iso 镜像开机进行安装
  
  # 通过正常安装流程进行联网、镜像源设置，随后终止安装流程
  setup-alpine
  # 安装分区工具
  apk add parted e2fsprogs
  # 进行分区
  parted -sa optimal /dev/sda mklabel msdos # 设置分区表为mbr格式
  parted -sa optimal /dev/sda mkpart primary 512B 50MB # 划分boot分区
  parted -sa optimal /dev/sda mkpart primary 50MB 100% # 划分所有容量至主分区
  parted -sa optimal /dev/sda set 1 boot # 设置分区1启动卷标
  mkfs.ext4 /dev/sda1 # 格式化boot分区
  mkfs.ext4 /dev/sda2 # 格式化主分区
  # 重启
  reboot
  # 挂载磁盘，注意先后及新建文件夹
  mount /dev/sda2 /mnt
  mount /dev/sda1 /mnt/boot
  ```
# 通过正常安装流程进行所有设置，到选择磁盘后终止
  setup-alpine
  # 安装
  setup-disk /mnt

  	# 实测这个 vhd 上传阿里自定义镜像后，正常开机使用

  ```
  
  

  ```
在阿里云低配置服务器上安装 Alpine Linux
近期有几个服务器到期，又对国内低流量、大带宽的服务器有一定需求（主要是用于内网穿透），于是入手了阿里云的 2C0.5G T6 突发性能实例。综合下来五年仅需不到 200 元，性价比极高。

然而云服务的一大特点是「块存储」，也就是硬盘收费很贵，算下来硬盘价格比服务器本身还高。因此选用一个体积较小的操作系统就显得尤为重要。早在之前 LMS 就已介绍了如何自定义 Alpine Linux 镜像以超低价格购买该配置的实例。然而对我来说，还有几个需要考虑的地方：

希望使用 LUKS 加密，以防止阿里云的「自动化扫描硬盘」
出于个人偏好，想要使用 btrfs 文件系统
由于内存较小，因此使用 x86-32 而非 x86-64 架构以节省内存占用
同时，不同于该文章使用 Hyper-V 创建虚拟机的方式，本文使用了笔者更加熟悉的 Proxmox VE。

本文所涉 Alpine Linux 版本为 3.21，未来更新版本的配置方式可能有所区别，敬请读者在操作时注意。

分区
使用 Proxmox VE 获取镜像及创建虚拟机的过程在此不再赘述，由于 32 位系统默认不支持 UEFI，因此请选择 BIOS 引导类型。

笔者建议，在开始安装 Alpine Linux 之前，使用其他发行版的镜像（例如「Arch Linux 安装介质」或 SystemRescue）先行完成分区工作。

注意

这里需要注意的是，和其他发行版不同，Alpine Linux 默认的 syslinux 引导程序只支持从 512B 处读取 /boot 分区。因此，无法使用 cfdisk、fdisk 工具进行分区（因为其默认会进行 2048B 对齐）。为了指定准确的分区开始位置，建议使用 parted 工具进行分区。

为了获得更好的性能，笔者依然在划分主分区时进行了对齐，即在 /dev/vda1 和 /dev/vda2 之间留下部分间隙，/dev/vda1 使用 parted 分区设置的起始位置为 512B、不对齐到 2048B；/dev/vda2 使用 cfdisk 分区工具对齐到 2048B。

然而，由于未知的 bug，cfdisk 写入分区表不会被 Alpine Linux 安装介质的内核重新加载，因此建议在其他操作系统完成分区后，再使用 Alpine Linux 安装介质进行格式化和安装。

1
2
3
4
5
6
parted -sa optimal /dev/vda mklabel msdos
parted -sa optimal /dev/vda mkpart primary 512B 128MB
parted -sa optimal /dev/sda set 1 boot

# 在 cfdisk 界面中创建第二个分区
cfdisk /dev/vda
注意

GRUB 可能并不需要为第一个分区设置 bootable flag，但是 Alpine Linux 在使用 syslinux 引导程序的情况下，为 /boot 分区设置 bootable flag 是必要的。否则，Alpine Linux 将无法引导。

提示

尽管 50MB 已足够 Alpine Linux 的 /boot 分区使用，但在默认情况下，btrfs 需要大于 128MB 的空间才能格式化。因此，笔者将 /boot 分区设置为 128MB。

安装和格式化
在分区完成后，使用 Alpine Linux 安装介质引导系统。进入安装界面后，使用 setup-alpine 命令进行安装。

1
setup-alpine
安装过程在此不再赘述。在完成镜像设置之后、选择安装磁盘前，使用 Ctrl+C 退出安装程序。

首先安装需要的软件包：

1
apk add --no-cache cfdisk parted e2fsprogs btrfs-progs cryptsetup lsblk
然后对之前的分区进行格式化：

1
2
mkfs.btrfs -L alpine-boot /dev/vda1
cryptsetup luksFormat /dev/vda2
请在提示时输入 YES （必须为大写字母） 以确认格式化。接下来，使用 cryptsetup luksOpen 命令打开加密分区，并完成后续操作：

1
2
cryptsetup luksOpen /dev/vda2 root
mkfs.btrfs -L alpine-root /dev/mapper/root
由于 Alpine Linux 作为最小化操作系统，并不总是加载所有内核模块，因此如果直接进行分区挂载，会显示 Invalid argument 错误。因此，我们需要手动加载内核模块：

1
2
modprobe btrfs
modprobe ext4
然后挂载分区：

1
2
3
mount /dev/mapper/root /mnt
mkdir /mnt/boot
mount /dev/vda1 /mnt/boot
完成后，使用 lsblk 命令检查分区是否正确挂载。

如果一切正常，继续安装 Alpine Linux：

1
setup-disk -m sys /mnt
如果一切正常，重启后将进入引导界面，输入 LUKS 密码后可以正常进入系统。

镜像导出 Proxmox VE
在 Proxmox VE 关机的情况下，使用 qemu-img 命令将虚拟机的磁盘导出为 qcow2 格式：

1
qemu-img convert /data/images/<vmid>/vm-<vmid>-disk-0/disk.raw ~/alpine.qcow2 -O qcow2 -f raw
其中：

/data/images 为 Proxmox VE 中设置的 VM 磁盘存储路径
<vmid> 为虚拟机 ID
假设磁盘 ID 为 0
完成后，通过 scp 或其他终端软件集成的文件管理器将 alpine.qcow2 文件下载到本地。

镜像导入阿里云
在计划创建服务器的同一地域（即，如果打算在杭州创建服务器，那么就需要在杭州地域创建一个 OSS）创建一个 OSS，名称随意，访问权限可以为私有。

将本地的 alpine.qcow2 文件上传到 OSS 中。在阿里云的镜像导入界面，选择 「导入镜像」。

镜像文件 URL：填写 OSS 中的文件 URL，有无签名均可
镜像名称：根据自己需要填写
操作系统类型：Linux
操作系统版本：Customized Linux
系统架构：32 位
启动模式：BIOS
镜像格式：qcow2
此处需要 勾选「配置云盘属性」，并设置云盘大小为 1GB 或 2GB（根据实际需要）。

注意

阿里云默认导入的镜像大小为 20GB，因此如果不勾选「配置云盘属性」，会导致创建服务器时无法将系统盘设置得更小。

完成导入后，创建服务器的过程不再赘述。

创建完成后，可以使用阿里云自带的 Web VNC 连接到服务器，以输入 LUKS 密码并登录。

SSH 安全配置
注意

由于 SSH 尚未配置，本节内容在 VNC 界面中完成。

由于安装 Alpine 时选择了 OpenSSH，因此其他发行版的 OpenSSH 配置可以通用。

1
2
3
4
5
6
sudo sed -i "/^#HostKey/s/^#//g"                                           /etc/ssh/sshd_config
sudo sed -i "/^#ListenAddress 0.0.0.0/s/^#//g"                             /etc/ssh/sshd_config
sudo sed -i "/^#PubkeyAuthentication yes/s/^#//g"                          /etc/ssh/sshd_config
sudo sed -i "s/^#PasswordAuthentication yes$/PasswordAuthentication no/g"  /etc/ssh/sshd_config
sudo sed -i "s/^#PermitRootLogin yes$/PermitRootLogin prohibit-password/g" /etc/ssh/sshd_config
sudo sed -i "s/^#PermitRootLogin no$/PermitRootLogin prohibit-password/g"  /etc/ssh/sshd_config
然后，重启 SSH 服务：

1
sudo rc-service sshd restart
配置 SSH 安全密钥：

1
2
mkdir -p ~/.ssh
echo "<YOUR_PUBLIC_KEY>" >> ~/.ssh/authorized_keys
如果使用阿里云，可以使用 VNC 控制台的「黏贴命令」来黏贴你的 SSH 公钥。

如果配置正常，至此，即可使用 SSH 连接服务器公网 IP。

如果无法连接，请检查云服务是否分配公网 IP 及安全组、防火墙等设置。

更换镜像源
注意

此节及之后的内容在 SSH 界面中完成，您需要以 root 身份登录 SSH。

修改 /etc/apk/repositories 文件，将 dl-cdn.alpinelinux.org 替换为想要的源地址，视情况可取消 Community 源的注释。

1
2
https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.21/main
https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.21/community
如果使用阿里云，可以使用内网源：

1
2
http://mirrors.cloud.aliyuncs.com/alpine/v3.21/main
http://mirrors.cloud.aliyuncs.com/alpine/v3.21/community
vi = vim，以及不得不装的工具
安装 vim：

1
2
3
apk add vim sudo curl
rm /bin/vi
ln -s /usr/bin/vim /bin/vi
修改默认 shell 为 bash
安装 bash：

1
2
apk update
apk add bash bash-completion shadow
修改默认 shell：

1
chsh -s /bin/bash
有强迫症可以清除 ash 的历史记录：

1
rm -v ~/.ash_history
配置 LUKS 自动解锁
会降低安全性，但是对于服务器来说，重启可以自动化，无需人工干预输入密码。是否进行这一步骤，请慎重考虑。

1
2
3
4
5
dd if=/dev/urandom of=/crypto_keyfile.bin bs=1024 count=4
chmod 000 /crypto_keyfile.bin
cryptsetup luksAddKey \
    --pbkdf pbkdf2 --pbkdf-memory 25600 \
    <luks-device> /crypto_keyfile.bin
其中，<luks-device> 是加密分区的设备名，例如 /dev/sda2。

如果服务器内存很小（小于 1GB），可以使用 --pbkdf pbkdf2 --pbkdf-memory 25600 来换用内存更少的 PBKDF2 算，并限制内存使用量为 25600 KiB。

如果服务器内存较大，可以去掉 --pbkdf 和 --pbkdf-memory 参数，使用更加安全的 Argon2 算法。

使用下面的命令确认是否成功，如果成功，则可以看见新增的 Key Slot（一般为 Slot 1）：

1
cryptsetup luksDump <luks-device>
然后，修改 /etc/mkinitfs/mkinitfs.conf 文件，在 features 中添加 cryptkey 和 btrfs (由于我的 /boot 分区使用了 btrfs，因此需要添加这个选项)。

1
2
3
# /etc/mkinitfs/mkinitfs.conf
# 这是我的配置文件，可能和你的不一样，请根据实际情况添加
features="ata base ide scsi usb virtio ext4 btrfs cryptsetup cryptkey keymap"
更新 initramfs：

1
mkinitfs
此外，还需要修改 /etc/update-extlinux.conf 文件：

在 modules 中添加 btrfs（如果你的 /boot 分区使用了 btrfs，如果没有使用 btrfs，则不需要添加这个选项）
在 default_kernel_opts 中添加 cryptkey
1
2
3
4
5
6
7
8
9
10
# /etc/update-extlinux.conf
# 这是我的配置文件，可能和你的不一样，请根据实际情况添加（至少 UUID 是肯定不一样的！）

# default_kernel_opts
# default kernel options
default_kernel_opts="cryptroot=UUID=6dc7d6d2-8677-41d5-b38d-acc582080c8e cryptkey cryptdm=root quiet rootfstype=ext4"

# modules
# modules which should be loaded before pivot_root
modules=sd-mod,usb-storage,ext4,btrfs
根据我的个人习惯，另外的，我还会修改以下选项：

verbose 选项设置为 1，这样执行 update-extlinux 时会显示详细的执行过程
去掉 default_kernel_opts 中的 quiet 选项，这样可以在启动时看到详细的启动过程
然后，更新 extlinux：

1
update-extlinux
重启服务器，如果没有配置错误，此时可以看到服务器自动解锁 LUKS 分区，进入系统。

最后，如果重启成功，可以删除原有的 LUKS 密码，以增加安全性：

1
2
3
cryptsetup luksKillSlot \
    --key-file /crypto_keyfile.bin \
    <luks-device> 0
用户默认的 dotfiles
使用 /etc/skel 目录中的文件作为新用户的默认配置文件。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
mkdir -p /etc/skel

cat <<EOF > /etc/skel/.vimrc
syntax on
filetype on
set showmatch
set ruler
set incsearch
set mouse=
set backspace=indent,eol,start
EOF

cat <<EOF > /etc/skel/.bashrc
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias dir='dir --color=auto'
alias vdir='vdir --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

export PS1="[\[\e[01;34m\]\u\[\e[0m\]@\[\e[01;31m\]\H \[\e[01;33m\]\w\[\e[0m\]] "
export EDITOR=vim
EOF

cat <<EOF > /etc/skel/.bash_profile
if [ -f $HOME/.bashrc ]; then
    . $HOME/.bashrc
fi
EOF

cp /etc/skel/.* ~
配置开机后及 TTY 登出时清屏
在 Debian 上，计算机开机之后及在 TTY 登出时，都会自动清屏。要在 Alpine 上实现这个行为，需要修改 /etc/issue 文件。

1
2
3
4
clear > issue
cat /etc/issue >> issue
cat issue > /etc/issue
rm -iv issue
可以通过 vim 打开 /etc/issue 文件，查看是否有控制字符，来确定是否成功。

修改 MOTD
1
2
3
4
. /etc/os-release
echo -e "Welcome to \e[34m${PRETTY_NAME}\e[0m" >> /etc/motd
# 下面这行只对阿里云有效
echo -e "Public IP: \e[36m$(curl -sf --connect-timeout 5 http://100.100.100.200/latest/meta-data/eipv4)\e[0m" >> /etc/motd
调整内核参数
1
2
3
4
5
6
echo 'net.core.default_qdisc = fq'           | tee -a /etc/sysctl.d/10-tcp-bbr.conf
echo 'net.ipv4.tcp_congestion_control = bbr' | tee -a /etc/sysctl.d/10-tcp-bbr.conf

echo 'net.ipv6.conf.default.disable_ipv6 = 1' | tee -a /etc/sysctl.d/20-disable-ipv6.conf
echo 'net.ipv6.conf.all.disable_ipv6 = 1'     | tee -a /etc/sysctl.d/20-disable-ipv6.conf
echo 'net.ipv6.conf.lo.disable_ipv6 = 1'      | tee -a /etc/sysctl.d/20-disable-ipv6.conf
另外可以尝试 https://omnitt.com/ 的 TCP 调参算法，但是我没有尝试过。

添加 swap 和 zram
安装 zram-init：

1
apk add zram-init
编辑 /etc/conf.d/zram-init 文件，设置 zram 的大小：

1
2
num_devices=1  # zram 设备数量
size0=128      # 单位为MB，配置为物理 RAM 的一半
然后启动 zram-init：

1
rc-service zram-init start
然后配置 swap：

1
2
3
4
dd if=/dev/zero of=/swapfile bs=1M count=512
chmod 000 /swapfile
mkswap -L alpine-swap /swapfile
swapon /swapfile
然后，编辑 /etc/fstab 文件，添加 swap：

1
echo -e "/swapfile\tswap\tswap\tdefaults\t0 0" | tee -a /etc/fstab
如果有需要，也可以删除 fstab 内无用的 USB 和 CD-ROM 的挂载项。

配置 NTP
创建 /etc/periodic/hourly/10-timesync-ntpd 文件：

1
2
#!/bin/sh
ntpd -d -q -n -p ntp.cloud.aliyuncs.com
该 NTP 服务器为阿里云内网 NTP 服务器，如果你在其他云服务商上，请自行寻找合适的 NTP 服务器。

然后，给文件添加可执行权限：

1
chmod +x /etc/periodic/hourly/10-timesync-ntpd

```



## 紧急临时网络

```
# 紧急网络恢复（如果网络完全无法使用）

ip addr 				查看它的输出的网络配置
ip route show default   查看默认网关

# 重置所有网络接口

ip addr flush dev eth0
ip route del default
	# 清除可能存在的旧配置

ip link set eth0 down
ip link set eth0 up

# 手动配置 IP（临时）

ip addr add 172.21.123.73/16 dev eth0
ip route add default via 172.21.127.253

# 手动配置 DNS

echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

# 实测到这里能 ping 通 qq.com 了

```





## 永久网络

```

vi /etc/network/interfaces
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
        address 172.21.123.73
        netmask 255.255.0.0
        gateway 172.21.127.253

vi /etc/resolv.conf
nameserver 8.8.8.8

```







# 中文显示

https://three-corner.xyz/blog/blogdetail/245

https://zhuanlan.zhihu.com/p/689702275 极高效极安全的搭建微服务Docker环境：一步到位的实用教程

https://blog.csdn.net/weixin_56364253/article/details/141190043

https://sspai.com/post/92955

https://ivonblog.com/posts/alpine-linux-installation/



```

apk del gcompat libc6-compat
	# 关键

wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk

wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-bin-2.35-r1.apk

wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-i18n-2.35-r1.apk

wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-dev-2.35-r1.apk

wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub

apk add glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-dev-2.35-r1.apk glibc-i18n-2.35-r1.apk --allow-untrust --force-overwrite
	# 实测成功安装 

apk add bash bash-doc bash-completion

/bin/bash

/usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8

vi /etc/profile
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

source /etc/profile


# 到这里还是没有显示出中文


apk add fonts-noto-core fonts-noto-cjk

apk add ttf-dejavu fontconfig

mkfontscale && mkfontdir && fc-cache --force

vi /etc/profile
export LANG=zh_CN.utf8
source /etc/proflie

/usr/glibc-compat/bin/localedef --help 
	# 这里面应该能显示中文


https://www.cnblogs.com/equation/p/15346858.html

##加入path
13 #vi /etc/profile
14 ##在apeend_path函数后面添加一行#
15 #...
16 #append_path "/usr/glibc-compat/bin"
17 #...
18 ##然后按esc 输入wq退出
19 #
20 ##生成zh_CN.utf8 locale
21 #/usr/glibc-compat/bin/localedef -i zh_CN -f UTF-8 zh_CN.UTF-8
22 ##修改locale.sh
23 #vi /etc/profile.d/locale.sh
24 #用#号注释掉原有的所有语句,添加一条语句
25 #...
26 #export LANG=zh_CN.utf8
27 #...
28 ##然后按esc 输入wq退出
29 #
30 ##使配置立即生效
31 #source /etc/proflie
32 #
33 ##安装中文字体和相关时区信息
34 #apk add --update tzdata busybox-extras fontconfig ttf-dejavu
35 ##设置本地时区
36 #ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
37 #echo 'Asia/Shanghai' > /etc/timezone


```









```


# Arch Linux。其中noto-fonts为西文字体，noto-fonts-cjk为中日韩文字体
sudo pacman -S noto-fonts noto-fonts-cjk

# Ubuntu
sudo apt install fonts-noto-core fonts-noto-cjk

# Alpine
sudo apk update
sudo apk add --upgrade font-noto font-noto-cjk

# Void Linux
sudo xbps-install -Su noto-fonts-ttf noto-fonts-cjk


/usr/share/fonts/
	# 自定义字体放这
    


```





```

apk add fontconfig && apk add --update ttf-dejavu && fc-cache --force

apk add gcompat
	#  glibc-compatible APIs for use on musl libc systems

apk add bash
chsh -s /bin/bash
	# 使用对 locale 支持更好的 shell


vi Dockerfile
FROM alpine:3.22.1

# 安装基础工具和glibc
RUN apk --no-cache add ca-certificates wget && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-bin-2.35-r1.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-i18n-2.35-r1.apk

# 安装glibc并清理
RUN apk update && apk add glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-i18n-2.35-r1.apk && \
    rm -rf glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-i18n-2.35-r1.apk

# 设置时区为上海
RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

# 复制locale配置文件
COPY ./locale.md /locale.md

# 生成UTF-8 locale
RUN cat locale.md | xargs -i /usr/glibc-compat/bin/localedef -i {} -f UTF-8 {}.UTF-8

# 设置中文环境变量
ENV LANG=zh_CN.UTF-8 \
    LANGUAGE=zh_CN.UTF-8 \
    LC_ALL=zh_CN.UTF-8

# 安装基础工具和字体（可选）
RUN apk add --no-cache bash curl vim

# 设置工作目录
WORKDIR /app

# 默认启动bash
CMD ["/bin/bash"]


vi locale.md
zh_CN
zh_TW
en_US


vi test.sh
#!/bin/bash

echo "=== 中文显示测试 ==="
echo ""

# 测试中文输出
echo "1. 直接输出中文："
echo "你好，世界！"
echo ""

# 测试环境变量
echo "2. 环境变量设置："
echo "LANG=$LANG"
echo "LANGUAGE=$LANGUAGE"
echo "LC_ALL=$LC_ALL"
echo ""

# 测试locale
echo "3. 可用locale："
locale -a | grep -E "(zh|en)"
echo ""

# 测试当前locale设置
echo "4. 当前locale设置："
locale
echo ""

# 测试文件编码
echo "5. 创建包含中文的文件："
echo "这是一个测试文件，包含中文：你好世界" > test_file.txt
cat test_file.txt
echo ""

# 测试中文文件名
echo "6. 创建中文文件名："
touch "中文文件.txt"
ls -la *中文*
echo ""

echo "=== 测试完成 ==="

```







```


要让 Alpine Linux 中的 ash shell 正确显示中文，需要进行以下几个配置：

1. 安装必要的语言包：
​```bash
apk add --no-cache font-noto-cjk
​```

2. 设置正确的语言环境变量，在 `/etc/profile` 或 `~/.profile` 中添加：
​```bash
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
​```

3. 确保终端支持 UTF-8 编码：
​```bash
export TERM=xterm-256color
​```

4. 如果使用的是容器环境，可能需要在启动容器时设置这些环境变量：
​```bash
docker run -e LANG=zh_CN.UTF-8 -e LC_ALL=zh_CN.UTF-8 alpine /bin/ash
​```

5. 对于某些应用程序，可能还需要安装额外的本地化包：
​```bash
apk add --no-cache musl-locales
​```

完成这些设置后，重新登录或重新加载配置文件（`source ~/.profile`），ash shell 应该能够正确显示中文字符了。
        
        
        




如果在 Alpine Linux 中 `cat` 命令仍然无法正确显示中文，可能需要进行更全面的配置。以下是一些更深入的解决方案：

1. **确保已安装完整的本地化支持**：
   ```bash
   apk add --no-cache musl-locales musl-locales-lang
   ```
```

2. **安装更多字体支持**：
   ```bash
   apk add --no-cache font-noto font-noto-cjk font-noto-emoji
   ​```LAiL
```
```
   
3. **检查文件编码**：
   确保你的文件是 UTF-8 编码的。可以使用 `file` 命令检查：
   ```bash
   file -i 你的文件名
```
   如果不是 UTF-8 编码，可以使用 `iconv` 转换：
   ```bash
   apk add --no-cache iconv
   iconv -f 原编码 -t UTF-8 原文件 > 新文件
   ```

4. **配置完整的本地化环境**：
   在 `/etc/profile.d/` 目录下创建一个新文件，例如 `locale.sh`：
   ```bash
   echo 'export LANG=zh_CN.UTF-8' > /etc/profile.d/locale.sh
   echo 'export LC_ALL=zh_CN.UTF-8' >> /etc/profile.d/locale.sh
   echo 'export LANGUAGE=zh_CN.UTF-8' >> /etc/profile.d/locale.sh
   chmod +x /etc/profile.d/locale.sh
   source /etc/profile.d/locale.sh
   ```

5. **检查终端模拟器设置**：
   如果你是在本地机器上通过SSH或终端模拟器连接到Alpine，确保你的终端模拟器也配置为支持UTF-8。

6. **尝试使用其他工具查看文件**：
   ```bash
   apk add --no-cache less
   export LESSCHARSET=utf-8
   less 你的文件名
   ```

7. **如果是在Docker容器中**：
   确保在启动容器时设置了正确的环境变量：
   ```bash
   docker run -e LANG=zh_CN.UTF-8 -e LC_ALL=zh_CN.UTF-8 -e LANGUAGE=zh_CN.UTF-8 alpine
   ```

8. **检查glibc兼容性**：
   Alpine使用musl libc而不是glibc，某些情况下可能需要安装glibc兼容层：
   ```bash
   apk add --no-cache gcompat
   ```

如果以上方法都不能解决问题，可能需要考虑是否有特殊字符或编码问题，或者考虑使用更完整的Linux发行版，如Ubuntu或Debian，它们默认提供更全面的本地化支持。
        


```





```

# 更新软件包索引
apk update

# 安装中文字体和语言支持
apk add font-noto-cjk
apk add musl-locales
apk add musl-locales-lang

# 编辑 locale 配置
vi /etc/locale.conf

LANG=zh_CN.UTF-8
LC_ALL=zh_CN.UTF-8

# 对于 ash/sh (Alpine 默认)
vi ~/.profile
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
export LC_CTYPE=zh_CN.UTF-8

# 重新加载环境变量
source ~/.profile


# 检查当前 locale 设置
locale

# 测试中文显示
echo "你好，世界！"


# 安装 X11 和桌面环境（可选）
apk add xorg-server
apk add xfce4
apk add font-noto-cjk

# 安装中文输入法（可选）
apk add ibus
apk add ibus-libpinyin


```



```
#!/bin/sh
# 中文配置脚本

# 安装必要软件包
apk update
apk add font-noto-cjk musl-locales musl-locales-lang

# 配置 locale
echo "LANG=zh_CN.UTF-8" > /etc/locale.conf
echo "LC_ALL=zh_CN.UTF-8" >> /etc/locale.conf

# 配置用户环境
echo "export LANG=zh_CN.UTF-8" >> ~/.profile
echo "export LC_ALL=zh_CN.UTF-8" >> ~/.profile
echo "export LC_CTYPE=zh_CN.UTF-8" >> ~/.profile

echo "中文配置完成，请重启系统！"





# Docker



```



# Docker + alpine

https://wener.me/notes/os/alpine/glibc

https://zhuanlan.zhihu.com/p/689702275

```

apk del gcompat libc6-compat
apk add glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-dev-2.35-r1.apk --allow-untrust --force-overwrite

	# 关键

```

Almalinux 9 docker 里的 alpine v3.20 x84_x64 正常显示中文

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


```





vi docker-alpine
FROM alpine:latest
MAINTAINER xltianc

#更换aline源
RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/community" > /etc/apk/repositories
RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/main" >> /etc/apk/repositories

#update apk
RUN apk update && apk upgrade
RUN apk --no-cache add ca-certificates

# bash vim wget curl net-tools
RUN apk add bash bash-doc bash-completion
RUN apk add vim wget curl net-tools
RUN rm -rf /var/cache/apk/*
RUN /bin/bash

#setup glibc
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-bin-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-i18n-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-dev-2.35-r1.apk
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN apk add glibc-2.35-r1.apk
RUN apk add glibc-bin-2.35-r1.apk
RUN apk add glibc-dev-2.35-r1.apk
RUN apk add glibc-i18n-2.35-r1.apk
RUN rm -rf *.apk

#setup 时间
RUN apk add tzdatacp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#setup language 解决中文乱码
RUN /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANG=en_US.UTF-8

#copy jdk-8u401-linux-x64.tar.gz 自己到oracle官网下载，放在dockerfile，就是跟这个文件同级目录
ADD jdk-8u401-linux-x64.tar.gz /usr/local

#setup java env
ENV JAVA_HOME=/usr/local/jdk1.8.0_401
ENV PATH=$PATH:.:$JAVA_HOME/bin
ENV CALSSPATH=$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar



docker build -f docker-alpine-jdk8 -t xltianc/alpine-jdk:1.0.0 .






运行docker build，注意最后的那个 ·

docker build -f docker-alpine-jdk8 -t xltianc/alpine-jdk:1.0.0 .
等待完成之后，docker images测试。

3. 如何将自己的微服务打进alpine容器镜像

上面步骤，主要属于我们的前期准备，下来我们需要将我们的微服务Jar包打进镜像，并且运行起来。

Maven打包就不说了，包括使用Jenkins对原代码进行打包。

假设Jar包已经打好了，我们通过工具或者ftp已经上传到我们的docker所在的服务器了。那么接下来如何操作？

1. 首先给第二步骤xltianc/alpine-jdk:1.0.0打一个tag，标记一下。

docker tag xltianc/alpine-jdk:1.0.0 prowhh/alpine-java8:latest
2. 再写一个Dockerfile，使用tag镜像容器运行Jar

FROM prowhh/alpine-java8:latest
# 微服务jar
ADD /app.jar //
# 运行参数
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "-Xms3072m","-Xmx3072m","-Xmn384m","-XX:SurvivorRatio=3","-XX:+HeapDumpOnOutOfMemoryError", "-XX:HeapDumpPath=/path/heap/dump", "-Duser.timezone=GMT+08","-Djasypt.encryptor.password=EL_1234","/app.jar"]
VOLUME /data
运行docker build

docker build -f Dockerfile -t prowhh/app-server:prod .
4. 快速运行

以上步骤运行完之后，我们再写一个脚本run.sh，进行整体调度，包含容器已经存在进行停止，删除，如果没有进行重新创建，以及映射日志文件操作。

#!/bin/bash

pjname=$1
imprefix="prowhh/$pjname"
containerdata='/data'
echo '#############################################################'
echo "项目名：$pjname"
if [ `docker ps -a|awk '{print $NF}'|grep -w $pjname-prod|wc -l` -ge 1 ];then
  # 停止容器
  echo "停止项目名：$pjname"
  docker stop $pjname-prod &> /dev/null
  # 删除容器
  docker rm -f $pjname-prod &> /dev/null
fi
echo "创建项目名：$pjname"
# 创建一个新的容器
if [ `docker images|awk -v OFS=':' '{print $1,$2}'|grep "$imprefix":prod$|wc -l` -ne 0 ];then
  mkdir -p $containerdata/$pjname-logs/{logs,applogs} &> /dev/null
  docker run -dit --restart=always  --net=host --name $pjname-prod -v /data/dump:/path/heap/dump -v $containerdata/$pjname-logs:/data/logs -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v $containerdata/applogs:/data/applogs -v /data/appdatas:/data/appdatas:ro $imprefix:prod
else
  echo "$imprefix:prod镜像不存在！"  
fi
# 清理生成的临时镜像
if [ `docker images|grep '<none>'|awk '{print $3}'|wc -l` -ne 0 ];then
  docker images|grep '<none>'|awk '{print $3}'|xargs docker rmi &> /dev/null
  echo test > /dev/null
fi


 sh run.sh app-server
以上步骤结束之后，可以将我们自己编译的容器上传至docker hub，以后要用到直接pull即可。


```





# install void linux

```

qemu-img create -f qcow2  void.qcow2 20G

qemu-system-x86_64 -m 2048 -hda void.qcow2 -cdrom void-live-x86_64-20250202-base.iso -boot d -netdev user,id=net0 -device e1000,netdev=net0
lsblk
qemu-system-x86_64 -m 2048 -hda void.qcow2  -boot c -netdev user,id=net0,hostfwd=tcp::127.0.0.1:2112-:22 -device e1000,netdev=net0 装完以后这样启动
  # 端口转发 2112 -> 22


```




```