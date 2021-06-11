
#define DIRECTINPUT_VERSION 0x0700 
#include <dinput.h>

#pragma comment(lib,"dinput.lib") 

extern HWND hWnd;

namespace CheckInput {

	enum Button{LeftButton = 1, RightButton = 2};
	enum Key{Enter = 13, ESC = 27, G = 71, Number1 = 49};  

	extern LPDIRECTINPUT7              g_pDirectInput;
	extern LPDIRECTINPUTDEVICE         g_pMouse;
	extern DIMOUSESTATE                g_pMouseData;
	extern int                         g_MouseX;
	extern int                         g_MouseY;
	extern bool                        g_MouseDown1;
	extern bool                        g_MouseDown2;
	extern int                         g_MouseHit1;
	extern int                         g_MouseHit2;
	extern int                         g_MouseSpeed;
	
	int MouseX(void);
	int MouseY(void);
	int MouseDown (Button);
	void MoveMouse (int x, int y);
	int MouseHit (Button);
	bool KeyDown (Key);
	bool KeyHit (Key);
	
	void UpdateMouse(void);
	void ReleaseDirectInput(void);
	bool initDirectInput(HWND);
}