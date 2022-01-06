
import os,sys,subprocess,re

videopath = 'D:/Downloads/[Skytree][火影忍者][NARUTO][001][GB_JP][X264_AAC][960P][DVDRIP][天空树双语字幕组][V2].mp4'

# ffmpeg -skip_frame nokey -i 1.mp4 -vsync 0 -f image2 tmp/%06d.png
    # 高清关键帧  缺点：不知道时间

# ffmpeg -i 1.mp4 -vsync 0 -f image2 tmp/%09d.png

# out_bytes = subprocess.check_output([r"ffmpeg", "-i", videopath, "-skip_frame", "nokey", "-vsync", "0", "-f",
#                                      "image2", "tmp/%06d.png"
#                                      ])

# out_bytes = subprocess.check_output(["ffprobe", "-loglevel", "error", "-select_streams", "v:0", "-show_entries", "packet=pts_time,flags", "-of", "csv=print_section=0", "1.mp4"])
# out_text = out_bytes.decode('utf-8')
# out_text = re.sub(r"\r\n", "\n", out_text, flags=re.UNICODE)
# out_text = out_text.strip().split('\n')

"""
ffmpeg -skip_frame nokey -i 1.mp4 -r 1000 -vsync 0 -frame_pts true tmp/out%d.png
skip_frame tells the decoder to process only keyframes. -vsync 0 (in this command) preserves timestamps. -frame_pts sets the numeral portion of the output image filename to represent the timestamp. The interpretation of the number requires you to know the framerate e.g. if the framerate is 30 then an image name of out75 corresponds to a timestamp of 75/30 = 2.50 seconds. You can add -r 1000 if you want numbers to represent milliseconds.
"""

out_bytes = subprocess.check_output(["ffprobe", "-loglevel", "error", "-select_streams", "v:0", "-show_entries", "packet=pts_time,flags", "-of", "csv=print_section=0", "1.mp4"])
out_text = out_bytes.decode('utf-8')
out_text = re.sub(r"\r\n", "\n", out_text, flags=re.UNICODE)
out_text = out_text.strip().split('\n')

a = 1

"""
所有关键帧的时间，带K_ 的是关键帧
ffprobe -loglevel error -select_streams v:0 -show_entries packet=pts_time,flags -of csv=print_section=0 1.mp4

You get some output like this...

0.000000,K_
0.167000,__
0.083000,__
0.042000,__
"""
