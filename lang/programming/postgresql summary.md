## Install PG



好用的代理  https://github.com/TyrantLucifer/ssr-command-client

v2ray  https://printempw.github.io/v2ray-ws-tls-cloudflare/



conda info --env

conda activate flask_ftspg





sftp root@172.18.0.3 # 连接远程服务器

put -r pg_jieba .    # 上传目录到运程服务器（docker）



https://github.com/TyrantLucifer/ssr-command-client



centos7 install [u](https://computingforgeeks.com/how-to-install-postgresql-13-on-centos-7/)

vps [ramnode](https://www.ramnode.com/)



```
pm2 -n ftspg8084 start /root/insertstudio/ftspg.js
pm2 save
```



```
which pg_config
--> /usr/bin/pg_config

ERROR:  could not open extension control file "/usr/share/postgresql/13/extension/pgroonga.control": No such file or directory
```





```
# 日语分词插件
https://pgroonga.github.io/install/ubuntu.html
# 使用
https://ravenonhill.blogspot.com/2019/09/pgroonga-traditional-chinese-full-text-search-in-postgresql-for-taiwanese.html

# 这样查
SELECT * FROM anime WHERE jp &@ '遅刻';
```

```
https://web.chaperone.jp/w/index.php?PostgreSQL/pgroonga
```

```
def createDatabase_anime( host = 'xxxxx.166'):

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

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            # cur.execute("create extension rum;")
            # cur.execute("CREATE INDEX fts_rum_anime ON anime USING rum (v_jp rum_tsvector_ops);")

            cur.execute('BEGIN;')
            jp = '今日は学校に遅刻した。'
            sql = f"""insert into anime(jp) values('{jp}');"""
            cur.execute( sql )
            cur.execute('COMMIT;')

```



```
pgroonga_test=# CREATE TABLE memos (
pgroonga_test(#   id integer,
pgroonga_test(#   content text
pgroonga_test(# );
CREATE TABLE
pgroonga_test=#
pgroonga_test=# CREATE INDEX pgroonga_content_index ON memos USING pgroonga (content);
CREATE INDEX
pgroonga_test=# INSERT INTO memos VALUES (1, 'PostgreSQLはリレーショナル・データベース管理システムです。');
INSERT 0 1
pgroonga_test=# INSERT INTO memos VALUES (2, 'Groongaは日本語対応の高速な全文検索エンジンです。');
INSERT 0 1
pgroonga_test=# INSERT INTO memos VALUES (3, 'PGroongaはインデックスとしてGroongaを使うためのPostgreSQLの拡張機能です。');
INSERT 0 1
pgroonga_test=# INSERT INTO memos VALUES (4, 'groongaコマンドがあります。');
INSERT 0 1
pgroonga_test=#
pgroonga_test=# SET enable_seqscan = off;
SET
pgroonga_test=#
pgroonga_test=# SELECT * FROM memos WHERE content &@ '全文検索';
 id |                      content
----+---------------------------------------------------
  2 | Groongaは日本語対応の高速な全文検索エンジンです。
(1 row)

pgroonga_test=# explain analyze SELECT * FROM memos WHERE content &@ '全文検索';
                                                           QUERY PLAN
--------------------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on memos  (cost=0.16..10.85 rows=635 width=36) (actual time=0.424..0.425 rows=1 loops=1)
   Recheck Cond: (content &@ '全文検索'::text)
   Heap Blocks: exact=1
   ->  Bitmap Index Scan on pgroonga_content_index  (cost=0.00..0.00 rows=13 width=0) (actual time=0.413..0.413 rows=1 loops=1)
         Index Cond: (content &@ '全文検索'::text)
 Planning time: 0.137 ms
 Execution time: 0.641 ms
(7 rows)
```

 



to_tsvector('Chinese', content);





用**Navicat** 客户端查数据

- HeidiSQL 有点问题


```bash
apt install postgresql-server-dev-13
find / -name "postgres.h" -print  # 后面编译pg_jieba 要用
```



After fresh installation of PostgreSQL 13 on **CentOS 7** initialization is required.

```
$ sudo /usr/bin/postgresql-13-setup initdb
$ sudo systemctl start postgresql-13
$ systemctl status postgresql-13
```





Success. You can now start the database server using:

```bash
pg_ctlcluster 13 main start
```

```
# windows # 需要管理员仅限
pg_ctl.exe restart -D "E:\Program Files\PostgreSQL\13\data"

# 登录，用户名密码都是postgres
E:\Program Files\PostgreSQL\13\bin>psql -U postgres
```





登录 [u](https://www3.ntu.edu.sg/home/ehchua/programming/sql/PostgreSQL_GetStarted.html)

```mysql
sudo -u postgres psql
select version();
\password postgres  # 修改密码
\q
```



Added the line as below in `pg_hba.conf`:

```sql
# vi /etc/postgresql/13/main/pg_hba.conf
# 加在最后面
hostnossl    all          all            0.0.0.0/0  trust        
```

and this was modified in `postgresql.conf`, as shown:

```sql
# vi /etc/postgresql/13/main/postgresql.conf
listen_addresses = '*'  
```



```nodejs
npm install pg
```



## 显示数据目录

show data_directory;



## 列出所有可用数据库

\l

\c studio  # 切换数据库

```mysql
insert into studio(en, zh, type, time, v_en, v_zh ) values('When something does not go as you expected and you feel anxious or upset, it helps to understand that these feelings are part of the package.', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。','AD050851', '01:20.3', 'no', to_tsvector('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。'));
```





```sql
sudo -u postgres psql -c '\set AUTOCOMMIT on'
```



要想使得配置永久生效，需要在/data/postgresql.conf总添加lc_messages='zh_CN.UTF-8'，保存后，重启服务或者重载。



## insert studio



```python
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

#host = 'xxxxx.195'
host = '127.0.0.1'
#host = 'xxxxx.166'






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



# createDatabase_studio()
articles, idioms = createDatabase_economistglobl()

print('hi')
```






## nodejs

https://github.com/sehrope/node-pg-db



```javascript
const { Pool, Client } = require('pg')
const connectionString = 'postgresql://postgres:postgres@111.229.53.195:5432/studio'
const pool = new Pool({
  connectionString,
})

sql = "select id, en, zh, type from studio where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;"
keywd = '情緒'
pool.query(sql, [keywd], (err, res) => {
  if(err) {
    return console.error('error fetching client from pool', err);
  }
  console.log(res['rows'])
  pool.end()
})
```



### Server



```javascript
'use strict';
var express = require('express'),
  app = express(),
  cookieParser = require('cookie-parser'),
  expressSession = require('express-session'),
  bodyParser = require('body-parser');

const { Pool, Client } = require('pg')
const connectionString = 'postgresql://postgres:postgres@111.229.53.195:5432/studio'
const pool = new Pool({
  connectionString,
})

// var db = require('pg-db')("postgres://postgres:psql@192.157.212.220/studio");

app.use(cookieParser());
app.use(expressSession({
  secret: 'somesecrettokenhere'
}));
app.use(bodyParser());

app.get('/', function(req, res) {

  var html = '<form action="/" method="post">' +
    'keyword: <input type="text" name="keyword"><br>' +
    '<button type="submit">Search</button>' +
    '</form>';
  if (req.session.keyword) {
    var keywd = req.session.keyword;
    if (typeof keywd != 'undefined' &&
      typeof keywd != null && keywd.trim().length > 0) {
      keywd = keywd.trim();
      var zhQ = false;
      for (var i in keywd) {
        if (keywd.charCodeAt(i) > 127) {
          zhQ = true;
          break;
        }
      }

      /*

      select id, en, zh, type, time from studio where v_en @@  to_tsquery('en', 'achieving') limit 3;

SELECT id, ts_headline(en, q), rank
FROM (SELECT id, en, q, ts_rank_cd(en, q) AS rank
FROM studio, to_tsquery('en', 'achieving') q
WHERE en @@ q
ORDER BY rank DESC
LIMIT 3) AS foo;
      */

      var sql = "";
      if (zhQ) {
        sql = "select id, en, zh, type from studio where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;"
      } else {
        sql = "SELECT id, ts_headline(en, q) as en, zh, type \
                FROM studio, plainto_tsquery('en', $1) q \
                WHERE v_en @@ q \
                ORDER BY RANDOM() LIMIT 3 ;";
      }

      pool.query(sql, [keywd], (err, rt) => {
        if (err) throw err;
        // JSON.stringify
        for (var i in rt['rows']) {
          html += ('<br>' + rt['rows'][i].en + '<br>' + rt['rows'][i].zh + '<br>' + rt['rows'][i].type);
          html += ('<br>' + '<br>');
        }

        res.cookie('keywd', req.session.keyword);
        html += '<br>Your keyword is: ' + req.session.keyword;
        console.log('session is: ' + req.session.keyword);
        html += '<form action="/next" method="post">' +
          '<button type="submit">Next</button>' +
          '</form>';

        res.send(html);
      });

    } else {
      html += 'ooops: keyword plz.'
      res.send(html);
    }
  } else {
    res.send(html);
  }
});

app.post('/', function(req, res) {
  //if (req.cookies.bar) {
  //req.session.keyword = req.body.keyword;
  req.session.keyword = req.body.keyword;
  res.redirect('/');
    //}
    //res.send(req.cookies.bar);
    //res.redirect('/');
});

app.post('/next', function(req, res) {
  console.log('cookies is: ', req.cookies.keywd);
  req.session.keyword = req.cookies.keywd;
  res.redirect('/');
});


app.listen(80, function() {
  console.log("ready captain.");
});
```







```javascript

// pg.js

/*
// drop database studio
pg_ctlcluster 9.5 main stop --force
pg_ctlcluster 9.5 main start
dropdb -U postgres  studio -h 127.0.0.1 -p 5432
*/

var dbpostgres = require('pg-db')("postgres://postgres:psql@192.157.212.220/postgres");
var db = require('pg-db')("postgres://postgres:psql@192.157.212.220/studio");
var sqlite3 = require('sqlite3').verbose();
var dbsq = new sqlite3.Database('./db/studioclassroom.db', sqlite3.OPEN_READONLY);
var util = require('util');

// CREATE TABLE 'studioclassroom_content'(docid INTEGER PRIMARY KEY, 'c0en', 'c1zh', 'c2name', 'c3time');
// SELECT * FROM "studioclassroom_content;

function queryStudio(callback) {
	dbsq.all("SELECT * FROM studioclassroom_content;", function(err, rows) {
		callback(rows);
	}); /**/
}

function createDatabase(cb) {
	dbpostgres.execute("CREATE DATABASE studio \
WITH OWNER = postgres \
   ENCODING = 'UTF8' \
   TABLESPACE = pg_default \
   LC_COLLATE = 'zh_CN.UTF-8' \
   CONNECTION LIMIT = -1 \
   TEMPLATE template0;", function(err, result) {
		cb(err, 'createDatabase ok.');
	});
}

function dropTable(cb) {
	db.execute("DROP TABLE IF EXISTS studio;", function(err, result) {
		cb(err, 'dropTable ok.');
	});
}

function createTable(cb) {
	db.execute("create table studio( \
   id serial primary key, \
   en text, \
   zh text, \
   type text, \
   time text, \
   v_en  tsvector, \
   v_zh  tsvector \
);", function(err, result) {
		cb(err, 'createTable ok.');
	});
}

function insertStudio(cb) {
	db.execute("insert into studio(en, zh, type, time, v_en, v_zh ) values('When something does not go as you expected and you feel anxious or upset, it helps to understand that these feelings are part of the package.', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。','AD050851', '01:20.3', 'no', to_tsvector('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。'));", function(err, result) {
		cb(err, 'insertStudio ok.');
	});
}

queryStudio(function(rows) {
	createDatabase(function(err, msg) {
		if (err) throw err;
		console.log(msg);
		db.tx.series([
			dropTable,
			createTable,
			function(cb) {
				db.execute('create extension pg_jieba;', function(err) {
					cb(err, 'create extension pg_jieba ok.');
				});
			},
			function(cb) {

				var curr = 0;
				var last = 10000 - 1; // rows.length - 1;

				for (var i = 0; i < rows.length; i++) {
					var sql = "insert into studio(en, zh, type, time, v_en, v_zh ) values('%s', '%s', '%s', '%s', 'no', to_tsvector('jiebacfg', '%s'));";
					sql = util.format(sql, rows[curr].c0en.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c2name.replace(/\n/g, ''), rows[curr].c3time.replace(/\n/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''));
					//console.log(sql);
					db.execute(sql, function(err, result) {
						if (err) {
							console.log(sql);
							throw err;
						}
						curr = curr + 1;
						console.log('insrt one task done. curr/last is: ', curr, '/', last); //console.log(rows.length, rows[curr].c0en, rows[curr].c1zh, rows[curr].c2name, rows[curr].c3time);
						if (curr > last) {
							console.log('insrt all task done. curr is: ' + curr);
							cb(null, 'insertStudio ok.');
						}
					});
				}

				function insrt(curr, last) {
					if (curr > last) {
						console.log('insrt all task done. curr is: ' + curr);
						cb(null, 'insertStudio ok.');
						return;
					}
					var sql = "insert into studio(en, zh, type, time, v_en, v_zh ) values('%s', '%s', '%s', '%s', 'no', to_tsvector('jiebacfg', '%s'));";
					sql = util.format(sql, rows[curr].c0en.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c2name.replace(/\n/g, ''), rows[curr].c3time.replace(/\n/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''));
					//console.log(sql);
					//db.execute("insert into studio(en, zh, type, time, v_en, v_zh ) values('When something does not go as you expected and you feel anxious or upset, it helps to understand that these feelings are part of the package.', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。','AD050851', '01:20.3', 'no', to_tsvector('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。'));", function(err, result) {
					db.execute(sql, function(err, result) {
						if (err) {
							console.log(sql);
							throw err;
						}
						console.log('insrt one task done. curr/last is: ', curr, '/', last);
						insrt(curr + 1, last);
						//console.log(rows.length, rows[curr].c0en, rows[curr].c1zh, rows[curr].c2name, rows[curr].c3time);
						//cb(err, 'insertStudio ok.');
					});
				}
				//insrt(curr, last);
				//cb(null,'inset ok.');
			}
		], function(err, rs) {
			if (err) throw err;
			console.log(rs);
			console.log('all task done.');
		});
	});
});

/*
createDatabase(function(err, msg) {
	if (err) throw err;
	console.log(msg);
	db.tx.series([
		dropTable,
		createTable,
		function(cb) {
			db.execute('create extension pg_jieba;', function(err) {
				cb(err, 'create extension pg_jieba ok.');
			});
		},
		insertStudioFromSqlite
	], function(err, rs) {
		if (err) throw err;
		console.log(rs);
		console.log('all task done.');
	});
});*/

/*
db.tx.series([
	//dropTable,
	//createTable,
	
	function(cb) {
		db.execute('create extension pg_jieba;', function(err) {
			cb(err);
		});
	},
	//insertStudion
], function(err, rs) {
	if (err) throw err;
	console.log('all task done.');
});*/
```





```python

```



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import psycopg2

# Connection details:
dbname = 'sampledb'
user = 'postgres'
host = '127.0.0.1'
password = '123456789'


def get_tables_databases():
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select table_name from INFORMATION_SCHEMA.TABLES '
                        'where table_type=\'BASE TABLE\' '
                        'and table_schema not in (\'pg_catalog\', \'information_schema\');')
            return [r for (r,) in cur]


def get_column_table(table_name: str):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select column_name from INFORMATION_SCHEMA.COLUMNS '
                        'where table_name=\'' + table_name + '\';')
            return [r for (r,) in cur]


def get_column_details_table(table_name: str):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS '
                        'where table_name=\'' + table_name + '\';')
            return [r for r in cur]


