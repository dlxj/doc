
#ifndef CHECK_INPUT_H
#define CHECK_INPUT_H

namespace CheckInput {

	extern enum Button;
	extern enum Key;   // 回车和数字1的ASCII码

	int MouseX(void);
	int MouseY(void);
	int MouseDown (Button);
	int MouseHit (Button);
	bool KeyDown (Key);
	bool KeyHit (Key);

	void UpdateMouse(void);


}

#endif