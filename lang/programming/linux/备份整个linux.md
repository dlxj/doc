https://blog.csdn.net/mmh19891113/article/details/81698453

备份前准备工作

在做整个系统的备份前我们要做一些准备工作。

```
在做整个系统的备份前我们要做一些准备工作。
删除所有的emails
清空你的浏览器的一些历史
取消挂载的硬盘等设备
删除家目录里你不想要备份的文件
```




开始备份



```
备份需要使用root账号。我们执行sudo su - root 切换到root账号下面。
切换目录到根目录
cd  /
执行tar命令备份
tar -cvpzf backup.tar.gz --exclude=/backup.tar.gz --one-file-system / 

c 创建的意思- create a new backup archive.
v 显示详细信息- verbose mode, tar will print what it's doing to the screen.
p 保持文件权限- preserves the permissions of the files put in the archive for restoration later.
z 使用gzip压缩- compress the backup file with 'gzip' to make it smaller.
f <filename> 备份后生成的文件- specifies where to store the backup, backup.tar.gz is the filename used in this example. 
				It will be stored in the current working directory, the one you set when you used the cd command.

--exclude=/example/path 排除某个路径不去备份- The options following this model instruct tar what directories NOT to backup. 
				We don't want to backup everything since some directories aren't very useful to include. 
				The first exclusion rule directs tar not to back itself up, this is important to avoid errors during the operation.

--one-file-system 的意思是 不包含其他文件系统- Do not include files on a different filesystem

```





另外一种使用完全手动指定备份目录，不备份的目录



```
cd / # THIS CD IS IMPORTANT THE FOLLOWING LONG COMMAND IS RUN FROM /

tar -cvpzf backup.tar.gz \
--exclude=/backup.tar.gz \
--exclude=/proc \
--exclude=/tmp \
--exclude=/mnt \
--exclude=/dev \
--exclude=/sys \
--exclude=/run \ 
--exclude=/media \ 
--exclude=/var/log \
--exclude=/var/cache/apt/archives \
--exclude=/usr/src/linux-headers* \ 
--exclude=/home/*/.gvfs \
--exclude=/home/*/.cache \ 
--exclude=/home/*/.local/share/Trash /
```





备份后切分为小的文件

```
通过管道一次行的切分好文件
tar -cvpz <put options here> / | split -d -b 3900m - /name/of/backup.tar.gz. 

这个是打包后在单独切分文件
split -d -b 3900m /path/to/backup.tar.gz /name/of/backup.tar.gz. 

切分后的文件怎么解压
cat *tar.gz* | tar -xvpzf - -C /  
```





通过网络备份



```
接收端
nc -l 1024 > backup.tar.gz 

发送端
tar -cvpz <all those other options like above> / | nc -q 0 <receiving host> 1024 


更好的方式通过ssh传输
tar -cvpz <all those other options like above> / | ssh <backuphost> "( cat > ssh_backup.tar.gz )"

```





怎么恢复



```
把硬盘挂载到/media 下面
ls /media
sudo tar -xvpzf /path/to/backup.tar.gz -C /media/whatever --numeric-owner

mkdir /proc /sys /mnt /media 

# 恢复 grub
sudo -s
for f in dev dev/pts proc ; do mount --bind /$f /media/whatever/$f ; done
chroot /media/whatever
dpkg-reconfigure grub-pc

```




我备份打包这个系统是准备作为一个docker image来使用的



```
使用docker导入我们刚刚备份的文件
docker import  /path/to/your.tar.gz
最后可以导入成功的，然后还可以运行起来。这样里面的环境都是我们之前物理系统上的，之前安装好的软件，配置号的环境都是存在的。

docker import backup.tar.gz bs-ubuntu-14.04
 
docker run -it bs-ubuntu-14.04 /bin/bash
```








