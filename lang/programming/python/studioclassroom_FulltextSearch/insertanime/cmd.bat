rem ffmpeg -i t.mp3 -c:v h265 -hls_time 1 out\p.m3u8


rem ffmpeg  -y -ss 00:01:12.960 -to 00:01:14.640 -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -c:v h264  out\p.m3u8

rem ffmpeg  -y -ss 00:01:12.960 -to 00:01:14.640 -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -c:v h264  1.ts

ffmpeg -y -f mjpeg -ss 0.1 -t 0.001 -s 675*432 1.jpg

cmd.exe