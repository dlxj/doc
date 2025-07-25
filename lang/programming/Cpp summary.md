

# visual studio 2022 复制到 bin

```

see huggingface\iWeChatOcr\src\WeChatOcrCpp\WeChatOcrCpp.vcxproj
	
	see huggingface\ColorTextEditorV2\build\src\imrad.vcxproj

<ItemGroup>
  <None Include="..\..\data\**\*.*">
    <Link>data\%(RecursiveDir)%(Filename)%(Extension)</Link>
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup>
	# 复制整个目录 保持目录结构 用这个！！！


  <ItemGroup>
    <Content Include="..\..\style\**">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
      <PackageCopyToOutput>true</PackageCopyToOutput>
      <Link>style\%(RecursiveDir)%(Filename)%(Extension)</Link>
    </Content>
  </ItemGroup>
    	# 保持目录结构要这样
    		# 复制整个文件夹

  <ItemGroup>
    <Content Include="wco_data\**">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
      <PackageCopyToOutput>true</PackageCopyToOutput>
    </Content>
  </ItemGroup>
  		# 复制整个文件夹

<ItemGroup>
  <Content Include="..\..\3rdparty\opencv\lib\*.dll">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    <Link>%(Filename)%(Extension)</Link>
  </Content>
</ItemGroup>
	# 只复制里面的 dll


```



# CMake 配置

```

CMake-gui

choco install pkgconfiglite
	# 依赖这个
		# C:\ProgramData\chocolatey\lib\pkgconfiglite\tools\pkg-config-lite-0.28-1\bin


```





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



#### 成功提取中文

```
#include <iostream>
#include <vector>
#include <regex>

int main() {
    std::wstring str = L"aa中bb文";
    std::wregex pattern(L"[\\u4E00-\\u9FAF]+");
    std::wsregex_iterator it(str.begin(), str.end(), pattern);
    std::wsregex_iterator end;

    std::vector<std::pair<std::wstring, std::size_t>> chinese_substrings;
    while (it != end) {
        std::wstring substr = it->str();
        std::size_t pos = it->position();
        chinese_substrings.push_back(std::make_pair(substr, pos));
        ++it;
    }

    for (const auto& pair : chinese_substrings) {
        std::wcout << "中文子串: " << pair.first << ", 位置: " << pair.second << std::endl;
    }

    return 0;
}

```



```
#include <iostream>
#include <vector>
#include <regex>

int main() {
    std::wstring str = L"aa中bb文";
    std::wregex pattern(L"[\\u4E00-\\u9FAF]+");
    std::wsregex_iterator it(str.begin(), str.end(), pattern);
    std::wsregex_iterator end;

    std::vector<std::wstring> chinese_substrings;
    while (it != end) {
        chinese_substrings.push_back(it->str());
        ++it;
    }

    for (const auto& substr : chinese_substrings) {
        std::wcout << substr << std::endl;
    }

    return 0;
}

```



# vscdoe + MSVC

