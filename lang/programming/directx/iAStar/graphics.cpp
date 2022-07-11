

#include "graphics.h"
#include <assert.h>


//extern int g_screenWidth;
//extern int g_screenHeight;


namespace Graphics {
	
	HWND hWnd = NULL;
	DWORD                       g_ClsColor=0;
	COLORREF                    g_FontColor=RGB(255,255,255);
	HBRUSH                      g_hBrush=NULL;
	HFONT                       g_hFont=NULL;
	HPEN                        g_hPen=NULL;
	int                         g_screenWidth = 0;
	int                         g_screenHeight = 0;
	int                         g_screenDepth = 0;
	short                       g_screenFormat16Bit = 0;
	bool                        g_AutoMidHandle=false;
	int                         g_Pitch=0;
	void*                       g_pSurface = NULL;
	LPDIRECTDRAW7               g_pDirectDraw = NULL;
	LPDIRECTDRAWSURFACE7        g_pFrontBuffer= NULL; 
	LPDIRECTDRAWSURFACE7        g_pBackBuffer = NULL;
	LPDIRECTDRAWPALETTE         g_pPalette = NULL;
	PALETTEENTRY                g_PaletteEntry[256];
	LPDIRECT3D7                 g_pD3D = NULL;
	LPDIRECT3DDEVICE7           g_pD3DDevice = NULL;
	D3DTLVERTEX                 g_Vertex[4]; //quad vertices for 3D images


	//Globals used to keep track of current drawing buffer
	char                        g_pCurrentBuffer = 2;//1=front, 2 = back, 3 = image
	cImage*                     g_pCurrentImage = NULL;//pointer to the cImage in buffer
	LPDIRECTDRAWSURFACE7        g_pCurrentSurface = NULL;//pointer to the surface in buffer


	
	
	//Globals used by cImage class	
	cImage*                     g_pFirstImage = NULL;//pointer to first item in linked list
	cImage*                     g_pLastImage = NULL;//pointer to last item in linked list
	
	/*
	cImage* mousePointer; 
	cImage* grid; cImage* greengrid; cImage* bluegrid; cImage* dottedPath;
	cImage* greenBlock=NULL; cImage* redBlock; cImage* wallBlock;
	cImage* parentArrow[9]; cImage* number[10];
	
	*/

	CSTR g_strString;

	CSTR& CSTR::operator-(char* nextString){
		strcpy (this->actualString,nextString); 
		return Graphics::g_strString;
	}
	
	CSTR& CSTR::operator-(int number){
		char temp [33];
		_itoa (number,temp,10); 
		strcpy (this->actualString,temp);
		return g_strString;}
	
	CSTR& CSTR::operator-(double number){
		char temp [20];
		_gcvt (number,10,temp);
		strcpy (this->actualString,temp);
		return g_strString;}
	
	CSTR& CSTR::operator+(char* nextString){
		strcat (this->actualString,nextString); 
		return g_strString;}
	
	CSTR& CSTR::operator+(int number){
		char temp [33];
		_itoa (number,temp,10); 
		strcat (this->actualString,temp); 
		return g_strString;}
	
	CSTR& CSTR::operator+(double number){
		char temp [20];
		_gcvt (number,10,temp);
		strcat (this->actualString,temp);
		return g_strString;}
}


