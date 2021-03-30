
"""
pip install xmltodict
GFW
https://www.ishells.cn/archives/linux-ssr-server-client-install
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
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

#escape_string = pymysql.escape_string

#host = '111.229.53.195'
host = '127.0.0.1'
#host = '192.168.1.166'






def createDatabase_studio( host = '127.0.0.1', studiodb = './db/studioclassroom.db' ):

    with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port='5432') as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS studio;")
            cur.execute("CREATE DATABASE studio \
                WITH OWNER = postgres \
                ENCODING = 'UTF8' \
                TABLESPACE = pg_default \
                CONNECTION LIMIT = -1 \
                TEMPLATE template0;")

    with psycopg2.connect(database='studio', user='postgres', password='postgres',host=host, port='5432') as conn:

        with conn.cursor() as cur:
        
            cur.execute("DROP TABLE IF EXISTS studio;")
            cur.execute("create table studio( \
                id serial primary key, \
                en text, \
                zh text, \
                type text, \
                time text, \
                v_en  tsvector, \
                v_zh  tsvector \
            );")
            """
            需要安装两个扩展，一个分词，一个FTS
                https://github.com/postgrespro/rum
            """
            cur.execute("create extension pg_jieba;")
            cur.execute("create extension rum;")
            cur.execute("CREATE INDEX fts_rum_studio ON studio USING rum (v_zh rum_tsvector_ops);")
        
            with sqlite.connect(studiodb) as cx: # './db/studioclassroom.db'

                cu = cx.cursor()
                cu.execute("SELECT * FROM studioclassroom_content;", [])
                rows = cu.fetchall()

                cur.execute('BEGIN;')

                for row in rows:
                    # sql 语句里本身有单引号时用两个单引号来代替
                    en = row[1].replace("'", "''").replace("\n",'')
                    zh = row[2].replace("'", "''").replace("\n",'')
                    ty = row[3].replace("'", "''").replace("\n",'')
                    ti = row[4].replace("'", "''").replace("\n",'')

                    sql = f"""insert into studio(en, zh, type, time, v_en, v_zh ) values('{en}', '{zh}', '{ty}', '{ti}', 'no', to_tsvector('jiebacfg', '{zh}'));"""

                    cur.execute( sql )
        
            cur.execute('COMMIT;')


def createDatabase_economistglobl( host = '127.0.0.1',  economistglobl= './db/economist/data/data/com.economist.hummingbird/databases/t_economics_database.db' ):
        
    with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port='5432') as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS economistglobl;")
            cur.execute("CREATE DATABASE economistglobl \
                WITH OWNER = postgres \
                ENCODING = 'UTF8' \
                TABLESPACE = pg_default \
                CONNECTION LIMIT = -1 \
                TEMPLATE template0;")
        

    with psycopg2.connect(database='economistglobl', user='postgres', password='postgres',host=host, port='5432') as conn:

        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS article;")
            cur.execute("create table article( \
                id serial primary key, \
                issue_time text, \
                pubdate text, \
                en text, \
                zh text, \
                zh_tw text, \
                v_en tsvector, \
                v_zh  tsvector, \
                v_zh_tw  tsvector \
            );")

            """
            需要安装两个扩展，一个分词，一个FTS
                https://github.com/postgrespro/rum
            """
            cur.execute("create extension pg_jieba;")
            cur.execute("create extension rum;")
            cur.execute("CREATE INDEX fts_rum_article ON article USING rum (zh_tw rum_tsvector_ops);")


        with sqlite.connect(economistglobl) as cx:
            
            cu = cx.cursor()
            cu.execute("select issue_id, title as issue_time from issue_table;", [])
            rows = cu.fetchall()

            issue_time = {}

            for row in rows:
                issueid = row[0]
                issuetime = row[1]
                issue_time[ issueid ] = issuetime

            cu.execute("select article_folder as folder_id, issue_id from article_table;", [])
            rows = cu.fetchall()
            
            
            folder_id = {}
            
            for row in rows:
                folderid = row[0]
                issueid  = row[1]
                folder_id[ folderid ] = issueid

            articles = []
            idioms = []

            xmls = glob.glob('./db/economist/**/article.xml', recursive=True)
            for xml in xmls:
                with open(xml, "r", encoding="utf-8") as fp:
                    data = fp.read()
                    js = xmltodict.parse(data)
                    article = {}
                    idiom = {}
                    _id = js['article']['@id']
                    pubdate = js['article']['pubdate']
                    
                    article['issue_time'] = issue_time[ folder_id[_id] ]
                    article['pubdate'] = pubdate

                    #print(type( js['article']['body']['idioms'] ))
                    
                    if js['article']['body']['idioms'] != None:
                        idiom['issue_time'] = issue_time[ folder_id[_id] ]
                        idiom['pubdate'] = pubdate
                        idiom['idiom'] = js['article']['body']['idioms']['idiom']
                        idioms.append(idiom)

                    article['content'] = []



                    for ph in js['article']['body']['content']['paragraph']:
                        
                        if ph == 'copy':
                            copy = js['article']['body']['content']['paragraph']['copy']
                            en = copy[0]['#text']
                            zh = copy[1]['#text']
                            zw = copy[2]['#text']
                        else:
                            copy = ph['copy']
                            en = copy[0]['#text']                
                            zh = copy[1]['#text']
                            zw = copy[2]['#text']


                        article['content'].append( { 'en':en, 'zh':zh, 'zh_tw':zw } )

                    articles.append( article )
                
            return articles, idioms

def createDatabase_anime( host = '192.168.1.166'):

    with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port='5432') as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS anime;")
            cur.execute("CREATE DATABASE anime \
                WITH OWNER = postgres \
                ENCODING = 'UTF8' \
                TABLESPACE = pg_default \
                CONNECTION LIMIT = -1 \
                TEMPLATE template0;")

    with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port='5432') as conn:

        with conn.cursor() as cur:
        
            cur.execute("DROP TABLE IF EXISTS anime;")
            cur.execute("create table anime( \
                id serial primary key, \
                jp text, \
                zh text, \
                en text, \
                type text, \
                time text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector \
            );")
            """
            需要安装两个扩展，一个分词，一个FTS
                https://github.com/postgrespro/rum
            """
            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            # cur.execute("create extension rum;")
            # cur.execute("CREATE INDEX fts_rum_anime ON anime USING rum (v_jp rum_tsvector_ops);")

            cur.execute('BEGIN;')
            jp = '今日は学校に遅刻した。'
            sql = f"""insert into anime(jp) values('{jp}');"""
            cur.execute( sql )
            cur.execute('COMMIT;')
        
    


# createDatabase_studio()
# articles, idioms = createDatabase_economistglobl()
createDatabase_anime()

print('hi')