[VS Code for Microsoft C++](https://code.visualstudio.com/docs/cpp/config-msvc)

```
解决 vscode 调试窗口 utf8 显示乱码
win键 -> 设置 -> 时间和语言 -> 最右边"日期、时间和区域格式设置" 
  ->其他日期、时间和区域设置 ->区域 更改日期、时间或数字格式
  -> 管理 ->更改系统区域设置 ->Beta版:使用Unicode UTF-8提供全球语言支持


打开 Developer Command Prompt for VS 2019 命令行
在这个命令行运行 code ，会打开 vscode
打开目录 -> 打开文件t.cpp -> ctrl + shift + P -> 输入C++ 
  -> 选 C/C++:Debug C/C++File
  	# 会自动生成 task.json

{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: cl.exe build active file",
            "command": "cl.exe",
            "args": [
                "/Zi",
                "/EHsc",
                "/nologo",
                "/Fe${fileDirname}\\${fileBasenameNoExtension}.exe",
                "${file}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$msCompile"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by Debugger."
        }
    ],
    "version": "2.0.0"
}




```





[vscode使用visual studio编译工具MSVC构建C++工程](https://blog.csdn.net/qq_37429313/article/details/120588483)

```
ctrl + shift + x -> 输入 easy c
	# 安装 Easy C++ projects 插件

ctrl + shit + p -> 输入 c json
	# 会生成 c_cpp_properties.json

ctrl + shit + p -> 输入 easy -> 选新建工程
	# 选 x64 visual studio 2019
	# 会自动生成 .vscode 下的各种配置

```



```
# 自动生成的 build.bat 修改成这样
@echo off
if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" (
    call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64
) else (
    if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" (
        call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
    ) else (
        call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64
    )
)
set compilerflags=/Od /Zi /EHsc /std:c++latest /I include /I C:\src\vcpkg\packages\fplus_x64-windows\include
set linkerflags=/OUT:bin\main.exe
cl.exe %compilerflags% src\*.cpp /link %linkerflags%
del bin\*.ilk *.obj *.pdb
```



```
# 自动生成的(不是) main.cpp 修改成这样
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



```
# 对比 MSYS32 MINGW64 或许可以改进一下
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe build active file",
            "command": "C:\\msys64\\ucrt64\\bin\\g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe",
                "-IC:\\Program Files (x86)\\FunctionalPlus\\include"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by Debugger."
        }
    ],
    "version": "2.0.0"
}
```



## conan

```

conan profile detect

C:\Users\i\conanfile.txt
[requires]
protobuf/3.21.12

[generators]
CMakeDeps
CMakeToolchain

[layout]
cmake_layout

conan install . --build=missing

C:\Users\i\build\generators
	# 生成的一些文件在这

C:\Users\i\.conan2\p\proto47a676cb9257b\d\conan_package.tgz
	# 它下载的 protobuf 二进制包在这里

```





## vcpkg

```
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg; .\bootstrap-vcpkg.bat
	# 安装 vcpkg
	

cd D:\usr\vcpkg

 git log --color=always --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ad)' --date=short | grep --color=never protobuf
	# 找特定版本的 protobuf

git checkout 5294d36841
	# 回退到指定版本

./vcpkg install protobuf
	# error: try_read_contents("D:\usr\vcpkg\scripts\vcpkg-tools.json"): no such file or directory
		# 不知道为什么出错

```



```
vcpkg install boost-regex[icu]:x64-windows
    # C:/src/vcpkg/packages/boost-regex_x64-windows
    # C:\src\vcpkg\packages\icu_x64-windows\include
    # C:\src\vcpkg\installed\x64-windows\bin
        # dll 在这，复制到 exe 同目录下成功运行，否则会出错
    # 成功安装
vcpkg install nlohmann-json
// see nodejs sumarry.md -> C++ Monads
// vcpkg.exe search boost
// vcpkg.exe install boost-regex
```



# vscode genie

[chatgpt-vscode](https://github.com/ai-genie/chatgpt-vscode)

[CopilotForXcode](https://github.com/intitni/CopilotForXcode)



# 改 main 参数

```

see huggingface\wechat-ocr\src\main.cpp

