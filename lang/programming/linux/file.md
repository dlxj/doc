

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





