[TOC]



# mingw32 summary



## libeb16-dev for epwing



环境变量path 添加：E:\mingw32\bin



g++ -c main.c

g++ main.o -o main.exe

g++ -I"d:\workcode\cpp\libeb16-dev-windows\include"  -c main.c

-L"e:\Qt\4.8.7\lib"



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









