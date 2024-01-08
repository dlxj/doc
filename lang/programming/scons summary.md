



see nodejs summary.js -> videoStreamPlayer -> GoZen-ffmpeg



```
git clone https://github.com/VoylinsGamedevJourney/GoZen.git && \
cd GoZen && \
git clone https://github.com/VoylinsGamedevJourney/GoZen-ffmpeg.git && \
cd GoZen-ffmpeg && \
git reset --hard b0eb64e && \
git clone https://github.com/godotengine/godot-cpp.git && \
cd godot-cpp && \
git reset --hard f3143c7

复制 elly_videoplayer\src\ffmpeg 到 GoZen\gozen-ffmpeg\ffmpeg
修改 gozen-ffmpeg/SConstruct 
	env.Append(CPPPATH=["src/", "ffmpeg/include/"])
	env.Append(LIBPATH=["ffmpeg/lib/"])
		# 可能只有 linux 能编译成功

cd GoZe/GoZen-ffmpeg && \
scons -Q -j2 destination=../src/editor/bin target=template_release platform=windows

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