int main(int argc, char* argv[])
{
	const char* newArgs[] = {
		argv[0], 
		"E:/huggingface/wechat-ocr/wechat4/extracted/wxocr.dll", // "C:/Users/i/AppData/Roaming/Tencent/xwechat/XPlugin/Plugins/WeChatOcr/8033/extracted/wxocr.dll", 
		"E:/huggingface/wechat-ocr/wechat4//Weixin/4.0.5.26",                       // "C:/Program Files/Tencent/Weixin/4.0.5.26", 
		"E:/huggingface/wechat-ocr/t.jpg"
	}; 

	argc = 4;
	argv = (char**)newArgs;
```





# string

[utfcpp](https://github.com/nemtrif/utfcpp)



C++11 标准中增加了一些表示字符串常量的标识，如下有：

L"您好！"： wstring 字符串常量，使用文件保存编码方式字符集
R"(您 好 \n)": 原始字符串常量（字节数组），保留所有的字符
u8"您好！"： string 字符串常量（字节数组），使用 UTF8 进行编码保存



- UTF16编码中，英文字符占两个字节；绝大多数汉字（尤其是常用汉字）占用两个字节，个别汉字（在后期加入unicode编码的汉字，一般是极少用到的生僻字）占用四个字节。

- UTF8编码中，英文字符占用一个字节；绝大多数汉字占用三个字节，个别汉字占用四个字节。



```
json j = json::parse(u8"JSON string with Chinese characters");
// or
json j = json::parse(u8 R"(JSON string with Chinese characters)");
```





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



## wsring 转 utf8 string 

```
#include <codecvt>
std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
std::string first_ = converter.to_bytes(first);
```



## 八进制转义字节序列

```
#include <iostream>
#include <string>
#include <filesystem>

int main() {
    std::string s = "\347\254\254\344\270\200\345\215\225\345\205\203";
    std::u8string u8s = std::filesystem::path(s).u8string();
    
    // 在C++20中，可以直接使用u8字符串字面量
    // std::u8string u8s = u8"第一单元";
    
    // 输出UTF-8字符串
    for (char8_t c : u8s) {
        std::cout << static_cast<unsigned char>(c);
    }
    std::cout << std::endl;
    
    return 0;
}
```





# vector

```
std::vector<std::pair<std::string, std::string>> styleNames; //name, path

    styleNames = {
        { "Classic", "" },
        { "Light", "" },
        { "Dark", "" }
    };
    
    
    styleNames.push_back({ u8string(it->path().stem()), u8string(it->path()) });

```



## 转指针

```

see huggingface\ColorTextEditorV2\src\ImGuiColorTextEdit\TextEditor.cpp

std::vector<uchar> buf;
std::vector<int> params;
params.push_back(cv::IMWRITE_JPEG_QUALITY);
params.push_back(90); // JPEG质量设为90%

bool success = cv::imencode(".jpg", cut, buf, params);

const unsigned char* imagedata = reinterpret_cast<const unsigned char*>(buf.data());

```





# dict

```
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> my_dict = {{"apple", 1}, {"banana", 2}, {"orange", 3}};

    // 输出字典中的元素
    for (const auto &pair : my_dict) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}

```



```
#include <iostream>
#include <map>
#include <string>
#include <tuple>

int main() {
    std::map<std::string, std::tuple<int, std::string>> dict;

    // Adding values to the dictionary
    dict["key1"] = std::make_tuple(42, "value1");
    dict["key2"] = std::make_tuple(99, "value2");

    // Accessing values from the dictionary
    std::tuple<int, std::string> value1 = dict["key1"];
    std::cout << "Value for key1: " << std::get<0>(value1) << ", " << std::get<1>(value1) << std::endl;

    std::tuple<int, std::string> value2 = dict["key2"];
    std::cout << "Value for key2: " << std::get<0>(value2) << ", " << std::get<1>(value2) << std::endl;

    return 0;
}

```



```
#include <iostream>
#include <map>

int main() {
    std::map<int, std::string> myMap = {{1, "one"}, {2, "two"}, {3, "three"}};

    // 使用count()函数
    if (myMap.count(2) > 0) {
        std::cout << "Key exists!" << std::endl;
    } else {
        std::cout << "Key does not exist!" << std::endl;
    }

    // 使用find()函数
    auto it = myMap.find(4);
    if (it != myMap.end()) {
        std::cout << "Key exists!" << std::endl;
    } else {
        std::cout << "Key does not exist!" << std::endl;
    }

    return 0;
}

```



# pair

```

拆包 see huggingface\ColorTextEditorV2\src\main.cpp

std::pair<std::filesystem::path, std::filesystem::path>

auto [pth_img, pth_json] = get_img_json_pth(m5);