//-----------------------------------------------------------------------------
// Name: Graphics 
// Desc: Creates an instance of Direct Draw.
//-----------------------------------------------------------------------------
int Graphics::InitGraphics (int screenWidth, int screenHeight, int screenDepth, 
			  HWND hWnd, const TCHAR* pPalleteFile)
{

	Graphics::hWnd = hWnd;
	//Record screen dimensions as globals.
	g_screenWidth = screenWidth;
	g_screenHeight = screenHeight;
	g_screenDepth = screenDepth;

	//Create the Direct Draw object. Use DirectDrawCreateEx to enable
	//3d stuff.
	HRESULT hr = DirectDrawCreateEx(
         NULL, //use the GUID of the active display
         (VOID**)&g_pDirectDraw,//address of variable representing Direct Draw object
         IID_IDirectDraw7,//Specify Direct Draw 7
         NULL); //Advanced COM stuff
	if (hr != DD_OK) return 2;




	//Set the cooperative level
	hr = g_pDirectDraw->SetCooperativeLevel(
         hWnd, //handle of program's window
         DDSCL_ALLOWREBOOT | DDSCL_EXCLUSIVE | DDSCL_FULLSCREEN);
	if (hr != DD_OK) {ReleaseObjects();return 3;}

	

	// Set the display mode
	hr = g_pDirectDraw->SetDisplayMode(
         g_screenWidth, g_screenHeight, //set screen width, height
         g_screenDepth,//set the screen bit depth (8,16,24,32)
         0, //screen refresh rate - set to 0 for hardware default rate
         0); //for rarely used standard VGA mode stuff
	if (hr != DD_OK) 
	{
		if (g_pDirectDraw != NULL)
		{
		g_pDirectDraw->Release();
		g_pDirectDraw = NULL;
		}
		return 4;
	}
	
	

	//Create the primary surface (frontbuffer)
	DDSURFACEDESC2              ddsd;
	ZeroMemory(&ddsd, sizeof(ddsd));
	ddsd.dwSize = sizeof(ddsd);
	ddsd.dwFlags = DDSD_CAPS | DDSD_BACKBUFFERCOUNT;
	ddsd.ddsCaps.dwCaps = DDSCAPS_PRIMARYSURFACE |
                          DDSCAPS_FLIP |
                          DDSCAPS_COMPLEX |
						  DDSCAPS_3DDEVICE;
	ddsd.dwBackBufferCount = 1;
	
	
	hr = g_pDirectDraw->CreateSurface(&ddsd, &g_pFrontBuffer, NULL);
	if (hr != DD_OK) {ReleaseObjects();return 5;}

	//Create the backbuffer
	DDSCAPS2                    ddscaps;
	ZeroMemory(&ddscaps, sizeof(ddscaps));
	ddscaps.dwCaps = DDSCAPS_BACKBUFFER;
	hr = g_pFrontBuffer->GetAttachedSurface(&ddscaps,&g_pBackBuffer);
	if (hr != DD_OK) {ReleaseObjects();return 6;}

	

	//Make the back buffer the current buffer.
	g_pCurrentBuffer = 2;
	g_pCurrentSurface = g_pBackBuffer;
	
	

	//If in 8 bit mode, set a palette
	if (g_screenDepth == 8)
	{
	LoadPalette(&g_pPalette,pPalleteFile);
	g_pFrontBuffer->SetPalette(g_pPalette);
	g_pBackBuffer->SetPalette(g_pPalette);
	}

	//If in 16 bit mode, save the screen format (555 or 565)
	if (g_screenDepth == 16)
	{
		DDSURFACEDESC2 ddsd2;
		ZeroMemory(&ddsd2, sizeof(ddsd2));
		ddsd2.dwSize = sizeof(ddsd2);
		hr = g_pFrontBuffer->GetSurfaceDesc(&ddsd2); 
		if (ddsd2.ddpfPixelFormat.dwGBitMask == 992) g_screenFormat16Bit = 555;//555 16 bit
		if (ddsd2.ddpfPixelFormat.dwGBitMask == 2016) g_screenFormat16Bit = 565;//565 16 bit
	}

	

	//Create the clipper object
	LPDIRECTDRAWCLIPPER	pcClipper; //Declare the clipper object
	hr = g_pDirectDraw->CreateClipper( //create the clipper object
	NULL, //unused flag
	&pcClipper, //address of variable pointing to clipper object
	NULL); //advanced COM stuff
	if (hr != DD_OK) {ReleaseObjects();return 8;}

	//Create the clip list, which is a list of RECTS (rectangles) we want to
	//clip to. At this point there is only one item on the list, the screen.
	LPRGNDATA lpClipList //declare pointer to RGNDATA structure containing list
		= (LPRGNDATA)malloc(sizeof(RGNDATAHEADER)//allocate memory (malloc) for
		+ sizeof(RECT)); //header; allocate memory for rect holding screen
	RECT rcBoundary = {0, 0,g_screenWidth,g_screenHeight};//boundaries of screen
	memcpy(lpClipList->Buffer, &rcBoundary, sizeof(RECT));// set clip list
	lpClipList->rdh.dwSize = sizeof(RGNDATAHEADER);   // size of header
	lpClipList->rdh.iType = RDH_RECTANGLES;    // type of clip regions
	lpClipList->rdh.nCount = 1;               // number of rects in clip list
	lpClipList->rdh.nRgnSize = sizeof(RECT); // size of Buffer
	lpClipList->rdh.rcBound = rcBoundary;// bounding RECT for all items on list

	//Set the clip list
	pcClipper->SetClipList(
	lpClipList, //address of a valid RGNDATA structure, created above
	0);//unused flag
	if (hr != DD_OK) 
	{free(lpClipList);ReleaseObjects();return 9;}

	//Attach the clipper to the backbuffer
	if( FAILED( hr = g_pBackBuffer->SetClipper( pcClipper ) ) )
	{
	pcClipper->Release();
	ReleaseObjects();
	return 10;
	}

	//Free the clipper and clip list.
	free(lpClipList);
	pcClipper->Release();

	//Hide the Windows cursor
	ShowCursor(FALSE);




	//If not in 8 bit/24 bit mode, activate 3D mode for special effect
	//(fast rotations, alpha blending, etc.).
	if (g_screenDepth != 8 && g_screenDepth != 24)
	{

	//Query DirectDraw for access to Direct3D
    hr = g_pDirectDraw->QueryInterface(IID_IDirect3D7,(VOID**)&g_pD3D);
    if(FAILED(hr)) {ReleaseObjects();return 17;};

	//Create the D3D device using hardware
	hr = g_pD3D->CreateDevice(
		IID_IDirect3DHALDevice, 
		g_pBackBuffer, 
		&g_pD3DDevice);//I'm getting a no palette attached error

	//If no hardware support, create the D3D device using sofware
    if(FAILED(hr))
    {
        hr = g_pD3D->CreateDevice( 
		IID_IDirect3DRGBDevice, 
		g_pBackBuffer,
		&g_pD3DDevice);
	    if(FAILED(hr)) {ReleaseObjects();return 18;}
    }

    //Create the viewport
    D3DVIEWPORT7 vp = {0,0, g_screenWidth, g_screenHeight, 0.0f, 1.0f };
    hr = g_pD3DDevice->SetViewport(&vp);
	if(FAILED(hr)) {ReleaseObjects();return 19;}
	}//if (g_screenDepth != 8)


	return 1;
}

