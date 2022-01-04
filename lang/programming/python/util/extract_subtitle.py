
import os,sys,subprocess

videopath = ''

out_bytes = subprocess.check_output([r"ffmpeg", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3",
                                     "-ar", "44100", "-ac", "2", "-b:a", "192k",
                                     "tmp.mp3"])

out_text = out_bytes.decode('utf-8')