```





# tuple

```
std::vector<std::tuple<std::wstring, std::wstring, std::wstring>> three_part;

                                three_part.push_back(std::tuple<std::wstring, std::wstring, std::wstring>(first, second, third));


    std::vector<std::tuple<std::wstring, std::wstring, std::wstring>> three_part2 = _::filter<std::vector<std::tuple<std::wstring, std::wstring, std::wstring>>>(three_part, [&](const std::tuple<std::wstring, std::wstring, std::wstring>& value) {
        std::wstring first = std::get<0>(value);
        std::wstring second = std::get<1>(value);
        std::wstring third = std::get<2>(value);

        if (first != L"") {
            int a = 1;
        }

        return true;
    });
```





# Lambda

- `[&]`是一个捕获列表（capture list），表示以引用方式捕获所有外层作用域中的变量。





# file

##　read write

```
#include <iostream>
#include <fstream>

inline void write(std::string str)
{
    std::ofstream file;
    file.open("example.txt");

    if (file.is_open())
    {
        file << str;
        file.close();
    }
    else
    {
        std::cerr << "无法打开文件" << std::endl;
    }
}
```





## 遍历目录

```
/std:c++17 需要这个参数 传给 cl.exe
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: cl.exe build active file",
            "command": "cl.exe",
            "args": [
                "/Zi",
                "/EHsc",
                "/nologo",
                "/std:c++17",
                "/I",
                "C:\\src\\vcpkg\\packages\\nlohmann-json_x86-windows\\include",
                "/Fe${fileDirname}\\${fileBasenameNoExtension}.exe",
                "${file}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$msCompile"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by Debugger."
        }
    ],
    "version": "2.0.0"
}
```



# path

```


std::filesystem::path getExecutablePath() {
    char path[MAX_PATH];
    GetModuleFileNameA(NULL, path, MAX_PATH);
    return std::filesystem::path(path).parent_path();
}

std::filesystem::path currPath = getExecutablePath(); // std::filesystem::current_path();
	# 得到可执行文件目录
const std::string Constant::WeChatOcrData = ( currPath / std::filesystem::path("wco_data") ).lexically_normal().u8string(); // ".\\wco_data";





see huggingface\ColorTextEditorV2\src\main.cpp

        std::filesystem::path exePath = std::filesystem::current_path(); // 注意：这是工作目录

        auto pth_img = exePath.parent_path().parent_path() / std::filesystem::path("data/img") / std::format("{}.txt", m5); // 提取目录部分
        pth_img = pth_img.lexically_normal();
        



see huggingface\imrad\src\imrad.cpp

fs::path u8path(std::string_view s)
{
#if __cplusplus >= 202002L
    return fs::path((const char8_t*)s.data(), (const char8_t*)s.data() + s.size());
#else
    return fs::u8path(s);
#endif
}

std::string u8string(const fs::path& p)
{
#if __cplusplus >= 202002L
    return std::string((const char*)p.u8string().data());
#else
    return p.u8string();
#endif
}

std::string generic_u8string(const fs::path& p)
{
#if __cplusplus >= 202002L
    return std::string((const char*)p.generic_u8string().data());
#else
    return p.generic_u8string();
#endif
}
```





# JSON

[json](https://github.com/nlohmann/json)

[Chinese character ](https://github.com/nlohmann/json/issues/2325)

```
vcpkg install nlohmann-json
```



```

see huggingface\ColorTextEditorV2\src\main.cpp

#include "nlohmann_json/json.hpp"
using json = nlohmann::json;

		std::ifstream f(pth_json);
        if (!f.is_open()) {
            return 1;
        }
        json jsn = json::parse(f);
        
        
```





## string 比较的坑



```
std::wstring type = se["type"];
        type.pop_back(); // 它存了一个 \0 在最后，删掉最后一个字符才能比较
        std::wstring tmp = L"jp";
        if (type == tmp)
        { // need seg
            int a = 1;
        }