//-----------------------------------------------------------------------------
// Name: ReleaseObjects
// Desc: Releases Direct Draw objects. Called by EndGraphics and
//	Graphics functions.
//-----------------------------------------------------------------------------
int Graphics::ReleaseObjects(void)
{
	int imageCount = 0;//variable recording the number of images
	//excluding the front and backbuffers, that were deleted
	//at exit.
	
	//Delete GDI objects
	if (g_hBrush != NULL) DeleteObject(g_hBrush);
	if (g_hFont != NULL) DeleteObject(g_hFont);
	if (g_hPen != NULL) DeleteObject(g_hPen);


	//Release Direct3D objects (release before Direct Draw objects)
	if (g_pD3D != NULL)
	{
		//Release Direct3D device
		if (g_pD3DDevice != NULL)
		{
			g_pD3DDevice->Release();//this command causes an error
			g_pD3DDevice = NULL;
		}
		
		g_pD3D->Release();
		g_pD3D = NULL;
	}

	
	
	//Release Direct Draw objects
	if (g_pDirectDraw != NULL)
	{
		
		//Release all image objects and release their video memory
		cImage* pImage = g_pFirstImage;
		while(pImage != NULL)
		{
			imageCount = imageCount + 1;//keep track of images deleted
			cImage* pTemp = pImage->nextImage;
			if (pImage->pSurface != NULL) pImage->pSurface->Release();//release VRAM
			delete pImage; //delete its container object
			pImage = pTemp;
		}
		
		//Release palette, if any (8 bit mode)
		if (g_pPalette != NULL)
		{
			g_pPalette->Release();
			g_pPalette = NULL;
		}
		
		//Release backbuffer
		if (g_pBackBuffer != NULL)
		{
			g_pBackBuffer->Release();
			g_pBackBuffer = NULL;
		}
		
		//Release primary surface
		if (g_pFrontBuffer!= NULL)
		{
			g_pFrontBuffer->Release();
			g_pFrontBuffer= NULL;
		}
		
		//Release Direct Draw object
		g_pDirectDraw->Release();
		g_pDirectDraw = NULL;
	}
	
	//DestroyWindow(g_hWndGame);
	//PostQuitMessage(0);	
	
	/**/
	return imageCount;
  
}


