# 找回休眠功能



```
# 管理员运行 powershell
powercfg -h on

电源和睡眠 ->其他电源设置 -> 更改当前不可用设置 -> 选择电源按钮的功能

```



# 磁盘管理工具

```
diskmgmt.msc
```



# 安装 FTP 

[window server 2022 搭建FTP服务器](https://zhuanlan.zhihu.com/p/622408091)

[开启服务设置端口防火墙](https://www.vdtutorials.com/install-and-configure-ftp-server-on-windows-server-2022/)

[用户名_FTP站点](https://cloudinfrastructureservices.co.uk/how-to-setup-ftp-server-using-iis-on-windows-server-2022/)



# App Installer

[installing App Installer (winget) on Windows Server 2022](https://gist.github.com/carey/62070ee199099c4233f572a17315366d)

[winget-and-appinstaller](https://www.andreasnick.com/112-install-winget-and-appinstaller-on-windows-server-2022.html)

[Windows Server安装Microsoft Store的应用 ](https://www.cnblogs.com/cqpanda/p/16650721.html)

```

wsl --install

winget search alma
-->AlmaLinux 9  9P5RWLM70SN9  Unknown  msstore
   AlmaLinux 8 WSL  9NMD96XJJ19F  Unknown  msstore

winget install 9NMD96XJJ19F
	# 没有成功，闪退了

```



```
Windows Server 2022 无法正常使用 Microsoft Store 下载应用程序。

您可以尝试以下方案进行操作，看看是否可行：

设置>>应用>>应用和功能>>找到应用商店>>高级选项>>重置。

 

另外，您还可以尝试清理应用商店的缓存，看看是否可以恢复正常：

 

按“Win+R”键，在运行窗口中，键入 WSReset.exe并点击“ 运行 ”。

 

如果问题依旧，建议您尝试以下方案重新部署您的应用商店：

 

在打开的“管理员：Windows Powershell”窗口中输入以下命令：

 

get-appxpackage *store* | remove-Appxpackage

 

再次安装：

 

add-appxpackage -register "C:\Program Files\WindowsApps\*Store*\AppxManifest.xml" -disabledevelopmentmode


完成后重启您的 Microsoft Store ，看看是否可以正常下载安装应用程序。
```







# windows Long path

1. Open the Start menu and type “regedit.” Launch the application.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Right-click the value “LongPathsEnabled” and select Modify.
4. Change “Value data” from 0 to 1.
5. Click OK.



# 处理路径

- https://blog.csdn.net/zeqi1991/article/details/110531406

```

	#include <Shlwapi.h>
	#pragma comment(lib, "shlwapi.lib")

	//去除路径的参数
    PathRemoveArgs
    //去除路径最后的反斜杠”\”
    PathRemoveBackslash
    //在路径最后加上反斜杠”\”
    PathAddBackslash
    //去除路径前后的空格
    PathRemoveBlanks
    //在文件路径后面加上扩展名
    PathAddExtension
    //去除文件路径扩展名
    PathRemoveExtension
    //更改文件路径扩展名
    PathRenameExtension
    //去除文件名,得到目录
    PathRemoveFileSpec
    //去除路径中的首尾空格
    PathUnquoteSpaces
    //判断路径中是否有空格,有的话,就是用”“引号把整个路径包含起来
    PathQuoteSpaces
    //将一个路径追加到另一个路径后面
    PathAppend
    //合并两个路径
    PathCombine
    //去掉路径中的磁盘符或UNC部分
    PathSkipRoot
    //去掉路径中的目录部分,得到文件名
    PathStripPath
    //去掉路径的文件部分,得到根目录
    PathStripToRoot
    //根据像素值生成符合长度的路径
    PathCompactPath
    //如原始路径: C:\path1\path2\sample.txt
    //根据120像素截断后为: C:\pat…\sample.txt
    //根据25像素截断后为: …\sample.txt
    //根据字符个数来生成符合长度的路径
    PathCompactPathEx
    //将路径数据设置到对话框的子控件上
    PathSetDlgItemPath
    //去除路径中的修饰
    PathUndecorate
    //将路径中部分数据替换为系统环境变量格式
    PathUnExpandEnvStrings
    //从路径中查找路径
    PathFindOnPath
    //查找路径的扩展名
    PathFindExtension
    //获取路径的文件名
    PathFindFileName
    //查找匹配路径
    PathFindNextComponent
    //查找给定的文件名是否有给定的后缀
    PathFindSuffixArray
    //获取路径参数
    PathGetArgs
    //获取路径字符类型
    PathGetCharType
    //根据逻辑盘符返回驱动器序号
    PathGetDriveNumber
    //创建一个路径到另一个路径的相对路径。
    PathRelativePathTo
    //将一个相对路径或绝对路径转换为一个合格的路径
    PathResolve
    //规范化路径。将格式比较乱的路径整理成规范的路径格式
    PathCanonicalize
    //根据给定的磁盘序号创建根目录路径
    PathBuildRoot
    //创建目录
    CreateDirectory
    //将长路径转为8.3格式的短路径格式
    GetShortPathName
    //将短路径格式转为长路径。
    GetLongPathName
    //将长路径转为短路径格式（8.3格式）
    PathGetShortPath
    //将URL路径转为MS-DOS格式
    PathCreateFromUrl
    //把路径全部转为小写,增加可读性
    PathMakePretty
    //给路径增加系统属性
    PathMakeSystemFolder
    //去除路径中的系统属性
    PathUnmakeSystemFolder
    //从模板创建统一的路径格式
    PathMakeUniqueName
    //生成一个可执行的路径,比如有参数的,会自动将路径用”“包含
    PathProcessCommand
    //去除路径中不合法的字符
    PathCleanupSpec
    //比较并提取两个路径相同的前缀
    PathCommonPrefix
    //验证路径是否存在
    PathFileExists
    //判断路径是否匹配制定的扩展名
    PathMatchSpec
    //判断路径是否是一个有效的目录
    PathIsDirectory
    //验证路径是否一个文件名（有可能是一个路径）
    PathIsFileSpec
    //验证路径是否是可执行文件
    PathIsExe
    //注意:不仅仅是.exe,还有.bat、.com、.src等
    //路径是否为根路径
    PathIsRoot
    //判断路径是否是相对路径
    PathIsRelative
    //检测文件是否为制定类型
    PathIsContentType
    //例如:
    PathIsContentType(“hello.txt”,”text/plain”) 返回TRUE
    PathIsContentType(“hello.txt”,”image/gif”) 返回FALSE

    //判断路径是否是html文件类型——根据系统注册类型判断
    PathIsHTMLFile
    //判断路径是否是长路径格式
    PathIsLFNFileSpec
    //判断路径是否是一个网络路径。
    PathIsNetworkPath
    //判断路径是否含有指定前缀
    PathIsPrefix
    //判断路径是否有相同根目录
    PathIsSameRoot
    //判断路径是否是一个高度延迟的网络连接
    PathIsSlow
    //判断路径是否有系统属性（属性可以自己设定）
    PathIsSystemFolder
    //路径是否是UNC格式（网络路径）
    PathIsUNC
    //路径是否是UNC服务器
    PathIsUNCServer
    //路径是否仅仅是UNC的共享路径格式
    PathIsUNCServerShare
    //路径是否是http格式。
    PathIsURL
    //基于已存在的文件,自动创建一个唯一的文件名。比如存在”新建文件”,此函数会创建文件名”新建文件(2)”
    PathYetAnotherMakeUniqueName 

```







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



# 遍历进程

[遍历进程](https://github.com/dbshch/DOAXVV-script)



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

