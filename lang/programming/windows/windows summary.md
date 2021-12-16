### windows Long path

1. Open the Start menu and type “regedit.” Launch the application.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Right-click the value “LongPathsEnabled” and select Modify.
4. Change “Value data” from 0 to 1.
5. Click OK.



# 无法在分区上安装windows

```
rufus-3.17
二、无法在驱动器0分区上安装windows解决方法
1、在当前安装界面按住Shift+F10调出命令提示符窗口；
2、输入diskpart，按回车执行；
3、进入DISKPART命令模式，输入list disk回车，列出当前磁盘信息；
4、要转换磁盘0格式，则输入select disk 0回车，输入clean，删除磁盘分区；
5、输入convert mbr，回车，将磁盘转换为MBR，输入convert gpt则转为GPT；
6、最后输入exit回车退出命令提示符，返回安装界面继续安装系统。
7、然后点击新建磁盘就可以安装驱动。

记住：最重要的是，完成以上步骤之后，返回刚开始的界面重新点击安装Windows，之后，才可以。

作者：He_Yu
链接：https://www.jianshu.com/p/e747d9cb3153
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