//-----------------------------------------------------------------------------
// Name: LoadPalette
// Desc: Loads a palette from a particular bitmap. This function is called
// from the Graphics function.
//-----------------------------------------------------------------------------
HRESULT Graphics::LoadPalette(
	LPDIRECTDRAWPALETTE* ppPalette,//global variable pointing to palette
	const TCHAR* strBMP )//string representing file location of bitmap
{
	HANDLE            hFile = NULL;//handle of the bitmap file being opened
	DWORD             iColor; //specific color entry in palette
	DWORD             dwColors;//total number of colors used in bitmap
	BITMAPFILEHEADER  bf;//structure that holds bitmap file info
	BITMAPINFOHEADER  bi;//structure that holds bitmap header info
	DWORD             dwBytesRead;//used by ReadFile (see below)

	if( g_pDirectDraw == NULL || strBMP == NULL || ppPalette == NULL )
        return E_INVALIDARG;

	*ppPalette = NULL;

	// Read the bitmap's file, header, and palette information.
	hFile = CreateFile( 
	strBMP, //string representing file location of bitmap
	GENERIC_READ, //declare desired file access rights as generic read-only
	0, //Prevent access to file until handle is closed (see below)
	NULL, //security attributes of file
	OPEN_EXISTING, //action to take on file
	0, //file attributes flags (encripted, read-only, hidden, etc.)
	NULL);//unused file template parameter
	if( NULL == hFile )
        return E_FAIL;

	// Read the BITMAPFILEHEADER, which contains info about the bitmap's
	// type (bitmap) and size.
	ReadFile( 
	hFile, //handle of file to be read
	&bf,   //address of structure that will receive the read info
	sizeof(bf), //number of bytes to read from the file
	&dwBytesRead, //pointer to the variable that receives the number of bytes read.
	NULL );//overlapped bytes stuff (unused)
	if( dwBytesRead != sizeof(bf) )
	{
        CloseHandle( hFile );
        return E_FAIL;
	}


	// Read the BITMAPINFOHEADER, a data structure that contains info
	// about the bitmap's size, width, height, color depth, compression, etc.
	ReadFile( hFile, &bi, sizeof(bi), &dwBytesRead, NULL );
	if( dwBytesRead != sizeof(bi) )
	{
        CloseHandle( hFile );
        return E_FAIL;
	}

	// Read the PALETTEENTRY, read pallete info from the bitmap and 
	// save it in the g_PaletteEntry PALETTEENTRY structure.
	ReadFile( hFile, g_PaletteEntry, sizeof(g_PaletteEntry), &dwBytesRead, NULL );
	if( dwBytesRead != sizeof(g_PaletteEntry) )
	{
        CloseHandle( hFile );
        return E_FAIL;
	}

	CloseHandle( hFile );

	//  Colors stored in a DIB (bitmap) palette are in BGR order.
	//  Colors used in a Direct Draw PALETTEENTRY structure are
	//  in RGB order, so flip them around. The PALETTEENTRY 
	//  structure also holds alpha information, but it's not used here.

	// Figure out how many colors there are by reading it from the 
	// bitmap header.
	if( bi.biSize != sizeof(BITMAPINFOHEADER) )
        dwColors = 0;
	else if (bi.biBitCount > 8) //if bit count of bitmap is > 8
        dwColors = 0;           //set palette colors used to 0
	else if (bi.biClrUsed == 0)
        dwColors = 1 << bi.biBitCount;
	else
        dwColors = bi.biClrUsed; //header info indicating # colors
                 //from header used in bitmap

	//For each color in the g_PaletteEntry PALETTEENTRY structure, swap the red 
	//and blue values so they are in the correct order.
	for( iColor = 0; iColor < dwColors; iColor++ )
	{
        BYTE r = g_PaletteEntry[iColor].peRed; //read red value
        g_PaletteEntry[iColor].peRed  = g_PaletteEntry[iColor].peBlue; //swap blue into red
        g_PaletteEntry[iColor].peBlue = r; //save blue into red position
	}

	//Create the pallete from the g_PaletteEntry PALETTEENTRY structure.	
	return g_pDirectDraw->CreatePalette(
	DDPCAPS_8BIT, //flag indicated its an 8 bit/256 color palette
	g_PaletteEntry, //address of array of PALETTEENTRY structures
	ppPalette, //pointer to palette. This is used by SetPalette()
	NULL ); //advanced COM stuff

}



