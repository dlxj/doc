//-----------------------------------------------------------------------------
// WINDOWS LIBRARY: This include file contains functions that create
//  a Window and process Windows messages.
//-----------------------------------------------------------------------------

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

#include "graphics.h"


#define WINDOW_NAME "Program" //Visible when game is minimized

HWND hWnd = NULL;
int g_screenWidth = 800;
int g_screenHeight = 600;


//#pragma comment(lib,"dinput.lib") 


int startX = 3, startY = 6; //Set seeker location
int targetX = 12, targetY = 6;//Set initial target location. This can
							  //be changed by right-clicking on the map.

using Graphics::cImage;

cImage* mousePointer; 
cImage* grid; cImage* greengrid; cImage* bluegrid; cImage* dottedPath;
cImage* greenBlock=NULL; cImage* redBlock; cImage* wallBlock;
cImage* parentArrow[9]; cImage* number[10];


void LoadGraphics (void);
void RenderScreen ();
void Driver()
{
	Graphics::InitGraphics(800,600,16,hWnd);
	LoadGraphics();

	//Graphics::DrawBlock (greenBlock,startX*50,startY*50);
	//Graphics::DrawBlock (redBlock,targetX*50,targetY*50);
	//Graphics::DrawImage (mousePointer,400,300);
	RenderScreen();

}


//-----------------------------------------------------------------------------
// Name: LoadGraphics
// Desc: Loads graphics
//-----------------------------------------------------------------------------
void LoadGraphics (void)
{
	using namespace Graphics;

	SetFont("Arial",14);
	
	mousePointer = LoadImage("../images/red_pointer.bmp");
	MaskImage (mousePointer, 255,255,255);
	
	//Load grids
	grid = LoadImage("../images/grid.bmp");		
	MaskImage (grid,255,255,255);
	greengrid = LoadImage("../images/greengrid.bmp");		
	MaskImage (greengrid,255,255,255);
	bluegrid = LoadImage("../images/bluegrid.bmp");		
	MaskImage (bluegrid,255,255,255);
	dottedPath = LoadImage("../images/path.bmp");		
	MaskImage (dottedPath,255,255,255);
	
	//Load blocks
	greenBlock = LoadImage("../images/start.bmp");
	redBlock = LoadImage("../images/end.bmp");
	wallBlock = LoadImage("../images/wall.bmp");


	//Load parentArrows - these point from a square to its parent in 
	//the pathfinding search.
	
	for (int z = 1; z <= 8 ; z++)
	{
		CSTR string = combine "../images/arrow"+z+".bmp";
		parentArrow[z] = LoadImage(string.actualString);
		MaskImage (parentArrow[z],255,255,255);
	}
	
	
	//Load parentArrows - these point from a square to its parent in 
	//the pathfinding search.
	for (z = 0; z <= 9 ; z++)
	{
		CSTR string = combine "../images/number"+z+".bmp";
		number[z] = LoadImage(string.actualString);
		MaskImage (number[z],0,0,0);
	}
}

//-----------------------------------------------------------------------------
// Name: RenderScreen
// Desc: Draws stuff on screen
//-----------------------------------------------------------------------------
void RenderScreen () 
{

	using namespace Graphics;

	// Clears the screen
	Cls();

	Graphics::DrawBlock (greenBlock,startX*50,startY*50);
	Graphics::DrawBlock (redBlock,targetX*50,targetY*50);
	Graphics::DrawImage (mousePointer,400,300);
	
	DrawBlock (wallBlock,0*50,0*50);
	DrawImage (greengrid,1*50,0*50);
	DrawImage (bluegrid,2*50,0*50);
	DrawImage (dottedPath,3*50,0*50);

    DrawImage (parentArrow[1],4*50,0*50);
	DrawImage (parentArrow[2],5*50,0*50);	
	DrawImage (parentArrow[3],6*50,0*50);
	DrawImage (parentArrow[4],7*50,0*50);	
	DrawImage (parentArrow[5],8*50,0*50);
	DrawImage (parentArrow[6],9*50,0*50);
	DrawImage (parentArrow[7],10*50,0*50);
	DrawImage (parentArrow[8],11*50,0*50);

	DrawImage (number[0],0*50,1*50);
	DrawImage (number[1],1*50,1*50);
	DrawImage (number[2],2*50,1*50);
	DrawImage (number[3],3*50,1*50);
	DrawImage (number[4],4*50,1*50);
	DrawImage (number[5],5*50,1*50);
	DrawImage (number[6],6*50,1*50);
	DrawImage (number[7],7*50,1*50);
	DrawImage (number[8],8*50,1*50);
	DrawImage (number[9],9*50,1*50);

	//Draw the grid overlay.
	DrawImage (grid,0*50,2*50);
	DrawImage (grid,1*50,2*50);
	DrawImage (grid,2*50,2*50);
	DrawImage (grid,3*50,2*50);
	DrawImage (grid,0*50,3*50);
	DrawImage (grid,1*50,3*50);
	DrawImage (grid,2*50,3*50);
	DrawImage (grid,3*50,3*50);
	DrawImage (grid,0*50,4*50);
	DrawImage (grid,1*50,4*50);
	DrawImage (grid,2*50,4*50);
	DrawImage (grid,3*50,4*50);

	Graphics::Flip();
}




//-----------------------------------------------------------------------------
// Function Prototypes
//-----------------------------------------------------------------------------
LRESULT CALLBACK WndProc(HWND hwnd, UINT Message, WPARAM wParam, LPARAM lParam);
int CheckWinMessages(void);
//void GameMain(HWND hwnd);


//-----------------------------------------------------------------------------
// Name: WinMain
// Desc: Launch program.
//-----------------------------------------------------------------------------
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
   LPSTR lpCmdLine, int nCmdShow)
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
	ShowWindow (hWnd, nCmdShow);
	UpdateWindow (hWnd);
	CheckWinMessages();

	//GameMain(hwnd);//see main.cpp

	Driver();

	MessageBox(hWnd, "hello", "prompt", MB_OK);

	//Graphics::ReleaseObjects();

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
