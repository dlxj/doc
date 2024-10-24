

# ISO

https://ftp.riken.jp/Linux/ubuntu-releases/20.04/



# 安装后进不去

```
启动后光标移到 *ubuntu -> 按 e 键 -> 启动参数的最后删几个字，加入 nomodeset -> ctrl + x 退出
	# 成功进入 ubuntu 
	# 装完 4090 驱动就好了
	
```



# Grub Timeout

```
vi /etc/default/grub
	# timeout 设成5
	# nomodest 好像也可以在这里设置

update-grub
	# 更新配置，它自动找到了 windows 启动项

```





# 显卡声卡

```
see huggingface\gasr\readme.txt

https://us.download.nvidia.com/XFree86/Linux-x86_64/550.100/NVIDIA-Linux-x86_64-550.100.run
	# 4090 驱动 它也自带声卡的？
	x86_64-linux-gnu-gcc-12 它一定要这个版本
	apt-get install gcc-12 g++-12 -y
		# see ubuntu summary.md -> gcc 多版本共存
	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12 --slave /usr/bin/g++ g++ /usr/bin/g++-12
	update-alternatives --config gcc
	gcc -v
	g++ -v
	./NVIDIA-Linux-x86_64-550.100.run
	nvidia-smi

https://cloud.tencent.com/developer/article/1932876
	# https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture#Installation
	# 声卡配置
	cat /proc/asound/cards
	aplay -L
	plughw:CARD=Audio,DEV=0
		USB Audio, USB Audio
    	Hardware device with all software conversions
		  # 这是 usb 回音壁？
	cd /root/huggingface/gasr/gasr-jp && 
	aplay -D plughw:CARD=Audio,DEV=0 static/60s.wav
		# 成功出声
		sudo lsof /dev/snd/*
			# 声卡被占用，kill 掉进程
		
```



## 声卡图形化配置

- https://itsfoss.com/fix-sound-ubuntu-1404/

  - ```
    alsamixer
    	# 因为默认是 HDMI 输出，所以内置扬声器没有声音
    aplay -l
    	card 2: Audio [USB Audio], device 0: USB Audio [USB Audio]
     		# 这是 usb 回音壁
    
    vi /etc/asound.conf
    	# 这文件是全局自定义的，默认不存在
    defaults.pcm.card 2
    defaults.pcm.device 0
    	# 保存重启电脑
    
    vi /usr/share/alsa/alsa.conf
    defaults.ctl.card 0
    defaults.pcm.card 0
    defaults.pcm.device 0
    	# 这个文件是存在的，上面是默认配置
    
    ```

  - 

```
声卡图形化配置
	1. 重启动电脑
	2. apt-get install pavucontrol
	3. 输入 pavucontrol
	4. 选择配置选项
```





# 设置代理

```
# see nodejs summary.md -> 抱抱脸

vi ~/.bashrc
alias setproxy="export ALL_PROXY=socks5h://172.16.6.185:1080"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"
	# curl 正常

source ~/.bashrc
	
unsetproxy && \
pip install pysocks && \
setproxy && \
ip
```





# 安装时ACPI错误

