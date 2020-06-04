export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
CC=gcc
#CC=arm-none-linux-gnueabi-gcc
main:main.c libtest.so
	$(CC) -o main main.c -ldl -L. -ltest
libtest.so:myalib.c
	$(CC) -shared -fPIC -o libtest.so myalib.c
clean:
	rm -f *.i *.s *.o main libtest.so
