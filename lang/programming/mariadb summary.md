

**CentOS 7 下 MySQL 5.7 的安装与配置** [u](https://www.jianshu.com/p/1dab9a4d0d5f)

> su -   # 注意切root 账号才能启动mysqld 
>
> systemctl start mysqld  # 启动
>
> netstat -tnlp | grep 3306  # 看是否成功
>
> systemctl status mysqld   # 看是否成功
>
> ps aux | grep mysql          # 看是否成功
>
> grep "temporary password" /var/log/mysqld.log  # 默认密码
>
> > A temporary password is generated for root@localhost: qpigpq-j4&G2
>
> mysql -uroot -p
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'AIDev@2020';
>
> GRANT ALL PRIVILEGES ON *.* TO 'aidev'@'%' IDENTIFIED BY 'AIDev2020@' WITH GRANT OPTION;


netstat -tnlp | grep 3306



**Ubuntu 18.04 安装配置 MySQL 5.7** [u](https://my.oschina.net/u/4351216/blog/3238036)

> apt-get install mysql-server-5.7
> sudo cat /etc/mysql/debian.cnf  # 查看初始安装后的用户名和密码
>
> mysql -h localhost -u debian-sys-maint -p
>
> Enter password: 
>
> ```mysql
> update mysql.user set authentication_string=password('root') where user='root' and host='localhost';
> ```
>
>
> mysql> use mysql;
> mysql> update user set plugin='mysql_native_password';
> mysql> flush privileges;
> mysql> quit;





centos7下yum安装mariadb
1.安装MariaDB

删除已安装的mysql
yum remove mysql mysql-server mysql-libs mysql-devel
删除存放数据的目录
rm -rf /var/lib/mysql

安装mariaDB
yum -y install mariadb mariadb-server

安装完成后启动MariaDB
systemctl start mariadb

设置开机启动命令
systemctl enable mariadb

安装10.3版本的mariadb:
vi /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.3/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
或者使用阿里云的源
[mariadb]
name = MariaDB
baseurl = http://mirrors.aliyun.com/mariadb/yum/10.3/centos7-amd64/
gpgkey = http://mirrors.aliyun.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck = 1
安装命令
yum -y install MariaDB-server MariaDB-client

2.进行MariaDB的简单配置
mysql_secure_installation
首先是设置密码，会提示先输入密码
Enter current password for root (enter for none):<–初次运行直接回车
Set root password? [Y/n] <– 是否设置root用户密码，输入y并回车或直接回车
New password: <– 设置root用户的密码
Re-enter new password: <– 再输入一次你设置的密码
Remove anonymous users? [Y/n] <– 是否删除匿名用户，回车
Disallow root login remotely? [Y/n] <–是否禁止root远程登录,回车,
Remove test database and access to it? [Y/n] <– 是否删除test数据库，回车
Reload privilege tables now? [Y/n] <– 是否重新加载权限表，回车
Thanks for using MariaDB!
初始化完成。

使用设置的密码登录mariadb：
mysql -uroot -ppassword

done!



## 设置root 密码

- mysql_secure_installation # 设置root 密码



## 显示后台进程

- jobs
- ps -ef





## 删除cent7 自带mariadb

```
yum remove mariadb* -y				# 将yum自带的mariadb移除
cat /etc/my.cnf                     # 先清空
ls /var/log/mysqld.log              # 先清空
ls /var/lib/mysql/                  # 先清空
ls /var/log/mariadb/                # 先清空
ls /var/run/mariadb/                # 先清空
ls /etc/my.cnf.d/                   # 先清空
ls /etc/my.cnf.rpmsave              # 先清空
```



## 删除mysql

```
rpm -qa |grep -i mysql
mysql-community-client-5.7.32-1.el7.x86_64
mysql-community-server-5.7.32-1.el7.x86_64
mysql-community-common-5.7.32-1.el7.x86_64
mysql-community-libs-5.7.32-1.el7.x86_64
mysql57-community-release-el7-11.noarch
```



netstat -tnlp | grep 3306

jobs

ps -ef





### 删除mariadb yum源

```
/etc/yum.repos.d/mariadb.repo	#新建mariadbyum源
```



### 更新中科大源

http://centos.ustc.edu.cn/help/centos.html

```bash
yum clean all
yum makecache

sudo yum update
```



## 静态IP 配置

```
$ cat /etc/sysconfig/network-scripts/ifcfg-enp3s0 
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="none"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="enp3s0"
UUID="c371f269-7b8c-48e0-8589-1e010f2153fa"
DEVICE="enp3s0"
ONBOOT="yes"
IPADDR="192.168.1.166"
PREFIX="24"
GATEWAY="192.168.0.1"
DNS1="192.168.0.1"
DNS2="114.114.114.114"
IPV6_PRIVACY="no"
```



## root 密码

https://mariadb.com/kb/en/authentication-from-mariadb-104/



用cent7 的root 账号可以免密登录

mysql -uroot

```
use mysql;
update user set password=PASSWORD("new_password_here") where User='root';
flush privileges;
```





**CentOS 7 通过 yum 安装 MariaDB** [u](https://zhuanlan.zhihu.com/p/49046496)

```bash
yum install -y mariadb-server
/usr/bin/mysql_secure_installation   # 初始设置

vi /etc/my.cnf.d/client.cnf
[client]
default-character-set = utf8  # 加一行

vi /etc/my.cnf.d/mysql-clients.cnf
[mysql]
default-character-set = utf8  # 加一行

vi /etc/my.cnf.d/server.cnf
[mysqld]
collation-server = utf8_general_ci
init-connect = 'SET NAMES utf8'
character-set-server = utf8
sql-mode = TRADITIONAL


$ systemctl start mariadb  # 启动服务器
$ ss -nalpt | grep 3306

```



```bash
https://stackoverflow.com/questions/20270879/whats-the-default-password-of-mariadb-on-fedora

ran sudo mysqld_safe --skip-grant-tables --skip-networking &
ran sudo mysql -uroot and got into mysql console
run ALTER USER root@localhost identified via  unix_socket; and flush privileges; consecutively to allow for password-less login
If you want to set the password then you need to do one more step, that is running ALTER USER root@localhost IDENTIFIED VIA mysql_native_password; and SET PASSWORD = PASSWORD('YourPasswordHere'); consecutively.

UPDATE

Faced this issue recently and here is how I resolved it with recent version, but before that some background. Mariadb does not require a password when is run as root. So first run it as a root. Then once in the Mariadb console, change password there. If you are content with running it as admin, you can just keep doing it but I find that cumbersome especially because I cannot use that with DB Admin Tools. TL;DR here is how I did it on Mac (should be similar for *nix systems)

sudo mariadb-secure-installation

then follow instructions on the screen!

Hope this will help someone and serve me a reference for future problems
```



```
set password = password("root");
```





```

sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

To start mysqld at boot time you have to copy
support-files/mysql.server to the right place for your system

PLEASE REMEMBER TO SET A PASSWORD FOR THE MariaDB root USER !
To do so, start the server, then issue the following commands:

'/usr/bin/mysqladmin' -u root password 'new-password'
'/usr/bin/mysqladmin' -u root -h localhost.localdomain password 'new-password'

Alternatively you can run:
'/usr/bin/mysql_secure_installation'

which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.

See the MariaDB Knowledgebase at http://mariadb.com/kb or the
MySQL manual for more instructions.

You can start the MariaDB daemon with:
cd '/usr' ; /usr/bin/mysqld_safe --datadir='/var/lib/mysql'

You can test the MariaDB daemon with mysql-test-run.pl
cd '/usr/mysql-test' ; perl mysql-test-run.pl

Please report any problems at http://mariadb.org/jira

The latest information about MariaDB is available at http://mariadb.org/.
You can find additional information about the MySQL part at:
http://dev.mysql.com
Consider joining MariaDB's strong and vibrant community:
https://mariadb.org/get-involved/

```









**mariadb高版本yum安装** [u](https://blog.csdn.net/yts1115084429/article/details/100882992)



```
est ~]# vim /etc/my.cnf		(编辑这几处即可) 
[mysqld]												#指的是mysql服务端
port                           	= 3306					#指定运行端口
socket                         	= /data/mydata/mysql.sock	#指定sock	
character-set-server 	= utf8        							#指定字符集
log-error                     	= /data/logs/mysql/mysql-error.log		#指定错误日志(路劲自定义)	
datadir                        	= /data/mydata			#指定数据库存放路劲(路劲自定义)

[client]
default-character-set          	= utf8
port            				= 3306
socket          				= /data/mydata/mysql.sock

#创建mysql
[root@test ~]# id mysql			#存在的话,就不用创建,(用户的创建方式:groupadd -g 27  mysqle ; useradd -g 27 -s /sbin/nologin  mysql)
uid=27(mysql) gid=27(mysql) 组=27(mysql)

#创建主要目录并且授权
[root@test ~]# mkdir -p /data/logs/mysql /data/mydata	#创建日志目录及数据库存放路劲
[root@test ~]# chown mysql.mysql /data/mydata/ /data/logs/mysql/	#授权给mysql(Mariaadb默认以mysql用户运行的)
[root@test ~]# ln -s /data/mydata/mysql.sock /var/lib/mysql/mysql.sock		#建立软连接(具体啥用我忘记了,建立一个放着也行)	

#初始化
[root@test ~]# mysql_install_db --defaults-file=/etc/my.cnf --user=mysql		#初始化(但是保证/etc/my.cnf文件已创建并且进行授权)

#启动mariabd
[root@test ~]# systemctl start mariadb
[root@test ~]# ss -nalpt | grep 3306
LISTEN     0      128         :::3306                    :::*                   users:(("mysqld",pid=29585,fd=22))

#删除用户‘’并且创建root用户密码
[root@test ~]# mysql -uroot -e "delete  from mysql.user where user=''"			#删除用户 这个用户是' ' 
[root@test ~]# mysqladmin -uroot password "你的密码"	#设置root密码(mysqladmin是执行管理操作的客户端程序)
[root@test ~]# mysqladmin -uroot -h 127.0.0.1 password "你的密码"		
[root@test ~]# mysql -uroot -p -e "delete from mysql.user where password=''"		#删除'' 空密码
```







```
# cat /etc/my.cnf
[mysqld]
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
user=mysql
```





**Installing MariaDB Binary Tarballs** [u](https://mariadb.com/kb/en/installing-mariadb-binary-tarballs/)



```bash
Installing MariaDB/MySQL system tables in '/var/lib/mysql' ...
OK

To start mysqld at boot time you have to copy
support-files/mysql.server to the right place for your system


Two all-privilege accounts were created.
One is root@localhost, it has no password, but you need to
be system 'root' user to connect. Use, for example, sudo mysql
The second is mysql@localhost, it has no password either, but
you need to be the system 'mysql' user to connect.
After connecting you can set the password, if you would need to be
able to connect as any of these users with a password and without sudo

See the MariaDB Knowledgebase at https://mariadb.com/kb or the
MySQL manual for more instructions.

You can start the MariaDB daemon with:
cd '.' ; ./bin/mysqld_safe --datadir='/var/lib/mysql'

You can test the MariaDB daemon with mysql-test-run.pl
cd './mysql-test' ; perl mysql-test-run.pl

```

