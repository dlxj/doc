```bash

# 提前2.2 秒，嵌入日文作为硬字幕  # 试转一小段看对不对，经实验 -2.2 比较好
ffmpeg -y -itsoffset -2.2 -i 1.mp4 -ss 00:01:49.000 -to 00:05:00.000 -vf subtitles=1.srt advance2second.mp4

# 先提前2.2 秒，再嵌入日文软字幕
ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv

# 1 是pokemon台版中文硬字幕mp4，2 是日文软字幕mkv，中硬比日软要慢2.2 秒左右
```



# subtitles 绝对路径的写法很特殊

```
ffmpeg -y -itsoffset -2.2 -i "E:\t\1.mp4" -vf  "subtitles='E\:\\t\\1.srt'"  advance2second_hardjp.mp4
```





```
ffmpeg -i "G:\棒球英豪国日双语1080p\[棒球英豪].[zhbconan][Touch][001][HDTVRip][1440x1080][AVC_AAC_AC3][CHS&JPN](ED2000.COM).mkv" -map 0:s:0 out.srt
```

```
ffmpeg -i "G:\棒球英豪国日双语1080p\[棒球英豪].[zhbconan][Touch][001][HDTVRip][1440x1080][AVC_AAC_AC3][CHS&JPN](ED2000.COM).mkv" -map 0:s:0 out.lrc
```



```
ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.lrc
```





```bash
ffmpeg -i input.mkv -map 0:s:0 out.ass

这将下载第一个字幕轨。如果有几个，使用0:s:1下载第二个，0:s:2下载第三个，等等。

字幕格式是srt或者ass修改后缀名就可以了；

 

法二、视频添加提取字幕：

ffmpeg -i F:\472ca95769ddf65f288ed6da2602ef89.mp4 -i F:\lc.srt -map 0:0 -map 0:1 -map 1 -c:a copy -c:v copy -c:s copy F:\video.mkv

ffmpeg -i F:\video.mkv -vn -an -codec:s:0 srt F:\subtitle.srt
```



# insert anime



```
pip install chardet

```





```

# ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p06_executing_external_command_and_get_its_output.html

import subprocess
import re


# out_bytes = subprocess.check_output([r"ffmpeg", "-i", "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv", "-map", "0:s:0", "out.srt"])
# out_text = out_bytes.decode('utf-8')

def readstring(fanme):
    with open(fanme, "r", encoding="utf-8") as fp:
        return fp.read()

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)


if __name__ == "__main__":
    strs = "\n"+readstring("out.srt")+"\n"
    iters = re.finditer(r"\n\d+\n", strs, re.DOTALL)
    poss = [ i.span() for i in iters ]


    chinese = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        
        n = strs[start:end]

        content = None
        if i == ( len(poss) - 1 ):
            content = strs[ end : len(strs) ]
        else:
            content = strs[ end : poss[i+1][0] ]
        
        time = content.strip().split('\n')[0]
        content = content.strip().split('\n')[1]
        subtitle = re.compile(r'size=.+>(.+?)\<\/font\>').findall(content)[0]
        subtitle = subtitle.replace('<b>','').replace('</b>','')
        if len( unchinese_remove(subtitle) ) > 0:
            chinese.append( subtitle )


    print("hi,,,")





# "</font>"



```



# inject subtitle
- https://www.dyxmq.cn/other/add-subtitles-by-ffmpeg.html

```
给视频添加字幕的操作非常简单，执行一行命令即可：

ffmpeg -i video.mkv -i subtitle.ass -c copy output.mkv
替换掉已有字幕：

ffmpeg -i input.mkv -i input.ass -c copy -map 0 -map -0:s -map 1 output.mkv
参数说明：

-map 0：选择第一个输入文件的所有流
-map -0:s：删除第一个输入文件中的subtitles流（即删除字幕）
-map 1：选择第二个输入文件中的流
```



# make mkv

