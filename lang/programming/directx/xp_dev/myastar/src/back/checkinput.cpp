

#include "checkinput_impl.h"


extern int g_screenWidth;
extern int g_screenHeight;


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

