



QtCore.framework  拖进xcode 工程

​	/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/lib/QtCore.framework



Search Paths

​	Framework Search Paths

​		/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/lib

​	Header Search Paths

​		/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/lib/QtCore.framework/Headers /usr/local/include

​	Library Search Paths

​		/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/lib /System/Library/Frameworks/ /usr/local/lib



Linking -> other Linker Flags

```
-stdlib=libc++ -headerpad_max_install_names -Wl,-rpath,@executable_path/../Frameworks -Wl,-rpath,/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/lib -F/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/lib
```





## 传参

Product->Scheme->Edit Scheme，弹出一个对话框如下，在Run->Arguments



## xcode 编译QT 项目

[关于dyld: Library not loaded那点事儿](https://www.jianshu.com/p/5bf7795db50d)



1. 先用QT Creator 建一个空项目
2. 添加main.cpp 等源文件并保证通过编译，正常运行
3. qmake 生成makefile
4. qmake 生成xcode 工程

```
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -o makefile eblib2.pro
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -spec macx-clang
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake && make -j4
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -spec macx-xcode
```







[macOS - Compile QT5 Project in Xcode 7+(2019)](https://gist.github.com/xul76/1a13f9743b4a5ce4c2246b8bdc6f2029)

https://gist.github.com/xul76/1a13f9743b4a5ce4c2246b8bdc6f2029



```
/ * 
     *  macOS - Compile QT5 Project in Xcode [7+] (2019)
   / *
   
   
   This method of building (compiling) a QT 5.x project in Xcode [7+] on macOS requires:
   
   
      o QT 5.x (recommended: 5.9.7)
      o Xcode 7.2+ (other versions might work as well)
   
   
   The result of this is that you will create a .xcodeproj file in the same folder as your <project>.pro file. This file
   allows you to edit- and build QT C++ projects in Xcode.
   
   
   Note: Replace "<username>" in the following commands with your macOS username.
         If you have installed QT in a different folder: replace paths accordingly.
   
   
   1. Open a Terminal
   
   2. # cd <qt project folder>
   
   3. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake -o makefile <project>.pro
   
   4. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake -spec macx-clang
   
   5. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake && make -j4
        ... ! DO NOT CLEAN AFTER BUILDING !
   
   6. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake -spec macx-xcode
   
   7. Open .xcodeproj file in Xcode
   
   8. You will see a warning asking you if you want to update this project file with new values.
      Press "Update"
      
   9. Click on your Project (top of File Explorer in Xcode)
   
  10. Click on "Build Settings"
  
  11. Under "Build Locations", correct paths that have double slashes
   
  12. ???
  
  13. PROFIT
  
  +xuL
```







```cpp

/*
 
 ## xcode 编译QT 项目

 1. 先用QT Creator 建一个空项目
 2. 添加main.cpp 等源文件并保证通过编译，正常运行
 3. qmake 生成makefile

 ```
 /Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -o makefile eblib2.pro
 /Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -spec macx-clang
 /Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake && make -j4
 /Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -spec macx-xcode
 ```

 /usr/local/include
 
 
 libeb 从这里下载自行编译，并安装到/usr/local
    https://github.com/mistydemeo/eb/
 
 Header Search Paths
    /usr/local/include
 Library Search Path
    /usr/local/lib

 Build Phase -> Link Binary With Librarie
    libeb.16.dylib
    # 从/usr/local/lib 拖这个文件到界面上
 
 
 编译选项Realse 再加上：
    Apple Clang - Custom Compiler Flags
        Other C Flags
            -DQT_NO_DEBUG
        other C++ Flags
            -DQT_NO_DEBUG
 
 
 另一个项目在这：
    Documents/github/doc/lang/programming/xcode/ebinfo

 "Ａ級"
 
 日文编码查询
    https://www.asahi-net.or.jp/~ax2s-kmtn/ref/jisx0208.html
 
 QTextCodec
 
 
 关于dyld: Library not loaded那点事儿
    https://www.jianshu.com/p/5bf7795db50d
 
 */

#include <stdio.h>

#define ASSERT(value) if (!(value)) {   __asm__ __volatile__("hlt"); /*_asm {int 3};*/}

#include <eb/eb.h>
#include <eb/binary.h>
#include <eb/text.h>
#include <eb/font.h>
#include <eb/appendix.h>
#include <eb/error.h>

#include <QTextCodec>

#define NHK "/Users/vvw/Documents/dic/NHK/exported/"

void dataWrite(char *fname, char *dat, int siz) {
    FILE *pf;
    if ( (pf = fopen(fname,"wb")) != 0) {
        fwrite(dat,siz,1,pf);
    } else {
        ASSERT(0);
    }
    fclose(pf);
}


EB_Error_Code iHOOK_WIDE_JISX0208(EB_Book *book, EB_Appendix *appendix,
    void *classp, EB_Hook_Code code, int argc, const unsigned int* argv)
{
    QTextCodec * codec_ISO, * codec_GB, * codec_Euc;
    
    codec_ISO = QTextCodec::codecForName( "ISO8859-1" );
    codec_GB = QTextCodec::codecForName( "GB2312" );
    codec_Euc = QTextCodec::codecForName("EUC-JP");
    
    const char codes[] = { char(argv[0] >> 8), char(argv[0] & 0xff), 0 };  // 拆出高低两字节
    // \xa3 \xc1 \0  0xa3 0xc1 0x0
    //return eucCodec->toUnicode(code, std::size(code)).toUtf8();
    // A3 C1  -> A  第一次回调
    // B5 E9  -> 級 第二次回调
    
    QString title = codec_Euc->toUnicode(codes); // .toUtf8();
    
    return EB_SUCCESS;
}

EB_Error_Code iHook_WAVE(EB_Book *book, EB_Appendix *appendix,
    void *classp, EB_Hook_Code code, int argc, const unsigned int* argv)
{
    if( code == EB_HOOK_END_WAVE ) {
        // 回调只是通知你，音频已经读完了。后面没有了
        return EB_SUCCESS;
    }
    
    EB_Position spos, epos;
    spos.page = argv[ 2 ];
    spos.offset = argv[ 3 ];
    epos.page = argv[ 4 ];
    epos.offset = argv[ 5 ];
    
    char wavpath[1024+1];
    char wavname[512+1];
    sprintf(wavname, "%dx%d.wav", spos.page, spos.offset);
    sprintf(wavpath, "%s%s", NHK, wavname);

    EB_Error_Code ecode =  eb_set_binary_wave( book, &spos, &epos );
    if (ecode != EB_SUCCESS) { ASSERT(0); }
    
    ssize_t len;
    #define BUFFSIZE 1024*1024+1
    char *buff = (char*)malloc(BUFFSIZE); // 申请1M 内存
    for(;;) {
        ecode = eb_read_binary(book, BUFFSIZE, buff, &len);
        if (ecode != EB_SUCCESS) { free(buff); ASSERT(0); }
        if (len <= 0) { ASSERT(0); }
        if (len < BUFFSIZE) {
            break;  // 一次读完了
        } else {
            ASSERT(0);  // 图片和音频按理说不应该大于1M，https://github.com/vvw/x32/blob/master/std.c ，
            // 增加buff 的内存，继续读剩余内容？
            // QT github qolibri 是这么做的：QByteArray b;  b += QByteArray(buff, (int)len);
        }
    }
    
    dataWrite(wavpath, buff, (int)len);
    free(buff);
        
    return EB_SUCCESS;
}

// 成功回调图片
EB_Error_Code iHookBEGIN_IN_COLOR_JPEG(EB_Book *book, EB_Appendix *appendix,
    void *classp, EB_Hook_Code code, int argc, const unsigned int* argv)
{

    EB_Position pos;
    pos.page = argv[2];
    pos.offset = argv[3];
    
    char imgpath[1024+1];
    char imgname[512+1];
    sprintf(imgname, "%dx%d.jpg", pos.page, pos.offset);
    sprintf(imgpath, "%s%s", NHK, imgname);
    
    EB_Error_Code ecode = eb_set_binary_color_graphic(book, &pos);
    if (ecode != EB_SUCCESS) { ASSERT(0); }
    
    ssize_t len;
    #define BUFFSIZE 1024*1024+1
    char *buff = (char*)malloc(BUFFSIZE); // 申请1M 内存
    for(;;) {
        ecode = eb_read_binary(book, BUFFSIZE, buff, &len);
        if (ecode != EB_SUCCESS) { ASSERT(0); }
        if (len <= 0) { free(buff); ASSERT(0); }
        if (len < BUFFSIZE) {
            break;  // 一次读完了
        } else {
            ASSERT(0);  // 图片和音频按理说不应该大于1M，https://github.com/vvw/x32/blob/master/std.c ，
            // 增加buff 的内存，继续读剩余内容？
            // QT github qolibri 是这么做的：QByteArray b;  b += QByteArray(buff, (int)len);
        }
    }
    
    dataWrite(imgpath, buff, (int)len);
    free(buff);
    
    return EB_SUCCESS;

}

EB_Hook ihooks[] = {
  { EB_HOOK_WIDE_JISX0208, iHOOK_WIDE_JISX0208},
  { EB_HOOK_BEGIN_IN_COLOR_JPEG, iHookBEGIN_IN_COLOR_JPEG },
  { EB_HOOK_BEGIN_WAVE, iHook_WAVE },
  { EB_HOOK_END_WAVE, iHook_WAVE },
  { EB_HOOK_NULL, NULL }
};

int main(int argc, const char * argv[]) {
    
    EB_Book book;
    EB_Appendix appendix;
    EB_Hookset hookset;
    //EB_BookList bookList;
    
    
    eb_initialize_library();
    eb_initialize_book(&book);
    eb_initialize_appendix(&appendix);
    eb_initialize_hookset(&hookset);

    EB_Error_Code ecode;
    //extern EB_Hook ihooks[];
    ecode = eb_set_hooks(&hookset, ihooks);
    ecode = eb_bind( &book,"/Users/vvw/Documents/dic/NHK" );
        
    EB_Subbook_Code codes[EB_MAX_SUBBOOKS];
    int cnt;

    ecode = eb_subbook_list(&book, codes, &cnt);
    ecode = eb_set_subbook(&book, codes[0]);

    EB_Position pos;
    //ecode = eb_text(&book, &pos);  // first word position
    
    // "Ａ級" 的position
    pos.page = 11721;
    pos.offset = 1490;
    ecode = eb_seek_text(&book, &pos);

    char buff[1024+1];
    ssize_t len;

    ecode = eb_read_text(&book, &appendix, &hookset, NULL,  // 可以传void** 进去，发生回调的时侯别人会原样回传给你
                1024, buff, &len);
    
    eb_finalize_book( &book );
    eb_finalize_appendix(&appendix);
    
    printf("Hello, World!\n");
    return 0;
}


```