```
ffmpeg -y -i 1.mp4 -map 0:v -map 0:a:0 -ss 00:01.500 -c copy out.mp4
	# -map 0:v 复制第0 个输入的视频(v)
	# -map 0:a:0 复制第0 个输入的第 0个音频(a)
	# -c copy 指定编码为与原编码一至，既不转换
	
ffmpeg -y -i out.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
	# 复制第0 个输入的视频(v)
	# 复制第1 个输入的第 0个音频(a) 作为第一条音轨
	# 复制第0 个输入的第 0个音频(a) 作为第二条音轨
	# 复制第2 个输入作为字幕，编码为 srt
	
cmd.exe
```





# tutorial



- https://blog.csdn.net/qq_31622015/article/details/109048766

  > 全全全

```
ffmpeg -i AmericanCaptain.mkv -map 0:v -vcodec copy -map 0:a:1 -acodec copyAmericanCaptain.mp4 -strict -2

命令说明：
0:v 代表提取所有视频流（一般视频流只有1路）
0:a:1 代表提取第2路音频流

这个MKV是有2个音轨的，第一个为英文，第二个为中文，若不清楚原文件的信息，输入ffmpeg-i AmericanCaptain.mkv查看。

```



```
ffmpeg用法说明
-i : 输入文件名
-map : 参数格式, 输入文件 index:各种流index:channels index , 即输入文件的索引(从0开始算起), 接着此文件中的音/视频等流的index, 再接着是channels的Index, 所有的index都是从0算起的. e.g. 0:1说明test.mkv文件中的第2条音频流的数据
-codec:a aac , 即音频编解码器用aac
-codec:a copy, 即不做重新编码, 直接拷贝
ffmpeg -codecs 可列出ffmpeg支持的所有编解码器
ffmpeg -formats 可列出ffmpeg支持的所有格式
ffmpeg -encoders/decoders 可列出ffmpeg支持的所有编码器/解码器
```



```
方法四：使用 FFmpeg concat 过滤器重新编码（有损）
语法有点复杂，但是其实不难。这个方法可以合并不同编码器的视频片段，也可以作为其他方法失效的后备措施。
ffmpeg -i input1.mp4 -i input2.webm -i input3.avi -filter_complex '[0:0] [0:1] [1:0] [1:1] [2:0] [2:1] concat=n=3:v=1:a=1 [v] [a]' -map '[v]' -map '[a]' <编码器选项> output.mkv
如你所见，上面的命令合并了三种不同格式的文件，FFmpeg concat 过滤器会重新编码它们。 注意这是有损压缩。
[0:0] [0:1] [1:0] [1:1] [2:0] [2:1] 分别表示第一个输入文件的视频、音频、第二个输入文件的视频、音频、第三个输入文件的视频、音频。 concat=n=3:v=1:a=1 表示有三个输入文件，输出一条视频流和一条音频流。 [v] [a] 就是得到的视频流和音频流的名字，注意在 bash 等 shell 中需要用引号，防止通配符扩展。

```



## 有用

```
6.合并、提取音视频
提取视频：
ffmpeg -i in.mp4 -vcodec copy -an v.mp4
-vcodec copy: 保持原编码格式不变
-an ：用来静音，剔除音频
提取音频：
ffmpeg -i in.mp4 -vn -acodec copy a.m4a
有些视频具有多个音频流 -map 0:3 增加参数来提取指定音频流
合并音视频：
ffmpeg -i a.m4a -i v.mp4 -c copy out.mp4

7.截取、连接音视频
截取音频
ffmpeg -i in.mp3 -ss 00:01:0 -to 00:01:10 -acodec copy out.mp3
ffmpeg -i in.mp3 -ss 00:01:00 -t 10 -acodec copy out.mp3
-ss 00:01:00 -to 00:01:00 ： 起始时间和结束时间
截取视频:
ffmpeg -i in.mp4 -ss 00:01:00 -to 00:01:10 -c copy out.mp4
ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -c copy out.mp4
ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -c copy -copyts out.mp4 (用这一种)
连接多个视频:（参数是一样的，格式、宽高和码率）
ffmpeg -i “concat:01.mp4|02.mp4|03.mp4” -c copy out.mp4
推荐使用图形界面：
Avidemux，专门用来剪切和合并视频视频（开源）
连接多个音频:
？

8.截图、水印、动图
截图:
ffmpeg -i in.mp4 -ss 5 -vframes 1 img.jpg
-ss 5：第五秒
视频添加水印:
ffmpeg -i in.mp4 -i logo.png -filter_complex “overlay=20:20” out.mp4
-filter_complex: 用来添加滤镜
“overlay=20:20” : 水印的位置
制作gif动图:
ffmpeg -i in.mp4 -ss 7.5 -to 8.5 -s 640x320 -r 15 out.gif

9. 录屏、直播
录屏:
ffmpeg -f gdigrab -i desktop rec.mp4
推荐软件：OBS studio 免费、开源、强大
直播:
ffmpeg -re -i rec.mp4 按照网站要求编码 -f flv “你的rtmp地址/你的直播码”
```