[安装时ACPI错误](https://blog.csdn.net/huohongpeng/article/details/120508304)



disable secure boot in bios
apt install --reinstall linux-headers-$(uname -r)

关闭安全启动 nvidia 驱动就正常加载了。

nvidia-smi



# 允许 root ssh

```

# ubuntu 20.04 成功
ufw disable && \
apt install openssh-server -y && \
systemctl enable --now ssh && \
systemctl status ssh

vi /etc/ssh/sshd_config

PermitRootLogin yes
PasswordAuthentication yes
PubkeyAuthentication yes
	# systemctl restart ssh
	# 改这三个重启 ssh 成功登录

sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config;
sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config;
sed -i 's/^#\?PubkeyAuthentication.*/PubkeyAuthentication yes/g' /etc/ssh/sshd_config;


mkdir -p /var/run/sshd && \
/usr/sbin/sshd -D &
	# docker 可以这样启动


docker run -tid --name gradio_server_6116 -p 222:22  -p 6116:6116 --privileged=true ubuntu:20.04 /bin/bash

docker exec -it gradio_server_6116 bash

docker cp proxychains-ng-master.zip gradio_server_6116:/root




sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

systemctl restart ssh

ufw allow ssh



https://zhuanlan.zhihu.com/p/355748937






vi /etc/ssh/sshd_config.d/01-permitrootlogin.conf
	# PermitRootLogin yes
	# 改成这个

/etc/ssh/sshd_config
	# 这文件定义了一句 Include /etc/ssh/sshd_config.d/*.conf
	# 所以可以在 /etc/ssh/sshd_config.d/ 里面自定义 xxx.conf 文件
	# PermitRootLogin yes
		# 弄成这样试试
```


# 允许 root 登录图形界面

```

https://itsfoss.com/ubuntu-login-root/

vi /etc/gdm3/custom.conf

[daemon]
AllowRoot=true
	# add this line

vi /etc/pam.d/gdm-autologin
vi /etc/pam.d/gdm-password

auth   required        pam_succeed_if.so user != root quiet_success
	# 注释掉这一行（上面两个文件都要）


```



## 4090 显卡本地 root 登录黑屏

```
root ssh 登录以后重装驱动：
Please update your xorg.conf file as    
  appropriate; see the file /usr/share/doc/NVIDIA_GLX-1.0/README.txt for details.          
  root 重装以后正常root 登录了图形界面了，但是声音出不来
 
```



# ssh 代理登录

```

see github\echodict\README.md -> AWS Lightsail

https://www.cnblogs.com/LexLuc/p/17673672.html
	# 在WSL实测nc可实现代理流量转发

chmod 600 LightsailDefaultKey-ap-southeast-1.pem

ssh -i ./LightsailDefaultKey-ap-southeast-1.pem ubuntu@54.251.144.81 -o "ProxyCommand=nc -X connect -x 172.16.6.158:5782 %h %p"
	# wsl 上运行，实测成功连上



see nodejs summary.dm -> vscode + MSYS2 +  Mingw-w64 
安装 msys2 from https://www.msys2.org/

按 win 键 -> 找到 MSYS2 MINGW64 图标 -> 运行
	pacman -S netcat
	 whereis nc
	 	-> /usr/bin/nc.exe
	pacman -S openssh
		#  ssh -i ./LightsailDefaultKey-ap-southeast-1.pem ubuntu@54.251.144.81 -o "ProxyCommand=nc -X connect -x 172.16.6.158:5782 %h %p"
		# 没用，出错

下载 ncat
	linux：https://nmap.org/ncat/
	windows：https://nmap.org/dist/ncat-portable-5.59BETA1.zip

ssh -i E:\\LightsailDefaultKey-ap-southeast-1.pem ubuntu@54.251.144.81 -o "ProxyCommand=D:\\usr\\ncat.exe --proxy 172.16.6.158:5782 %h %p"
	# powershell 执行
		-> key文件的权限不对，因为它是 windows 的文件，默认 777 ，应该是 600
	
cd E:\
icacls "LightsailDefaultKey-ap-southeast-1.pem" /remove "NT AUTHORITY\Authenticated Users"
icacls "LightsailDefaultKey-ap-southeast-1.pem" /remove "Users"
icacls "LightsailDefaultKey-ap-southeast-1.pem" /inheritance:r
icacls "LightsailDefaultKey-ap-southeast-1.pem" /grant:r "$(whoami):r"
	# powershell 执行，改变权限
	# 实测现在权限变小了，不得行

右键 -> LightsailDefaultKey-ap-southeast-1.pem -> 安全 -> 改成确保当前登录账号有完全控制权限
	ssh -i E:\\LightsailDefaultKey-ap-southeast-1.pem ubuntu@54.251.144.81 -o "ProxyCommand=D:\\usr\\ncat.exe --proxy 172.16.6.158:5782 %h %p"
	# powershell 执行
	# 成功登录！
	
C:\Users\i\.ssh
Host 54.251.144.81
  HostName 54.251.144.81
  Port 22
  User ubuntu
  IdentityFile E:\\LightsailDefaultKey-ap-southeast-1.pem
  ProxyCommand D:\\usr\\ncat.exe --proxy 172.16.6.158:5782 %h %p
	  # 实测成功连接


vi /etc/ssh/sshd_config
PermitRootLogin yes
PasswordAuthentication yes
PubkeyAuthentication yes
	# systemctl restart ssh
	# 改这三个重启 ssh 成功登录



ssh -i ./LightsailDefaultKey-ap-southeast-1.pem ubuntu@54.251.144.81 -o "ProxyCommand=/C/msys64/usr/bin/nc.exe -X connect -x 172.16.6.158:5782 %h %p"
nc: unknown option -- X
Try `/usr/bin/nc --help' for more information.
Connection closed by UNKNOWN port 65535



ProxyCommand C:\\msys64\\usr\\bin\\nc.exe -X connect -x 172.16.6.158:5782 %h %p

ProxyCommand C:\\Program\ Files\\Git\\mingw64\\bin\\connect.exe -H 172.16.6.158:5872   47.100.192.57  22
		# 实测不行

```



```
vscode 需要多加这一项
ProxyCommand [第二步下载的ncat.exe的绝对路径] --proxy-type http --proxy [代理服务器ip]:[代理服务器端口号] %h %p
```







# 安装开发环境

```

disable secure boot in bios
apt install --reinstall linux-headers-$(uname -r)

关闭安全启动 nvidia 驱动就正常加载了。

nvidia-smi

apt-get update && \
(sleep 1; echo "Y";) | apt-get install build-essential && \
(sleep 1; echo "Y";) | apt-get install p7zip-full unzip vim curl lsof git iputils-ping ufw wget net-tools git pollen libsodium-dev


git lfs clone https://huggingface.co/datasets/dlxjj/gradio

git-lfs 3.4.0         
	# 这个片本正常
	
wget https://github.com/git-lfs/git-lfs/releases/download/v3.4.0/git-lfs-linux-amd64-v3.4.0.tar.gz
	# 这样装才行
	# ok 这样设置 .gitconfig 后就正常了

curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && \
apt-get install git-lfs


vi ~/.bashrc
alias setproxy="export ALL_PROXY=socks5h://172.16.6.185:1080"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"
	# curl 正常

source ~/.bashrc

unsetproxy && \
pip install pysocks && \
setproxy && \
ip

vi ~/.condarc
proxy_servers:
  http: http://172.16.6.253:8118
  https: http://172.16.6.253:8118
ssl_verify: false
	# 康达设置代理

conda clean -a
	# 代理是OK 的，出错执行这个就可以了

ssh -CNg -L 6006:127.0.0.1:6006 root@connect.bjb1.seetacloud.com -p 53862
http://localhost:6006
	# 成功访问 gradio


https://blog.csdn.net/qq_20466211/article/details/128731196
apt-get update && \
(sleep 1; echo "Y";) | apt-get install build-essential && \
(sleep 1; echo "Y";) | apt-get install p7zip-full unzip vim curl lsof git iputils-ping ufw wget net-tools git pollen libsodium-dev && \
apt-get install -y dialog apt-utils && \
apt install -y wget net-tools build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov libsodium-dev nginx libcairo2-dev && \
apt update && apt upgrade -y && \
apt install python3.10-dev -y && \ 
apt install software-properties-common -y && \
add-apt-repository ppa:deadsnakes/ppa && \
apt install python3.10 && \
apt install python3.10-distutils && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
python3.10 get-pip.py && \
pip install --upgrade requests && \
pip install pysocks wheel && \
ufw disable

	# python3.10 的pip 需要另外安装

pip install pysocks
	# shocks 代理要先装这个

apt remove python3-apt && \
apt autoremove && \
apt autoclean && \
apt install python3-apt
	# 出错运行这个
	
20.04 的 python3.8 是不能删的
ln -s /root/mini/bin/python3.10 /usr/bin/python
	# 这样，pip 也这样 就可以了

apt update && apt upgrade -y && \
add-apt-repository ppa:ubuntuhandbook1/ffmpeg6 && \
apt update && \
apt install ffmpeg && \
ffmpeg -version && \
ffprobe -version
	# apt install ppa-purge && sudo ppa-purge ppa:ubuntuhandbook1/ffmpeg6  
	# remove



cat /etc/os-release

dnf install langpacks-en glibc-all-langpacks -y && \
localectl set-locale LANG=en_US.UTF-8 && \
localectl

vi /etc/environment
LANG=en_US.utf-8
LC_ALL=en_US.utf-8
	# 添加这两项 

source /etc/environment

cat /var/lib/pgsql/13/initdb.log

# almalinux 9
dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf install -y tar p7zip libsodium curl net-tools cronie lsof git wget yum-utils make gcc g++ clang openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel 

	# ffmpeg
dnf install epel-release -y && \
dnf config-manager --set-enabled crb && \
dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm -y && \
dnf install --nogpgcheck https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm -y

dnf install ffmpeg ffmpeg-devel && \
rpm -qi ffmpeg


# almalinux 8
dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y && \
dnf install -y python39 && \
pip3 install conan && \
dnf install -y passwd openssh-server tar p7zip tmux libsodium nmap curl net-tools cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel boost-devel systemd-devel ntfsprogs ntfs-3g nginx cronie systemtap-sdt-devel redhat-rpm-config ntfsprogs ntfs-3g

	# ffmpeg
	[How to install RPM fusion on AlmaLinux 8](https://linux.how2shout.com/how-to-install-rpm-fusion-on-almalinux-8-rocky-linux-8/)

wget https://github.com/Kitware/CMake/releases/download/v3.23.4/cmake-3.23.4.tar.gz && \
tar xvf cmake-3.23.4.tar.gz && \
cd cmake-3.23.4 && \
mkdir build && \
cd build && \
../configure --prefix=/usr/local/cmake/3.23.4 && \
make -j 4 && \
make install && \
ln -s /usr/local/cmake/3.23.4/bin/cmake /usr/bin/cmake && \
ln -s /usr/local/cmake/3.23.4/bin/cpack /usr/bin/cpack && \
ln -s /usr/local/cmake/3.23.4/bin/ctest /usr/bin/ctest


curl https://sh.rustup.rs -sSf | sh && \
source "$HOME/.cargo/env"



```



## 自动化安装

假设你要设置时区为 `America/New_York`，可以使用以下命令：

```
echo "tzdata tzdata/Areas select America" | sudo debconf-set-selections
echo "tzdata tzdata/Zones/America select New_York" | sudo debconf-set-selections
```

1. **安装软件包**：现在你可以安装软件包而不会提示选择地理区域：

也可以将其应用到其他类似的交互配置中。通用的步骤如下：

1. **找到配置项**：可以通过运行 `sudo dpkg-reconfigure ` 并查看需要的配置项。
2. **设置默认值**：使用 `debconf-set-selections` 命令来预先设置。
3. **静默安装**：使用 `-y` 选项进行静默安装。



## gcc 多版本共存

[how-to-install-latest-gcc-on-ubuntu-lts.txt](https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91)

```
These commands are based on a askubuntu answer http://askubuntu.com/a/581497
To install gcc-6 (gcc-6.1.1), I had to do more stuff as shown below.
USE THOSE COMMANDS AT YOUR OWN RISK. I SHALL NOT BE RESPONSIBLE FOR ANYTHING.
ABSOLUTELY NO WARRANTY.

If you are still reading let's carry on with the code.

sudo apt-get update && \
sudo apt-get install build-essential software-properties-common -y && \
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
sudo apt-get update && \
sudo apt-get install gcc-snapshot -y && \
sudo apt-get update && \
sudo apt-get install gcc-6 g++-6 -y && \
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6 && \
sudo apt-get install gcc-4.8 g++-4.8 -y && \
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 60 --slave /usr/bin/g++ g++ /usr/bin/g++-4.8;

When completed, you must change to the gcc you want to work with by default. Type in your terminal:
sudo update-alternatives --config gcc

To verify if it worked. Just type in your terminal
gcc -v

If everything went fine you should see gcc 6.1.1  by the time I am writing this gist

Happy coding!

See my blog post at https://www.application2000.com
```



## 链接库配置

```
Toolkit:  Installed in /usr/local/cuda-12.3/
Please make sure that
 -   PATH includes /usr/local/cuda-12.3/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-12.3/lib64, or, add /usr/local/cuda-12.3/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-12.3/bin

```



```
vi /root/.bashrc
if [ -z $LD_LIBRARY_PATH ]; then
  LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64
else
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-12.1/lib64
fi
export LD_LIBRARY_PATH

source ~/.bashrc && 
echo $LD_LIBRARY_PATH
```







## 安装 postgresql

```
dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && 
dnf -qy module disable postgresql && 
dnf -y install postgresql13 postgresql13-server postgresql13-contrib postgresql13-devel && 
/usr/pgsql-13/bin/postgresql-13-setup initdb && 
cat /var/lib/pgsql/13/initdb.log && 
ls /var/lib/pgsql/13/data/postgresql.conf

sed -i -e s/"#listen_addresses = 'localhost'"/"listen_addresses = '*'"/ -i /var/lib/pgsql/13/data/postgresql.conf  && \
cp /var/lib/pgsql/13/data/pg_hba.conf /var/lib/pgsql/13/data/pg_hba.conf_backup && \
echo "hostnossl    all          all            0.0.0.0/0  md5"  >>/var/lib/pgsql/13/data/pg_hba.conf

systemctl enable postgresql-13 && \
systemctl start postgresql-13 && \
systemctl status postgresql-13



# 改强密码
su - postgres
	psql
	\password postgres
	然后输入密码
	\q


chown -R postgres /data
	# 改拥有者

chgrp -R postgres /data
	# 改用户组

chmod -R 700 /data
	# 改文件夹权限
	# 只有自已有完全权限，其他人完全没有任何权限


psql -h 127.0.0.1 -p 5432 -U postgres
	# docker 内运行成功
	
psql -h 172.20.0.2 -p 5432 -U postgres
	# docker 内运行成功




偷梁换柱，改数据文件夹
	su - 
		# 切到 root
	
	systemctl stop postgresql-13 && \
	mkdir /data/psqldata && \
	cp -R /var/lib/pgsql/13/data /data/psqldata && \
	chown -R postgres /data && \
	chgrp -R postgres /data && \
	chmod -R 700 /data && \
	mv /var/lib/pgsql/13/data /var/lib/pgsql/13/data__link__to_data_psqldata && \
	ln -s /data/psqldata /var/lib/pgsql/13/data
		# unlink 取消软链用这个
	
	systemctl start postgresql-13
		# 成功启动 
		



恢得已备份的数据库（已弃用）
    CREATE EXTENSION IF NOT EXISTS dblink;
    DO $$
    BEGIN
    PERFORM dblink_exec('', 'CREATE DATABASE Touch WITH OWNER = postgres ENCODING = ''UTF8'' TABLESPACE = pg_default CONNECTION LIMIT = -1 TEMPLATE template0');
    EXCEPTION WHEN duplicate_database THEN RAISE NOTICE '%, skipping', SQLERRM USING ERRCODE = SQLSTATE;
    END
    $$;

		# 好像数据库名只能是小写


```



## 测速

```
wget -qO- bench.sh | bash
curl -Lso- bench.sh | bash
```





# Ubuntu22.04远程桌面

```

vi /etc/xrdp/startwm.sh


sudo /etc/init.d/xrdp start
	# 这样启动
	
apt install xfce4 xfce4-goodies -y && 
apt install xrdp -y 

选 lightdm

dpkg-reconfigure lightdm
	# 装完以后可以用这个再选一次 lightdm

vi /etc/xrdp/xrdp.ini
port=3390
	# 端口改成 3390 防止和 windows 冲突

cd ~ && 
echo "xfce4-session" | tee .xsession 

/etc/init.d/xrdp start
	# WSL2 里面不能用 systemd, 所以需要手动启动

win10 远程桌面用这个连接：

localhost:3390
	# 成功连接！
	



apt install xfce4 xfce4-goodies -y && \
apt install xrdp -y && \
systemctl enable xrdp && \
systemctl status xrdp
 
ufw disable
	# 禁用防火墙

cd ~ && \
echo "xfce4-session" | tee .xsession && \
systemctl restart xrdp 

lsof -i:3389
	# 成功


win10 上执行：
	win + r -> mstsc -> 输入vps ip, 用户名 root 
		# 成功显示远程桌面

```





# 替换成国内源

```

# ubuntu 20.04  autodl 是这个版本
cp /etc/apt/sources.list /etc/apt/sources.list__

deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

apt update
	# 有点小错误，不影响



cp -r /etc/yum.repos.d/ /etc/yum.repos.d_bak

sed -e 's|^mirrorlist=|#mirrorlist=|g' \
      -e 's|^# baseurl=https://repo.almalinux.org|baseurl=https://mirrors.aliyun.com|g' \
      -i.bak \
      /etc/yum.repos.d/almalinux*.repo
      
      
阿里云AlmaLinux镜像：https://mirrors.aliyun.com/almalinux/
腾讯云AlmaLinux镜像：https://mirrors.cloud.tencent.com/almalinux/
华为云AlmaLinux镜像：https://repo.huaweicloud.com/almalinux/
上海交大AlmaLinux镜像：https://mirror.sjtu.edu.cn/almalinux/
西安交大AlmaLinux镜像：https://mirrors.xjtu.edu.cn/archlinux/
浙江大学AlmaLinux镜像：https://mirrors.zju.edu.cn/almalinux/
南京大学大AlmaLinux镜像：https://mirrors.nju.edu.cn/almalinux/
兰州大学almalinux镜像：https://mirror.lzu.edu.cn/almalinux/
大连东软almalinux镜像：https://mirrors.neusoft.edu.cn/almalinux/

```







# 关闭防火墙



```

ufw disable && \
apt install openssh-server -y && \
systemctl enable --now ssh && \
systemctl status ssh




systemctl disable firewalld
	# 永久关闭

yum install nmap
	# 扫描指定端口是否开放	
	nmap 118.178.137.176 -p222
		PORT    STATE  SERVICE
		222/tcp closed rsh-spx	
			# 端口并没有开放

	netstat -aptn | grep -i 222
		tcp        0      0 0.0.0.0:222             0.0.0.0:*               LISTEN      45594/conmon
			# 好像本地 222 端口是开放了的

	lsof -i:222
		conmon  45594 root    5u  IPv4 446985      0t0  TCP *:rsh-spx (LISTEN)
			# 也是显示开放了


	https://blog.csdn.net/qq_39176597/article/details/111939051
		# linux关闭防火墙了，但端口还是访问不了

		systemctl  start  firewalld
			# 启动防火墙
			systemctl  status  firewalld

		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=6006/tcp --permanent
			# 开放端口
	
		firewall-cmd --reload
			# 重新加载配置文件
		
		firewall-cmd --list-ports
			# 查看已经开放的端口
```



# 配置静态 IP



## IPv4

```
# インストール時にホスト名を設定していない場合は設定
[root@localhost ~]# hostnamectl set-hostname dlp.srv.world
# デバイス確認
[root@localhost ~]# nmcli device
DEVICE  TYPE      STATE      CONNECTION
enp1s0  ethernet  connected  enp1s0
lo      loopback  unmanaged  --

# 固定 IPv4 アドレス設定
[root@localhost ~]# nmcli connection modify enp1s0 ipv4.addresses 10.0.0.30/24
# ゲートウェイ設定
[root@localhost ~]# nmcli connection modify enp1s0 ipv4.gateway 10.0.0.1
# 参照する DNS 設定
# 複数設定する場合はスペース区切り ⇒ ipv4.dns "10.0.0.10 10.0.0.11 10.0.0.12"
[root@localhost ~]# nmcli connection modify enp1s0 ipv4.dns 10.0.0.10
# DNS サーチベース 設定 (自身のドメイン名 - 複数設定する場合はスペース区切り)
[root@localhost ~]# nmcli connection modify enp1s0 ipv4.dns-search srv.world
# IP アドレス固定割り当てに設定 (DHCP は [auto])
[root@localhost ~]# nmcli connection modify enp1s0 ipv4.method manual
# インターフェースを再起動して設定を反映
[root@localhost ~]# nmcli connection down enp1s0; nmcli connection up enp1s0
Connection 'enp1s0' successfully deactivated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/1)
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/2)