def get_length_table(table_name: str):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select count(*) from "' + table_name + '";')
            return cur.fetchone()[0]


def get_aprox_length_table(table_name: str):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select reltuples as estimate from pg_class '
                        'where relname=\'' + table_name + '\';')
            return cur.fetchone()[0]


def get_size_database():
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select pg_size_pretty(pg_database_size(pg_database.datname)) as size from pg_database '
                        'where pg_database.datname=\'' + dbname + '\';')
            return cur.fetchone()[0]


def get_rows_table(table_name: str,):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute('select * from ' + table_name + ';')
            return cur.fetchall()


def export_table_csv(table_name: str, file_path: str = None, with_title: bool = False):
    file_name = os.path.join(file_path if file_path else '.', table_name + '.csv')
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, mode="w", encoding="UTF-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
            # column names
            if with_title:
                with conn.cursor() as cur:
                    cur.execute('select column_name from INFORMATION_SCHEMA.COLUMNS '
                                'where table_name=\'' + table_name + '\';')
                    title = []
                    for (r,) in cur:
                        title.append(r)
                    csvwriter.writerow(title)
            # content
            with conn.cursor('server-side-cursor') as cur:
                cur.itersize = 100000  # how much records to buffer on a client
                cur.execute('select * from ' + table_name + ';')
                for r in cur:
                    csvwriter.writerow(r)


