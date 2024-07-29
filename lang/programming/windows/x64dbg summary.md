

# dll

```
根据这个思路，我们从rundll32开始调试就好了

x64dbg打开"C:\Windows\System32\rundll32.exe"，32位应该是"C:\Windows\SysWOW64\rundll32.exe"
文件->改变命令行，补充dll路径和导出函数名，例如: "C:\Windows\SysWOW64\rundll32.exe" "C:\Users\alice\Desktop\hello.dll",sayhello
选项->选项->事件(当以下事件发生时暂停:)，勾选"用户DLL入口"
运行到要调试的dll入口时，切换到"符号"窗口，选择要调试的dll，在相应的导出函数下断点，
继续运行即可在指定的导出函数开始处断下

如果调试的dll要访问额外的文件，注意当前文件夹是rundll32.exe所在的文件夹
```



```
"C:\Windows\System32\rundll32.exe" "E:\SODA.dll",CreateExtendedSodaAsync 
```