# 設定確認
[root@localhost ~]# nmcli device show enp1s0
GENERAL.DEVICE:                         enp1s0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         52:54:00:DF:87:AD
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     enp1s0
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveC>
WIRED-PROPERTIES.CARRIER:               on
IP4.ADDRESS[1]:                         10.0.0.30/24
IP4.GATEWAY:                            10.0.0.1
IP4.ROUTE[1]:                           dst = 10.0.0.0/24, nh = 0.0.0.0, mt = 1>
IP4.ROUTE[2]:                           dst = 0.0.0.0/0, nh = 10.0.0.1, mt = 100
IP4.DNS[1]:                             10.0.0.10
IP4.SEARCHES[1]:                        srv.world
IP6.ADDRESS[1]:                         fe80::5054:ff:fedf:87ad/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = fe80::/64, nh = ::, mt = 100
```



## IPV6

```
# IPv6 無効化
[root@localhost ~]# grubby --update-kernel ALL --args ipv6.disable=1
# 確認
[root@localhost ~]# grubby --info DEFAULT
index=0 kernel="/boot/vmlinuz-5.14.0-17.el9.x86_64" args="ro crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M resume=/dev/mapper/cs-swap rd.lvm.lv=cs/root rd.lvm.lv=cs/swap console=ttyS0,115200n8 selinux=0 ipv6.disable=1" root="/dev/mapper/cs-root" initrd="/boot/initramfs-5.14.0-17.el9.x86_64.img" title="CentOS Stream (5.14.0-17.el9.x86_64) 9" id="ab414d4792d04b9dbc1e2361f936e849-5.14.0-17.el9.x86_64"
[root@localhost ~]# reboot
[root@localhost ~]# ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 52:54:00:df:87:ad brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.30/24 brd 10.0.0.255 scope global noprefixroute enp1s0
       valid_lft forever preferred_lft forever

