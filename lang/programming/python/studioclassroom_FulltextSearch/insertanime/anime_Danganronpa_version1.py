
# ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p06_executing_external_command_and_get_its_output.html

import os,sys,subprocess
import re
import glob
import chardet
import MeCab
tagger = MeCab.Tagger()

import platform

def OSXQ():
    return platform.system() == 'Darwin'


"""
D:\GitHub\doc\lang\programming\postgresql summary.md
    docker exec -it centos7PG10 /bin/bash
        54322 port
    Install PG_Jieba [u](https://github.com/jaiminpan/pg_jieba)

pip install mecab-python3
pip install unidic-lite

pip install xmltodict
GFW
https://www.ishells.cn/archives/linux-ssr-server-client-install
"""


"""

SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
 --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}


CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("include_reading", true)')
  LOOP
    reading = (js -> 'metadata' ->> 'reading');

    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
  END LOOP;

  RETURN array_to_string(total, '');
END;
$func$ LANGUAGE plpgsql IMMUTABLE;


SELECT ja_reading ('有');
-- 

/*
{"{\"value\":\"海\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"ウミ\"}}"}
{"{\"value\":\"1\",\"position\":0,\"force_prefix_search\":false}"}
*/


{
  "force_prefix_search": false,
  "metadata": {
    "reading": "シ"
  },
  "position": 0,
  "value": "する"
}



SELECT string_to_array('xx~^~yy~^~zz', '~^~')
  --> {xx,yy,zz}


"""

"""

https://groonga.org/docs/reference/tokenizers/token_mecab.html

https://github.com/pgroonga/pgroonga/issues/171

My thought has become

CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);

CREATE INDEX idx_tatoeba_jpn ON dict.tatoeba
  USING pgroonga ("jpn")
  WITH (
    tokenizer='TokenMecab("use_base_form", true, "include_form", true, "include_reading", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );
CREATE INDEX idx_tatoeba_eng ON dict.tatoeba
  USING pgroonga ("eng")
  WITH (plugins='token_filters/stem', token_filters='TokenFilterStem');
Then

SELECT * FROM dict.tatoeba
WHERE jpn &@ 'うみ'
ORDER BY pgroonga_score(tableoid, ctid) DESC
LIMIT 10;
But it isn't comparable to 海.
"""

"""

&@ 单关键词的fulltext search

CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);



CREATE INDEX idx_tatoeba_jpn_base_form ON dict.tatoeba
  USING pgroonga ((jpn || ''))
  WITH (
    tokenizer='TokenMecab("use_base_form", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );

CREATE INDEX idx_tatoeba_jpn_reading ON dict.tatoeba
  USING pgroonga ((jpn || '' || ''))
  WITH (
    tokenizer='TokenMecab("use_reading", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );

SELECT * FROM dict.tatoeba
WHERE (jpn || '')       &@~ ja_expand('海') -- search by base_form
   OR (jpn || '' || '') &@~ ja_expand('海') -- search by reading
LIMIT 10;
"""

"""
CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);

CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("include_reading", true)')
  LOOP
    reading = (js -> 'metadata' ->> 'reading');

    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
  END LOOP;

  RETURN array_to_string(total, '');
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION ja_expand (TEXT) RETURNS TEXT AS
$func$
BEGIN
  IF $1 ~ '[\u4e00-\u9fa5]' THEN
    RETURN  $1||' OR '||ja_reading($1);
  END IF;

  RETURN $1;
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

SELECT * FROM dict.tatoeba
WHERE jpn &@~ ja_expand('海')
LIMIT 10;
"""


"""

CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
		LOOP
			reading = (js -> 'metadata' ->> 'reading');
			IF reading IS NULL THEN
					RETURN 0;
      END IF;
		
		END LOOP;
  END LOOP;
	
	RETURN 1;
	
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

"""