```



# csv

[rapidcsv](https://github.com/d99kris/rapidcsv)

```
# 没有 heard 的 csv 这样读

#include <iostream>
#include <vector>
#include "rapidcsv.h"

rapidcsv::Document doc("Book1.csv", rapidcsv::LabelParams(-1, -1)); // No Headers
            std::vector<std::string> close = doc.GetColumn<std::string>(0);
            # 取第 0 列
```







# windows



## utf-8

```

see huggingface\wechat-ocr\src\main.cpp

	SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
    setlocale(LC_ALL, "en_US.UTF-8");
```





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

   """

cpp origin


# include <iostream>
# include <opencv2/opencv.hpp>

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

 //剪裁图片
  Mat roiImage = srcImage(Rect(0, 0, srcImage.cols - 70, srcImage.rows - 30));
  imshow("0:抠图操作", roiImage);

    //对图像进行二值化
  threshold(roiImage, binaryImage, 92, 255, THRESH_BINARY_INV );
  imshow("1:二值操作", binaryImage);


  Mat morhpImage;
  Mat kernel = getStructuringElement(MORPH_RECT, Size(20, 2), Point(-1, -1));//自定义一个核
  morphologyEx(binaryImage, morhpImage, MORPH_OPEN, kernel, Point(-1, -1));//开操作
  imshow("2:开操作", morhpImage);


  Mat dilateImage;
  kernel = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));
  dilate(morhpImage, dilateImage, kernel);
  imshow("3:膨胀操作", dilateImage);

  
  vector<Vec4i> lines;
  HoughLinesP(dilateImage, lines, 1, CV_PI / 180.0, 30, 20.0, 0);
  dstImage = srcImage.clone();
  cvtColor(dstImage, dstImage, COLOR_GRAY2BGR);
  for (size_t t = 0; t < lines.size(); t++) {
    Vec4i ln = lines[t];
    line(dstImage, Point(ln[0], ln[1]), Point(ln[2], ln[3]), Scalar(0, 0, 255), 2, 8, 0);
  }
  imshow("4:绘制直线", dstImage);

    """



"""
https://mp.weixin.qq.com/s?__biz=MzA4ODgyMDg0MQ==&mid=100001057&idx=1&sn=ebfd3cf30ffb3a48909bd309fa59f82d&chksm=1025182727529131c5c63d02663bfc517b89c23f4884c4d49334fee27d12947b792e9b36643f#rd
面对直线，你说霍夫线变换是万能的吗

https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/?ref=gcse

doc\lang\programming\opencv summary.md

"""

import numpy as np
import cv2

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':

    imgData = np.fromfile('./填空题.png', dtype=np.uint8)
    img_origin = cv2.imdecode(imgData, -1)
    img_rgb = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGRA2RGB)

    # 转灰度图
    img_gray = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGR2GRAY)   #cv2.COLOR_RGB2BGR
    print(type(img_gray))

    w = img_gray.shape[0]  # w,h 反了这里，可能是将错就错后面才看起来对
    h = img_gray.shape[1]

    # slice 子矩阵，既剪裁图像
    img_crop = img_gray[0:w-30, 0:h-70]

    # 二值化
    ret, img_binary = cv2.threshold(img_crop, 92, 255, cv2.THRESH_BINARY_INV)
    # imshow("1:二值操作", binaryImage)

    # 开操作(将文字这些密集的“孔洞”给腐蚀掉，仅留下直线)
    rect_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (20, 2))  # 定义了20*2 大小的矩形核
    img_opening = cv2.morphologyEx(img_binary, cv2.MORPH_OPEN, rect_kernel)

    # 膨胀加粗
    rect_kernel2 = cv2.getStructuringElement(
        cv2.MORPH_RECT, (3, 3))  # 定义了20*2 大小的矩形核
    img_dilate = cv2.dilate(img_opening, rect_kernel2)

    #edges = cv2.Canny(img_dilate,50,150,apertureSize=3)


    # Apply HoughLinesP method to
    # to directly obtain line end points
    lines = cv2.HoughLinesP(
        img_dilate,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi/180,  # Angle resolution in radians
        threshold=30,  # Min number of votes for valid line
        minLineLength=20,  # Min allowed length of line
        maxLineGap=0  # Max allowed gap between line for joining them
        )

    #img_color = cv2.cvtColor(img_origin, cv2.COLOR_BGR2RGB)


    for points in lines:
      # Extracted points nested in the list
      x1,y1,x2,y2=points[0]
      # Draw the lines joing the points
      # On the original image
      #cv2.line(img_origin, (x1,y1),(x2,y2),(0,0,255, 255), 2)  # 原图是四通道的BGRA(蓝绿红 + alpha 透明度)
      cv2.line(img_rgb, (x1,y1),(x2,y2),(0,0,255), 2)  # 看来无论原图怎么样，cv2 的三个通道顺序永远都是: BGR
      

    cv2.imshow("origin", img_origin)
    cv2.imshow("croped", img_crop)
    cv2.imshow("binary", img_binary)
    cv2.imshow("opening", img_opening)
    cv2.imshow("dilate", img_dilate)  
    cv2.imshow("result", img_rgb)

    cv2.waitKey(0)



 






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



## 解码图片

```

