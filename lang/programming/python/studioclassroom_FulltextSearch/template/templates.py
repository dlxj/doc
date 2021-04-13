
# https://www.jianshu.com/p/765afe303bf8

import subprocess
import re
import chardet

import MeCab
tagger = MeCab.Tagger()

from zhconv import convert


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlite3 as sqlite # Python 自带的

# from pymysql import escape_string  # pip install **pymysql==0.9.3** # 高版本没有escape_string
import glob

import json
import decimal
import datetime

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
port1 = 5432
port2 = 54322

@app.route('/', methods=['get'])
@cross_origin(supports_credentials=True)
def default_get():

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


        with psycopg2.connect(database='studio', user='postgres', password='postgres',host=host, port=port1) as conn:
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

                    return render_template('result.html', title='Welcom!', enrows=rows, keywd=keywd)
                
                if (isCh):
                    sql = f"select id, en, zh, type from studio where v_zh @@  to_tsquery('jiebacfg', '{keywd}') ORDER BY RANDOM() limit 3;"

                    cur.execute(sql)
                    rows = cur.fetchall()
                    return render_template('result.html', title='Welcom!', enrows=rows, keywd=keywd)

                if (isJp):
                    with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port2) as conn2:
                        with conn2.cursor() as cur2:
                            cur2.execute(f"SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ '{keywd}' ORDER BY RANDOM() limit 3;")
                            rows = cur2.fetchall()

                            return render_template('result.html', title='Welcom!', jprows=rows, keywd=keywd)

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
        print(rowid)

    def generate():
        path = 'static/t.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8085, debug=True)
