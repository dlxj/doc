

#include "checkinput_impl.h"
#include <assert.h>


extern HWND hWnd;
extern int  g_screenWidth;
extern int  g_screenHeight;


//-----------------------------------------------------------------------------
// Name: variable
//-----------------------------------------------------------------------------
namespace CheckInput {

LPDIRECTINPUT7              g_pDirectInput = NULL;
LPDIRECTINPUTDEVICE         g_pMouse=NULL;
DIMOUSESTATE                g_pMouseData;
int                         g_MouseX=0;
int                         g_MouseY=0;
bool                        g_MouseDown1=false;
bool                        g_MouseDown2=false;
int                         g_MouseHit1=0;
int                         g_MouseHit2=0;
int                         g_MouseSpeed=2;

}

//-----------------------------------------------------------------------------
// Name: MouseX()
// Desc: Returns the current x location of the mouse in screen coordinates.
//-----------------------------------------------------------------------------
int CheckInput::MouseX(void)
{
	return g_MouseX;
}


//-----------------------------------------------------------------------------
// Name: MouseY()
// Desc: Returns the current y location of the mouse in screen coordinates.
//-----------------------------------------------------------------------------
int CheckInput::MouseY(void)
{
	return g_MouseY;
}



//-----------------------------------------------------------------------------
// Name: UpdateMouse
// Desc: Updates the mouse by using Direct Input. This function can be 
//	called directly. It is also called automatically by the Flip() function.
//-----------------------------------------------------------------------------
void CheckInput::UpdateMouse (void)
{
	g_pMouse->GetDeviceState(sizeof(g_pMouseData), &g_pMouseData);
	
	//Get and calculate current mouse position info.
	if (abs(g_pMouseData.lX) <= 10) 
		g_MouseX = g_MouseX+g_pMouseData.lX;
	else
		g_MouseX = g_MouseX+g_MouseSpeed*g_pMouseData.lX;
	if (g_MouseX < 0) g_MouseX = 0;
	if (g_MouseX >= g_screenWidth) g_MouseX = g_screenWidth-1;
	
	if (abs(g_pMouseData.lY) <= 10) 
		g_MouseY = g_MouseY+g_pMouseData.lY;
	else 
		g_MouseY = g_MouseY+g_MouseSpeed*g_pMouseData.lY;
	if (g_MouseY < 0) g_MouseY = 0;
	if (g_MouseY >= g_screenHeight) g_MouseY = g_screenHeight-1;
	
	//Return left button status
	if (g_pMouseData.rgbButtons[0] & 0x80)
		g_MouseDown1 = true;
	else
		g_MouseDown1 = false;
	
	//Return right button status
	if (g_pMouseData.rgbButtons[1] & 0x80)
		g_MouseDown2 = true;
	else
		g_MouseDown2 = false;
}



bool CheckInput::initDirectInput(HWND hWnd)
{
	/*
	
	assert(hWnd!=NULL);
	
	//Set up Direct Input
	HANDLE hr = DirectInputCreateEx(
		GetModuleHandle(NULL),//HINSTANCE hinst,                  
		DIRECTINPUT_VERSION,                  
		IID_IDirectInput7,
		(VOID**)&g_pDirectInput,  
		NULL);
	if (hr != DD_OK) {ReleaseDirectInput();return false;}
	
	//Set up a Direct Input-enabled mouse
	hr = g_pDirectInput->CreateDeviceEx(
		GUID_SysMouse,// 
		IID_IDirectInputDevice7,
        (void**)&g_pMouse,
		NULL);
	if (hr != DD_OK) {ReleaseDirectInput();return false;}
	hr = g_pMouse->SetDataFormat(&c_dfDIMouse);
	if (hr != DD_OK) {ReleaseDirectInput();return false;}
	hr = g_pMouse->SetCooperativeLevel(hWnd,
		DISCL_NONEXCLUSIVE | DISCL_FOREGROUND);
	if (hr != DD_OK) {ReleaseDirectInput();return false;}
	
	//Set up buffer for MouseHit()
	DIPROPDWORD dipdw; //device property header data structure
	dipdw.diph.dwSize       = sizeof(DIPROPDWORD);
	dipdw.diph.dwHeaderSize = sizeof(DIPROPHEADER);
	dipdw.diph.dwObj        = 0;
	dipdw.diph.dwHow        = DIPH_DEVICE;
	dipdw.dwData            = 10; //# of buffered data items
	hr = g_pMouse->SetProperty(DIPROP_BUFFERSIZE, &dipdw.diph);
	if (hr != DI_OK)
	{
		if (hr == DI_PROPNOEFFECT) 
		{ReleaseDirectInput();return false;}
		else
		{ReleaseDirectInput();return false;}
	}
	
	//Acquire the mouse
	hr = g_pMouse->Acquire();
	if (hr != DD_OK) {ReleaseDirectInput();return false;}
	g_MouseX = g_screenWidth/2;
	g_MouseY = g_screenHeight/2;
	*/

	return true;
}


//-----------------------------------------------------------------------------
// Name: ReleaseObjects
// Desc: Releases Direct Draw objects. Called by EndGraphics and
//	Graphics functions.
//-----------------------------------------------------------------------------
void CheckInput::ReleaseDirectInput(void)
{

	//Release all Direct Input objects
	if (g_pDirectInput != NULL)
	{
		
		//Release Direct Input mouse
		if (g_pMouse != NULL)
		{
			g_pMouse->Unacquire();
			g_pMouse->Release();
			g_pMouse = NULL;
		}
		
		//Release Direct Input object
		g_pDirectInput->Release();
		g_pDirectInput = NULL;
	}
}