# IPv6 有効に戻す場合は以下 (変更後は要再起動)
[root@localhost ~]# grubby --update-kernel ALL --remove-args ipv6.disable
```







```
二、设置IP地址、网关、DNS

说明：AlmaLinux-9.x默认安装好之后启用DHCP自动获取ip地址，我们修改为静态ip

#AlmaLinux-9.x放弃了之前的网络配置目录/etc/sysconfig/network-scripts/，采用新的存储目录

#进入网络配置文件目录

cd /etc/NetworkManager/system-connections

vi /etc/NetworkManager/system-connections/ens160.nmconnection

[connection]

id=ens160

uuid=cbc0db63-c2bb-339e-86d8-46bd89c7ad59

type=ethernet

autoconnect-priority=-999

interface-name=ens160

timestamp=1654435924

[ethernet]

[ipv4]

address1=192.168.21.91/24,192.168.21.2

dns=8.8.8.8;8.8.4.4;

method=manual

[ipv6]

addr-gen-mode=eui64

method=auto

[proxy]

:wq! #保存退出

nmcli n off && nmcli n on #重启网络

ip addr #用修改后的ip登录系统，查看ip地址

相关网络命令

ip link 显示网络设备的运行状态

ip -s link 显示更详细的设备信息

ip link show dev ens160 仅显示ens160的信息

