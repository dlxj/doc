一、修复MBR：
    MBR（Master Boot Record主引导记录）：

        硬盘的0柱面、0磁头、1扇区称为主引导扇区。其中446Byte是bootloader，64Byte为Partition table，剩下的2Byte为magic number。

 



    备份MBR：
    
        #dd if=/dev/sda of=/root/mbr.bak count=1 bs=512

 



    破坏bootloader：
    
        #dd if=/dev/zero of=/dev/sda count=1 bs=200
    
        这里边block size只要小于等于446即可。

 



    修复方式：
    
        1、借助其他系统挂载磁盘修复。
    
            修复方式同光盘修复类似，也是使用grub2-install命令。

 



        2、借助安装光盘修复。
    
            1.装入光盘，在光盘引导界面选择troubleshooting：


​                    

            2.选择进入救援模式：


​                   

            3.按回车键继续：


​                    

            4.进入磁盘挂载选择模式：
    
                磁盘将会被挂载至/mnt/sysp_w_picpath/下



continue 以rw方式挂载分区。

read only 以ro方式挂载分区。

skip 跳过，将来自己手工挂载磁盘。

            5.选择continue，稍等片刻，提示已经挂载完成。


​                        

​                        

            6.此时进入救援模式的命令行： 


​                     

            7.使用grub2-install命令重建bootloader：
    
                #grub2-install root-directory=/mnt/sysp_w_picpath /dev/sda


​                    

                 显示无错误，使用sync写入硬盘，reboot重启系统。
    
            8.重启后无错误，grub正常运行：


​                    

                至此，MBR修复完成。

 





二、修复grub
    grub配置文件丢失：

        开机后会直接进入grub界面，显示为grub>：


​        

        修复步骤如下：
    
        grub>insmod xfs
    
        grub>set root=(hd0,1)
    
        grub>linux16 /vmlinuz-xxxxx root=/dev/mapper/centos-root
    
        grub>initrd16 /initramfs-.xxxxx.img


​            

    修复完成后即可进入系统，重建配置文件。
    
    注意：CentOS7因为使用的是grub2，配置文件同grub有不少变化，一定要切记备份grub.cfg以便恢复。

列外：

1. 
win pe修复win7引导后centos7引导消失的恢复方法： 
步骤（一）：用centos iso 制作启动u盘进入到安装centos的界面，开机选择的时候不要选择安装centos,而是选择trouble shooting疑难解答选项，然后选择rescue a centos system。按tab键选择continue (一定要选），然后选择ok. 
步骤（二）: 进入命令行界面，输入：chroot /mnt/sysp_w_picpath ，接着就是重要的一步，安装grub2了。执行以下命令： /sbin/grub2-install /dev/sda， 安装成功后执行reboot重新启动系统。但是以上步骤只是又把centos的启动项找回来了，windows7的引导又不见了，win7的引导需要在后续步骤通过grub2来完成。

2. 
恢复centos引导后继续恢复windows7引导的方法： 
经过前面所述步骤之后centos系统又能打开了，所以可以直接通过centos的grub2功能实现windows的引导。此时可以输入此命令直接搞定：grub2-mkconfig -o /boot/grub2/grub.cfg，然而，输入该命令后并没有发现与window相关的任何信息，纠结了半天发现是centos不能识别本人win7系统的磁盘格式。也就是说使用上述命令的前提是centos能够识别windows7系统的磁盘格式。

由于本人的windows7系统安装在ntfs格式的分区中，所以我先安装ntfs-3g，使centos能识别出windows所在的分区。

步骤（一）：安装ntfs-3g的步骤如下：

添加ntfs-3g下载源， 输入： 
wget -O /etc/yum.repos.d/epel.repo  http://mirrors.aliyun.com/repo/epel-7.repo 
更新yum，输入： 
yum update 
开始安装ntfs-3g，输入： 
yum install ntfs-3g 
至此，ntfs-3g安装完毕，只要成功安装了ntfs-3g, 那么恢复win7启动项的光辉时刻就已经到了，并且，步骤及其简单，您只需再次输入之前提到的命令：
grub2-mkconfig -o /boot/grub2/grub.cfg， 系统就能自动找到win7系统或xp系统的引导项，并加入到了grub.cfg菜单中。这样就避免了手工改动文件的危险，并且所有系统都能正常启动。不过，我多此一举的使用以下命令挂载了 windows NTFS 的分区（我的 Windows 分区分别是 /dev/sda1、 /dev/sda2、 /dev/sda4），注意：挂载是不必要的，因为在这个步骤中我们的真正目的是恢复win7的启动项，作为一个linux小白，我只是借此场景熟悉一下mount命令的用法而已。我用以下命令分别挂载了通过 grub2-mkconfig -o /boot/grub2/grub.cfg命令搜索到的所有windows分区： 
cd /mnt 
mkdir forwin 
mount -t ntfs-3g /dev/sda1 /mnt/forwin 
mkdir forwin2 
mount -t ntfs-3g /dev/sda2 /mnt/forwin2 
mkdir forwin3 
mount -t ntfs-3g /dev/sda4 /mnt/forwin3