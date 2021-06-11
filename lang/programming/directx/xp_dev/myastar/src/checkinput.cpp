

#include "checkinput_impl.h"
#include <assert.h>


extern HWND hWnd;
extern int  g_screenWidth;
extern int  g_screenHeight;

typedef LONG HRESULT;


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



//-----------------------------------------------------------------------------
// Name: MouseX()
// Desc: Returns the current x location of the mouse in screen coordinates.
//-----------------------------------------------------------------------------
int MouseX(void)
{
	return g_MouseX;
}


//-----------------------------------------------------------------------------
// Name: MouseY()
// Desc: Returns the current y location of the mouse in screen coordinates.
//-----------------------------------------------------------------------------
int MouseY(void)
{
	return g_MouseY;
}


//-----------------------------------------------------------------------------
// Name: MouseDown()
// Desc: Returns whether the selected mouse is down. 
// - Example = Mouse demo
//-----------------------------------------------------------------------------
int MouseDown (Button button)
{
	UpdateMouse();
	if (button == 1)
		return g_MouseDown1;
	else
		return g_MouseDown2;
}

int MouseHitCheck (void);

//-----------------------------------------------------------------------------
// Name: MouseHit()
// Desc: Checks to see how many times a specific mouse button has been
//	hit since the last time this command was called.
// - Example = Mouse demo
//-----------------------------------------------------------------------------
int MouseHit (Button button)
{
	MouseHitCheck();
	if (button == LeftButton)
	{
		int temp = g_MouseHit1;
		g_MouseHit1 = 0;
		return temp;
	}
	else
	{
		int temp = g_MouseHit2;
		g_MouseHit2 = 0;
		return temp;
	}
	
}


//-----------------------------------------------------------------------------
// Name: MouseHitCheck()
// Desc: Checks to see how many times the mouse has been hit since the
//	last time this command was called. This command uses buffered Direct
//	Input data via GetDeviceData.
//-----------------------------------------------------------------------------
int MouseHitCheck (void)
{
	/**/
	DIDEVICEOBJECTDATA inputBuffer[16]; //array storing buffer items
	DWORD numberItems = 10; // number of items to be retrieved
	
	HRESULT hr = g_pMouse->GetDeviceData(
		sizeof(DIDEVICEOBJECTDATA),          
		inputBuffer,  
		&numberItems,            
		0);//use DIGDD_PEEK to leave buffered items in buffer
	
	//Unable to read data or no data available
	if (FAILED(hr))
	{
		return -1;
	}		
	if (numberItems == 0) 
	{
		return 0;
	}
	
	//Check buffer for left and right button presses
	for (DWORD item=0; item < numberItems; item++)
	{
		if ((inputBuffer[item].dwOfs == DIMOFS_BUTTON0) && 
			(inputBuffer[item].dwData & 0x80))
			g_MouseHit1 = g_MouseHit1+1;
		if ((inputBuffer[item].dwOfs == DIMOFS_BUTTON1) && 
			(inputBuffer[item].dwData & 0x80)) 
			g_MouseHit2 = g_MouseHit2+1;
	}
	
	
	return 1;
}



//-----------------------------------------------------------------------------
// Name: MoveMouse()
// Desc: Moves the mouse to the selected spot on the screen. 
//-----------------------------------------------------------------------------
void MoveMouse (int x, int y)
{
	g_MouseX = x;
	if (g_MouseX < 0) g_MouseX = 0;
	if (g_MouseX >= g_screenWidth) g_MouseX = g_screenWidth-1;
	
	g_MouseY = y;
	if (g_MouseY < 0) g_MouseY = 0;
	if (g_MouseY >= g_screenHeight) g_MouseY = g_screenHeight-1;
}




//-----------------------------------------------------------------------------
// Name: UpdateMouse
// Desc: Updates the mouse by using Direct Input. This function can be 
//	called directly. It is also called automatically by the Flip() function.
//-----------------------------------------------------------------------------
void UpdateMouse (void)
{
	assert(g_pMouse!=NULL);

	
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
	/**/
}


//-----------------------------------------------------------------------------
// Name: KeyDown()
// Desc: Returns whether a specific key is down. The key is the virtual
//	key code of the key. For A through Z, a through z, or 0 through 9,
//	use the ASCII value. For other keys, use the virtual key code.
//  - Example = FreeImage demo
//-----------------------------------------------------------------------------
bool KeyDown (Key key)
{
	if ((GetKeyState(key) & 0x8000) != 0)
		return true;
	else
		return false;
}


//-----------------------------------------------------------------------------
// Name: KeyHit()
// Desc: Returns whether a specific key has been pressed and released.
//-----------------------------------------------------------------------------
bool KeyHit (Key key)
{
	static int keyPressed;
	if ((GetKeyState(key) & 0x8000) != 0) //if key is down
	{
		keyPressed = key;
		return false;
	}
	else if (keyPressed == key) //if key is released after being pressed
	{
		keyPressed = 0;
		return true;
	}
	return false;
}



bool initDirectInput(HWND hWnd)
{
	
	
	assert(hWnd!=NULL);

	//Set up Direct Input
	HRESULT hr = DirectInputCreateEx(
		GetModuleHandle(NULL),//HINSTANCE hinst,                  
		DIRECTINPUT_VERSION,                  
		IID_IDirectInput7,
		//(void**)&g_pDirectInput,  
		(void**)&g_pDirectInput,  
		NULL);

	
	
	
	if (FAILED(hr)) {ReleaseDirectInput();return false;}
	
	//Set up a Direct Input-enabled mouse
	hr = g_pDirectInput->CreateDeviceEx(
		GUID_SysMouse,// 
		IID_IDirectInputDevice7,
        (void**)&g_pMouse,
		NULL);
	if (FAILED(hr)) {ReleaseDirectInput();return false;}
	
	hr = g_pMouse->SetDataFormat(&c_dfDIMouse);
	if (FAILED(hr)) {ReleaseDirectInput();return false;}
	hr = g_pMouse->SetCooperativeLevel(hWnd,
		DISCL_NONEXCLUSIVE | DISCL_FOREGROUND);
	if (FAILED(hr)) {ReleaseDirectInput();return false;}
	
	//Set up buffer for MouseHit()
	DIPROPDWORD dipdw; //device property header data structure
	dipdw.diph.dwSize       = sizeof(DIPROPDWORD);
	dipdw.diph.dwHeaderSize = sizeof(DIPROPHEADER);
	dipdw.diph.dwObj        = 0;
	dipdw.diph.dwHow        = DIPH_DEVICE;
	dipdw.dwData            = 10; //# of buffered data items
	hr = g_pMouse->SetProperty(DIPROP_BUFFERSIZE, &dipdw.diph);
	if (FAILED(hr))
	{
		if (hr == DI_PROPNOEFFECT) 
		{ReleaseDirectInput();return false;}
		else
		{ReleaseDirectInput();return false;}
	}
	
	
	
	//Acquire the mouse
	hr = g_pMouse->Acquire();
	if (FAILED(hr)) {ReleaseDirectInput();return false;}
	g_MouseX = g_screenWidth/2;
	g_MouseY = g_screenHeight/2;
	/**/

	return true;
}


//-----------------------------------------------------------------------------
// Name: ReleaseObjects
// Desc: Releases Direct Draw objects. Called by EndGraphics and
//	Graphics functions.
//-----------------------------------------------------------------------------
void ReleaseDirectInput(void)
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


}  // namespace CheckInput
