

https://github.com/lanthora/gateway

https://github.com/mayooot/grok-docker/blob/main/Dockerfile



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





# Install Docker



```
# ubuntu 22.04
# Add Docker's official GPG key:
sudo apt-get update && 
sudo apt-get install ca-certificates curl && 
sudo install -m 0755 -d /etc/apt/keyrings && 
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && 
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update



apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y


docker run hello-world

```



## 音视频图片标注



```
# see -> python summary -> gradio -> video -> 音视频图片标注

conda create --name label-studio && 
conda activate label-studio && 
conda install psycopg2 && 
pip install label-studio
	# 实测正常运行
	
pm2 --name label_studio_8080 start "/root/miniforge3/envs/label-studio/bin/python /usr/local/bin/label-studio"
	
http://xxx.77:8080/projects/
	# 它只支持 http


docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
```



# Docker+CentOS

```
# see nodejs summary.md -> docker

docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    yum install -y nginx redis nfs-utils crontabs && \\
    mkdir -p /project/shared && \\
    mkdir -p /project/script && \\
    chmod 755 /project/shared && \\
    cd /project && \\
    git clone http://用户名:AccessToten@gitlab.xxxxx.git && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /project/aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=这里放冒号转义后的json" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /project/aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' "  && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable rpcbind && systemctl start rpcbind" && \
docker exec -it centos7_server_6006_ENV bash -c "mkdir -p /project/shared/test_cooperate_img && chmod 755 /project/shared/test_cooperate_img && \\
    ls -al /project/shared/test_cooperate_img" && \
docker exec -it centos7_server_6006_ENV bash -c "showmount -e 172.16.15.13" && \
docker exec -it centos7_server_6006_ENV bash -c "mount -t nfs 172.16.15.13:/yingedu/web/aicby_v2/test_cooperate_img  /project/shared/test_cooperate_img" && \
docker exec -it centos7_server_6006_ENV bash -c "echo 'hello from docker' > /project/shared/test_cooperate_img/hi.txt" && \
cat /yingedu/web/aicby_v2/test_cooperate_img/hi.txt && \
docker exec -it centos7_server_6006_ENV bash -c "echo 'umount /project/shared/test_cooperate_img 
mount -t nfs 172.16.15.13:/xx/xxx  /project/xxxxx_img  
if [ \$? -ne 0 ]; then 
    echo mount failed  
    sleep 30s; echo try agin 
    umount /project/shared/test_cooperate_img 
    mount -t nfs 172.16.15.13:/xxx_img  /project/shared/test_cooperate_img 
else 
    echo mount nfs succeed
fi
' > /project/script/auto_mount.sh" && \
docker exec -it centos7_server_6006_ENV bash -c "echo '@reboot  /project/script/auto_mount.sh' > /var/spool/cron/root" && \
docker exec -it centos7_server_6006_ENV bash -c "chmod +x /project/script/auto_mount.sh" && \
docker exec -it centos7_server_6006_ENV bash -c "crontab -l" && \
docker exec -it centos7_server_6006_ENV bash -c "cat /project/script/auto_mount.sh" && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006




	kill -9 $(jobs -p)
		# 可以正常 exit 容器了


配置 nginx 80 转 6006


vi /etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}



vi /etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}

server {
  listen 80;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://centos7_server_6006;
    }
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 9999999;
    proxy_connect_timeout 9999999;
    proxy_send_timeout 9999999;
  }
}


nginx -s reload


nmap 172.20.0.2 -p6006
	# 扫描指定端口是否开放






```



# Docker+Ubuntu

