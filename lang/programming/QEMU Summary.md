



```

https://qemu.weilnetz.de/w64/qemu-w64-setup-20250826.exe

vi /etc/apk/repositories
community 那一行默认是注释了的

apk update
apk add git
apk add git-lfs
git lfs install



qemu-img create -f qcow2  alpine.qcow2 20G  创建虚拟磁盘
qemu-system-x86_64 -m 1024 -hda alpine.qcow2 -cdrom alpine-standard-3.22.1-x86_64.iso -boot d -netdev user,id=net0 -device e1000,netdev=net0
lsblk
qemu-system-x86_64 -m 1024 -hda alpine.qcow2  -boot c -netdev user,id=net0 -device e1000,netdev=net0 装完以后这样启动
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



