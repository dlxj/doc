



```c
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
```



