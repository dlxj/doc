#include <stdlib.h>

namespace AStar
{
	const mapWidth = 25, mapHeight = 16, tileSize = 50, numberPeople = 1;
	//const mapWidth = 32, mapHeight = 24, tileSize = 50, numberPeople = 1;
	
	const notfinished = 0, notStarted = 0;// path-related constants
	const found = 1, nonexistent = 2; 
	const walkable = 0, unwalkable = 1;// walkability array constants
	extern int whichList[mapWidth+1][mapHeight+1];
	extern char walkability [mapWidth][mapHeight];
	
	void ReadPath(int pathfinderID);
	int FindPath (int pathfinderID,int startingX, int startingY,
			  int targetX, int targetY, bool stepByStep = false);

	typedef struct 
	{
		int x;
		int y;
	} step;

	typedef struct
	{
		step* steps;
		int lenght;
	}Paths;

	 extern Paths paths;
}



