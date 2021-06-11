
// https://stackoverflow.com/questions/60121151/why-is-direct2d-not-drawing-to-the-screen

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

#define SAFE_RELEASE(P) if(P){P->Release() ; P = NULL ;}


#include "astar.hpp"
#include "graphics.hpp"
#include "checkinput.hpp"

LRESULT CALLBACK WndProcFunc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    RECT rc;
    switch (message)
    {

    case WM_KEYDOWN: {

        if (wParam == CheckInput::Enter) {
            int result = AStar::do_find_path();
        }
    }
    break;
    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        GetClientRect(hwnd, &rc);
        Graphics::pow->BindDC(ps.hdc, &rc);
        Graphics::draw();
        Graphics::draw_result();

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
    //int foundQ = AStar::do_find_path();
    //Graphics::draw_result();

    WNDCLASS wc{};
    wc.style = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WndProcFunc;
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = L"Class_Name";
    wc.hCursor = LoadCursor(nullptr, IDC_ARROW);
    RegisterClass(&wc);
    
    int windowWidth = AStar::mapWidth* AStar::tileSize;
    int windowHeight = AStar::mapHeight * AStar::tileSize;
    
    HWND hWnd = CreateWindow(L"Class_Name", L"Test", WS_OVERLAPPEDWINDOW, 100, 100, windowWidth+16, windowHeight+38, NULL, NULL, GetModuleHandle(NULL), NULL);
    Graphics::initize();

    ShowWindow(hWnd, 1);
    UpdateWindow(hWnd);


    //while (!CheckInput::KeyDown(CheckInput::ESC)) {

    //}

    MSG Msg;
    while (GetMessage(&Msg, NULL, 0, 0))
    {
        TranslateMessage(&Msg);
        DispatchMessage(&Msg);
    }

    return 0;
}

