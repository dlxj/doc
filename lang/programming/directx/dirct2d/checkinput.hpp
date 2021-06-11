
#include <Windows.h>
#include <WinUser.h>

namespace CheckInput {

	enum Key { Enter = 13, ESC = 27, G = 71, Number1 = 49, Space = VK_SPACE };

	//-----------------------------------------------------------------------------
	// Name: KeyDown()
	// Desc: Returns whether a specific key is down. The key is the virtual
	//	key code of the key. For A through Z, a through z, or 0 through 9,
	//	use the ASCII value. For other keys, use the virtual key code.
	//  - Example = FreeImage demo
	//-----------------------------------------------------------------------------
	bool KeyDown(Key key)
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
	bool KeyHit(Key key)
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

}




