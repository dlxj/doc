ffmpeg -y -itsoffset -2.2 -i 1.mp4 -i 2.mkv -map 0:v -map 1:a:0 -vf subtitles=1.srt advance2second_hardjp.mp4
cmd.exe