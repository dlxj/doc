

docker exec -it centos7PG10 /bin/bash



```
docker ps -a
docker rm xxx
docker images
docker rmi xxxx
exit  (quit)
CTRL + P + Q (quit)
docker inspect container_name | grep IPAddress
  --> 172.18.0.3
# 需要更多IP 时
iptables -t nat -A  DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22

iptables -t nat -A  DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22
```



```
# 查看规则
iptables -L 
```







docker ps -a  # 全部状态都列出来，强大一些

docker start centos7



# 移除镜像

docker images

docker rmi xxx



# 移除容器

docker stop 17b3d18c1428

docker rm 17b3d18c1428









docker pull centos:7

docker run -it --rm centos:7 bash

```
# 特权模式创建容器
docker run -tid --name centos7 -p 222:22 --privileged=true centos:7 /sbin/init 
		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口
# 运行
docker exec -it centos7 /bin/bash
# 安装ssh
yum install openssh-server -y
# 修改配置
vi /etc/ssh/sshd_config
PermitRootLogin yes # 改成这个
UsePAM no # 改成这个
# 启动ssh
systemctl start sshd
# 退出容器
eixt

# 查看容器的IP
docker inspect centos7 | grep IPAddress
  --> "IPAddress": "172.18.0.3"

# 登录看看
ssh root@172.18.0.3
  --> 成功






```

https://plutoacharon.github.io/2020/02/23/Docker%E5%AE%B9%E5%99%A8%E5%87%BA%E7%8E%B0%E4%BD%BF%E7%94%A8systemctl%E9%97%AE%E9%A2%98%EF%BC%9AFailed-to-get-D-Bus-connection-Operation-not-permitted/




# 如果需要更多的端口映射

```
# https://blog.opensvc.net/yun-xing-zhong-de-dockerrong-qi/

# 已有端口映射
iptables -t nat -vnL DOCKER
  --> tcp dpt:8083 to:172.18.0.2:8083
  --> tcp dpt:54322 to:172.18.0.3:5432

# 这种方法每次docker 重启会失效
iptables -t nat -A DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.17.0.3:22

```



1、获得容器IP
将container_name 换成实际环境中的容器名
docker inspect `container_name` | grep IPAddress

2、iptable转发端口
将宿主机的8888端口映射到IP为192.168.1.15容器的8080端口
iptables -t nat -A  DOCKER -p tcp --dport 8888 -j DNAT --to-destination 192.168.1.15:8080



一、添加docker容器端口映射
以tomcat容器为例：

root@localhost /]# docker run --name mytomcat -d -p 8888:8080 tomcat
1
–name：创建的tomcat镜像名称
‐d：后台运行
‐p：将主机的端口映射到容器的一个端口，8888:8080代表：主机端口:容器内部的端口

执行完会返回新创建的tomcat镜像ID





# Docker 中的postgreql



```
# 特权模式创建容器
docker run -tid --name centos7PG10 -p 54322:5432 --privileged=true centos:7 /sbin/init 
		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口

# 运行docker 的shell
docker exec -it centos7PG10 /bin/bash

# 安装PG13
yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

yum -y update
yum search postgresql13
yum -y install postgresql13 postgresql13-server
/usr/pgsql-13/bin/postgresql-13-setup initdb
systemctl start postgresql-13
systemctl status postgresql-13
systemctl enable postgresql-13 # 自启动

# 改强密码
su - postgres
psql -c "alter user postgres with password '这里填的一个强密码'"
# 允许运程连接
vi /var/lib/pgsql/13/data/postgresql.conf
	listen_addresses = '*' # 改成这个
vi /var/lib/pgsql/13/data/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  trust  
	# 加在最后面，接受所有远程IP

systemctl restart postgresql-13

# docker 连接测试
psql -h 127.0.0.1 -p 5432 -U postgres  # 注意端口
  --> 成功
# 宿主连接测试
psql -h 127.0.0.1 -p 54322 -U postgres # 注意端口
  --> 成功
  
```

<img src="postgresql summary.assets/image-20210330185047454.png" alt="image-20210330185047454" style="zoom:50%;" />

**navicat 连接**



# docker 退出方法

