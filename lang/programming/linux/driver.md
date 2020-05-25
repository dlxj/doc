   sudo ubuntu-drivers autoinstall



## 无法正常关机

在终端输入以下命令：

sudo gedit /etc/default/grub
1
找到这一行：GRUB_CMDLINE_LINUX_DEFAULT=”quiet splash”
改成：GRUB_CMDLINE_LINUX_DEFAULT=”quiet splash acpi=force pci=nomsi”
保存退出。

输入以下命令更新Grub：

sudo update-grub


在终端输入命令：sudo gedit /boot/grub/grub.conf 在文中的最后输入：apm=power_off acpi=on（我的grub.conf文件中没有东西，开始的时候，还不是很相信，后来还是加上试了一下就可以了）。



```bash
find . -type f | xargs cat | 
 grep "<p>.*仁.*<span class='note-inline'>(\[CloseCurlyDoubleQuote]
  仁者(而親反周禮云德一曰仁鄭玄曰愛人及物曰仁上下相親曰仁釋名仁者忍也好生惡煞善惡含忍也)。
```