## 有用2

```
C# FFmpeg合并多个音频文件，并指定每段音频的插入时间。
合成音频的FFmpeg命令为：

ffmpeg -i 11.wav -i 13.wav -filter_complex "[0]adelay=1s:all=1[0a];[1]adelay=26s:all=1[1a];[0a][1a]amix=inputs=2[a]" -map "[a]" output.wav
不知道具体啥意思，大概猜测一下，
-i <fileName> 输入文件的路径，有几个文件就几个-i命令
[0]adelay=1s:all=1[0a] [0]和[0a]指的是第几个文件，索引从0开始，adelay=1s 从音频的第一秒开始插入，默认是毫秒，adelay=1000, 如果加后缀s，则指的秒数，此时不支持小数位写法。（4.2版本以下不支持1s这种写法），all：Use last set delay for all remaining channels. By default is disabled. This option if enabled changes how option delays is interpreted.
amix=inputs=2 2指的是一共有几个文件
output.wav 输出文件的路径或者文件名
```



## 超有用

- https://blog.lintian.co/archives/70

```
# 复制音轨/字幕（流拆分）
ffmpeg -i The.Outpost.2020.WEB.H.265.2160p.mkv -map 0:v -map 0:a:1 -map 0:s:2 -c copy tmp.mkv
# 添加内封字幕（流合成）
ffmpeg -i The.East[1080p][H264].mp4 -i English.eng.srt -i Dutch.dut.srt -map 0 -map 1 -map 2 -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=eng -metadata:s:s:0 title=English -metadata:s:s:1 language=dut -metadata:s:s:1 title=Dutch test.mp4

```

- `-i 文件名`：指定输入文件，可以是视频，也可以是音频/字幕文件。
- `-map [0-n]:[v:a:s]:[0-n]`：流选择器
  第一个数字是`-i`的文件序号，且数字从`0`开始。
  第二个字母是流的类型，v：视频轨、a：音轨、s：字幕轨（可省略，未指定则代表所有流）
  第三个数字是流编号，从`0`开始计数，且每种流都是独立计数（可省略，未指定则代表所有流）