```
# see nodejs summary.md -> docker
docker system prune --volumes
docker image ls | grep ubuntu:22.04
if [ $? -ne 0 ] ;then
    echo 'image ubuntu:22.04 not found, pull'
    docker pull ubuntu:22.04
    echo 'image ubuntu:22.04 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir ubuntu_soda && \
cd ubuntu_soda && \
touch Dockerfile && \
echo "FROM ubuntu:22.04 
RUN set -x; apt-get update && \\
apt-get install -y build-essential && \\
apt-get install -y p7zip-full unzip vim curl lsof git iputils-ping ufw wget net-tools git pollen libsodium-dev && \\
apt-get install -y dialog apt-utils && \\
apt install -y wget net-tools build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov libsodium-dev nginx libcairo2-dev && \\
apt install python3.10-dev -y && \\
apt install software-properties-common -y && \\
(sleep 1; echo '\n';) | add-apt-repository ppa:deadsnakes/ppa && \\
apt install python3.10 && \\
apt install python3.10-distutils && \\
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \\
python3.10 get-pip.py && \\
pip install --upgrade requests && \\
pip install pysocks wheel && \\
ufw disable && \\
update-rc.d ssh enable && \\
service ssh restart && \\
service ssh status && \\
mkdir -p /root/huggingface && \\
chmod -R 600 /root/huggingface && \\
cd /root/huggingface && \\
echo done. " > Dockerfile && \
docker build -t ubuntu_soda . && \
docker run -tid --name ubuntu_soda_ENV --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true ubuntu_soda /sbin/init 



git clone http://用户名:AccessToten@gitlab.xxxxx.git"  > Dockerfile && \

```



## ubuntu_soda

```
apt install -y tk-dev && \\
	# auto select the geographic area: apt install -y tk-dev
	# 没有解决自动选位置就不要它了

ufw disable && \\
	# 这句出错

docker stop ubuntu_soda_ENV
docker rm ubuntu_soda_ENV
rm -rf ubuntu_soda && mkdir ubuntu_soda
docker system prune --volumes
docker image ls | grep ubuntu:22.04
if [ $? -ne 0 ] ;then
    echo 'image ubuntu:22.04 not found, pull'
    docker pull ubuntu:22.04
    echo 'image ubuntu:22.04 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
cd ubuntu_soda && \
touch Dockerfile && \
echo "FROM ubuntu:22.04 
RUN set -x; apt-get update && \\
apt install -y wget net-tools build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov libsodium-dev nginx libcairo2-dev && \\
apt-get install -y p7zip-full unzip vim curl lsof git iputils-ping ufw wget net-tools git pollen libsodium-dev && \\
apt-get install -y dialog apt-utils && \\
apt install python3.10-dev -y && \\
apt install software-properties-common -y && \\
(sleep 1; echo '\n';) | add-apt-repository ppa:deadsnakes/ppa && \\
apt install python3.10 && \\
apt install python3.10-distutils && \\
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \\
python3.10 get-pip.py && \\
pip install --upgrade requests && \\
pip install pysocks wheel && \\
apt install openssh-server -y && \\
update-rc.d ssh enable && \\
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config && \\ 
sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config && \\ 
sed -i 's/^#\?PubkeyAuthentication.*/PubkeyAuthentication yes/g' /etc/ssh/sshd_config && \\ 
/etc/init.d/ssh restart && \\
/etc/init.d/ssh status && \\
mkdir -p /root/huggingface && \\
chmod -R 600 /root/huggingface && \\
cd /root/huggingface && \\
echo done. " > Dockerfile && \
docker build -t ubuntu_soda . && \
docker run -tid --name ubuntu_soda_ENV --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true ubuntu_soda /bin/bash && \
docker exec -it ubuntu_soda_ENV bash -c "echo 'root:root' | chpasswd" && \
docker exec -it ubuntu_soda_ENV bash -c "/etc/init.d/ssh restart" && \
docker exec -it ubuntu_soda_ENV bash -c "echo 'all task done.'" && \
docker exec -it ubuntu_soda_ENV bash -c "curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash" && \
docker exec -it ubuntu_soda_ENV bash -c "apt install -y git-lfs" && \
rm /root/.ssh/known_hosts

ssh root@127.0.0.1 -p 222
	# 成功登录
	# 注意了：容器的端口是由 docker run 指定的
		# 不能直接访问 容器内网ip:端口号
		# 而是应该访问 host ip:映射端口 
		
		
		
# vscode代理连docker
C:\Users\i\.ssh
Host 209.141.34.77
  HostName 209.141.34.77
  Port 222
  User root
  ProxyCommand D:\\usr\\ncat.exe --proxy 127.0.0.1:5782 %h %p
  	# 成功连接
  

下载 ncat
	linux：https://nmap.org/ncat/
	windows：https://nmap.org/dist/ncat-portable-5.59BETA1.zip



```