//-----------------------------------------------------------------------------
// Name: LoadImage()
// Desc: Create a Direct Draw Surface from a bitmap resource.
//	- Example = DrawImage demo
//-----------------------------------------------------------------------------
Graphics::cImage* Graphics::LoadImage (LPCWSTR szBitmap, char loadTo)
{
	

	HRESULT                 hr; //variable to receive results from DD commands

	//Try to load the bitmap from disk
	HBITMAP                 hbm;  //handle of the loaded bitmap
	BITMAP                  bm;   //bitmap class

    //  这里调用的是 Windows的同名函数 LoadImage

	hbm = (HBITMAP) ::LoadImage( //type cast the handle
        NULL,  //hInstance of image
        szBitmap, //string indicating source of file
        IMAGE_BITMAP,//image type, as opposed to IMAGE_CURSOR or IMAGE_ICON
        0, //desired image width if resizing, 0 if using original width
        0, //desired image width if resizing, 0 if using original height
        LR_LOADFROMFILE | LR_CREATEDIBSECTION);
 
	//If that fails, exit
	if (hbm == NULL) return NULL;

	//Save the bitmap in a Windows GUI-compatible device context
	//Note that doing this may slightly change the exact RGB colors used in the
	//original bitmap if the bytes per pixel in the incoming bitmap are
	//higher than the color depth being used in the game. For example,
	//if the game is a 256 color, 8 bit game, and the loaded image is 24 
	//color, "selecting" the bitmap into the compatible DC will involve
	//mapping the 24 color image as well as possible to the 256 color
	//palette that is being used. Conversions the other way (8 bit to 24 bit)
	//should involve no color loss, however.
	HDC hdcImage = CreateCompatibleDC(NULL);//create device context for image
	SelectObject( //place the bitmap into the memory DC
	hdcImage,//device context of image created above
	hbm);//handle of the loaded bitmap

	//Set up the Direct Draw surface description
	DDSURFACEDESC2 ddsd; //surface description data structure
	ZeroMemory(&ddsd, sizeof(ddsd));// zero-out the memory area
	ddsd.dwSize = sizeof(ddsd);
	ddsd.dwFlags = DDSD_CAPS | //ddsCaps structure is valid (see below
                 DDSD_HEIGHT | //dwHeight member is valid
                 DDSD_WIDTH;   //dwWidth member is valid

	//Specify type of surface (plain offscreen) and location (VRAM/RAM)
	if (loadTo == 0) ddsd.ddsCaps.dwCaps = DDSCAPS_OFFSCREENPLAIN; 
	if (loadTo == 1) ddsd.ddsCaps.dwCaps = DDSCAPS_OFFSCREENPLAIN 
		| DDSCAPS_SYSTEMMEMORY; //load to RAM if loadTo == 1

	GetObject(hbm, sizeof(bm), &bm); // Get the size of the bitmap
	ddsd.dwWidth = bm.bmWidth;  //record image width (gotten from GetObject)
	ddsd.dwHeight = bm.bmHeight;  //record image height (gotten from GetObject)

	//Create the Direct Draw surface in specified memory area
	LPDIRECTDRAWSURFACE7 pSurface; //pointer to Direct Draw surface
	if (g_pDirectDraw->CreateSurface(
	&ddsd, //address of above DDSURFACEDESC2 structure that describes surface
	&pSurface, //address of the variable pointing to the surface
	NULL)  //advanced COM stuff
	!= DD_OK) return NULL;

	//If this fails, exit
	if (pSurface == NULL) return NULL;

	// Make sure the Direct Draw surface is restored.
	pSurface->Restore();

	//Get device context of Direct Draw surface
	HDC hdc;  //handle of display version of image
	if ((hr = pSurface->GetDC(&hdc)) == DD_OK)

	//Copy the bitmap to Direct Draw surface.
	{
	BitBlt(
		hdc,	// handle of VRAM destination DC
		0,		// x-coord of destination upper-left corner
		0,		// y-coord of destination upper-left corner
		ddsd.dwWidth,	// width of destination rectangle
		ddsd.dwHeight,	// height of destination rectangle
		hdcImage,	// handle of RAM source DC
		0, // width of source rectangle
		0, // height of source rectangle
		SRCCOPY );	// raster operation code
	}

	//Clean up by releasing stuff we don't need anymore
	if( FAILED( hr = pSurface->ReleaseDC(hdc))) return NULL;
	DeleteDC(hdcImage);//delete the GUI device context (DC)
	DeleteObject(hbm);//delete the bitmap object.

	//Create a new cImage class instance to hold image data 
	cImage* pImage = new cImage;
	pImage->pSurface = pSurface; //pointer to the image
	pImage->imageWidth = ddsd.dwWidth;
	pImage->imageHeight = ddsd.dwHeight;
	pImage->isMasked = false;
	pImage->memLocation = loadTo;
	pImage->imageIs3D = false;
	if (g_AutoMidHandle == false)
	{
	pImage->xHandle = 0;
	pImage->yHandle = 0;
	}
	if (g_AutoMidHandle == true)
	{
	pImage->xHandle = pImage->imageWidth/2;
	pImage->yHandle = pImage->imageHeight/2;
	}

	//Update linked list of images
	if (g_pFirstImage == NULL) g_pFirstImage = g_pLastImage = pImage;
	if (g_pFirstImage != pImage) 
	{
	g_pLastImage->nextImage = pImage;//link this item to end of list
	pImage->previousImage = g_pLastImage;//do a return link
	g_pLastImage = pImage;//make this item the last one on the list
	}

	return pImage;
}


