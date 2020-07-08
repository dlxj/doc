[TOC]



# mingw32 summary



## libeb16-dev for epwing



环境变量path 添加：E:\mingw32\bin



g++ -c main.c

g++ main.o -o main.exe

g++ -I"d:\workcode\cpp\libeb16-dev-windows\include"  -c main.c



apt-get install zlib1g.dev



```bash
g++ -I"d:\workcode\cpp\libeb16-dev-windows\include"  -L"D:\workcode\cpp\libeb16-dev-windows\lib"  -leb  -c main.c
g++ main.o -o main.exe
main.exe
cmd.exe
```





```c
#include "stdio.h"

/*
#include <eb/text.h>
#include <eb/appendix.h>
#include <eb/error.h>
#include <eb/binary.h>
#include <eb/font.h>
*/

int main() {
    
    EB_Book book;

	EB_Error_Code ret = eb_bind(&book, "E:\\GoldenDict\\content\\NHK");
    
	char c;
	printf("hi,,,");
	//c = getchar();
	return 0;
}
```





## libeb16-dev ubuntu



./configure

make && make install



```
test -z "/usr/local/lib" || /bin/mkdir -p "/usr/local/lib"
 /bin/bash ../libtool   --mode=install /usr/bin/install -c  'libeb.la' '/usr/local/lib/libeb.la'
libtool: install: /usr/bin/install -c .libs/libeb.so.16.0.0 /usr/local/lib/libeb.so.16.0.0
libtool: install: (cd /usr/local/lib && { ln -s -f libeb.so.16.0.0 libeb.so.16 || { rm -f libeb.so.16 && ln -s libeb.so.16.0.0 libeb.so.16; }; })
libtool: install: (cd /usr/local/lib && { ln -s -f libeb.so.16.0.0 libeb.so || { rm -f libeb.so && ln -s libeb.so.16.0.0 libeb.so; }; })
libtool: install: /usr/bin/install -c .libs/libeb.lai /usr/local/lib/libeb.la
libtool: install: /usr/bin/install -c .libs/libeb.a /usr/local/lib/libeb.a
libtool: install: chmod 644 /usr/local/lib/libeb.a
libtool: install: ranlib /usr/local/lib/libeb.a
libtool: finish: PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/sbin" ldconfig -n /usr/local/lib
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib
```





linux下编译，常会遇到后缀为：.o .so .a .la .ko等格式文件，尽管linux并不以扩展名作为识别文件格式的唯一依据，但规范约定还是有的，如下：

- .o 是目标对象文件,相当于windows中的.obj文件
- .a 为静态库，可以是一个或多个.o合在一起,用于静态连接
- .la 为libtool生成的共享库，其实是个配置文档。可以用$file *.la查看*.la文件，或用vi来查看。
- .so 为共享库，类似windows平台的dll文件

补充： 还有一种扩展名为.ko 文件，不过它是Linux内核使用的动态链接文件后缀，属于模块文件，用来在Linux系统启动时加载内核模块。