```





```



# docker-in-docker

https://www.zhaowenyu.com/docker-doc/dind/docker-in-docker.html

https://github.com/kubernetes/minikube

https://fancyerii.github.io/2020/08/28/minikube/ 

- https://www.cnblogs.com/yinzhengjie/p/12258215.html

- ```
  $ grep -E --color 'vmx|svm' /proc/cpuinfo
  	# 检查虚拟化的支持，如果上面的命令返回的不是空就ok
  	
  
  ```



```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

sudo dpkg -i minikube_latest_amd64.deb

su i

sudo usermod -aG docker $USER && newgrp docker

minikube start
 # 成功启动
	
	

```





```
要在 Minikube 上运行 Ubuntu 22.04 的容器，你可以指定使用 `ubuntu:22.04` 镜像。以下是一个示例 Pod 配置文件，可以帮助你在 Minikube 上运行一个 Ubuntu 22.04 的容器：

​```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-22-04-pod
spec:
  containers:
  - name: ubuntu
    image: ubuntu:22.04
    command: ["/bin/bash", "-c", "sleep infinity"]
    resources:
      limits:
        memory: "256Mi"
        cpu: "500m"
​```

以下是详细步骤：

1. **创建 YAML 文件：** 使用上面的内容创建一个名为 `ubuntu-22-04-pod.yaml` 的文件。

2. **在 Minikube 中部署 Pod：** 在终端中，导航到包含该 YAML 文件的目录，并使用以下命令应用配置：
   ```bash
   kubectl apply -f ubuntu-22-04-pod.yaml
   ```

3. **验证 Pod 是否运行：** 使用以下命令检查 Pod 的状态：
   ```bash
   kubectl get pods
   ```
   
   你应该能够看到 `ubuntu-22-04-pod` 的状态为 `Running`。

4. **进入 Ubuntu 22.04 容器：** 要访问和使用 Ubuntu 22.04 的环境，可以运行：
   ```bash
   kubectl exec -it ubuntu-22-04-pod -- /bin/bash
   ```

这会启动一个交互式 Bash 会话，你可以在其中使用 Ubuntu 22.04 进行任何需要的测试和开发。使用 Kubernetes 和容器技术，你可以轻松地部署和管理这种轻量级的测试环境。
```









```
kicbase 提供了完整的隔离环境，也提供 systemd 的系统服务的管理，和 VM 虚拟机使用体验很相似，也可以安装启动其他 systed 服务。

minikube 社区使用 kicbase 就用来提供类似虚拟化 VM 的驱动，使用该驱动来运行 Kubernetes 集群的。
```





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

docker run -tid --name ubuntu22.04 -p 222:22 --privileged=true ubuntu:22.04 /sbin/init
	
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



# Docker 自动修改密码

```
docker exec -it ubuntu_soda_ENV bash -c "echo 'root:1wDSFDFDED555dFDFDE$#' | chpasswd"
```





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


1. docker 命令本身的代理

mkdir -p /etc/systemd/system/docker.service.d && \
touch /etc/systemd/system/docker.service.d/proxy.conf

在这个proxy.conf文件（可以是任意*.conf的形式）中，添加以下内容：

