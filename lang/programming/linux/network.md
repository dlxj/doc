

# vmware

- https://zhuanlan.zhihu.com/p/130984945





```
yum install net-tools # ifconfig 
	# 没有的话用 ip addr show


 vi /etc/sysconfig/network-scripts/ifcfg-enp0s3  # 修改网卡配置

nmcli connection up ens33 # 使网卡配置生效

service network restart # 重启网络
	
```



```
# 查看显卡
lspci | grep -i vga
```



- https://www.hostnextra.com/kb/how-to-install-smartctl-utility-on-centos-7/

```
# 硬盘健康度
smartctl -A -d ata /dev/sda

smartctl -H -d ata /dev/sda
```



```
# 查看 raid 信息
lspci -v -s $(lspci | grep -i raid |awk ‘{print $1}’)


```



- https://www.dell.com/community/PowerEdge%E6%9C%8D%E5%8A%A1%E5%99%A8/dell-R720-raid1-%E5%A6%82%E4%BD%95%E6%8A%8A%E5%B0%8F%E5%AE%B9%E9%87%8F%E7%A1%AC%E7%9B%98%E6%9B%BF%E6%8D%A2%E6%88%90%E5%A4%A7%E5%AE%B9%E9%87%8F%E7%A1%AC%E7%9B%98/td-p/7578002

```
只有RAID 0、RAID 1、RAID 5、RAID 6支持增加硬盘扩容。
RAID10、RAID 50、RAID 60不支持增加硬盘扩容。
当硬盘组中包含了2个或2个以上的VD时，无法通过添加新硬盘扩容。
RAID卡不支持同时对两个RAID组进行重新配置（即“Reconfigure Virtual Drives”操作，包括进行加盘扩容或迁移RAID级别），请在当前进程完成后再对下一个RAID组进行操作。
对系统的影响
增加硬盘扩容过程中，如果出现硬盘故障，会导致：

若出现故障盘后，RAID中已无冗余数据（例如RAID 0扩容过程中出现1个故障盘），则RAID失效。
若出现故障盘后，RAID中仍存在冗余数据（例如RAID 1扩容过程中出现1个故障盘），则扩容操作会继续进行。需要等待扩容完成后，重新更换新硬盘并手动重构RAID。
请谨慎执行增加硬盘扩容操作。
```











