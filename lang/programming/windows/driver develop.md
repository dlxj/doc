

[PC Hunter](https://www.portablesoft.org/pc-hunter/) 大量使用了 Windows 内核技术，尤其是为了做一些检测而使用了些 Windows 未公开的内核数据结构，目前初步实现如下功能：

- 进程、线程、进程模块、进程窗口、进程内存信息查看，杀进程、杀线程、卸载模块等功能
- 内核驱动模块查看，支持内核驱动模块的内存拷贝
- SSDT、Shadow SSDT、FSD、KBD、TCPIP、Classpnp、Atapi、Acpi、SCSI、IDT、GDT信息查看，并能检测和恢复 ssdt hook 和 inline hook
- CreateProcess、CreateThread、LoadImage、CmpCallback、BugCheckCallback、Shutdown、Lego 等 Notify Routine 信息查看，并支持对这些 Notify Routine 的删除
- 端口信息查看，目前不支持2000系统
- 查看消息钩子
- 内核模块的 iat、eat、inline hook、patches 检测和恢复
- 磁盘、卷、键盘、网络层等过滤驱动检测，并支持删除
- 注册表编辑
- 进程 iat、eat、inline hook、patches 检测和恢复
- 文件系统查看，支持基本的文件操作
- 查看（编辑）IE插件、SPI、启动项、服务、Host文件、映像劫持、文件关联、系统防火墙规则、IME
- ObjectType Hook 检测和恢复
- DPC 定时器检测和删除
- MBR Rootkit 检测和修复
- 内核对象劫持检测
- WorkerThread 枚举
- Ndis 中一些回调信息枚举
- 硬件调试寄存器、调试相关API检测
- 枚举 SFilter/Fltmgr 的回调
- 系统用户名检测