vi /etc/systemd/system/docker.service.d/proxy.conf
[Service]
Environment="ALL_PROXY=http://127.0.0.1:8118/"

systemctl restart docker && \
systemctl status docker
	# 成功

2. 运行中的容器的代理

vi ~/.docker/config.json
{
 "proxies":
 {
   "default":
   {
     "httpProxy": "http://172.16.6.253:8118/",
     "httpsProxy": "http://172.16.6.253:8118/",
     "noProxy": "localhost,127.0.0.1,.example.com"
   }
 }
}


socks5 转 http
	see nodejs summray.md -> 抱抱脸 

# https://maplege.github.io/2017/09/04/socksTOhttp/
	# socks转为http代理
	apt update && apt-get install privoxy
	dnf update && dnf install -y privoxy
	vi /etc/privoxy/config
forward-socks5   /               172.16.6.253:1080 .
listen-address 172.16.6.253:8118
	# 注意：直接写 ip 可以, 写 0.0.0.0 不可以！！！
    service privoxy restart
    http_proxy=http://127.0.0.1:8118 curl google.com
    	# 成功访问 google
    	
    	
vi ~/.bashrc
alias setproxy="export ALL_PROXY=http://172.16.6.253:8118"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"
	# curl 正常    


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



# Ubuntu 20.04

https://stackoverflow.com/questions/76810738/how-do-i-access-docker-service-in-the-host-windows-server-2022-from-a-hyper-v

https://www.ssldragon.com/how-to/remove-ssl-certificates-windows-10/

- **ping 不通 Docker**

  ```
  Test-NetConnection 127.0.0.1 -p 3306
  可以改用 host模式部署 --net=host
  2022 自带容器功能，不要安装 Docker destop   https://www.cnblogs.com/shanyou/p/16413929.html
  ```




```

curl -fsSL https://get.docker.com -o get-docker.sh 
sudo sh get-docker.sh 
	# 安装Docker 
 
sudo apt-get install -y docker-compose
	# 安装Docker Compose

service docker start && 
service docker status 

```





```
docker image rm ubuntu:20.04
docker pull ubuntu:20.04

docker stop ubuntu_server_6006
docker rm ubuntu_server_6006
docker network rm customnetwork

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

[System.Text.Encoding]::UTF8.GetBytes('FROM ubuntu:20.04
RUN set -x; apt-get update && \
apt-get install -y build-essential && \
apt-get install -y p7zip-full unzip vim curl lsof git iputils-ping ufw wget pollen libsodium-dev && \
pwd ') | Set-Content Dockerfile -Encoding Byte

docker build -t ubuntu_server_6006 .
docker run -tid --name ubuntu_server_6006 --net=host -p 222:22 -p 6006:6006 -p 7860:7860 -p 7861:7861 -p 5432:5432 -p 6379:6379 -p 8880:8880 -p 8080:8080 --privileged=true ubuntu_server_6006 /bin/bash

docker exec -it ubuntu_server_6006 bash -c 'ifconfig'

docker exec -it ubuntu_server_6006 bash -c 'apt-get install -y dialog apt-utils && \
apt install -y wget net-tools build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov libsodium-dev'

docker exec -it ubuntu_server_6006 bash -c 'ufw disable'

docker exec -it ubuntu_server_6006 bash -c "curl -fsSL https://get.pnpm.io/install.sh | bash - &&
source /root/.bashrc && 
ln -s /root/.local/share/pnpm/pnpm /usr/bin/pnpm
"

docker exec -it ubuntu_server_6006 bash -c 'version=v20.11.1 && 
wget https://nodejs.org/download/release/$version/node-$version-linux-x64.tar.gz && 
tar xvf node-$version-linux-x64.tar.gz && 
cd node-$version-linux-x64/bin && 
chmod +x node npm npx && 
cd ../.. && 
mv node-$version-linux-x64 /usr/local && 
ln -s /usr/local/node-$version-linux-x64/bin/node /usr/local/bin/node && 
ln -s /usr/local/node-$version-linux-x64/bin/npm /usr/local/bin/npm && 
ln -s /usr/local/node-$version-linux-x64/bin/npx /usr/local/bin/npx'

docker exec -it ubuntu_server_6006 bash -c 'VERSION=3.10.13 && 
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && 
tar -xf Python-${VERSION}.tgz && 
cd Python-${VERSION} && 
./configure --with-openssl="/usr" && 
make clean && 
make -j 8 && 
make altinstall &&
ln -s /usr/local/bin/pip3.10 /usr/bin/pip &&
ln -s /usr/local/bin/python3.10 /usr/bin/python'


docker exec -it ubuntu_server_6006 bash -c 'pnpm --version && 
node --version && 
python --version && 
pip --version'

docker exec -it ubuntu_server_6006 bash -c 'pip install gradio==4.21.0'

docker exec -it ubuntu_server_6006 bash -c 'gradio cc create myvideo --template Video && 
cd myvideo && 
gradio cc install && 
gradio cc dev'




	# | ENV="$HOME/.bashrc" SHELL="$(which bash)" bash -

--net=customnetwork --ip=172.20.0.2 

```








