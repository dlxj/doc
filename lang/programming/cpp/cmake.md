

# CMAKE



## CMAKE_CURRENT_SOURCE_DIR



cmakelist.txt 所在的目录



```cmake
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/maclib/include")
```



# MAKE



ipaly/doc/koreader4k3.txt

```
arm-none-linux-gnueabi-gcc -o iplay iplay.c -I/usr/include -I/usr/include/alsa -L/usr/lib -lasound -lpthread -lm -lrt -ldl
```





## compile .so



```
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
CC=gcc
#CC=arm-none-linux-gnueabi-gcc
main:main.c libtest.so
	$(CC) -o main main.c -ldl -L. -ltest
libtest.so:myalib.c
	$(CC) -shared -fPIC -o libtest.so myalib.c
clean:
	rm -f *.i *.s *.o main libtest.so
```