```
docker 退出方法
	# kill -9  $(jobs -p)
	# exit

# centos8 没有软件源
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo

sed -i -e"s|mirrors.cloud.aliyuncs.com|mirrors.aliyun.com|g " /etc/yum.repos.d/CentOS-*

sed -i -e "s|releasever|releasever-stream|g" /etc/yum.repos.d/CentOS-*

yum clean all && yum makecache

yum update --allowerasing
```



# docker-compose

see nodejs summary.md  -> 范畴论 -> Python Monads

[dejavu audio match](https://github.com/worldveil/dejavu) 宝藏

- ```
  proxychains4 docker-compose build
  
  ```



# Docker 走代理

https://note.qidong.name/2020/05/docker-proxy/

```

在执行docker pull时，是由守护进程dockerd来执行。 因此，代理需要配在dockerd的环境中。 而这个环境，则是受systemd所管控，因此实际是systemd的配置。

mkdir -p /etc/systemd/system/docker.service.d && \
touch /etc/systemd/system/docker.service.d/proxy.conf

在这个proxy.conf文件（可以是任意*.conf的形式）中，添加以下内容：

vi /etc/systemd/system/docker.service.d/proxy.conf
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:8118/"
Environment="HTTPS_PROXY=http://127.0.0.1:8118/"
Environment="NO_PROXY=localhost,127.0.0.1,.example.com"



mkdir ~/.docker && \
touch ~/.docker/config.json

vi ~/.docker/config.json
{
        "auths": {},
        "HttpHeaders": {
                "User-Agent": "Docker-Client/19.03.2 (linux)"
        },

                "proxies":
                {
                        "default":
                        {
                        "httpProxy": "http://127.0.0.1:8118",
                        "httpsProxy": "http://127.0.0.1:8118"
                        }
                }
}

systemctl restart docker && \
systemctl status docker



```



# windows server 2022

```
# windows server 2022

cd "C:\Program Files\Docker\Docker\"

& '.\Docker Desktop Installer.exe'
	# 启动失败
	empty package
   at Docker.Installer.InstallWorkflow.<DoProcessAsync>d__23.MoveNext()

"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control"
ServicesPipeTimeout=dword:0000ea60


Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
	# 安装 chco

choco
	# 成功执行

choco install docker-desktop --upgrade --force
	# 强制更新 docker
	# 重启系统，运行前面的命令虽然还弹错，但是可以启动不闪退了
	
```








# AlmaLinux9

```
docker image rm almalinux:9.3
docker pull almalinux:9.3

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

[System.Text.Encoding]::UTF8.GetBytes('FROM almalinux:9.3
RUN set -x; dnf makecache --refresh && \
dnf update -y && dnf upgrade -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf install -y tar p7zip libsodium net-tools cronie lsof git wget yum-utils make gcc g++ clang openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel && \
dnf install epel-release -y && \
dnf config-manager --set-enabled crb && \
dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm -y && \
dnf install --nogpgcheck https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm -y && \
dnf install ffmpeg ffmpeg-devel -y && \
pwd ') | Set-Content Dockerfile -Encoding Byte


docker build -t almalinux9_server_6006 .
docker run -tid --name almalinux9_server_6006 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5432:5432 -p 6379:6379 -p 8880:8880 -p 8080:8080 --privileged=true almalinux9_server_6006 /sbin/init


```






# AlmaLinux8



```
New-Item -ItemType Directory -Path AlmaLinux8_server_8880
cd AlmaLinux8_server_8880
New-Item -ItemType File -Path Dockerfile

docker stop almalinux8_server_8880 && \
docker rm almalinux8_server_8880
docker image rm almalinux:8.7
docker network rm customnetwork

$t = $(docker image ls) -like "*almalinux*8.7*"
if (-not $t)
{
    Write-Host 'almalinux:8.7 not found, pull'
    docker pull almalinux:8.7
    Write-Host 'almalinux:8.7 pull success'
}

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

[System.Text.Encoding]::UTF8.GetBytes("FROM almalinux:8.7
RUN set -x; dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y && \
dnf install -y python39 && \
pip3 install conan && \
dnf install -y passwd openssh-server tar p7zip libsodium curl net-tools firewalld cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel boost-devel systemd-devel ntfsprogs ntfs-3g nginx cronie && \
pwd ") | Set-Content Dockerfile -Encoding Byte

docker build -t almalinux8_server_8880 .
docker run -tid --name almalinux8_server_8880 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5432:5432 -p 6379:6379 -p 8880:8880 -p 8080:8080 --privileged=true almalinux8_server_8880 /sbin/init

docker run -tid --name almalinux8_server_8880 -v D:/shared:/data -v E:/shared:/data2 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5432:5432 -p 3306:3306 --privileged=true almalinux8_server_8880 /sbin/init
	# 成功将 windows 的 D:/shared 目录映射到 linux 的 /data

	
docker exec -it almalinux8_server_8880 bash -c "systemctl start sshd &&
systemctl enable sshd &&
systemctl status sshd"

docker exec -it almalinux8_server_8880 bash -c 'chpasswd <<<"root:root"'

# rwkv runner

docker cp /root/proxychains-ng-master.zip almalinux8_server_8880:/root

./configure --prefix=/usr --sysconfdir=/etc && \
make && \
make install && \
make install-config

vi /etc/proxychains.conf
localnet 127.0.0.0/255.0.0.0
localnet 172.16.0.0/255.240.0.0
localnet 192.168.0.0/255.255.0.0
[ProxyList]
socks5  127.0.0.1 1080
	# 改成这样


docker pull ubuntu:20.04
	# almalinux安装rwkv 包出错
docker run -tid --name almalinux8_server_8880 -p 1417:1417 --privileged=true ubuntu:20.04 /bin/bash

docker exec -it almalinux8_server_8880 bash

apt-get update && \
(sleep 1; echo "Y";) | apt-get install build-essential
apt-get install p7zip-full vim curl lsof git wget 

https://blog.csdn.net/qq_20466211/article/details/128731196
apt-get install dialog apt-utils && \
apt install -y wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov

apt update && apt upgrade -y && \
apt install software-properties-common -y && \
add-apt-repository ppa:deadsnakes/ppa && \
apt install python3.10 && \
apt install python3.10-distutils && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py
	# python3.10 的pip 需要另外安装


https://linuxhint.com/install_yarn_ubuntu/
	# 安装 yarn
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee && \
apt install yarn




dnf search python39* && \
dnf install -y python39.x86_64 python39-devel.x86_64 p7zip && \
mkdir RWKV-Next-Web && \
cd RWKV-Next-Web && \
proxychains4 git clone https://github.com/josStorer/RWKV-Runner --depth=1 && \
proxychains4 python3.10 -m pip install torch torchvision torchaudio && \
pip3.10 install cyac && \
	# 这个出错
apt install -f --reinstall python3.10-minimal && \
apt install --reinstall libglib2.0-0/focal && \
apt install libpython3.10-dev && \
pip3.10 install pycairo && \
python3.10 -m pip install -r RWKV-Runner/backend-python/requirements.txt

python3.10 -m pip install -r RWKV-Runner/backend-python/requirements_without_cyac.txt --ignore-installed PyYAML
	# 成功!



kill  -9 $(jobs -p)


docker exec -it almalinux8_server_8880 bash -c "
dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && 
dnf -qy module disable postgresql && 
dnf -y install postgresql13 postgresql13-server postgresql13-contrib postgresql13-devel && 
/usr/pgsql-13/bin/postgresql-13-setup initdb && 
cat /var/lib/pgsql/13/initdb.log && 
ls /var/lib/pgsql/13/data/postgresql.conf
"

sed -i -e s/"#listen_addresses = 'localhost'"/"listen_addresses = '*'"/ -i /var/lib/pgsql/13/data/postgresql.conf  && \
cp /var/lib/pgsql/13/data/pg_hba.conf /var/lib/pgsql/13/data/pg_hba.conf_backup && \
echo "hostnossl    all          all            0.0.0.0/0  md5"  >>/var/lib/pgsql/13/data/pg_hba.conf

git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-13/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install
	# 安装 RUM
make USE_PGXS=1 installcheck && \
psql DB -c "CREATE EXTENSION rum;"


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

# 关闭防火墙
systemctl stop firewalld
# 关闭 apache 
service httpd stop

fdisk -l
	# 查看要挂载的硬盘

mount -o uid=26,gid=26,dmask=077,fmask=077 -t ntfs-3g /dev/sda1 /mnt
	# 成功挂载，而且权限是对的

mount
	-->/dev/sda1 on /mnt type fuseblk (rw,relatime,user_id=0,group_id=0,default_permissions,allow_other,blksize=4096)
	# 是读写仅限

echo '/dev/sda1 /mnt ntfs-3g defaults,noatime,uid=26,gid=26,dmask=077,fmask=077 0 0' | sudo tee -a /etc/fstab
	# 成功开机自动挂载







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
		

恢得已备份的数据库
    CREATE EXTENSION IF NOT EXISTS dblink;
    DO $$
    BEGIN
    PERFORM dblink_exec('', 'CREATE DATABASE Touch WITH OWNER = postgres ENCODING = ''UTF8'' TABLESPACE = pg_default CONNECTION LIMIT = -1 TEMPLATE template0');
    EXCEPTION WHEN duplicate_database THEN RAISE NOTICE '%, skipping', SQLERRM USING ERRCODE = SQLSTATE;
    END
    $$;

		# 好像数据库名只能是小写





dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
dnf -qy module disable postgresql && \
dnf -y install postgresql13 postgresql13-server && \
/usr/pgsql-13/bin/postgresql-13-setup initdb && \
cat /var/lib/pgsql/13/initdb.log && \
ls /var/lib/pgsql/13/data/postgresql.conf && \

sed -i -e s/"#listen_addresses = 'localhost'"/"listen_addresses = '*'"/ -i /var/lib/pgsql/13/data/postgresql.conf

cp /var/lib/pgsql/13/data/pg_hba.conf /var/lib/pgsql/13/data/pg_hba.conf_backup

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


psql -h 127.0.0.1 -p 5432 -U postgres
	# docker 内运行成功
	
psql -h 172.20.0.2 -p 5432 -U postgres
	# docker 内运行成功


netstat -aptn
	# 显示当前正在监听的所有端口，已建立的外部链接也会显示
	



vi /etc/ssh/sshd_config
	# 修改配置
	PermitRootLogin yes # 改成这个
	UsePAM no # 改成这个
	
/usr/pgsql-13/bin/pg_ctl -D /var/lib/pgsql/13/data/ -l logfile start


docker stop almalinux8_server_8880
docker rm almalinux8_server_8880
docker image rm almalinux:8.7
docker network rm customnetwork
	# 一次性删除所有东西，要小心

docker system prune --volumes -y
	# 危险！



```



```
# Install RUM for pg
dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y && \
dnf install -y python39 && \
pip3 install conan && \
dnf install -y passwd openssh-server tar p7zip libsodium nmap curl net-tools cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel boost-devel systemd-devel ntfsprogs ntfs-3g nginx cronie postgresql13 postgresql13-server postgresql13-contrib postgresql13-devel systemtap-sdt-devel redhat-rpm-config 

curl https://sh.rustup.rs -sSf | sh && \
source "$HOME/.cargo/env"

git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-13/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install



```





```
# no need
systemctl unmask firewalld && \
systemctl start firewalld && \
systemctl disable firewalld && \
systemctl stop firewalld
```







## Docker 更改已存在的端口和共享目录

[更改已存在的端口和共享目录](https://blog.csdn.net/bf96163/article/details/108405502)



## redis

```
wget https://download.redis.io/redis-stable.tar.gz && \
tar -xzvf redis-stable.tar.gz && \
cd redis-stable && \
make && \
make install

nohup redis-server >outlog &

redis-cli
	# exit

127.0.0.1:6379> config set protected-mode yes/no
	# config get protected*


npm uninstall redis
npm install redis
	# 装最新版的 redis 有 connect 函数


"redis": "^3.1.2",
	# 装这个旧版的可能可以兼容旧版写法
	"redis": "^4.6.7",
		# 新版不好用
		
		
		
npm install redis@3.1.2 --save

```





```
        await this.redis.defaultDB.smartsign.state.set(`tt`, "just for test")

        let redis_prefix = `smartsign.state`
        let { createClient } = require('redis')
        const redis_client = createClient({ url: 'redis://127.0.0.1:6379' })
        redis_client.on('error', (err) => { 
            console.log('********* Error: Redis Client Error', err) 
        })
        await redis_client.connect()

# 新旧写法对比

```





## 