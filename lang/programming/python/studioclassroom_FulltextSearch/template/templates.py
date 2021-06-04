
# https://www.jianshu.com/p/765afe303bf8
# https://github.com/MikimotoH/furigana 汉字标注
# ThreadedConnectionPool

# pip install psycopg2-binary

import subprocess
import re
import chardet

import MeCab
tagger = MeCab.Tagger()

from zhconv import convert
import jaconv


import psycopg2
import psycopg2.pool
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlite3 as sqlite # Python 自带的

# from pymysql import escape_string  # pip install **pymysql==0.9.3** # 高版本没有escape_string
import glob

import json
import decimal
import datetime
import platform

def OSXQ():
    return platform.system() == 'Darwin'


# import xmltodict

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


# out_bytes = subprocess.check_output([r"ffmpeg", "-i", "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv", "-map", "0:s:0", "out.srt"])
# out_text = out_bytes.decode('utf-8')

def readstring(fanme):
    with open(fanme, "r", encoding="utf-8") as fp:
        return fp.read()

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def chinese_remove(s):
    return re.sub(r"[\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def unjp_remove(s):
    return re.sub(r"[^\u0800-\u4e00]", "", s, flags=re.UNICODE)

def unhana_remove(s):
    return re.sub(r"[^\u3040-\u309F^\u30A0-\u30FF]", "", s, flags=re.UNICODE)

def jpQ(s):
    return len( unhana_remove(s) ) > 0

def chQ(s):
    return not jpQ(s) and len( chinese_remove(s) ) == 0
    

from flask import Flask, request, jsonify, redirect, render_template_string,session,Response,render_template,url_for


import datetime
import copy

from flask_cors import CORS, cross_origin
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


app.config['SECRET_KEY'] = 'STRONGSECRTKEY'

host = '111.229.53.195'
host2 = '209.141.34.77'

host = host2 # 暂时这样先，host 关机了

port1 = 5432
port2 = 5432

#hostAPI = 'echodict.com'
hostAPI = '127.0.0.1'

pool1 = psycopg2.pool.SimpleConnectionPool(1, 200, user="postgres",
    #password="postgres",
    password="echodict.com",
    host=host,
    port=port1,
    #database="studio")
    database="anime")

pool2 = psycopg2.pool.SimpleConnectionPool(1, 200, user="postgres",
    password="echodict.com",
    host=host2,
    port=port2,
    database="anime")


connection = pool1.getconn()
cursor = connection.cursor()
cursor.execute('select 1;')
records = cursor.fetchall()
cursor.close()
pool1.putconn(connection)

@app.route('/', methods=['get'])
@cross_origin(supports_credentials=True)
def default_get():

    path = 'static/index.html'
    with open(path, 'r', encoding="utf-8") as fmp3:
        data = fmp3.read()
        return render_template_string(data)

    #return render_template_string(readstring('static/index.html'))


    #session['keyword'] = 'result'
    
    isEn = False
    isCh = False
    isJp = False

    if ('keyword' in session and len( session['keyword'].strip() ) > 0 ):
        keywd = session['keyword']
        keywd = keywd.strip()
        print(f'session is: {keywd}')
        
        if ( chQ(keywd)):
            #a = unhana_remove(keywd)
            print('### ch.')
            keywd = convert(keywd, 'zh-hant')
            isCh = True
        elif ( jpQ(keywd)):
            print('### jp.')
            isJp = True
        else:
            print('### en.')
            isEn = True


        # with psycopg2.connect(database='studio', user='postgres', password='postgres',host=host, port=port1) as conn:
        #with pool1.getconn() as conn:
        conn = pool1.getconn()
        if True:
            with conn.cursor() as cur:

                sql = ""
                if (isEn):
                    print('### select en.')

                    sql = f"SELECT id, ts_headline(en, q) as en, zh, type \
                    FROM studio, to_tsquery('{keywd}')  q \
                    where en @@ to_tsquery('{keywd}') \
                    ORDER BY RANDOM() LIMIT 3; \
                    "

                    cur.execute(sql)
                    rows = cur.fetchall()
                    pool1.putconn(conn)

                    return render_template('result.html', title='Welcom!', enrows=rows, keywd=keywd)
                
                if (isCh):
                    sql = f"select id, en, zh, type from studio where v_zh @@  to_tsquery('jiebacfg', '{keywd}') ORDER BY RANDOM() limit 3;"

                    cur.execute(sql)
                    rows = cur.fetchall()
                    pool1.putconn(conn)

                    return render_template('result.html', title='Welcom!', enrows=rows, keywd=keywd)

                if (isJp):
                    #with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port2) as conn2:

                    if len( unhana_remove(keywd) ) == len(keywd):
                        keywd = jaconv.hira2kata(keywd)
                    

                    

                    conn2 = pool2.getconn()
                    #with pool2.getconn() as conn2:
                    if True:
                        with conn2.cursor() as cur2:
                            cur2.execute(f"SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ '{keywd}' ORDER BY RANDOM() limit 3;")
                            rows = cur2.fetchall()
                            pool2.putconn(conn2)

                            return render_template('result.html', title='Welcom!', jprows=rows, keywd=keywd, hostAPI=hostAPI)

    return render_template('result.html', title='Welcom!')


@app.route('/', methods=['post'])
@cross_origin(supports_credentials=True)
def default_post():
    keyword = request.values.get("keyword")
    print(f"keyword: {keyword}")
    select = request.values.get('lang_select')
    print(f"select: {select}")

    session['keyword'] = keyword
    session['select'] = select
    
    return redirect('/')


@app.route('/next', methods=['post'])
@cross_origin(supports_credentials=True)
def next():

    html = """
    <form action="/" method="post">
    keyword: <input type="text" name="keyword"><br>
    <option value ="en">en</option>
    <option value ="jp">jp</option>
    <button type="submit">Search</button>
    </form>
    """

    if 'keyword' in session and  session['keyword'].strip() != "":
        print('/next redirect.')
        return redirect('/')

    print('/next default page.')
    return render_template_string(html)


@app.route('/audio', methods=['get'])
def stream_mp3():
    print('request.args:', request.args)
    if 'id' in request.args:
        rowid = request.args.get('id')

    conn2 = pool2.getconn()
    with conn2.cursor() as cur2:
        sql = f"SELECT id, audio FROM anime WHERE id={rowid};"
        cur2.execute(sql)
        row = cur2.fetchone()
        idd = row[0]
        bytea = row[1]

        pool2.putconn(conn2)

        return Response(bytea, mimetype="audio/mpeg")

#         import base64

# rows = cur.fetchall()
# binary_img = rows[0][0] # 
# base64_img = base64.b64encode(binary_img)

    def generate():
        path = 'static/t.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    bytea = generate()
    return Response(bytea, mimetype="audio/mpeg")


@app.route('/iso', methods=['get'])
def stream_ISO():
    def generate():
        path = 'static/LaoMaoTao.iso'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    bytea = generate()
    return Response(bytea, mimetype="application/octet-stream")



if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8085, debug=True)




    """
    ここ


    とかい【都会】  トカイ
    """






    """

进程安全池

    import os
from psycopg2.pool import ThreadedConnectionPool


class ProcessSafePoolManager:

    def __init__(self, *args, **kwargs):
        self.last_seen_process_id = os.getpid()
        self.args = args
        self.kwargs = kwargs
        self._init()

    def _init(self):
        self._pool = ThreadedConnectionPool(*self.args, **self.kwargs)

    def getconn(self):
        current_pid = os.getpid()
        if not (current_pid == self.last_seen_process_id):
            self._init()
            print "New id is %s, old id was %s" % (current_pid, self.last_seen_process_id)
            self.last_seen_process_id = current_pid
        return self._pool.getconn()

    def putconn(self, conn):
        return self._pool.putconn(conn)

pool = ProcessSafePoolManager(1, 10, "host='127.0.0.1' port=12099")
    """