
Termux + Github
 

ssh 传的是私钥
- ssh -i .ssh/id_rsa -T git@github.com

不用每次都输入密码
- git config --global credential.helper store

Update
> git add  
git commit -m 'a'  
git push origin master  

useradd gg  
visudo  
**chmod -R 777  /home**  




## termux
apt update && apt upgrade -y  
apt search texlive  
apt install texlive  
用tlmgr  更新包  
tlmgr search  
tlmgr install  
tlmgr update --self --all  更新整个 TeX Live 系统  

pkg uninstall [package name]  卸载  


使用lualatex  
https://liam.page/2014/12/11/ptex-intro-and-tutorial-03/  

https://www.ctan.org  搜luatexja 

LuaTeX中振假名与中日文混排的实现  
Yang Hong  
学物理哒~  
https://zhuanlan.zhihu.com/p/24881553  


普通排版  
```
\documentclass{article}
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```
platex -kanji utf8 hello-ptex.tex  
dvipdfmx hello-ptex.dvi  

```
\documentclass{article}
\usepackage{CJKutf8}
\usepackage{CJKspace}
\begin{document}
\begin{CJK*}{UTF8}{min}
\LaTeX{} で日本語を書きましょう！
\end{CJK*}
\end{document}
```



luatexja 排版  
```
\documentclass{article}
\usepackage{luatexja}
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```

lualatex -kanji utf8 hello-luatexja.tex  


$ sudo apt install texlive-lang-japanese  



NLP
- Google Colab 在线python 编辑器，免费GPU  
- notion 云笔记  
- 纯纯写作 永不丢失的笔记
- typora+坚果云 = 个人云笔记   
- 坚果云 + hexo = GitHub 博客  
- markor 安卓的markdownd 阅读器  
- Jsho 自动分割日语句子查单词  
- 日语动词词典 查动词的各种活用
- Bochs Limboemu APQ QEMU 安卓上安装Linux虚拟机
- virmach 便宜的vps  
- Termux 安卓上的linux 环境，有git
- linux deploy 安卓手机刷原生Linux  
- AndroCat 安卓坚果云客户端  
- Aurora Store 应用商店xda 出品  
- Hacker's Keyboard 黑客键盘PC 全键位 
-  vol.moe 漫画   
- 深度学习500问  


https://utaten.com  日语歌词检索  
http://www.hiragana.jp  网站日文假名标注  
https://m.jcinfo.net  日文句子假名标注 

https://chaoli.club  超理论坛  
https://www.codecogs.com  生线生成latex 公式    
https://nyaa.si   
https://e-hentai.org 漫画  
https://music.ghpym.com 音乐、歌词下载  
https://github.com/scutan90/DeepLearning-500-questions  

ainiyorin@gmail.com  

niconico

fc-list :lang=zh  


git clone https://aur.archlinux.org/aurutils.git   
cd aurtuils  
makepkg -si  

aur sync texlive-core  

texlive-langjapanese texlive-core texlive-localmanager-git



aur search texlive-localmanager  
pacman -Qmq  也可以这样搜  
aursync -c google-chrome  同步aur  
pacman -S google-chrome  可以用pacman 安装了       



Server = file:///var/cache/pacman/customon my /etc/pacman.d/custom/pacman.conf

% pkgfile pacconf community/pacutils



/etc/pacman.conf  



yay -Syu --devel --combinedupgrade --save  

.config/yay/config.json  

https://aur.tuna.tsinghua.edu.cn  

https://mirrors.tuna.tsinghua.edu.cn/help/archlinuxcn/ 



中科大源的archlinuxcn源 然后导入key 然后就可以直接装了 安装软件前要先sudo pacman -Syy


うなずうなず
