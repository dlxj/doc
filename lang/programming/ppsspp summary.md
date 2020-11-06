

```
git clone --recursive https://github.com/hrydgard/ppsspp.git
```





```
Ah, that means you didn't clone with --recursive. You can go into the /home/jose/alex/ppsspp-master folder and use git submodule update.

Basically, we use libraries and code that other people have written. If you clone our repo or download the zip from GitHub, that ONLY contains ppsspp's code. It doesn't contain ffmpeg, armips, glslang, etc.

Also make sure you've run:

sudo apt-get install build-essential

This should give you pthreads.
```





#### Building for macOS

You need to have the Command Line Tools installed (XCode is not needed):

```
xcode-select --install
```

Use [Homebrew](https://brew.sh/) to install the required dependencies:

```
brew upgrade
brew install sdl2 cmake libzip qt5 snappy
```

Then build using:

```
./b.sh --qtbrew
```



==> **Installing** **FFmpeg**

🍺 /usr/local/Cellar/FFmpeg/4.3.1_2: 273 files, 54.1MB



brew install GLEW

==> **Pouring glew-2.2.0.catalina.bottle.tar.gz**

🍺 /usr/local/Cellar/glew/2.2.0: 38 files, 3.4MB



==> **Summary**

/usr/local/Cellar/qt/5.15.1: 10,691 files, 370.4MB



qt is keg-only, which means it was not symlinked into /usr/local,

because Qt 5 has CMake issues when linked.



If you need to have qt first in your PATH run:

 echo 'export PATH="/usr/local/opt/qt/bin:$PATH"' >> ~/.profile



For compilers to find qt you may need to set:

 export LDFLAGS="-L/usr/local/opt/qt/lib"

 export CPPFLAGS="-I/usr/local/opt/qt/include"



For pkg-config to find qt you may need to set:

 export PKG_CONFIG_PATH="/usr/local/opt/qt/lib/pkgconfig"

