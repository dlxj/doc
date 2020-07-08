



## 查看导出函数



**注意dll 的相互依赖**，调用不成功可能是因为缺了它的依赖dll



Visual studio，Tools -> Visual studio  Command Prompt

```
dumpbin /exports a.dll
```





```c++
extern "C" __declspec(dllexport)  int __cdecl reconize(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness) {


calldll
int dll() {
    typedef int(_cdecl*FunctionPtr)(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness);
    //typedef int(_stdcall*FunctionPtr)(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness);
    
    //reconize(char * imageFileName, char * p, int numOfTest, int numOfOption, double rate, unsigned int brightness);
    char *imageName = "IMG_0167.JPG";
    char *fileName = "hi.txt";
    char *buf = (char*)malloc(1024*1024*3);
    memset(buf, 0, 1024 * 1024 * 3);
    HINSTANCE   ghDLL = NULL;
    FunctionPtr   reconize;
    ghDLL = LoadLibrary("rec32160622.dll");
    ASSERT(ghDLL != NULL);
    reconize = (FunctionPtr)GetProcAddress(ghDLL, "reconize");
    ASSERT(reconize != NULL);
    //reconize(imageName, buf);
    reconize("IMG_1119.jpg", buf, 100, 4, 0.4, 125);
    //dataWrite(fileName, buf, strlen(buf));
    //fprintf(stdout, buf);
    printf("done.");
    free(buf);
    getchar();
    return 0;
} 


2)_cdecl调用
   _cdecl是C/C++的缺省调用方式，参数采用从右到左的压栈方式，由调用者完成压栈操作 ，传送参数的内存栈由调用者维护。
   _cedcl约定的函数只能被C/C++调用，每一个调用它的函数都包含清空堆栈的代码，所以产生的可执行文件大小会比调用_stdcall函数的大。
   按C编译方式，_cdecl调用约定仅在输出函数名前面加下划线，形如_functionname。
   按C++编译方式，可参看（三）
```





