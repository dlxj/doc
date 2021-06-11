
// ��checkinput.h �ļ�����������Ϊ��ʹ�������ܼ��һ����

#include "checkinput.h"  
#include <dinput.h>

namespace CheckInput {
	
	int MouseX(void);
	int MouseY(void);
	int MouseDown (Button);
	int MouseHit (Button);
	bool KeyDown (Key);
	bool KeyHit (Key);

	enum Button{LeftButton = 1, RightButton = 2};
	enum Key{Enter = 13, ESC = 27, Number1 = 49};   // �س�������1��ASCII��

	void UpdateMouse (void);
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
}