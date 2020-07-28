**Mac**  

- **proxifier 全局代理**  
- izotope rx 7  **音频P S**   
- riffstation **爬谱**   
- 如何优雅地一键实现 macOS 网络代理切换  
- sudo spctl --master-disable  允许从任何来源  
- **feem 离线热点文件传输** feem.io  

**对付MacOS catalina 只读文件保护**  

- **tidcal haskell 音乐编程**    
- **安装ghc 8.6.5  cabal 2.4.1  tidcalcycles** 
- csrutil status  
- **sudo mount -uw /**  

>重启按 cmd+R  
>**csrutil disable**  
>**vi ~/.bashrc**  
>**export PATH=/Users/vvw/.cabal/bin:$PATH**  
>**source ~/.bashrc**   
>./configure --prefix=/usr  
>make install  
>link xxx /usr/bin  

**bashrc 下次就不生效了**  

> vi ~/**.bash_profile**    
> PATH="${HOME}/usr/bin:${PATH}"  
> export PATH  
> **~/.bash_profile  每次开shell 都执行**  

**Mac 内录**  

> ShowU Audio Capture   
>  Soundflower：https://github.com/mattingalls/Soundflower/releases  
> https://www.jianshu.com/p/db035dad616a  

**Mac 软件打不开**    
sudo spctl --master-disable  
sudo codesign --force --deep --sign - /Applications/CleanMyMac\ X.app 