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



