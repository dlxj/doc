
#include <ddraw.h> //Direct Draw header
#define D3D_OVERLOADS
#include <d3d.h>


#ifndef GRAPHICS_H
#define GRAPHICS_H


#pragma comment(lib,"ddraw.lib") 
#pragma comment(lib,"dxguid.lib") 

namespace Graphics {
	
	#define combine g_strString-
	
	
	class cImage;
	class CSTR;

	int InitGraphics (int screenWidth, int screenHeight, int screenDepth, 
				  HWND hWnd, char* pPalleteFile = NULL);
	int ReleaseObjects(void);

	HRESULT LoadPalette(
		LPDIRECTDRAWPALETTE* ppPalette,
		const TCHAR* strBMP );

	//void LoadGraphics (void);

	int SetFont (char* typeface, int typesize, int bold=0, int italic=0, 
			 int underline=0);

	cImage* LoadImage (char* szBitmap, char loadTo=0);
	int MaskImage (cImage* pImage, int r, int g, int b);
	DWORD ColorMatch(LPDIRECTDRAWSURFACE7 pdds, COLORREF rgb);

	void RenderScreen (bool stepByStep);
	int Cls (void);
	int DrawBlock (cImage* pImage, int x, int y);
	int DrawImage (cImage* pImage, int x, int y);
	int Flip (void);


	//-----------------------------------------------------------------------------
	// Name: Class Declarations
	//-----------------------------------------------------------------------------
	class cImage //class containing info about an image
	{
	public:
		LPDIRECTDRAWSURFACE7 pSurface; //pointer to the image
		int imageWidth;
		int imageHeight;
		int xHandle;
		int yHandle;
		bool isMasked; //0 = no, 1 = yes
		int convertedMaskColor;//mask color converted to used pixel format
		byte memLocation; //0 = VRAM, 1 = RAM
		bool imageIs3D; //0 = false, 1 = true
		
		cImage* previousImage;//pointer to previous item in linked list
		cImage* nextImage;//pointer to next item in linked list
		
		//constructor member function
		cImage()
		{
			previousImage = NULL;
			nextImage = NULL;
		}
	};

	class CSTR 
	{
	public:
		char actualString[255];
		CSTR& operator-(char* nextString);
		CSTR& operator-(int number);
		CSTR& operator-(double number);
		CSTR& operator+(char* nextString);
		CSTR& operator+(int number);
		CSTR& operator+(double number);
	};

	extern CSTR g_strString;

}



#endif  // GRAPHICS_H



