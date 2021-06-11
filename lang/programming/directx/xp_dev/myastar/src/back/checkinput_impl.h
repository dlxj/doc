
// 将checkinput.h 文件包含进来是为了使编译器能检查一致性

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
	enum Key{Enter = 13, ESC = 27, Number1 = 49};   // 回车和数字1的ASCII码

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