//--------------------------------------------------------------------------
// Name: MaskImage
// Desc: Masks an image  
//- 16 bit bitmaps do not mask properly in 32 bit display modes
//- 24 bit bitmaps do not mask properly in 16 and 32 bit display modes
//- this has something to do with the ColorMatch algorithm
//- Example = DrawImage demo
//-----------------------------------------------------------------------------
int Graphics::MaskImage (cImage* pImage, int r, int g, int b)
{	
	//Get and translate the image pointer
	if(pImage == NULL) return E_INVALIDARG;
	if(pImage->pSurface == NULL) return E_INVALIDARG;
	
	COLORREF rgb = RGB(r,g,b);
	
	DDCOLORKEY ddck;
	ddck.dwColorSpaceLowValue = ColorMatch(pImage->pSurface, rgb);
	ddck.dwColorSpaceHighValue = ddck.dwColorSpaceLowValue;
	pImage->isMasked = true;
	pImage->convertedMaskColor = ddck.dwColorSpaceLowValue;
	return pImage->pSurface->SetColorKey(DDCKEY_SRCBLT, &ddck);
}

//-----------------------------------------------------------------------------
// Name: ColorMatch()
// Desc: This function translates a specified rgb color value into a format
//	appropriate to the color depth being used. For example, if 8 bit color
//	depth is used, it translates it into the appropriate palette entry. 
//	If 16 bit color depth is used, it translates the rgb into a 16 bit 
//	color, etc.
//	
//	Used by MaskImage and Cls
//-----------------------------------------------------------------------------
DWORD Graphics::ColorMatch(LPDIRECTDRAWSURFACE7 pdds, COLORREF rgb)
{
    COLORREF                rgbT;
    HDC                     hdc;
    DWORD                   dw = CLR_INVALID;
    DDSURFACEDESC2          ddsd;
    HRESULT                 hres;
	
    // Use GDI SetPixel to color match for us
    if (rgb != CLR_INVALID && pdds->GetDC(&hdc) == DD_OK)
    {
        rgbT = GetPixel(hdc, 0, 0);     // Save current pixel value
        SetPixel(hdc, 0, 0, rgb);       // Set our value
        pdds->ReleaseDC(hdc);
    }
	
    //Now lock the surface so we can read back the converted color
    ddsd.dwSize = sizeof(ddsd);
    while ((hres = pdds->Lock(NULL, &ddsd, 0, NULL)) == DDERR_WASSTILLDRAWING);
    if (hres == DD_OK)
    {
        dw = *(DWORD *) ddsd.lpSurface;// Get DWORD
        if (ddsd.ddpfPixelFormat.dwRGBBitCount < 32)
            dw &= (1 << ddsd.ddpfPixelFormat.dwRGBBitCount) - 1;// Mask it to bpp
        pdds->Unlock(NULL);
    }
	
    //Now put the color that was there back.
    if (rgb != CLR_INVALID && pdds->GetDC(&hdc) == DD_OK)
    {
        SetPixel(hdc, 0, 0, rgbT);
        pdds->ReleaseDC(hdc);
    }
    return dw;
}