"""

自动重连

https://github.com/psycopg/psycopg2/blob/9e6c3322d8640bca7007a222973d87d8ea60057c/lib/pool.py#L103

status = conn.get_transaction_status()
                if status == _ext.TRANSACTION_STATUS_UNKNOWN:
                    # server connection lost
                    conn.close()
                elif status != _ext.TRANSACTION_STATUS_IDLE:
                    # connection in error or in transaction
                    conn.rollback()
                    self._pool.append(conn)
                else:
                    # regular idle connection
                    self._pool.append(conn)
"""


import psycopg2
import psycopg2.extensions as _ext
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#from psycopg2.extensions import ISOLATION_LEVEL_DEFAULT

import sqlite3 as sqlite # Python 自带的

from pymysql import escape_string
import glob

import json
import decimal
import datetime

import xmltodict



class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def writestring(fname, strs):
    with open(fname, "w", encoding="utf-8") as fp:
        fp.write(strs)
        fp.close()

# out_bytes = subprocess.check_output([r"ffmpeg", "-i", "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv", "-map", "0:s:0", "out.srt"])
# out_text = out_bytes.decode('utf-8')

# \u4e00-\u9fa5

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def chinese_remove(s):
    return re.sub(r"[\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def unjp_remove(s):
    return re.sub(r"[^\u0800-\u4e00]", "", s, flags=re.UNICODE)

def unhana_remove(s):
    return re.sub(r"[^\u3040-\u309F^\u30A0-\u30FF]", "", s, flags=re.UNICODE)

def hasHanaQ(s):
    return len( unhana_remove(s) ) > 0

def parseSrtTime(time):
  
  #time = "00:01:12,960 --> 00:01:14,640"
  begin = time.split('-->')[0].strip()
  end = time.split('-->')[1].strip()

  begin = begin.replace(',', '.')
  end = end.replace(',', '.')

  return begin, end

  # if match := re.compile(r'(\d\d):(\d\d):(\d\d),(\d\d\d)').search(begin):
  #   h1 = int(match.group(1))
  #   m1 = int(match.group(2))
  #   s1 = int(match.group(3))
  #   ms1 = int(match.group(4))

  #   totalMs1 = h1 * 3600 * 1000 + m1 * 60 * 1000 + s1 * 1000 + ms1

  #   if match := re.compile(r'(\d\d):(\d\d):(\d\d),(\d\d\d)').search(begin):
  #     h2 = int(match.group(1))
  #     m2 = int(match.group(2))
  #     s2 = int(match.group(3))
  #     ms2 = int(match.group(4))

  #     totalMs2 = h2 * 3600 * 1000 + m2 * 60 * 1000 + s2 * 1000 + ms2

  #     ms3 = totalMs1 - totalMs2  
  # print(h1)

def readImage(fname):

    fin = None

    try:
        fin = open(fname, "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        sys.exit(1)

    finally:

        if fin:
            fin.close()


"""
ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3
Explanation of the used arguments in this example:

-i - input file

-vn - Disable video, to make sure no video (including album cover image) is included if the source would be a video file

-ar - Set the audio sampling frequency. For output streams it is set by default to the frequency of the corresponding input stream. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options.

-ac - Set the number of audio channels. For output streams it is set by default to the number of input audio channels. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options. So used here to make sure it is stereo (2 channels)

-b:a - Converts the audio bitrate to be exact 192kbit per second

-hide_banner -loglevel error

"""
def extractAudio(videopath, begintime, endtime):
  # Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
  # -vn  no video
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.mp3"])
    
    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
      "-ar", "44100", "-ac", "2", "-b:a", "192k", \
        "tmp.mp3"])

    out_text = out_bytes.decode('utf-8')
    bts = readImage("tmp.mp3")
    os.remove("tmp.mp3")
    return bts
    
