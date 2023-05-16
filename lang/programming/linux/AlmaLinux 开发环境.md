

# 允许 root ssh

```
vi /etc/ssh/sshd_config.d/01-permitrootlogin.conf
	# PermitRootLogin yes
	# 改成这个

/etc/ssh/sshd_config
	# 这文件定义了一句 Include /etc/ssh/sshd_config.d/*.conf
	# 所以可以在 /etc/ssh/sshd_config.d/ 里面自定义 xxx.conf 文件
	# PermitRootLogin yes
		# 弄成这样试试
```





# 安装开发环境

```

cat /etc/os-release

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
dnf install -y tar p7zip libsodium curl net-tools cronie lsof git wget yum-utils make gcc g++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel cargo


# almalinux 8
dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y && \
pip3 install conan && \
dnf install -y tar p7zip libsodium curl net-tools cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel ntfsprogs ntfs-3g

curl https://sh.rustup.rs -sSf | sh && \
source "$HOME/.cargo/env"




```



# 关闭防火墙



```
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

