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
#include "checkinput_impl.h"
#include "astarlibrary.h"


#define WINDOW_NAME "Program" //Visible when game is minimized

HWND hWnd = NULL;
int g_screenWidth = 1440; //800;
int g_screenHeight = 900; //600;


//#pragma comment(lib,"dinput.lib") 

int pathfinderID = 1;
int startX = 3, startY = 6; //Set seeker location
int targetX = 12, targetY = 6;//Set initial target location. This can
							  //be changed by right-clicking on the map.

int drawing=0, erasing=0;

using Graphics::cImage;

cImage* mousePointer; 
cImage* grid; cImage* greengrid; cImage* bluegrid; cImage* dottedPath;
cImage* greenBlock=NULL; cImage* redBlock; cImage* wallBlock;
cImage* parentArrow[9]; cImage* number[10];


void LoadGraphics (void);
void RenderScreen ();
void CheckUserInput (void);
void Driver()
{
	using namespace AStar;
	using namespace CheckInput;

	//Graphics::InitGraphics(800,600,16,hWnd);
	Graphics::InitGraphics(g_screenWidth,g_screenHeight,16,hWnd);
	LoadGraphics();

	CheckInput::initDirectInput(hWnd);
	//CheckInput::UpdateMouse();

    while (!KeyDown(ESC)) //While escape key not pressed
    {
		int CheckWinMessages(void);
		CheckWinMessages();

		CheckUserInput();
		RenderScreen();
	}

	//CheckUserInput();

	Graphics::ReleaseObjects();
	
	//RenderScreen();
	free(paths.steps);

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
	using namespace AStar;

	// Clears the screen
	Cls();

	Graphics::DrawBlock (greenBlock,startX*50,startY*50);
	Graphics::DrawBlock (redBlock,targetX*50,targetY*50);
	//Graphics::DrawImage (mousePointer,400,300);

	/*
	if (paths.lenght > 0)
	{
		int len = paths.lenght;
		for (int i=0; i<len; i++)
		{
			int x = paths.steps[i].x;
			int y = paths.steps[i].y;
			DrawImage (dottedPath,x*50,y*50);
		}
	}*/

	for (int x = 0; x <= AStar::mapWidth - 1; x++) //draw each of 16 tiles across the screen
	{
		for (int y = 0; y <= AStar::mapHeight - 1; y++) //draw each of 12 tiles down the screen
		{
			
			//Draw blue walls
			if (walkability[x][y] == unwalkable) DrawBlock(wallBlock,x*50,y*50);
			
			//Draw paths
			if (whichList[x][y] == 3) DrawImage (dottedPath,x*50,y*50);

			//Draw the grid overlay.
			DrawImage (grid,x*50,y*50);
		}
	}

	
	DrawImage (mousePointer,CheckInput::MouseX(),CheckInput::MouseY());

	Graphics::Flip();
}


//-----------------------------------------------------------------------------
// Name: CheckUserInput
// Desc: Process key and mouse presses.
//-----------------------------------------------------------------------------
void CheckUserInput (void) 
{
	using namespace CheckInput;
	using namespace	AStar;

	
	static int path=0;
	
	if (MouseDown(LeftButton) == 0 && MouseDown(RightButton) == 0) drawing = 0;
	if (MouseDown(LeftButton) == 0 && MouseDown(RightButton) == 0) erasing = 0;
	int mouseXCoordinate = MouseX()/50;
	int mouseYCoordinate = MouseY()/50;	
	
	//Draw and Erase walls (blue squares)
	if (MouseDown(LeftButton) == 1 && (!(KeyDown(G))))//if not "g" key
	{
		//Draw walls
		if (walkability[mouseXCoordinate][mouseYCoordinate]
			== walkable && erasing == 0)
		{
			walkability[mouseXCoordinate][mouseYCoordinate] = unwalkable;
			drawing = 1;
		}
		
		//Erase walls	
		if (walkability[mouseXCoordinate][mouseYCoordinate]
			== unwalkable && drawing == 0)
		{
			walkability[mouseXCoordinate][mouseYCoordinate] = walkable;		erasing = 1;
		}
	}

	//Move red target square around
	if (MouseHit(RightButton) == 1) 
	{
		targetX = mouseXCoordinate;
		targetY = mouseYCoordinate;
	}
		
	//Move green starting square around
	if (KeyDown(G)) {// if g key is down while left clicking	
		if (MouseDown(LeftButton) == 1) {
			startX = mouseXCoordinate;
			startY = mouseYCoordinate;
	}}
	
	//Start A* pathfinding search if return/enter key is hit
	if (path == notfinished) { //if path not searched
		if (KeyHit(Enter))
		{
			path=FindPath(pathfinderID,startX*50,startY*50,targetX*50,targetY*50);	
			if (path == found) ReadPath(pathfinderID);	
			whichList[startX][startY] = 0;//don't highlight the start square (aesthetics)	
		}
	}
	
	//Reset after finishing A* search if pressing mouse button or "1" or enter key 
	if (path != notfinished) {//if path is done
		if (MouseDown(LeftButton)==1 || MouseDown(RightButton)==1 || KeyHit(Enter)) {
			for (int x = 0; x < mapWidth;x++)
			{
				for (int y = 0; y < mapHeight;y++)
					whichList [x][y] = 0;
			}
			path = notfinished;
		}	
	}
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

	//MessageBox(hWnd, "hello", "prompt", MB_OK);

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