# success
# hevc 表示使用h.265 编码
# ffmpeg -y -ss 00:01:12.960 -to 00:01:14.640  -i t.mkv  -codec:v hevc -acodec mp3 -ar 44100 -ac 2 -b:a 192k t.ts
def extractVideo(videopath, begintime, endtime):
  # Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
  # -vn  no video
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.mp3"])
    
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-codec:v", "hevc",  "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.ts"])

    """
    # jsmpeg.js normal play
    ! ffmpeg -i t.mkv -y -ss 00:01:12.960 -to 00:01:14.640 -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=t.mkv t.ts
    """
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-f", "mpegts", "-codec:v", "mpeg1video",  "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.ts"])

    tmpmkv = "tmp.mkv"
    if ( os.path.exists(tmpmkv) ):
      os.unlink("tmp.mkv")
    os.symlink(videopath, "tmp.mkv")
    
    #cmd = f'ffmpeg -i \"{videopath}\" -y -ss {begintime} -to {endtime} -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=\"{videopath}\" tmp.ts' #% (videopath,videopath)#('t.mkv', 't.mkv')
    cmd = f'ffmpeg -i \"{videopath}\" -y -hide_banner -loglevel error -ss {begintime} -to {endtime} -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=\"tmp.mkv\" tmp.ts' #% (videopath,videopath)#('t.mkv', 't.mkv')

    out_bytes = subprocess.check_output(cmd, shell=True)

    

    out_text = out_bytes.decode('utf-8')
    bts = readImage("tmp.ts")
    #os.remove("tmp.t")
    return bts


def allfname(root, ext):
    names = os.listdir(root)
    #names = list( filter(lambda s: ext in s,names) )
    
    # tmp = f'{root}/*.{ext}'
    # tmp = '/Users/olnymyself/Downloads/*.mkv'
    # tmp = "/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]/*.mkv"
    # names = glob.glob(tmp)
    names = list(map(lambda ns:os.path.basename(ns),names))
    #names.sort() # key = lambda x: int(x[:-4])

    # if os.path.exists( root ):
    #   p =  os.path.join( root, '*.mkv' )
    #   names = os.listdir(root) # glob.glob(p)
    #   a = 1    
    # path = r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"+ f'/*.mkv'
    # names = glob.glob(path)
    return names
  











# 有假名的是日语，没有pgroonga_tokenize 分出来没有读音的不是日语
# 没有读音的不是
# SELECT pgroonga_tokenize('并','tokenizer', 'TokenMecab("use_base_form", true,"include_reading", true)') # use_base_form 可能会把变形转成原形？
# SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true,"include_reading", true)')
  # --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}

def jpQ(s):
    return len( unhana_remove(s) ) > 0


def createAnimeDB(host, port):
    with psycopg2.connect(database='postgres', user='postgres', password='echodict.com',host=host, port=port) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS anime;")
            cur.execute("CREATE DATABASE anime \
                WITH OWNER = postgres \
                ENCODING = 'UTF8' \
                TABLESPACE = pg_default \
                CONNECTION LIMIT = -1 \
                TEMPLATE template0;")

    with psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port) as conn:
        with conn.cursor() as cur:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur.execute("DROP TABLE IF EXISTS anime;")
            #  id serial primary key, \
            cur.execute("create table anime( \
                id integer primary key generated always as identity, \
                name text, \
                jp text, \
                zh text DEFAULT '', \
                en text DEFAULT '', \
                type text, \
                time text, \
                jp_mecab text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector, \
                videoname text, \
                seasion text DEFAULT '', \
                audio bytea, \
                video bytea \
            );")
            #cur.execute("CREATE TABLE audio(id SERIAL PRIMARY KEY, data BYTEA);")

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            cur.execute("CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);")

            cur.execute("create extension pg_jieba;")

            cur.execute("CREATE INDEX animename_index ON anime (name);")
            cur.execute("CREATE INDEX videoname_index ON anime (videoname);")
            #cur.execute("create unique index audio_unique_hash_index on anime (md5(audio));")
            
            
            # cur.execute("create extension rum;") 
            # cur.execute("CREATE INDEX fts_rum_anime ON anime USING rum (v_jp rum_tsvector_ops);")

            # 加一个函数，只要有一个字没有读音就不是jp 
            cur.execute(
              """
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
		LOOP
			reading = (js -> 'metadata' ->> 'reading');
			IF reading IS NULL THEN
					RETURN 0;
      END IF;
		
		END LOOP;
  END LOOP;
	
	RETURN 1;
	
END;
$func$ LANGUAGE plpgsql IMMUTABLE;
              """
            )

