[IPA Unicode Keyboards](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=uniipakeyboard#79dbd88a)    







首先，我找到了这里
[IPA Unicode Keyboards](https://link.zhihu.com/?target=http%3A//scripts.sil.org/cms/scripts/page.php%3Fsite_id%3Dnrsi%26id%3Duniipakeyboard%2379dbd88a)，下载了SIL的IPA输入法，将安装包打开后，里面有一个IPA.keylayout文件，把它放到你 Mac 的 “电脑\资料库\Keyboard Layouts”文件夹，注销或重启一下，再按<command+空格>就能看到IPA输入法了。
要想输入国际音标，要对照安装包里的说明文档，先输入deadkey（有<, >, | , @，#等等）再输入对应的字母（区分大小写）。
为了方便老婆查询，我还打印了说明文档。

然而，老婆只看了一眼说，实在太多了，臣妾根本找不到啊！！！！

好吧，继续想办法吧。

后来我找到了这个[lukhnos/openvanilla · GitHub](https://link.zhihu.com/?target=https%3A//github.com/lukhnos/openvanilla)，应该是台湾同胞做的Mac下可定制的输入法[openvanilla](https://link.zhihu.com/?target=https%3A//github.com/lukhnos/openvanilla)，它的好处是可——以——定——制——自己的输入法！！！！

有了这个就好办了。

github页面上有下载链接[https://app.openvanilla.org/file/openvanilla/OpenVanilla-Installer-Mac-1.0.11.zip ](https://link.zhihu.com/?target=https%3A//app.openvanilla.org/file/openvanilla/OpenVanilla-Installer-Mac-1.0.11.zip)
不过需要翻墙。。。。
我已经下好了，在这里：[http://pan.baidu.com/s/1jG0bTjC](https://link.zhihu.com/?target=http%3A//pan.baidu.com/s/1jG0bTjC) 密码：d6w2

下一步就是要建立自己的国际音标输入法了。

OpenVanilla可以存多个输入法，每个输入法是由一个cin文件描述的。

我们先看看已经做好的是什么样子的，**biaoyin.cin**

  ：

```text
%gen_inp
%ename Biaoyin
%cname 表音
%encoding UTF-8
%selkey 1234567890
%endkey '"-()[];:,.!?/
%keyname begin
' '

/ /
1 1
2 2
3 3
4 4
a a
b b
c c
d d
e e
f f
g g
h h
（省略若干行）
z z
%keyname end
%chardef begin
a	a
a	A
a1	ā
a1	Ā
a2	á
a2	Á
a3	ǎ
a3	Ǎ
a4	à
a4	À
（省略若干行）
%chardef end
```

这个是将键盘上的按键对应到类似汉语拼音上，是不是和我们要实现的很像！！！

我们要做的就是将

```text
%gen_inp
%ename Biaoyin
%cname 表音
%encoding UTF-8
%selkey 1234567890
%endkey '"-()[];:,.!?/
%keyname begin
```

改为

```text
%gen_inp
%ename IPA
%cname 国际音标
%encoding UTF-8
%selkey 1234567890
%keyname begin
```



**说明一下：**
%gen_inp    标识输入法开始的标记
%ename      为输入法的英文名字
%cname      为输入法的中文名字
%encoding  为编码格式
%selkey      为选择字符时的按键
%endkey     可以不用了。
%keyname begin
.....
%keyname 
%chardef begin
......
%chardef end



后面的%keyname begin和%keyname end之间的就是要把你可能用到的按键都放进去，应该有a到z吧，还有辅助标点符号之类的。

%chardef begin和%chardef end之间是**重点**了，这里应该是你每个按键对应的国际音标。每个按键可以对应多个，别怕多，可以通过0-9的数字选取的（输入国际音标还是要用到前面的IPA输入法）。

比如这是按键a对应的音标：

```text
a a
a A
a ɐ
a æ
a ɑ
a ᵅ
a ᵃ
a ᶏ
a α
a ᶐ
a ᵄ
a ᶛ
```

看到了没？
接着把剩下的每个国际音标都对应某个按键输进去，就做好了，然后保存为ipa.cin文件，可以存到文稿里。

然后安装OpenVanilla，用<command + 空格>切换到OpenVanilla输入法，点屏幕上部的输入法图标，在下拉菜单中选“OpenVanilla设置”，打开后左边有加入新的输入法，选“汇入”，找到你刚存的cin文件，就大功告成了！！

如果觉得不满意可以按照你的想法修改，需要移除之前汇入的输入法，然后重新汇入一次就行了。



试试按几个字母，看看效果如何？

**不足之处**：

- 有若干个音标在编辑cin时无法打出，所以也无法通过OpenVanilla打出。不得不切换到IPA打出来。



如果哪位发现改进的方法，望不吝赐教。

差点忘了，这是我和老婆一起做的cin文件，欢迎使用。

链接：[http://pan.baidu.com/s/1dDoaK9r](https://link.zhihu.com/?target=http%3A//pan.baidu.com/s/1dDoaK9r) 密码：eup0



2018年1月5日更新：

最新版的OpenVanilla：链接:[https://pan.baidu.com/s/1geNyPH5](https://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1geNyPH5)  密码:un8j