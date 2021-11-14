
#include <stdio.h>
#include "stdarg.h"
#include <string.h>
#include <ctype.h>

#define ASSERT(value) if (!(value)) { if (PFLOG != NULL) fclose(PFLOG); exit(-7);}

#define bool  int
#define true  1
#define false 0

#define SPLITTER      ','

#define DBWORDWAV     "./db/wordwav.db"
#define DBINFLECTION  "./db/wordinfle.db"
#define DIRAUDIO      "./audio"
#define INFLESOURCE   "./data/collins.html.utf8"

#if __STDC_VERSION__ < 199901L
# if __GNUC__ >= 2
#  define __func__ __FUNCTION__
# else
#  define __func__ "<unknown>"
# endif
#endif

// these functions intended use for lua program
char* path_DBWORDWAV() {
    return DBWORDWAV;
}

char* path_DBINFLECTION() {
    return DBINFLECTION;
}

char* path_DIRAUDIO() {
    return DIRAUDIO;
}

char* path_INFLESOURCE() {
    return INFLESOURCE;
}

char* splitter() {
    static char spliter[2] = {SPLITTER, 0};
    return spliter;
}

static FILE *PFLOG = NULL;
#define LOGFNAME "log"

void LOG(char *msg) {
    if (PFLOG == NULL) {
        if ( (PFLOG = fopen(LOGFNAME,"wb")) == 0) ("can't open file '%s' in %s", LOGFNAME, __func__);
    }
    fprintf(PFLOG, "%s\n", msg);
    printf("%s\n", msg);
}

void DBLOG(char *patern, ...) {
    char buf[512];
    va_list vlist;
    va_start(vlist, patern);
    vsnprintf(buf, 512, patern, vlist);
    va_end(vlist);
    LOG(buf);
}

void ERR(char *msg) {
    LOG(msg);
    ASSERT(0);
}

void DBERR(char *patern, ...) {
    char buf[512];
    va_list vlist;
    va_start(vlist, patern);
    vsnprintf(buf, 512, patern, vlist);
    va_end(vlist);
    LOG(buf);
    ASSERT(0);
}

int sizef(FILE *pf) {
    int cur, siz;
    cur = ftell(pf);
    fseek(pf, 0, SEEK_END);
    siz = ftell(pf);
    fseek(pf, cur, SEEK_SET);
    return siz;
}

char *data(char *fname, int *out_siz_buf) {
    FILE *pf;
    char *buf;
    int siz, siz_r;
    if ( (pf = fopen(fname,"rb")) != 0) {
        siz = sizef(pf);
        buf = (char*)malloc(siz); if (buf == 0) { ERR("malloc fail. in data()"); }
        siz_r = fread(buf, 1, siz, pf); if (siz_r != siz) { ERR("Error in data(). fread file siz not correct"); }
    } else {
        DBERR("can't open file '%s' in %s", fname, __func__);
    }
    *out_siz_buf = siz_r;
    fclose(pf);
    return buf;
}

// buf 指向的数组大小增加n 字节，新增的字节置初值0。警告：该函数可能会改变buf 指向的内存地址，使用时请千万小心。
void increases_nbytes(void **buf, int *siz, int n) {
    if (*buf == NULL && *siz != 0) DBERR("Error: bad argument. in fuction %s()", __func__);
    if (*siz < 0 || n <= 0) DBERR("Error: bad argument. in fuction %s()", __func__);
    char * r = realloc(*buf, *siz + n);
    if (r == NULL) DBERR("ERROR: realloc fail. in function %s()", __func__);
    if (r != *buf) LOG("Warning: realloc change point's addr");
    *buf = r;
    memset(*buf+*siz, 0, n);
    *siz = *siz + n;
}

// use for free memory that allocate by split() function
void free_split_memory(unsigned int *pointerArray) {
    if (pointerArray != NULL) {
        free( (void*)(pointerArray[0]) );  // free memory that pointerArray pointer to
        free( (void*)pointerArray );       // free pointerArray itself
    }
}

// @buf     : a string that terminal with NULL, it contains more word, each word use  a seperater [3th argument c] splits.
// @siz     : nbyte
// @c       : seperater
// @out_siz : nbyte of the buffer that this function return. it was a pointer array exactly.
unsigned int *split(const char *buf, int siz, char c, int *out_siz) {
    if (buf == NULL || siz <= 0 || siz > 1024 || buf[siz -1] != 0 || strlen(buf) != siz - 1) DBERR("ERROR: bad argument. in fuction %s()", __func__);
    const char de[2] = {c, 0};
    char *bf = (char*)calloc(1, siz);
    unsigned int *pointerArray = NULL; int szofpointerArray = 0; int nPointer = szofpointerArray / (sizeof (char*));

    memcpy(bf, buf, siz);

    int i = 0;
    increases_nbytes( (void**)&pointerArray, &szofpointerArray, sizeof(char*) );
    pointerArray[i] = strtok(bf, de);
    if (pointerArray[i] != NULL) {
        //DBLOG("%s", (char*)(*pointerArray));
        char *p;
        while ( (p=strtok(NULL, de)) != NULL ) {
            increases_nbytes( (void**)&pointerArray, &szofpointerArray, sizeof(char*) );
            i = i + 1;
            pointerArray[i] = p;
            //DBLOG("%s", (char*)(*(pointerArray+i)) );
        }
    } else {
        free((void*)pointerArray);
        pointerArray = NULL;
        return NULL;
    }
    nPointer = szofpointerArray / (sizeof (char*));
    //DBLOG("nPointer = %d", nPointer);
    *out_siz = szofpointerArray;
    return pointerArray;
}

char* lowercase(char *word) {
    #define TMPSIZE 128
    static char buf[TMPSIZE] = {0};
    if (word == NULL) DBERR("ERROR: NULL pointer. in function %s()", __func__);
    if ( strlen(word) > TMPSIZE -1 ) DBERR("ERROR: size of 'word' too large. in function %s()", __func__);
    memset(buf, 0, TMPSIZE);
    memcpy(buf, word, strlen(word)+1);
    int i;
    for (i=0; i < strlen(buf); i++)
        buf[i] = tolower(buf[i]);
    return buf;
}
