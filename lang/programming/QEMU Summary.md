

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





# 阿里云安装 alpine

https://josephcz.xyz/technology/linux/install-alpine-on-aliyun/



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

2. **安装更多字体支持**：
   ```bash
   apk add --no-cache font-noto font-noto-cjk font-noto-emoji
   ```LAiL

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



```



# Docker + alpine

https://wener.me/notes/os/alpine/glibc

https://zhuanlan.zhihu.com/p/689702275

```

apk del gcompat libc6-compat
apk add glibc-2.35-r1.apk glibc-bin-2.35-r1.apk glibc-dev-2.35-r1.apk --allow-untrust --force-overwrite
	# 关键




yum install -y yum-utils device-mapper-persistent-data lvm2

yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

yum install docker-ce

systemctl start docker

systemctl enable docker

docker version

docker ps

docker images


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



