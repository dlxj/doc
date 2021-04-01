

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



### 移除镜像

docker images

docker rmi xxx



### 移除容器

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



### 如果需要更多的端映射

```
# 将宿主机的222端口映射到IP为172.18.0.3容器的22端口
# 些方法可以用于增加额外的端口？？？
iptables -t nat -A  DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22
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





### Docker 中的postgreql



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

