

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
dnf install -y passwd openssh-server tar p7zip libsodium nmap curl net-tools cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel boost-devel systemd-devel ntfsprogs ntfs-3g nginx cronie

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



# 配置静态 IP



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

dnf install ./xrdp-0.9.22-5.el8.x86_64.rpm
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



# Install Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
wget https://dl.google.com/linux/linux_signing_key.pub && \
rpm --import linux_signing_key.pub && \
dnf install -y google-chrome-stable_current_x86_64.rpm

```



