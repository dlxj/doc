

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
dnf install -y tar p7zip libsodium curl net-tools cronie lsof git wget yum-utils make gcc g++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel systemd-devel 

# almalinux 8
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



```



```
dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && 
dnf -qy module disable postgresql && 
dnf -y install postgresql13 postgresql13-server postgresql13-contrib && 
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



# 替换成国内源

```

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

dnf install ./xrdp-0.9.22-5.el8.x86_64.rpm
	# 装完就可以成功用 windows 远程登录了
	# 失效了
	
dnf install ./xrdp-0.9.22.1-2.el8.x86_64.rpm
	
	
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



# Install Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
wget https://dl.google.com/linux/linux_signing_key.pub && \
rpm --import linux_signing_key.pub && \
dnf install -y google-chrome-stable_current_x86_64.rpm

```



