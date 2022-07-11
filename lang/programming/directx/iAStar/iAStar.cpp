
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#include <windows.h>  //Windows header
#include <windowsx.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <mmsystem.h>
//#include <fstream.h>
#endif

#include "graphics.h"

//-----------------------------------------------------------------------------
// Name: WndProc
// Desc: Windows callback function that processes Windows messages. It is
//	called by both CheckWinMessages() and by Windows directly.
//-----------------------------------------------------------------------------
LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	return DefWindowProc(hwnd, msg, wParam, lParam);
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



#define WINDOW_NAME L"Program" //Visible when game is minimized

HWND hWnd = NULL;
int g_screenWidth = 1440; //800;
int g_screenHeight = 900; //600;


//#pragma comment(lib,"dinput.lib") 

int pathfinderID = 1;
int startX = 3, startY = 6; //Set seeker location
int targetX = 12, targetY = 6;//Set initial target location. This can
							  //be changed by right-clicking on the map.

int drawing = 0, erasing = 0;

using Graphics::cImage;

cImage* mousePointer;
cImage* grid; cImage* greengrid; cImage* bluegrid; cImage* dottedPath;
cImage* greenBlock = NULL; cImage* redBlock; cImage* wallBlock;
cImage* parentArrow[9]; cImage* number[10];



//-----------------------------------------------------------------------------
// Name: LoadGraphics
// Desc: Loads graphics
//-----------------------------------------------------------------------------
void LoadGraphics(void)
{
	using namespace Graphics;

	SetFont(L"Arial", 14);

	mousePointer = Graphics::LoadImage(L"./images/red_pointer.bmp");
	//HBITMAP h = (HBITMAP)LoadImage(GetModuleHandle(NULL), L"D:\\workcode\\directx\\iAStar\\Debug\\images\\red_pointer.bmp", IMAGE_BITMAP, 0, 0,
	//	LR_DEFAULTSIZE | LR_LOADFROMFILE);
	//HBITMAP h = (HBITMAP)LoadImage(GetModuleHandle(NULL), L"./images/red_pointer.bmp", IMAGE_BITMAP, 0, 0,
	//	LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	MaskImage(mousePointer, 255, 255, 255);

	//Load grids
	grid = LoadImage(L"./images/grid.bmp");
	MaskImage(grid, 255, 255, 255);
	greengrid = LoadImage(L"./images/greengrid.bmp");
	MaskImage(greengrid, 255, 255, 255);
	bluegrid = LoadImage(L"./images/bluegrid.bmp");
	MaskImage(bluegrid, 255, 255, 255);
	dottedPath = LoadImage(L"./images/path.bmp");
	MaskImage(dottedPath, 255, 255, 255);

	//Load blocks
	greenBlock = LoadImage(L"./images/start.bmp");
	redBlock = LoadImage(L"./images/end.bmp");
	wallBlock = LoadImage(L"./images/wall.bmp");


	//Load parentArrows - these point from a square to its parent in 
	//the pathfinding search.

	char buf[256] = { 0 };

	for (int z = 1; z <= 8; z++)
	{
		//CSTR string = "./images/arrow" + z + ".bmp";

		parentArrow[z] = LoadImage(L"./images/number0.bmp");
		MaskImage(parentArrow[z], 255, 255, 255);
	}


	//Load parentArrows - these point from a square to its parent in 
	//the pathfinding search.
	for (int z = 0; z <= 9; z++)
	{
		//CSTR string = combine "../images/number" + z + ".bmp";
		number[z] = LoadImage(L"./images/number0.bmp");
		MaskImage(number[z], 0, 0, 0);
	}
}

void Driver()
{
	//using namespace AStar;
	//using namespace CheckInput;

	Graphics::InitGraphics(g_screenWidth, g_screenHeight, 16, hWnd);
	LoadGraphics();
	

	//CheckInput::initDirectInput(hWnd);
	////CheckInput::UpdateMouse();

	//while (!KeyDown(ESC)) //While escape key not pressed
	//{
	//	int CheckWinMessages(void);
	//	CheckWinMessages();

	//	CheckUserInput();
	//	RenderScreen();
	//}

	////CheckUserInput();

	//Graphics::ReleaseObjects();

	////RenderScreen();
	//free(paths.steps);

}


//-----------------------------------------------------------------------------
// Name: WinMain
// Desc: Launch program.
//-----------------------------------------------------------------------------
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
	LPSTR lpCmdLine, int nCmdShow)
{
	//Declare window class
	WNDCLASSEX wc;
	wc.cbSize = sizeof(WNDCLASSEX);
	wc.style = 0; //window style
	wc.lpfnWndProc = WndProc; //Windows message function
	wc.cbClsExtra = 0; //unused
	wc.cbWndExtra = 0; //unused
	wc.hInstance = hInstance;
	wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);//program icon
	wc.hCursor = LoadCursor(NULL, IDC_ARROW); //program cursor
	wc.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
	wc.lpszMenuName = NULL;
	wc.lpszClassName = L"Windows DX";//window class name (see below)
	wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

	//Register the window class
	if (!RegisterClassEx(&wc)) return 0;

	//Create the window
	hWnd = CreateWindowEx(
		NULL,// extended style, not needed
		L"Windows DX", //window class name
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

	if (hWnd == NULL) return 0;
	ShowWindow(hWnd, nCmdShow);
	UpdateWindow(hWnd);
	CheckWinMessages();



	Driver();

	//MessageBox(hWnd, "hello", "prompt", MB_OK);


	return 0;
}