```c++




https://github.com/node-ffi/node-ffi/blob/master/example/factorial/factorial.c


#include <stdint.h>
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
EXPORT uint64_t factorial(int max) {
    int i = max;
    uint64_t result = 1;
    while (i >= 2) {
        result *= i--;
    }
    return result;
}  





var FFI = require('ffi');

var hi = new FFI.Library('hi', {
   'factorial': [
      'int32', ['int32']
   ]
});
console.log ( hi.factorial(3) );




C:\Documents and Settings\Administrator\node_modules\ffi

var FFI = require('G:/Program Files/nodejs/node_modules/ffi');




原因：win7下的64位系统，在运行程序的时候，需要的DLL必须是64位系统编译的，VS2010也必须在安装的时候，选择了32位编译的支持。如果安装的时候，已经选择了，那么出现该问题的解决办法：

      （1）右键项目名，点击属性，弹出项目属性页，找到链接器----高级，修改右侧的目标计算机，选择有X64的那个选项。

      （2）右键项目名，选择清理解决方案，清理完之后选择X64平台编译器，然后重新生成解决方案，便可以调试成功。选择X64平台编译器如下图：



来源： <http://www.cnblogs.com/CodeGuy/archive/2013/05/17/3083518.html>
 




var FFI = require('ffi');


function TEXT(text){
   return new Buffer(text, 'ucs2').toString('binary');
}


var user32 = new FFI.Library('user32', {
   'MessageBoxW': [
      'int32', [ 'int32', 'string', 'string', 'int32' ]
   ]
});


var OK_or_Cancel = user32.MessageBoxW(
   0, TEXT('I am Node.JS!'), TEXT('Hello, World!'), 1
);




#include <stdint.h>
 
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
 
EXPORT uint64_t factorial(int max) {
  int i = max;
  uint64_t result = 1;
 
  while (i >= 2) {
    result *= i--;
  }
 
  return result;
}




#include "stdio.h"
#include "windows.h"


#include <intrin.h>
#define ASSERT(value) if (!(value)) { __writecr0(__readcr0() & ~0x1000); }


char *reconize() {
  static char tmp[8] = {0};
	typedef int (*FunctionPtr)(int);
	HINSTANCE   ghDLL = NULL;
	FunctionPtr   factorial;
  int ret;


  #define BUFFERLEN 10240
  char *buf = (char*)malloc(BUFFERLEN);
  memset(buf, 0, BUFFERLEN);
  //free(buf);


	//ghDLL = LoadLibrary("ExamSheetReader.dll");
	ghDLL = LoadLibrary("64dll.dll");
	ASSERT(ghDLL != NULL);


  factorial = (FunctionPtr)GetProcAddress(ghDLL, "factorial");
  ASSERT(factorial != NULL);


  ret = factorial(3);
  sprintf (tmp, "%d", ret);
  //ret = rcnz("imageName", buf, BUFFERLEN);


  free(buf);
	return tmp;
}


#include <node.h>


using namespace v8;


void Add(const FunctionCallbackInfo<Value>& args) {
  char *json = reconize();


  Isolate* isolate = Isolate::GetCurrent();
  HandleScope scope(isolate);


  if (args.Length() < 2) {
    isolate->ThrowException(Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong number of arguments")));
    return;
  }


  if (!args[0]->IsNumber() || !args[1]->IsNumber()) {
    isolate->ThrowException(Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong arguments")));
    return;
  }


  double value = args[0]->NumberValue() + args[1]->NumberValue();
  Local<Number> num = Number::New(isolate, value);


  Local<String> str = String::NewFromUtf8(isolate, json);
  args.GetReturnValue().Set(str);
}


void Init(Handle<Object> exports) {
  NODE_SET_METHOD(exports, "add", Add);
}


NODE_MODULE(addon, Init)








var FFI = require('ffi'),
    ref = require('ref'),Struct = require('ref-struct');/* First, create the necessary data structures that'll be used
   by our windows api calls. */var pointStruct = Struct({'x': 'long','y': 'long'});var msgStruct = Struct({'hwnd': 'int32','message': 'int32','wParam': 'int32','lParam': 'int32','time': 'int32','pt': pointStruct
});var msgStructPtr = ref.refType(msgStruct);/* Second, register the functions we'd like to use by providing
   their method signatures. */var user32 = new FFI.Library('user32', {'RegisterHotKey': ['bool', ['int32', 'int', 'int32', 'int32']],'GetMessageA': ['bool', [msgStructPtr, 'int32', 'int32', 'int32']]/* You may prefer to use PeekMessageA which has the same
     signature as GetMessageA, but is non-blocking. I haven't
     tested it, though.

});

/* Third, register your hotkeys. I wanted to control a media player,
   so these keys reflect that. */var ALT = 0x0001,
    CTRL = 0x0002,
    SHIFT = 0x0004;var MEDIA_NEXT = 0xB0,
    MEDIA_PREV = 0xB1,
    MEDIA_STOP = 0xB2,
    MEDIA_PLAY_PAUSE = 0xB3,
    MEDIA_LAUNCH = 0xB5;var PERIOD = 0xBE,
    COMMA = 0xBC,
    EQUAL = 0xBB,
    DIVIDE = 0xBF,
    SQUOTE = 0xDE,
    PAGEUP = 0x21,
    PAGEDOWN = 0x22;

registrations = [];
registrations.push(user32.RegisterHotKey(0, 1, 0, MEDIA_NEXT));
registrations.push(user32.RegisterHotKey(0, 1, 0, MEDIA_PREV));
registrations.push(user32.RegisterHotKey(0, 1, 0, MEDIA_STOP));
registrations.push(user32.RegisterHotKey(0, 1, 0, MEDIA_PLAY_PAUSE));
registrations.push(user32.RegisterHotKey(0, 1, 0, MEDIA_LAUNCH));
registrations.push(user32.RegisterHotKey(0, 1, CTRL, PERIOD));
registrations.push(user32.RegisterHotKey(0, 1, CTRL, COMMA));
registrations.push(user32.RegisterHotKey(0, 1, CTRL, EQUAL));
registrations.push(user32.RegisterHotKey(0, 1, CTRL, DIVIDE));
registrations.push(user32.RegisterHotKey(0, 1, CTRL | ALT, PAGEUP));
registrations.push(user32.RegisterHotKey(0, 1, CTRL | ALT, PAGEDOWN));// an array of booleans telling us which registrations failed/succeeded
console.log(registrations);/* Fourth, wait for new hotkey events from the message queue. */var myMsg = new msgStruct;while (user32.GetMessageA(myMsg.ref(), 0, 0, 0)) {var key = myMsg.lParam >> 16;switch (key) {case MEDIA_NEXT: console.log('media next'); break;case MEDIA_PREV: console.log('media prev'); break;case MEDIA_STOP: console.log('media stop'); break;case MEDIA_PLAY_PAUSE: console.log('media play/pause'); break;case MEDIA_LAUNCH: console.log('media launch'); break;case PERIOD: console.log('next'); break;case COMMA: console.log('previous'); break;case EQUAL: console.log('play/pause'); break;case DIVIDE: console.log('info'); break;case PAGEUP: console.log('volume up'); break;case PAGEDOWN: console.log('volume down'); break;default: console.log('undefined hotkey', key, key.toString(16));}}

If you want this to work with node-webkit, make sure you build all the native add-ons with nw-gypwith the --target set to your version of node-webkit (0.5.1 in my case):

# Make sure you run this command in the following directories (where the binding.gyp files are):#  node_modules/ffi/#  node_modules/ffi/node_modules/ref/#  node_modules/ref/
$ nw-gyp clean configure --target=v0.5.1 build

Review the MSDN docs to understand the method signatures and structs used. Hope this helps!



来源： <http://stackoverflow.com/questions/14799035/node-webkit-winapi?lq=1>


```





