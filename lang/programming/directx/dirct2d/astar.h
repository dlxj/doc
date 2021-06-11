//#include <stdlib.h>

namespace AStar
{
	const int mapWidth = 30, mapHeight = 20, tileSize = 50;

	int pathfinderID = 1;
	int startX = 3, startY = 10; //Set seeker location
	int targetX = 25, targetY = 10;//Set initial target location. This can
								  //be changed by right-clicking on the map.

	int drawing = 0, erasing = 0;
}