def export_database_csv(file_path: str = None, with_title: bool = False):
    file_path = file_path if file_path else dbname
    os.makedirs(file_path, exist_ok=True)
    for table in get_tables_databases():
        export_table_csv(table, file_path, with_title)


def export_table_copy(table_name: str, file_path: str = None, with_title: bool = False):
    file_name = os.path.join(file_path if file_path else '.', table_name + '.copy')
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, mode="w", encoding="UTF-8") as copyfile:
        with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
            with conn.cursor() as cur:
                # column names
                if with_title:
                    cur.execute('select column_name from INFORMATION_SCHEMA.COLUMNS '
                                'where table_name=\'' + table_name + '\';')
                    title = ''
                    for (r,) in cur:
                        title += r + '|'
                    copyfile.write(title[:-1] + '\n')
                # content
                cur.copy_to(copyfile, table_name, sep="|")


def export_database_copy(file_path: str = None, with_title: bool = False):
    file_path = file_path if file_path else dbname
    os.makedirs(file_path, exist_ok=True)
    for table in get_tables_databases():
        export_table_copy(table, file_path, with_title)


def export_table_sql(table_name: str, file_path: str = None):
    file_name = os.path.join(file_path if file_path else '.', table_name + '.sql')
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, mode="w", encoding="UTF-8") as sqlfile:
        with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
            # table
            with conn.cursor() as cur:
                cur.execute('select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS '
                            'where table_name=\'' + table_name + '\';')
                columns = []
                for r in cur:
                    (cname, ctype, clen) = r
                    if ctype in {'character varying', 'varchar', 'character', 'char', 'text'}:
                        ctype = 'varchar'
                    elif ctype == 'money':
                        ctype = 'double precision'
                    elif ctype == 'bytea':
                        ctype = 'BLOB'
                    clen = '(' + str(clen) + ')' if clen and ctype == 'varchar' else ''
                    columns.append(cname + ' ' + ctype + clen)
                sqlfile.write('create table ' + table_name + ' (' + ', '.join(columns) + ');\n')
            # rows
            with conn.cursor('server-side-cursor') as cur:
                cur.itersize = 100000  # how much records to buffer on a client
                cur.execute('select * from ' + table_name + ';')
                for r in cur:
                    data = []
                    for rd in r:
                        if rd == 'null':
                            data.append('NULL')
                        else:
                            if isinstance(rd, str):
                                rd = rd.replace('\'', '\'\'')
                            data.append(repr(rd).replace('"', '\''))
                    sqlfile.write('insert into ' + table_name + ' values (' + ', '.join(data) + ');\n')


def export_database_sql(file_path: str = None):
    file_path = file_path if file_path else dbname
    os.makedirs(file_path, exist_ok=True)
    for table in get_tables_databases():
        export_table_sql(table, file_path)


def erase_database():
    tables = get_tables_databases()
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            for table in tables:
                cur.execute('drop table if exists ' + table + ' cascade;')
    full_vacuum()


def create_database(dbname: str):
    with psycopg2.connect(dbname='postgres', user=user, host=host, password=password) as conn:
        old_isolation_level = conn.isolation_level
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute('create database ' + dbname + ';')
        conn.set_isolation_level(old_isolation_level)


def delete_database(dbname: str):
    with psycopg2.connect(dbname='postgres', user=user, host=host, password=password) as conn:
        old_isolation_level = conn.isolation_level
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute('drop database ' + dbname + ';')
        conn.set_isolation_level(old_isolation_level)


