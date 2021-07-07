

import os,sys,subprocess
import re
import glob
import chardet
import MeCab
tagger = MeCab.Tagger()

import platform
from joblib import Parallel, delayed
from multiprocessing import cpu_count

print("cpu count: {0}".format(os.cpu_count()))



def OSXQ():
    return platform.system() == 'Darwin'


def allfname(root, ext):
    names = os.listdir(root)
    names = list(map(lambda ns:os.path.basename(ns),names))
    return names


def cut(fname, idx):
    
    videoname = fname
    frtname = f"{fname}.srt"
    fname = os.path.join( root, fname )
    videopath = os.path.join( root, videoname )
    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
    out_text = out_bytes.decode('utf-8')

    print("### idx {0} doen.", idx)

    animename = 'Danganronpa'
    seasion = '01'


if __name__ == "__main__":

    """
    pg_ctlcluster 13 main start       # echo pg

    docker exec -it centos7PG10 /bin/bash
    systemctl restart postgresql-13   # echo docker pg
    """

    
    # return Parallel(n_jobs=os.cpu_count(), verbose=10)(delayed(f)(ts, i) for i in range(len(ts)-1))  # 子循环多核并发执行，加速运算

    print("start")

    OS = ''
    try:
      test = os.uname()
      if test[0] == "Linux":
        OS = "Linux"
      elif test[0] == 'Darwin':
        OS = "OSX"
    except Exception as e:
      OS = "Windows"


    print(f"OS: {OS}")

    #begin, end = parseSrtTime("00:01:12,960 --> 00:01:14,640")

    #host = '111.229.53.195'
    host = '209.141.34.77'
    port = 5432

    #createAnimeDB(host, port)

    
    root = r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    if OS == "Linux":
      root = r"/mnt/videos/anime/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    if OS == "OSX":
      #root = r"/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
      root = r"/Users/olnymyself/Downloads/d"

    print( f"root path: \n{root}" )

    fnames = allfname(root, 'mkv')

    fnames = sorted(fnames, key=lambda s: s, reverse=False)  # sort by name

    ret = Parallel(n_jobs=os.cpu_count(), verbose=10)(delayed(cut)(fnames[i], i) for i in range(len(fnames)-1))

    # for fname in fnames:
    #   videoname = fname
    #   frtname = f"{fname}.srt"
    #   fname = os.path.join( root, fname )
    #   videopath = os.path.join( root, videoname )
    #   out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
    #   out_text = out_bytes.decode('utf-8')

    #   animename = 'Danganronpa'
    #   seasion = '01'
