

# su -

切换成root 登陆 



## 允许root 登陆

- sudo vi /etc/ssh/sshd_config
  - 把 PermitRootLogin 修改为 yes



groupdel ubt
useradd ubt



**logout**

```
sudo pkill -u username
is not in the sudoers file 解决方案：
首需要切换到root身份
$su -
(注意有- ，这和su是不同的，在用命令"su"的时候只是切换到root，但没有把root的环境变量传过去，还是当前用户的环境变量，用"su -"命令将环境变量也一起带过去，就象和root登录一样)

然后
$visudo //切记，此处没有vi和sudo之间没有空格
```

vi /etc/sudoers

```
1、移动光标，到最后一行
2、按a，进入append模式
3、输入
your_user_name ALL=(ALL) ALL
4、按Esc
5、输入“:w”(保存文件)
6、输入“:q”(退出)

这样就把自己加入了sudo组，可以使用sudo命令了。


你运行ls -l / | grep usr,不就知道要什么权限了。
一般是要root权限。

二楼的做法对，但是不推荐su,推荐sudo，因为sudo提供详细的日志和不需要根用户密码，sudo mkdir /usr/你要建的文件名。

希望你的问题能得到解决。
```

用recovery mode模式启动后，进入命令行模式，提示符应该是 #

1、输入用户管理的命令，新建用户（以test为例）：

useradd test

修改 test 用户的密码：

passwd test

2、将新用户添加到管理组：

gpasswd -a test admin

3、给 test 用户创建自己的目录：

cd /home

mkdir test

chown test /home/test

添加root 权限

vi /etc/passwd 文件，找到如下行，把用户ID修改为 0 

 

tommy:x:500:500:tommy:/home/tommy:/bin/bash

 

修改后如下

 

tommy:x:0:500:tommy:/home/tommy:/bin/bash

whoami 

  root

rootiZ2335

rootiZ23354321

正规方法：

\# useradd -ou 0 -g 0 john
\# passwd john

We've just created the user john, with **UID 0** and **GID 0**, so he is in the same group and has the **same permissions as root**.

4、重新启动，

reboot

然后用 test 登录，

登录以后，点菜单“系统－系统管理－用户和组”，进去选中你的用户，点右边的“属性”按钮，到用户权限里打勾需要的；



来源： <[http://wiki.ubuntu.org.cn/%E6%96%B0%E5%BB%BA%E7%94%A8%E6%88%B7%E5%B9%B6%E6%B7%BB%E5%8A%A0%E5%88%B0%E7%AE%A1%E7%90%86%E7%BB%84](http://wiki.ubuntu.org.cn/新建用户并添加到管理组)>

 

