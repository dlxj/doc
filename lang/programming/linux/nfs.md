[CentOS 7 下 yum 安装和配置 NFS](https://qizhanming.com/blog/2018/08/08/how-to-install-nfs-on-centos-7)



## 成功

- ​	https://qizhanming.com/blog/2018/08/08/how-to-install-nfs-on-centos-7

````
nfs 成功
	umount -f -l  /home/data/users/xxx/mnt     # 取消挂载

	vi /etc/exports      # .124
		/home/data/users/xxx/data_backup/    192.168.2.0/24(rw,sync,no_root_squash,no_all_squash)
	
	systemctl restart nfs
	# 找不到命令改成这个  service nfs-server restart
	
	客户端
		yum -y install nfs-utils

		mkdir /yingedu/shared
		chmod 755 /xxx/shared

		showmount -e 192.168.1.xxx     # 显示 .124 的共享文件

		mount -t nfs 192.168.1.xxx:/home/data/users/xxx/data_backup  /yingedu/shared    # 挂载远程目录
		


# windwos 客户端

【Win+R】运行，复制输入以下命令：

OptionalFeatures

将 NFS相关的这三项，全部打上勾，确定。安装完成。



		
````



# 三、Win10客户端访问NFS服务

## 1. Win10安装NFS客户端

打开 控制面板 —> 程序 —> 启用或关闭Windows功能

也可以用【Win+R】运行，复制输入以下命令：

```
OptionalFeatures
```

![Win10客户端访问NFS服务1](nfs.assets/win10-nfs-1.png)

如上图，将 NFS相关的这三项，全部打上勾，确定。安装完成。

## 2. 访问NFS目录

安装好后就能在Windows的命令行，使用 showmount 和 mount 命令访问NFS服务器了。

```PowerShell
C:\Users\OdinXu> showmount -e 192.168.1.32
Exports list on 192.168.1.32:
/data                              192.168.1.27
/public                            192.168.1.0/24
/var/www/html                      *

C:\Users\OdinXu> mount \\192.168.1.32\public  X:
X: is now successfully connected to \\192.168.1.32\public

The command completed successfully.
```

showmount命令参数和Linux的一样。 mount命令有些不同，不是使用一个目录作为挂载点，而是使用一个未使用的盘符。比如命令行最后一个 X: 表示将远程NFS目录，映射为Windows本地的一个磁盘X盘。也可以使用其它英文字母 A–Z

映射成功后如下图：

![Win10客户端访问NFS服务2](nfs.assets/win10-nfs-2.png)

使用完后，可以用umount命令卸载磁盘映射。

```PowerShell
C:\Users\OdinXu> umount X:
```

单独输入 `mount` 不带任何参数，可以列出当前所有已经加载(映射)的NFS目录。

## 3. 只读问题

访问NFS正常，但是只能读，不能写，不能创建目录。

先确认`/etc/exports`配置文件内容，是否为 `rw` 再确认目录权限，试试777：

```bash
chmod 777 /public/
```

## 4. Win10访问NFS存在中文乱码问题

原因是Linux通常是UTF-8编码，而Windows自带的NFS客户端工具，一直不升级支持UTF-8，从而导致中文显示乱码。这绝对是Windows的锅。

详见`mount --help`说明：

```
-o lang=euc-jp|euc-tw|euc-kr|shift-jis|big5|ksc5601|gb2312-80|ansi
```

### 解决方法1

使用第三方开源工具 https://github.com/cbodley/ms-nfs41-client

64位Windows下载安装这个： [ms-nfs41-client-setup-x64.exe](https://github.com/cbodley/ms-nfs41-client/releases/download/v1.0.0/ms-nfs41-client-setup-x64.exe)

32位Windows下载安装这个： [ms-nfs41-client-setup-x86.exe](https://github.com/cbodley/ms-nfs41-client/releases/download/v1.0.0/ms-nfs41-client-setup-x86.exe)

安装好后，这样用：

```PowerShell
nfs_mount X: 192.168.1.32:/public
```

### 解决方法2 【不推荐使用】

```
2020/5/5 修改为不推荐使用
因为用了这个设置后，我用招商银行专业版，出现乱码。改回来就恢复正常。
还是使用上面的解决方法1吧。
```

用【Win+R】运行，复制输入以下命令：

```
intl.cpl
```

![Win10客户端访问NFS服务–解决中文乱码问题](nfs.assets/win10-nfs-3.png)

如上图，在打开的“区域”功能界面，选择“管理”标签 —> 更改系统区域设置 —> 勾选中“Beta版：使用Unicode UTF-8提供全球语言支持” —> 确定 —> 重启Windows系统。

这样操作之后，中文显示就一切正常了。





## 前言

NFS 是 Network File System 的缩写，即网络文件系统。功能是让客户端通过网络访问不同主机上磁盘里的数据，主要用在类Unix系统上实现文件共享的一种方法。 本例演示 CentOS 7 下安装和配置 NFS 的基本步骤。

### 环境说明

CentOS 7（Minimal Install）

```
$ cat /etc/redhat-release 
CentOS Linux release 7.5.1804 (Core) 
```

本例演示环境如下

| Name           | IP Addr       | Descprition         |
| :------------- | :------------ | :------------------ |
| Server         | 192.169.0.110 | 服务端 IP           |
| Client         | 192.168.0.101 | 客户端 IP           |
| Windows Client | 192.168.0.102 | Windows Server 2008 |

根据官网说明 [Chapter 8. Network File System (NFS) - Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-nfs)，CentOS 7.4 以后，支持 NFS v4.2 不需要 rpcbind 了，但是如果客户端只支持 NFC v3 则需要 rpcbind 这个服务。

## 服务端

### 服务端安装

使用 yum 安装 NFS 安装包。

```
$ sudo yum install nfs-utils
```

*`注意`*

> 只安装 nfs-utils 即可，rpcbind 属于它的依赖，也会安装上。

### 服务端配置

设置 NFS 服务开机启动

```
$ sudo systemctl enable rpcbind
$ sudo systemctl enable nfs
```

启动 NFS 服务

```
$ sudo systemctl start rpcbind
$ sudo systemctl start nfs
```

防火墙需要打开 rpc-bind 和 nfs 的服务

```
$ sudo firewall-cmd --zone=public --permanent --add-service={rpc-bind,mountd,nfs}
success
$ sudo firewall-cmd --reload
success
```

### 配置共享目录

服务启动之后，我们在服务端配置一个共享目录

```
$ sudo mkdir /data
$ sudo chmod 755 /data
```

根据这个目录，相应配置导出目录

```
$ sudo vi /etc/exports
```

添加如下配置

```
/data/     192.168.0.0/24(rw,sync,no_root_squash,no_all_squash)
```

1. `/data`: 共享目录位置。
2. `192.168.0.0/24`: 客户端 IP 范围，`*` 代表所有，即没有限制。
3. `rw`: 权限设置，可读可写。
4. `sync`: 同步共享目录。
5. `no_root_squash`: 可以使用 root 授权。
6. `no_all_squash`: 可以使用普通用户授权。

`:wq` 保存设置之后，重启 NFS 服务。

```
$ sudo systemctl restart nfs
```

可以检查一下本地的共享目录

```
$ showmount -e localhost
Export list for localhost:
/data 192.168.0.0/24
```

这样，服务端就配置好了，接下来配置客户端，连接服务端，使用共享目录。

## Linux 客户端

### 客户端安装

与服务端类似

```
$ sudo yum install nfs-utils
```

### 客户端配置

设置 rpcbind 服务的开机启动

```
$ sudo systemctl enable rpcbind
```

启动 NFS 服务

```
$ sudo systemctl start rpcbind
```

*`注意`*

> 客户端不需要打开防火墙，因为客户端时发出请求方，网络能连接到服务端即可。
> 客户端也不需要开启 NFS 服务，因为不共享目录。

### 客户端连接 NFS

先查服务端的共享目录

```
$ showmount -e 192.168.0.110
Export list for 192.168.0.110:
/data 192.168.0.0/24
```

在客户端创建目录

```
$ sudo mkdir /data
```

挂载

```
$ sudo mount -t nfs 192.168.0.101:/data /data
```

挂载之后，可以使用 `mount` 命令查看一下

```
$ mount
...
...
192.168.0.110:/data on /data type nfs4 (rw,relatime,sync,vers=4.1,rsize=131072,wsize=131072,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=sys,clientaddr=192.168.0.100,local_lock=none,addr=192.168.0.101)
```

这说明已经挂载成功了。

### 测试 NFS

测试一下，在客户端向共享目录创建一个文件

```
$ cd /data
$ sudo touch a
```

之后取 NFS 服务端 `192.168.0.101` 查看一下

```
$ cd /data
$ ll
total 0
-rw-r--r--. 1 root root 0 Aug  8 18:46 a
```

可以看到，共享目录已经写入了。

### 客户端自动挂载

自动挂载很常用，客户端设置一下即可。

```
$ sudo vi /etc/fstab
```

在结尾添加类似如下配置

```
#
# /etc/fstab
# Created by anaconda on Thu May 25 13:11:52 2017
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/cl-root     /                       xfs     defaults        0 0
UUID=414ee961-c1cb-4715-b321-241dbe2e9a32 /boot                   xfs     defaults        0 0
/dev/mapper/cl-home     /home                   xfs     defaults        0 0
/dev/mapper/cl-swap     swap                    swap    defaults        0 0
192.168.0.110:/data     /data                   nfs     defaults        0 0
```

由于修改了 `/etc/fstab`，需要重新加载 `systemctl`。

```
$ sudo systemctl daemon-reload
```

之后查看一下

```
$ mount
...
...
192.168.0.110:/data on /data type nfs4 (rw,relatime,vers=4.1,rsize=131072,wsize=131072,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=sys,clientaddr=192.168.0.100,local_lock=none,addr=192.168.0.101)
```

此时已经启动好了。如果实在不放心，可以重启一下客户端的操作系统，之后再查看一下。

## Windows 客户端

Windows 安装 NFS 客户端，不同的 Windows 版本，安装方式不大一样，本例列举几个。

| Windows             | 步骤                                            |
| :------------------ | :---------------------------------------------- |
| Windows Server 2008 | servermanagercmd.exe -install FS-NFS-Services   |
| Windows 7           | 程序和功能 - 启动或关闭 Widnows 功能 - NFS 服务 |
| Windows Server 2012 | 添加功能角色 - 添加文件打印服务 - NFS 客户端    |
| Windows 10          | 程序和功能 - 启动或关闭 Widnows 功能 - NFS 服务 |

### 客户端安装

本例的 Windows 为 `Windows Server 2008 R2`

```
C:> servermanagercmd.exe -install FS-NFS-Services
```

### 客户端配置

首先要了解服务端的文件夹权限，本例服务端 `/data` 目录的所有者为 `root`，查看一下 root 用户的信息

```
$ sudo id root
uid=0(root) gid=0(root) groups=0(root)
```

可以看到 `uid=0`, `gid=0`，需要在 Windows 客户端上进行配置，参考 [UID/GID using the registry entries](https://blogs.msdn.microsoft.com/sfu/2009/03/27/can-i-set-up-user-name-mapping-in-windows-vista/)

> **`注意`**
> 本例以 root 为例，生产环境要考虑安全因素，请修改为相应的有权限的用户

回到 Windows 进行配置

首先，启动注册表编辑器

```
C:> regedit
```

然后，进行如下步骤

1. 定位到这一项 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default`
2. 创建两个 DWORD 值，名称分别为 `AnonymousUid` 和 `AnonymousGid`
3. 设置 UID 和 GID 的值，本例设置为 `0`
4. 重启 Windows 操作系统 (或者重启 NFS Client 服务)

服务器重启之后，挂载文件夹，在 DOS 命令窗口输入命令

```
C:> mount 192.168.0.110:/data X:
```

这样，就将 NFS 服务端的共享文件夹挂载到了本地的 `X:` 盘，

也可以卸载掉这个驱动器，使用如下命令：

```
C:> umount X:
```

*`注意`*

> 通过此命令操作挂载，当服务器重启时，不会自动挂载。

登录时自动挂载，进行如下步骤

1. 点击此电脑
2. 在弹出的计算机对话框中，在工具栏找到 `映射网络驱动器`
3. 驱动器地址输入 `X:`
4. 文件夹输入 `192.168.0.110:/data`
5. 确认 `登录时重新连接` 是勾选的，这个配置表示登录时自动挂载共享目录。

### 客户端测试

Windows 操作都是有界面的，本例不做具体截图，可以点击进入 X 盘，创建文件夹试试，然后新建文件试试。

如果有问题，请确认一下服务端的文件加权限。