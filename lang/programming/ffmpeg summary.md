

```bash
ffmpeg -i input.mkv -map 0:s:0 out.ass

这将下载第一个字幕轨。如果有几个，使用0:s:1下载第二个，0:s:2下载第三个，等等。

字幕格式是srt或者ass修改后缀名就可以了；

 

法二、视频添加提取字幕：

ffmpeg -i F:\472ca95769ddf65f288ed6da2602ef89.mp4 -i F:\lc.srt -map 0:0 -map 0:1 -map 1 -c:a copy -c:v copy -c:s copy F:\video.mkv

ffmpeg -i F:\video.mkv -vn -an -codec:s:0 srt F:\subtitle.srt
```



