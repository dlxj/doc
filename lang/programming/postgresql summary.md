## Install PG

centos7 install [u](https://computingforgeeks.com/how-to-install-postgresql-13-on-centos-7/)



用**Navicat** 客户端查数据

- HeidiSQL 有点问题


```bash
apt install postgresql-server-dev-13
find / -name "postgres.h" -print  # 后面编译pg_jieba 要用
```



After fresh installation of PostgreSQL 13 on **CentOS 7** initialization is required.

```
$ sudo /usr/pgsql-13/bin/postgresql-13-setup initdb
Initializing database ... OK
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

# sql 语句里本身有单引号时用两个单引号来还替之

"""
GFW
https://www.ishells.cn/archives/linux-ssr-server-client-install
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlite3 as sqlite # Python 自带的


with psycopg2.connect(database='postgres', user='postgres', password='postgres',host='111.229.53.195', port='5432') as conn:
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with conn.cursor() as cur:
        cur.execute("DROP DATABASE IF EXISTS studio;")
        cur.execute("CREATE DATABASE studio \
            WITH OWNER = postgres \
            ENCODING = 'UTF8' \
            TABLESPACE = pg_default \
            CONNECTION LIMIT = -1 \
            TEMPLATE template0;")

with psycopg2.connect(database='studio', user='postgres', password='postgres',host='111.229.53.195', port='5432') as conn:
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
        cur.execute("create extension pg_jieba;")
        cur.execute("insert into studio(en, zh, type, time, v_en, v_zh ) values('When something does not go as you expected and you feel anxious or upset, it helps to understand that these feelings are part of the package.', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。','AD050851', '01:20.3', 'no', to_tsvector('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。'));")
        
        cx = sqlite.connect('./db/studioclassroom.db')
        cu = cx.cursor()
        cu.execute("SELECT * FROM studioclassroom_content;", [])
        rows = cu.fetchall()
        cx.commit()
        cx.close()

        row = rows[0]
        print(row[0])
        print(row[1])
        print(row[2])

print('hi')
```






## nodejs

https://github.com/sehrope/node-pg-db



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



```bash
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





## a

```bash
C:\>w2 start -z rootCA.crt
```

