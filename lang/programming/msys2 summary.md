

# msys2

source: nodejs summary.md node-sdl

- https://github.com/kmamal/node-sdl

- https://github.com/fosterseth/sdl2_video_player  **视频播放**

  - [必看](https://gist.github.com/thales17/fb2e4cff60890a51d9dddd4c6e832ad2) [2](https://hustlei.github.io/2018/11/msys2-for-win.html) [3](https://www.v2ex.com/t/823471)

  - [vcpkg 可能是更好的选择](https://github.com/microsoft/vcpkg/issues/23873) [2](https://stackoverflow.com/questions/64079180/vs-auto-linking-against-sdl2-libraries-installed-with-vcpkg-on-windows)

  - [nuget 优先用这个]()

    ```
    打开 C:\msys64\msys2.exe
    	# 从开始菜单进去 MSYS2 MINGW64
    		才找得到 gcc !!!
    	C:\msys64\home\Administrator
    		# 代码放这里
    
    pacman -Rs mingw-w64-x86_64-ffmpeg
    pacman -Rs mingw-w64-x86_64-SDL2
    	# 删除
    	
    pacman -Syu
    	# update all
    
    pacman -S git mingw-w64-x86_64-toolchain mingw64/mingw-w64-x86_64-SDL2 mingw64/mingw-w64-x86_64-SDL2_mixer mingw64/mingw-w64-x86_64-SDL2_image mingw64/mingw-w64-x86_64-SDL2_ttf mingw64/mingw-w64-x86_64-SDL2_net mingw64/mingw-w64-x86_64-cmake make
    
    
    
    sdl2-config --cflags --libs
    --> -IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main
    -LC:/msys64/mingw64/lib -lmingw32 -mwindows -lSDL2main -lSDL2
    
    // sd.c
    #include <SDL.h>
    int main(int argc, char *argv[]) {
    	return 0;
    }
    
    gcc -IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main -LC:/msys64/mingw64/lib -lmingw32 -mwindows -lSDL2main -lSDL2 sd.c
    	# 成功编译
    
    ```

    

- https://github.com/raullalves/player-cpp-ffmpeg-sdl 比较新

- https://github.com/kingslay/KSPlayer swiftui

  

msys2 packages:

- mingw-w64-x86_64-ffmpeg 3.3-1
- mingw-w64-x86_64-SDL2 2.0.5-1

```
https://www.msys2.org/
	# install and open it

pacman -S mingw-w64-x86_64-ffmpeg
	# C:\msys64\mingw64\include\libavutil
pacman -S mingw-w64-x86_64-SDL2
	# C:\msys64\mingw64\include\SDL2

gcc -IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main
-LC:/msys64/mingw64/lib -lmingw32 -mwindows -lSDL2main -lSDL2 sd.c


#include <SDL.h>
int main(int argc, char *argv[]) {
	return 0;
}

git clone https://github.com/fosterseth/sdl2_video_player.git


#include <libavcodec/avcodec.h>
	# 需要加一句

https://blog.csdn.net/jacke121/article/details/79312064
	# codec参数在58版本及之后就不会支持了，需要由codecpar参数所替代
	
	
        /* find decoder for the stream */
        //dec_ctx = st->codec;
        //dec = avcodec_find_decoder(dec_ctx->codec_id);
        //if (!dec) {
        //    fprintf(stderr, "Failed to find %s codec\n",
        //            av_get_media_type_string(type));
        //    return AVERROR(EINVAL);
        //}
			# 注释上面，添加下面

        //找到视频解码器，比如H264
        AVCodec* dec = avcodec_find_decoder(st->codecpar->codec_id);
        //独立的解码上下文
        AVCodecContext* dec_ctx = avcodec_alloc_context3(dec);
        avcodec_parameters_to_context(dec_ctx, st->codecpar);	
	

打开ps命令行
gcc -o ccc -IC:\msys64\mingw64\include -LC:\msys64\mingw64\bin -LE:\t\sdl_vide\sdl2_video_player\bin -lSDL2 -lavcodec-57 vidserv.c 

gcc -o ccc -IC:\msys64\mingw64\include -Dmain=SDL_main sd.c

gcc -o ccc -IC:\msys64\mingw64\include  -municode sd.c

x86_64-w64-mingw32-g++


-IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main


int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, PWSTR pCmdLine, int nCmdShow)

```



1. Install MSYS2 from [https://www.msys2.org 2](https://www.msys2.org/)
2. Open “MSYS2 MinGW 64-bit” terminal then install needed software and libraries:
   `pacman -Syu` to update repositories and upgrade outdated packages
   `pacman -S --needed mingw-w64-x86_64-toolchain mingw-w64-x86_64-SDL2 mingw-w64-x86_64-SDL2_image mingw-w64-x86_64-SDL2_mixer mingw-w64-x86_64-SDL2_ttf mingw-w64-x86_64-cmake`
   You can install other needed packages, if you need.
3. Add “MSYS2 MinGW 64-bit” terminal to your VSCode by editing `settings.json`:
   Open command palette by `CTRL + SHIFT + P`
   Choose “Open user settings (JSON)”
   Add a new subobject to `terminal.integrated.profiles.windows` object:

```swift
"MSYS2 MinGW 64-bit": {
	"path": "C:\\msys64\\msys2_shell.cmd",
	"args": [
		"-defterm",
		"-here",
		"-no-start",
		"-mingw64"
	]
}
```

Adjust paths if needed.
Your config will look like this:

```swift
{
	// many other options
	"terminal.integrated.profiles.windows": {
		"MSYS2 MinGW 64-bit": {
			"path": "C:\\msys64\\msys2_shell.cmd",
			"args": [
				"-defterm",
				"-here",
				"-no-start",
				"-mingw64"
			]
		},
		// many other terminals
	}
}
```

1. Install and Microsoft C++ extension via extension marketplace, and you may need to install “CMake” and “CMake Tools” extensions, if you want to use CMake.
   Optional: You can also use clangd as code model, you need to install clangd extension and package ( `mingw-w64-clang-x86_64-clang-tools-extra`) then provide path to clangd executable in VSCode:
   `C:\msys64\mingw64\bin\clangd.exe`
2. In VSCode settings find “Cmake: Cmake Path” setting and enter path to your MinGW CMake:
   `C:\msys64\mingw64\bin\cmake.exe`
3. Create/open your CMake project and start exploring it by yourself.

Maybe I missed something, so feel free to ask about it.

You also can just use Makefiles but it’s not simple for beginner, and you will face some code model issues in VSCode.