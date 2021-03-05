[TOC]

# windows



## dll



### stdcall

```
#pragma comment(lib, "FreeImage.lib")

https://github.com/node-ffi/node-ffi/blob/master/example/factorial/factorial.c

#include <stdint.h>
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
EXPORT uint64_t factorial(int max) {
    int i = max;
    uint64_t result = 1;
    while (i >= 2) {
        result *= i--;
    }
    return result;
}  


var FFI = require('ffi');
var hi = new FFI.Library('hi', {
   'factorial': [
      'int32', ['int32']
   ]
});
console.log ( hi.factorial(3) );

原因：win7下的64位系统，在运行程序的时候，需要的DLL必须是64位系统编译的，VS2010也必须在安装的时候，选择了32位编译的支持。如果安装的时候，已经选择了，那么出现该问题的解决办法：

      （1）右键项目名，点击属性，弹出项目属性页，找到链接器----高级，修改右侧的目标计算机，选择有X64的那个选项。

      （2）右键项目名，选择清理解决方案，清理完之后选择X64平台编译器，然后重新生成解决方案，便可以调试成功。选择X64平台编译器如下图：


```







### _cdecl

```


extern "C" __declspec(dllexport)  int __cdecl reconize(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness) {


calldll
int dll() {
    typedef int(_cdecl*FunctionPtr)(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness);
    //typedef int(_stdcall*FunctionPtr)(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness);
    
    //reconize(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness);
    char *imageName = "IMG_0167.JPG";
    char *fileName = "hi.txt";
    char *buf = (char*)malloc(1024*1024*3);
    memset(buf, 0, 1024 * 1024 * 3);
    HINSTANCE   ghDLL = NULL;
    FunctionPtr   reconize;
    ghDLL = LoadLibrary("rec32160622.dll");
    ASSERT(ghDLL != NULL);
    reconize = (FunctionPtr)GetProcAddress(ghDLL, "reconize");
    ASSERT(reconize != NULL);
    //reconize(imageName, buf);
    reconize("IMG_1119.jpg", buf, 100, 4, 0.4, 125);
    //dataWrite(fileName, buf, strlen(buf));
    //fprintf(stdout, buf);
    printf("done.");
    free(buf);
    getchar();
    return 0;
} 


2)_cdecl调用
   _cdecl是C/C++的缺省调用方式，参数采用从右到左的压栈方式，由调用者完成压栈操作 ，传送参数的内存栈由调用者维护。
   _cedcl约定的函数只能被C/C++调用，每一个调用它的函数都包含清空堆栈的代码，所以产生的可执行文件大小会比调用_stdcall函数的大。
   按C编译方式，_cdecl调用约定仅在输出函数名前面加下划线，形如_functionname。
   按C++编译方式，可参看（三）


 
```









[语法糖](https://www.zhihu.com/question/298981020)

```c++
std::tuple<int,string> nextToken(){
    return {4,"fallthrough"};
}
auto[tokenType,lexeme] = nextToken();
```



vscode configure

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/textrank",
            "args": ["/home/ubuntu/workcode/gitlab/cpp/textrank-master/data/abc.txt", "1", "2", "./out.txt"],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```



https://launchpad.net/~codeblocks-devs/



[string](https://github.com/chenshuo/recipes/blob/master/string/StringTrivial.h)



```python
 // In C++11, this is unifying assignment operator
  String& operator=(String rhs) // yes, pass-by-value
  {
    // http://en.wikibooks.org/wiki/More_C++_Idioms/Copy-and-swap
    swap(rhs);
    return *this;
  }

  // C++11 move-ctor
  String(String&& rhs) noexcept
    : data_(rhs.data_)
  {
    rhs.data_ = nullptr;
  }

  /* Not needed if we have pass-by-value operator=() above,
   * and it conflits. http://stackoverflow.com/questions/17961719/
  String& operator=(String&& rhs)
  {
    swap(rhs);
    return *this;
  }
  */
```



sudo add-apt-repository ppa:codeblocks-devs/release

sudo apt update

sudo apt install codeblocks codeblocks-contrib



sudo add-apt-repository --remove ppa:codeblocks-devs/release

sudo apt remove --autoremove codeblocks codeblocks-contrib



右值引用（&&），move语义（std::move）和完美转发（std::forward<T>(t)）啦

nullptr

lambda表达式（匿名函数对象）

类的非静态成员在声明时赋值

auto_ptr 被弃用，应使用 unique_ptr

C 语言风格的类型转换被弃用，应该使用 static_cast、reinterpret_cast、const_cast 来进行类型转换

快速组装一个函数对象的bind绑定器

新增了一个容器——元组（tuple）

线程库第一次被纳入到标准库中

时间日期库——chrono

模板的>>中间不需要加空格了



![image-20200527163804499](Cpp summary.assets/image-20200527163804499.png)



xcode + cpp11

 Build Settings  -> C++ Language Dialect ->select c++11

-std=c++11

clang -std=c++98 -pedantic-errors



## C# interop



```
# C 分配的内存只能由自已释放，C# 不可以

# C#
IntPtr pout = Simhash256.simhash256();

            var hs = Marshal.PtrToStringUTF8(pout);
            Marshal.FreeHGlobal(pout);
            
        class Simhash256
        {

            [DllImport("simhash256.dll")]
            public static extern IntPtr simhash256();
        }
 
 # C
 
 #include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

__declspec(dllexport) void* simhash256() { // uint8_t* input, size_t number_of_bytes
    //uint64_t hash_1, hash_2, hash_3, hash_4;
    //simple_simhash(input, number_of_bytes, &hash_1, &hash_2, &hash_3, &hash_4);
    char* out = (char*)malloc(128);
    sprintf_s(out, 128, "%s", "hello, wrold!\n");
    //free(out);
    //sprintf_s(out, 128, "%16.16" PRIx64 "-%16.16" PRIx64 "-%16.16" PRIx64 "-%16.16"
    //    PRIx64 "\n", hash_1, hash_2, hash_3, hash_4);
    return (void*)out;
}

int main() {

    simhash256();
    //free(pout);
}
        
        
```







# Dictionary



```c++
map<string, vector<string> > sentence_token_map;  // key: sentence  value: words 
sentence_token_map.begin()->first
```





# List



```cpp
    // mapStudent.insert(pair<int, string>(1, "student_one"));
    // vector添加数据的缺省方法是push_back()  

    map<string, vector<string> > senten_words;
    vector<string> words;
    //senten_words.insert(make_pair(sent_vec[i], bigram_vec));
```





pair 是有first, second两个成员变量的结构体  



std::pair<std::string, double>("This is a StringTest0.", 9.7);

std::make_pair("This is a StringTest.", 9.9);  







[textrank c++](https://github.com/lostfish/textrank)



```cpp
    map<string, vector<string> > senten_words;
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    
    vector<pair<string, double> > great_sents;
    SentenceRank rank(3, 100, 0.85, 0.0001);
    
    rank.ExtractKeySentence(senten_words, great_sents, 2);
```



