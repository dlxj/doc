

## 再论网上解决macbook升级第三方ssd后休眠睡死的问题



2020.1.29更新：建议经费充足的朋友直接买Intel 760p、Intel 7600P、Intel 660p、西数SN720这四款固态硬盘。实测这四种固态硬盘均无需调整pmset参数，直接能在hibernatemode=3模式下完美休眠。其中7600p功耗比原装更低，发热量更小。

2020.2.2更新：暂时不要升级Catalina，休眠有问题！

 

型号：A1466, Macbook Air early 2015, 4G 内存

OS: Mojave 10.14.5

升级ssd型号：建兴LITEON CA3-8D512

众所周知，自己动手升级非官方的SSD最害怕遇到休眠睡死问题。大家经常用pmset命令来将hibernatemode改为25。然而实际上这是个治标不治本的方法。hibernatemode受standbydelayhigh和standbydelaylow两个参数限制。其原理应该是在hibernatemode 3情形下，其休眠受standbydelayhigh和standbydelaylow的两个数值之间的某个时间点，机器自动将内存里的数据写入到硬盘。而第三方的硬盘往往无法在此过程中被识别出来，导致了长时间休眠后睡死唤不醒。

测试到底第三方ssd能否完美兼容的方法很简单：

1、查询现有电源模式

pmset -g custom
应该可以看到默认情况下，standbydelayhigh = 86400 （24小时）， standbydelaylow=10800(3小时）

2、修改hibernatemode为25

sudo pmset -a hibernatemode 25
这个步骤做完了应该看起来休眠问题解决了，其实不然。

3、调整standbydelayhigh和standbydelaylow两个参数

sudo pmset standbydelayhigh =300
300单位是秒，可以调成任何一个时间。注意两个参数一大一小。

4、合盖休眠到300秒后打开看下是不是睡死的问题又来了？

那么，反其道而行之，对于不支持hibernatemode 3的第三方SSD，我们可以在设置hibernatemode为25的同时将这两个参数设置成较大的数值，然后避免在日常使用中电脑进入休眠状态。这样能一定程度上解决睡死问题。代价是唤醒比较慢，同时放置超过设定时间后可能有文件丢失的风险。

附录：关于pmset参数，可以用man pmset查看： 

     hibernatemode = 0 (binary 0000) by default on supported desktops. The
     system will not back memory up to persistent storage. The system must
     wake from the contents of memory; the system will lose context on power
     loss. This is, historically, plain old sleep.
     
     hibernatemode = 3 (binary 0011) by default on supported portables. The
     system will store a copy of memory to persistent storage (the disk), and
     will power memory during sleep. The system will wake from memory, unless
     a power loss forces it to restore from disk image.
     
     hibernatemode = 25 (binary 0001 1001) is only settable via pmset. The
     system will store a copy of memory to persistent storage (the disk), and
     will remove power to memory. The system will restore from disk image. If
     you want "hibernation" - slower sleeps, slower wakes, and better battery
     life, you should use this setting.
简单翻译下，0是直接休眠不把内存镜像写入硬盘，唤醒时从内存恢复，是桌面版mac的默认设置； 3是把内存镜像写入磁盘的同时也给内存供电，直到电池临界值。唤醒的时候从内存唤醒，除非内存断电了那就从硬盘唤醒，速度可快可慢，取决于休眠多久，是移动版mac的默认设置；25是把内存镜像写入磁盘，断开内存供电，唤醒的时候从硬盘读取，速度较慢。