see huggingface\ColorTextEditorV2\src\main.cpp

see huggingface\ColorTextEditorV2\src\ImGuiColorTextEdit\TextEditor.cpp
	# void TextEditor::HandleMouseInputs()

std::pair<std::filesystem::path, std::filesystem::path> get_img_json_pth(const std::string& m5) {
#ifdef _DEBUG
    // 这是工作目录
    auto pth_img = g_currPath.parent_path().parent_path() / std::filesystem::path("data/img") / std::format("{}.txt", m5);
    auto pth_json = g_currPath.parent_path().parent_path() / std::filesystem::path("data/json") / std::format("{}.json", m5);
#else
    // 这是可执行文件所在目录
    auto pth_img = g_currPath / std::filesystem::path("data/img") / std::format("{}.txt", m5);
    auto pth_json = g_currPath / std::filesystem::path("data/json") / std::format("{}.json", m5);
#endif // DEBUG

    pth_img = pth_img.lexically_normal();
    pth_json = pth_json.lexically_normal();

    std::pair<std::filesystem::path, std::filesystem::path> pth_pair{ pth_img, pth_json };

	return pth_pair;
}


std::vector<unsigned char> base64_decode(const std::string& input) {
    
    const std::string BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    std::vector<int> decode_table(256, -1);
    for (int i = 0; i < 64; i++)
        decode_table[BASE64_CHARS[i]] = i; // 构建解码表[6,8](@ref)

    std::vector<unsigned char> decoded;
    int val = 0, bits = -8; // val:24位缓冲区, bits:当前有效位数
    for (unsigned char c : input) {
        if (c == '=') break;               // 遇填充符终止
        if (decode_table[c] == -1) continue; // 跳过非法字符

        val = (val << 6) + decode_table[c]; // 合并6位数据[6](@ref)
        bits += 6;
        if (bits >= 0) {                   // 每凑够8位输出1字节
            decoded.push_back((val >> bits) & 0xFF);
            bits -= 8;
        }
    }
    return decoded;
}

std::string readFileToString(const std::string& filePath) {
    std::ifstream file(filePath, std::ios::binary);
    if (!file) return "";
    std::ostringstream buffer;
    buffer << file.rdbuf(); // 将文件流缓冲区内容写入字符串流
    return buffer.str();
}


