[TOC]

# C++ Monads

see nodejs summary.md -> C++ Monads

[FunctionalPlus](https://github.com/Dobiasd/FunctionalPlus)

- [install](https://github.com/Dobiasd/FunctionalPlus/blob/master/INSTALL.md)

- [vcpkg 包管理](https://github.com/microsoft/vcpkg/blob/master/README_zh_CN.md#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B-windows)

## [utfcpp u8string](https://github.com/nemtrif/utfcpp)

  > ```
  > // http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=中
  > 
  > /*
  > 中
  > Decimal	UTF-8	    UTF-16	UTF-32
  > 20013	    E4 B8 AD 	4E2D	00004E2D
  > 文
  > Decimal	UTF-8	    UTF-16	UTF-32
  > 25991	    E6 96 87 	6587	00006587
  > */
  > // 成功逐字符输出中文
  > // see nodejs sumarry.md -> C++ Monads
  > #include <fplus/fplus.hpp>
  > #include <iostream>
  > #include "src/utf8.h"
  > #include <string.h>
  > #include <iostream>
  > #include <string>
  > #include <fstream>
  > #include <vector>
  > using namespace std;
  > 
  > std::string str("中文");
  > for (auto it = str.begin(), it2 = str.begin(); it2 != str.end(); ) {
  > utf8::next(it2, str.end());
  > while (it < it2) {
  > cout << *it;
  > ++it;
  > }
  > cout << endl;
  > }
  > 
  > // 先转成 std::u32string 再用正则
  > std::string str2("中文");
  > std::vector<unsigned long> utf32result;
  > 	utf8::utf8to32(str2.begin(), str2.end(), std::back_inserter(utf32result));
  > 	size_t size1 = utf32result.size();
  > std::u32string strr(utf32result.begin(), utf32result.end());
  > cout << "all task done." << endl;
  > 
  > ```
  >
  > ```
  > inline std::wstring from_utf8(const std::string& utf8) {
  >  std::vector<unsigned long> utf32result;
  > 	utf8::utf8to32(utf8.begin(), utf8.end(), std::back_inserter(utf32result));
  > 	size_t size1 = utf32result.size();
  >  std::wstring wstr(utf32result.begin(), utf32result.end());
  >  return wstr;
  > }
  > 
  > inline std::string to_utf8(const std::wstring& ws) {
  >  std::string utf8;
  > 	utf8::utf16to8(ws.begin(), ws.end(), std::back_inserter(utf8));
  > 	return utf8;
  > }
  > 
  > int main()
  > {
  >  std::string test = "john.doe@神谕.com"; // utf8
  >  std::string expr = "[\\u0080-\\uDB7F]+"; // utf8
  > 
  >  std::wstring wtest = from_utf8(test);
  >  std::wstring wexpr = from_utf8(expr);
  > 
  >  std::wregex we(wexpr);
  >  std::wsmatch wm;
  >  if(std::regex_search(wtest, wm, we))
  >  {
  >      std::cout << to_utf8(wm.str(0)) << '\n';
  >  }
  > }
  > ```
  >
  > 

  




```powershell
New-Item -ItemType Directory -Path C:\src -Force
cd C:\src
git clone https://github.com/microsoft/vcpkg
.\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg.exe integrate install
.\vcpkg\vcpkg install fplus:x64-windows

--> C:/src/vcpkg/packages/fplus_x64-windows/share/fplus/copyright
fplus provides CMake targets:

    # this is heuristically generated, and may not be correct
    find_package(FunctionalPlus CONFIG REQUIRED)
    target_link_libraries(main PRIVATE FunctionalPlus::fplus)

```



```
# 源码安装
# win -> MINGW64 -> 右键 -> 管理员身份运行
git clone https://github.com/Dobiasd/FunctionalPlus
cmake -S FunctionalPlus -B FunctionalPlus/build && \
cmake --build FunctionalPlus/build && \
cmake --install FunctionalPlus/build
	# CPP Monads
	--> -- Installing: C:/Program Files (x86)/FunctionalPlus/include/fplus
	

```





```c++
#include <fplus/fplus.hpp>
#include <iostream>
using namespace std;

bool is_odd_int(int x) { return x % 2 != 0; }

int main(){
    typedef vector<int> Ints;
    Ints values = { 24, 11, 65, 44, 80, 18, 73, 90, 69, 18 };
    auto odds = fplus::keep_if(is_odd_int, values);
    std::cout << "done." << std::endl;
}
```



### regex

see nodejs summary.md C++ Monads

```

vcpkg install boost-regex[icu]:x64-windows
	# C:/src/vcpkg/packages/boost-regex_x64-windows
	# 成功安装
	#include "boost/regex.hpp"
	#include "boost/regex/icu.hpp"
	https://github.com/unicode-org/icu/releases 下载
		icu-cldr\icu4c\source\allinone
			# 有 vc 工程

// // Include the Boost regex header 
// #include <boost/regex.hpp> // Include other headers as needed 
// #include <iostream> 
// #include <string>

// int main() {

//     boost::regex reg("[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+"); 

//     //boost::regex reg("(A.*)");

//     // Create a string that contains some Japanese characters 
//     std::string s = "This is a string with 日本語 characters."; 
//     // Create a regex object with the syntax option for ICU regex 
//     // boost::regex reg("/[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+/", boost::regex::icu); 
//     // // Use regex_search to check if the string contains any Japanese characters 
//     // if (boost::regex_search(s, re)) {
//     //     std::cout << "The string contains Japanese characters.\n"; 
//     //     // Use regex_iterator to iterate over all the matches of the regex in the string 
//     //     boost::sregex_iterator it(s.begin(), s.end(), re); 
//     //     boost::sregex_iterator end; 
//     //     while (it != end) { 
//     //         // Print each match and its position in the string 
//     //         std::cout << "Match: " << it->str() << "\n"; 
//     //         std::cout << "Position: " << it->position() << "\n"; ++it; } 
//     //     } 
//     // else {
//     //     std::cout << "The string does not contain Japanese characters.\n"; 
//     // } 
//     return 0; 
// }
```





# string



## 不转义



```c++
    // https://github.com/ReneNyffenegger/cpp-base64

    const std::string orig =
        "René Nyffenegger\n"
        "http://www.renenyffenegger.ch\n"
        "passion for data\n";

    // C++ 11 only, 不转义 $"(xxx)" 括号里的内容不转义，而且括号前后都可以有其它内容
    std::ifstream t(R"(D:\workcode\csharp\dll\Examples\DllExport\BasicExport\UnmanagedCppConsole\base64.txt)");
    std::stringstream buffer;
    buffer << t.rdbuf();


    std::string str_base64 = buffer.str(); 

    std::string encoded = base64_encode(reinterpret_cast<const unsigned char*>(orig.c_str()), orig.length());
    std::string decoded = base64_decode(encoded);
```



# JSON

[json](https://github.com/nlohmann/json)



# windows



## dll



Unicode 字符集会调用失败

 **注意：常规 -> 高级 ->  使用多字节字符集**



### C++ 调用 node.dll



```

// C++ 调用 node.dll

#include <iostream>

#include "windows.h"

int main()
{
    HINSTANCE   ghDLL = NULL;
    ghDLL = LoadLibrary("D:\\GitHub\\node-14.21.1\\out\\Debug\\node.dll");

    typedef int (_cdecl* FunctionPtr) (int argc, wchar_t* wargv[]);

    FunctionPtr wmain;

    wmain = (FunctionPtr)GetProcAddress(ghDLL, "wmain");

    int argc = 2;

    wchar_t* wargv[] = {
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
      nullptr
    };

    wmain(argc, wargv);

    std::cout << "Hello World!\n";
}
```



### C# 调用 node.dll



````

// C# 调用 node.dll

using System.Runtime.InteropServices;

namespace ConsoleApp2
{
    class Program
    {
        [DllImport("user32.dll", EntryPoint = "MessageBoxA")]
        public static extern int MsgBox(int hWnd, string msg, string caption, int type);

        // 定义给 C# 的传参，全部参数都定义在这个结构数组里
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        public struct wmain_params
        {
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
            public string[] wargv;  // 大小固定为 3 个元素，最后一个元素设置为空指针，表示结束
        }
        [DllImport("D:\\GitHub\\node-14.21.1\\out\\Debug\\node.dll", EntryPoint = "wmain", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Ansi)]
        public static extern int wmain(int argc,  ref wmain_params wargv);


        static void Main(string[] args)
        {

            wmain_params pms = new wmain_params();
            pms.wargv = new string[] {
                "C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
                "C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
                null
            };

            wmain(2, ref pms);


            MsgBox(0, "C#调用DLL文件", "这是标题", 0x30);
        }
    }
}
````





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
# 成功调用，就是只支持 .net 4.5
# https://github.com/3F/DllExport
PEModule ClassLibrary1(_T("ClassLibrary1.dll")); // 定义函数 origin, 返回int ，参数int
double re = ClassLibrary1.call<int>("origin", 5);
```





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



```C#
# https://www.cnblogs.com/s5689412/p/12773177.html
static string PtrToStringUTF8(IntPtr ptr)
{
    var bytesCount = 0;
    byte b;
    do
    {
        b = Marshal.ReadByte(ptr, bytesCount);
        bytesCount++;
    }
    while (b != 0);
    var bytes = new byte[bytesCount - 1];
    Marshal.Copy(ptr, bytes, 0, bytesCount - 1);
    return Encoding.UTF8.GetString(bytes);
}


byte[] bytes = new byte[4096];
GCHandle pinned = GCHandle.Alloc(bytes, GCHandleType.Pinned);
var result = iReadXXX(pinned.AddrOfPinnedObject());
pinned.Free();
int count = bytes.ToList().FindIndex(b => b == 0);
var text = Encoding.Default.GetString(bytes, 0, count);

```



```
// Unmanaged Signature
int MessageBoxEx(
    HWND hWnd,
    LPCTSTR lpText,
    LPCTSTR lpCaption,
    UINT uType,
    WORD wLanguageId);
    
[DllImport("User32.dll", CharSet = CharSet.Unicode)]
[return: MarshalAs(UnmanagedType.I4)]
static extern Int32 MessageBoxEx
    (IntPtr hWnd,
    // Marshaling as Unicode characters
    [param: MarshalAs(UnmanagedType.LPTStr)]
    String lpText,
    // Marshaling as Unicode characters
    [param: MarshalAs(UnmanagedType.LPTStr)]
    String lpCaption,
    // Marshaling as 4-bytes (32-bit) unsigned integer
    [param: MarshalAs(UnmanagedType.U4)]
    UInt32 uType,
    // Marshaling as 2-bytes (16-bit) unsigned integer
    [param: MarshalAs(UnmanagedType.U2)]
    UInt16 wLanguageId);    
  
```



```C++

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

__declspec(dllexport) void simhash256(void* input, size_t number_of_bytes, uint64_t* hash256, void* buffer) { // uint8_t* input, size_t number_of_bytes
    uint64_t hash_1, hash_2, hash_3, hash_4;

    simple_simhash((uint8_t*)input, number_of_bytes, &hash256[0], &hash256[1], &hash256[2], &hash256[3]);
    sprintf_s((char*)buffer, 128, "%16.16" PRIx64 "-%16.16" PRIx64 "-%16.16" PRIx64 "-%16.16"
        PRIx64, hash256[0], hash256[1], hash256[2], hash256[3]);
}

int main() {

    uint8_t input[] = "0123456789";

    char buffer[128] = { 0 };
    char buf[128] = { 0 };
    uint64_t hash256[] = { 0, 0, 0, 0 };

    simhash256(input, strlen(input), hash256, buffer);

    sprintf_s((char*)buf, 128, "%16.16" PRIx64 "-%16.16" PRIx64 "-%16.16" PRIx64 "-%16.16"
        PRIx64 "\n", hash256[0], hash256[1], hash256[2], hash256[3]);

}

```





### 指针

```
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/pointer-related-operators




```





## C# call C++



```
https://github.com/xanatos/CSharpCPlusPlusInteropSamples
```





## dll 注入进程

- https://github.com/AYIDouble/Simple-DLL-Injection



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



# OpenCV

- https://mp.weixin.qq.com/s?__biz=MzA4ODgyMDg0MQ==&mid=100001057&idx=1&sn=ebfd3cf30ffb3a48909bd309fa59f82d&chksm=1025182727529131c5c63d02663bfc517b89c23f4884c4d49334fee27d12947b792e9b36643f#rd
  - 面对直线，你说霍夫线变换是万能的吗

```

#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
  Mat srcImage, dstImage, binaryImage;
  srcImage = imread("原图.png",0);  
  imshow("原图", srcImage);
  
  waitKey(0);
  return 0;
}
```



