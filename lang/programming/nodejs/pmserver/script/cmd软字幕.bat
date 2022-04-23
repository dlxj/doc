ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
cmd.exe