def importAnime(animename, seasion, frtname, videoname, videopath):
    dic_chs = {}

    currDir = os.path.dirname(os.path.abspath(__file__))

    
    fsrt = os.path.join(currDir, frtname)
    strs = "\n"+readstring(fsrt)+"\n"
    iters = re.finditer(r"\n\d+\n", strs, re.DOTALL)
    poss = [ i.span() for i in iters ]


    #animename = 'Danganronpa'

    chinese = []
    jpanese = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        
        n = strs[start:end]

        content = None
        if i == ( len(poss) - 1 ):
            content = strs[ end : len(strs) ]
        else:
            content = strs[ end : poss[i+1][0] ]
        
        arr = content.strip().split('\n')
        if len(arr) < 2:
          continue
        time = content.strip().split('\n')[0]
        content = content.strip().split('\n')[1]



        

        if len( re.compile(r'size=.+>(.+?)\<\/font\>').findall(content) ) > 0:
          subtitle = re.compile(r'size=.+>(.+?)\<\/font\>').findall(content)[0]
        else:
          content = re.compile(r"""face=".+?\"""").sub('', content)
          content = re.compile(r"""size="\d+\"""").sub('', content)
          content = re.compile(r"""color=".+?\"""").sub('', content)
          content = re.compile(r"""<font.+?>""").sub('', content)
          content = re.compile(r"""{\\an7}""").sub('', content)
          
          subtitle = content

        # elif match := re.compile("""(<font face=".+?" size="\d+"><font size="\d+">).+?""").search(content):
        #   m = match.group(1)
        #   subtitle = content.replace(m, "")
        # elif match := re.compile(r"""(<font face=".+?" size="\d+"><font face=".+?">{\\an\d+}<font size="\d+">).+?""").search(content):
        #   m = match.group(1)
        #   subtitle = content.replace(m, "")
        # else:
        #   raise RuntimeError('some err')

        subtitle = subtitle.replace('<b>','').replace('</b>','')
        
        chrst = chardet.detect(subtitle.encode())

        
        if chrst['encoding'] == 'ascii' and chrst['confidence'] > 0.99:
            b = 1
        elif hasHanaQ(subtitle): # 有jia ming 的是jp
          jpanese.append( (subtitle, time) )
        else:
            tmp = unchinese_remove(subtitle)
            if tmp != "":
              
              if time in dic_chs:
                continue
                #raise RuntimeError('some err')
              
              dic_chs[time] = subtitle

              tmp = "|".join( list(tmp) )
              begin = time.split('-->')[0].strip()
              end = time.split('-->')[1].strip()
              allhasjpduyingQ = False


    jpanese = sorted(jpanese, key=lambda tu: tu[1], reverse=False)  # sort by time asc


              # with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port) as conn: 
              #   with conn.cursor() as cur:
              #     sql = f"select JPQ ('{tmp}');"
              #     cur.execute( sql )
              #     row = cur.fetchone()
              #     tt = row[0]
              #     if row[0] == 1:
              #       allhasjpduyingQ = True
              #     else:
              #       allhasjpduyingQ = False

              #chinese.append( (subtitle, time) )

    # writestring('jp.txt', "\r\n".join(jpanese[0]+jpanese[1]))
    # writestring('ch.txt', "\r\n".join(chinese[0]+chinese[1]))


    with psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port) as conn:
        #conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # 不自动开启事务？
        with conn.cursor() as cur:
          
            #cur.execute('BEGIN;')
            count = 0
            for idx, tu in enumerate(jpanese):

                status = conn.get_transaction_status()
                if status == _ext.TRANSACTION_STATUS_UNKNOWN:
                    # server connection lost
                    conn.close()
                    conn = psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port)
                    cur = conn.cursor()
                elif status != _ext.TRANSACTION_STATUS_IDLE:
                    # connection in error or in transaction
                    #conn.rollback()
                    #self._pool.append(conn)
                    pass
                else:
                    # regular idle connection
                    #self._pool.append(conn)
                    pass

                j = tu[0]
                zh = ""
                # if (idx < len(chinese)):
                #     zh = chinese[idx][0].replace("(", "`(`").replace(")", "`)`")
                tags = tagger.parse(j)
                #tags = tags.split('\n')
                t = tu[1]
                begintime, endtime = parseSrtTime(t)
                #bts = extractAudio(videopath, begintime, endtime)
                bts = b''
                bts = psycopg2.Binary(bts)
                #bts_video = extractVideo(videopath, begintime, endtime)
                bts_video = b''
                bts_video = psycopg2.Binary(bts_video)

                if (t in dic_chs):
                  zh = dic_chs[t].replace("(", "`(`").replace(")", "`)`").replace("'", "''")
                videoname = videoname.replace("(", "`(`").replace(")", "`)`").replace("'", "''")
                sql = f"""insert into anime(name, seasion, jp, time, jp_mecab, zh, v_zh, videoname, audio, video) values('{animename}', '{seasion}','{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'), '{videoname}', %s, %s);"""
                cur.execute( sql, (bts,bts_video,) )
                count += 1
                #if count % 10 == 0:
                print( f"###### {count} / {len(jpanese)}" )
                
                #if count >= 10:
                #  break
                # sql = f"""insert into anime(name, jp, time, jp_mecab, zh, v_zh, videoname) values('{animename}', '{j}', '{t}', '{tags}', '{zh}', '{videoname}', to_tsvector('jiebacfg', '{zh}'));"""
                #cur.execute( sql )

                #cur.execute("""INSERT INTO audio(data) VALUES(%s);""", (bts,))
                #break

            #cur.execute('COMMIT;')


    with psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port) as conn:
        with conn.cursor() as cur:
            #cur.execute("SELECT * FROM anime WHERE jp &@ '遅刻';")
            cur.execute("SELECT * FROM anime WHERE jp_mecab &@ 'チコク';")
            rows = cur.fetchall()
    
    # with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port=port) as conn:
    #     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #     with conn.cursor() as cur:
    #         cur.execute("DROP DATABASE IF EXISTS anime;")

    print("hi,,,")

