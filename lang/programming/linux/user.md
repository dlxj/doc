```
https://www.jianshu.com/p/be342d3659ff
https://blog.csdn.net/dengbin_40/article/details/87997128
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



