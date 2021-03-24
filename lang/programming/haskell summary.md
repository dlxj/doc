

```
# mario
https://github.com/GunioRobot/monao

# sdl lib
apt-get install libsdl1.2-dev libsdl-mixer1.2-dev

# haskll binding
https://github.com/keera-studios/hssdl
https://hackage.haskell.org/package/SDL-mixer

```

/haskell/monao-master# make configure

```
runhaskell Setup.lhs configure
Configuring monao-0.0.1...
Setup.lhs: Encountered missing dependencies:
SDL-mixer -any
```


https://github.com/GunioRobot/monao

https://gist.github.com/BoredBored/3187339a99f7786c25075d4d9c80fad5

https://github.com/keera-studios/hssdl

https://hackage.haskell.org/package/SDL-mixer



/usr/local/lib/x86_64-linux-ghc-8.0.2/SDL-0.6.6-4rCPAt8MGQyDlL8vy3uVTM
Registering SDL-0.6.6...



# VMWare



```
C:\Users\i>ipconfig

Windows IP 配置

以太网适配器 以太网:

   连接特定的 DNS 后缀 . . . . . . . :
   IPv4 地址 . . . . . . . . . . . . : 192.168.0.163
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . : 192.168.0.1

以太网适配器 VMware Network Adapter VMnet1:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : fe80::98c9:f45e:1538:bab5%26
   IPv4 地址 . . . . . . . . . . . . : 192.168.136.1
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . :


vm@ubuntu:~$ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.163.129  netmask 255.255.255.0  broadcast 192.168.163.255
        inet6 fe80::ae7a:43d3:ee0a:45cc  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:97:e9:27  txqueuelen 1000  (Ethernet)
        RX packets 11641  bytes 14714202 (14.7 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5469  bytes 407853 (407.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 397  bytes 35115 (35.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 397  bytes 35115 (35.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


# 
VMWare：编辑>虚拟网络编辑器
	点VMnet8 NAT模式这一行 >NAT设置 > 添加 > 端口填22，IP 填虚拟机ifconfig 出来的地址
	
# 成功
vm@ubuntu:~$ ping 192.168.0.163   # ping真机
C:\Users\i>  ping 192.168.163.129 # ping虚拟


```



# ssh

```
https://cloud.tencent.com/developer/article/1679861
```





```
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock
sudo rm /var/cache/apt/archives/lock
都运行一遍，具体也不知道哪条起了作用。

用 lsof 命令看看这几个文件是被哪个进程锁住的啊，然后先杀掉那几个进程。

不杀进程，直接移除文件的话，可能仍有其他进程在操作 apt 的缓存，多个命令同时写 apt 缓存很容易发生冲突。
```



# 防火墙

```
https://blog.csdn.net/Manipula/article/details/91491699
```





