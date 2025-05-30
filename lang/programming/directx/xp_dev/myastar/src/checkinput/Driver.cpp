//#include <windows.h>




#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#include <windows.h>  //Windows header
#include <windowsx.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <mmsystem.h>
#include <fstream.h>
#endif

#include <iostream>

#include "checkinput_impl.h"


#define WINDOW_NAME "Program" //Visible when game is minimized

HWND hWnd = NULL;
int g_screenWidth = 800;
int g_screenHeight = 600;



//#pragma comment(lib,"dinput.lib") 



void Driver()
{
	using namespace CheckInput;
	using std::string;
	

	CheckInput::initDirectInput(hWnd);
	CheckInput::UpdateMouse();
	int x = CheckInput::MouseX();
	int y = CheckInput::MouseY();


	string str="MouseX=";
	char buf[10];
	
	itoa(x, buf, 10);
	str+=buf;
	str+="\nMouseY=";
	itoa(y, buf, 10);
	str+=buf;

	MessageBox(hWnd, "请按ESC键退出!!!", "重要提示", MB_OK);

    while (!KeyDown(ESC)) //While escape key not pressed
    {
		UpdateWindow (hWnd);

		int CheckWinMessages(void);
		CheckWinMessages();

		if (KeyDown(Number1))	
			MessageBox(hWnd, "你按了1键\n请按ESC键退出!!!", "prompt", MB_OK);
		
		if (KeyDown(Enter))		
			MessageBox(hWnd, "你按了Enter键\n请按ESC键退出!!!", "prompt", MB_OK);
	}	

	MessageBox(hWnd, str.c_str(),"title",MB_OK);
}


//-----------------------------------------------------------------------------
// Function Prototypes
//-----------------------------------------------------------------------------
LRESULT CALLBACK WndProc(HWND hwnd, UINT Message, WPARAM wParam, LPARAM lParam);
int CheckWinMessages(void);
void GameMain(HWND hwnd);


int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
                 LPSTR lpCmdLine, int nShowCmd)
{

	//Declare window class
	WNDCLASSEX wc;
	wc.cbSize        = sizeof(WNDCLASSEX);
	wc.style         = 0; //window style
	wc.lpfnWndProc   = WndProc; //Windows message function
	wc.cbClsExtra    = 0; //unused
	wc.cbWndExtra    = 0; //unused
	wc.hInstance     = hInstance;
	wc.hIcon         = LoadIcon(NULL, IDI_APPLICATION);//program icon
	wc.hCursor       = LoadCursor(NULL, IDC_ARROW); //program cursor
	wc.hbrBackground = (HBRUSH) GetStockObject (BLACK_BRUSH);
	wc.lpszMenuName  = NULL;
	wc.lpszClassName = "Windows DX";//window class name (see below)
	wc.hIconSm       = LoadIcon(NULL, IDI_APPLICATION);
	
	//Register the window class
	if(!RegisterClassEx(&wc)) return 0;
	
    //Create the window
    hWnd = CreateWindowEx(
		NULL,// extended style, not needed
		"Windows DX", //window class name
		WINDOW_NAME, //window name (defined in main.cpp)
		WS_POPUP, //window style
		0, //horizontal position of Window
		0, //vertical position of Window
		GetSystemMetrics(SM_CXSCREEN), //window width
		GetSystemMetrics(SM_CYSCREEN), //window height
		NULL,//handle to parent of Window, if any
		NULL, //handle to menu or child-window
		hInstance,//handle to program instance
		NULL);//pointer to window creation data
	
	if(hWnd == NULL) return 0;
	ShowWindow (hWnd, nShowCmd);
	UpdateWindow (hWnd);
	CheckWinMessages();
	
	Driver();
	MessageBox(hWnd, "hello","title",MB_OK);

	return 0;	
}


//-----------------------------------------------------------------------------
// Name: CheckWinMessages
// Desc: Checks the Windows message queue and, if there are any,
//	forwards them to WndProc. Messages to close the program
//	are returned as such. This is called from GameMain(). It returns
//	0 when a close window message has been posted.
//-----------------------------------------------------------------------------
int CheckWinMessages(void)
{
	MSG msg; //Declare variable that holds messages
	if (PeekMessage(&msg, 0, 0, 0, PM_NOREMOVE))
    {
        if (!GetMessage(&msg, NULL, 0, 0))//Get the message
		{
			return msg.wParam;//returns 0 when closing
		}
        TranslateMessage(&msg);//Translate it
        DispatchMessage(&msg);//Send it to WndProc
    }
	return 1;
}


//-----------------------------------------------------------------------------
// Name: WndProc
// Desc: Windows callback function that processes Windows messages. It is
//	called by both CheckWinMessages() and by Windows directly.
//-----------------------------------------------------------------------------
LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	return DefWindowProc(hwnd, msg, wParam, lParam);
}