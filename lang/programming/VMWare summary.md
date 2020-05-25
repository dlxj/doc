

[TOC]

# VMWare summary



![image-20200525170251271](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200525170251271.png)



mount /dev/cdrom /mnt

cd /mnt





## Key



```
VMware Workstation 15 Pro

官方下载链接：https://download3.vmware.com/software/wkst/file/VMware-workstation-full-15.0.0-10134415.exe

永久许可证：ZC10K-8EF57-084QZ-VXYXE-ZF2XF

附：备用许可项

UF71K-2TW5J-M88QZ-8WMNT-WKUY4

AZ7MK-44Y1J-H819Z-WMYNC-N7ATF

CU702-DRD1M-H89GP-JFW5E-YL8X6

YY5EA-00XDJ-480RP-35QQV-XY8F6

VA510-23F57-M85PY-7FN7C-MCRG0
```



NAT 可以理解为虚拟机集群里的虚拟的局域网

NAT模式，这种模式下，虚拟机与所在的物理机单独组成了一个新的局域网，他们共享接入物理机的IP段

局域网内的其他计算机相对于虚拟机和物理机新组的局域网来说属于外网，这时候还需要在物理机中对其进行端口映射，这个与局域网中利用路由器对其中某个IP端口进行映射的原理是一样的，通过这种也可以实现局域网访问虚拟机内的服务



感觉最简单的就是 代理软件端口改成 0.0.0.0:8080，虚拟机只要能 ping 通物理主机，虚拟机就用物理主机 ip:8080 进行代理





## Proxy Setting



#### ss选择允许其他设备连入



#### Ubuntu 网络设置

1. 桥接模式（不是NAT）
2. Ubuntu18.04 ->Setting->System Settings->Network
3. Option ->IPV4Settings  ->Method ->Manual ->Add
4. 添加与主机不同的局域网IP地址。点击save保存
5. 点击Wired右侧的开关重启一下
6. 此时你的Ubuntu应该可以正常上网了



#### 代理设置



Network proxy 在右侧的Method选择Manual ，然后在下面的Proxy中全部填写主机的IP地址和代理端口，到此代理设置完成



![image-20200525160259244](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200525160259244.png)







