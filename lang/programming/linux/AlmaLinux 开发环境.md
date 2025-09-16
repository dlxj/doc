# ISO

[ISO](https://ftp.riken.jp/Linux/almalinux/9.3/isos/x86_64/)



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

hostnamectl

git lfs clone https://huggingface.co/datasets/dlxjj/gradio

git-lfs 3.4.0         
	# 这个片本正常
	
wget https://github.com/git-lfs/git-lfs/releases/download/v3.4.0/git-lfs-linux-amd64-v3.4.0.tar.gz
	# 这样装才行
	# ok 这样设置 .gitconfig 后就正常了

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

# 启用 EPEL 仓库
sudo dnf install epel-release -y \
  && sudo dnf config-manager --set-enabled epel \
  && sudo dnf config-manager --set-enabled crb \
  && sudo dnf update -y


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



## wifi

https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/proc_connecting-to-a-wifi-network-by-using-nmcli_assembly_managing-wifi-connections



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



## 安装 postgresql 17

```

# 启用 EPEL 仓库
sudo dnf install epel-release -y
sudo dnf config-manager --set-enabled epel

# 启用 CRB 仓库（AlmaLinux/Rocky Linux 9）
sudo dnf config-manager --set-enabled crb

# 更新仓库元数据
sudo dnf update -y




# Install the repository RPM:
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Disable the built-in PostgreSQL module:
sudo dnf -qy module disable postgresql

# Install PostgreSQL:
sudo dnf install -y postgresql17-server

# Optionally initialize the database and enable automatic start:
sudo /usr/pgsql-17/bin/postgresql-17-setup initdb
sudo systemctl enable postgresql-17
sudo systemctl start postgresql-17


sudo -u postgres psql
select version();
\password postgres  # 修改密码
\q

postgres 	post4321
	# 用户名 密码

psql -h 127.0.0.1 -p 5432 -U postgres
	# 成功登录

mkdir /home/psqldata

chown -R postgres:postgres /home/psqldata



 systemctl stop postgresql-17

cp -R /var/lib/pgsql/17/data /home/psqldata   # 只能透亮换柱了

mv /var/lib/pgsql/17/data /var/lib/pgsql/17/data__link__to_home_psqldata

ln -s  /home/psqldata/data  /var/lib/pgsql/17/data
			# unlink 取消软链用这个

chown -R postgres:postgres /home/psqldata



systemctl start postgresql-17

systemctl status postgresql-17



# 允许运程连接
vi /var/lib/pgsql/17/data/postgresql.conf
	listen_addresses = '*' # 改成这个
vi /var/lib/pgsql/17/data/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  md5  
	# hostnossl    all          all            0.0.0.0/0  trust  # 任何密码都能连
	# 加在最后面，接受所有远程IP


systemctl restart postgresql-17
systemctl status postgresql-17



yum groupinstall "Development Tools" && \
yum install llvm-toolset-7-clang && \
yum install postgresql17-devel && \
yum install postgresql17-contrib && \
yum install systemtap-sdt-devel


git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-17/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install

make USE_PGXS=1 installcheck && \
psql DB -c "CREATE EXTENSION rum;"



yum install pgvector_17 -y
	# https://github.com/pgvector/pgvector 先安装

CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS test_vector (
    ID integer generated always as identity,
    AppID integer NOT NULL,
    TestID integer NOT NULL,
    ChildTableID integer NOT NULL,
    TestCptID integer DEFAULT -1,
    S_Test text NOT NULL,
    V_Test vector(1536) NOT NULL,
    AddedTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    AddUserID integer DEFAULT -1,
    UpdateUserID integer DEFAULT -1,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (AppID, TestID, ChildTableID) 
);
CREATE INDEX IF NOT EXISTS idx_appid ON test_vector (AppID);
CREATE INDEX IF NOT EXISTS idx_appid_cptid ON test_vector (AppID, TestCptID);
CREATE INDEX ON test_vector USING hnsw (V_Test vector_cosine_ops);


(async () => {
  let bent = require('bent')
  let post = bent("http://128.1.41.47:8094", 'POST', 'json', 200)
  
  let response = await post('/embeddings', JSON.stringify({"sentence":"什么什么向量"}), { 'Content-Type': "application/json;chart-set:utf-8" })

  if (response.status == 0) {
      return [response.data, '']
  } else {
      return [null, response.msg]
  }
})()


```





# 安装指定版本

```
yum list installed | grep git-lfs
	# 已安装版本

yum list git-lfs
	# 可用版本
	


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
address1=172.16.6.253/24
gateway=172.16.6.1
dns=8.8.8.8;1.1.1.1
method=manual

[ipv6]

addr-gen-mode=eui64

method=auto

[proxy]

:wq! #保存退出

nmcli n off && nmcli n on #重启网络

nmcli con reload

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



```
# dhcp 这样就可以，但是要记得重启电脑

[ipv4]
method=auto
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

# reboot
	# 不重启也可以连

systemctl stop firewalld
	# 关掉防火墙以后成功用 windows 远程桌面登录
systemctl disable firewalld
	# 永久关闭防火墙


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





# 增加虚拟内存

```
dd if=/dev/zero of=/mnt/swapfile bs=1M count=20480
	# 20G 空文件

mkswap /mnt/swapfile
	# 格式化交换文件

swapon /mnt/swapfile
	# 挂载交换文件

vi /etc/fstab
/mnt/swapfile swap swap defaults 0 0
	# 加在后面，开机自动加载
	
free -h
	# 查看内存大小
```







# clean

```
yum autoremove && \
yum clean all

rpm -qa | grep boost
```





# Install Chrome

```
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





# Install .Net SDK



```

https://download.visualstudio.microsoft.com/download/pr/1cac4d08-3025-4c00-972d-5c7ea446d1d7/a83bc5cbedf8b90495802ccfedaeb2e6/dotnet-sdk-6.0.417-linux-x64.tar.gz

mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-6.0.417-linux-x64.tar.gz  -C $HOME/dotnet
export DOTNET_ROOT=$HOME/dotnet && \
export PATH=$PATH:$HOME/dotnet


```



# CUDA

https://medium.com/@kiena/almalinux-9-2-installing-nvidia-driver-5d67d19bb27d





# 阿里云Archlinux

https://blog.51cto.com/u_16213696/7915426

https://www.nolightblog.com/posts/fe4463fe/

https://www.nodeseek.com/post-128045-1  纯手工重装云服务器操作系统(阿里云ECS + Debian 12版)

https://www.cnblogs.com/shankun/p/aliyunECS_archlinux.html 

https://blog.csdn.net/mineo/article/details/134713925

```

blkid /arch.iso
/arch.iso: BLOCK_SIZE="2048" UUID="2025-09-01-16-37-02-00" LABEL="ARCH_202509" TYPE="iso9660" PTUUID="2d9d5c0b" PTTYPE="dos"
	# archisolabel= 要填这里输出的 LABEL，既 ARCH_202509

fdisk -l /arch.iso 
Device     Boot   Start     End Sectors  Size Id Type
/arch.iso1 *         64 2433599 2433536  1.2G  0 Empty
/arch.iso2      2433600 2941503  507904  248M ef EFI (FAT-12/16/32)

fdisk -l
Disklabel type: gpt
Disk identifier: 656BD20C-0FC7-43A8-B07B-98C45B710F4A

Device      Start      End  Sectors  Size Type
/dev/vda1    2048     4095     2048    1M BIOS boot
/dev/vda2    4096   413695   409600  200M EFI System
/dev/vda3  413696 83886046 83472351 39.8G Linux filesystem


wget -o /arch.iso https://mirrors.tuna.tsinghua.edu.cn/archlinux/iso/latest/archlinux-x86_64.iso


vi /boot/grub/grub.cfg

set timeout=20

#编辑grub.cfg文件，将下面内容塞到第一个menuentry前面，让grub自动引导Arch Live。
menuentry 'ArchISO' --class iso {
  set isofile=/arch.iso
  loopback loop0 $isofile
  #archisolabel设置ArchISO文件所在的文件系统标签。
  #img_dev指出ArchISO 文件所在的设备
  #img_loop是ArchISO文件在img_dev里的绝对位置
  # 下面这两个文件名字需要自己到镜像文件当中查看，Arch Linux 不同版本的名字可能不太一样。
  linux (loop0)/arch/boot/x86_64/vmlinuz-linux archisolabel=ARCH_202509 img_dev=/dev/vda3 img_loop=$isofile
  initrd (loop0)/arch/boot/x86_64/initramfs-linux.img
}
	# 实测连 vnc 连接，reboot 后成功进入 arch livecd
	# 重启第一次 vnc 进入有花屏，要等一下才有反应
		

lsblk
vda3 254:3 0 39.8G part /run/archiso/img_dev
	# 正在运行的这个系统被挂载到 /run/archiso/img_dev
	
passwd
	# 重设 root 密码，然后用 xshell 登录方便贴命令

mount -o rw /dev/vda3 /mnt \
  && mount -o remount,rw /dev/vda3 /mnt
	# 以读写方式挂载

保留 ubuntu 系统的 /boot 用于启动，就不用在 Arch Linux 安装 Grub 了
cd /mnt
ls | grep -v arch.iso | grep -v boot | xargs rm -rf
	# 除了 arch.iso 文件和 boot 文件夹保留，其他全部删除
	

pacstrap /mnt base base-devel
	# 安装基本系统
		# linux linux-firmware grub	vi
	
genfstab -L /mnt >> /mnt/etc/fstab
	# 配置挂载表
	cat /mnt/etc/fstab  
		# /dev/vda3 被挂载到   /

pacstrap /mnt linux linux-firmware \
  dhcpcd systemd-resolvconf \
  iproute2 iputils net-tools bind-tools
	# 安装网络工具


arch-chroot /mnt
    - 控制权交给刚装好的硬盘系统
    - 如果picman 出问题：  
      - **rm /var/lib/pacman/db.lck**

passwd
	# 重设 root 密码，不然等下登录不上
	
vi /boot/grub/grub.cfg
menuentry 'Arch Linux' --class arch --class gnu-linux --class gnu --class os {
    set root='hd0,gpt3'  # 对应/dev/vda3
    linux /boot/vmlinuz root=/dev/vda3 rw
    initrd /boot/initrd.img
}
	# 注意这里用的是原 ubuntu 的 boot 文件
	# 加配置，硬盘启动 arch linux


exit
reboot
	# 验证安装正常输出，到这里整个安装应该就完成了
	# 实测重启后 vnc 能正常进 Arch Linux 更盘系统了，但是 ssh 还没有配
	# 但是，进去以后没有网络


# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:16:3e:18:df:af brd ff:ff:ff:ff:ff:ff
    altname enp0s5
    altname enx00163e18dfaf
    inet 172.21.123.73/20 metric 1024 brd 172.21.127.255 scope global dynamic ens5
       valid_lft 1892159820sec preferred_lft 1892159820sec
    inet6 fe80::216:3eff:fe18:dfaf/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever



# UEFI 配置开始
mkdir -p /boot/efi
mount /dev/vda2 /boot/efi
	# 假设 EFI 分区是 /dev/vda2，挂载到 /boot/efi

pacman -S efibootmgr
 
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg

 
 
pacman -Sy grub
grub-install --target=i386-pc /dev/vda
	# 参数 --target=i386-pc 强制 GRUB 使用传统 BIOS 模式，即使系统支持 UEFI。
grub-mkconfig -o /boot/grub/grub.cfg
	# 安装Bootloader
        如果出错：
        vi /etc/lvm/lvm.conf这个文件，找到use_lvmetad = 1将1修改为0，保存，重新配置grub


ls /boot/vmlinuz-linux \
  && ls /boot/grub/grub.cfg
  	# 验证安装


exit
umount -R /mnt  
reboot
	# 验证安装正常输出，到这里整个安装应该就完成了


arch-chroot /mnt
ls /boot/vmlinuz-linux
	--> ls: cannot access '/boot/vmlinuz-linux': No such file or directory
		# 这是不正常的
		
pacman -S base linux linux-firmware	
	# 重装内核
	
pacman -S base-devel vi grub


grub-install /dev/vda
	# 安装 GRUB 到硬盘 MBR
	
grub-mkconfig -o /boot/grub/grub.cfg
	# 生成 GRUB 配置文件

vi /etc/default/grub
GRUB_DISABLE_OS_PROBER=false
GRUB_TERMINAL=console
	# 添加或修改成这样

grub-install /dev/vda

exit 或按 Ctrl+d 退出 chroot 环境。
umount -R /mnt  
reboot





这时侯如果直接重启，就会进入 grub 救援模式

ls
ls (hd0,gpt3)/
	# 能看到 arch.iso

set root=(hd0,gpt3)                  				# 设置包含ISO文件的分区为root
linux /vmlinuz-linux root=/dev/sda3   # 请根据实际情况修改根分区设备号
initrd /initramfs-linux.img
boot



loopback loop /arch.iso  							# 将ISO文件映射为loop设备
linux (loop)/arch/boot/x86_64/vmlinuz-linux   		# 加载内核
initrd (loop)/arch/boot/x86_64/initramfs-linux.img 	# 加载initramfs
boot                                  				# 启动
	# 依次输入以上命令



vi /etc/pacman.d/mirrorlist 
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
	# 最前面加

pacman -Syyu
	# pacman -Syyuu 从一个较新的镜像切换到较旧的镜像，以下命令可以降级部分包，以避免系统的部分更新











安装必需的软件包
使用 pacstrap(8) 脚本，安装 base 软件包和 Linux 内核以及常规硬件的固件：

# pacstrap /mnt base linux linux-firmware
提示：
可以将 linux 替换为内核页面中介绍的其他内核软件包。
在虚拟机或容器中安装时，可以不安装固件软件包。
base 软件包并没有包含 Live 环境中的全部程序。因此要获得一个功能齐全的基本系统，可能需要安装其他软件包。特别要考虑安装：

管理所用文件系统的用户工具（比如 XFS 和 Btrfs 对应的管理工具）；
访问RAID或LVM分区的工具；
未包含在 linux-firmware 中的额外固件(如用于声卡的sof-firmware)；
联网所需要的程序 (如网络管理器或DHCP客户端)；
文本编辑器（如：nano、vim 等）；
访问 man 和 info 页面中文档的工具：man-db，man-pages 和 texinfo。
要安装其他软件包或软件包组（比如 base-devel），请将它们的名字追加到上文的 pacstrap 命令后 (用空格分隔)，或者也可以在 Chroot 进新系统后使用 pacman 手动安装软件包或软件包组。packages.x86_64 中可以看到不同软件包或软件包组间的差异。

配置系统
Fstab
用以下命令生成 fstab 文件 (用 -U 或 -L 选项设置 UUID 或卷标)：

# genfstab -U /mnt >> /mnt/etc/fstab
强烈建议在执行完以上命令后，检查一下生成的 /mnt/etc/fstab 文件是否正确。

Chroot
chroot 到新安装的系统：

# arch-chroot /mnt
时区
要设置时区：

# ln -sf /usr/share/zoneinfo/Region（地区名）/City（城市名） /etc/localtime
提示： 以要设置为上海时区为例，请运行 # ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
然后运行 hwclock(8) 以生成 /etc/adjtime：

# hwclock --systohc
这个命令假定已设置硬件时间为 UTC 时间。详细信息请查看 System time#Time standard。

本地化
程序和库如果需要本地化文本，都依赖区域设置，后者明确规定了地域、货币、时区日期的格式、字符排列方式和其他本地化标准。

需在这两个文件设置：locale.gen 与 locale.conf。

编辑 /etc/locale.gen，然后取消掉 en_US.UTF-8 UTF-8 和其他需要的 区域设置 前的注释（#）。

接着执行 locale-gen 以生成 locale 信息：

# locale-gen
然后创建 locale.conf(5) 文件，并 编辑设定 LANG 变量，比如：

/etc/locale.conf
LANG=en_US.UTF-8
另外对于中文用户：

提示：
用户可以设置自己的 locale，详情请参阅 在用户会话中覆盖系统区域设置 或 设置当前区域；
将系统 locale 设置为 en_US.UTF-8 ，系统的 log 就会用英文显示，这样更容易判断和处理问题；
也可以设置为 en_GB.UTF-8 或 en_SG.UTF-8，附带以下优点：
进入桌面环境后以 24 小时制显示时间；
LibreOffice 等办公软件的纸张尺寸会默认为 A4 而非 Letter(US)；
可尽量避免不必要且可能造成处理麻烦的英制单位。
设置的 LANG 变量需与 locale 设置一致，否则会出现以下错误：
Cannot set LC_CTYPE to default locale: No such file or directory
警告： 不推荐在此设置任何中文 locale，会导致 tty 乱码。
如果需要修改 #控制台键盘布局，可编辑 vconsole.conf(5) 使其长期生效，例如：

/etc/vconsole.conf
KEYMAP=de-latin1
网络配置
创建 hostname 文件:

/etc/hostname
myhostname（主机名）
请接着完成新安装的环境的网络配置，配置过程中可能需要安装合适的网络管理软件。

Initramfs
通常不需要自己创建新的 initramfs，因为在执行 pacstrap 时已经安装 linux，这时已经运行过 mkinitcpio 了。

对于 LVM、 system encryption 或 RAID 等分区配置，请修改 mkinitcpio.conf 并用以下命令重新创建一个 Initramfs：

# mkinitcpio -P
Root 密码
设置 Root 密码：

# passwd
安装引导程序
需要安装 Linux 引导加载程序，才能在安装后启动系统，可以使用的的引导程序已在 启动加载器 中列出，请选择一个安装并配置它，GRUB (简体中文) 是最常见的选择。

如果有 Intel 或 AMD 的 CPU，请另外启用 微码 更新。

警告： 这是安装的最后一步也是至关重要的一步，请按上述指引正确安装好引导加载程序后再重新启动。否则重启后将无法正常进入系统。
重启
输入 exit 或按 Ctrl+d 退出 chroot 环境。

可选用 umount -R /mnt 手动卸载被挂载的分区：这有助于发现任何「繁忙」的分区，并通过 fuser(1) 查找原因。

最后，通过执行 reboot 重启系统，systemd 将自动卸载仍然挂载的任何分区，然后使用 root 帐户登录到新系统。


```





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

```
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



