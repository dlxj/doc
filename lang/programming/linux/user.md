```
https://www.jianshu.com/p/be342d3659ff
https://blog.csdn.net/dengbin_40/article/details/87997128
```



```
# 修改密码
echo 'root' | passwd --stdin root
```





```
为添加的用户指定相应的用户组

# useradd -g root -r -d /home/pp pp

groups pp
userdel pp
useradd pp -o -u 0 -g root -G root -s /bin/bash -d /home/pp



```





```
shell> groupadd web
shell> useradd -r -g mysql mysql

usermod -g web qinjing

# 改用户的home 目录
usermod -d xxxxx qin (qin为你的用户名)

qinjing

chown -R qinjing:qinjing .


1.
groupadd web
useradd -d xxxxxxx -m qin -g web
	-d 用户的 home 目录
	

2.

xxxxxxx  上层目录权限设置为 755 以下


vi /etc/ssh/sshd_config
	# 一定要加在它的最后，否则后果严重！

Match User qin
     ChrootDirectory /yingedu/www/web
     ForceCommand internal-sftp
     AllowTcpForwarding no
     X11Forwarding no


# 重启ssh
systemctl status sshd


userdel qin



```