ip link show up 仅显示处于激活状态的设备

ip link set ens160 down down掉ens160

ip link set ens160 up 激活ens160

nmcli device status 显示设备状态

nmcli device show 显示全部网络接口属性

nmcli device show ens160 显示ens160网络接口属性

nmcli device connect ens160 激活网卡

nmcli device disconnect ens160 停用网卡

nmcli connection down ens160 down掉ens33设备

nmcli connection up ens160 启用ens33设备

nmcli con reload 重新加载网卡

nmcli con add help 可以查看帮助

三、设置主机名为www

hostnamectl set-hostname www #设置主机名为www

vi /etc/hostname #编辑配置文件

www #修改localhost.localdomain为www

:wq! #保存退出

vi /etc/hosts #编辑配置文件

127.0.0.1 localhost www #修改localhost.localdomain为www

:wq! #保存退出
```





## aws 光帆 IPV6

https://docs.aws.amazon.com/zh_cn/lightsail/latest/userguide/amazon-lightsail-configure-ipv6-on-ubuntu-16.html

https://candinya.com/posts/ipv6-configure-for-buyvm/  buyvm ipv6 配置

https://cyp0633.icu/post/add-ipv6-on-ubuntu-22.04/  干货



```
https://lightsail.aws.amazon.com/ls/webapp/home/instances

18.176.53.159

sixxxy@gmail.com pwd同 QQ

https://test-ipv6.com/

ip addr

inet6 xxx scope link
	# scope global 才行！

ip a
vi /etc/netplan/50-cloud-init.yaml
network:
    ethernets:
        ens5:
            dhcp4: true
            dhcp6: true
            match:
                macaddress: 06:4a:41:cd:ad:ef
            set-name: ens5
    version: 2

sudo netplan apply && 
sudo systemctl restart systemd-networkd && 
ping6 google.com
	# 成功 ping 通

ping -6 google.com
	# windows 这样 ping ipv6


.77
	$ ip a
    inet 209.141.34.77/24 brd 209.141.34.255 scope global dynamic eth0
       valid_lft 2591979sec preferred_lft 2591979sec
    inet6 fe80::216:f4ff:fee0:bcc/64 scope link 

ipv4
IP
209.141.34.77
Netmask
255.255.255.0
Gateway
209.141.34.1
Resolver1
205.185.112.68
Resolver2
205.185.112.69


控制面板的设置
Ip
2605:6400:20:105a:4914:4f4d:6555:1577
Netmask
48
Gateway
2605:6400:20::1

        address 2605:6400:20:105a:4914:4f4d:6555:1577
        netmask 48
        gateway 2605:6400:20::1

vi /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      dhcp6: true


改为：
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      dhcp6: true
	  gateway4: 209.141.34.1
      gateway6: 2605:6400:20::1
      addresses: [209.141.34.77/24,'2605:6400:20:105a:4914:4f4d:6555:1577/48']

如果你的 Netmask 也是 255.255.255.0，那么 / 24 就不需要变动，它们的意义相同，只是一个 Netmask 和 Bitmask 的相互转换，前者是 IPv4 惯用表述，后者则是 IPv6 的表述。Netplan 统一用后者。


sudo netplan try
	# 检查配置

sudo netplan apply
	# 应用更改
	
networkctl status eth0
	# 网卡 eth0 状态
	# 绿色的 routable(configured) 表示一切正常

ping6 google.com
	# 成功 ping 通

