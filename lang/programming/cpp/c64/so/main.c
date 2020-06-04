//main.c ���Զ�̬����ʽ���õĳ���  
#include <stdio.h>
#include <dlfcn.h>  //���ڶ�̬������ϵͳͷ�ļ�    

//#define NULL 0

//#include "myalib.h"//Ҫ�Ѻ�����ͷ�ļ������������������ʱ�ᱨ��  
int main(int argc,char* argv[])  
{  
//������Ӧ�ĺ����ĺ���ָ��  
void (*pTest)();  
 //���ض�̬��  
void *pdlHandle = dlopen("./libtest.so", RTLD_LAZY);  
//������  
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
//��ȡ�����ĵ�ַ  
pTest = dlsym(pdlHandle, "test");  
pszErr = dlerror();  
if(pszErr != NULL)  
{  
printf("%s\n", pszErr);  
dlclose(pdlHandle);  
return -1;  
}  
//ʵ�ֺ�������  
(*pTest)();  
//�������ʱ�رն�̬��  
dlclose(pdlHandle);  
return 0;    
} 