if __name__ == "__main__":

    """
    pg_ctlcluster 13 main start       # echo pg

    docker exec -it centos7PG10 /bin/bash
    systemctl restart postgresql-13   # echo docker pg
    """

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

    createAnimeDB(host, port)






    realroot = r"F:\videos\anime"
    if OS == "Linux":
      realroot = r"/mnt/videos/anime"
    if OS == "OSX":
      root = r"/Users/olnymyself/Downloads/videos/anime"


    fnames2 = glob.glob(realroot + '/**/*.mkv', recursive=True)
    tmp = fnames2[0]
    dir = os.path.dirname(tmp)
    dir2 = os.path.dirname(dir)
    dir3 = os.path.dirname(dir2)
    rootorigin = dir  # root origin
    seasion = os.path.basename(dir2)
    animename = os.path.basename(dir3)

    
    root = rootorigin # r"F:\videos\anime\Danganronpa\S01\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]" # r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    if OS == "Linux":
      root = r"/mnt/videos/anime/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    if OS == "OSX":
      #root = r"/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
      root = r"/Users/olnymyself/Downloads/d"

    print( f"root path: \n{root}" )

    fnames = allfname(root, 'mkv')

    fnames = sorted(fnames, key=lambda s: s, reverse=False)  # sort by name

    cur = 0
    for fname in fnames:
      videoname = fname
      frtname = f"{fname}.srt"
      fname = os.path.join( root, fname )
      videopath = os.path.join( root, videoname )
      out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
      out_text = out_bytes.decode('utf-8')

      #animename = 'Danganronpa'
      #seasion = '01'
      importAnime(animename, seasion, frtname, videoname, videopath)

      cur = cur + 1

      print('one task done. ', cur, '/', len(fnames) )

      #break


    print("all task done.")

    """
    ここ
    とかい【都会】  トカイ
    """