# AlmaLinux9

```

# power shell 执行

docker image rm almalinux:9.3
docker pull almalinux:9.3

docker stop almalinux9_server_6006
docker rm almalinux9_server_6006
docker network rm customnetwork

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

[System.Text.Encoding]::UTF8.GetBytes('FROM almalinux:9.3
RUN set -x; dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf install -y passwd openssh-server tar p7zip libsodium net-tools nmap cronie lsof git wget yum-utils make gcc g++ clang openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel  && \
pwd ') | Set-Content Dockerfile -Encoding Byte


docker build -t almalinux9_server_6006 .
docker run -tid --name almalinux9_server_6006 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 6006:6006 -p 7860:7860 -p 7861:7861 -p 5432:5432 -p 6379:6379 -p 8880:8880 -p 8080:8080 --privileged=true almalinux9_server_6006 /sbin/init

docker exec -it almalinux9_server_6006 bash -c "systemctl start sshd &&
systemctl enable sshd &&
systemctl status sshd"

docker exec -it almalinux9_server_6006 bash -c 'chpasswd <<<"root:u"'

docker exec -it almalinux9_server_6006 bash -c "curl -fsSL https://get.pnpm.io/install.sh | sh - &&
source /root/.bashrc"

docker exec -it almalinux9_server_6006 bash -c 'VERSION=3.10.13 && 
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && 
tar -xf Python-${VERSION}.tgz && 
cd Python-${VERSION} && 
./configure --with-openssl="/usr" && 
make clean && 
make -j 8 && 
make altinstall &&
ln -s /usr/local/bin/pip3.10 /usr/bin/pip &&
ln -s /usr/local/bin/python3.10 /usr/bin/python'

docker exec -it almalinux9_server_6006 bash -c 'version=v20.11.1 && 
wget https://nodejs.org/download/release/$version/node-$version-linux-x64.tar.gz && 
tar xvf node-$version-linux-x64.tar.gz && 
cd node-$version-linux-x64/bin && 
chmod +x node npm npx && 
cd ../.. && 
mv node-$version-linux-x64 /usr/local && 
ln -s /usr/local/node-$version-linux-x64/bin/node /usr/local/bin/node && 
ln -s /usr/local/node-$version-linux-x64/bin/npm /usr/local/bin/npm && 
ln -s /usr/local/node-$version-linux-x64/bin/npx /usr/local/bin/npx'

docker exec -it almalinux9_server_6006 bash -c 'curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | bash &&
yum install -y git-lfs'

docker exec -it almalinux9_server_6006 bash -c 'git config --global user.name "dlxjj" && 
git config --global user.email "12345@qq.com" &&
git config --global push.default matching'

docker exec -it almalinux9_server_6006 bash -c 'pip install huggingface_hub && 
git config --global credential.helper store && 
huggingface-cli login'


docker exec -it almalinux9_server_6006 bash -c 'pip install gradio==4.21.0 &&
gradio cc create myvideo --template Video && 
cd myvideo && 
gradio cc install && 
gradio cc dev'

docker exec -it almalinux9_server_6006 bash -c 'mkdir huggingface &&
cd huggingface &&
git clone https://huggingface.co/datasets/dlxjj/myvideo &&
cd myvideo && 
gradio cc install && 
gradio cc dev'

docker exec -it almalinux9_server_6006 bash -c 'dnf install -y nmap &&
nmap 172.20.0.2 -p22'

ssh root@172.20.0.2 -p22

sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

systemctl restart ssh

docker exec -it almalinux9_server_6006 bash -c '/bin/bash'


docker exec -it almalinux9_server_6006 bash -c 'dnf install firewalld -y && 
systemctl start firewalld &&
firewall-cmd --state &&
systemctl stop firewalld &&
systemctl disable firewalld'

docker exec -it almalinux9_server_6006 bash -c 'systemctl stop firewalld'
docker exec -it almalinux9_server_6006 bash -c 'dnf install firewalld && 
systemctl stop firewalld
systemctl disable firewalld'

ssh -CNg -L 7861:127.0.0.1:7861 root@172.20.0.2 -p 22
	# 手动端口映射

```



