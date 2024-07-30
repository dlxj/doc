

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



# soda

```
PID=17272
名称=chrome
路径=C:\Program Files\Google\Chrome\Application\chrome.exe
命令行参数=--type=utility --utility-sub-type=media.mojom.SpeechRecognitionService --lang=zh-CN --service-sandbox-type=speech_recognition --video-capture-use-gpu-memory-buffer --field-trial-handle=2060,i,416351341486393937,12593638908818774446,262144 --variations-see

搜字符串可能可以找到创健进程的地方？  SpeechRecognitionService

火绒的安全分析工具 -> 进程 -> 在 chrome top 进程搜字符串，能搜到

单进程模式：
	“快捷方式”选项卡。 你需要做的就是在“目标”的路径后面加上下面这个参数:" --single-process"
	
	"C:\Program Files\Google\Chrome\Application\chrome.exe" --single-process
	
	breakpoint这个回调，我在x64dbgpy中使用了，的确很迅速，好用。
	

```



## windbg

```

在调试父进程时使用.childdbg命令

```





# debugger tools

https://down.52pojie.cn/Tools/Debuggers/

https://bbs.kanxue.com/forum-10.htm

```
https://bbs.kanxue.com/thread-277984.htm
位大佬，应该是俄罗斯的，收集了IDA历次版本(Demo/Free/Leak)，从0.1到8.3，在		http://fckilfkscwusoopguhi7i6yg3l6tknaz7lrumvlhg5mvtxzxbbxlimid.onion/  
	# 暗网？
	https://blog.smallfang.us/cn/0012/

```



## 子进程插件

https://github.com/therealdreg/DbgChild



## jdk

```
# see huggingface\gasr\readme.txt
vi ~/.bashrc 
export JAVA_HOME=/root/jdk-21.0.4+7/
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar　
source ~/.bashrc
	# jdk 配置
```



