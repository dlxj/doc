









## 允许密码登录

/etc/ssh/sshd_config

PubkeyAuthentication yes
PasswordAuthentication no



vi /etc/ssh/sshd_config

PermitRootLogin yes



service ssh restart

> sudo systemctl restart sshd

service ssh status



### 远程桌面

apt-get install -y ubuntu-desktop 

sudo service gdm3 start



sudo apt install xrdp

sudo vim /etc/xrdp/startwm.sh

> 把最下面的test和exec两行注释掉，添加一行
>
> gnome-session



sudo adduser xrdp ssl-cert

sudo service xrdp restart

sudo service xrdp status



重新启动ubuntu，不要登录！
windows远程桌面连接

1. windows打开远程桌面输入ubuntu主机ip或者主机名
2. 选择xorg，输入用户名密码
3. 会提示几次授权修改主机的颜色设置什么的，都可以cancel掉，然后即可登陆成功





















sudo apt-get update
sudo apt-get install xserver-xorg-core
sudo apt-get install xrdp
sudo apt-get install xserver-xorg-core
sudo apt-get -y install xserver-xorg-input-all
sudo apt-get install xorgxrdp

reboot



[ERROR] Cannot read private key file /etc/xrdp/key.pem: Permission denied



```

```





## 软件安装

仅需要

```bash
sudo apt install xrdp
```

## 编辑配置

```text
sudo vim /etc/xrdp/startwm.sh
```

把最下面的test和exec两行注释掉，添加一行

```text
gnome-session
```

## 重新启动ubuntu，不要登录！

## windows远程桌面连接

1. windows打开远程桌面输入ubuntu主机ip或者主机名
2. 选择xorg，输入用户名密码
3. 会提示几次授权修改主机的颜色设置什么的，都可以cancel掉，然后即可登陆成功

