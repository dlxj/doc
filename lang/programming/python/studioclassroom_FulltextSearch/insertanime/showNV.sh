#/bin/bash
for i in encoders decoders filters; do
    echo $i:; ffmpeg -hide_banner -${i} | egrep -i "npp|cuvid|nvenc|cuda"
done