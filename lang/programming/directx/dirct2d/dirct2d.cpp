
// https://stackoverflow.com/questions/60121151/why-is-direct2d-not-drawing-to-the-screen

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#include <d2d1.h>

#include <wincodec.h>

#pragma comment(lib, "d2d1.lib")
#pragma comment(lib, "Windowscodecs.lib")

#define SAFE_RELEASE(P) if(P){P->Release() ; P = NULL ;}

extern "C" ID2D1Bitmap * mybitmapcreate(ID2D1DCRenderTarget*);
float left = 5;
float top = 10;
float Bottom = 10;
float Right = 30;
ID2D1Bitmap* pBitmap = NULL;
IWICImagingFactory* pIWICFactory = NULL;

void initize();
void draw();
D2D1_RECT_F myrect = D2D1::RectF(left, top, Bottom, Right);
ID2D1DCRenderTarget* pow;
ID2D1Bitmap* mybitmap;
ID2D1Factory* l;
REFIID x = __uuidof(ID2D1Factory);

HRESULT LoadBitmapFromFile(
    ID2D1RenderTarget* pRenderTarget,
    IWICImagingFactory* pIWICFactory,
    PCWSTR uri,
    UINT destinationWidth,
    UINT destinationHeight
)
{
    HRESULT hr = S_OK;

    IWICBitmapDecoder* pDecoder = NULL;
    IWICBitmapFrameDecode* pSource = NULL;
    IWICStream* pStream = NULL;
    IWICFormatConverter* pConverter = NULL;
    IWICBitmapScaler* pScaler = NULL;


    hr = pIWICFactory->CreateDecoderFromFilename(
        uri,
        NULL,
        GENERIC_READ,
        WICDecodeMetadataCacheOnLoad,
        &pDecoder
    );
    if (SUCCEEDED(hr))
    {

        // Create the initial frame.
        hr = pDecoder->GetFrame(0, &pSource);
    }
    if (SUCCEEDED(hr))
    {
        hr = pIWICFactory->CreateFormatConverter(&pConverter);
    }
    // If a new width or height was specified, create an
// IWICBitmapScaler and use it to resize the image.
    if (destinationWidth != 0 || destinationHeight != 0)
    {
        UINT originalWidth, originalHeight;
        hr = pSource->GetSize(&originalWidth, &originalHeight);
        if (SUCCEEDED(hr))
        {
            if (destinationWidth == 0)
            {
                FLOAT scalar = static_cast<FLOAT>(destinationHeight) / static_cast<FLOAT>(originalHeight);
                destinationWidth = static_cast<UINT>(scalar * static_cast<FLOAT>(originalWidth));
            }
            else if (destinationHeight == 0)
            {
                FLOAT scalar = static_cast<FLOAT>(destinationWidth) / static_cast<FLOAT>(originalWidth);
                destinationHeight = static_cast<UINT>(scalar * static_cast<FLOAT>(originalHeight));
            }

            hr = pIWICFactory->CreateBitmapScaler(&pScaler);
            if (SUCCEEDED(hr))
            {
                hr = pScaler->Initialize(
                    pSource,
                    destinationWidth,
                    destinationHeight,
                    WICBitmapInterpolationModeCubic
                );
            }
            if (SUCCEEDED(hr))
            {
                hr = pConverter->Initialize(
                    pScaler,
                    GUID_WICPixelFormat32bppPBGRA,
                    WICBitmapDitherTypeNone,
                    NULL,
                    0.f,
                    WICBitmapPaletteTypeMedianCut
                );
            }
        }
    }
    if (SUCCEEDED(hr))
    {
        // Create a Direct2D bitmap from the WIC bitmap.
        hr = pRenderTarget->CreateBitmapFromWicBitmap(
            pConverter,
            NULL,
            &pBitmap
        );
    }

    SAFE_RELEASE(pDecoder);
    SAFE_RELEASE(pSource);
    SAFE_RELEASE(pStream);
    SAFE_RELEASE(pConverter);
    SAFE_RELEASE(pScaler);

    return TRUE;
}

LRESULT CALLBACK WndProcFunc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    RECT rc;
    switch (message)
    {
    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        GetClientRect(hwnd, &rc);
        pow->BindDC(ps.hdc, &rc);
        draw();
        EndPaint(hwnd, &ps);
    }
    break;
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }
    return DefWindowProc(hwnd, message, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance,    //Main windows function
    HINSTANCE hPrevInstance,
    LPSTR lpCmdLine,
    int nShowCmd)
{
    WNDCLASS wc{};
    wc.style = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WndProcFunc;
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = L"Class_Name";
    wc.hCursor = LoadCursor(nullptr, IDC_ARROW);
    RegisterClass(&wc);

    HWND hWnd = CreateWindow(L"Class_Name", L"Test", WS_OVERLAPPEDWINDOW, 100, 100, 1000, 500, NULL, NULL, GetModuleHandle(NULL), NULL);
    initize();

    ShowWindow(hWnd, 1);
    UpdateWindow(hWnd);

    MSG Msg;
    while (GetMessage(&Msg, NULL, 0, 0))
    {
        TranslateMessage(&Msg);
        DispatchMessage(&Msg);
    }

    return 0;
}

void initize()
{
    HRESULT h = CoInitializeEx(NULL, COINIT_MULTITHREADED);
    h = CoCreateInstance(CLSID_WICImagingFactory, NULL, CLSCTX_INPROC_SERVER, IID_IWICImagingFactory, reinterpret_cast<void**>(&pIWICFactory));

    // Create a Direct2D render target.
    D2D1_RENDER_TARGET_PROPERTIES props = D2D1::RenderTargetProperties(
        D2D1_RENDER_TARGET_TYPE_DEFAULT,
        D2D1::PixelFormat(
            DXGI_FORMAT_B8G8R8A8_UNORM,
            D2D1_ALPHA_MODE_IGNORE),
        0,
        0,
        D2D1_RENDER_TARGET_USAGE_NONE,
        D2D1_FEATURE_LEVEL_DEFAULT
    );

    HRESULT hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &l);
    l->CreateDCRenderTarget(&props, &pow);

}

void draw()
{

    LoadBitmapFromFile(pow, pIWICFactory, L"braynzar.bmp", 256, 256);


    pow->BeginDraw();

    pow->Clear(D2D1::ColorF(D2D1::ColorF::White));

    D2D1_SIZE_F size = pBitmap->GetSize();
    D2D1_POINT_2F upperLeftCorner = D2D1::Point2F(0.f, 0.f);

    // Draw bitmap
    pow->DrawBitmap(
        pBitmap,
        D2D1::RectF(
            upperLeftCorner.x,
            upperLeftCorner.y,
            upperLeftCorner.x + size.width,
            upperLeftCorner.y + size.height)
    );
    pow->EndDraw();

}