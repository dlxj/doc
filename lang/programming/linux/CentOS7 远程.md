```
sudo apt install xfce4
sudo apt install xrdp && \
sudo echo xfce4-session >~/.xsession && \
sudo service xrdp restart
```






```
# https://serverspace.io/support/help/installing-and-configuring-a-vnc-server-on-centos-7/

yum install tigervnc-server
sudo adduser rootvnc
sudo passwd rootvnc
su - rootvnc

cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service



vnc4server

vncserver :1 && vncserver -kill :1
```





```
# https://www.rootusers.com/how-to-install-xfce-gui-in-centos-7-linux/
# https://www.hiroom2.com/2017/10/01/centos-7-xrdp-xfce-en/
# https://www.jianshu.com/p/1cda88d2070a
# https://draculaservers.com/tutorials/install-xrdp-centos/

systemctl stop firewalld

yum install epel-release -y
yum groupinstall "Server with GUI" -y  
	#  this will also install GNOME, you’ll be able to change to Xfce later though

yum groupinstall "Xfce" -y
	# success. df -hl 3G space comsume
	# yum groupremove "Xfce"  # remove
	# yum remove -y libxfce4*

systemctl get-default
	# 看默认是不是图形登录

systemctl set-default multi-user.target # no gui
systemctl set-default graphical.target  # gui

which xfce4-session
	# /usr/bin/xfce4-session  # 成功

```

```
yum install -y epel-release
yum install -y xrdp
vi /etc/xrdp/xrdp.ini
	# change 3389 to 3390  # 端口改成3390 
systemctl restart xrdp

$ sudo systemctl enable xrdp
$ sudo systemctl start xrdp

systemctl status xrdp.service  # 查看状态
```







