
GeneralUtilities`PrintDefinitions[BinLists]
Information[BinLists]
??GeneralUtilities`*
SetDirectory@NotebookDirectory[];
Get@FileNameJoin[{(*ParentDirectory[]*)NotebookDirectory[],"std.wl"}];
Names["Std`*"]
(*Names["Std`Private`*"]*)
(*??Std`bomFreeQ*)
(*Mathematica 黑魔法：查看内部函数定义*)
Map (*trigger auto-load*)
Unprotect[Map];ClearAttributes[Map,ReadProtected];
Begin["System`Map`"]
Information[Map]
<<Spelunking`
Names["Spelunking`*"]
Information[Spelunking`Spelunk]
(*Spelunk["System`Map"]*)
<<CodeFormatter`
FullCodeFormat[Map]


跳转括号的方法
    在一个括号上连续点击三次，会选中括号内的所有内容
    然后再按一下右箭头就跳转到括号最后了

显示读保护的代码
Debug`$ExamineCode = True  

??BinLists

(*get system clipboard's image*)
cb = ToExpression@
   Cases[NotebookGet[ClipboardNotebook[]], BoxData[_], Infinity] //
  First

Cell["Examples and tests for FFmpeg", "Title"]
Cell[" Package Declarations", "Section"]
Cell["FFmpeg Function", "Subsection"]
Cell["Testing input for the functions", "Subsubsection"]

查看内核的运行情况
    Parallel`Developer`KernelStatus[]  这个命令. 

I believe Ctrl + K and Ctrl + Shift + K should be mentioned.

mma的GUI 开发
    plz search  stanalone interface

运行mma 脚本
    Wolfram Language Scripts
Running Mathematica scripts directly from the Unix shell
1) Select cells with pretty expressions within the Mathematica Notebook and click Cell > Convert to > InputForm
2) Cut and paste the resulting inputform code into a textfile, e.g. script.m.
3) Repeat 1)-2) as needed.
4) Terminate textfile with:  Exit[]
5) Execute script from the command line prompt with:
~$ MathKernel -noprompt -run “<<script.m”

package 开发
-- hi.m
BeginPackage["hi`"]
    f::usge = "f[],hi,,,";
Begin["`Private`"]
    f[]:=5
End[]
EndPackage[]
-- tt.nb
Get@FileNameJoin[{NotebookDirectory[],"tt", "hi.m"}]
?hi`*        
<< "Skew.m"
$Packages

mma IDE
    Wolfram Workbench

AuthorTools
    AuthorTools is an add-on package that simplifies the creation of documents in the Wolfram System and is particularly suited for book production tasks.


utf-8 乱码

UnicodeLanguageFontMapping.tr文件里有“# Japanese”和“# ChineseSimplified”区块啊，你把在前者且同在后者的那些字符（这时他们的Unicode码是一样的），都挪到中文那个区块里去就行了。字符比较多，你可以编个程序筛选一下，用Complement之类的函数什么的……

CJK的范围看Unicode规范文档：

CJKSymbolsAndPunctuationRange = Range[12288, 12351];
CJKExtARange = Range[13312, 19903];
CJKRange = Range[19968, 40959];

这三个合在一起就差不多是常用汉字字符的Unicode码集了。用ToCharacterCode[字符, "CP936"]把他们对应的CP936码列出来，格式化一下加在“# ChineseSimplified”区块里。把“# Japanese”区块里那些在刚才列出的常用汉字集合里的删掉。

需要注意的是Mathematica的FromCharacterCode和ToCharacterCode用的码表在\SystemFiles\CharacterEncodings\下面，而不是直接调用的操作系统的codepage。

矩阵中连续的两个或三个连续的全零行替换成全2行

{{{0,0},{0,0}},{{1,1}},{{0,0}} } /. {{x:Repeated[{0..},{2,3}]}:>({x}/.{0->2}) }
    {{{2,2},{2,2}},{{1,1}},{{0,0}}}
    x匹配的是一个Sequence，所以外面用{}括起来
    :> 这里用的是延迟规则(RuleDelayed)，不要立既计算。注意不要被delayed和非delayed 坑了 

$CharacterEncoding
CP935
$CharacterEncoding="utf-8"

跟据上表，解读 UTF-8 编码非常简单。如果一个字节的第一位是0，则这个字节单独就是一个字符；如果第一位是1，则连续有多少个1，就表示当前字符占用多少个字节。

下面，还是以汉字严为例，演示如何实现 UTF-8 编码。

严的 Unicode 是4E25（100111000100101），根据上表，可以发现4E25处在第三行的范围内（0000 0800 - 0000 FFFF），因此严的 UTF-8 编码需要三个字节，即格式是1110xxxx 10xxxxxx 10xxxxxx。然后，从严的最后一个二进制位开始，依次从后向前填入格式中的x，多出的位补0。这样就得到了，严的 UTF-8 编码是11100100 10111000 10100101，转换成十六进制就是E4B8A5。


[shredder12]$ ffmpeg -i inputfile.avi -r 1 -s 4cif -f image2 image-%3d.jpeg

4cif options stands for the frame size 704x576. There are a variety of options that you can use.

sqcif   128x96  qcif    176x144 cif 352x288
4cif    704x576 qqvga   160x120 qvga    320x240
vga 640x480 svga    800x600 xga 1024x768
uxga    1600x1200   qxga    2048x1536   sxga    1280x1024
qsxga   2560x2048   hsxga   5120x4096   wvga    852x480
wxga    1366x768    wsxga   1600x1024   wuxga   1920x1200
woxga   2560x1600   wqsxga  3200x2048   wquxga  3840x2400
whsxga  6400x4096   whuxga  7680x4800   cga 320x200
hd480   852x480 hd720   1280x720    hd1080  1920x1080




