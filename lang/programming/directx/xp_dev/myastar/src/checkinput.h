
#ifndef CHECK_INPUT_H
#define CHECK_INPUT_H



//#pragma comment(lib,"dinput.lib") 

extern HWND hWnd;

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
	//void ReleaseDirectInput(void);
	//bool initDirectInput(HWND);
}

#endif