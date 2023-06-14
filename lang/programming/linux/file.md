

df -h shows disk space in human-readable format



show all soft link in a dir

  find dir -type l



file /usr/bin/vncserver

  /usr/bin/vncserver: symbolic link to `/etc/alternatives/vncserver'



show size of file(s)

  ls -s



biggest files

  du -Sh | sort -rh | head -n 15



## 当前目录大小



```bash
du -h --max-depth=1 your_dest_dir
```



统计当前目录下文件的个数（不包括目录）

```bash
$ ls -l | grep "^-" | wc -l
```



查看某目录下文件夹(目录)的个数（包括子目录）

```bash
$ ls -lR | grep "^d" | wc -l
```



[root@localhost 11]# du -h --max-depth=0 .
185G	.
[root@localhost 11]# ls -l | grep "^-" | wc -l
128947



## 磁盘扩容

- https://itcn.blog/p/19501309720.html home多余磁盘扩容给root





# cp 参数过长

```
find img_origin/ -name "*.txt" | xargs -i cp {} img

xargs命令是给其他命令传递参数的一个过滤器，也是组合多个命令的一个工具。-i会将xargs的内容赋值给{}。

```



# mount

```
umount /mnt

```

## ntfs分区权限错误 

```
You:
linux中root账号为什么没有目录的写入权限，那个目录的所有者是其他账号

ChatGPT:
在Linux中，root用户（也称为超级用户）在默认情况下对系统中的所有文件和目录都具有读、写、执行的权限。这是因为root用户拥有最高的权限级别，可以对系统进行任何更改。   

如果root用户不能写入某个特定的目录，可能的原因包括：

1. 
目录的权限被特别修改了：虽然root用户在默认情况下有所有的权限，但是某些情况下，系统管理员可能会特别地修改某个目录的权限，以防止任何用户（包括root用户）进行修改。这
情况下，你可以使用`chmod`命令修改这个目录的权限。

2. 文件系统被挂载为只读：如果文件系统被挂载为只读模式，那么任何用户（包括root用户）都不能对其进行写操作。在这种情况下，你需要重新挂载文件系统为读写模式。

3. 文件系统有错误：如果文件系统有错误，或者磁盘已满，那么可能无法写入文件或目录。

4. 
目录被设置了特殊的属性或ACL权限：Linux系统中可以通过设置属性或ACL权限来进一步控制对文件或目录的访问，如果设置了这些特殊的权限，那么可能会影响到root用户的访问权限 
。

总的来说，虽然root用户在默认情况下具有所有权限，但是还是可能会遇到无法写入某个目录的情况，这时候需要根据具体的情况来进行排查和处理。

You:
mount 命令有一行的输出是这样的：/dev/sda1 on /mnt type fuseblk (ro,noatime,user_id=0,group_id=0,default_permissions,allow_other,blksize=4096)  ，那么这个 /mnt    
目录 root 账号有没有写入权限

ChatGPT:
根据你给出的 mount 命令的输出，`/dev/sda1` 已经被挂载到 `/mnt` 目录，而且是以只读模式（ro）进行挂载的。在这种情况下，不论是哪个用户（包括 root 用户）都无法对     
`/mnt` 目录进行写操作。如果你希望 root 用户能够对这个目录进行写操作，你需要将其重新挂载为读写模式。

下面是一个重新挂载为读写模式的例子：

​```bash
mount -o remount,rw /mnt
​```

在这个命令中，`-o` 参数用于指定挂载选项，`remount,rw` 表示重新挂载并且使用读写模式。`/mnt` 是你要重新挂载的目录。请注意，运行这个命令可能需要 root 权限。

另外，请确保你知道重新挂载为读写模式可能会带来的风险，例如，如果 `/dev/sda1` 文件系统本身存在问题，那么进行写操作可能会导致数据丢失。

You:
这个问题怎么解决： mount -o uid=26,gid=26,dmask=077,fmask=077 -t ntfs-3g /dev/sda1 /mnt
The disk contains an unclean file system (0, 0).
Metadata kept in Windows cache, refused to mount.
Falling back to read-only mount because the NTFS partition is in an
unsafe state. Please resume and shutdown Windows fully (no hibernation
or fast restarting.)
Could not mount read-write, trying read-only

ChatGPT:
这个错误通常发生在尝试在Linux中挂载Windows分区时。Windows使用了快速启动或休眠模式，这将使得Windows在关闭时仍然保持对硬盘的一些控制，使得Linux不能完全访问这个分区 
，尤其是以写入模式访问。

解决这个问题的最直接的方法是重启你的Windows系统，然后完全关闭它，而不是让它进入休眠模式或者使用快速启动。以下是详细的步骤：

1. 在Windows中，打开"控制面板" -> "硬件和声音" -> "电源选项"。
2. 在左侧菜单中选择 "选择电源按钮的功能"。
3. 点击 "更改当前不可更改的设置"。
4. 去掉 "启用快速启动 (推荐)" 的勾选，然后保存更改。

此外，确保你在重启Windows时没有选择 "休眠" 或 "睡眠"。你应该选择 "关机" 或 "重新启动"。

在完成以上操作后，你应该就能够在Linux中以读写模式挂载Windows分区了。如果你仍然遇到问题，你可能需要在Windows中检查并修复文件系统。这可以通过在Windows中打开命令提示
符，然后运行如下命令完成：

​```shell
chkdsk /f <drive>:
​```

其中， `<drive>` 是你要检查的驱动器的字母。例如，如果你要检查 C 驱动器，你可以运行 `chkdsk /f C:`。这个命令将会在下次重启Windows时运行，并检查并修复文件系统错误。
```

