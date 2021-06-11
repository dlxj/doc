#include <windows.h>
#include "astarlibrary.h"


//Set pathfinderID and starting locations
int pathfinderID = 1;
int startX = 3, startY = 6; //Set seeker location
int targetX = 12, targetY = 6;//Set initial target location. This can
							  //be changed by right-clicking on the map.


int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
				   LPSTR lpCmdLine, int nCmdShow)
{

	using namespace AStar;

	int path=0;

	path= FindPath(pathfinderID,startX*50,startY*50,targetX*50,targetY*50);	
	if (path == found) ReadPath(pathfinderID);	


	/*
	for (int x = 0; x <= 15; x++) //draw each of 16 tiles across the screen
	{
		for (int y = 0; y <= 11; y++) //draw each of 12 tiles down the screen
		{
			//if (whichList[x][y] == 3) DrawImage (dottedPath,x*50,y*50);
		}
	}
	
	*/


	if (path == found)
	{
		MessageBox(NULL, "path has found", "congras", MB_OK);
	}
	else
		MessageBox(NULL, "path has  no found", "Ooops", MB_OK);

	return 0;
}

