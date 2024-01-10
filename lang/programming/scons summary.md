



see nodejs summary.js -> videoStreamPlayer -> GoZen-ffmpeg



scons -c

​	# 清理



```
git clone https://github.com/VoylinsGamedevJourney/GoZen.git && \
cd GoZen && \
git clone https://github.com/VoylinsGamedevJourney/GoZen-ffmpeg.git && \
cd GoZen-ffmpeg && \
git reset --hard b0eb64e && \
git clone https://github.com/godotengine/godot-cpp.git && \
cd godot-cpp && \
git reset --hard f3143c7

cd GoZen\gozen-ffmpeg && \
curl --output ffmpeg.zip -L -O https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl-shared.tar.xz
	# 下载 ffmpeg


复制 elly_videoplayer\src\ffmpeg 到 GoZen\gozen-ffmpeg\ffmpeg
修改 gozen-ffmpeg/SConstruct 
	env.Append(CPPPATH=["src/", "ffmpeg/include/"])
	env.Append(LIBPATH=["ffmpeg/lib/"])
		# 可能只有 linux 能编译成功

cd GoZe/GoZen-ffmpeg && \
scons -Q -j2 destination=../src/editor/bin target=template_release platform=windows


https://download.visualstudio.microsoft.com/download/pr/1cac4d08-3025-4c00-972d-5c7ea446d1d7/a83bc5cbedf8b90495802ccfedaeb2e6/dotnet-sdk-6.0.417-linux-x64.tar.gz

mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-6.0.417-linux-x64.tar.gz  -C $HOME/dotnet
export DOTNET_ROOT=$HOME/dotnet && \
export PATH=$PATH:$HOME/dotnet


E:\t\GoZen\gozen-ffmpeg\src\ffmpeg_includes.hpp(4): fatal error C1083: 无法打开包括文件: “libavcodec/avcodec.h”: No such file or directory
	# 他只官方编译了 linux 版





gh repo clone VoylinsGamedevJourney/GoZen-ffmpeg -- --recurse-submodules

gh repo clone VoylinsGamedevJourney/GoZen -- --recurse-submodules


ssh-keyscan github.com >> ~/.ssh/known_hosts

git clone --recursive https://github.com/VoylinsGamedevJourney/GoZen-ffmpeg.git

git clone --recursive https://github.com/VoylinsGamedevJourney/GoZen.git && \
cd GoZen
scons -j 2 destination=../src/editor/bin target=template_release platform=windows
```