//-----------------------------------------------------------------------------
// Name: SetFont()
// Desc: Designates a font typeface for use by text functions 
// Some typical typefaces are Arial, Courier New, Garamond, Times New Roman 
//	- Example = GUI Commands demo
//-----------------------------------------------------------------------------
int Graphics::SetFont (LPCWSTR typeface, int typesize, int bold, int italic,
			 int underline)
{
	
	int weight = 0;
	if (bold==0) weight = 200;
	if (bold==1) weight = 700;
	
	if (g_hFont != NULL) DeleteObject(g_hFont);
	g_hFont = NULL;
	g_hFont = CreateFont(
		typesize,//height of font
		0,//int average character width
		0,//int angle of escapement
		0,//int base-line orientation angle
		weight,//font weight 0-1000 
		italic,//DWORD italic attribute option
		underline,//DWORD underline attribute option
		0,//DWORD strikeout attribute option
		0,//DEFAULT_CHARSET,//DWORD character set identifier
		0,//OUT_DEFAULT_PRECIS,//DWORD output precision
		0,//CLIP_DEFAULT_PRECIS,//DWORD clipping precision
		0,//DWORD output quality
		0,//DWORD pitch and family
		typeface);//LPCTSTR typeface name
	
	HDC hdc = GetDC (hWnd);
	SelectObject(hdc,g_hFont);
	ReleaseDC (hWnd, hdc);

	return 1;
}




//-----------------------------------------------------------------------------
// Name: DrawImage
// Desc: This function blits a masked image on the screen.
//	Example = DrawImage demo
//-----------------------------------------------------------------------------
int Graphics::DrawImage (cImage* pImage, int x, int y)
{
	HRESULT                     hr;
	//Error check
	if(pImage == NULL) return E_INVALIDARG;
	if(pImage->pSurface == NULL) return E_INVALIDARG;
	
	x = x-pImage->xHandle;
	y = y-pImage->yHandle;
	//Compute destination rectangle
	RECT rectDest;
	rectDest.left=x;
	rectDest.right=x + pImage->imageWidth;
	rectDest.top=y;
	rectDest.bottom=y + pImage->imageHeight;
	
	//Blit to the backbuffer
	//If image is not masked, draw it as-is
	if (pImage->isMasked == false)
	{
		hr = g_pCurrentSurface->Blt(
			&rectDest, //Destination RECT
			pImage->pSurface,  //lpDDSrcSurface
			NULL, //Source RECT or NULL for entire surface
			DDBLT_WAIT, //DDBLT_WAIT = wait until blitter is free
			NULL ); //special effects
	}
	
	//If image is masked, draw it masked.
	else
	{
		hr = g_pCurrentSurface->Blt(
			&rectDest, //Destination RECT
			pImage->pSurface,  //lpDDSrcSurface
			NULL, //Source RECT or NULL for entire surface
			DDBLT_KEYSRC | DDBLT_WAIT, //DDBLT_KEYSRC = use source color key
			NULL ); //special effects
	}
	
	//Return result (should be DD_OK, which is 0, if drawn ok)
	return hr;
}



