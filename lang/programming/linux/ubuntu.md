

# Ubuntu22.04远程桌面

```
apt install xfce4 xfce4-goodies -y && \
apt install xrdp -y && \
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



# Install python3.11

```
apt-get update && \
apt-get install -y build-essential checkinstall && \
apt -y install gdb lcov libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev

VERSION=3.11.3 && \
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && \
tar -xf Python-${VERSION}.tgz && \
cd Python-${VERSION} && \
./configure && \
make -j 4 && \
sudo make altinstall 

```



# network

## dns

```
apt install -y net-tools && \
ifconfig && \
apt-get install -y iproute2 && \
ip a && \
apt install -y network-manager && \
nmcli connection show

mkdir /etc/systemd/resolved.conf.d/ && \
vi/etc/systemd/resolved.conf.d/dns_servers.conf

[Resolve]
DNS=1.1.1.1 8.8.8.8

systemctl restart systemd-resolved
	# 有可能要 reboot 才生效

```





