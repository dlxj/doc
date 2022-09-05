

# vmware

- https://zhuanlan.zhihu.com/p/130984945





```
yum install net-tools # ifconfig 
	# 没有的话用 ip addr show


 vi /etc/sysconfig/network-scripts/ifcfg-enp0s3  # 修改网卡配置

nmcli connection up ens33 # 使网卡配置生效

service network restart # 重启网络
	
```









