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
```









# 查看端口点用



```
netstat -aon | findstr "8080"
```



# 多用户远程登录

- https://www.exitthefastlane.com/2018/02/resource-sharing-in-server2016-rdsh.html?m=1



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

