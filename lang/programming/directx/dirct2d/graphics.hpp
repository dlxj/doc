
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#include <d2d1.h>

#include <wincodec.h>

#pragma comment(lib, "d2d1.lib")
#pragma comment(lib, "Windowscodecs.lib")

namespace Graphics {

    ID2D1DCRenderTarget* pow;
    ID2D1Factory* l;

    IWICImagingFactory* pIWICFactory = NULL;

    ID2D1Bitmap* pBitmap_grid_black = NULL;

    ID2D1Bitmap* pBitmap_start = NULL;
    ID2D1Bitmap* pBitmap_end = NULL;
    ID2D1Bitmap* pBitmap_wall = NULL;
    ID2D1Bitmap* pBitmap_path = NULL;
    

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

    HRESULT LoadBitmapFromFile(
        ID2D1RenderTarget* pRenderTarget,
        IWICImagingFactory* pIWICFactory,
        PCWSTR uri,
        UINT destinationWidth,
        UINT destinationHeight,
        ID2D1Bitmap** ppBitmap
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
                ppBitmap
                //&pBitmap
            );
        }

        SAFE_RELEASE(pDecoder);
        SAFE_RELEASE(pSource);
        SAFE_RELEASE(pStream);
        SAFE_RELEASE(pConverter);
        SAFE_RELEASE(pScaler);

        return TRUE;
    }


    void draw()
    {
        const int tileSize = AStar::tileSize;
        LoadBitmapFromFile(Graphics::pow, pIWICFactory, L"images/grid_black.bmp", tileSize, tileSize, &pBitmap_grid_black);
        LoadBitmapFromFile(Graphics::pow, pIWICFactory, L"images/start.bmp", tileSize, tileSize, &pBitmap_start);
        LoadBitmapFromFile(Graphics::pow, pIWICFactory, L"images/end.bmp", tileSize, tileSize, &pBitmap_end);
        LoadBitmapFromFile(Graphics::pow, pIWICFactory, L"images/wall.bmp", tileSize, tileSize, &pBitmap_wall);
        LoadBitmapFromFile(Graphics::pow, pIWICFactory, L"images/path_black.bmp", tileSize, tileSize, &pBitmap_path);

        Graphics::pow->BeginDraw();

        Graphics::pow->Clear(D2D1::ColorF(D2D1::ColorF::White));

        D2D1_SIZE_F size = pBitmap_grid_black->GetSize();
        D2D1_POINT_2F upperLeftCorner = D2D1::Point2F(0.f, 0.f);


        // ªÊ÷∆±≥æ∞µÿÕº
        for (int j = 0; j < AStar::mapHeight; j++) { // AStar::mapHeight
            for (int i = 0; i < AStar::mapWidth; i++) {
                FLOAT left = upperLeftCorner.x + i * size.width;
                FLOAT top = upperLeftCorner.y + j * size.width;
                Graphics::pow->DrawBitmap(
                    pBitmap_grid_black,
                    D2D1::RectF(
                        left,
                        top,
                        left + size.width,
                        top + size.height)
                );
            }
        }

        Graphics::pow->DrawBitmap(
            pBitmap_start,
            D2D1::RectF(
                AStar::startX * AStar::tileSize,
                AStar::startY * AStar::tileSize,
                AStar::startX * AStar::tileSize + size.width,
                AStar::startY * AStar::tileSize + size.height)
        );

        Graphics::pow->DrawBitmap(
            pBitmap_end,
            D2D1::RectF(
                AStar::targetX * AStar::tileSize,
                AStar::targetY * AStar::tileSize,
                AStar::targetX * AStar::tileSize + size.width,
                AStar::targetY * AStar::tileSize + size.height)
        );

        Graphics::pow->EndDraw();

    }

    void draw_result() {

        Graphics::pow->BeginDraw();

        for (int x = 0; x <= AStar::mapWidth - 1; x++)
        {
            for (int y = 0; y <= AStar::mapHeight - 1; y++)
            {

                //Draw paths
                if (AStar::whichList[x][y] == 3) {

                    Graphics::pow->DrawBitmap(
                        pBitmap_path,
                        D2D1::RectF(
                            x * AStar::tileSize,
                            y * AStar::tileSize,
                            x * AStar::tileSize + AStar::tileSize,
                            y * AStar::tileSize + AStar::tileSize)
                    );
                }
            }
        }

        Graphics::pow->EndDraw();
    }
}


