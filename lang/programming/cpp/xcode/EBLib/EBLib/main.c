//
//  main.c
//  EBLib

/*
 
 libeb 从这里下载自行编译，并安装到/usr/local
    https://github.com/mistydemeo/eb/
 
 Header Search Paths
    /usr/local/include
 Library Search Path
    /usr/local/lib

 Build Phase -> Link Binary With Librarie
    libeb.16.dylib
    # 从/usr/local/lib 拖这个文件到界面上
 
 
 */

#include <stdio.h>

#include <eb/eb.h>
#include <eb/binary.h>
#include <eb/text.h>
#include <eb/font.h>
#include <eb/appendix.h>
#include <eb/error.h>

// 成功回调图片
EB_Error_Code iHookBEGIN_IN_COLOR_JPEG(EB_Book *book, EB_Appendix *appendix,
    void *classp, EB_Hook_Code code, int argc, const unsigned int* argv)
{

    EB_Position spos, epos;
    spos.page = argv[ 2 ];
    spos.offset = argv[ 3 ];
    epos.page = argv[ 4 ];
    epos.offset = argv[ 5 ];
    
    return EB_SUCCESS;

}

int main(int argc, const char * argv[]) {
    
    EB_Hook ihooks[] = {
      { EB_HOOK_BEGIN_IN_COLOR_JPEG, iHookBEGIN_IN_COLOR_JPEG },
      { EB_HOOK_NULL, NULL }
    };

    EB_Book book;
    EB_Appendix appendix;
    EB_Hookset hookset;
    EB_BookList bookList;

    eb_initialize_book(&book);
    eb_initialize_appendix(&appendix);
    eb_initialize_hookset(&hookset);

    EB_Error_Code ecode;
    //extern EB_Hook ihooks[];
    ecode = eb_set_hooks(&hookset, ihooks);
    ecode = eb_bind( &book,"/Users/vvw/Documents/dic/NHK" );
    
    eb_finalize_book( &book );
    eb_finalize_appendix(&appendix);
    
    EB_Subbook_Code codes[EB_MAX_SUBBOOKS];
    int cnt;

    ecode = eb_subbook_list(&book, codes, &cnt);
    ecode = eb_set_subbook(&book, codes[0]);

    EB_Position pos;
    ecode = eb_text(&book, &pos);  // first word position
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