const char* m5 = gh.mImageMD5;
if (m5 && *m5) {
				auto [pth_img, pth_json] = get_img_json_pth(std::string(m5));

				auto b64_str = readFileToString(pth_img.string());
				auto b64_buf = base64_decode(b64_str);

				auto img_orgin = cv::imdecode(b64_buf, -1);
				
				cv::cvtColor(img_orgin, img_orgin, cv::COLOR_GRAY2BGR);

				cv::rectangle(img_orgin, cv::Point(gh.x, gh.y), cv::Point(gh.x + gh.w, gh.y + gh.h), cv::Scalar(0, 0, 255), 2);

				//cv::Mat srcImage, dstImage, binaryImage;
				//auto pth = std::string("E:\\huggingface\\ColorTextEditorV2\\data\\0003.jpg");
				//srcImage = cv::imread(pth, 0);
				//cv::InputArray src(srcImage);
				//auto tag = std::string("原图");
				//const std::string window_name = "OpenCV Based Annotation Tool";
				cv::imshow("原图", img_orgin);

				cv::waitKey(0);
}

```



## DX11 纹理

```

see huggingface\ColorTextEditor\main.cpp

// 函数：从 cv::Mat 创建 DX11 纹理
HRESULT LoadTextureFromMemoryDX11(
    ID3D11Device* device,
    const cv::Mat& image,
    ID3D11ShaderResourceView** outSRV
) {
    // 1. 检查输入有效性
    if (image.empty() || !device || !outSRV)
        return E_INVALIDARG;

    // 2. 转换图像格式为 DXGI 兼容格式（关键！）
    cv::Mat convertedImage;
    switch (image.channels()) {
    case 1: // 单通道灰度图 → 扩展为 RGBA
        cv::cvtColor(image, convertedImage, cv::COLOR_GRAY2RGBA);
        break;
    case 3: // 三通道BGR → 转换为 RGBA
        cv::cvtColor(image, convertedImage, cv::COLOR_BGR2RGBA);
        break;
    case 4: // 四通道直接使用（需确认OpenCV为BGRA）
        convertedImage = image.clone();
        break;
    default:
        return E_FAIL;
    }

    // 3. 配置纹理描述符
    D3D11_TEXTURE2D_DESC desc;
    ZeroMemory(&desc, sizeof(desc));
    desc.Width = convertedImage.cols;
    desc.Height = convertedImage.rows;
    desc.MipLevels = 1;
    desc.ArraySize = 1;
    desc.Format = DXGI_FORMAT_R8G8B8A8_UNORM; // RGBA 8位/通道
    desc.SampleDesc.Count = 1;
    desc.Usage = D3D11_USAGE_DEFAULT;
    desc.BindFlags = D3D11_BIND_SHADER_RESOURCE;
    desc.CPUAccessFlags = 0;

    // 4. 填充纹理初始化数据
    D3D11_SUBRESOURCE_DATA initData;
    ZeroMemory(&initData, sizeof(initData));
    initData.pSysMem = convertedImage.data;
    initData.SysMemPitch = convertedImage.cols * 4; // 每行字节数 = 宽×4通道
    initData.SysMemSlicePitch = 0;

    // 5. 创建纹理资源
    ID3D11Texture2D* texture = nullptr;
    HRESULT hr = device->CreateTexture2D(&desc, &initData, &texture);
    if (FAILED(hr)) return hr;

    // 6. 创建着色器资源视图（SRV）
    D3D11_SHADER_RESOURCE_VIEW_DESC srvDesc;
    ZeroMemory(&srvDesc, sizeof(srvDesc));
    srvDesc.Format = desc.Format;
    srvDesc.ViewDimension = D3D11_SRV_DIMENSION_TEXTURE2D;
    srvDesc.Texture2D.MipLevels = 1;
    hr = device->CreateShaderResourceView(texture, &srvDesc, outSRV);

    // 7. 释放临时资源
    texture->Release();
    return hr;
}

    cv::Mat srcImage = cv::imread("data/er.jpeg", cv::IMREAD_COLOR_BGR);
	
    // 将OpenCV图像转换为纹理
	ID3D11ShaderResourceView* outSRV = nullptr;
    HRESULT hr = LoadTextureFromMemoryDX11(g_pd3dDevice, srcImage, &outSRV);

    ImTextureID cv_texture_id = (ImTextureID)(intptr_t)outSRV;

    int cv_width = srcImage.cols;
    int cv_height = srcImage.rows;
    
    
    