## Linux 运行 Docker 



```
see echodict/docker部署.txt

# bash 执行

docker stop almalinux9_server_6006
docker rm almalinux9_server_6006
docker image remove almalinux9_server_6006
docker network rm customnetwork


docker image ls | grep almalinux

mkdir almalinux9_server_6006 && \
cd almalinux9_server_6006 && \
touch Dockerfile && \
echo "FROM almalinux:9.3 
RUN set -x; dnf makecache --refresh && \\
dnf update -y && \\
dnf install -y epel-release && \\
dnf update -y && \\
dnf install -y passwd openssh-server tar p7zip libsodium net-tools nmap cronie lsof git wget yum-utils make gcc g++ clang openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel  && \\
pwd " > Dockerfile && \
docker build -t almalinux9_server_6006 . 

docker run -tid --name almalinux9_server_6006 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 6006:6006 -p 7860:7860 -p 7861:7861 -p 5432:5432 -p 8880:8880 -p 8080:8080 --privileged=true almalinux9_server_6006 /sbin/init


docker exec -it almalinux9_server_6006 bash -c 'export ALL_PROXY=http://172.16.6.253:8118 &&
curl http://ip-api.com/json/?lang=zh-CN'

# 实际运行 gradio 不能开代理
docker exec -it almalinux9_server_6006 bash -c 'cd ~ && 
cd myvideo && 
gradio cc dev'


# 全部要执行的命令都在这里编辑和执行
docker exec -it almalinux9_server_6006 bash -c 'export ALL_PROXY=http://172.16.6.253:8118 && cd ~ && 

cd myvideo && 
gradio cc dev && 


pip install gradio==4.21.0 &&
gradio cc create myvideo --template Video && 
cd myvideo && 
gradio cc install && 



curl -fsSL https://get.pnpm.io/install.sh | sh - && 
ln -s /root/.local/share/pnpm/pnpm /usr/bin/pnpm && 
source /root/.bashrc && 


version=v20.11.1 && 
wget https://nodejs.org/download/release/$version/node-$version-linux-x64.tar.gz && 
tar xvf node-$version-linux-x64.tar.gz && 
cd node-$version-linux-x64/bin && 
chmod +x node npm npx && 
cd ../.. && 
mv node-$version-linux-x64 /usr/local && 
ln -s /usr/local/node-$version-linux-x64/bin/node /usr/local/bin/node && 
ln -s /usr/local/node-$version-linux-x64/bin/npm /usr/local/bin/npm && 
ln -s /usr/local/node-$version-linux-x64/bin/npx /usr/local/bin/npx && 

VERSION=3.10.13 && 
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && 
tar -xf Python-${VERSION}.tgz && 
cd Python-${VERSION} && 
./configure --with-openssl="/usr" && 
make clean && 
make -j 8 && 
make altinstall &&
ln -s /usr/local/bin/pip3.10 /usr/bin/pip &&
ln -s /usr/local/bin/python3.10 /usr/bin/python && 


pnpm --version && 
node --version && 
python --version && 
pip --version && 







curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | bash &&
yum install -y git-lfs &&




'






alias setproxy="export ALL_PROXY=http://127.0.0.1:8118"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"


```



