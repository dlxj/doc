

# git-lfs

[免费用户上传超过1G账号会被冻结](https://zhuanlan.zhihu.com/p/630784945)

[查看已用空间](https://github.com/settings/billingusage)

1. [git-lfs windows installter](https://github.com/git-lfs/git-lfs/releases) 下载安装
2. 运行  git lfs install​

### 使用

1. 执行 `git lfs install` 开启lfs功能
2. 使用 `git lfs track` 命令进行大文件追踪 例如`git lfs track "*.png"` 追踪所有后缀为png的文件
3. 使用 `git lfs track` 查看现有的文件追踪模式
4. 提交代码需要将`gitattributes`文件提交至仓库. 它保存了文件的追踪记录
5. 提交后运行`git lfs ls-files` 可以显示当前跟踪的文件列表
6. 将代码 push 到远程仓库后，LFS 跟踪的文件会以『Git LFS』的形式显示:
7. clone 时 使用'git clone' 或 `git lfs clone`均可



解决github 错误

> git config --global url."https://".insteadOf git://



13.229.188.59  github.com  
185.199.111.153  assets-cdn.github.com  
31.13.82.23  github.global.ssl.fastly.net  

>  ip138.com 查询    

 

Termux + Github

git config --global user.name "dlxj"    

git config --global user.email  "12345@qq.com"  

git config --global push.default matching  

ssh-keygen -t rsa -C "12345@qq.com"  



-f output_keyfile  



config 配置有system级别 global（用户级别） 和local（当前仓库）三个 设置先从system-》global-》local  底层配置会覆盖顶层配置 分别使用--system/global/local 可以定位到配置文件

查看系统config

git config --system --list
　　

查看当前用户（global）配置

1it config --global  --list


查看当前仓库配置信息
git config --local  --list

git config --local   user.name "g"
git config --local   user.email  "1@qq.com"



```
人多应该在主干上禁止 merge, 有个专门的策略叫线性历史(Linear History)

你可以在 Github 上看到这个选项, 可以禁止不小心 merge 到主干.


线性历史并不禁止 merge, 只是禁止 merge 到主干.

线性历史有两个主要分支, 一个叫 main, 一个叫 dev

所有其他的分支都从 main 分裂出去, 然后合并(merge/rebase/squash)到 dev

然后 dev 有专门的人 rebase 去掉所有的 merge 节点

(你实在不懂 rebase 那你直接 squash)

当 dev 稳定后, 打一个 tag

然后 main 分支执行 fast-forward 抵达这一稳定节点.

线性历史解决了 merge 盘丝洞的问题, log 清晰, 容易 revert

你说有个feature 需要长期游离在 main 和 dev 之外?

那这种情况你应该用 fork, 将当前的 repo 变成上游, 然后顺便改个名

建议 20 人以上的团队都试着开启 linear history, 你们会感谢这个风格的

```



# 抱抱脸账号 

[Huggingface上传自己的模型](https://juejin.cn/post/7081452948550746148)

see nodejs summary.md -> 抱抱脸

```
dlxjj pwd email same as github's dlxj

pip install huggingface_hub && \
git config --global credential.helper store && \
huggingface-cli login
	# 用 token 登录
	# Your token has been saved to 
		/root/.cache/huggingface/token

huggingface-cli repo create pandora --type dataset
	# --type {model, dataset, space}
	# 创建创库 完了以后在官网把它设为 私有
	# huggingface-cli repo create InternLM-SFT --type dataset




git lfs install && \
git add . && \
git commit -m 'm' && \
git lfs migrate import --everything && \
git push
	# 成功提交大文件

vi sync_hubggingface.sh
cd /mnt/hubggingface/pandora && \
/usr/bin/cp -rf /root/echodict/pandora/* . && \
git add . && \
git commit -m 'm' && \
git lfs migrate import --everything && \
git push
	# 备份 pandora 到 hubggingface

crontab -e
00   00    *      *   *  sh /root/backup.sh
00   *    *      *   *  sh /root/sync_hubggingface.sh
30   *    *      *   *  sh /root/sync_hubggingface.sh
@reboot  mount /dev/sda1 /mnt
@reboot  pm2 resurrect
	# 每半小时自动备份一次



huggingface-cli lfs-enable-largefiles /mnt/hubggingface/pandora
	# 大于5G 文件 需要这样设置
	
	

安装好 git-lfs 后：

git lfs install
git lfs clone https://huggingface.co/datasets/dlxjj/pandora

git lfs clone https://huggingface.co/datasets/dlxjj/echodict

git restore --source=HEAD :/
	# retry

pip3.9 install huggingface_hub
https://huggingface.co/settings/tokens
	# copy token 
	
huggingface-cli login



huggingface-cli lfs-enable-largefiles /root/hugface/echodict

```





# 黑科技



## GIT_SSH_COMMAND

```
GIT_SSH_COMMAND='ssh -i private_key_file' git pull  
  # needs git 2.3.0 above. git source  
```

```
## 远程挂载
sshfs [user@]hostname:[directory] mountpoint
```

```
sftp root@xxx.xxx.xx.xx << EOF
cd /root/environment/apache-tomcat/webapps/static/xxx
put -r ./web-view
put -r ./mp-images
bye
EOF
```

```
echo 'EOF
cd /root
put /Users/vvw/gitee/GFW/keye
bye
EOF' | sftp -i ~/gitee/GFW/keyt root@111.229.53.195 && \
echo 'upload gitee private key tasks done.'
```



## xargs 多行输出转一行输出



xargs命令将多行输出内容转换成一行以空格分隔的输出内容，通过管道传递给awk命令，然后使用awk命令以空格为分隔符，获取第一个最高的版本号



## Automatically answer in Bash Script



```
(sleep 3; echo "Y";) | apt-get install build-essential
yes "Y" | apt-get install build-essential
```







pbcopy < ~/.ssh/id_rsa.pub -- copy public SSH key to clipboard  

github.com ->setting ->add SSH key ->paste


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

git clone https://github.com/dlxj/doc.git  


**gitee码云账号**    

git config --list   查看当前账号  

cegbdfa  
123468935@qq.com   
https://gitee.com/cegbdfa  


git config --global user.name "cegbdfa"  
git config --global user.email   "123468935@qq.com"  

rsa公钥直接拿github的用，不生成了  
免密码登录不配置  

**回滚到上一次提交**    

> git reflog    
git reset --hard  451880c        

列出所有最近两周内的提交   
> $ git log --since=2.weeks   
想找出添加或移除了某一个特定函数的引用的提交  
>  $ git log -Sfunction_name   
2018 年 4 月期间，Junio Hamano 提交的但未合并的测试文件  
> $ git log --pretty="%h - %s" --author=gitster --since="2018-04-01" --before="2018-05-01" --no-merges -- t/  

**解决冲突**  [u](https://juejin.cn/post/6873035040758956046)

> 冲突标记  
> <<<<<<<与=======之间是我的修改  
> =======与>>>>>>>之间是别人的修改    
> **强制提交**  
> git push origin master -f     
> **完全覆盖本地**    
> git checkout .  
> git pull  
>
> ```
> # 不行就用这个
> git checkout -f && \
> git clean -df && \
> git pull
> 
> git checkout -b master 2e0ed59cb56c45decdb1756cc520510f58e05149
> 	# 拉指定某次提交
> 
> ```
>
> 

p
> git pull && \
git add . && \                   
git commit -m 'm' && \
git push origin master && \         
echo "push doc success!"

## vi 
:$  or  G   跳到文件尾  
:0  or  gg 跳到文件首  
A  跳到行尾，并进入后插模式    
I  跳到行首，并进入前插模式    
u  撤销上次更改   
dd 删除当前行  


## overleaf  LaTex  

使用自定义包  
> 上传tipa.sty  



## Termux



### TF Card 256G

```bash
cd ~
termux-setup-storage
cd storage
cd external-1
# external-1 soft link to -> /storage/1CE4-09FD/Android/data/com.termux/files
## this only directory has permission can read && write in TF Card 
```









apt update && apt upgrade -y  
apt search texlive  
apt install texlive  
用tlmgr  更新包  
tlmgr search  
tlmgr install  
tlmgr update --self --all  更新整个 TeX Live 系统  

pkg uninstall [package name]  卸载  

**tar 可以保留权限等属性**  
> tar -cf lib.tar /lib  
tar xvf  

**7z 最大压缩**
> 7z a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on xx.7z dir
7z x filename    
7z 解压无顶层目录的文件  
> 7z x pgf_3.0.0.tds.zip -o*  
7z x *.7z -o*  
apt-get install p7zip-full

**Could not get lock**  
> killall apt-get; \
rm /data/data/com.termux/files/usr/var/cache/apt/archives/lock  
**pkg install p7zip**  




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
- **markor**  markdown编辑器   
- **feem 离线热点文件传输** feem.io  
- Google Colab 在线python 编辑器，免费GPU  
- notion 云笔记  
- VSCode + Latex Workshop + TeX Live + Git + Sumatra PDF  
- **纯纯写作** 永不丢失的笔记  
- **sublime text**  写代码    
- typora+坚果云 = 个人云笔记   
- 坚果云 + hexo = GitHub 博客  
- **markor** 安卓的**markdownd 编辑器**  
- https://www.**overleaf**.com **LaTex qq email login** 
- **Detexify 手写字符，生成LaTeX代码**  
- Jsho 自动分割日语句子查单词  
- 日语动词词典 查动词的各种活用  
- **nplayer** 视频播放  
- LRC Editor  
- **乐秀视频编辑器** 视频提取mp3  
- **Super Sound 切割mp3**    
- LongShot 长截图  
- Pixlr 图片编辑  
- Gallery 图片浏览  
- **PDF切割器**  apk  
- **Xodo 免费PDF阅读器**    
- 阅读  apk  
- 全民追书  apk  
- **博看书苑 apk  机构号：szghdzsw 密码:83393023**   
- **异次元  在线漫画**    
- **Comic Screen** ・perfect viewer **看本地漫画**  
- **flud** bt下载  
- **transmission**  bt下载  
- Bochs Limboemu APQ QEMU 安卓上安装Linux虚拟机  
- yandex  **支持插件的浏览器**  
- virmach 便宜的vps  
- Termux 安卓上的linux 环境，有git
- linux deploy 安卓手机刷原生Linux  
- AndroCat 安卓坚果云客户端  
- Aurora Store 应用商店xda 出品  
- Hacker's Keyboard 黑客键盘PC 全键位 
- 深度学习500问  

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
**csrutil disable**  
**vi ~/.bashrc**  
**export PATH=/Users/vvw/.cabal/bin:$PATH**  
**source ~/.bashrc**   
./configure --prefix=/usr  
make install  
link xxx /usr/bin  

**bashrc 下次就不生效了**  
> vi ~/**.bash_profile**    
PATH="${HOME}/usr/bin:${PATH}"  
export PATH  
**~/.bash_profile  每次开shell 都执行**  

**Mac 内录**  
> ShowU Audio Capture   
 Soundflower：https://github.com/mattingalls/Soundflower/releases  
https://www.jianshu.com/p/db035dad616a  

**Mac 软件打不开**    
sudo spctl --master-disable  
sudo codesign --force --deep --sign - /Applications/CleanMyMac\ X.app  



piano  
- Sibelius 打谱软件  西贝柳斯  
- Overtrue 4.1.5  打谱软件  
- OvePlayer.dmg  
- Hypersonic.2.iso 钢琴软件  
- 施坦威II大钢琴音源素材  
- Kongaudio中国民族乐器软音源十三种乐器  

**音乐**  
> **logic x pro**   
Cubase   
FL Mobile  
**feem 离线热点文件传输** feem.io  
洞箫入门半个老师    
Euterpea  haskell muz   
【编曲/作曲】Nice Chord**好和弦**乐理教程  
**music21**  mit miz lib     
**Tidal haskell**  live coding music    
当当云阅读  写歌秘籍：歌词写作基础教程  
https://www.jita5.cn  吉他层很多书  
https://masuit.com/ 懒得勤快互联网分享 多软件  
https://yun.naodai.org/Software/  多软件  
**bilibili** 15726712xxx  
Mathematica 激活指南  
**vvw dlxj github cegbdfa gitee**  
**Telegram** 1572671xxxx  **facetheworld** 
**https://ftw.jzfj.shop/**   
https://pt.eastgame.org/  **TLF电影** aiiniyo  siluplsy@gmail.com  vN5   
**Deluge** windows  
**Transmission** linux osx  
**flud**  android  
音乐术语对照词典    
外国音乐表演用语词典  
**和弦进行秘笈・活用与演奏-浦田太宏**  
**流行歌词写作教程**·尤静波著  
【田馥甄】强势还原《**小幸运**》台式小清新治好了我上周的感冒 MIDI工程演示  **logic x 工程**

**查汉字**  
https://ctext.org/pre-qin-and-han/zhs?searchu=**晏如**  中国哲学电子书计划  
http://cls.lib.ntu.edu.tw/tang/Database/index.html  **全唐诗检索**     
https://books.google.co.jp  靖静 大漢和辭典    
http://www.52shici.com  **格律在线检测**    
http://www.duiduilian.com/pzcx/ **平仄查询**    
app **fooview** **诗词助手、押韵助手、诗云，韵典**  **ReadEra**  djvu pdf 阅读器  
**IPA Keyboard** **国际音标输入法**       
**漢字古今中外讀音查詢**      
**IPA Phonetics ios**  
**AV Phonetics android**  **学国际音标**  
**IPA FOR PARISIAN FRENCH**  法语音标发音    
**NotesDeMusique  读谱训练**      
https://linguistlist.org/unicode/ipa.html  音标字符    https://westonruter.github.io/ipa-chart/keyboard/  
**香港语言学学会粤语拼音方案**  
https://zh.m.wikipedia.org/zh-hans/%E9%A6%99%E6%B8%AF%E8%AA%9E%E8%A8%80%E5%AD%B8%E5%AD%B8%E6%9C%83%E7%B2%B5%E8%AA%9E%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88  
**日语国际音标**    
https://en.m.wikipedia.org/wiki/Hiragana#Table_of_hiragana
高垣彩陽 初恋 site:https://utaten.com    
掌上书苑  
**般若波罗蜜多心经  中華電子佛典協會**    
http://cbetaonline.dila.edu.tw/zh/T0251_001  
https://dialogue.moe  **剧本对白全文检索**    
https://github.com/windrises/dialogue.moe   
https://bgm.tv/group/a  **技术宅真可怕**https://bgm.tv/group/a  
https://epubw.com  **书最全**  
https://epubw.xyz   
http://www.ireadweek.com  **周读 电子书**  
sobooks.cc kindle电子书  
https://5kindle.com  子午书简  
https://yunpanzhushou.com  **云盘助手**  
https://www.jiumodiary.com  **PDF书多**  
http://libgen.lc  梁思成全集  
https://www.soepub.com  掌上书苑  
https://convertio.co/zh/azw3-mobi/  转mobi  
https://utaten.com  日语歌词检索  
http://www.hiragana.jp  网站日文假名标注  
https://m.jcinfo.net  日文句子假名标注 
https://freemdict.com/  字典  
https://chaoli.club  超理论坛  
https://www.codecogs.com  生线生成latex 公式    
https://nyaa.si   
vol.moe **漫画**   
https://e-hentai.org 漫画  
https://www.weblio.jp 日语词典    
https://ja.wikipedia.org    
https://music.ghpym.com 音乐、歌词下载  
https://github.com/scutan90/DeepLearning-500-questions  
http://wpspro.support.wps.cn/gov/guangdong/zhaoqing/  政府版wps  


ainiyorin@gmail.com  

https://my.yunxiazai.xyz/  坚果加速  
> aiiniyo 

http://ftw.jzfj.shop/user  facetheworld   
> 123468935@qq.com  
群：584237371  
15726712516 15726712516电报群

小七手游  15726712516  口袋进化  187服  
光环助手  果盘  18277286430  


pacman -S texlive-core texlive-langjapanese  





$ sudo pacman -S noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra   

vi /etc/locale.gen  
locale-gen
export LANG=ja_JP.UTF-8   
luatex  




localectl set-locale LANG=ja_JP.UTF-8    

vi /etc/locale.conf  
LANG=ja_JP.UTF-8   

shutdown 0  





niconico

fc-list :lang=zh  
fc-cache -f  


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


最大压缩  
7z a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on xx.7z dir  

https://github.com/dlxj/doc  
https://github.com/vvw/  
https://gitee.com/cegbdfa  



chrome缓存路径

> 地址栏打开：chrome://version
>
> | Profile Path | /Users/xxx/Library/Application Support/Google/Chrome/Default |
> | ------------ | ------------------------------------------------------------ |
> |              |                                                              |



递归查找包含某串的所有文件

- grep -r mresources ./tutorial

- grep -rl 参数l 只打印文件名

- grep -rl mresources ./tutorial | xargs  sed -i ""  's/mresources/cegfdb/g'

  > 全局替换 mresources替换为cegfdb



### NFS

- https://github.com/termux/termux-packages/issues/11696



## Neo4j



> ```
> # Config
> sudo vi /etc/environment
> 
> # Add the line below
> # JAVA_HOME="/usr/lib/jdk-11.0.9/"
> 
> # Config
> sudo vi ~/.bashrc
> # Add the lines below
> # JAVA_HOME=/usr/lib/jdk-11.0.9/
> # PATH=$JAVA_HOME/bin:$PATH
> source ~/.bashrc
> 
> # Verify
> echo $JAVA_HOME
> javac --version
> ```

