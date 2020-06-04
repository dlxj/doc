
/*

man readdir
man opendir
man 2 stat

*/

#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>
#include <stdio.h>

#include "std.c"

static void dirWalk(char *path, unsigned int **buf_4_save_pchar, int *nbytes, int level) {
    char buf[1025] = {0}; // EXTRA STORAGE MAY BE NEEDED
    if (path == NULL || strlen(path) <= 0) DBERR("ERROR: bad argument. in function %s", __func__);
    DIR *dir = opendir(path);
    if (dir == NULL) { DBERR("ERROR: '%s' %s. in function %s", path, strerror(errno), __func__); }
    struct dirent *d;
    while ( (d = readdir(dir))!= NULL) {
        if (d->d_type == DT_DIR) {
            //int i; for (i = 0; i < level; i++) printf("  ");
            //printf("%s\n", d->d_name);
            if (d->d_name[0] != '.') {
                strcpy(buf, path);
                strcat(buf, "/");
                strcat(buf, d->d_name);
                struct stat info;
                if (stat(buf, &info) == -1)  DBERR("stat() error on %s: %s", path, strerror(errno));
                if (! S_ISDIR(info.st_mode)) DBERR("'%s' not a dir. %s in function %s()", buf, __func__);
                dirWalk(buf, buf_4_save_pchar, nbytes, level+1);
            }
        } else if (d->d_type == DT_REG) {
            // normal file
            //int i; for (i = 0; i < level; i++) printf("  ");
            //printf("%s\n", d->d_name);
            strcpy(buf, path);
            strcat(buf, "/");
            strcat(buf, d->d_name);
            struct stat info;
            if (stat(buf, &info) == -1) DBERR("stat() error on %s: %s", path, strerror(errno));
            if (! S_ISREG(info.st_mode)) DBERR("'%s' not a normal file. %s in function %s()", buf, __func__);

            int len = strlen(buf) + 1;
            char *fname = (char*)calloc(len, 1);  // len item, each item's size is 1 byte, and init mem with 0
            memcpy(fname, buf, strlen(buf));

            increases_nbytes((void **)buf_4_save_pchar, nbytes, sizeof(char*));  // increases 4 bytes to store a char*
            int nfname = *nbytes / sizeof(char*);
            ((unsigned int *)*buf_4_save_pchar)[nfname -1] = fname;
        }
    }
    closedir(dir);
}

static unsigned int* fpaths(char *dir, int *out_nfname) {
    // buf 用来存char* 指针
    unsigned int *buf = NULL; int siz = 0;
    dirWalk(dir, &buf, &siz, 0);
    int nfname = siz / sizeof(char*);
    if (nfname <= 0 || buf == NULL) return NULL;
    *out_nfname = nfname;
    return buf;
}

int maindir() {
    char *path = DIRAUDIO;
    int nfname = 0;
    unsigned int *buf = fpaths(path, &nfname);
    if (buf != NULL && nfname <= 0) DBERR("something wrong. in %s", __func__);
    if (buf != NULL) {
        int i;
        for (i = 0; i < nfname; i++) {
            printf("%s\n", buf[i]);
            free((void*)buf[i]);
        }
    } else {
        DBLOG("'%s' there is no files.", path);
    }
    return 0;
}
