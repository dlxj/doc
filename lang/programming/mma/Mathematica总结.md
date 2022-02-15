[TOC]

# Mathematica总结



$Version

- 显示版本号



sameQ :=(Length[#1 \[Intersection] #2]  == Length[ #1])&
sameQ[{1,2,3}, {1,3,2}]

用交集来判断集合是否相等？



文本搜索，这就更有意思了
 TextSearch
 文件系统Map，这就有意思了
 FileSystemMap
 可以递归的获取所有文件名
 FileNames

 show biggest file or dirctory on mac
 sudo du - sh* | grep - E "\dG\[CloseCurlyDoubleQuote]
      

      查慧林音义 仁
      
      find . -type f | xargs cat | grep " < p > .*仁.* < 
    span class = ' note - inline' > ("
仁者 (而親反周禮云德一曰仁鄭玄曰愛人及物曰仁上下相親曰仁釋名仁者忍也好生惡煞善惡含忍也)。



## Mathematica 黑魔法：查看内部函数定义

GeneralUtilities`PrintDefinitions[BinLists]



## 每次启动MMA自动把编码设成UTF8



```
If[$CharacterEncoding =!= "UTF-8",
	$CharacterEncoding = "UTF-8";
	Print[{
		Style["$CharacterEncoding has changed to UTF-8 to avoid problems.", Red],
		Style["Now all IO operation are using UTF-8 as default.", Red],
	} // TableForm];
	st = OpenAppend[FindFile["init.m"]];
	WriteString[st, "$CharacterEncoding=\"UTF-8\";"];
	Close[st];
];
```

```
Get["~/test.m", CharacterEncoding -> "UTF-8"]
```



# WalframScript

```
wolframscript --version
```

```
Print[InputString[]];
echo "Hello" | mathematicaScript
```

```
#!/Applications/Mathematica.11.3.0.app/Contents/MacOS/wolframscript
(* ::Package:: *)

argv = Rest @ $ScriptCommandLine;
argc = Length @ argv;
Do[Print[argv[[i]]], {i, argc}]
```



```
currDir = If[$InputFileName=="", NotebookDirectory[], Directory[]]
mfiles = FileNames["*.m", currDir,Infinity];
Export[FileNameJoin[{currDir,"out.txt"}], mfiles];
```





# Stdin



```
Print[InputString[]];
```





## Package

```mathematica
?? std`iSim`*
?? std`iSim`similarOfSents
Names["std`*`*"]
```



```mathematica
$ContextPath
Names["Std`*"]
Names["Std`Private`*"]
??Std`bomFreeQ
```







### 全局符号列表 $ContextPath

```mathematica
$ContextPath  
```



### 符号在哪个包下面

```mathematica
Context[Integrate]
```





## 集合



### 交集 Intersection 

```
Intersection
```



## 函数重载



```
ClearAll[f]
f[x_ /; x > 0] := 999 
f[x_ /; x <= 0] := -1 
f[x_ /; StringQ[x] ] := -999 
(*f[x_/; MatchQ[x, List[_String..]]]:= 10000*)
f[x : List[_String ..]] := 10000
f[{"a"}]
=> 10000
```



## UTF8



Get["~/test.m", CharacterEncoding -> "UTF-8"]

```mathematica
(* :fixfiles.m: *)
(* convert all files encoding to utf-8, which ".m" file in the current and it's sub directory *)
currDir = If[$InputFileName=="", NotebookDirectory[], Directory[]]; 
mfiles = FileNames["*.m", currDir, Infinity];
$FixRule = {
	char : RegularExpression["\\\\:.{4}"] :> ParseCharacter@char,
	char : ("\\[" ~~ Shortest[c__] ~~ "]") :> ParseCharacter@char
};
ParseCharacter = With[{t = ToExpression[#, InputForm, Unevaluated]}, SymbolName@t]&;
FixFile[file_String] := Export[file,
	ToCharacterCode[StringReplace[Import[file, "Text"], $FixRule], "UTF-8"],
	"Binary"
];
logs = Export[#,ToCharacterCode[ StringReplace[Import[#, "Text"], $FixRule], "UTF-8"], "Binary"]& /@ mfiles;
Export[FileNameJoin[{currDir,"logs.txt"}], logs]
```





Mathematica 保存文件会自动使用 ASCII 兼容转义

这非常不利于 IDE 源码阅读和版本管理

我们可以强制转换到 UTF8 编码:

```mathematica
$FixRule = {
	char : RegularExpression["\\\\:.{4}"] :> ParseCharacter@char,
	char : ("\\[" ~~ Shortest[c__] ~~ "]") :> ParseCharacter@char
};
ParseCharacter = With[{t = ToExpression[#, InputForm, Unevaluated]}, SymbolName@t]&;
FixFile[file_String] := Export[file,
	ToCharacterCode[StringReplace[Import[file, "Text"], $FixRule], "UTF-8"],
	"Binary"
];
```

注意有些字符还是会显示框框, 这是因为 Wolfram 使用了保留区的 Unicode 编码.

实际是能正常运行的, 如果代码无法导入, 运行下列代码强制所有 IO 改为 UTF8.

```mathematica
If[$CharacterEncoding =!= "UTF-8",
	$CharacterEncoding = "UTF-8";
	Print[{
		Style["$CharacterEncoding has changed to UTF-8 to avoid problems.", Red],
		Style["Now all IO operation are using UTF-8 as default.", Red],
	} // TableForm];
	st = OpenAppend[FindFile["init.m"]];
	WriteString[st, "$CharacterEncoding=\"UTF-8\";"];
	Close[st];
];
```



```mathematica
SetDirectory@NotebookDirectory[];
(*strm=OpenRead["学研国語大辞典ku00.txt",Method\[Rule]{"File",CharacterEncoding\[Rule]"ShiftJIS"}];*)
shiftj=FromCharacterCode[BinaryReadList@"学研国語大辞典ku00.txt","ShiftJIS"];
Characters@shiftj//Take[#,{8}]&
file="学研国語大辞典ku00utf8.txt";
stream=OpenWrite[file,CharacterEncoding->"UTF-8"];
WriteString[stream,shiftj];
Close@stream;
```





## Nothing Null None

1. **Nothing** 

    > 被替换成Nothing 的东西会被自动删除

2. **Null** 

    > 可以作为函数的返回值，然后调用者用来进行逻辑判断 

3. **None** 
   
    > 是用在Option 里的东西，Option 可以理解成一组默认参数



## Sequence

Sequence

> 表达式要返回多个值，又不想装在List 里面，可以用Sequence[x, y]



## GUI

help -> DirectedEdge

> Graph[{Labeled[1\[DirectedEdge]2,"Hello"],2\[DirectedEdge]3,3\[DirectedEdge]1}]
>
> Graph[{Button[Style[1\[DirectedEdge]2,Red],Speak["Hello"]],2\[DirectedEdge]3,3\[DirectedEdge]1}]
>
> Graph[Table[Property[v,{VertexSize->0.2+0.2Mod[v,5],VertexStyle->Hue[v/15,1,1]}],{v,0,14}],Table[v\[UndirectedEdge]Mod[v+1,15],{v,0,14}]]



## Thread 组合

Thread

> 有将两样东西组合起来的能力



## MapIndexed

MapIndexed

### 带索引的Map

> 数据在列表中的位置信息以第二参给出



## Fold 累积

### Fold 具有累积效果的函数

```
Fold[f,x,{a,b,c,d}]
f[f[f[f[x,a],b],c],d]
```



## Nest

### Applying Functions Repeatedly

```
Nest[f,x,4]
f[f[f[f[x]]]]
```



## List

### Transpose

##### ctrl+^, ESC+tr+ESC





##  DictionaryLookup

### 所有字典可查询的语言

```
DictionaryLookup[All]
(* MMA所有词典语言 *)
Rasterize@ Style[#,Large]&@ Grid@ Partition[#,5,5,1,"\\"]&@LanguageData["Hebrew","Letters"]
(* 希伯来语字母表 *)
Rasterize@ Style[#,Large]&@ Grid@ Partition[#,5,5,1,"\\"]&@ LanguageData["Hindi","Letters"]
(* 印地语字母表 *)
DictionaryLookup[x__/;StringLength[x]>6]
(* 长度大于6的单词 *)
```



## Rasterize 光栅化





## Lookup

### Lookup 配合Association 使用

```
(* 取某列的所有数据 *)
table = {
   <|a -> 1, b -> 2|>,
   <|a -> 3, b -> 1|>,
   <|a -> 4, b -> 3|>
   };
Lookup[<|a -> 1, b -> 2|>, a]
{1, 3, 4}
```



## KeyMap

### KeyMap 配合Association 使用

### Reverse 配合AssociationMap 使用

> 让key value 反过来



## 参数检查和错误处理
```
  rsqrt[x_] /; If[TrueQ[x >= 0], True, Message[rsqrt::nnarg, x]; False] := Sqrt[x]
  rsqrt::nnarg = "The argument `1` is not greater than or equal to zero.";
  (*占位符 `1`*)
```
>如果参数不符合条件Message 会打印一条红色的消息。/; 遇到False 模式配配失败后面的代码不会执行 
  但是没有终止程序，除非用 Throw@ $Failed; Abort[]; 



##  中缀表达式

> list  ~ Take  ~ 5



## String



### 字符串格式化 StringTemplate

```mathematica
StringTemplate["first `a` then `b`"][<|"a" -> 1234, "b" -> 5678|>]
StringTemplate["a is ``, b is ``"][5555, 6666]
```



### TemplateSlot

```
In[1]:= t = Mean[{TemplateSlot["me"], 50, 30}];
TemplateApply[t, <|"me" -> 100|>]
Out[1]= 60
```



### ToCharacterCode

```mathematica
ToCharacterCode["abcABC\[Alpha]\[Beta]\[Gamma]","UTF8"]
FromCharacterCode[%, "UTF8"]
```



### CharacterRange

```
CharacterRange["a", "z"]
CharacterRange[1000, 1020] (* use char code *)
```





## TrueQ MatchQ ContainsAny

## HoldComplete Unevaluated



## Block 

Block

> 里面可以临时修改系统变量的值，这之后函数的行为会受到影响



## 文件和目录

### DirectoryName

完整路径的目录部分

### FileBaseName

文件名去掉扩展名的部分

### FileExtension

扩展名部分



```mathematica
SetDirectory[NotebookDirectory[]];
j = Import[FileNameJoin[{$HomeDirectory,"/Documents/GitHub/ebmac/","tiny.json"}],"JSON", "Compact"->False]
jj = Import[FileNameJoin[{$HomeDirectory,"/Documents/GitHub/ebmac/","guoyu.json"}],"RawJSON"];
ass=Import["[Kamigami] Shoujo Shuumatsu Ryokou - 01 [1080p x265 AAC].ass","Text",CharacterEncoding->"UTF8"];
(*终末少女的旅行中日字幕，诸神字幕组*)
lines=StringSplit[ass,RegularExpression["(?m)^"]];  (*(?m)^换行符*)
jps=Reap[lines /. x_String?(StringMatchQ[#,"Dialogue"~~__~~",TEXT-JP"~~__]& ):>(Sow[x]);Nothing]//Flatten;
chs=Reap[lines /. x_String?(StringMatchQ[#,"Dialogue"~~__~~",TEXT-CN"~~__]& ):>(Sow[x]);Nothing]//Flatten;
(* MMA 速查文档 https://mresources.github.io/tutorial/ *)
(* MMA 建站代码 https://github.com/mresources/tutorial *)
(* MMA 建站文档 https://www.wolframcloud.com/objects/b3m2a1.docs/BTools/ref/WebSiteBuild.html *)
(* MMA 帮助文档快速生成 https://zhuanlan.zhihu.com/p/113333655 *)
(* ASS SRT 字幕，音视频开发  https://www.cnblogs.com/tocy/ *)
 (*让语句返回值为Nothing，然后存在List 里面的Nothing 就自已消失了*)
(* MapIndexed 带index 的map 第一参： #1 列表元素，第二参： #2 { index } *)
(* RegularExpression 正则表达式 *)
(* 字符串格式化 StringTemplate *)
(* AppExecute["ListPackages","BTools"]~Take~5 https://github.com/b3m2a1/mathematica-BTools/wiki/BasicUsage *)
debug:=GeneralUtilities`PrintDefinitions
```





## 运行外部程序

```
RunProcess[{"ffmpeg"},ProcessEnvironment -> <|"PATH" ->"/usr/local/bin/"|>]
```



## DataSet



### List to Dataset



```
ListsToAssociation:=Association[Thread[Rule[#colNames,#alist]]]&

jpsDataset:=Dataset@Map[ListsToAssociation[<|"colNames"->{"order","beginTime","endTime","text"}, "alist"->#|>]&, AssDialogueFirstN[<|"assList"-> Map[ReplaceNewline,jps], "n"->All|>]],
chsDataset:=Dataset@Map[ListsToAssociation[<|"colNames"->{"order","beginTime","endTime","text"}, "alist"->#|>]&, AssDialogueFirstN[<|"assList"->  Map[ReplaceNewline,chs], "n"->All|>]]
(* Ass 中日字幕数据集 *)
},
```





### 指定行列取值

```
dataset[3, "a"]
```



### Map

```
jpsDataset[All, {"beginTime"->AssTimeToSrtTime, "endTime"->AssTimeToSrtTime}]
```



### 分页

```
jpsDataset[Select[ 10 <= #order <= 20 &]]
(* order *) 是列名，序号。#order 是Associate 的取值简写
```

### 变回Association

#### Normal



### SQL运算符：内联接 & GroupBy 

#### guide/DatabaseLikeOperationsOnDatasets



## RegularExpression 

正则表达式

### Split 字符串在换行处

```
StringSplit["line1\nline2\nline3",RegularExpression["(?m)^"]]//InputForm
```





## TTS 时高亮文本

(*

Highlight and speak each substring

TTS 时高亮文本

*)

lst = {"Ooops!", "there", "are", "errors"};

Monitor[Do[Speak[lst[[i]]]; Pause[0.8], {i, Length[lst]}],

 Row[MapAt[Style[#, CMYKColor[0, 0.4, 1, 0]] &, lst, 

  If[IntegerQ[i], i, 1]], " "]]

SpokenString

## 数学公式的文字表达

$Version

  返回版本号

$SystemID

  返回OS 信息

?Head 

  返回帮助

% 

  上一个输出结果

%% 

  上上个输出结果

Head

  返回变量类型

TextString

   任意表达式转String 

@

  Prefix 前缀，优先级很高

  会把后面所有的东西用括号括起来

@@

  Apply 是换头术, 把原来的Head 全部换成另一个Head

  f@@{1,2} List[1,2] 中的List 被替换为f

@@@

  Level 1 处换头, {} 最外这一层是Level 0, 里面在加几个List, 这些List 就是Level 1

\#

   \#1 的别名，第一参 

\#n

  \#1, #2, #3 第一二三参

\#0 

  函数本身

#name

  命名参数是和“联合” (Association)结构一起用的，#name 是 #1[“name"] 的简写。

  这会通过name 对Association 进行取值

  #x &[<|"x" -> a, "y" -> b|>] 输出 a 

\##

  函数所有参数的序列(Sequence) 

 \##n 

  从第n 个起到最后一个，函数所有参数的序列(Sequence)   

```
1
```

  Massage函数的占位符，详见StringTemplate 

Case

  DLLTable = {"MacOSX-x86-64" -> {FileNameJoin[{$InstallationDirectory, 

   "SystemFiles", "Links", "MP3Tools", "LibraryResources", 

   "MacOSX-x86-64"}]}}

  dlls = Cases[DLLTable, ($SystemID -> l_) :> l]

  匹配Pattern，抽出成功匹配的各元素   

Sow Reap

  Reap[Sow[x]] (* {表达式返回值, {收集到的东西放这}} *)

  播种，收割  

First Rest

GatherBy TakeWhile 

Prepend Append AppendTo 

Block Module With 

Catch Throw  

  TesseractToolsImpl.m 

GatherBy

  GatherBy[{1, 2, 3, 4, 5}, OddQ] （*奇数分一组，偶数分一组*）

  GatherBy[{{a, 1}, {b, 1}, {a, 2}, {d, 1}, {b, 3}}, First] (*第一部分相等的分在同一组*)

  按元素的属性分组，聚类。GatherBy 实际上就是用你给的一个函数Map 进去，比较输出值，相等的分在同一组。 

Ceiling

  上取整 

Round

  给出最接近的整数(五舍，五点一入)





## Scan

   p.112 Power Programming With Mathematica 

  Scan[Print, {1, 2}] 函数本身没有返回值，函数有副作用。除这两点外和Map 一样 

  (*利用Scan 的副作用实现计数*)

  data =Table[Random[],{100}]; (*一百个包含0～1之间的实数List*)

  hint = Table[0,{5}] (* List[0,0,0,0,0] *)

  Scan[ hint[[Ceiling[# 5]]]++&, data ]

  (*Ceiling[5 #] 5 * 0~1之间的实数，得到0~5 之间的实数，Ceiling 上取整，得到0 ~ 5 之间的整数*)

  (* a++ 先返回a, 然后a = a + 1*)

  hint  

  

  myOddQ[x_] := ( Print["debug:" <> TextString@{x, OddQ[x]}]; OddQ[x] ) (*打印调试信息的小技巧*)

  And @@ myOddQ /@ {1, 2, 3} (*Apply 替换Head, f@@{1,2} List[1,2] 中的List 被替换为f*)

  Scan[If[myOddQ[#], True, Return[False] ] &, {1, 3, 5}] === Null 

  (*Scan 除非主动Return 否则返回值是Null 利用这点进行逻辑判断*)  

Throw and Catch 

   p.117 Power Programming With Mathematica 

  从内层循环返回Throw 

  Catch 捕获？  

TakeWhile

sameQ :=(Length[#1 [Intersection] #2] == Length[ #1])&

sameQ[{1,2,3}, {1,3,2}]

用交集来判断集合是否相等？

GeneralUtilities`PrintDefinitions[BinLists]

Information[BinLists]

??GeneralUtilities`*

SetDirectory@NotebookDirectory[];

Get@FileNameJoin[{(*ParentDirectory[]*)NotebookDirectory[],"std.wl"}];

Names["Std`*"]

(*Names["Std`Private`*"]*)

(*??Std`bomFreeQ*)

ScientificForm

xx?AtomQ 原子表达式(不能在拆分成子表达式了) 

 {{x1,x2},{x3,x4}}/.{x_?AtomQ,y_}->f[x,y]

   {f[x1,x2],f[x3,x4]}


{{2,2},{2,2}}/.x:{2..}:>(x/._Integer?(#==2&)->3)

Cases[{1,2,"ab","cd",x,y},_String]

(*closure 闭包, 内部含有记数器的函数*)

add = Module[{y}, y = 0; Function[x, y = y + x]];

add /@ {1, 2, 3}

特殊键盘字符的表示

  tutorial/StructuralElementsAndKeyboardCharacters

RGBColor[0.952941, 0.67451, 0.227451, 1]

teal blue 蓝绿色 w3.css https://[www.w3schools.com/w3css/default.asp](http://www.w3schools.com/w3css/default.asp)

## Tooltip 指针提示

Quiet 安静，不要输出任何打印

\#

 pure function 的第一参

\#0

   代表纯函数本身

\#n

 第n 参

\#1,#2,#3

   传入的第一参，第二参， ...

  sameQ :=(Length[#1 \[Intersection] #2] == Length[ #1])& (* 用交集来判断集合是否相等？ *)

  sameQ[{1,2,3}, {1,3,2}]

用交集来判断集合是否相等？

\##

  SlotSequence

  所有传入参数

  \##&[a,b,c]

​    Sequence[a,b,c]

​      Sequence 类似 ___ (*0或多Sequence*)

\##2

   所有传入参数，略过第2 个之前的参数

&

   前面是一个匿名函数

   &  的优先级非常低  

Function[body]

   等价于 body &

   body的计算结果就是返回值

   Function[{a,b..}, body]

​    多参函数

[[]]

   see ?Part

/@

   Map[f, expr]

   

@@

   see ?Apply

@@@

   Apply at level 1

​     f @@@ {{a, b, c}, {d, e}}

​     {f[a, b, c], f[d, e]}

$

   系统定义符号以大写字母或$ 开头。

` 

   指定精度

​     5.0`4 ^ 73

​     Precision

/.

   ReplaceAll   expr/.rules

   applies a rule or list of rules in an attempt to transform each subpart of an expression expr. 

   1 + x^2 + x^4 /. x^p_ -> f[p]

   1 + f[2] + f[4]

   

/;

   Condition   patt /; test

   is a pattern which matches only if the evaluation of test yields True. 

   (*Replace all elements which satisfy the condition of being negative:*)

   {6, -7, 3, 2, -1, -2} /. x_ /; x < 0 -> w 

===, =!=

   SameQ, UnsameQ

:->(*仅表示形状*)

  ref/character/RuleDelayed

  RuleDelayed (:>, :>)

  输入：Esc + :> + Esc



## .

### 一个任意字符，除换行外

```
RegularExpression["."]
```



## ..

  ### 重复1 或多

## ...

 ### 重复0或多次

## _

  Blank

### 一个任意表达式

  symble_Head

​    前面给出名字，后面给出类型

## __

  BlankSequence

### 一个或多个表达式

___

  BlankNullSequence

  0 或多

Longest[p]

  is a pattern object that matches the longest sequence consistent with the pattern p.

  贪心匹配

Shortest[p]

  Shortest[__ ~~ "\n\n"]

  is a pattern object that matches the shortest sequence consistent with the pattern p. 

Optional (:)

  f[x_, y_: 0] := {x, y}

​    y 有一个默认值

OptionsPattern

OptionValue

  有点类似特定命名空间下的枚举值

<|...|>

  Association

   Hash表

  represents an association between keys and values.

_&

  Array[_&,3] 

   {_,_,_}

 **howto/MapAFunctionOverAList**

前缀形式还好，若想带多个参数，可以用Apply：Apply[f, {x, y}] 等价于f@@{x, y}，即f[x, y]。



## Span (;;)

### 连续或不连续索引用于取值 



## Graph



### 近义词图

```
words=DictionaryLookup["wol*"];
Flatten[Map[(Thread[#\[DirectedEdge]DeleteCases[Nearest[words,#,3],#]])&,words]];
Graph[%,VertexLabels->"Name",ImageSize->450]
```



## Sort

Sort 的第二参是排序函数，Sort 会把List 里的元素一个个的传进去，**排序函数要做的是从元素里提取出可供排序的值**

```mathematica
ReverseSortBy[wordlist, Values[#][[1]] &];
Sort
```









### CompleteGraph

> 全结点全连接的图



SetDirectory[NotebookDirectory[]];
j = Import[FileNameJoin[{$HomeDirectory,"/Documents/GitHub/ebmac/","tiny.json"}],"JSON", "Compact"->False]
jj = Import[FileNameJoin[{$HomeDirectory,"/Documents/GitHub/ebmac/","guoyu.json"}],"RawJSON"];
ass=Import["[Kamigami] Shoujo Shuumatsu Ryokou - 01 [1080p x265 AAC].ass","Text",CharacterEncoding->"UTF8"];
(*终末少女的旅行中日字幕，诸神字幕组*)
lines=StringSplit[ass,RegularExpression["(?m)^"]];  (*(?m)^换行符*)
jps=Reap[lines /. x_String?(StringMatchQ[#,"Dialogue"~~__~~",TEXT-JP"~~__]& ):>(Sow[x]);Nothing]//Flatten;
chs=Reap[lines /. x_String?(StringMatchQ[#,"Dialogue"~~__~~",TEXT-CN"~~__]& ):>(Sow[x]);Nothing]//Flatten;
(* MMA 速查文档 https://mresources.github.io/tutorial/ *)
(* MMA 建站代码 https://github.com/mresources/tutorial *)
(* MMA 建站文档 https://www.wolframcloud.com/objects/b3m2a1.docs/BTools/ref/WebSiteBuild.html *)
(* MMA 帮助文档快速生成 https://zhuanlan.zhihu.com/p/113333655 *)
(* ASS SRT 字幕，音视频开发  https://www.cnblogs.com/tocy/ *)
 (*让语句返回值为Nothing，然后存在List 里面的Nothing 就自已消失了*)
(* MapIndexed 带index 的map 第一参： #1 列表元素，第二参： #2 { index } *)
(* RegularExpression 正则表达式 *)
(* 字符串格式化 StringTemplate *)
(* AppExecute["ListPackages","BTools"]~Take~5 https://github.com/b3m2a1/mathematica-BTools/wiki/BasicUsage *)
debug:=GeneralUtilities`PrintDefinitions
(*SystemOpen[DirectoryName[AbsoluteFileName["vis-à-vis-dictionary.com.png"]]]*)
(*"guoyu.json"*)(*"tinyGuoYuDic.json"*)(*"tiny.json"*) 
(*
	Computational Linguistics 计算语言学用户组  Classifying Japanese characters from the Edo period  
https://community.wolfram.com/groups/-/m/t/1221098
	  https://github.com/FooSoft/zero-epwing
提取epwin 学研国语词典的活用表
	  '形式名 活用形 下接語例\n' 根据这个标记识别目标
utf8编码查询
	  http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=%E4%81%A0

GeneralUtilities`PrintDefinitions[BinLists] (*Mathematica 黑魔法：查看内部函数定义*)

Scan
	p.112 Power Programming With Mathematica
	Scan[Print,{1,2}] 函数本身没有返回值，函数有副作用。除这两点外和Map 一样
	(*利用Scan 的副作用实现计数*)
	data=Table[Random[],{100}];(*一百个包含0～1之间的实数List*)
      hint=Table[0,{5}] (*List[0,0,0,0,0]*)
	   Scan[hint[[Ceiling[# 5]]]++&,data]
   (*Ceiling[5 #] 5*0~1之间的实数，得到0~5 之间的实数，Ceiling 上取整，得到0~5 之间的整数*)
	   (*a++ 先返回a,然后a=a+1*)
   hint

myOddQ[x_]:=(Print["debug:"<>TextString@{x,OddQ[x]}];OddQ[x]) (*打印调试信息的小技巧*)
	And@@myOddQ/@{1,2,3} (*Apply 替换Head,f@@{1,2} List[1,2] 中的List 被替换为f*)
	Scan[If[myOddQ[#],True,Return[False]]&,{1,3,5}]\[Equal]Null
(*Scan 除非主动Return 否则返回值是Null 利用这点进行逻辑判断*)

Throw and Catch
		p.117 Power Programming With Mathematica
		从内层循环返回Throw
		Catch 捕获？

Input Stream
输入流
StringToStream

文字识别
ref/TextRecognize
guide/LowLevelNotebookProgramming

语音合成
AudioPlay[SpeechSynthesize["this is some text"]];

 单词IPA发音
https://mathematica.stackexchange.com/questions/34391/split-lingusticipa-at-words-unique-sounds
https://mathematica.stackexchange.com/questions/32148/find-a-words-linguistic-pronunciation

重载系统函数的黑科技
https://mathematica.stackexchange.com/questions/18187/overloading-second-argument-of-countrydata
[dictionary.com](https://www.dictionary.com/e/word-of-the-day/)

未文档函数的黑科技
https://mresources.github.io/tutorial/reference-guides/undocumented-contexts/system-%2A.html

[dictionary.com](https://www.dictionary.com/e/word-of-the-day/)

# happy 

[ **hap**-ee] PHONETIC RESPELLING

/ˈhæp i/IPA

SendMail\[LongDash]发送电子邮件
GoogleTranslate-谷歌翻译
字幕
[英日]https://horriblesubs.info
[动画字幕搜索引擎-中日](https://github.com/windrises/dialogue.moe)
[诸神字幕组][少女终末旅行 Shoujo Shuumatsu Ryokou][简繁外挂字幕][01-12][WEBrip][1080P]
	  [深入理解计算机系统视频及字幕](https://github.com/EugeneLiu/translationCSAPP)
		str 字幕

弹系统对话框，选颜色、录音、保存文件什么的
SystemDialogInput 
文本按句分割
TextSentences
文本按词分割
TextWords
单词原型
WordStem
识别语言类型
LanguageIdentify
文本翻译
WordTranslation
自然语言理解
Natural Language Understanding

文本搜索，这就更有意思了
TextSearch
文件系统Map，这就有意思了
FileSystemMap
可以递归的获取所有文件名
FileNames

show biggest file or dirctory on mac
sudo du-sh* |grep-E "\dG\[CloseCurlyDoubleQuote]

查慧林音义 仁

find . -type f | xargs cat | grep "<p>.*仁.*<span class='note-inline'>(\[CloseCurlyDoubleQuote]
仁者(而親反周禮云德一曰仁鄭玄曰愛人及物曰仁上下相親曰仁釋名仁者忍也好生惡煞善惡含忍也)。

content=Drop[Transpose[Import["~/Downloads/19162.csv"]],2];

sorted=GatherBy[DeleteCases[DeleteCases[Flatten[content],""],"="],StringTake[#,StringPosition[#,"="][[1]][[1]]]&];

tab=OutputForm[TableForm[sorted]];

Export["~/Downloads/19162.txt",tab]

SetDirectory@NotebookDirectory[];
(*strm=OpenRead["学研国語大辞典ku00.txt",Method\[Rule]{"File",CharacterEncoding\[Rule]"ShiftJIS"}];*)
shiftj=FromCharacterCode[BinaryReadList@"学研国語大辞典ku00.txt","ShiftJIS"];
Characters@shiftj//Take[#,{8}]&
file="学研国語大辞典ku00utf8.txt";
stream=OpenWrite[file,CharacterEncoding\[Rule]"UTF-8"];
WriteString[stream,shiftj];
Close@stream;

https://mathematica.stackexchange.com/questions/75797/how-to-export-speak-output/76841#76841
URLExecute["http://tts-api.com/tts.mp3",{"q"\[Rule]gymString}]
URLSave["http://tts-api.com/tts.mp3","gym.mp3","Parameters"\[Rule]{"q"\[Rule]gymString}]
Run["say -v Zarvox "<>gymString]
Run["say -o gym.mp4 -v Zarvox "<>gymString]

*)





## Linear Math



![image-20200523190009649](C:\Users\echod\AppData\Roaming\Typora\typora-user-images\image-20200523190009649.png)





# Image



### 清理图片



```mathematica
clean[i_]:=i//ColorNegate//DeleteSmallComponents[#, 20]&
i//clean
```



### 倾斜校正

```mathematica
clean[i_]:=i//ColorNegate//DeleteSmallComponents[#, 20]&
preserveHLine[i_]:=i//ImageConvolve[#,{{1},{-1}}]&//DeleteSmallComponents//
	Binarize[#,.999]&//DeleteSmallComponents[#, 7]&
lines = preserveHLine[i//clean]//ImageLines[#,0,1]&
HighlightImage[i,lines]
skewAngle[i_]:=i//clean//preserveHLine//ImageLines[#,0,1]&//#[[1]]&//#[[1]]&//#[[2]]-#[[1]]&//Complex@@#&//Arg@#&
correctSkew[i_]:=With[{radian=i//skewAngle,
	iClean=i//clean},
ImageRotate[iClean,-radian]
]
skewAngle[i]
correctSkew[i]
```







### 填充到指定宽度

```mathematica
padRight[image_,width_]:=PadRight[#, width,1]& /@ (ImageData@image)//Image
```

```
# 同宽度的图片合成一张图
ImageAssemble
```







# 汉字画图

```mathematica
BoundaryDiscretizeGraphics[
 Text[Style["国", FontFamily -> "Microsoft YaHei", 
   FontSize -> 12]], _Text]
```



# 运行python

- https://mathematica.stackexchange.com/questions/15647/is-there-a-way-to-run-python-from-within-mathematica

```mathematica
path="D:\\usr\\python.exe";
p=StartProcess[{path,"-i"}];(*the'-i' argument is important*)
cmd="print('hello')";(*or any valid python expression*)
Pause[1];(*important!!!*)
WriteLine[p,cmd];
out=ReadString[p,EndOfBuffer]
KillProcess@p;
```



```
process = StartProcess[$SystemShell];
WriteLine[process, "cd /home/path/to/folder/"]
Now, I run the program

WriteLine[process, "./prog"];
If i want to insert some input, I use the same logic

WriteLine[process, "String with input"];
Finally, I kill the process

KillProcess@process;
```



