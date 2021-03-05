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

