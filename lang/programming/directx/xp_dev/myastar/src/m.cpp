
#include <windows.h>

#define DIRECTINPUT_VERSION 0x0700 
#include <dinput.h>

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
   LPSTR lpCmdLine, int nCmdShow)
{

	/**/
	//Set up Direct Input
	HRESULT hr = DirectInputCreateEx(
		GetModuleHandle(NULL),//HINSTANCE hinst,                  
		DIRECTINPUT_VERSION,                  
		IID_IDirectInput7,
		//(void**)&g_pDirectInput,  
		(void**)&g_pDirectInput,  
		NULL);
		

    return 0;
}