ping6 2605:6400:20:105a:4914:4f4d:6555:1577
	# 光帆成功 ping 通 .77 的 ipv6
	# ping -6 2605:6400:20:105a:4914:4f4d:6555:1577
		# windows 成功 ping 通 .77 （开代理才行！）

ping6 2406:da14:12f1:1a00:5a6d:b685:3659:5b64
	# .77 成功 ping 通光帆的 ipv6
	# ping -6 2406:da14:12f1:1a00:5a6d:b685:3659:5b64
		# windows 成功 ping 通光帆 （开代理才行！）

ipv6.msftconnecttest.com/connecttest.txt
	# 确保能访问

使用 networkctl status eth0 命令查看 eth0 端口情况。除了查看 Address 信息有没有错误之外，最重要的是 State。如果是绿色的 routable(configured)，那么一切正常。否则，degraded 表示可能没有连接公网，而若下方 log 中提示 No Route to Host 则可能代表 Gateway 设置错误。

这之后，可以使用 ping6 google.com 测试一下 IPv6 下的网络连接。也可以用其他设备 Ping 你刚刚分配的 IPv6 地址。如果都不会提示 Network Unreachable，那么就万事大吉了


```



AWS Lightsail 光帆 3.5$ 每月

目前靠谱的就是 hyestria+端口跳跃，Xray-vision ，有闲心也可以上 naiveproxy 。

前两个可以用 mack-a 的一键脚本，谷歌一下就有。



Hysteria科学上网

https://mephisto.cc/tech/hysteria/



# DNS

```
vi /etc/systemd/resolved.conf
[Resolve]
DNS=1.1.1.1

rm -f /etc/resolv.conf && 
ln -sv /run/systemd/resolve/resolv.conf /etc/resolv.conf && 
service systemd-resolved restart

ping qq.com

	# 实测问题解决

```





# socks5 转 http

```
# https://maplege.github.io/2017/09/04/socksTOhttp/
	# socks转为http代理
	apt update && apt-get install privoxy
	vi /etc/privoxy/config
	forward-socks5   /               172.16.6.253:1080 .
	listen-address 0.0.0.0:1080
    service privoxy restart
    http_proxy=http://127.0.0.1:1080 curl google.com
    	# 成功访问 google
```





# 远程桌面

[Xrdp with GNOME_GUI on AlmaLinux_8](https://wiki.crowncloud.net/?How_to_Install_Xrdp_with_GNOME_GUI_on_AlmaLinux_8)

```
yum groupinstall -y "Server with GUI" && \ 
systemctl set-default graphical && \
dnf install epel-release && \
rpm -qi epel-release && \
dnf --enablerepo=epel group

wget https://rpmfind.net/linux/epel/testing/8/Everything/x86_64/Packages/x/xrdp-0.9.22-5.el8.x86_64.rpm
	# 失效了

wget https://rpmfind.net/linux/epel/8/Everything/x86_64/Packages/x/xrdp-0.9.22.1-2.el8.x86_64.rpm

dnf install -y ./xrdp-0.9.22.1-2.el8.x86_64.rpm
	# 装完就可以成功用 windows 远程登录了

	
dnf install -y xrdp && \
systemctl start xrdp && \
systemctl enable xrdp

nmap 127.0.0.1  -p 3389
	# 3389/tcp open  ms-wbt-server  端口是开着的 
	# 再用外网地址测一次

firewall-cmd --permanent --add-port=3389/tcp && \
firewall-cmd --reload

reboot

```





```

# fail

dnf install -y epel-release && \
rpm -qi epel-release && \
dnf --enablerepo=epel group && \
dnf group list | grep -i xfce && \
dnf groupinstall "Xfce" "base-x"


echo "exec /usr/bin/xfce4-session" >> ~/.xinitrc && \
systemctl set-default graphical && \
systemctl get-default


dnf install xrdp && \
systemctl start xrdp && \
systemctl enable xrdp && \
systemctl status xrdp



reboot




```



## xfce4

```
dnf install epel-release && \
rpm -qi epel-release && \
dnf --enablerepo=epel group && \
dnf group list | grep -i xfce && \
dnf groupinstall -y "Xfce" "base-x" && \
echo "exec /usr/bin/xfce4-session" >> ~/.xinitrc && \
systemctl set-default graphical && \
dnf install -y xrdp && \
systemctl start xrdp && \
systemctl enable xrdp && \
systemctl status xrdp && \
systemctl disable firewalld

reboot

systemctl stop firewalld
	# 关掉防火墙以后成功用 windows 远程桌面登录
systemctl disable firewalld
	# 永久关闭防火墙


```



# nginx

```
see echodict/README.md -> ali 57

apt install nginx && 
/etc/init.d/nginx start

ali 服务端反代 windows 3389 远程桌面
vi /etc/nginx/nginx.conf
stream {
    upstream windows_33899 {
        server 10.0.0.3:3389; 
    }

    server {
        listen 33899;
        proxy_pass windows_33899;
    }
}
	# 加在配置的最后
	
nginx -t
nginx -s reload
/etc/init.d/nginx status

win11 远程桌面，连 10.0.0.1:33899 成功
```





# NTFS

```

sudo ntfsfix /dev/sda1
	# 解决因为休眠造成的问题
umount -lf /mnt
mount -t ntfs-3g /dev/sda1 /mnt


# 硬盘扩容
ls /dev/disk/by-id/
	--> ata-QEMU_DVD-ROM_QM00004  scsi-0BUYVM_SLAB_VOLUME-7514
		# scsi-0BUYVM_SLAB_VOLUME-7514 是新增的512G

fdisk -l
	# 看到新硬盘是sda

# 分区
# https://www.daniao.org/9632.html
fdisk /dev/sda



