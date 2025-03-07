
#include <eb/eb.h>
#include <eb/text.h>
#include <eb/appendix.h>
#include <eb/error.h>
#include <eb/binary.h>
#include <eb/font.h>

#include <stdio.h>
#include <stdlib.h>

#define NHK "/Users/vvw/Documents/dic/NHK/exported/"
#define PATHJOIN(dir, path) dir##path

EB_Error_Code myHookBEGIN_IN_COLOR_JPEG(EB_Book *book, EB_Appendix*a,
    void *classp, EB_Hook_Code c, int argc, const unsigned int* argv)
{
    EB_Position pos;
    pos.page = argv[2];
    pos.offset = argv[3];
    
    EB_Error_Code ecode = eb_set_binary_color_graphic(book, &pos);
    char imgpath[1024+1];
    char imgname[512+1];
    sprintf(imgname, "%dx%d.jpg", pos.page, pos.offset);
    sprintf(imgpath, "%s%s", NHK, imgname);
    
    FILE * fp = fopen(imgpath, "wb"); // 二进制写
    #define BinaryBufferSize 50000
    char *buf = (char*)malloc(BinaryBufferSize);
    ssize_t length;
    for( ; ; ) {
        ecode = eb_read_binary(book, BinaryBufferSize, buf, &length );
        if (ecode != EB_SUCCESS) {
            break;
        }
        if (length > 0) {
            fwrite(buf, sizeof(char), length, fp);
        }
        if (length < BinaryBufferSize) {
            break;
        }
    }
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

    eb_initialize_library();
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

int main(int argc, char *argv[])
{
    starthook();
    return 0;
}
