# windows Long path

1. Open the Start menu and type “regedit.” Launch the application.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Right-click the value “LongPathsEnabled” and select Modify.
4. Change “Value data” from 0 to 1.
5. Click OK.



# 无法在分区上安装windows

```
rufus-3.17
二、无法在驱动器0分区上安装windows解决方法
1、在当前安装界面按住Shift+F10调出命令提示符窗口；
2、输入diskpart，按回车执行；
3、进入DISKPART命令模式，输入list disk回车，列出当前磁盘信息；
4、要转换磁盘0格式，则输入select disk 0回车，输入clean，删除磁盘分区；
5、输入convert mbr，回车，将磁盘转换为MBR，输入convert gpt则转为GPT；
6、最后输入exit回车退出命令提示符，返回安装界面继续安装系统。
7、然后点击新建磁盘就可以安装驱动。

记住：最重要的是，完成以上步骤之后，返回刚开始的界面重新点击安装Windows，之后，才可以。

```



# 同一个局域网中，ping不通其他电脑



```
原因：

因为windows防火墙默认设置的是不让别人ping通的，所以方法就是，修改防火墙相关设置。

步骤：控制面板 →  系统和安全 → Windows防火墙 → 高级设置 → 入站规则 → 文件和打印机共享（回显请求 - ICMPv4-In）设置为启用


现在，应该就可以成功ping通了。
```



# 更新失败

```
　操作方法：

　　1、右键点击“此电脑”，选择“管理”。

　　2、进入到计算机管理后，点击左侧下面的“服务和应用程序”，点选“服务”。

　　3、找到windows Update，点击后，选择“属性”。

　　4、进入到属性界面后，在启动类型中选：手动。点击确定后退出设置。

　　5、右击：windows Update ，选择：启动即可。

　　以上就是win10系统更新错误的详细解决方法了，大家可以按照上述的步骤来解决遇到的错误代码0x800f081f问题
```







# 手机连网上邻居

```
电脑端目前由于Win10 系统最新补丁修改了 Samba 访问服务器的安全策略，window10系统默认不开启“SMB1.0/CIFS 文件共享支持”功能，所以win10电脑连接网络邻居邻居前，要先打开SMB1.0/CIFS 文件共享。

1、进入控制面板。

2、在程序分类中找到程序和功能，在左侧栏找到启用和关闭windows功能，再依次找到图中所示的SMB 1.0 /CIFS 服务器，勾选左侧的勾，点击确定。

3、重启。

然后手机尝试连接，步骤如下：

将手机和电脑连接到同一个 Wi-Fi 网络。
在电脑上，设置想在手机上访问文件夹的共享权限。有关电脑侧的操作，请参考电脑所装操作系统的相关说明。
在手机上，打开“”“文件管理”。
在“分类”页签下，点击“网络邻居”，即可查看到家中的电脑设备。
点击要访问的电脑设备，输入电脑设备的登录帐号和密码。登录成功后，即可在手机上访问电脑已共享的文件。
如需停止访问，在网络邻居设备列表中，长按设备即可断开连接。
```





# 安装程序 2503 错误



```
cmd # 以管理员远行
msiexec /package 7z1900-x64.msi
```





# 双网卡 Wi-Fi 中继（一收一发）



- https://www.sailstars.one/post/L2cMH1XUC/

  > 双网卡 Wi-Fi 中继（一收一发）



# mkdir -p



```
mkdir "src/java/resources" "src/main/resources"

src
-----java
-------resources
-----main
-------resources

mkdir "E:\videos\anime\Danganronpa\S01\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
```



# which

```
> Get-Command node  # 显示node 的路径
```



# ln -s

```
cd C:/
C:
cd "Program Files"
mklink /D nodejs nodejs_v14.18.1  # 创建软链接nodejs
	# 软链可以直接删除
mklink /D nodejs D:\usr\node-v10.14.2-win-x64

```









# 查看端口点用



```
netstat -aon | findstr "8080"
```



# 杀进程

```
taskkill -PID 进程号 -F
```





# 多用户远程登录

- https://www.exitthefastlane.com/2018/02/resource-sharing-in-server2016-rdsh.html?m=1



# Win10 WSL | Ubuntu 18.04 with Xfce & Xrdp



## MUST make sure that the XRDP doesn’t use port 3389 

- which is used by Microsoft RDP (in case if your Windows 10 is already configured for RDP)



```
sudo apt install xfce4
sudo apt install xrdp && \
sudo echo xfce4-session >~/.xsession && \
sudo service xrdp restart
```



### Change the port from 3389 to 3390



```
vi /etc/xrdp/xrdp.ini

service xrdp restart
```



## Use Win10 remote destop to connect



Press Win key -> 附件 -> 远程桌面

> input: 
>
> localhost:3390








```
sudo apt-get install xfce4

如果网速较慢，这会持续一段时间。

然后安装xrdp组件和vnc服务器：

sudo apt-get install xrdp vnc4server

安装好后要自行新建配置文件，使得在远程登录时默认使用xfce作为界面登录，然后重启xrdp服务：

echo "xfce4-session" >~/.xsession

sudo service xrdp restart

这个相当于在当前用户的home目录下新建一个名为.xsession的隐藏文件，并向文件中写入一行xfce4-session。也可以用touch新建文件，并用vi编辑：

touch ~/.xsession

vi ~/.xsession
```









# Docker

- https://blog.yowko.com/windows-server-2016-hyper-v/
  - 如何在 Windows Server 2016 上安裝 Hyper-V

- https://blog.yowko.com/windows-server-2016-linux-container/
  - 在 Windows Server 2016 上使用 Linux Container



# NFS



- https://blog.csdn.net/qq_34158598/article/details/81976063



# 内网测速

- https://zhuanlan.zhihu.com/p/137958252

  > iPerf3 搭建局域网内部测速环境



# wifi crack



- https://lofter.me/2018/10/22/Kali-Linux-%E9%AB%98%E6%95%88%E7%A0%B4%E8%A7%A3Wifi%E5%AF%86%E7%A0%81/

