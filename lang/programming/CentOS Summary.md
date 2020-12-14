



默认Centos7没有安装p7zip安装包，默认源里面也没有这个安装包，需要安装epel源才能安装p7zip安装包[u](https://www.linuxprobe.com/centos7-7zip-compression.html)

```bash
[root@localhost ~]# yum -y install epel-release
[root@localhost ~]# yum -y install p7zip p7zip-plugins
```