# 格式化
mkfs.ext4 -F /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-7514

	============   后来的方案，让linux 适应windows 的分区 =======================
	# yum install ntfsprogs
	# fdisk /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-7514
	# 这里用fdisk 分好区
	# mkfs.ntfs --fast -F /dev/sda1
		# 因为windows 不知为什么不识别ext4 分区了，只能让linux 去识别ntfs 分区

	# mount -t ntfs-3g /dev/sda1 /mnt
	# df -T
		# /dev/sda1           fuseblk  536867836  104168 536763668   1% /mnt
	
	# 开机自动挂
	# echo '/dev/sda1 /mnt/ ntfs-3g defaults 0 0' | sudo tee -a /etc/fstab
	# 注意：linux 分出来的ntfs 分区并不能被windows 识别，所以还是用windows 格式化吧，然后linux 装ntfsprogs，和ntfs-3g 挂载
	
 ------------->  mount 出来的ntfs分区全部是 root 权限，psql 读不了   <---------------------
	Thanks, I solved mounting the disk on fstab with this options: UUID=XXXXXXX   /mnt/shared ntfs-3g defaults,noatime,uid=1000,gid=users,dmask=022,fmask=133  0   0 
	
	
	id -u postgres  # 用户ID
	26
	id -g postgres  # 用户组ID
	26
	
	mount -o uid=26,gid=26,dmask=077,fmask=077 -t ntfs-3g /dev/sda1 /mnt
		# 成功挂载，而且权限是对的
			# 设成077 以后就没错了，它要求只有自已有完全权限，其他人完全没有任何权限
		# 更新：仅限不对导至psql 启动失败
			# Permissions should be u=rwx (0700) or u=rwx,g=rx (0750).  他希望的权限是这个
		https://superuser.com/questions/1271534/file-permissions-correct-ntfs-mount-option
			fmask=133 sets files permissions to 644
		
		https://www.nixonli.com/22806.html
			实际权限 = 777 - mask
				644 = 777 - 133
				700 = 777 - 077
				755 = 777 - 022

	
	echo '/dev/sda1 /mnt ntfs-3g defaults,noatime,uid=26,gid=26,dmask=022,fmask=133 0 0' | sudo tee -a /etc/fstab
	# 成功开机自动挂载
	
	
	Windows and Linux have a very different user and permissions model that is incompatible. For either chmod or chown to work, the file system needs to support users and permissions in a Linux-like way. NTFS is a Windows file system and so these commands can't possibly work.

One thing you can do is to mount the NTFS partition specifying a different user and mode for all of the files / directories:

mount -o uid=26,gid=26,dmask=022,fmask=133 /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-7514 /mnt 
This will mount with specified user and group giving directories mode 755 and files mode 644.



    ======================================================================



# 挂载
mkdir /data
mount -o discard,defaults /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-7514 /data
# 开机自动挂
echo '/dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-7514 /data ext4 defaults,nofail,discard 0 0' | sudo tee -a /etc/fstab



# chrome for windows 2012
https://www.google.com/intl/en/chrome/?standalone=1
# 磁盘管理
https://hostloc.com/thread-830521-1-1.html
	diskmgmt.msc
```



# auto mount

```
vi /yxxx/script/auto_mount2.sh
umount /yxxx/204_shared
mount -t nfs 172.16.7.204:/home/shared /yxxx/204_shared
if [ $? -ne 0 ]; then
    echo "mount failed..."
    sleep 30s; echo "try agin..."
    umount /yxxx/204_shared
    mount -t nfs 172.16.7.204:/home/shared /yxxx/204_shared
else
    echo "mount succeed!!!"
fi

@reboot  /yxxx/script/auto_mount2.sh
	# crontab

apt-get install cron




```







# 安装双系统

先装 windows server 2022, 再装 AlmaLinux8.8, 重启自动进入 linux

```
dnf install ntfs-3g
	# 以下操作必须要能识别 ntfs 分区才行

fdisk -l
Device     Boot     Start       End   Sectors  Size Id Type
/dev/vda1  *         2048    718847    716800  350M  7 HPFS/NTFS/exFAT
/dev/vda2          718848 115340927 114622080 54.7G  7 HPFS/NTFS/exFAT
/dev/vda3       115341312 117438463   2097152    1G 83 Linux
/dev/vda4       117438464 167772159  50333696   24G  5 Extended
/dev/vda5       117440512 167772159  50331648   24G 8e Linux LVM

ls /etc/grub.d/40_custom
	# 存在

vi  /etc/grub.d/40_custom # 加在最后
menuentry "Windows Server 2016" {
	set root=(hd0,1)
	chainloader +1
}

grub2-mkconfig --output=/boot/grub2/grub.cfg
	--> Found Windows Recovery Environment on /dev/vda1
	# 成功识别	

reboot

重启就看到Windows Server 2022 了

```



- `hd0` 表示系统中的第一块硬盘。如果你有多块硬盘，第二块硬盘会被编号为 `hd1`，第三块硬盘会被编号为 `hd2`，以此类推。

- `,1` 表示硬盘上的第一个分区。如果一个硬盘上有多个分区，第二个分区会被编号为 `,2`，第三个分区会被编号为 `,3`，以此类推。



# Install Chrome

```

apt install fonts-liberation libu2f-udev && 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&
dpkg -i google-chrome-stable_current_amd64.deb &&
apt --fix-broken install

 snap remove chromium
 	# 卸载

cd /usr/share/applications/ &&
cp google-chrome.desktop ~/Desktop/
	# 手动添加快捷方式 ？


git config --global core.autocrlf ture

wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
wget https://dl.google.com/linux/linux_signing_key.pub && \
rpm --import linux_signing_key.pub && \
dnf install -y google-chrome-stable_current_x86_64.rpm

google-chrome &
	# 注意：chrome 需要非 root 账号运行
	useradd i
	passwd i
		# 密码设置成和 root 一样

vi /usr/bin/google-chrome

最后一行加：
--user-data-dir --test-type --no-sandbox

改完后：

exec -a "$0" "$HERE/chrome" "$@" --user-data-dir --test-type --no-sandbox

	# root 成功运行 chrome

```



# Install vscode

[how-to-install-visual-studio-code-on-almalinux](https://www.linuxcapable.com/how-to-install-visual-studio-code-on-almalinux/)



```
vi /usr/bin/code

CAN_LAUNCH_AS_ROOT=1
	# 报错的前一句加这行
	
ELECTRON_RUN_AS_NODE=1 "$ELECTRON" "$CLI" "$@" --user-data-dir --no-sandbox
	# 最后一行改成这样



see python summary -> Gradio -> svelte -> vite

# vscode 设置 -> 搜:
allowBreakpointsEverywhere

vscdoe 插件
	JavaScript Debugger
	Svelte for VS Code

.vscode/launch.json  
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "chrome",
            "request": "launch",
            "name": "Launch Chrome against localhost",
            "url": "http://localhost:5174",
            "webRoot": "${workspaceFolder}"
        }
    ]
}
	# 正常进断点需要这个

