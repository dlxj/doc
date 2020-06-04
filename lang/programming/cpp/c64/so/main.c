//main.c 测试动态库显式调用的程序  
#include <stdio.h>
#include <dlfcn.h>  //用于动态库管理的系统头文件    

//#define NULL 0

//#include "myalib.h"//要把函数的头文件包含进来，否则编译时会报错  
int main(int argc,char* argv[])  
{  
//声明对应的函数的函数指针  
void (*pTest)();  
 //加载动态库  
void *pdlHandle = dlopen("./libtest.so", RTLD_LAZY);  
//错误处理  
if(pdlHandle == NULL ){  
printf("Failed load library\n");  
return -1;  
}  
char* pszErr = dlerror();  
if(pszErr != NULL)  
{  
printf("%s\n", pszErr);  
return -1;  
}  
//获取函数的地址  
pTest = dlsym(pdlHandle, "test");  
pszErr = dlerror();  
if(pszErr != NULL)  
{  
printf("%s\n", pszErr);  
dlclose(pdlHandle);  
return -1;  
}  
//实现函数调用  
(*pTest)();  
//程序结束时关闭动态库  
dlclose(pdlHandle);  
return 0;    
} 