### node server

```javascript
const http = require('node:http');
const hostname = '0.0.0.0';
const port = 6116;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
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





# CentOS7.9 安装Docker

https://www.cnblogs.com/kohler21/p/18331060 配置源

- ```
  sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak && 
  wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
  
  
  vi /etc/yum.repos.d/CentOS-Base.repo
  [base]
  name=CentOS-$releasever - Base - mirrors.aliyun.com
  failovermethod=priority
  baseurl=https://mirrors.aliyun.com/centos-vault/7.9.2009/os/x86_64/
  gpgcheck=1
  gpgkey=http://mirrors.aliyun.com/centos-vault/7.9.2009/RPM-GPG-KEY-CentOS-7
   
  #released updates 
  [updates]
  name=CentOS-$releasever - Updates - mirrors.aliyun.com
  failovermethod=priority
  baseurl=https://mirrors.aliyun.com/centos-vault/7.9.2009/os/x86_64/
  gpgcheck=1
  gpgkey=http://mirrors.aliyun.com/centos-vault/7.9.2009/RPM-GPG-KEY-CentOS-7
   
  #additional packages that may be useful
  [extras]
  name=CentOS-$releasever - Extras - mirrors.aliyun.com
  failovermethod=priority
  baseurl=https://mirrors.aliyun.com/centos-vault/7.9.2009/os/x86_64/
  gpgcheck=1
  gpgkey=http://mirrors.aliyun.com/centos-vault/7.9.2009/RPM-GPG-KEY-CentOS-7
   
  #additional packages that extend functionality of existing packages
  [centosplus]
  name=CentOS-$releasever - Plus - mirrors.aliyun.com
  failovermethod=priority
  baseurl=https://mirrors.aliyun.com/centos-vault/7.9.2009/os/x86_64/
  gpgcheck=1
  enabled=0
  gpgkey=http://mirrors.aliyun.com/centos-vault/7.9.2009/RPM-GPG-KEY-CentOS-7
   
  #contrib - packages by Centos Users
  [contrib]
  name=CentOS-$releasever - Contrib - mirrors.aliyun.com
  failovermethod=priority
  baseurl=http://mirrors.aliyun.com/centos-vault/7.9.2009/contrib/$basearch/
  gpgcheck=1
  enabled=0
  gpgkey=http://mirrors.aliyun.com/centos-vault/7.9.2009/RPM-GPG-KEY-CentOS-7
  
  
  yum clean all
  sudo yum makecache
  
   yum install -y http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.107-3.el7.noarch.rpm   
  
  ```

  

https://www.cnblogs.com/jhdhl/p/17072590.html

```
# cat /etc/redhat-release
	# CentOS Linux release 7.9.2009 (Core)
	# uname -r 显示操作系统的发行版号
	# uname -a 示系统名、节点名称、操作系统的发行版号、内核版本等等。
# uname -r
	# 3.10.0-1160.25.1.el7.x86_64
	
	
yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
	# 删除旧版本
    

yum -y install gcc gcc-c++ yum-utils

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

    
 yum install -y http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.107-3.el7.noarch.rpm   
 	# 先安装这个依赖
 
 
	
```

