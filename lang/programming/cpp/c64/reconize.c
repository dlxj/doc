#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT int one() {
	return 1;
}

#include "stdio.h"
#include "windows.h"

// #define ASSERT(value) if (!(value)) { _asm{int 3};}
	// nonstandard extension used : '_asm' keyword not supported on this architecture
	//Using Microsoft's compiler intrinsics,
	//#include <intrin.h>
	//__writecr0(__readcr0() & ~0x1000);
#include <intrin.h>
#define ASSERT(value) if (!(value)) { __writecr0(__readcr0() & ~0x1000); }
// 在64位的windows系统中，一个64位进程不能加载一个32位dll，同理一个32位进程也不能加载一个64位dll。

void dataWrite(char *fname, char *dat, int siz) {
	FILE *pf;
	if ((pf = fopen(fname, "wb")) != 0) {
		fwrite(dat, siz, 1, pf);
	}
	else {
		printf("can't open file '%s' in %s", fname, "dataWrite");
	}
	fclose(pf);
}

int main(int argc, char **argv) {
	typedef int(_stdcall*FunctionPtr)(char *, char *);
	argv[1] = "IMG_0167.JPG";
	argv[2] = "hi.txt";
	char *imageName = argv[1];
	char *fileName = argv[2];
	char *buf = (char*)malloc(10240);
	memset(buf, 0, 10240);

	HINSTANCE   ghDLL = NULL;

	FunctionPtr   ESR_getJsonFromImageFile;
	ghDLL = LoadLibrary("ExamSheetReader.dll");
	ASSERT(ghDLL != NULL);

	ESR_getJsonFromImageFile = (FunctionPtr)GetProcAddress(ghDLL, "ESR_getJsonFromImageFile");
	ASSERT(ESR_getJsonFromImageFile != NULL);

	ESR_getJsonFromImageFile(imageName, buf);

	dataWrite(fileName, buf, strlen(buf));
	fprintf(stdout, buf);
	free(buf);
	getchar();
}

// https://github.com/node-ffi/node-ffi/blob/master/example/factorial/factorial.c

// #include <stdint.h>
// #if defined(WIN32) || defined(_WIN32)
// #define EXPORT __declspec(dllexport)
// #else
// #define EXPORT
// #endif
// EXPORT uint64_t factorial(int max) {
//     int i = max;
//     uint64_t result = 1;
//     while (i >= 2) {
//         result *= i--;
//     }
//     return result;
// }  


// var FFI = require('ffi');
// var hi = new FFI.Library('hi', {
//    'factorial': [
//       'int32', ['int32']
//    ]
// });
// console.log ( hi.factorial(3) );