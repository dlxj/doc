
#ifndef CHECK_INPUT_H
#define CHECK_INPUT_H

namespace CheckInput {

	extern enum Button;
	extern enum Key;   // �س�������1��ASCII��

	int MouseX(void);
	int MouseY(void);
	int MouseDown (Button);
	int MouseHit (Button);
	bool KeyDown (Key);
	bool KeyHit (Key);

	void UpdateMouse(void);


}

#endif