- `-c`：指定编码
  `-c copy`：仅复制视频源数据并进行封装，不会对视频进行编码。
  `-c:[0-n]:[v:a:s]:[0-n]`：同`map`一样，可以指定流。
  对于视频编码来说，一般的整理用`copy`即可，需要二次编码时则可指定为`h264`、`hevc`等。
  对于字幕编码来说，一般`srt`字幕需指定为在`mp4`中的编码为`mov_text`、`mkv`中`srt`文件编码为`srt`[[1\]](https://blog.lintian.co/archives/70#fn1),`ass`文件为`ass`。
- `-metadata`：指定数据类型，`K` `V`形式。一般用于设置流的语言和标题
  `-metadata:s:s:0 language=eng`：设置第一个字幕的语言为英语。



## 实在是高

https://www.zhangwenbing.com/blog/ffmpeg/S1uzUUNc8Cf

- ffmpeg音频合成命令全集



```
ffmpeg \
    -i source.mkv \
    -i Logo_White.ico \
    -filter_complex \
    "[0:v][1:v]overlay[logo];\
    [logo]ass=source.ass[sub]" \
    -map [sub] \
    -map 0,0 \
    output.final.mp4


首先看到命令中有两个输入，一个是视频文件，为 input0，一个是 logo 图像，为 input1.
filter_complex 滤镜的参数里面 [0:v]的0是 input0，v代表处理的是视频而不是音频，处理音频的待会儿再讲
整体来看，[0:v][1:v]overlay[logo]是一个2输入1输出的管子，管子把 input1 的视频流（此处为一张图）叠加到 input0 的上面，出来的产品叫做[logo]
然后下一句[logo]ass=source.ass[sub]中，可以把中间那个ass滤镜当做一个1输入1输出的管子，这个管子对每个视频流进行处理，在视频上打上字幕，出来的产品叫做[sub]
最终把这个[sub] 映射到 output.final.mp4 上面

```



## 字幕调整时间

pokemon 台版中文硬字幕比 amazon pokemon 版的字幕慢了两秒，

所以要把它的整个所有流（包括视频和音频流）都提前两秒，-itsoffset -2  参数可以作到这一点，假设原视频是60 秒，调整后视频也还是60 秒，但是最后2 秒无了，变成最后一帧延长两秒的静止画面。

```
# 提前2.2 秒，嵌入日文作为硬字幕
ffmpeg -y -itsoffset -2.2 -i 1.mp4 -ss 00:01:49.000 -to 00:05:00.000 -vf subtitles=1.srt advance2second.mp4
 
 # 试转一小段看对不对，经实验 -2.2 比较好
```

```
# 先提前2.2 秒，再嵌入日文软字幕
ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
```



### subtitles 绝对路径的写法很特殊

```
ffmpeg -y -itsoffset -2.2 -i "E:\t\1.mp4" -vf  "subtitles='E\:\\t\\1.srt'"  advance2second_hardjp.mp4
```





```
vf 烧录字幕时会把字幕文件和视频流时间轴零点对齐，可以先调字幕文件时间轴，然后烧录，比如下面这两行，只给第 2 分钟的视频烧录字幕，

$ ffmpeg -itsoffset -00:01:00 -i rawsub.ass -map 0 -c ass sub.ass
$ ffmpeg -ss 00:01:00 -to 00:02:00 -i rawvideo.mp4 -map 0 -filter:v ass=f=sub.ass -c:v h264 -c:a copy video.mp4



```

### -itsoffset

The itsoffset option applies to all streams embedded within the input file. Therefore, adjusting timestamps only for a single stream requires to specify twice the same input file.

```
ffmpeg -i INPUT -itsoffset 5 -i INPUT -map 0:v -map 1:a OUTPUT
```

adjusts timestamps of the input audio stream(s) only.

#### positive offset

```
ffmpeg -itsoffset 5 -i INPUT OUTPUT
```

delays all the input streams by 5 seconds.

If the input file was 60 seconds long, the output file will be 65 seconds long. The first 5 seconds will be a still image (first frame).

#### negative offset

```
ffmpeg -itsoffset -5 -i INPUT OUTPUT
```

advances all the input streams by 5 seconds.

This discards the first five seconds of input. However, if the input file was 60 seconds long, the output file will also be 60 seconds long. The last 5 seconds will be a still image (last frame).



# 精准剪切

```
造成这些问题的原因是ffmpeg无法seek到非关键帧上
ffmepg升级最新版
加上参数-accurate_seek -avoid_negative_ts 1
-- 自己例子
ffmpeg -ss 00:00:00 -to 00:00:01 -accurate_seek -i out.mp4 -vcodec copy -acodec copy -avoid_negative_ts 1 -y out-1.mp4
ffmpeg -ss 00:00:30 -to 00:00:52 -accurate_seek -i out.mp4 -vcodec copy -acodec copy -avoid_negative_ts 1 -y out-2.mp4
echo -e "file 'out-1.mp4' \nfile 'out-2.mp4'" >> list.txt
ffmpeg -safe 0 -f concat -i list.txt -vcodec copy -acodec copy -strict -2 -y concat.mp4
```