pnpm create vite vite-svelte -- --template svelte
cd vite-svelte
pnpm install
pnpm run dev
    # vite 有几个选项，选 svelte ，选 javascript
	# vsocde 里 F5 能正常在 Counter.svelte 单步断下


gradio cc create ivideo --template Video
	# 自定义gradio 的 video 组件
	#　把 frontend 下　node_modules shared　这两个文件夹复到 vite_gradio_video 目录下，能正常引用，并运行
        # 把 dependencies 下的包复制过来， pnpm i 就可以了 


App.svelte
<script>
  import Counter from './lib/Counter.svelte'
  import Player from '../shared/Player.svelte';
	# 这样引用组件





```


# Input pinyin

```

apt-get install -y fcitx im-config
im-config ## choose fcitx

apt-get install fcitx-googlepinyin

## choose fcitx keyboard icon, choose "Text Entry Setting"
## in the opned windows, click "+" icon
## search "pinyin" and Google Pinin" will come out

## if cannot not be used immediately, log out once

```



# install candy



apt-get --fix-broken install ./candy_5.6+ubuntu22.04_amd64.deb



# mecab

[MeCab+NEologd](https://qiita.com/heimaru1231/items/1f4f03088bc0f6bdefc6)

- [groonga fulltext search](https://github.com/groonga/groonga/issues/1521)

```
cat /etc/redhat-release && \
dnf -y install --nogpgcheck https://packages.groonga.org/almalinux/8/x86_64/Packages/groonga-release-2021.10.30-1.noarch.rpm && \
dnf -y makecache && \
dnf -y install mecab mecab-ipadic mecab-devel patch --nogpgcheck && \
mecab -v 

git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
cd mecab-ipadic-neologd && \
./bin/install-mecab-ipadic-neologd -n -a
	# 其间要输入一个 "yes"	
	# dic is here: /usr/lib64/mecab/dic/mecab-ipadic-neologd
	# https://phoenixnap.dl.sourceforge.net/project/mecab/mecab-ipadic/2.7.0-20070801/mecab-ipadic-2.7.0-20070801.tar.gz
	# 下载 csv 词典原始数据，它的编码是 EUC-JP

mecab -d /usr/lib64/mecab/dic/mecab-ipadic-neologd


import MeCab
import subprocess

cmd='echo `mecab-config --dicdir`"/mecab-ipadic-neologd"'
path = (subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True).communicate()[0]).decode('utf-8')
m=MeCab.Tagger("-d {0}".format(path))
print(m.parse("彼女はペンパイナッポーアッポーペンと恋ダンスを踊った。"))


```





# 乱码

https://juejin.cn/post/7320102376175501322

- ```
  # see huggingface/Sakura_Launcher_GUI/readme.txt
  # wsl2 ubuntu22.04 执行
  mkdir -p /usr/share/fonts/windows11 && 
  cp -rf /mnt/c/Windows/Fonts/* /usr/share/fonts/windows11 && 
  /usr/share/fonts/windows11/
  	# 实测解决问题
  	
  设置 Ubuntu 中文语言环境
  
  安装中文语言包
  
  bash 代码解读复制代码sudo apt install language-pack-zh-han*
  
  
  运行语言支持检查
  
  bash 代码解读复制代码sudo apt install $(check-language-support)
  
  
  修改相关配置文件（两种方法）
  
  方法 1：
  bash 代码解读复制代码sudo vim /etc/default/locale
  
  替换原始内容如下：
  bash 代码解读复制代码LANG="zh_CN.UTF-8"
  LANGUAGE="zh_CN:zh"
  LC_NUMERIC="zh_CN"
  LC_TIME="zh_CN"
  LC_MONETARY="zh_CN"
  LC_PAPER="zh_CN"
  LC_NAME="zh_CN"
  LC_ADDRESS="zh_CN"
  LC_TELEPHONE="zh_CN"
  LC_MEASUREMENT="zh_CN"
  LC_IDENTIFICATION="zh_CN"
  LC_ALL="zh_CN.UTF-8"
  
  方法 2：
  通过图形界面修改上述文件中的 LANG 字段。
  bash 代码解读复制代码sudo dpkg-reconfigure locales
  
  使用空格键选择 en_US.UTF-8 以及 zh_CN.UTF-8，使用 TAB 键切换至 OK，再将 en_US.UTF-8 选为默认（此处选择 zh_CN.UTF-8 及修改上述文件中的 LANG 字段）。
  然后重启 WSL2
  
  修改环境变量
  添加 LANG=zh_CN.UTF-8 到配置文件末尾。有两种做法，仅供参考。
  
  bash 代码解读复制代码echo "LANG=zh_CN.UTF-8" >> ~/.profile
  
  bash 代码解读复制代码echo "LANG=zh_CN.UTF-8" >> /etc/profile
  
  WSL2 无内容显示无法操作
  折腾的途中遇到 WSL2 只有光标闪烁，无内容显示也无法操作，wsl --shutdown wsl -l -v 等等指令都没有效果。
  解决方法：
  在启动或关闭Windows功能中，关掉适用于Linux的Windows子系统，再重新打开。重启后一切恢复正常
  
  
  ```

  

https://blog.csdn.net/weixin_39246554/article/details/123487843

see huggingface/Sakura_Launcher_GUI/readme.txt  **没解决**

```
sudo apt-get install language-pack-zh-hans



dnf install langpacks-en glibc-all-langpacks -y && \
localectl set-locale LANG=en_US.UTF-8 && \
localectl

vi /etc/environment
LANG=en_US.utf-8
LC_ALL=en_US.utf-8
	# 添加这两项 

source /etc/environment

vi /etc/profile.d/utf8.sh 
export LANG="en_US.utf-8"
export LC_ALL="en_US.utf-8"
export LANGUAGE="en_US"




see dlxj's RedisAll github

git clone --recursive https://github.com/RedisJSON/RedisJSON.git && \
cd RedisJSON && \
./sbin/setup

	vi /etc/profile.d/utf8.sh
		# 好像是这个把 utf8 环境搞坏的 
export LANG="en_US.utf-8"
export LC_ALL="en_US.utf-8"
export LANGUAGE="en_US"
			# 内容一定要先改成这样

```



