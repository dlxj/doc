



# qolibri-subtraction  qolibri 项目精简



只留搜索框。并图片回调保持正常



## 先自行编译eblib 安装到 /usr/local/lib



## 原始CMake 的修改



加入：

find_library(EB_LIBRARY eb /usr/local/lib/ REQUIRED)

include_directories("/usr/local/include/")



然后在链接的最后加入：

${EB_LIBRARY}



target_link_libraries(qolibri Qt5::Multimedia Qt5::Network Qt5::WebEngine Qt5::WebEngineWidgets Qt5::Widgets z ${EB_LIBRARY}) # eb



## 搜索 Ａ級





## qolibri.cpp mainWin.show();   前可以hook 到图片



```cpp
    extern void starthook();
    starthook();
    mainWin.show();
```





## hook 的关键是加eb_initialize_library();  函数

```cpp
EB_Error_Code myHookBEGIN_IN_COLOR_JPEG(EB_Book *book, EB_Appendix*a,
    void *classp, EB_Hook_Code c, int argc, const unsigned int* argv)
{
    EB_Position pos;
    pos.page = argv[2];
    pos.offset = argv[3];

    return EB_SUCCESS;
}

EB_Hook myhooks[] = {
  { EB_HOOK_BEGIN_IN_COLOR_JPEG, myHookBEGIN_IN_COLOR_JPEG },
  { EB_HOOK_NULL, NULL }
};

void starthook() {

    const char * errs;
    const char * errmsg;

    EB_Book book;
    EB_Appendix appendix;
    EB_Hookset hookset;

    eb_initialize_book(&book);
    eb_initialize_appendix(&appendix);
    eb_initialize_hookset(&hookset);

    EB_Error_Code ecode;

    ecode = eb_set_hooks(&hookset, myhooks);
    ecode = eb_bind( &book,"/Users/vvw/Documents/dic/NHK");  // path.toUtf8();

    EB_Subbook_Code codes[EB_MAX_SUBBOOKS];
    int cnt;

    ecode = eb_subbook_list(&book, codes, &cnt);
    ecode = eb_set_subbook(&book, codes[0]);
    if( ecode != EB_SUCCESS )
    {
      errs =  eb_error_string( ecode );
      errmsg = eb_error_message( ecode );

    }

    EB_Position pos;
    ecode = eb_text(&book, &pos);  // first word position

    ecode = eb_seek_text(&book, &pos);

    char buff[1024+1];
    ssize_t len;

    ecode = eb_read_text(&book, &appendix, &hookset, NULL,  // 可以传void** 进去，发生回调的时侯别人会原样回传给你
                1024, buff, &len);
}
```



```
#include "ebook.h"
#include "book.h"

QEb::initialize();
```