def vacuum(full: bool= False, freeze: bool = False, verbose: bool = False, analyze: bool = False, table: str = None, column: str = None):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        old_isolation_level = conn.isolation_level
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute('vacuum ' + ('full ' if full else '') +
                                    ('freeze ' if freeze else '') +
                                    ('verbose ' if verbose else '') +
                                    ('analyze ' if analyze else '') +
                                    (table + (' ' + column if column else '') if table else '') + ';')
        conn.set_isolation_level(old_isolation_level)


def analyze(verbose: bool = False, table: str = None, column: str = None):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        old_isolation_level = conn.isolation_level
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute('analyze ' + ('verbose ' if verbose else '') +
                                    (table + (' ' + column if column else '') if table else '') + ';')
        conn.set_isolation_level(old_isolation_level)


def import_sql_file(file_name: str):
    with open(file_name, mode="r", encoding="UTF-8") as sqlfile:
        with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
            with conn.cursor() as cur:
                for line in sqlfile:
                    cur.execute(line)


def execute_query(query: str):
    with psycopg2.connect(dbname=dbname, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            if cur.rownumber:
                return cur.fetchall()
```







## Install PG_Jieba [u](https://github.com/jaiminpan/pg_jieba)

which pg_config



CentOS7 编译成功 https://github.com/jaiminpan/pg_jieba



```
yum groupinstall "Development Tools"
```


```
yum install centos-release-scl-rh
yum install llvm-toolset-7-clang
yum install postgresql13-devel
```

export PostgreSQL_ROOT=/usr/pgsql-13



submodule 拉取错误(git submodule update --init --recursive)


```
git submodule foreach git pull
```



cmake  -DCMAKE_PREFIX_PATH=/usr/pgsql-13  -DPostgreSQL_TYPE_INCLUDE_DIR=/usr/pgsql-13/include/server/ ..



pg_config 在这个目录，但是CMAKE 找不到

ls /usr/pgsql-13/bin/

```
export PATH=$PATH:/usr/pgsql-13/bin/
```

c99 错误

```
# 在Cmakelist.txt 加一句
set(CMAKE_C_FLAGS "-std=gnu99")
```

CXX错误

```
# 在Cmakelist.txt 加一句
set(CMAKE_CXX_FLAGS "-std=c++11")
```



cmake  -DCMAKE_PREFIX_PATH=/usr/pgsql-13  -DPostgreSQL_TYPE_INCLUDE_DIR=/usr/pgsql-13/include/server/ ..



```bash
# centos7 成功，比ubuntu 复杂很多，上方设置都需要
[root@2416f0b833b2 build]# make install
[100%] Built target pg_jieba
Install the project...
-- Install configuration: ""
-- Installing: /usr/pgsql-13/lib/pg_jieba.so
-- Installing: /usr/pgsql-13/share/extension/pg_jieba.control
-- Installing: /usr/pgsql-13/share/extension/pg_jieba--1.1.1.sql
-- Installing: /usr/pgsql-13/share/tsearch_data/jieba_base.dict
-- Installing: /usr/pgsql-13/share/tsearch_data/jieba_hmm.model
-- Installing: /usr/pgsql-13/share/tsearch_data/jieba_user.dict
-- Installing: /usr/pgsql-13/share/tsearch_data/jieba.stop
-- Installing: /usr/pgsql-13/share/tsearch_data/jieba.idf
```





```bash
# ubuntu 比较简单，以下几就就可以成功
cmake -DPostgreSQL_TYPE_INCLUDE_DIR=/usr/include/postgresql/13/server/ ..
make
make install

-- Installing: /usr/lib/postgresql/13/lib/pg_jieba.so
-- Installing: /usr/share/postgresql/13/extension/pg_jieba.control
-- Installing: /usr/share/postgresql/13/extension/pg_jieba--1.1.1.sql
-- Installing: /usr/share/postgresql/13/tsearch_data/jieba_base.dict
-- Installing: /usr/share/postgresql/13/tsearch_data/jieba_hmm.model
-- Installing: /usr/share/postgresql/13/tsearch_data/jieba_user.dict
-- Installing: /usr/share/postgresql/13/tsearch_data/jieba.stop
-- Installing: /usr/share/postgresql/13/tsearch_data/jieba.idf
```



```mysql
sudo -u postgres psql
create extension pg_jieba;
select * from to_tsquery('jiebacfg', '是拖拉机学院手扶拖拉机专业的。不用多久，我就会升职加薪，当上CEO，走上人生巅峰。');
select * from to_tsquery('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。');
```



替换成同时支持简繁的字典

```
proxy wget https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big

# 出错了，不用替换也可以查繁体
cp  /usr/share/postgresql/13/tsearch_data/jieba_user.dict
```



## Install pgroonga

https://pgroonga.github.io/install/



## 事务



PostgreSQL 事务 [u](https://www.jianshu.com/p/f35d01b95a38)

> 默认情况下 PostgreSQL会将每一个SQL语句都作为一个事务来执行。如果我们没有发出BEGIN命令，则每个独立的语句都会被加上一个隐式的BEGIN以及（如果成功）COMMIT来包围它。一组被BEGIN和COMMIT包围的语句也被称为一个事务块。
>
> 
>
> ```sql
> BEGIN;
> UPDATE accounts SET balance = balance - 100.00
>     WHERE name = 'Alice';
> COMMIT;
> ```



## 分词



```
前言  
PostgreSQL 被称为是“最高级的开源数据库”，它的数据类型非常丰富，用它来解决一些比较偏门的需求非常适合。  
  
前些天将 POI 点关键词查询的功能迁到了 PgSQL，总算对前文 空间索引 - 各数据库空间索引使用报告 有了一个交代。  
  
由于 PgSQL 国内的资料较少，迁移过程踩了不少坑，这里总结记录一下，帮助后来的同学能顺利使用 PgSQL。而且目前在灰度测试刚布了一台机器，后续可能还要添加机器，整理一下流程总是好的。  
  
文章经常被人爬，而且还不注明原地址，我在这里的更新和纠错没法同步，这里注明一下原文地址：http://www.cnblogs.com/zhenbianshu/p/7795247.html  
  
开始  
安装  
首先是安装 PgSQL，这里我使用的是 PgSQL 9.6，PgSQL 10 也刚发布了，有兴趣的可以尝下鲜。  
  
PgSQL 的安装可以说非常复杂了，除了要安装 Server 和 Client 外，还需要安装 devel 包。为了实现空间索引功能，我们还要安装最重要的 PostGIS 插件，此插件需要很多依赖，自己手动安装非常复杂而且很可能出错。  
  
推荐自动化方式安装，Yum 一定要配合 epel 这样的 Yum 源，保障能将依赖一网打尽。当然最好的还是使用 docker 来运行，找个镜像就行了。  
  
插件  
由于 PgSQL 的很多功能都由插件实现，所以还要安装一些常用的插件，如:  
  
postgis_topology（管理面、边、点等拓扑对象）  
pgrouting（路径规划）  
postgis_sfcgal（实现3D相关算法）  
fuzzystrmatch（字符串相似度计算）  
address_standardizer/address_standardizer_data_us（地址标准化）  
pg_trgm（分词索引）  
这些插件在安装目录 /path/extensions 下编译完毕后，在数据库中使用前要先使用 create extension xxx 启用。  
  
启动  
切换到非 root 用户。（PgSQL 在安装完毕后会创建一个名为 postgres 的超级用户，我们可以使用这个超级用户来操作 PgSQL，后期建议重新创建一个普通用户用来管理数据）；  
切换到 /installPath/bin/ 目录下，PgSQL 在此目录下提供了很多命令，如 createdb、createuser、dropdb、pg_dump 等；  
使用 createdb 命令初始化一个文件夹 dir_db (此目录不能已存在)存放数据库物理数据，使用 -E UTF8 参数指定数据库字符集为 utf-8；  
使用 pg_ctl -D dir_db 指定数据库启动后台服务；  
使用 psql -d db 在命令行登陆 PgSQL;  
配置  
安装完毕后还要配置一些比较基本的参数才能正常使用。  
  
Host权限  
PgSQL需要在 pg_hba.conf 文件中配置数据库 Host 权限，才能被其他机器访问。  
  
# TYPE  DATABASE        USER            ADDRESS                 METHOD  
local   all             all                                     trust  
host    all             all             127.0.0.1/32            md5  
host    all             all             172.16.0.1/16            md5  
文件中注释部分对这几个字段介绍得比较详细， 我们很可能需要添加 host(IP) 访问项， ADDRESS 是普通的网段表示法，METHOD 推荐使用 md5，表示使用 md5 加密传输密码。  
  
服务器配置  
服务器配置在 postgresql.conf中，修改配置后需要 使用 pg_ctl restart -D dir_db 命令重启数据库；  
  
此外，我们也可以在登陆数据库后修改配置项：使用 SELECT * FROM pg_settings WHERE name = 'config'; 查询当前配置项，再使用 UPDATE 语句更新配置。但有些配置如内存分配策略是只在当前 session 生效的，全局生效需要在配置文件中修改，再重启服务器。  
  
我们可以修改配置并用客户端验证 SQL 语句的优化，使用 \timing on 开启查询计时，使用 EXPLAIN ANALYSE 语句 分析查询语句效率。 下面介绍两个已实践过的配置参数：  
  
shared_buffers：用于指定共享内存缓冲区所占用的内存量。它应该足够大来存储常使用的查询结果，以减少物理I/O。但它也不能太大，以避免系统 内存swap 的发生， 一般设置为系统内存的 20%。  
work_mem：一个连接的工作内存，在查询结果数据量较大时，此值如果较小的话，会导致大量系统 I/O，导致查询速度急剧下降，如果你的 explain 语句内 buffer 部分 read数值过大，则表示工作内存不足，需要调整加此参数。但此值也不能太大，需要保证 work_mem * max_connections + shared_buffers + 系统内存 < RAM，不然同样可能会导致系统 内存swap。  
这样，PgSQL 就能作为一个正常的关系型数据使用了。  
  
分词  
全文索引的实现要靠 PgSQL 的 gin 索引。分词功能 PgSQL 内置了英文、西班牙文等，但中文分词需要借助开源插件 zhparser；  
  
SCWS  
要使用 zhparser，我们首先要安装 SCWS 分词库，SCWS 是 Simple Chinese Word Segmentation 的首字母缩写（即：简易中文分词系统），其 GitHub 项目地址为 hightman-scws，我们下载之后可以直接安装。  
  
安装完后，就可以在命令行中使用 scws 命令进行测试分词了， 其参数主要有：  
  
-c utf8 指定字符集  
-d dict 指定字典 可以是 xdb 或 txt 格式  
-M 复合分词的级别， 1~15，按位异或的 1|2|4|8 依次表示 短词|二元|主要字|全部字，默认不复合分词，这个参数可以帮助调整到最想要的分词效果。  
zhpaser  
下载 zhparser 源码 git clone https:github.com/amutu/zhparser.git；  
安装前需要先配置环境变量：export PATH=$PATH:/path/to/pgsql；  
make && make install编译 zhparser；  
登陆 PgSQL 使用 CREATE EXTENSION zhparser; 启用插件；  
添加分词配置  
  
CREATE TEXT SEARCH CONFIGURATION parser_name (PARSER = zhparser); // 添加配置  
ALTER TEXT SEARCH CONFIGURATION parser_name ADD MAPPING FOR n,v,a,i,e,l,j WITH simple; // 设置分词规则 （n 名词 v 动词等，详情阅读下面的文档）  
给某一列的分词结果添加 gin 索引 create index idx_name on table using gin(to_tsvector('parser_name', field));  
  
在命令行中使用上一节中介绍的 scws 命令测试分词配置，如我认为复合等级为 7 时分词结果最好，则我在 postgresql.conf添加配置  
  
zhparser.multi_short = true #短词复合: 1  
zhparser.multi_duality = true  #散字二元复合: 2  
zhparser.multi_zmain = true  #重要单字复合: 4  
zhparser.multi_zall = false  #全部单字复合: 8  
SQL  
查询中我们可以使用最简单的 SELECT * FROM table WHERE to_tsvector('parser_name', field) @@ 'word' 来查询 field 字段分词中带有 word 一词的数据；  
  
使用 to_tsquery() 方法将句子解析成各个词的组合向量，如 国家大剧院 的返回结果为 '国家' & '大剧院' & '大剧' & '剧院' ，当然我们也可以使用 & | 符号拼接自己需要的向量；在查询 长句 时，可以使用 SELECT * FROM table WHERE to_tsvector('parser_name', field) @@ to_tsquery('parser_name','words')；  
  
有时候我们想像 MySQL 的 SQL_CALC_FOUND_ROWS 语句一样同步返回结果条数，则可以使用 SELECT COUNT(*) OVER() AS score FROM table WHERE ...，PgSQL 会在每一行数据添加 score 字段存储查询到的总结果条数；  
  
到这里，普通的全文检索需求已经实现了。  
  
优化  
我们接着对分词效果和效率进行优化：  
  
存储分词结果  
我们可以使用一个字段来存储分词向量，并在此字段上创建索引来更优地使用分词索引：  
  
ALTER TABLE table ADD COLUMN tsv_column tsvector;           // 添加一个分词字段  
UPDATE table SET tsv_column = to_tsvector('parser_name', coalesce(field,''));   // 将字段的分词向量更新到新字段中  
CREATE INDEX idx_gin_zhcn ON table USING GIN(tsv_column);   // 在新字段上创建索引  
CREATE TRIGGER trigger_name BEFORE INSERT OR UPDATE  ON table FOR EACH ROW EXECUTE PROCEDURE  
tsvector_update_trigger(tsv_column, 'parser_name', field); // 创建一个更新分词触发器  
这样，再进行查询时就可以直接使用 SELECT * FROM table WHERE tsv_column @@ 'keyword' 了。  
  
这里需要注意，这时候在往表内插入数据的时候，可能会报错，提示指定 parser_name 的 schema， 这时候可以使用 \dF 命令查看所有 text search configuration 的参数：  
  
List of text search configurations  
Schema   |    Name    |              Description  
------------+------------+---------------------------------------  
pg_catalog | english    | configuration for english language  
public     | myparser   |  
注意 schema 参数，在创建 trigger 时需要指定 schema， 如上面，就需要使用 public.myparser。  
  
添加自定义词典  
我们可以在网上下载 xdb 格式的词库来替代默认词典，词库放在 share/tsearch_data/ 文件夹下才能被 PgSQL 读取到，默认使用的词库是 dict.utf8.xdb。要使用自定义词库，可以将词库放在词库文件夹后，在 postgresql.conf 配置 zhparser.extra_dict="mydict.xdb" 参数；  
  
当我们只有 txt 的词库，想把这个词库作为默认词库该怎么办呢？使用 scws 带的scwe-gen-dict 工具或网上找的脚本生成 xdb 后放入词库文件夹后，在 PgSQL 中分词一直报错，读取词库文件失败。我经过多次实验，总结出了一套制作一个词典文件的方法：  
  
准备词库源文件 mydict.txt：词库文件的内容每一行的格式为词 TF IDF 词性，词是必须的，而 TF 词频(Term Frequency)、IDF 反文档频率(Inverse Document Frequency) 和 词性 都是可选的，除非确定自己的词典资料是对的且符合 scws 的配置，不然最好还是留空，让 scws 自已确定；  
在 postgresql.conf 中设置 zhparse  
3ff7  
r.extra_dicts = "mydict.txt" 同时设置 zhparser.dict_in_memory = true；  
命令行进入 PgSQL，执行一条分词语句 select to_tsquery('parser', '随便一个词') ，分词会极慢，请耐心(请保证此时只有一个分词语句在执行)；  
分词成功后，在/tmp/目录下找到生成的 scws-xxxx.xdb 替换掉 share/tsearch_data/dict.utf8.xdb；  
删除刚加入的 extra_dicts dict_in_memory 配置，重启服务器。  
扩展  
由于查询的是 POI 的名称，一般较短，且很多词并无语义，又考虑到用户的输入习惯，一般会输入 POI 名称的前几个字符，而且 scws 的分词准确率也不能达到100%，于是我添加了名称的前缀查询来提高查询的准确率，即使用 B树索引 实现 LIKE '关键词%' 的查询。这里需  
  
这里要注意的是，创建索引时要根据字段类型配置 操作符类，不然索引可能会不生效，如在 字段类型为 varchar 的字段上创建索引需要使用语句CREATE INDEX idx_name ON table(COLUMN varchar_pattern_ops)，这里的 varcharpatternops 就是操作符类，操作符类的介绍和选择可以查看文档：11.9. 操作符类和操作符族。  
  
自此，一个良好的全文检索系统就完成了。  
  
总结  
简单的数据迁移并不是终点，后续要做的还有很多，如整个系统的数据同步、查询效率优化、查询功能优化（添加拼音搜索、模糊搜索）等。特别是查询效率，不知道是不是我配置有问题，完全达不到那种 E级毫秒 的速度，1kw 的数据效率在进行大结果返回时就大幅下降（200ms），只好老老实实地提前进行了分表，目前百万级查询速度在 20ms 以内，优化还有一段路要走。  
  
不过这次倒是对 技术的“生态”有了个更深的体会，这方面 PgSQL 确实和 MySQL 差远了，使用 MySQL 时再奇葩的问题都能在网上快速找到答案，而 PgSQL 就尴尬了，入门级的问题搜索 stackoverflow 来来回回就那么几个对不上的回答。虽然也有阿里的“德哥”一样的大神在辛苦布道，但用户的数量才是根本。不过，随着 PgSQL 越来越完善，使用它的人一定会越来越多的，我这篇文章也算是为 PgSQL 加温了吧，哈哈~希望能帮到后来的使用者。  
  
关于本文有什么问题可以在下面留言交流，如果您觉得本文对您有帮助，可以点击下面的 推荐 支持一下我，博客一直在更新，欢迎 关注 。  
  
参考：  
  
PostgreSQL系统配置优化  
  
[PG]使用 zhparser 进行中文分词全文检索  
  
SCWS 中文分词  
  
Fast Search Using PostgreSQL Trigram Indexes  
  
使用阿里云PostgreSQL zhparser时不可不知的几个参数  
  
德哥的PostgreSQL私房菜 - 史上最屌PG资料合集  
```



## FTS



PostgreSQL 全文检索加速 快到没有朋友 - RUM索引接口(潘多拉魔盒) [u](https://github.com/digoal/blog/blob/master/201610/20161019_01.md)



RUM索引

- 安装 https://github.com/postgrespro/rum

短语搜索



> create extension rum;
>
> CREATE INDEX fts_rum_studio ON studio USING rum (v_zh rum_tsvector_ops);



## a

```bash
C:\>w2 start -z rootCA.crt
```



```python

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

#host = 'xxxxx.195'
host = '127.0.0.1'
#host = 'xxx.166'



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

                    print(type( js['article']['body']['idioms'] ))
                    
                    if js['article']['body']['idioms'] != None:
                        idiom['idiom'] = js['article']['body']['idioms']['idiom']


# createDatabase_studio()
createDatabase_economistglobl()

```



## Docker

```
docker exec -it centos7PG10 /bin/bash
docker ps -a
docker inspect
exit  (quit)
CTRL + P + Q (quit)
docker inspect container_name | grep IPAddress
  --> 172.18.0.3
# 需要更多IP 时
iptables -t nat -A  DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22
```





```
# https://yeasy.gitbook.io/docker_practice/image/pull
# 进入docker
docker run -it --rm ubuntu:18.04 bash
```

```bash
只习惯用Centos系统，但是有些软件编译安装很麻烦不方便，但是呢在Ubuntu中就变得容易方便，所以我打算用docker运行Ubuntu系统弥补Centos短板和不足之处；

项目地址：https://hub.docker.com/_/ubuntu/

1、安装Ubuntu系统命令：
docker pull ubuntu
这是一个极度精简的系统，连最基本的wget命令都没有；所以先要apt-get update升级系统和安装apt-get install wget命令；

2、运行进入Ubuntu系统命令：
docker run -ti ubuntu bash

3、正确退出系统方式：
先按，ctrl+p
再按，ctrl+q
绝对不能使用exit或者ctrl+d来退出，这样整个系统就退出了！！！

4、共享宿主机目录到Ubuntu系统中：
docker run -it -v /AAA:/BBB ubuntu bash
这样宿主机根目录中的AAA文件夹就映射到了容器Ubuntu中去了，两者之间能够共享；

5、登陆docker中的ubuntu镜像系统：
docker run -ti ubuntu /bin/bash
#6866 是 IMAGE ID 前四位数字-能区分出是哪个image即可

6、退出后 再进入ubuntu
1、首先用docker ps -a 查找到该CONTAINER ID对应编号（比如：0a3309a3b29e）
2、进入该系统docker attach 0a3309a3b29e （此时没反应，ctrl+c就进入到ubuntu系统中去了）

PS:我运行的命令

docker run -it -v /download:/download -p 53:53 ubuntu bash

附加常用命令：
一、查看ubuntu版本：cat /etc/issue
二、修改ubuntu镜像源为ubuntu：
1、备份 cp /etc/apt/sources.list /etc/apt/sources.list.backup
2、清空内容加入以下内容 vi /etc/apt/sources.list

3、更新生效：apt-get update

三、安装开启ssh运行用户远程登录
1、安装sshd命令：apt-get install openssh-server openssh-client

2、编辑/etc/ssh/sshd_config ，注释掉：PermitRootLogin without-password，增加PermitRootLogin yes

3、启动命令
service ssh start
service ssh stop
service ssh restart
```



### Xshell如何连接Docker容器中的Linux

```

# https://blog.csdn.net/u010046887/article/details/90406725

步骤一：配置centos:7 容器SSH服务
 
# 1、获取系统镜像
[root@izwz9eftauv7x69f5jvi96z ~]# docker pull centos:7 
# 2、启动（可以使用systemd管理服务进程）
[root@izwz9eftauv7x69f5jvi96z ~]# docker run -tdi --privileged centos init
# 3、进入容器的bash
[root@izwz9eftauv7x69f5jvi96z ~]# docker ps
CONTAINER ID        IMAGE                                  COMMAND                  CREATED             STATUS              PORTS                         NAMES
0d77d1bf15b3        centos                                 "init"                   8 seconds ago       Up 8 seconds                                      elegant_joliot
[root@d26c58c4f740 /]# docker exec -it 0d bash
# 4、修改root密码，初始化密码Qwer1234
[root@d26c58c4f740 /]# passwd
Changing password for user root.
New password: 
BAD PASSWORD: The password fails the dictionary check - it is too simplistic/systematic
Retype new password: 
passwd: all authentication tokens updated successfully.
# 5、安装容器的openssh-server
[root@d26c58c4f740 /]# yum install openssh-server -y
………………
# 6、修改/etc/ssh/sshd_config配置并保存：PermitRootLogin yes    UsePAM no
[root@d26c58c4f740 /]# vi /etc/ssh/sshd_config
 
# 7、启动ssh服务
[root@0d77d1bf15b3 /]# systemctl start sshd
# 8、退出容器
[root@0d77d1bf15b3 /]# exit
exit
步骤二：构建并启动镜像

# 1、查看刚刚的容器ID
[root@izwz9eftauv7x69f5jvi96z ~]# docker ps
CONTAINER ID        IMAGE                                  COMMAND                  CREATED             STATUS              PORTS                         NAMES
0d77d1bf15b3        centos                                 "init"                   5 minutes ago       Up 5 minutes                                      elegant_joliot  
 
# 2、通过commit构建镜像
[root@izwz9eftauv7x69f5jvi96z ~]# docker commit \
> --author "wwx<wuweixiang.alex@gmail.com>" \
> --message "容器centos开启远程ssh成功" \
> 0d \
> wuweixiang/centos7-ssh:1.0.0
sha256:983d8f4594dc6ef98d0432c34331faa307a82e85bd15ed1a6d15bfb91bc81359
 
# 3、启动这个镜像的容器，并映射本地的一个闲置的端口（例如10000）到容器的22端口
[root@izwz9eftauv7x69f5jvi96z ~]# docker images
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
wuweixiang/centos7-ssh          1.0.0               983d8f4594dc        2 minutes ago       302MB
[root@izwz9eftauv7x69f5jvi96z ~]# docker run -d -p 10000:22 --name wwx-centos7-ssh 983 /usr/sbin/sshd -D
9004a532ed73cee18fb804cd2e36491785b26df885fb20f226929dd4428df859
三、用Xshell进行ssh连接成功
Connecting to 112.74.185.172:10000...
Connection established.
To escape to local shell, press 'Ctrl+Alt+]'.
 
Last login: Fri Nov 23 07:58:34 2018 from 120.42.130.201
[root@9004a532ed73 ~]#
```



docker ps -a  # 全部状态都列出来，强大一些

docker start centos7



### 移除镜像

docker images

docker rmi xxx



### 移除容器

docker stop 17b3d18c1428

docker rm 17b3d18c1428









docker pull centos:7

docker run -it --rm centos:7 bash

```
# 特权模式创建容器
docker run -tid --name centos7 -p 222:22 --privileged=true centos:7 /sbin/init 
		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口
# 运行
docker exec -it centos7 /bin/bash
# 安装ssh
yum install openssh-server -y
# 修改配置
vi /etc/ssh/sshd_config
PermitRootLogin yes # 改成这个
UsePAM no # 改成这个
# 启动ssh
systemctl start sshd
# 退出容器
eixt

# 查看容器的IP
docker inspect centos7 | grep IPAddress
  --> "IPAddress": "172.18.0.3"

# 登录看看
ssh root@172.18.0.3
  --> 成功






```

https://plutoacharon.github.io/2020/02/23/Docker%E5%AE%B9%E5%99%A8%E5%87%BA%E7%8E%B0%E4%BD%BF%E7%94%A8systemctl%E9%97%AE%E9%A2%98%EF%BC%9AFailed-to-get-D-Bus-connection-Operation-not-permitted/



### 如果需要更多的端口映射

```
# https://blog.opensvc.net/yun-xing-zhong-de-dockerrong-qi/

# 已有端口映射
iptables -t nat -vnL DOCKER
  --> tcp dpt:8083 to:172.18.0.2:8083
  --> tcp dpt:54322 to:172.18.0.3:5432

# 这种方法每次docker 重启会失效
iptables -t nat -A DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22

# 获取规则编号
iptables -t nat -nL --line-number

# 删除某条规则
iptables -t nat -D DOCKER 编号

```







```
# https://www.jianshu.com/p/5c71b4f40612

docker ps -a
docker inspect 短hash # 然后得到长ID
vi /var/lib/docker/containers/2416f0b833b226332db69fe5a5664d3ce6b11adfe8956be293ff87d6995bdebc/hostconfig.json

# 已有端口映射
"PortBindings":{"5432/tcp":[{"HostIp":"","HostPort":"54322"}]}

cp /var/lib/docker/containers/2416f0b833b226332db69fe5a5664d3ce6b11adfe8956be293ff87d6995bdebc/hostconfig.json /var/lib/docker/containers/2416f0b833b226332db69fe5a5664d3ce6b11adfe8956be293ff87d6995bdebc/hostconfig.json-backup

# 增加新的
"PortBindings":{"5432/tcp":[{"HostIp":"","HostPort":"54322"}],"22/tcp":[{"HostIp":"","HostPort":"222"}]} # 这里是直接改

cp /var/lib/docker/containers/2416f0b833b226332db69fe5a5664d3ce6b11adfe8956be293ff87d6995bdebc/config.v2.json /var/lib/docker/containers/2416f0b833b226332db69fe5a5664d3ce6b11adfe8956be293ff87d6995bdebc/config.v2.json-backup

vi /var/lib/docker/containers/2416f0b833b226332db69fe5a5664d3ce6b11adfe8956be293ff87d6995bdebc/config.v2.json

# 已有
"ExposedPorts":{"5432/tcp":{}}

# 增加
"ExposedPorts":{"5432/tcp":{},"22/tcp":{}} # 原
"ExposedPorts":{"22/tcp":{}} # 在它后面加

service docker restart

# 查看配置，是否修改成功
docker inspect 短hash

docker start xxx
```



```
 "Config": {
  "ExposedPorts": {
   // 添加内部端口5432映射
   "5432/tcp": {},
   "8080/tcp": {}
  },s
  ...
 },

"PortBindings":{
  // 添加内部端口以及外部端口15432
  "5432/tcp":[
   {
    "HostIp":"",
    "HostPort":"15432"
   }
  ],
  "8080/tcp":[
   {
    "HostIp":"",
    "HostPort":"28080"
   }
  ]
 },
```







```
# 将宿主机的222端口映射到IP为172.18.0.3容器的22端口
# 些方法可以用于增加额外的端口？？？
iptables -t nat -A  DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22
```





1、获得容器IP
将container_name 换成实际环境中的容器名
docker inspect `container_name` | grep IPAddress

2、iptable转发端口
将宿主机的8888端口映射到IP为192.168.1.15容器的8080端口
iptables -t nat -A  DOCKER -p tcp --dport 8888 -j DNAT --to-destination 192.168.1.15:8080



一、添加docker容器端口映射
以tomcat容器为例：

root@localhost /]# docker run --name mytomcat -d -p 8888:8080 tomcat
1
–name：创建的tomcat镜像名称
‐d：后台运行
‐p：将主机的端口映射到容器的一个端口，8888:8080代表：主机端口:容器内部的端口

执行完会返回新创建的tomcat镜像ID




### Docker 中的postgreql



```
# 特权模式创建容器
docker run -tid --name centos7PG10 -p 54322:5432 --privileged=true centos:7 /sbin/init 
		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口

# 运行docker 的shell
docker exec -it centos7PG10 /bin/bash

# 安装PG13
yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

yum -y update
yum search postgresql13
yum -y install postgresql13 postgresql13-server
/usr/pgsql-13/bin/postgresql-13-setup initdb
systemctl start postgresql-13
systemctl status postgresql-13
systemctl enable postgresql-13 # 自启动

# 改强密码
su - postgres
psql -c "alter user postgres with password '这里填的一个强密码'"
# 允许运程连接
vi /var/lib/pgsql/13/data/postgresql.conf
	listen_addresses = '*' # 改成这个
vi /var/lib/pgsql/13/data/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  trust  
	# 加在最后面，接受所有远程IP

systemctl restart postgresql-13

# docker 连接测试
psql -h 127.0.0.1 -p 5432 -U postgres  # 注意端口
  --> 成功
# 宿主连接测试
psql -h 127.0.0.1 -p 54322 -U postgres # 注意端口
  --> 成功
  
```

<img src="postgresql summary.assets/image-20210330185047454.png" alt="image-20210330185047454" style="zoom:50%;" />

**navicat 连接**



#### 启动已停止的容器

docker start 2416f0b833b2







## RUM



好文

https://www.mengqingzhong.com/2020/10/01/postgresql-index-rum-8/



我们再一个相对大一点的数据比较GIN和RUM：找出包含hello和hackers的十篇最相关的文档。

```sql
explain (costs off, analyze)
select * from mail_messages
where tsv @@ to_tsquery('hello & hackers')
order by ts_rank(tsv,to_tsquery('hello & hackers'))
limit 10;
```



select id, en, zh, type from studio where v_zh @@ to_tsquery('jiebacfg', '情緒') ORDER BY RANDOM() limit 3;



SELECT id, ts_headline(body, q), rank

FROM (SELECT id, body, q, ts_rank_cd(ti, q) AS rank

   FROM apod, to_tsquery('stars') q

   WHERE ti @@ q

   ORDER BY rank DESC

   LIMIT 10) AS foo;



```
 # rise err
 sql = f"SELECT id, ts_headline(en, q) as en, zh, type \
                FROM studio, plainto_tsquery('en', '{keywd}') q \
                WHERE v_en @@ q \
                ORDER BY RANDOM() LIMIT 3 ;"
```



```sql
drop index tsv_gin;
create index tsv_rum on mail_messages using rum(tsv);
```



这个索引包含了所有所需的信息，查询非常精确：

```sql
explain (costs off, analyze)
select * from mail_messages
where tsv @@ to_tsquery('hello <-> hackers');
```



**create index en_rum on studio using rum(en);**



SELECT id, ts_headline(en, q) as en, zh, type \

FROM studio, to_tsquery('rebell')  q

where en @@ to_tsquery('rebell')





# 调试



```
https://gist.github.com/jhngrant/c1787346fcb4b0e3001a
https://www.techsupportpk.com/2020/12/how-to-install-pldebugger-centos.html

plugin_debugger

# GFW https://github.com/TyrantLucifer/ssr-command-client
yum install -y python3
shadowsocksr-cli --add-url https://subscription.ftwapi.com/link/xxxxxxx?sub=1
shadowsocksr-cli -u

git clone https://git.postgresql.org/git/pldebugger.git
cd pldebugger
PATH=$PATH:/usr/pgsql-13/bin
export PATH
export USE_PGXS=1
yum -y install gcc gcc-c++ kernel-devel make git nano openssl openssl-devel krb5-libs krb5-devel
make
make install
	--> '/usr/pgsql-13/lib/plugin_debugger.so'


vi /var/lib/pgsql/13/data/postgresql.conf
shared_preload_libraries = 'plugin_debugger' # 找到这一句，改成这样

systemctl restart postgresql-13


su postgres
psql
CREATE EXTENSION pldbgapi;
\q

```



```
http://www.postgres.cn/docs/9.4/functions-json.html

'[1,2,3]'::json->>2  # 数组，索引2
	--> 3
'{"a":1,"b":2}'::json->>'b' # json 索引 "b"
	--> 2



```





```mysql

CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
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





SELECT ja_reading ('します');
-- 

/*
{"{\"value\":\"海\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"ウミ\"}}"}
{"{\"value\":\"1\",\"position\":0,\"force_prefix_search\":false}"}


SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
 --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}



*/
```