//-----------------------------------------------------------------------------
// Name: Flip
// Desc: This function flips stuff drawn on the back buffer to the front buffer
//	It also updates the mouse position.
//-----------------------------------------------------------------------------
int Graphics::Flip (void)
{
	HRESULT                     hr;
	while (TRUE)
	{
        hr = g_pFrontBuffer->Flip(NULL, 0);
        if (hr == DD_OK)
            break;
        if (hr == DDERR_SURFACELOST)
        {
            hr = g_pDirectDraw->RestoreAllSurfaces(); //Reload images
            if (hr != DD_OK) break; 
			//hr = g_pMouse->Acquire(); //reaquire mouse for Direct Input
			ShowCursor(FALSE);
			//g_MouseX = g_screenWidth/2;
			//g_MouseY = g_screenHeight/2;
        }
        if (hr != DDERR_WASSTILLDRAWING)
            break;
	}
    //UpdateMouse();
	return (1);
}


//-----------------------------------------------------------------------------
// Name: Cls
// Desc: Clears the screen with the designated CLS color, which is black
// unless changed by the ClsColor() command.
//-----------------------------------------------------------------------------
int Graphics::Cls (void)
{
	DDBLTFX ddbltfx;
	ZeroMemory( &ddbltfx, sizeof(ddbltfx));
	ddbltfx.dwSize      = sizeof(ddbltfx);
	ddbltfx.dwFillColor = g_ClsColor;
	
	// Blit the entire current buffer with the specified fill color
	HRESULT hr = g_pCurrentSurface->Blt(
		NULL, //destination rectangle of blit (0 = blit entire surface)
		NULL, //address of source surface blitted from (0 used here)
		NULL, //source rectangle of blit (0 = blit from entire surface)
		DDBLT_COLORFILL | DDBLT_WAIT, //blit flags; DDBLT_COLORFILL = use dwFillColor member
		// of the DDBLTFX structure as the RGB color that fills the destination
		&ddbltfx );//address of special effects ddbltfx structure created above
	
	if (hr == DD_OK)
		return 1;
	else
		return hr;
}


//-----------------------------------------------------------------------------
// Name: DrawBlock
// Desc: This function blits an unmasked version of an image on the screen
//	Example = DrawImage demo
//-----------------------------------------------------------------------------
int Graphics::DrawBlock (cImage* pImage, int x, int y)
{
	//Get incoming info
	if(pImage == NULL) return E_INVALIDARG;
	if(pImage->pSurface == NULL) return E_INVALIDARG;
	x = x-pImage->xHandle; //x position to draw image
	y = y-pImage->yHandle; //y position to draw image
	
	//Compute destination rectangle
	RECT rectDest;
	rectDest.left=x;
	rectDest.right=x + pImage->imageWidth;
	rectDest.top=y;
	rectDest.bottom=y + pImage->imageHeight;
	
	//Blit to the current buffer
	HRESULT hr = g_pCurrentSurface->Blt(
		&rectDest, //Destination RECT
		pImage->pSurface,  //lpDDSrcSurface
		NULL, //Source RECT or NULL for entire surface
		DDBLT_WAIT, //flags
		NULL ); //special effects
	
	//Return result (should be DD_OK, which is 0, if drawn ok)
	return hr;
}