// Open and read a file, then forward to LoadTextureFromMemory()
ImTextureID LoadTextureFromFile(const char* file_name, ID3D11Device* device, int* out_width, int* out_height)
{
    FILE* f = fopen(file_name, "rb");
    if (f == NULL)
        return 0;
    fseek(f, 0, SEEK_END);
    size_t file_size = (size_t)ftell(f);
    if (file_size == -1)
        return 0;
    fseek(f, 0, SEEK_SET);
    void* file_data = IM_ALLOC(file_size);
    fread(file_data, 1, file_size, f);
    fclose(f);
    ImTextureID texture_id = LoadTextureFromMemoryDX11(file_data, file_size, device, out_width, out_height);
    IM_FREE(file_data);
    return texture_id;
}




```



## OpenGL 纹理



```

see huggingface\ColorTextEditorV2\src\ImGuiColorTextEdit\TextEditor.cpp

							if (found) {
								// 左上 右上 右下 左下
								int x = line_pos[0]["x"];
								int y = line_pos[0]["y"];

								int x_min = std::min(line_pos[0]["x"], line_pos[3]["x"]);
								int x_max = std::max(line_pos[1]["x"], line_pos[2]["x"]);

								int y_min = std::min(line_pos[0]["y"], line_pos[1]["y"]);
								int y_max = std::max(line_pos[2]["y"], line_pos[3]["y"]);

								int w = x_max - x_min;
								int h = y_max - y_min;
								
								auto b64_str = readFileToString(pth_img.string());
								auto b64_buf = base64_decode(b64_str);

								//cv::Mat srcImage = cv::imread("E:\\er.jpeg", cv::IMREAD_COLOR_BGR);
								auto srcImage = cv::imdecode(b64_buf, -1);

								switch (srcImage.channels()) {
									case 1: // 单通道灰度图 → 扩展为 RGBA
										cv::cvtColor(srcImage, srcImage, cv::COLOR_GRAY2RGBA);
										break;
									case 3: // 三通道BGR → 转换为 RGBA
										cv::cvtColor(srcImage, srcImage, cv::COLOR_BGR2RGBA);
										break;
									case 4: // 四通道直接使用（需确认OpenCV为BGRA）
										//convertedImage = srcImage.clone();
										break;
								}

								cv::rectangle(srcImage, cv::Point(gh.x, gh.y), cv::Point(gh.x + gh.w, gh.y + gh.h), cv::Scalar(255, 0, 0, 255), 2);
									// 框出选中字符

								// 剪裁图片
								cv::Mat cut = srcImage(cv::Rect(x, y, w, h)).clone(); // cv::Rect(0, 0, img_orgin.cols, 500)

								ImRad::Texture tex2;
								unsigned char* image_data2 = cut.data;
								tex2.w = cut.cols;
								tex2.h = cut.rows;

								GLuint image_texture;
								glGenTextures(1, &image_texture);
								tex2.id = (ImTextureID)(intptr_t)image_texture;
								glBindTexture(GL_TEXTURE_2D, image_texture);


								int minFilter = GL_LINEAR;
								int magFilter = GL_LINEAR;
								int wrapS = GL_CLAMP_TO_EDGE; // This is required on WebGL for non power-of-two textures
								int wrapT = GL_CLAMP_TO_EDGE; // Same

								// Setup filtering parameters for display
								glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, minFilter);
								glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, magFilter);
								glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, wrapS);
								glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, wrapT);

								// Upload pixels into texture
								glPixelStorei(GL_UNPACK_ROW_LENGTH, 0);

								glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, tex2.w, tex2.h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data2);
								//stbi_image_free(image_data2);

								mRect.size = ImVec2((float)tex2.w, (float)tex2.h);
								mRect.SetTexture(tex2.id);

								//cv::imshow("原图", cut);
								//cv::waitKey(0);

							}
```



