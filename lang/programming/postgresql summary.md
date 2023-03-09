## Install PG

```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目

```

## nohup

```bash
# 加 -u 才能看到打印的输出
nohup python3.8 -u anime_Danganronpa_version1.py >outlog &
tail -f outlog
jobs -l # 查看运行中的进程
ps -aux | grep "anime_Danganronpa_version1.py"

kill -9 $(lsof outlog | tail -n +2  | awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:8077 | tail -n +2  | awk '{print $2}' | tr '\n' ' ')

```



https://github.com/ShadowsocksR-Live/shadowsocksr-native

```
curl --proxy socks5h://127.0.0.1:1080 www.google.com

```





不好用的代理  https://github.com/TyrantLucifer/ssr-command-client

```
重置订阅链接 shadowsocksr-cli --setting-url https://tyrantlucifer.com/ssr/ssr.txt
更新订阅列表 shadowsocksr-cli -u
打印节点列表 shadowsocksr-cli -l
开启美国节点代理 shadowsocksr-cli -s 1


查看订阅链接列表 shadowsocksr-cli --list-url
查看本地监听地址 shadowsocksr-cli --list-address
```



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
hostnossl    all          all            0.0.0.0/0  md5        
```

and this was modified in `postgresql.conf`, as shown:

```sql
# vi /etc/postgresql/13/main/postgresql.conf
listen_addresses = '*'  
```



```nodejs
npm install pg
```





## 备份表



```
# http://blog.itpub.net/28833846/viewspace-2742419/
PGPASSWORD="postgres" pg_dump -h 127.0.0.1 -U postgres -p 5432 -d touch -t public.anime --inserts | gzip -9 > ./touch_$(date +%Y-%m-%d).psql.gz

	# PGPASSWORD="xxx" pg_dump -h 127.0.0.1 -U postgres -p 5432 -d anime -t public.anime --inserts | gzip -9 > ./anime_$(date +%Y-%m-%d).psql.gz

	# sudo -u postgres psql
	# SHOW data_directory;
	ls -al 
	/var/lib/pgsql/13/data -> /mnt/psqldata  # 建了软链
	
	du -h --max-depth=9 /mnt/psqldata # 三个mkv 大小1G 
	
	PGPASSWORD="xxx" pg_dump -U postgres -h localhost anime > anime.pgsql # 成功
	
	PGPASSWORD="xxx" pg_dump -U postgres -h localhost anime | gzip -9 > ./anime_$(date +%Y-%m-%d).psql.gz
	
	psql -h 127.0.0.1 -p 5432 -U postgres # 提示输入密码
	


# 恢复数据库

#先建db
CREATE DATABASE anime WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default CONNECTION LIMIT = -1 TEMPLATE template0;

PGPASSWORD="xxx" psql -h 127.0.0.1 -p 5432 -U postgres -d anime -f anime_2021-07-11.psql

	
```





```
一、备份表

    1. 这里使用的是Linux服务器，首先进入安装当前数据库的服务器，可以在home目录下新建一个文件夹。

    2.输入命令：  pg_dump -t 表名 -U postgres 数据库名 > 备份文件名.dump

        例如：pg_dump -t user -t dept -t employee -U postgres test_table > test_copy.dump

       这样就可以实现多表同时备份。

二、还原表

     输入命令：psql -d 数据库名 -U postgres -f 备份文件名.dump

    例如：psql -d test_table -U postgres -f test_copy.dump

```



## 跨库查询

- https://cloud.tencent.com/document/product/409/67298

  ```
  yum install postgresql13-contrib
  
  create extension postgres_fdw;
  
  create server server_danganronpa2 foreign data wrapper postgres_fdw options (dbname 'danganronpa2'); 
  	# 不跨主机，仅跨数据库，指定 dbname 既可
  
  
  create foreign table remote_danganronpa2
  (
    "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (
  INCREMENT 1
  MINVALUE  1
  MAXVALUE 2147483647
  START 1
  ),
    "name" text COLLATE "pg_catalog"."default",
    "jp" text COLLATE "pg_catalog"."default",
    "zh" text COLLATE "pg_catalog"."default" DEFAULT ''::text,
    "en" text COLLATE "pg_catalog"."default" DEFAULT ''::text,
    "type" text COLLATE "pg_catalog"."default",
    "begintime" text COLLATE "pg_catalog"."default",
    "endtime" text COLLATE "pg_catalog"."default",
    "jp_ruby" text COLLATE "pg_catalog"."default",
    "jp_mecab" text COLLATE "pg_catalog"."default",
    "v_jp" tsvector,
    "v_zh" tsvector,
    "v_en" tsvector,
    "seasion" text COLLATE "pg_catalog"."default" DEFAULT ''::text,
    "seasionname" text COLLATE "pg_catalog"."default" DEFAULT ''::text,
    "episode" text COLLATE "pg_catalog"."default" DEFAULT ''::text,
    "audio" bytea,
    "video" bytea,
    "videoname" text COLLATE "pg_catalog"."default"
  ) server server_danganronpa2 options(table_name 'danganronpa');
  	# 创建外部表
  
  create user mapping for postgres server server_danganronpa2 options (user 'postgres',password 'password2');
  	# 
  	
  SELECT * FROM remote_danganronpa2 LIMIT 1;
  
  
  
  INSERT INTO anime ("name",
  jp,
  zh,
  en,
  "type",
  begintime,
  endtime,
  jp_ruby,
  jp_mecab,
  v_jp,
  v_zh,
  v_en,
  seasion,
  seasionname,
  episode,
  audio,
  video,
  videoname)
  
  SELECT 
  "name",
  jp,
  zh,
  en,
  "type",
  begintime,
  endtime,
  jp_ruby,
  jp_mecab,
  v_jp,
  v_zh,
  v_en,
  seasion,
  seasionname,
  episode,
  audio,
  video,
  videoname
  FROM remote_danganronpa2;
  
  ```

  

  ## 简介

  FDW（FOREIGN DATA WRAPPER，外部数据包装器）是 PostgreSQL 提供用于访问外部数据源的一类插件，外部数据源包括本实例其他库中数据或者其他实例的数据。使用过程包含以下步骤：

  1. 使用 “CREATE EXTENSION” 语句安装 FDW 插件。
  2. 使用 “CREATE SERVER” 语句，为每个需要连接的远程数据库创建一个外部服务器对象。指定除了 user 和 password 以外的连接信息作为服务器对象的选项。
  3. 使用 “CREATE USER MAPPING” 语句，为每个需要通过外部服务器访问的数据库创建用户映射。指定远程的帐号和密码作为映射用户的 user 和 password。
  4. 使用 “CREATE FOREIGN TABLE” 语句，为每个需要访问的远程表创建外部表。创建的外部表的对应列必须与远程表匹配。也可以在外部表中使用与远程表不同的表名和列名， 但前提是您必须将正确的远程对象名作为创建外部表对象的选项。

  由于 FDW 插件可以直接跨实例访问或在同实例中进行跨 database 访问。云数据库 PostgreSQL 对创建外部服务器对象时进行了权限控制优化，根据目标实例所在环境进行分类管理。在开源版本基础上增加了额外辅助参数，来验证用户身份和调整网络策略。

  ## postgres_fdw 插件辅助参数

  - **host**
    跨实例访问时候为必须项。目标实例的 IP 地址，postgres_fdw 使用。
  - **port**
    跨实例访问时候为必须项。目标实例的 port。
  - **instanceid**
    实例 ID
    a. 在云数据库 PostgreSQL 间跨实例访问时使用，当跨实例访问时为必选项。格式类似 postgres-xxxxxx、pgro-xxxxxx，可在 [控制台](https://console.cloud.tencent.com/postgres) 查看。
    b. 如果目标实例在腾讯云 CVM 上，则为 CVM 机器的实例 ID，格式类似 ins-xxxxx。
  - **dbname**
    database 名，填写需要访问的远端 PostgreSQL 服务的 database 名字。若不跨实例访问，仅在同实例中进行跨库访问，则只需要配置此参数即可，其他参数都可为空。
  - **access_type**
    非必须项。目标实例所属类型：
    1：目标实例为 TencentDB 实例，包括云数据库 PostgreSQL、云数据库 MySQL 等，如果不显示指定，则默认该项。
    2：目标实例在腾讯云 CVM 机器上。
    3：目标实例为腾讯云外网自建。
    4：目标实例为云 VPN 接入的实例。
    5：目标实例为自建 VPN 接入的实例。
    6：目标实例为专线接入的实例。
  - **uin**
    非必须项。实例所属的账号 ID，通过该信息鉴定用户权限，可参见 [查询 uin](https://console.cloud.tencent.com/developer)。
  - **own_uin**
    非必须项。实例所属的主账号 ID，同样需要该信息鉴定用户权限。
  - **vpcid**
    非必须项。私有网络 ID，目标实例如果在腾讯云 CVM 的 VPC 网络中，则需要提供该参数，可在 [VPC 控制台](https://console.cloud.tencent.com/vpc/vpc) 中查看。
  - **subnetid**
    非必须项。私有网络子网ID，目标实例如果在腾讯云CVM的VPC网络中，则需要提供该参数，可在 [VPC 控制台](https://console.cloud.tencent.com/vpc/subnet) 的子网中查看。
  - **dcgid**
    非必须项。专线 ID，目标实例如果需要通过专线网络连接，则需要提供该参数值。
  - **vpngwid**
    非必须项。VPN 网关 ID，目标实例如果需要通过 VPN 网络连接，则需要提供该参数值。
  - **region**
    非必须项。目标实例所在地域，如 “ap-guangzhou” 表示广州。如果需要跨地域访问数据，则需要提供该参数值。

  ## 使用 postgres_fdw 示例

  使用 postgres_fdw 插件可以访问本实例其他库或者其他 postgres 实例的数据。

  ### 步骤1：前置条件

  1. 在本实例中创建测试数据。

     ```
     postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
     postgres=>create database testdb1;
     CREATE DATABASE
     ```

     > 注意：
     >
     > 若创建插件报错，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云售后协助处理。

  2. 在目标实例中创建测试数据。

     ```
     postgres=>create role user2 with LOGIN  CREATEDB PASSWORD 'password2';
     postgres=> create database testdb2;
     CREATE DATABASE
     postgres=> \c testdb2 user2
     You are now connected to database "testdb2" as user "user2".
     testdb2=> create table test_table2(id integer);
     CREATE TABLE
     testdb2=> insert into test_table2 values (1);
     INSERT 0 1
     ```

  ### 步骤2：创建 postgres_fdw 插件

  > 说明：
  >
  > 若创建插件时，提示插件不存在或权限不足，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。

  

  ```
  #创建
  postgres=> \c testdb1
  You are now connected to database "testdb1" as user "user1".
  testdb1=> create extension postgres_fdw;
  CREATE EXTENSION
  #查看
  testdb1=> \dx
                              List of installed extensions
        Name     | Version |   Schema   |                    Description
  --------------+---------+------------+----------------------------------------------------
    plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
    postgres_fdw | 1.0     | public     | foreign-data wrapper for remote PostgreSQL servers
  (2 rows)
  ```

  

  ### 步骤3：创建 SERVER

  > 注意：
  >
  > 仅 v10.17_r1.2、v11.12_r1.2、v12.7_r1.2、v13.3_r1.2、v14.2_r1.0 及之后的内核版本支持跨实例访问。

  - 跨实例访问。

    ```
    #从本实例的 testdb1 访问目标实例 testdb2 的数据
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'postgres-xxxxx');
    CREATE SERVER
    ```

    

  - 不跨实例，仅跨 database 访问,仅需要填写 dbname 参数即可。

    ```
    #从本实例的 testdb1 访问本实例 testdb2 的数据
    create server srv_test1 foreign data wrapper postgres_fdw options (dbname 'testdb2');
    ```

    

  - 目标实例在腾讯云 CVM 上，且网络类型为基础网络。

    ```
        testdb1=>create server srv_test foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx', dbname 'testdb2', port '5432', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou'，uin 'xxxxxx'，own_uin 'xxxxxx');
        CREATE SERVER
    ```

    

  - 目标实例在腾讯云 CVM 上，且网络类型为私有网络。

    ```
        testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpcid 'vpc-xxxxxx', subnetid 'subnet-xxxxx');
        CREATE SERVER
    ```

    

  - 目标实例在腾讯云外网自建。

    ```
        testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '3', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx');
        CREATE SERVER 
    ```

    

  - 目标实例在腾讯云 VPN 接入的实例。

    ```
        testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '4', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');
    ```

    

  - 目标实例在自建 VPN 接入的实例。

    ```
        testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '5', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');   
    ```

    

  - 目标实例在腾讯云专线接入的实例。

    ```
        testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '6', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', dcgid 'xxxxxx');    
        CREATE SERVER       
    ```

    

  ### 步骤4：创建用户映射

  > 说明：
  >
  > 同实例的跨 database 访问则可跳过此步骤。

  

  ```
  testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
  CREATE USER MAPPING
  ```

  

  ### 步骤5：创建外部表

  

  ```
  testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(table_name 'test_table2');
  CREATE FOREIGN TABLE
  ```

  

  ### 步骤6：访问外部数据

  

  ```
  testdb1=> select * from foreign_table1;
    id
  ----
     1
  (1 row)
  ```

  

  ## postgres_fdw 使用注意

  目标实例，需要注意以下几点：

  1. 需要放开 PostgreSQL 的 hba 限制，允许创建的映射用户（如：user2）以 MD5 方式访问。hba 的修改可参考 [PostgreSQL 官方说明](https://www.postgresql.org/docs/10/static/auth-pg-hba-conf.html)。
  2. 如果目标实例非 TencentDB 实例，且搭建有热备模式，当主备切换后，需要自行更新 server 连接地址或者重新创建 server。

- https://segmentfault.com/a/1190000041034644

```
create extension postgres_fdw;

CREATE SERVER myserver FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host 'foo', dbname 'foodb', port '5432');

自建PostgreSQL实例可以通过oracle_fdw或mysql_fdw连接VPC外部的Oracle实例或MySQL实例。
连接自身跨库操作时，host请填写127.0.0.1，port请填写show port命令返回的本地端口。
需要将RDS PostgreSQL的专有网络网段（例如172.xx.xx.xx/16）添加到目标数据库的白名单中，允许RDS PostgreSQL访问。

```





```
# dblink() -- executes a query in a remote database
SELECT * 
FROM   table1 tb1 
LEFT   JOIN (
   SELECT *
   FROM   dblink('dbname=db2','SELECT id, code FROM table2')
   AS     tb2(id int, code text);
) AS tb2 ON tb2.column = tb1.column;

Don't forget to create extension CREATE EXTENSION IF NOT EXISTS dblink; 
```



## BIGSERIAL PRIMARY KEY

```
id BIGSERIAL PRIMARY KEY, 

    CREATE TABLE $$(tablename) (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        zh text DEFAULT '', 
        en text DEFAULT '', 
        type text, 
        begintime text,
        endtime text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector, 
        v_zh  tsvector, 
        v_en  tsvector, 
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode text DEFAULT '',
        audio bytea, 
        video bytea,
        videoname text 
      );

```



## UUID

```
从PostgreSQL v13开始，您可以使用核心函数uuid_generate_v4()
生成版本4（随机）uuid。
```



### 插入后返回 ID

```
INSERT INTO users (firstname, lastname) VALUES ('Joe', 'Cool') RETURNING id;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE key_values (
    key uuid DEFAULT uuid_generate_v4(),
    value jsonb
);
CREATE INDEX idx_key_values ON key_values USING hash (key);
postgres=# do $$
begin
for r in 1..1000 loop
INSERT INTO key_values (value)
VALUES ('{"somelarge_json": "bla"}');
end loop;
end;
$$;
```



## 重设自增ID



```
ALTER TABLE <table name> 
    ALTER COLUMN <column name> 
        RESTART WITH <new value to restart with>;
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



```

curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash - && \
sudo yum install nodejs && \
npm install -g pm2



```





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
yum install centos-release-scl-rh && \
yum install llvm-toolset-7-clang && \
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



```
$ sudo -H yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-$(cut -d: -f5 /etc/system-release-cpe | cut -d. -f1)-$(rpm -qf --queryformat="%{ARCH}" /etc/redhat-release)/pgdg-redhat-repo-latest.noarch.rpm
$ sudo -H yum install -y https://packages.groonga.org/centos/groonga-release-latest.noarch.rpm
$ sudo -H yum install -y postgresql13-pgdg-pgroonga
```



```
 sudo -H yum install -y groonga-tokenizer-mecab
```



```
sudo -u postgres -H psql --command 'CREATE DATABASE pgroonga_test'

sudo -u postgres -H psql -d pgroonga_test --command 'CREATE EXTENSION pgroonga'


```





## Install ffmpeg



```
# ffmpeg on centos7
sudo yum install epel-release && \
sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm && \
sudo yum install ffmpeg ffmpeg-devel
```



##  Install RUM



```
yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
yum -y update && \
yum search postgresql13 && \
yum -y install postgresql13 postgresql13-server && \
/usr/pgsql-13/bin/postgresql-13-setup initdb
	# 更多内容文档后面：Docker 中的postgreql

yum groupinstall "Development Tools" && \
yum install centos-release-scl-rh && \
yum install llvm-toolset-7-clang && \
yum install postgresql13-devel && \
yum install postgresql13-contrib && \
yum install systemtap-sdt-devel

git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-13/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install

make USE_PGXS=1 installcheck && \
$ psql DB -c "CREATE EXTENSION rum;"
```



```
CREATE INDEX index_rum_jp ON anime USING rum (v_jp rum_tsvector_ops);
```





## 事务



PostgreSQL 事务 [u](https://www.jianshu.com/p/f35d01b95a38)

> 默认情况下 PostgreSQL会将每一个SQL语句都作为一个事务来执行。如果我们没有发出BEGIN命令，则每个独立的语句都会被加上一个隐式的BEGIN以及（如果成功）COMMIT来包围它。一组被BEGIN和COMMIT包围的语句也被称为一个事务块。
>
> ```sql
>BEGIN;
> UPDATE accounts SET balance = balance - 100.00
>  WHERE name = 'Alice';
> COMMIT;
>    ```



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



## 随机查询 && 安装插件

- https://github.com/digoal/blog/blob/master/202105/20210527_01.md  

  - PostgreSQL 随机查询采样 - 既要真随机、又要高性能

  - https://github.com/digoal/blog/blob/master/202005/20200509_01.md 

  -  PostgreSQL 随机采样应用 - table sample, tsm_system_rows, tsm_system_time

    > select name from pg_available_extensions;  # 查询可用扩展
    >
    > yum install postgresql13-contrib
    >
    > create extension IF NOT EXISTS tsm_system_rows;
    >
    > create extension IF NOT EXISTS tsm_system_time;
    >
    > ```
    > 最多采样10毫秒, 返回符合play_count>=2000的10条. (如果很快就有10条符合条件, 那么不会继续扫描, 所以很快很快)
    > 
    > explain (analyze,verbose,timing,costs,buffers) select id,play_count from video as v1 TABLESAMPLE system_time(10)  where play_count>=2000 limit 10;  
    > 
    > 
    > 最多采样100条, 返回符合play_count>=2000的10条. (如果很快就有10条符合条件, 那么不会继续扫描, 所以很快很快)
    > 
    > explain (analyze,verbose,timing,costs,buffers) select id,play_count from video as v1 TABLESAMPLE  system_rows (100) where play_count>=2000 limit 10;
    > 
    > SELECT id, jp_ruby as jp, zh, p.begintime as time, type, name, seasion FROM anime p  TABLESAMPLE  system_rows (10000) WHERE p.v_jp @@ to_tsquery('ここ')  ORDER BY RANDOM()  LIMIT 3;
    > 
    > 在时间可控,代价可控的情况下(防止采样雪崩),保证采样随机性.
    > 如果where条件的记录占比很少很少, 可能达到采样上限后无法返回limit的条数. 这种情况下, 可以选择几种方法:
    > 1、调大采样上限, 注意防止雪崩
    > 2、修改where条件, 使得覆盖率变大.
    > 3、垃圾回收, 使得每个block的空洞变少.
    > 4、分区, 提高目标采样表中 where 条件符合条件记录的占比.                             
    > ```





## FTS



PostgreSQL 全文检索加速 快到没有朋友 - RUM索引接口(潘多拉魔盒) [u](https://github.com/digoal/blog/blob/master/201610/20161019_01.md)



RUM索引

- 安装 https://github.com/postgrespro/rum

  > ```
  > yum install -y systemtap-sdt-devel
  > ```

短语搜索



> create extension rum;
>
> CREATE INDEX fts_rum_anime ON anime USING rum (v_jp rum_tsvector_ops);
>
> CREATE INDEX fts_rum_studio ON studio USING rum (v_zh rum_tsvector_ops);





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



### json



```
CREATE TABLE bookdata (
  id  serial NOT NULL PRIMARY KEY,
  info json NOT NULL
)

CREATE INDEX bookdata_fts ON bookdata USING gin((to_tsvector('english',info->'title')));

INSERT INTO bookdata (info)
VALUES
 ( '{ "title": "The Tattooed Duke", "items": {"product": "Diaper","qty": 24}}'),
 ( '{ "title": "She Tempts the Duke", "items": {"product": "Toy Car","qty": 1}}'),
 ( '{ "title": "The Duke Is Mine", "items": {"product": "Toy Train","qty": 2}}'),
 ( '{ "title": "What I Did For a Duke", "items": {"product": "Toy Train","qty": 2}}'),
 ('{ "title": "King Kong", "items": {"product": "Toy Train","qty": 2}}');

SELECT info -> 'title' as title FROM bookdata
WHERE to_tsvector('english',info->'title') @@ to_tsquery('Duke');
```





```
https://stackoverflow.com/questions/45680936/how-to-implement-full-text-search-on-complex-nested-jsonb-in-postgresql
```



### 查询优化

- https://v2ex.com/t/840205#reply37
  - PostgreSQL 真的没有完美的分页方法吗？

- https://kaifeiji.cc/post/do-i-really-know-about-pagination/
  - 我真的会分页吗

- https://github.com/digoal/blog/blob/master/201801/20180119_03.md



#### 分页

不过借鉴这个思路，我们可以对某些场景的分页查询进行优化。
对于按需自动加载（*划到页面底部自动加载更多内容*）或者只提供**上一页/下一页**浏览模式的场景，可以进行如下优化：

1. 每次查询数据时，我们记录最后一条数据的ID或最后更新时间（这个主要根据order by字段来确定）
2. 加载下一页数据时，把本页的最后一条数据ID作为过滤条件。
3. 加载上一页数据时，则把本页第一条数据ID作为过滤条件。

**查询下一页**

```n1ql
SELECT * FROM orders WHERE order_id > page_last_id ORDER BY order_id
LIMIT page_sieze OFFSET 0;
```

**查询上一页**

```n1ql
SELECT * FROM orders WHERE order_id < page_first_id ORDER BY order_id
LIMIT page_sieze OFFSET 0;
```

小技巧：*每次查询数据时，多返回一条数据，即返回page_size + 1条数据，但显示时去掉最后一条数据，通过这多出来一条数据，我们可以用来判断数据是否还有下一页*。

另外对于可以跳转到任意页面的场景，也可以进行优化，这种可跳转场景，分页显示也是有限的，一般模式是**第一页/上一页/当前页前后10页……/下一页/最后一页**，也就是说，分页时，数据是在**一定范围内**（前后10页）移动，可以以当前页数据为基础，对数据进行过滤，减少数据扫描范围。
考虑orders表有10W条记录，每页显示10条，当前页码为1000时的场景，如果按照单独limit和offset模式，offset=1W，也就是数据库要扫码1W条记录。假如现在翻页要从1000页跳转到1005页，我们以第1000页最后一条数据ID为过滤条件，offset跳过1001-1004的40条数据即可。

**查询1005页**

```n1ql
SELECT * FROM orders WHERE order_id > page_1000_last_id ORDER BY order_id
LIMIT page_sieze OFFSET page_size * 4;
```

这种方法相比基础的分页方式，只要order by字段是主键或索引字段，数据扫描的行数从1W多条下降到了几十条，效率大大提升。



### 读写分离

- https://lofter.me/2017/10/25/PostgreSQL%E9%9B%86%E7%BE%A4%E5%8F%8A%E8%AF%BB%E5%86%99%E5%88%86%E7%A6%BB%E6%96%B9%E6%A1%88/

```
PostgreSQL集群及读写分离方案
```



# 图式搜索

- https://developer.aliyun.com/article/689151

  > 德哥PG系列：PostgreSQL 图式关系数据应用实践

- https://www.bilibili.com/video/BV1ff4y1b73U

  > 重新发现PostgreSQL之美 - 19 困扰古惑仔和海盗的数学难题 森林图式分佣

- https://developer.aliyun.com/article/328141

- https://www.bilibili.com/video/BV1Vv4115723

  > FTS 距离

- https://developer.aliyun.com/article/72699

  > PostgreSQL 递归查询 - 树型数据按路径分组输出

- https://www.cnblogs.com/ricklz/p/12590618.html

  > 通过使用RECURSIVE，一个**WITH查询可以引用它自己的输出**。
  >
  > - https://blog.csdn.net/u010251897/article/details/118515107

```
图式搜索是PostgreSQL在（包括流计算、全文检索、图式搜索、K-V存储、图像搜索、指纹搜索、空间数据、时序数据、推荐等）诸多特性中的一个。

采用CTE语法，可以很方便的实现图式搜索（N度搜索、最短路径、点、边属性等）。

其中图式搜索中的：层级深度，是否循环，路径，都是可表述的。
```





## Docker

```
service docker status
service docker start
systemctl enable docker  # 开机自启动
docker update --restart always xxxx  # 容器随docker 启动
```



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

yum whatprovides ifconfig
yum install net-tools

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



### 保存配置好的镜像



```
docker commit   --message "host 222 --> docker 22"  4ace0a92d191
```





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



<img src="postgresql summary.assets/image-20210526154947175.png" alt="image-20210526154947175" style="zoom:50%;" />



```
# 关闭防火墙
systemctl stop firewalld

# pm2 resurrect  # pm2 save 后恢复

# atuto run when reboot
chmod +x /etc/rc.d/rc.local
vi /etc/rc.d/rc.local
mount /dev/sda1 /mnt  # 加一句，挂载存储块

systemctl status postgresql-13
systemctl enable postgresql-13 # 自启动



# 特权模式创建容器
docker run -tid --name centos7PG10 -p 54322:5432 --privileged=true centos:7 /sbin/init 
		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口

# 运行docker 的shell
docker exec -it centos7PG10 /bin/bash

# 安装PG13
# https://gist.github.com/coder4web/13419dbfe7c22dc5bad8bb4e135138bc # 安装脚本
yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

yum -y update
yum search postgresql13
yum -y install postgresql13 postgresql13-server
/usr/pgsql-13/bin/postgresql-13-setup initdb
	# adduser postgres
	# chown -R postgres:postgres /mnt/psqldata
	务必看这里 \doc\tech\survive.md
		后来的方案，让linux 适应windows 的分区
		
		# https://unix.stackexchange.com/questions/491098/cannot-chown-chmod-on-mounted-ntfs-partition
			# linux mount ntfs chown 搜这个，改不了owner 属性
		# cp -R /var/lib/pgsql/13/data /mnt/psqldata # 只能透亮换柱了
		# mv /var/lib/pgsql/13/data /var/lib/pgsql/13/data__link__to_mnt_psqldata
		# ln -s  /mnt/psqldata  /var/lib/pgsql/13/data
			# unlink 取消软链用这个
		# chown -R postgres:postgres /mnt/psqldata
	# sudo -u postgres /usr/pgsql-13/bin/initdb -D /mnt/psqldata
	# su - postgres
	# /usr/pgsql-13/bin/initdb -D /mnt/psqldata
	# /usr/pgsql-13/bin/pg_ctl -D /mnt/psqldata -l logfile -o '--config-file=/mnt/psqldata/postgresql.conf' start
	# /usr/pgsql-13/bin/pg_ctl -D /mnt/psqldata -l logfile status # 查看状态
	# vi /mnt/psqldata/postgresql.conf
		listen_addresses = '*' # 改成这个
	# vi /mnt/psqldata/pg_hba.conf
		hostnossl    all          all            0.0.0.0/0  md5
		# 加在最后面，接受所有远程IP
	# psql -c "show config_file"
	# ps aux | grep /postgres
	# select name, setting from pg_Settings where name ='data_directory';
	
systemctl start postgresql-13
	# /usr/pgsql-13/bin/postmaster -D /var/lib/pgsql/13/data/
	# sudo -u postgres psql
	# SHOW data_directory;
	
systemctl status postgresql-13
systemctl enable postgresql-13 # 自启动

# 改强密码
su - postgres
	psql
	\password postgres
	然后输入密码
	\q
			这句不成功# psql -c "alter user postgres with password '这里填的一个强密码'"
		
# 允许运程连接
vi /var/lib/pgsql/13/data/postgresql.conf
	listen_addresses = '*' # 改成这个
vi /var/lib/pgsql/13/data/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  md5  
	# hostnossl    all          all            0.0.0.0/0  trust  # 任何密码都能连
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



#### WIN7+centos 双启问题 

```

务必看这里
\doc\tech\survive.md
	后来的方案，让linux 适应windows 的分区


```



#### 启动已停止的容器

docker start 2416f0b833b2





### ssh 保持连接



```
vi /etc/ssh/sshd_config

TCPKeepAlive yes #表示TCP保持连接不断开
ClientAliveInterval 300 #指定服务端向客户端请求消息的时间间隔，单位是秒，默认是0，不发送。设置个300表示5分钟发送一次（注意，这里是服务端主动发起），然后等待客户端响应，成功，则保持连接。
ClientAliveCountMax 3 #指服务端发出请求后客户端无响应则自动断开的最大次数。使用默认给的3即可。
（注意：TCPKeepAlive必须打开，否则直接影响后面的设置。ClientAliveInterval设置的值要小于各层防火墙的最小值，不然，也就没用了。）
```





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



# AgensGraph 图数据库

- https://blog.csdn.net/qq_21090437/article/details/120292081



# JSON

```
    select t.id, array_agg(t._name) as _board
    from (
        select 
            d.id,
            jsonb_extract_path_text(jsonb_array_elements(
                case jsonb_extract_path(d.data, 'board_members') 
                    when 'null' then '[{}]'::jsonb 
                    else jsonb_extract_path(d.data, 'board_members') 
                end
            ), 'first_name') || ' ' || jsonb_extract_path_text(jsonb_array_elements(
                case jsonb_extract_path(d.data, 'board_members') 
                    when 'null' then '[{}]'::jsonb 
                    else jsonb_extract_path(d.data, 'board_members') 
                end
            ), 'last_name') as _name
        from my_table d
        group by d.id
    ) t
    group by t.id
    

1


You can use jsonb_path_query_array to get all matching array elements:

jsonb_path_query_array(data, '$.board_members[*] ? (@.ind == true)')
The above returns

[
  {"ind": true, "last_name": "Grant", "first_name": "Hugo"}, 
  {"ind": true, "last_name": "Flair", "first_name": "Rick"}
]
for your sample data.

To get the concatenated first/lastname you need to unnest the array and aggregate the names back.

select id, 
       (select jsonb_agg(concat_ws(' ', p.item ->> 'first_name', p.item ->> 'last_name'))
        from jsonb_array_elements(jsonb_path_query_array(data, '$.board_members[*] ? (@.ind == true)')) as p(item)) as names
from my_table
The above returns ["Hugo Grant", "Rick Flair"] in the names column

```

## 带有唯一key 的JSON

```
Another option is to use JSON or JSONB with a unique hash index on the key.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE key_values (
    key uuid DEFAULT uuid_generate_v4(),
    value jsonb
);
CREATE INDEX idx_key_values ON key_values USING hash (key);
postgres=# do $$
begin
for r in 1..1000 loop
INSERT INTO key_values (value)
VALUES ('{"somelarge_json": "bla"}');
end loop;
end;
$$;
DO

Some queries

SELECT * FROM key_values WHERE key = '1cfc4dbf-a1b9-46b3-8c15-a03f51dde891';
Time: 0.514 ms
postgres=# SELECT * FROM key_values WHERE key = '1cfc4dbf-a1b9-46b3-8c15-a03f51dde890';
Time: 1.747 ms


Time: 58.327 ms
```



## 插入后返回 ID

```
INSERT INTO users (firstname, lastname) VALUES ('Joe', 'Cool') RETURNING id;
```





# KV存储

- https://blog.csdn.net/neweastsun/article/details/92849375

  > ```
  > CREATE EXTENSION hstore;
  > 	# 启用内置扩展，
  > 	
  > CREATE TABLE books (
  >    id serial primary key,
  >    title VARCHAR (255),
  >    attr hstore
  > );
  > 
  > INSERT INTO books (title, attr)
  > VALUES
  >    (
  >       'PostgreSQL Tutorial',
  >       '"paperback" => "243",
  >       "publisher" => "postgresqltutorial.com",
  >       "language"  => "English",
  >       "ISBN-13"   => "978-1449370000",
  >        "weight"   => "11.2 ounces"'
  >    );
  > ```



# 分布式集群

- https://www.xmmup.com/pggaokeyongzhicitusfenbushijiqundajianjishiyong.html  **小麦苗DBA宝典**

- https://github.com/citusdata/citus



# pool



```
# 最大连接配置

RAM 16GB

Our configs:

/etc/sysctl.conf
kernel.shmmax=100663296

/var/lib/pgsql/13/data/postgresql.conf
max_connection=100
shared_buffer=512
```

```
# https://www.enterprisedb.com/blog/postgresql-pgpool-connection-pool-database-load

# https://stackoverflow.blog/2020/10/14/improve-database-performance-with-connection-pooling/

	pgpool-II

# https://www.cnblogs.com/wy123/p/14087274.html
	在Postgre中设置max_connections时，为什么需要使用连接池 （译）

```







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



```
regexp_split_to_array('hello world', E'\\s+')
  --> {hello,world}
```



```
with my_table(resource_name, readiops, writeiops) as (
values
('90832-00:29:3E', 3.21, 4.00),
('90833-00:30:3E', 2.12, 3.45),
('90834-00:31:3E', 2.33, 2.78),
('90832-00:29:3E', 4.21, 6.00)
)

select 
    split_part(resource_name::text, '-', 1) as array_serial,
    split_part(resource_name::text, '-', 2) as ldev,
    string_agg(readiops::text, ',') as readiops,
    string_agg(writeiops::text, ',') as writeiops
from my_table
group by 1, 2;

 array_serial |   ldev   | readiops  | writeiops 
--------------+----------+-----------+-----------
 90832        | 00:29:3E | 3.21,4.21 | 4.00,6.00
 90833        | 00:30:3E | 2.12      | 3.45
 90834        | 00:31:3E | 2.33      | 2.78
(3 rows)
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





```
CREATE OR REPLACE FUNCTION "public"."ja_reading"(text)
  RETURNS "pg_catalog"."text" AS $BODY$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
  LOOP
    
		FOREACH s IN ARRAY string_to_array($1, '|')
		LOOP
		
			RETURN s; 
		
		END LOOP;

		
		reading = (js -> 'metadata' ->> 'reading');

		-- total = total || (js ->> 'value');
		-- RETURN total || (js ->> 'value');
		
		-- RETURN total || (js ->> 'value');
		
		
		/*
    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
		*/
  END LOOP;

  RETURN array_to_string(total, '');
END;
$BODY$
  LANGUAGE plpgsql IMMUTABLE
  COST 100
```







# JPQ



```mysql

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
```





# push stream



```
# atuto run when reboot
chmod +x /etc/rc.d/rc.local
vi /etc/rc.d/rc.local
mount /dev/sda1 /mnt  # 加一句，挂载存储块
```





How to configure data directory in PostgreSQL 13

https://dsquarehelp.com/postgresql-13-data-directory/



利用Nginx WebDAV搭建自己的网盘

https://www.cnblogs.com/DragonStart/p/13410090.html



详细命令

https://www.huaweicloud.com/articles/4a48bc251c6378d717caaf1f27acf1c4.html



NVIDIA FFmpeg 转码指南

https://developer.nvidia.com/zh-cn/blog/nvidia-ffmpeg-transcoding-guide/



```
# ffmpeg on centos7
sudo yum install epel-release
sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum install ffmpeg ffmpeg-devel
```



```
# m3u8
https://yocoha.com/article/31
https://www.jianshu.com/p/e97f6555a070
https://zhuanlan.zhihu.com/p/147019759

```



```
# hls.js
https://zhuanlan.zhihu.com/p/158525554
https://segmentfault.com/a/1190000018503818 # 干货
https://blog.csdn.net/weixin_43029824/article/details/103391494 # 更干货
```



```
# success
# hevc 表示使用h.265 编码
ffmpeg -y -ss 00:01:12.960 -to 00:01:14.640  -i t.mkv  -codec:v hevc -acodec mp3 -ar 44100 -ac 2 -b:a 192k t.ts
```



```
# http://ffmpeg.org/ffmpeg-filters.html#subtitles

! ffmpeg -i t.mkv -y -ss 00:01:12.960 -to 00:01:14.640 -codec:v hevc -acodec mp3 -ar 44100 -ac 2 -b:a 192k -c:s mov_text t.ts # 软字慕


! ffmpeg -i t.mkv -y -ss 00:01:12.960 -to 00:01:14.640 -codec:v hevc_nvenc -acodec aac -ar 44100 -ac 2 -b:a 192k -vf subtitles=t.mkv t.ts # 硬字幕


# jsmpeg.js 正常播放
! ffmpeg -i t.mkv -y -ss 00:01:12.960 -to 00:01:14.640 -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=t.mkv t.ts

# GPU加速
! ffmpeg -c:v mpeg1_cuvid -i t.mkv -y -ss 00:01:12.960 -to 00:01:14.640 -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=t.mkv t.ts
	# https://gist.github.com/garoto/54b46513fa893f48875a89bee0056d63
	! ffmpeg -decoders | grep cuvid

# showNV.sh
#/bin/bash
for i in encoders decoders filters; do
    echo $i:; ffmpeg -hide_banner -${i} | egrep -i "npp|cuvid|nvenc|cuda"
done
! chmod +x ./showNV.sh
! ./showNV.sh


# 960x540 

行 ffmpeg -i Tor_Animation_en.mp4 -i Tor_animation.zh-CN.srt Tor_Animation_subtitled.mkv 的时候，就会看到这样的输出：

Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> h264 (libx264))
  Stream #0:1 -> #0:1 (aac (native) -> vorbis (libvorbis))
  Stream #1:0 -> #0:2 (subrip (srt) -> ass (native))
它很直观地告诉我，在本次操作中， 0 号输入文件（也就是 Tor_Animation_en.mp4 ）中的 0 号媒体流变成了 0 号输出文件的 0 号媒体流， 0 号输入文件中的 1 号媒体流变成了 0 号输出文件的 1 号媒体流， 1 号输入文件（也就是 Tor_animation.zh-CN.srt ）的 0 号媒体流变成了 0 号输出文件的 2 号媒体流。编码的转换也被清晰地显示了出来。


因为字幕流也是媒体流，也有各种编码，所以，我们也可以通过 -scodec 或 -c:s 选项来指定字幕流的编码。这个例子可以让 FFmpeg 复制视频流和音频流（不用重新编码，加快了速度），而将字幕流转换为 ass 编码：

ffmpeg -i Tor_Animation_en.mp4 -i Tor_animation.zh-CN.srt -c:v copy -c:a copy -c:s ass Tor_Animation_subtitled.mkv
同样的， -c 选项除了会影响到视频流和音频流以外，也会影响到字幕流，也就是说，指定 -c copy 也会让 FFmpeg 不对字幕流进行重新编码。

你甚至可以将字幕文件作为单独的输入文件！也就是对字幕文件进行转码，比如 ffmpeg -i Tor_animation.zh-CN.srt Tor_animation.zh-CN.ass 就会将 SubRip 字幕转换为 ASS 字幕。（因为 ASS 封装格式的默认字幕编码就是 ass ，所以你在这条命令中不用写 -c:s ass ）



基于图像的字幕格式输入  使用覆盖滤镜。此示例将第四字幕流覆盖在第二视频流上，并复制第七音频流：
ffmpeg -i input.mkv -filter_complex "[0:v:2][0:s:3]overlay[v]" -map "[v]" -map 0:a:6 -c:a copy output.mp4

10.7 内嵌字幕
在播放器不支持独立字幕流的场合，需要将字幕混入视频流中（因此需要重编码）。

ffmpeg -i input.mp4 -vf subtitles=input.srt output.mp4
如果字幕以字幕流的形式位于一个视频文件中，可以直接调用：
ffmpeg -i input.mkv -vf subtitles=input.mkv output.mp4

处理方案
软字幕
MP4 格式支持流文字格式字幕，播放时可在播放器中选择对应的字幕，但该软字幕功能可能在有些播放器或者设备上不支持。

1
ffmpeg -i input.mkv -map 0:v:0 -map 0:a:1 -map 0:s:34 -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=chs output.mp4
相关参数:

-map 选项可将你想选择的原mkv文件中的视频流 (v) /音频流 (a) / 字幕流 (s) 复制到输出中；: 后的数字代表原mkv文件中的第几个流（mkv 里有多个音频流/字幕流）。
本例中选择了第0个视频流（默认），第1个音频流，第34个字幕流（简体中文）。
-c 选项则代编解码器名称，: 后的 v/a/s 意义同上；
在本例中视频和音频的编解码器直接复制的原视频音频流的编码器，所以编码器设置的为 copy 。
而 mov_text 则为此类软字幕编码器
-metadata 选项可设置视频的元数据信息，之后的 :s:s:0 为可选项，空格之后接一个要设置元信息的键值对。
本例中的 :s:0 表示对输出文件第0个字幕流进行元信息的设置，将字幕标识为简体中文。
如果要设置第0个视频流的元信息，则在 -metadata 之后加 :s:a:0
外挂字幕
尴尬的是 iOS 版的暴风影音不支持 mov_text 编码的软字幕，那就只能尝试能不能用外挂字幕了。

直接通过 -map 选项将简体中文字幕流导出到 output.srt 文件

1
ffmpeg -i input.mkv -map 0:s:34 output.srt
在暴风影音中选择这个 output.srt 文件，显示出来却是乱码，然而在电脑上的播放器上却一切正常，这暴风影音真的是不行啊。

硬字幕
字幕文件嵌入视频
将刚才导出的 srt 文件”烧入”到先前生成的那个 output.mp4 文件中，因为此处要对有字幕的视频帧进行压制，所以会比较慢。

1
ffmpeg -i output.mp4 -vf subtitles=output.srt output-Subtitles.mp4
-vf 选项代表使用视频过滤器 (Video Filters)

subtitles 就代表设置字幕为 = 之后接的字幕文件 / 流
如果需要嵌入的是 ass 格式的字幕，只需要将 subtitles 替换为 ass ，然后 = 之后接上 ass 字幕文件即可，例如 ffmpeg -i output.mp4 -vf ass=subtitle.ass output-Subtitles.mp4
这次生成的 mp4 文件终于能在暴风影音里播放了，真是够折腾的……

视频字幕流嵌入视频
但我不想生成中间的 srt 字幕文件，我们可以直接将 mkv 的字幕流在转成 mp4 的时候直接压制进视频文件中

1
ffmpeg -i input.mkv -filter_complex "[0:v:0]subtitles=input.mkv:si=34[v]" -map "[v]" -map 0:a:0 -c:a copy output.mp4
此处使用复杂图像过滤器 (Complex filtergraphs) 选项 -filter_complex 来处理视频，将第0个视频流加上 input.mkv 中的第34个字幕流一起压制到视频流 v 中，同时通过 -map 选项将第0个音频流直接导出到 output.mp4 中。

自此，又能完美的在 iOS 端的暴风影音上愉快地追剧了 d(`･∀･)b

```



```
# CUDA 加速
ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i input.mp4 -c:a copy -c:v h264_nvenc -b:v 5M output.mp4


将一张图片循环20000次生成视频，一个是硬编码一个是软编码，比较它们运行时间。
# time ./ffmpeg -f image2 -stream_loop 20000 -i 1.jpg -vcodec h264_nvenc -b:v 200k -r 10 -s 1920x1080 -y 2.mp4 
# time ./ffmpeg -f image2 -stream_loop 20000 -i 1.jpg -vcodec libx264 -b:v 200k -r 10 -s 1920x1080 -y 2.mp4 


  Duration: 00:23:30.01, start: 0.000000, bitrate: 1841 kb/s
    Stream #0:0: Video: h264 (High), yuv420p(tv, bt709, progressive), 1280x720 [SAR 1:1 DAR 16:9], 23.98 fps, 23.98 tbr, 1k tbn, 47.95 tbc (default)
    Stream #0:1(jpn): Audio: aac (LC), 48000 Hz, stereo, fltp (default)
    Stream #0:2(chi): Subtitle: ass (default)
```

```
# using libfaac on Mac OS X 10.6.8
# -vn : not copying video
# -acodec : specify codec used in flv file
# -ac : channels. 1 is for mono, 2 is for stereo
# -ab : specify bitrate for output file (note that rate is not kbps but bps)
# -ar : sampling frequency (Hz)
# -threads: number of threads for encoding
# "-strict experimental" is necessary to use libfaac

ffmpeg -y -i xxxxxxxxxxx.flv -vn -acodec aac -ac 2 -ab 128000 -ar 44100 -threads 4 -strict experimental xxxxx.m4a

# note that codec is 'libmp3lame'
ffmpeg -i xxxxxxxxxx.m4a -vn -acodec libmp3lame -ac 2 -ab 128 -ar 44100 -threads 4 -f mp3 zzzzzzzzzzz.mp3

# or you can directly convert audio track
ffmpeg -i xxxxxxxxxxx.flv -vn -acodec libmp3lame -ac 2 -ab 128000 -ar 44100 -threads 4 -f mp3  xxxxx.mp3

# for wav -acodec option is not necessary
ffmpeg -i xxxxxxxxxx.flv -vn -threads 4 -ac 1 -ar 44100 xxxxxx.wav

# for ogg
ffmpeg -i xxxxxxxxxx.flv -vn -threads 4 -acodec libvorbis -ac 2 -ar 44100 xxxxxxx.ogg

# simply extract audio without transcoding it.
ffmpeg -i xxxxxxxxxx -vn -threads 4 -acodec copy output.filename

# chop mp4 with/without transcoding
ffmpeg -ss <start.second> -i xxxxxx -t <duration.second> output.filename
ffmpeg -ss <start.second> -i xxxxxx -t <duration.second> -acodec copy -vcodec copy output.filename
```









![image-20210428171601026](postgresql summary.assets/image-20210428171601026.png)



```
ffmpeg -ss <start_time> -i video.mp4 -t <duration> -q:v 2 -vf select="eq(pict_type\,PICT_TYPE_I)" -vsync 0 frame%03d.jpg

ffmpeg -y -ss 00:01:12.960 -to 00:01:14.640 -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -r 1 -q:v 2 -f image2 -frames:v 1 snapshot.jpg




ffmpeg -y -ss 00:01:12.960 -to 00:01:14.640 -i "/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" "frames/out-%03d.jpg"


# 成功
# https://www.cnblogs.com/jisongxie/p/9948845.html
ffmpeg -y -ss 00:01:12.960 -t 10 -i "/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -r 1 -q:v 2 -f image2 "frames/out-%03d.jpg"


```





```
ffmpeg -y -ss 00:01:12.960 -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -skip_frame nokey -frames:v 1 -q:v 2 output.jpg

For JPEG output use -q:v to control output quality. Full range is a linear scale of 1-31 where a lower value results in a higher quality. 2-5 is a good range to try.

# 出错解决
https://www.reddit.com/r/ffmpeg/comments/lcttpl/deprecated_pixel_format_used_make_sure_you_did/ 

ffmpeg -i test.avi -y -f image2 -ss 00:00:00 -vframes 1 test.jpg
```





```
ffmpeg -i "[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -vn -ss 00:01:12.960 -to 00:01:14.640 -acodec mp3 -ar 44100 -ac 2 -b:a 192k ttttt.ts
```



```
psycopg2 returns the binary data (probably stored in a bytea column in your table) in a buffer object in Python 2, or in a memoryview in Python 3.

Both buffer and memoryview objects can be passed directly to a base64 string encoder, so this will encode the binary data in base 64:

import base64

rows = cur.fetchall()
binary_img = rows[0][0]
base64_img = base64.b64encode(binary_img)
In Python 2, if you want the binary data itself you can use str() or slice with [:] the buffer object. In Python 3 you can use the tobytes() method of the memoryview object.
```





```
# The adapter: converts from python to postgres
# note: this only works on numpy version whose arrays 
# support the buffer protocol,
# e.g. it works on 1.5.1 but not on 1.0.4 on my tests.

In [12]: def adapt_array(a):
  ....:     return psycopg2.Binary(a)
  ....:

In [13]: psycopg2.extensions.register_adapter(np.ndarray, adapt_array)


# The typecaster: from postgres to python

In [21]: def typecast_array(data, cur):
  ....:     if data is None: return None
  ....:     buf = psycopg2.BINARY(data, cur)
  ....:     return np.frombuffer(buf)
  ....:

In [24]: ARRAY = psycopg2.extensions.new_type(psycopg2.BINARY.values,
'ARRAY', typecast_array)

In [25]: psycopg2.extensions.register_type(ARRAY)


# Now it works "as expected"

In [26]: cur = cnn.cursor()

In [27]: cur.execute("select %s", (a,))

In [28]: cur.fetchone()[0]
Out[28]: array([ 1.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.])
```





```
https://my.oschina.net/u/4394125/blog/3310836

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>
    </script>
</head>
<body>
	<audio controls="controls" autoplay="autoplay">
	<source src="http://127.0.0.1:12345/cgmedia/28181/getaudio?id=34020000001310000001@192.168.1.108:5060&format=mp3&transporttype=udp&transportport=22000" type="audio/mpeg">
	</audio>
</body>
</html>


@app.route('/audio')
def stream_mp3():
    def generate():
        path = 't.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")

# 在audio标记中，如果不包含controls属性，则audio播放器将不会呈现在页面上。
# <img src="{{ url_for('static', filename='foo.jpg') }}">
# 在 Python 脚本里，url_for() 函数需要从 flask 包中导入，而在模板中则可以直接使用，因为 Flask 把一些常用的函数和对象添加到了模板上下文（环境）里。
# url_for('.static',_external=True,filename='pic/test.png') # 完整url
# https://zhuanlan.zhihu.com/p/67747626 让 Flask 模板引擎 Jinja2 和 JavaScript 模板引擎和平共存
{% raw %}
<div id="app">
    {{ js_var }}
</div>
{% endraw %}

{{ url_for('test',name=1) }} 相当于我们传递的XXX/?name=1 
@app.route('/test/<name>', methods=['GET'])
def test(name):

URL中传参
可以使用Flask request方法：request.args.get()，例如，前台请求URL为 http://localhost:5000/tk?p=1&type=1
@app.route('/tk', methods=['post','get'])
def tk():
    p = request.args.get('p')
    type = request.args.get('type')

https://www.zhangxinxu.com/wordpress/2019/07/html-audio-api-guide/
HTML audio基础API完全使用指南

连接池
https://pynative.com/psycopg2-python-postgresql-connection-pooling/

Python psycopg2 mogrify
The mogrify is a psycopg2 extension to the Python DB API that returns a query string after arguments binding. The returned string is exactly the one that would be sent to the database running the execute() method or similar.
 print(cur.mogrify("SELECT name, price FROM cars WHERE id=%s", (2,)))

# Binary
https://zetcode.com/python/psycopg2/
CREATE TABLE images(id SERIAL PRIMARY KEY, data BYTEA);
create table a(a bytea);
create unique index a_bytea_unique_hash on a (md5(a)); # md5 唯一索引


INSERT INTO test_table  
VALUES(1, pg_read_binary_file('/path/to/file')::bytea); 

    cur = con.cursor()
    data = readImage()
    binary = psycopg2.Binary(data)
    cur.execute("INSERT INTO images(data) VALUES (%s)", (binary,))

    con.commit()




CREATE TABLE btable (bvalue bytea);
INSERT INTO btable (bvalue) values(decode(‘%s’,’base64′));
SELECT encode(bvalue,’base64′) FROM btable;


def writeImage(data):

    fout = None

    try:
        fout = open('sid2.jpg', 'wb')
        fout.write(data)

    except IOError as e:

        print(f"Error {0}")
        sys.exit(1)

    finally:

        if fout:
            fout.close()


try:
    con = psycopg2.connect(database='testdb', user='postgres',
                    password='s$cret')

    cur = con.cursor()
    cur.execute("SELECT data FROM images LIMIT 1")
    data = cur.fetchone()[0]

    writeImage(data)


<td width="15%" align="center" valign="middle" style="border:1px solid #999;"><audio id="fayint99" src="/sound/mp3/ngo5.mp3" preload="preload"> <font color="#FF0000">您的浏览器不支持此发音。</font> </audio>
<img src="images/pc_fayin.gif" alt="点击发音" onclick="fyint99()" style=" cursor: pointer">
<script type="text/javascript">
<!--
var fyt99=document.getElementById("fayint99");
function fyint99()
{
if (fyt99.paused)
fyt99.play();
else
fyt99.pause();
}
//-->
</script>
</td>

```



```

# http://codingsky.com/doc/day/2018-06-10/12141.html
动态JPEG流传输：

    #!/usr/bin/env python
    from flask import Flask, render_template, Response
    from camera import Camera

    app = Flask(__name__)

    @app.route('/')
    def index():  
      return render_template('index.html')

    def gen(camera):
      while True:
        frame = camera.get_frame()
        yield (b'--framern'
            b'Content-Type: image/jpegrnrn' + frame + b'rn')

    @app.route('/video_feed')
    def video_feed():
      return Response(gen(Camera()),
              mimetype='multipart/x-mixed-replace; boundary=frame')

    if __name__ == '__main__':
      app.run(host='0.0.0.0', debug=True)
这个应用导入一个Camera类来负责提供帧序列。在这个例子中，将camera控制部分放入一个单独的模块是一个很好的主意。这样，Web应用会保持干净、简单和通用。

该应用有两个路由（route）。/路由为主页服务，被定义在index.html模板中。下面你能看到这个模板文件中的内容：



    <html>
     <head>
      <title>Video Streaming Demonstration</title>
     </head>
     <body>
      <h1>Video Streaming Demonstration</h1>
      <img src="{{ url_for('video_feed') }}">
     </body>
    </html>
```



```
# jquery
https://blog.csdn.net/l333f/article/details/60877276

# flask blog
https://github.com/zengxuanlin/my_blog

```



```
# auto play
<script type="text/javascript">
    window.onload = function(){
             setInterval("toggleSound()",100);
        }

    function toggleSound() {
                var music = document.getElementById("vd");//获取ID  
                    
                if (music.paused) { //判读是否播放  
                    music.paused=false;
                    music.play(); //没有就播放 
                }    
        }
</script>
```







```
ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3
Explanation of the used arguments in this example:

-i - input file

-vn - Disable video, to make sure no video (including album cover image) is included if the source would be a video file

-ar - Set the audio sampling frequency. For output streams it is set by default to the frequency of the corresponding input stream. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options.

-ac - Set the number of audio channels. For output streams it is set by default to the number of input audio channels. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options. So used here to make sure it is stereo (2 channels)

-b:a - Converts the audio bitrate to be exact 192kbit per second
```







```
ffmpeg -i -ss 0 -t 00:01:00
```



```
with -t which specifies the duration, like -ss 60 -t 10 to capture from second 60 to 70

```



## insert bytea



```
# 已有端口映射
iptables -t nat -vnL DOCKER
```

```
yum install openssh-server -y
vi /etc/ssh/sshd_config
	配置并保存：PermitRootLogin yes    UsePAM no
systemctl start sshd
exit (CTRL + P, CTRL + Q)
```



```
sftp root@172.17.0.2
ls lls pwd llpwd
put t.mp3 .
exit

ssh root@172.17.0.2
```



```
cp t.mp3 /var/lib/pgsql
su - postgres
psql
CREATE TABLE audio(id SERIAL PRIMARY KEY, data BYTEA);
INSERT INTO audio(data) VALUES(pg_read_binary_file('/var/lib/pgsql/t.mp3')::bytea);
```



### insert from psycopg2

```
binary = psycopg2.Binary(data)
cur.execute("INSERT INTO images(data) VALUES (%s)", (binary,))
```



### time out

```
psycopg2.connect( dbname = databaseName, user = userName, host = hostName, port = 5432, connect_timeout = 5, options='-c statement_timeout=5000')
```

### 自动重连

```
https://github.com/psycopg/psycopg2/issues/419
```









INSERT INTO test_table  

VALUES(1, pg_read_binary_file('/path/to/file')::bytea);



### 高端操作

https://bbengfort.github.io/2017/12/psycopg2-transactions/



## Cutting small sections

To extract only a small segment in the middle of a movie, it can be used in combination with `-t` which specifies the duration, like `-ss 60 -t 10` to capture from second 60 to 70. Or you can use the `-to` option to specify an out point, like `-ss 60 -to 70` to capture from second 60 to 70. `-t` and `-to` are mutually exclusive. If you use both, `-t` will be used.

Note that if you specify `-ss` before `-i` only, the timestamps will be reset to zero, so `-t` and `-to` will have the same effect. If you want to keep the original timestamps, add the `-copyts` option.

The first command will cut from 00:01:00 to 00:03:00 (in the original), using the faster seek.
The second command will cut from 00:01:00 to 00:02:00, as intended, using the slower seek.
The third command will cut from 00:01:00 to 00:02:00, as intended, using the faster seek.

```
ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy cut.mp4
ffmpeg -i video.mp4 -ss 00:01:00 -to 00:02:00 -c copy cut.mp4
ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy -copyts cut.mp4
```

If you cut with stream copy (`-c copy`) you need to use the [-avoid_negative_ts 1](https://ffmpeg.org/ffmpeg-all.html#Format-Options) option if you want to use that segment with the [concat demuxer](https://trac.ffmpeg.org/wiki/How to concatenate (join, merge) media files#demuxer) .

Example:

```
ffmpeg -ss 00:03:00 -i video.mp4 -t 60 -c copy -avoid_negative_ts 1 cut.mp4
```

If you have to re-encode anyway, e.g., to apply filters like [afade](https://trac.ffmpeg.org/wiki/AfadeCurves), which can be very slow, make sure to use, e.g., `-ss 120 -i some.mov -to 60` to get one minute from 120s to 120+60s, not `-to 180` for three minutes starting at 120s.



```
# show info
ffprobe xxx.mp4

“-an”（no audio）和“-vn”（no video）
ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -vn -acodec copy -ss 0 -t 00:01:00 ttttttttt.ts

ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -vn -acodec copy -ss 00:01:12.960 -to 00:01:14.640 ttttttttt.ts

00:01:12,960 --> 00:01:14,640


ffmpeg -i test.mp4 -codec copy -bsf h264_mp4toannexb test.ts
```





```
/usr/local/ffmpeg/bin/ffmpeg -ss START  -t LENGTH -i INPUTFILE  -vcodec copy -acodec copy OUTFILE

00:01:00 长度1分钟
/usr/local/ffmpeg/bin/ffmpeg -ss 0 -t 00:01:00 -i movie.mp4  -vcodec copy -acodec copy movie-1.mp4

```





```
https://it3q.com/article/59

```



```
今天考虑一个mcu混合的实现，也就是接收多路过来的rtp流，然后转发出去一路的rtmp流，使用ffmpeg测试做的记录，刚开始一直通过ffmpeg推送的文件流不能满足要求，还是对参数配置不熟悉；



0、ffmpeg 命令格式：

$ ffmpeg \

-y \ # 全局参数

-c:a libfdk_aac -c:v libx264 \ # 输入文件参数

-i input.mp4 \ # 输入文件

-c:v libvpx-vp9 -c:a libvorbis \ # 输出文件参数

output.webm # 输出文件



下列为较常使用的参数：

 

-i——设置输入文件名。

-f——设置输出格式。

-y——若输出文件已存在时则覆盖文件。

-fs——超过指定的文件大小时则结束转换。

-t——指定输出文件的持续时间，以秒为单位。

-ss——从指定时间开始转换，以秒为单位。

-t从-ss时间开始转换（如-ss 00:00:01.00 -t 00:00:10.00即从00:00:01.00开始到00:00:11.00）。

-title——设置标题。

-timestamp——设置时间戳。

-vsync——增减Frame使影音同步。

-c——指定输出文件的编码。

-metadata——更改输出文件的元数据。

-help——查看帮助信息

影像参数：

-b:v——设置影像流量，默认为200Kbit/秒。（单位请引用下方注意事项）

-r——设置帧率值，默认为25。

-s——设置画面的宽与高。

-aspect——设置画面的比例。

-vn——不处理影像，于仅针对声音做处理时使用。

-vcodec( -c:v )——设置影像影像编解码器，未设置时则使用与输入文件相同之编解码器。

声音参数：

-b:a——设置每Channel（最近的SVN版为所有Channel的总合）的流量。（单位请引用下方注意事项）

-ar——设置采样率。

-ac——设置声音的Channel数。

-acodec ( -c:a ) ——设置声音编解码器，未设置时与影像相同，使用与输入文件相同之编解码器。

-an——不处理声音，于仅针对影像做处理时使用。

-vol——设置音量大小，256为标准音量。（要设置成两倍音量时则输入512，依此类推。）

-preset：指定输出的视频质量，会影响文件的生成速度，有以下几个可用的值 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow。 



1、udp或者rtp推流

>最简单模式：

ffmpeg -re -i d:\videos\1080P.264 -vcodec copy -f rtp rtp://127.0.0.1:1234

ffplay接收端的命令：

ffplay -protocol_whitelist "file,udp,rtp" -i rtp://127.0.0.1:1234



>复杂模式，决定rtp包封装大小，封装格式，决定I帧间隔

ffmpeg -re -i tuiliu_mp4.mp4 -vcodec libx264 -b:v 800k -s 480x320   -preset:v ultrafast -tune:v zerolatency   -an -f rtp  -profile baseline  -rtpflags h264_mode0 -pkt_size 1460 -slice-max-size 1400 -maxrate 600k -minrate 600k  -r 20 -g 20 -keyint_min 20   -an -f rtp rtp://11.12.112.42:49196

关键命令参数说明：

-re一定要加，代表按照帧率发送

-i url (input)   输入文件路径或者 url

-vcodec libx264 ，表示使用x264重新编码

-b:v 800k  码率设置

-s 480x320   分辨率设置

-preset:v ultrafast    开启x264的 -preset fast/faster/verfast/superfast/ultrafast参数

-tune:v zerolatency   即时编码，去掉编码延迟

-profile: 设置编码等级，baseline, main, high 

-payload_type ：rtp的pt值

-pkt_size：rtp发送的最大长度

-slice-max-size：一个nula包数据的最大长度

-rtpflags h264_mode0  rtp打包模式 packetizition-mode=0， 当 packetization-mode 的值为 0 时或不存在时, 必须使用单一 NALU 单元模式.；当 packetization-mode 的值为 1 时必须使用非交错(non-interleaved)封包模式.；当 packetization-mode 的值为 2 时必须使用交错(interleaved)封包模式.

-pkt_size 1460 

-slice-max-size 1400 

-maxrate 600k 

-minrate 600k  (可以使用 -crf 24替换，控制视频码率和质量的均衡)

-r 20  设置帧率为20帧/s

-g 20 GOP间隔，每隔20个帧为一个GOP，两个关键帧之间的帧数称为一个GOP，将关键帧帧间隔设置为1s,也就是每秒一个关键帧

-keyint_min 20   最小关键帧间隔 

-an 没有音频，“-an”（no audio）和“-vn”（no video）分别用来单独输出视频和音频

-f:rtp 强制ffmpeg采用某种格式，后跟对应的格式。



> 使用RTP分别发送音频流和视频流

FFmpeg命令：

ffmpeg  -re -i <media_file> -an -vcodec copy -f rtp rtp://<IP>:5004 -vn -acodec copy -f rtp rtp://<IP>:5005 > test.sdp



FFplay接收的SDP文件：

SDP:
v=2 
m=video 5004 RTP/AVP 96
a=rtpmap:96 H264
t=0 0 
a=framerate:25
c=IN IP4 192.168.0.100
  
m=audio 5005 RTP/AVP 97
a=rtpmap:97 PCM/8000/1
a=framerate:25
c=IN IP4 192.168.0.100

2、rtsp推流

ffmpeg -re -i /root/mp4/1.mp4 -vcodec copy -acodec copy  -rtsp_transport tcp -f rtsp rtsp://192.168.2.161/live/rtsp_test

-rtsp_transport tcp 标识使用tcp作为rtp的通道



3、rtmp推流 

ffmpeg -re -i /root/mp4/1.flv -vcodec copy -acodec copy -f flv rtmp://192.168.2.161/live/rtsp_test



修改-i参数为rtsp的地址，可以拉监控流然后转发为rtmp流：

ffmpeg -f rtsp -i rtsp://admin:xdddd1998@11.12.112.249:554/h264/ch1/sub/av_stream -vcodec libx264 -b:v 800k -s 480x320 -preset:v ultrafast -tune:v zerolatency   -an -f rtp  -profile baseline  -rtpflags h264_mode0 -pkt_size 1460 -slice-max-size 1400 -maxrate 600k -minrate 600k -g 20 -keyint_min 20  -y rtp://11.12.112.42:62159



4、ffmpeg切片，很多人会问，直接播放mp4不就好了么，为什么要切片再播放？

如果是MP4文件，需要先完整的下载格式为 mp4 的视频文件，当视频文件下载完成后，网站才可以播放该视频，这就对于用户体验是极大的下降，所以需要切片为多个ts文件，以及m3u8文件，m3u8格式的视频是将文件分成一小段一小段的ts文件，播放完一个在播放下一个，由于每次请求的ts文件都很小，所以基本可以做到无延时播放：

切片mp4视频文件：

ffmpeg -i ./video.mp4 -c:v libx264 -hls_time 60 -hls_list_size 0 -c:a aac -strict -2 -f hls ./video.m3u8



切片mp3音频文件：

ffmpeg -i ./kczfrr.mp3 -c:a libmp3lame -map 0:0 -f segment -segment_time 10 -segment_list ./kczfrr.m3u8



web页面播放m3u8，一方面可以使用腾讯的js插件，另一方面就是使用video.js的插件:

引入相关资源
    <link href="https://cdn.bootcss.com/video.js/6.3.3/video-js.min.css" rel="stylesheet">
    <script src="https://cdn.bootcss.com/video.js/6.3.3/video.min.js"></script>
    <script src="https://cdn.bootcss.com/videojs-contrib-hls/5.11.0/videojs-contrib-hls.js"></script>
    <!–[if lt IE 9]>
    <script type="text/javascript" src="http://cdn.static.runoob.com/libs/html5shiv/3.7/html5shiv.min.js"></script>
    <![endif]–>
说明：
 
video-js.min.css 是播放器的主题样式
video.min.js 是video.js的核心代码
videojs-contrib-hls.js 用于支持HLS的库文件
html5shiv.min.js 由于video.js是基于H5构建的播放器，所以在浏览器不支持H5的时候，需要将相关资源引入到浏览器
放置播放器控件
<video  id="myVideo"  class="video-js vjs-default-skin vjs-big-play-centered"  width="400"
        controls="controls" autoplay="autoplay"
       x-webkit-airplay="true" x5-video-player-fullscreen="true"
       preload="auto" playsinline="true" webkit-playsinline
       x5-video-player-typ="h5">
    <source type="application/x-mpegURL" src="https://cn4.creativemas.cn/ppvod/DD7AB8D25F6AD21E4291775FEAC1F710.m3u8">
</video>
说明：
 
该控件中用于播放一个网络上找的m3u8的视频资源
给控件一个id主要方便video.js获取控件对象
使用video.js
<script>
    // videojs 简单使用
    var myVideo = videojs('myVideo',{
        bigPlayButton : true,
        textTrackDisplay : false,
        posterImage: false,
        errorDisplay : false,
    })
    myVideo.play() // 视频播放
    myVideo.pause() // 视频暂停
</script>


5、合并音视频

合并视频和音频
1、直接合并
视频文件中没有音频
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4video.mp4,audio.wav分别是要合并的视频和音频，output.mp4是合并后输出的音视频文件。
 
下面的命令是用audio音频替换video中的音频ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output.mp4
 
2、先提取视频中的音频，将两个音频合并成一个音频，然后将合并的音频与视频进行合并
#获取视频中的音频
ffmpeg -i input.mp4 -vn -y -acodec copy output.aac
#去掉视频中的音频
ffmpeg -i input.mp4 -an output.mp4
#合并两个音频
ffmpeg -i input1.mp3 -i output.aac -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 output.mp3
#合并音频和视频
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
 
 
3、合并视频
#横向合并视频
ffmpeg -i input1.mp4 -i input2.mp4 -lavfi hstack output.mp4
 
上面的命令虽然可以合并视频，两个视频可以正常播放，但是只保留了前面一个的音频。
#合并多个视频，可以使用下面命令行：
ffmpeg -i input1.mp4 -i input2.mp4 -i input3.mp4 -lavfi hstack=inputs=3 output.mp4
 
#纵向合并视频
ffmpeg -i input1.mp4 -i input2.mp4 -lavfi vstack output.mp4
 
 
#网格合并视频，来源:https://www.zhihu.com/question/300182407
当多个视频时，还可以合并成网格状，比如2x2，3x3这种。但是视频个数不一定需要是偶数，如果是奇数，可以用黑色图片来占位。
 
ffmpeg -f lavfi -i color=c=black:s=1280x720 -vframes 1 black.png
该命令将创建一张1280*720的图片
 
然后就可以使用下面这个命令来合并成网格视频了，如果只有三个视频，可以选择上面创建的黑色图片替代。
ffmpeg -i top_left.mp4 -i top_right.mp4 -i bottom_left.mp4 -i bottom_right.mp4 \
-lavfi "[0:v][1:v]hstack[top];[2:v][3:v]hstack[bottom];[top][bottom]vstack"
-shortest 2by2grid.mp4
 
上面创建的是正规的2x2网格视频。想象一下，现在只有三个视频，我想把第一个视频摆放在第一行的中间，然后把第二、三个视频摆放在第二行。那么就可以使用下面两个命令了。
 
ffmpeg -f lavfi -i color=c=black:s=640x720 -vframes 1 black.png
 
ffmpeg -i black.png -i top_center.mp4 -i bottom_left.mp4 -i bottom_right.mp4
-lavfi "[0:v][1:v][0:v]hstack=inputs=3[top];[2:v][3:v]hstack[bottom];[top][bottom]vstack"
-shortest 3_videos_2x2_grid.mp4
  
4、怎么合并两个视频并保留两个视频中的音频，注意视频的分辨率和格式必须一样。
#合并两个视频，只有一个声音;
纵向合并视频
ffmpeg -i input1.mp4 -i input2.mp4 -lavfi vstack output.mp4
 
#抽取两个视频中的音频，然后合并成一个音频; 
ffmpeg -i input_1.mp4 -vn -y -acodec copy output_a1.m4a
ffmpeg -i input_2.mp4 -vn -y -acodec copy output_a2.m4a
ffmpeg -i output_a1.m4a -i output_a2.m4a -filter_complex amerge -ac 2 -c:a copy -q:a 4 output_a.m4a
 
#将这个音频替换到之前的合并视频中;
ffmpeg -i video.mp4 -i output_a.m4a -c:v copy -c:a aac -strict experimental output.mp4
 
 
5、音频拼接
#两个拼接
/usr/local/ffmpeg/bin/ffmpeg -i d1.mp3 -i d2.mp3 -filter_complex '[0:0] [1:0] concat=n=2:v=0:a=1 [a]' -map [a] j5.mp3
#三个拼接
/usr/local/ffmpeg/bin/ffmpeg -i 片头.wav -i 内容.WAV -i 片尾.wav -filter_complex '[0:0] [1:0] [2:0] concat=n=3:v=0:a=1 [a]' -map [a] 合成.wav
 
#多文件拼接
ffmpeg -f concat -ilist.txt -c copycutebaby.mp3
list.txt文件内容:à按顺序连接cutebaby_1.mp3, football.mp3,cutebaby_2.mp3,cutebaby_3.mp3
 
#拼接不同格式的文件，下面的命令合并了三种不同格式的文件，FFmpeg concat 过滤器会重新编码它们。注意这是有损压缩。
[0:0] [0:1] [1:0] [1:1] [2:0] [2:1] 分别表示第一个输入文件的视频、音频、第二个输入文件的视频、音频、第三个输入文件的视频、音频。concat=n=3:v=1:a=1 表示有三个输入文件，输出一条视频流和一条音频流。[v] [a] 就是得到的视频流和音频流的名字，注意在 bash 等 shell 中需要用引号，防止通配符扩展。 
 
ffmpeg -i input1.mp4 -i input2.webm -i input3.avi -filter_complex '[0:0] [0:1] [1:0] [1:1] [2:0] [2:1] concat=n=3:v=1:a=1 [v] [a]' -map '[v]' -map '[a]' <编码器选项> output.mkv
```



```
m3u8格式的视频是将文件分成一小段一小段的ts文件，播放完一个在播放下一个，由于每次请求的ts文件都很小，所以基本可以做到无延时播放。目前WEB上主流的直播方案主要是HLS和RTMP，移动端主要是HLS，PC端主要是RTMP。

HLS是苹果推出的，移动端不管是IOS还是Android都天然支持HLS协议，直接在h5页面直接配置即可使用；PC端只有safari浏览器支持，其他浏览器均不支持。

可以用video.js和videojs-contrib-hls.js。video.js是非常好用的插件，关于它如何使用这里就不一一介绍了。

```



```
流媒体：ffmpeg生成HLS的m3u8与ts片段
 

转换方式一
1.直接把媒体文件转为ts

ffmpeg -i cat.mp4 -c copy -bsf h264_mp4toannexb cat.ts
2.使用segment参数进行切片

ffmpeg -i cat.ts -c copy -map 0 -f segment -segment_list playlist.m3u8 -segment_time 2 cat_output%03d.ts
 

 

转换方式二
1.ffmpeg切片命令，以H264和AAC的形式对视频进行输出

ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict -2 -f hls output.m3u8
2.ffmpeg转化成HLS时附带的指令

-hls_time n: 设置每片的长度，默认值为2。单位为秒

-hls_list_size n:设置播放列表保存的最多条目，设置为0会保存有所片信息，默认值为5

-hls_wrap n:设置多少片之后开始覆盖，如果设置为0则不会覆盖，默认值为0.这个选项能够避免在磁盘上存储过多的片，而且能够限制写入磁盘的最多的片的数量

-hls_start_number n:设置播放列表中sequence number的值为number，默认值为0

3.对ffmpeg切片指令的使用

ffmpeg -i output.mp4 -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 5 data/output.m3u8 
参数:

-hls_base_url   m3u8播放地址前缀

-segment_list_entry_prefix  m3u8播放地址前缀

-s 1280x720    :  720p分辨率
-b 1500k  比特率
-r 设定帧速率，默认为25
-aspect 设定画面的比例
```



# graphql

- https://github.com/graphile/postgraphile

  > nodejs

- https://ruby-china.org/topics/40334

  > PostGraphile：将 Postgres 数据库变成全功能 GraphQL 后端
  >
  > 这个工具可以直接把一个 postgres 数据库生成为一个 graphql 后端，内置了对每个表格的 crud query 及 mutation。
  >
  > 为什么说是全功能的呢？因为仅仅通过 graphile 和 pg 可以做到传统后端需要的任何事，而且所有需要写的代码和配置都在 postgres 里，迁移的时候直接导出 postgres 数据库，就能备份整个后端。
  >
  > 除了生成的 crud，用户可以用 pl/sql 写业务逻辑的函数，一个有副作用（cud）的函数会直接挂载为 graphql 的 mutation，无副作用的则会挂载为 query。
  >
  > graphile 对数据库的更新鉴权是使用 pg 内置的 role 和 row level security 实现的。一般应用需要两个 role：登陆前的 anonymous 和登陆后的 user。我们可以通过 grant 来对不同 role 配置他们能对表进行的操作，而 row level security 则允许我们配置一个 session 对行的权限，在 cud 行的时候，可以执行一些 check，例如检查当前用户 id 是不是和要修改的数据一样。
  >
  > 和 hasura 对比的好处：
  >
  > - graphile 以 postgres 为中心，没有自己的 metadata。hasura 把关联的配置保存为一份自己的配置，这样在迁移的时候除了导出数据库，还需要导出 hasura 的配置。而 graphile 的关联信息是完全通过 pg 内的外键关联推导出来的。
  > - hasura 实现登陆鉴权功能的时候需要一个外部服务器。graphile 不需要一个额外的服务器，凭借自身就可以实现登陆注册，签署 jwt。
  > - graphile 使用 pg 内置的 row level security 来处理权限，而 hasura 是用一套自己的鉴权机制来处理的。

- https://www.jianshu.com/p/a300a964c797

  

# nginx



```
有没有人遇到 Nginx 做反代 https 登陆页面出现问题

无聊做了个反代上dmm
结果dmm的https登陆页面一直不太对
首先响应的时间就非常长，经常超时
然后也无法正常登陆,一直提示密码错误

然而用squid正代就没有任何问题
基本可以确定肯定是nginx哪里错了

研究了半天还是没什么成果。。。所以我就想问问我究竟在哪里掉坑里了

贴部分配置：
server {
listen server_ip:443 ssl;
server_name www.dmmm.com;

ssl_certificate     /usr/local/nginx/conf/server.crt;
    ssl_certificate_key  /usr/local/nginx/conf/server.key;

    ssl_session_cache    shared:SSL:1m;
    ssl_session_timeout  5m;

    ssl_ciphers  HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers  on;

    location / {
        proxy_pass https://www.dmm.com;

        proxy_set_header Host $http_host;

        proxy_max_temp_file_size     0k;
        proxy_connect_timeout       60;
        proxy_send_timeout         60;
        proxy_read_timeout         60;
        proxy_buffers             256 4k;
        proxy_busy_buffers_size      64k;
        proxy_redirect            off;
    }
}
第 1 条附言  ·  2015-03-31 22:08:05 +08:00
今天已经完成排错任务原因为:
[kQBYS09a1******@********* ~]$ cat /usr/local/nginx/logs/error.log | grep invalid
2015/03/31 16:15:46 [info] 11637#0: *73 client sent invalid header line: "DMM_TOKEN: b909db2e73f6d2c9ab1a6**********" while reading client request headers, client: ********, server: www.dmm.com, request: "POST /my/-/login/ajax-get-token/ HTTP/1.1", host: "www.dmm.com"
经过查阅文档nginx对于"DMM_TOKEN"这类带有下划线的header认为不合法自动忽略
nginx作者和下划线到底有多大仇~~~~~
解决方法也很简单:
underscores_in_headers on
```



# acg power 代理



```
http://127.0.0.1:8123/proxy.pac  # 它定义的ip、网址规则，改它(for dmm game player)
```







# 解密



```
https://www.v2ex.com/t/311275

求帮忙破解 AES-128 加密的 m3u8+ts+key 视频
     gushengren · 2016-10-09 01:21:20 +08:00 · 18439 次点击  
这是一个创建于 1859 天前的主题，其中的信息可能已经有所发展或是发生改变。
把浏览器缓存的东西都复制出来了,除了 m3u8 和 key,其他的都是 ts 文件,哪位大神能帮忙破解一下,想把这个视频下下来啊.生成一个可以播放的视频
链接： http://pan.baidu.com/s/1nvvZCSh 密码： hoqf
18439 次点击  ∙  12 人收藏  加入收藏  Tweet  忽略主题  感谢
 M3U8 key 破解 帮忙32 条回复  •  2017-05-18 17:51:15 +08:00
gushengren		        Reply    1
gushengren   2016-10-09 02:49:26 +08:00
求大神来帮忙
annielong		        Reply    2
annielong   2016-10-09 09:21:47 +08:00
ts 文件也加密了吗？先看看 ts 文件能不能直接播放，如果可以直接播放就是没有加密，直接合并就行了
xxxyyy		        Reply    3
xxxyyy   2016-10-09 09:43:19 +08:00 via Android
av 来的呀，不过分辨率也太小了，只有 320x180 ，而且还打码了
Ellison		        Reply    4
Ellison   2016-10-09 11:25:49 +08:00
@xxxyyy 推荐楼主直接问老司机要番号
gushengren		        Reply    5
gushengren   2016-10-09 12:39:37 +08:00
@annielong TS 如果不加密,我就不用在这问了
gushengren		        Reply    6
gushengren   2016-10-09 12:40:10 +08:00
@xxxyyy 神人,你破了吗?
xxxyyy		        Reply    7
xxxyyy   2016-10-09 12:50:56 +08:00 via Android
@gushengren 你不知道里面的内容的吗？
gushengren		        Reply    8
gushengren   2016-10-09 12:56:05 +08:00
@xxxyyy 我知道啊,我看你居然知道里面的内容,你是破解了吗?兄弟,跪求方法啊
gushengren		        Reply    9
gushengren   2016-10-09 12:57:23 +08:00
@xxxyyy 可以留个联系方式吗?
gushengren		        Reply    10
gushengren   2016-10-09 14:12:33 +08:00
哪位大神神帮帮我啊.555555555555555555
xxxyyy		        Reply    11
xxxyyy   2016-10-09 14:50:15 +08:00 via Android
有 telegram 吗？
gushengren		        Reply    12
gushengren   2016-10-09 14:55:47 +08:00
@xxxyyy 没有呢,有没有比较低端的联系方式啊,呵呵
likuku		        Reply    13
likuku   2016-10-09 15:10:01 +08:00
暴力穷举猜密码的话，就放弃吧，当前地球人的计算设备还不够强。

坐等量子超级电脑。
xxxyyy		        Reply    14
xxxyyy   2016-10-09 15:20:13 +08:00
@gushengren QQ ：(捌)361(零)992(壹)
v2014		        Reply    15
v2014   2016-10-09 15:47:29 +08:00
费了洪荒之力终于看到那女的穿的是条纹衣服
gushengren		        Reply    16
gushengren   2016-10-09 15:55:23 +08:00
@v2014 哈哈,你能也破?跪求指导
v2014		        Reply    17
v2014   2016-10-09 16:02:33 +08:00
@gushengren 楼上不是有 QQ 么，你拿 key 和视频用 aes128 算法解密就可以了
gushengren		        Reply    18
gushengren   2016-10-09 16:04:12 +08:00
就是不知道怎么解密啊,兄弟,原理我都懂的,不然我也不会提供出解密需要的东西啊,能提供下 QQ 指导一下么,不胜感激
gushengren		        Reply    19
gushengren   2016-10-09 16:06:20 +08:00
@v2014 我用 ffmpeg 接收 它报个未知格式的错误,我 TM 就 SB 了,不知道咋办了
v2014		        Reply    20
v2014   2016-10-09 16:15:39 +08:00
@gushengren 我不会 ffmpeg ，只是用 python 解了个视频。你可以看看这个 http://dola.xinfan.org/?p=549
monkeygo		        Reply    21
monkeygo   2016-10-09 16:20:03 +08:00 via iPhone
都是老司机
gushengren		        Reply    22
gushengren   2016-10-09 16:22:18 +08:00
@v2014 这个我看了,根本不知道如何操作,提到命令行的时候,呵呵
tinyproxy		        Reply    23
tinyproxy   2016-10-09 17:09:44 +08:00   ❤️ 2
这个不叫破解。。。 AES 的 mode 就那么几个，你知道是 AES-128 ，试一下不就好了。

我随便下了一个文件，这个是我的代码，其它的你自己处理吧。
#!/usr/bin/env python
# -*- coding: utf8 -*-
from Crypto.Cipher import AES

raw = file('dyVuoO%2BiKIqY%2B3Ebf3CavNpB5RKlXfGtInP31znaGCfYnVkrSsAF46r2hg-1', 'rb').read()
iv = raw[0:16]
data = raw[16:]
key = file('key', 'rb').read()

plain_data = AES.new(key, AES.MODE_CBC, iv).decrypt(data)
file('fuck.mp4', 'wb').write(plain_data)
VYSE		        Reply    24
VYSE   2016-10-09 17:39:32 +08:00
http://www.dmm.co.jp
提取番号不就行了,这都是预览吧?
21grams		        Reply    25
21grams   2016-10-09 17:48:50 +08:00
key 都有了还不会解吗？
gushengren		        Reply    26
gushengren   2016-10-09 17:54:17 +08:00
@21grams 不会,我是小白
Jat001		        Reply    27
Jat001   2016-10-09 17:58:28 +08:00
@tinyproxy 万一是 gcm 怎么办？你怎么知道 iv 是前 16 字节？
tinyproxy		        Reply    28
tinyproxy   2016-10-09 18:48:49 +08:00   ❤️ 1
@Jat001
1. 楼上几位都明确暗示解密成功了，所以我也就是随便拿一种 mode 来猜的，当时第一反应是 CBC 。至于 GCM 咋办，因为没用过这种 mode ，所以暂时不了解加解密操作，不回复。
2. iv 是前 16 字节这个问题，这个是个人经验。我目前为止看过的所有代码都是直接把 iv 添加到密文前面去，所以也就随手试试，你看我的代码也没几行，不成功就算了呗。
Jat001		        Reply    29
Jat001   2016-10-09 19:08:57 +08:00
@tinyproxy gcm 加密时还需要 associated data ，加密完还会生成 tag 用作校验，具体实现可以参考。
https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.modes.GCM
crab		        Reply    30
crab   2016-10-09 19:13:56 +08:00
dmm 这网站的？
hwsdien		        Reply    31
hwsdien   2016-10-09 19:16:54 +08:00
key 都有了。。。
```







# hira2kata



```
pip install jaconv
```



```
import jaconv

# Hiragana to Katakana 平假名 ===> 片假名
jaconv.hira2kata(u'ともえまみ')
# => u'トモエマミ'

# Hiragana to half-width Katakana 平假名 ===> 半角片假名
jaconv.hira2hkata(u'ともえまみ')
# => u'ﾄﾓｴﾏﾐ'

# Katakana to Hiragana 片假名 ====> 平假名
jaconv.kata2hira(u'巴マミ')
# => u'巴まみ'

# half-width character to full-width character 半角 ===> 全角
jaconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
# => u'ティロ･フィナーレ'

# half-width character to full-width character
# but only ascii characters 只限ascii字符
jaconv.h2z(u'abc', ascii=True)
# => u'ａｂｃ'

# half-width character to full-width character
# but only digit characters
jaconv.h2z(u'123', digit=True)
# => u'１２３'

# half-width character to full-width character
# except half-width Katakana 除半角片假名
jaconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
# => u'ｱａｂｃ１２３'

# full-width character to half-width character 全角 ===> 半角
jaconv.z2h(u'ティロ・フィナーレ')
# => u'ﾃｨﾛ・ﾌｨﾅｰﾚ'

# full-width character to half-width character
# but only ascii characters 只限ascii字符
jaconv.z2h(u'ａｂｃ', ascii=True)
# => u'abc'

# full-width character to half-width character
# but only digit characters 只限数字
jaconv.z2h(u'１２３', digit=True)
# => u'123'

# full-width character to half-width character
# except full-width Katakana 除全角片假名
jaconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
# => u'アabc123'

# normalize
jaconv.normalize(u'ティロ･フィナ〜レ', 'NFKC')
# => u'ティロ・フィナーレ'

# Hiragana to alphabet 平假名===>罗马字
jaconv.kana2alphabet(u'じゃぱん')
# => japan

# Alphabet to Hiragana 罗马字===>平假名
jaconv.alphabet2kana(u'japan')
# => じゃぱん
```



# CentOS 远程

```
https://www.51sec.org/2020/07/06/install-configure-xfce-and-vnc-server-on-centos7/
	# 成功
	# 注意vncserver 的密码和linux 账号的密码是分开的
	# 要得设密码先切换某个linux 账号，然后 rm ~/.vnc/passwd
	# vncserver # 提示输入密码，后面再问设置 view only 密码，选择不设置
# https://vitux.com/centos-vnc-server/
# https://serverspace.io/support/help/installing-and-configuring-a-vnc-server-on-centos-7/

VNC 连接客户端用 Royal TSX，免费版就可以。只能建一个document
```



```
# https://www.getpagespeed.com/server-setup/clear-disk-space-centos
	清理空间
```





```
yum install -y epel-release && systemctl start xrdp && \
systemctl start xrdp && \
systemctl enable xrdp


firewall-cmd --zone=public  --add-port=3389/tcp --permanent
systemctl restart firewalld.service
```



```
# https://serverok.in/install-xfce-vnc-remote-desktop-on-centos-7

yum -y install epel-release & \
yum -y update

yum -y groupinstall "Server with GUI"
yum -y groupinstall "Xfce"
systemctl get-default
systemctl set-default graphical.target
systemctl isolate graphical.target
# yum groupremove "Xfce"
reboot


yum install -y tigervnc-server
vi ~/.vnc/xstartup
#!/bin/sh

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
/etc/X11/xinit/xinitrc
/bin/startxfce4
# 替换成上面


vncserver
vncserver -kill :1


https://www.realvnc.com/en/connect/download/viewer/windows/
# VNC Viewer 连接
209.141.34.77:1
```



```
# 查看端口
netstat -lntp | grep vnc
```



## 中文



```
locale -a |grep "zh_CN"
	yum groupinstall "fonts" -y # 没有输出则安装

vi /etc/locale.conf
LANG="zh_CN.uft8"  # 改成这样

source   /etc/locale.conf
echo $LANG 
date # 是否成功

```



```
# 成功，只要安装这个 VNC 就正常显示中文了
wget http://mirror.centos.org/centos/7/os/x86_64/Packages/google-noto-sans-cjk-fonts-20141117-5.el7.noarch.rpm

yum install google-noto-sans-cjk-fonts-20141117-5.el7.noarch.rpm -y
```



# Syncthing  同步

```
# https://www.cnblogs.com/jackadam/p/8568833.html

sed 's/127.0.0.1/0.0.0.0/g' /root/.config/syncthing/config.xml
	# 默认监听网络是127.0.0.1，远程不能访问

```





# FRP



```
frps.ini
[common]
bind_port = 7000

./frps -c frps.ini 
```



```
frpc.ini
[common]
server_addr = 209.141.34.77
server_port = 7000

[tcp_port]
type = tcp
local_ip = 127.0.0.1
local_port = 8085
remote_port = 7075

frpc.exe -c frpc.ini
```



```
209.141.34.77:7075 --> 会转到内网的8085
```









# NAS



```
linux使用LVM合并硬盘
FreeNAS11.0-U4配置iSCSI，给你电脑安装一个远程硬盘
ISCSI实现磁盘网络共享以及LVM方式共享拓展
用LVM，把四个盘在逻辑上集合成一个大盘组，再分区。
```



```
以 FreeNAS 举例，创建 iSCSI 存储的数量没有限制，还可以对已创建的 iSCSI 存储执行动态扩容，给电脑挂载一块无限容量的硬盘，很美妙吧。
```



# Colab

```
# star()开始
# stop()结束

function getElementByXpath(path) {
       return document.evaluate(path, document, null, 
       XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
 
function reconnect(){
	  console.log('working')
	  getElementByXpath("//div[@id='top-toolbar']/colab-connect-button").click()
}
var a = setInterval(reconnect, 1*60*1000);
function stop(){
	 clearInterval(a)
}
function start(){
	 a = setInterval(reconnect, 1*60*1000);
}
```



# VMWare





# NTFS



```
yum install ntfsprogs  # for mkfs.ntfs
```





https://www.51ittech.com/knowledge-base/centos-7-install-vmware-workstation-15/



```
https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle
YG5H2-ANZ0H-M8ERY-TXZZZ-YKRV8
UG5J2-0ME12-M89WY-NPWXX-WQH88
UA5DR-2ZD4H-089FY-6YQ5T-YPRX6
GA590-86Y05-4806Y-X4PEE-ZV8E0
ZF582-0NW5N-H8D2P-0XZEE-Z22VA
YA18K-0WY8P-H85DY-L4NZG-X7RAD
```

```
# 俄罗斯精简狂人 超级精简版集合 
# http://y-os.net/?p=770

Windows7旗舰版32位 ed2k://|file|cn_windows_7_ultimate_x86_dvd_x15-65907.iso|2604238848|D6F139D7A45E81B76199DDCCDDC4B509|/

Windows7旗舰版64位 ed2k://|file|cn_windows_7_ultimate_x64_dvd_x15-66043.iso|3341268992|7DD7FA757CE6D2DB78B6901F81A6907A|/

Windows7企业版32位 ed2k://|file|cn_windows_7_enterprise_x86_dvd_x15-70737.iso|2465783808|41ABFA74E57353B2F35BC33E56BD5202|/

Windows7企业版64位 ed2k://|file|cn_windows_7_enterprise_x64_dvd_x15-70741.iso|3203516416|876DCF115C2EE28D74B178BE1A84AB3B|/

Windows7专业版32位 ed2k://|file|cn_windows_7_professional_x86_dvd_x15-65790.iso|2604238848|E812FBE758F05B485C5A858C22060785|/

Windows7专业版64位 ed2k://|file|cn_windows_7_professional_x64_dvd_x15-65791.iso|3341268992|3474800521D169FBF3F5E527CD835156|/

Windows7家庭高级版32位 ed2k://|file|cn_windows_7_home_premium_x86_dvd_x15-65717.iso|2604238848|98E1EB474F92343B06737F227665DF1C|/

Windows7家庭高级版64位 ed2k://|file|cn_windows_7_home_premium_x64_dvd_x15-65718.iso|3341268992|9F976045631A6A2162ABE32FC77C8ACC|/

Windows7家庭初级版32位 ed2k://|file|cn_windows_7_home_basic_x86_dvd_x15-65975.iso|2604238848|AF82993DCF8F3D7AA08D54693691BB48|/

Windows7简易版32位 ed2k://|file|cn_windows_7_starter_x86_dvd_x15-69303.iso|2604238848|5A6796B2B6A97B3E372F7C37D3A42AA4|/

---------------------------------

Windows7英文旗舰版32位 ed2k://|file|en_windows_7_ultimate_x86_dvd_X15-65921.iso|2501894144|09902C7687C9CA86BD935BD0EFB61D3A|/

Windows7英文旗舰版64位 ed2k://|file|en_windows_7_ultimate_x64_dvd_X15-65922.iso|3224686592|6719AFC5486F38BE75F2DF39C8527113|/

Windows7繁体（台）旗舰版32位 ed2k://|file|tw_windows_7_ultimate_x86_dvd_x15-65908.iso|2578382848|D3570ECAED1D132724FCD399B523DB23|/

Windows7繁体（台）旗舰版64位 ed2k://|file|tw_windows_7_ultimate_x64_dvd_x15-65909.iso|3317223424|E6C906D22060285BE18929FADBA37F48|/

Windows7繁体（港）旗舰版32位 ed2k://|file|hk_windows_7_ultimate_x86_dvd_x15-65912.iso|2574176256|4AA63D85BEA48F5742BD22B8655363B2|/

Windows7繁体（港）旗舰版64位 ed2k://|file|hk_windows_7_ultimate_x64_dvd_x15-65911.iso|3313936384|917F16D04FBBFDE763A35E2A32595AD9|/

Windows7日文旗舰版32位  ed2k://|file|ja_windows_7_ultimate_x86_dvd_x15-65939.iso|2503079936|B02221E9B203CD065155D395B8C56E7F|/

Windows7日文旗舰版64位  ed2k://|file|ja_windows_7_ultimate_x64_dvd_x15-65940.iso|3241390080|826D4EF10382972267E39ECC011B81BA|/

Windows7多国语言包32位  ed2k://|file|mu_windows_7_language_pack_x86_dvd_x15-73272.iso|1936062464|A5FB4917B281929F30256924D8D0715E|/

Windows7多国语言包64位  ed2k://|file|mu_windows_7_language_pack_x64_dvd_x15-73276.iso|2306793472|21D6652E82D87305525366D5824AAFA2|/

---------------------------------

Windows Vista SP2简体中文32位  ed2k://|file|cn_windows_vista_with_sp2_x86_dvd_x15-36285.iso|3078893568|F50709974F03C63BB41B5CA0D406160D|/

Windows Vista SP2简体中文64位  ed2k://|file|cn_windows_vista_with_sp2_x64_dvd_x15-36322.iso|3817512960|3719CEC49ECC2D73FCF7AF152A42049A|/

Windows 2008 企业版&标准版 简体中文32位 ed2k://|file|cn_windows_server_standard_enterprise_and_datacenter_with_sp2_x86_dvd_x15-41045.iso|2190057472|E93B029C442F19024AA9EF8FB02AC90B|/

Windows 2008 企业版&标准版 简体中文64位 ed2k://|file|cn_windows_server_2008_standard_enterprise_and_datacenter_with_sp2_x64_dvd_x15-41319.iso|2952992768|5F2CA73C9DA296CB05E7C0319F7D0E62|/

Windows 2008 R2 企业版&标准版 简体中文64位 ed2k://|file|cn_windows_server_2008_r2_standard_enterprise_datacenter_web_vl_build_x64_dvd_x15-59777.iso|3270465536|1C7FDB37C0CEC1765A52CD49B2227CBE|/

==============================================
```


# whistle 抓包



https://wproxy.org/whistle/

https://github.com/whistle-plugins/examples



```
C:\Users\i\AppData\Roaming\npm
```





## 1. 启动 whistle： 

```shell
npm run start
```

## 2. 安装插件 

```shell
# npm 全局安装，跟普通 npm 包全局安装一样：
npm i -g whistle.autosave
```

## 3.启动前端

```shell
# 前端在插件根目录下的 public文件夹里边， \public\catchjson。也是安装了依赖的。
npm run serve
```

## 存在的问题

1. socket 没有做超时验证
2. 过于复杂



# CURL 



```
# 流媒体测试
	# https://github.com/CoiaPrant/MediaUnlock_Test/edit/main/check.sh
		由于国内外流媒体平台对与IP的限制，即使购买了对应区域的VPS，不进行不可描述操作的情况下是无法得知该VPS的IP是否解锁想要查询的流媒体平台的。
	# https://hostloc.com/forum.php?mod=viewthread&tid=895976&extra=&highlight=buyvm&page=1
		buyvm是frantech的分销商，最近正式推出了全新解锁多流媒体的VPS，一次性帮你搞定很多很多平时对IP要求严格的平台

	# buyvm官方流媒体优化机器中国特殊版China Special - STREAM RYZEN
		使用注意：
		1，自行把流媒体IP绑定到网卡，注意避免冲突，比如eth0:1
		2，后台设置出站IP为流媒体解锁IP
		3，相关程序 可能 也要修改出站IP
	
	# AbemaTV 不能看！台灣與香港解除地區限制懶人包
	

		使用的话，需要有日本的ip，自己vps或飞机场都行
		DNS设置为153.128.30.88

		仅提供AbemaTV

		如果无法观看，去这里测试
		www.dnsleaktest.com
		
		https://www.ablenet.jp/
			ablenet.jp之前用过，机器已经过期停掉了，没法给你做测试，但我的使用经验都是亲身体验，有个2个IP段给你作参考：	128.22.141.X、128.22.130.X，日本大阪原生IP
Netflix只能看自制剧，版权剧看不了，可以解锁公主连结日服、AbemaTV、DMM这些日本本地游戏、流媒体服务，网络标称200M带宽共享，流量不限，实际speedtest能跑出100多M这样，回大陆非晚高峰最高带宽只能再打个对折，甚至更慢，一旦短时间出现高带宽占用，无论是进网还是出网，比如运行测试脚本下载全世界多地区测试节点1GB大小的测试文件，就会被限速到10M以下

		https://www.daehub.com/archives/9611.html
			

	    kagoya.jp
            你可以试试kagoya.jp，按天计费，最低配月付价格和ablenet差不多，内存1G，比ablenet最低配高一倍，比cloudsigma日本最低配还便宜一些

	
#!/bin/bash
shell_version="1.4.1";
UA_Browser="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36";
UA_Dalvik="Dalvik/2.1.0 (Linux; U; Android 9; ALP-AL00 Build/HUAWEIALP-AL00)";
DisneyAuth="grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJiNDAzMjU0NS0yYmE2LTRiZGMtOGFlOS04ZWI3YTY2NzBjMTIiLCJhdWQiOiJ1cm46YmFtdGVjaDpzZXJ2aWNlOnRva2VuIiwibmJmIjoxNjIyNjM3OTE2LCJpc3MiOiJ1cm46YmFtdGVjaDpzZXJ2aWNlOmRldmljZSIsImV4cCI6MjQ4NjYzNzkxNiwiaWF0IjoxNjIyNjM3OTE2LCJqdGkiOiI0ZDUzMTIxMS0zMDJmLTQyNDctOWQ0ZC1lNDQ3MTFmMzNlZjkifQ.g-QUcXNzMJ8DwC9JqZbbkYUSKkB1p4JGW77OON5IwNUcTGTNRLyVIiR8mO6HFyShovsR38HRQGVa51b15iAmXg&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Adevice"
DisneyHeader="authorization: Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84"
Font_Black="\033[30m";
Font_Red="\033[31m";
Font_Green="\033[32m";
Font_Yellow="\033[33m";
Font_Blue="\033[34m";
Font_Purple="\033[35m";
Font_SkyBlue="\033[36m";
Font_White="\033[37m";
Font_Suffix="\033[0m";
LOG_FILE="check.log";

clear;
echo -e "流媒体解锁测试 MediaUnlock_Test" && echo -e "流媒体解锁测试 MediaUnlock_Test" > ${LOG_FILE};
echo -e "${Font_Purple}项目地址 https://github.com/CoiaPrant/MediaUnlock_Test ${Font_Suffix}" && echo -e "项目地址 https://github.com/CoiaPrant/MediaUnlock_Test" >> ${LOG_FILE};
echo -e "${Font_Purple}BUG反馈 https://github.com/CoiaPrant/MediaUnlock_Test/issues${Font_Suffix}" && echo -e "BUG反馈 https://github.com/CoiaPrant/MediaUnlock_Test/issues" >> ${LOG_FILE};
echo -e "${Font_Purple}联系作者 https://t.me/CoiaPrant${Font_Suffix}" && echo -e "联系作者 https://t.me/CoiaPrant" >> ${LOG_FILE};
echo -e "${Font_Purple}个人频道 https://t.me/CoiaPrant_Blog${Font_Suffix}" && echo -e "个人频道 https://t.me/CoiaPrant_Blog" >> ${LOG_FILE};
echo -e "${Font_Purple}声明 本测试工具根据GPL V3协议开源，严禁倒卖${Font_Suffix}" && echo -e "声明 本测试工具根据GPL V3协议开源，严禁倒卖" >> ${LOG_FILE};
echo -e "${Font_Purple}提示 本工具测试结果仅供参考，请以实际使用为准${Font_Suffix}" && echo -e "提示 本工具测试结果仅供参考，请以实际使用为准" >> ${LOG_FILE};
echo -e "${Font_Purple}国家代码 http://www.loglogo.com/front/countryCode/${Font_Suffix}" && echo -e "国家代码 http://www.loglogo.com/front/countryCode/" >> ${LOG_FILE};
echo -e " ** 当前版本: v${shell_version}" && echo -e " ** 当前版本: v${shell_version}" >> ${LOG_FILE};
echo -e " ** 系统时间: $(date)" && echo -e " ** 系统时间: $(date)" >> ${LOG_FILE};

export LANG="en_US";
export LANGUAGE="en_US";
export LC_ALL="en_US";

function InstallJQ() {
    #安装JQ
    if [ -e "/etc/redhat-release" ];then
        echo -e "${Font_Green}正在安装依赖: epel-release${Font_Suffix}";
        yum install epel-release -y -q > /dev/null;
        echo -e "${Font_Green}正在安装依赖: jq${Font_Suffix}";
        yum install jq -y -q > /dev/null;
        elif [[ $(cat /etc/os-release | grep '^ID=') =~ ubuntu ]] || [[ $(cat /etc/os-release | grep '^ID=') =~ debian ]];then
        echo -e "${Font_Green}正在更新软件包列表...${Font_Suffix}";
        apt-get update -y > /dev/null;
        echo -e "${Font_Green}正在安装依赖: jq${Font_Suffix}";
        apt-get install jq -y > /dev/null;
        elif [[ $(cat /etc/issue | grep '^ID=') =~ alpine ]];then
        apk update > /dev/null;
        echo -e "${Font_Green}正在安装依赖: jq${Font_Suffix}";
        apk add jq > /dev/null;
    else
        echo -e "${Font_Red}请手动安装jq${Font_Suffix}";
        exit;
    fi
}

function PharseJSON() {
    # 使用方法: PharseJSON "要解析的原JSON文本" "要解析的键值"
    # Example: PharseJSON ""Value":"123456"" "Value" [返回结果: 123456]
    echo -n $1 | jq -r .$2;
}

function PasteBin_Upload() {
    local uploadresult="$(curl -fsL -X POST \
        --url https://paste.ubuntu.com \
        --output /dev/null \
        --write-out "%{url_effective}\n" \
        --data-urlencode "content@${PASTEBIN_CONTENT:-/dev/stdin}" \
        --data "poster=${PASTEBIN_POSTER:-MediaUnlock_Test_By_CoiaPrant}" \
        --data "expiration=${PASTEBIN_EXPIRATION:-}" \
    --data "syntax=${PASTEBIN_SYNTAX:-text}")"
    if [ "$?" = "0" ]; then
        echo -e "${Font_Green}已生成报告 ${uploadresult} ${Font_Suffix}";
    else
        echo -e "${Font_Red}生成报告失败 ${Font_Suffix}";
    fi
}

function GameTest_Steam(){
    echo -n -e " Steam Currency:\t\t\t->\c";
    local result=`curl --user-agent "${UA_Browser}" -${1} -fsSL --max-time 30 https://store.steampowered.com/app/761830 2>&1 | grep priceCurrency | cut -d '"' -f4`;
    
    if [ ! -n "$result" ]; then
        echo -n -e "\r Steam Currency:\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Steam Currency:\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
    else
        echo -n -e "\r Steam Currency:\t\t\t${Font_Green}${result}${Font_Suffix}\n" && echo -e " Steam Currency:\t\t\t${result}" >> ${LOG_FILE};
    fi
}

function MediaUnlockTest_HBONow() {
    echo -n -e " HBO Now:\t\t\t\t->\c";
    # 尝试获取成功的结果
    local result=`curl --user-agent "${UA_Browser}" -${1} -fsSL --max-time 30 --write-out "%{url_effective}\n" --output /dev/null https://play.hbonow.com/ 2>&1`;
    if [[ "$result" != "curl"* ]]; then
        # 下载页面成功，开始解析跳转
        if [ "${result}" = "https://play.hbonow.com" ] || [ "${result}" = "https://play.hbonow.com/" ]; then
            echo -n -e "\r HBO Now:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo " HBO Now:\t\t\t\tYes" >> ${LOG_FILE};
            elif [ "${result}" = "http://hbogeo.cust.footprint.net/hbonow/geo.html" ] || [ "${result}" = "http://geocust.hbonow.com/hbonow/geo.html" ]; then
            echo -n -e "\r HBO Now:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " HBO Now:\t\t\t\tNo" >> ${LOG_FILE};
        else
            echo -n -e "\r HBO Now:\t\t\t\t${Font_Yellow}Failed (Parse Json)${Font_Suffix}\n" && echo -e " HBO Now:\t\t\t\tFailed (Parse Json)" >> ${LOG_FILE};
        fi
    else
        # 下载页面失败，返回错误代码
        echo -n -e "\r HBO Now:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " HBO Now:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
    fi
}

# 流媒体解锁测试-动画疯
function MediaUnlockTest_BahamutAnime() {
    echo -n -e " Bahamut Anime:\t\t\t\t->\c";
    local tmpresult=`curl -${1} --user-agent "${UA_Browser}" --max-time 30 -fsSL 'https://ani.gamer.com.tw/ajax/token.php?adID=89422&sn=14667' 2>&1`;
    if [[ "$tmpresult" == "curl"* ]]; then
        echo -n -e "\r Bahamut Anime:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Bahamut Anime:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result="$(PharseJSON "$tmpresult" "animeSn")";
    
    if [ "$result" != "null" ]; then
        resultverify="$(echo $result | grep -oE '[0-9]{1,}')";
        if [ "$?" = "0" ]; then
            echo -n -e "\r Bahamut Anime:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Bahamut Anime:\t\t\t\tYes" >> ${LOG_FILE};
        else
            echo -n -e "\r Bahamut Anime:\t\t\t\t${Font_Red}Failed (Parse Json)${Font_Suffix}\n" && echo -e " Bahamut Anime:\t\t\t\tFailed (Parse Json)" >> ${LOG_FILE};
        fi
    else
        local result="$(PharseJSON "$tmpresult" "error.code")";
        if [ "$result" != "null" ]; then
            resultverify="$(echo $result | grep -oE '[0-9]{1,}')";
            if [ "$?" = "0" ]; then
                echo -n -e "\r Bahamut Anime:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Bahamut Anime:\t\t\t\tNo" >> ${LOG_FILE};
            else
                echo -n -e "\r Bahamut Anime:\t\t\t\t${Font_Red}Failed (Parse Json)${Font_Suffix}\n" && echo -e " Bahamut Anime:\t\t\t\tFailed (Parse Json)" >> ${LOG_FILE};
            fi
        else
            echo -n -e "\r Bahamut Anime:\t\t\t\t${Font_Red}Failed (Parse Json)${Font_Suffix}\n" && echo -e " Bahamut Anime:\t\t\t\tFailed (Parse Json)" >> ${LOG_FILE};
        fi
    fi
}

# 流媒体解锁测试-哔哩哔哩大陆限定
function MediaUnlockTest_BilibiliChinaMainland() {
    echo -n -e " BiliBili China Mainland Only:\t\t->\c";
    local randsession="$(cat /dev/urandom | head -n 32 | md5sum | head -c 32)";
    # 尝试获取成功的结果
    local result=`curl --user-agent "${UA_Browser}" -${1} -fsSL --max-time 30 "https://api.bilibili.com/pgc/player/web/playurl?avid=82846771&qn=0&type=&otype=json&ep_id=307247&fourk=1&fnver=0&fnval=16&session=${randsession}&module=bangumi" 2>&1`;
    if [[ "$result" == "curl"* ]]; then
        echo -n -e "\r BiliBili China Mainland Only:\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " BiliBili China Mainland Only:\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result="$(PharseJSON "${result}" "code")";
    if [ "$?" -ne "0" ]; then
        echo -n -e "\r BiliBili China Mainland Only:\t\t${Font_Red}Failed (Parse Json)${Font_Suffix}\n" && echo -e " BiliBili China Mainland Only:\t\tFailed (Parse Json)" >> ${LOG_FILE};
        return;
    fi
    
    case ${result} in
        0)
            echo -n -e "\r BiliBili China Mainland Only:\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " BiliBili China Mainland Only:\t\tYes" >> ${LOG_FILE};
        ;;
        -10403)
            echo -n -e "\r BiliBili China Mainland Only:\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " BiliBili China Mainland Only:\t\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r BiliBili China Mainland Only:\t\t${Font_Red}Failed${Font_Suffix} ${Font_SkyBlue}(${result})${Font_Suffix}\n" && echo -e " BiliBili China Mainland Only:\t\tFailed (${result})" >> ${LOG_FILE};
        ;;
    esac
}

# 流媒体解锁测试-哔哩哔哩港澳台限定
function MediaUnlockTest_BilibiliHKMCTW() {
    echo -n -e " BiliBili Hongkong/Macau/Taiwan:\t->\c";
    local randsession="$(cat /dev/urandom | head -n 32 | md5sum | head -c 32)";
    # 尝试获取成功的结果
    local result=`curl --user-agent "${UA_Browser}" -${1} -fsSL --max-time 30 "https://api.bilibili.com/pgc/player/web/playurl?avid=18281381&cid=29892777&qn=0&type=&otype=json&ep_id=183799&fourk=1&fnver=0&fnval=16&session=${randsession}&module=bangumi" 2>&1`;
    if [[ "$result" == "curl"* ]]; then
        echo -n -e "\r BiliBili Hongkong/Macau/Taiwan:\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " BiliBili Hongkong/Macau/Taiwan:\tFailed (Network Connection)" >> ${LOG_FILE};
        return
    fi
    
    local result="$(PharseJSON "${result}" "code")";
    if [ "$?" -ne "0" ]; then
        echo -n -e "\r BiliBili Hongkong/Macau/Taiwan:\t${Font_Red}Failed (Parse Json)${Font_Suffix}\n" && echo -e " BiliBili Hongkong/Macau/Taiwan:\tFailed (Parse Json)" >> ${LOG_FILE};
        return;
    fi
    case ${result} in
        0)
            echo -n -e "\r BiliBili Hongkong/Macau/Taiwan:\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " BiliBili Hongkong/Macau/Taiwan:\tYes" >> ${LOG_FILE};
        ;;
        -10403)
            echo -n -e "\r BiliBili Hongkong/Macau/Taiwan:\t${Font_Red}No${Font_Suffix}\n" && echo -e " BiliBili Hongkong/Macau/Taiwan:\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r BiliBili Hongkong/Macau/Taiwan:\t${Font_Red}Failed${Font_Suffix} ${Font_SkyBlue}(${result})${Font_Suffix}\n" && echo -e " BiliBili Hongkong/Macau/Taiwan:\tFailed (${result})" >> ${LOG_FILE};
        ;;
    esac
}

# 流媒体解锁测试-哔哩哔哩台湾限定
function MediaUnlockTest_BilibiliTW() {
    echo -n -e " Bilibili Taiwan Only:\t\t\t->\c";
    local randsession="$(cat /dev/urandom | head -n 32 | md5sum | head -c 32)";
    # 尝试获取成功的结果
    local result=`curl --user-agent "${UA_Browser}" -${1} -fsSL --max-time 30 "https://api.bilibili.com/pgc/player/web/playurl?avid=50762638&cid=100279344&qn=0&type=&otype=json&ep_id=268176&fourk=1&fnver=0&fnval=16&session=${randsession}&module=bangumi" 2>&1`;
    if [[ "$result" == "curl"* ]]; then
        echo -n -e "\r Bilibili Taiwan Only:\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Bilibili Taiwan Only:Failed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result="$(PharseJSON "${result}" "code")";
    if [ "$?" -ne "0" ]; then
        echo -n -e "\r Bilibili Taiwan Only:\t\t\t${Font_Red}Failed (Parse Json)${Font_Suffix}\n" && echo -e " Bilibili Taiwan Only:Failed (Parse Json)" >> ${LOG_FILE};
        return;
    fi
    
    case ${result} in
        0)
            echo -n -e "\r Bilibili Taiwan Only:\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Bilibili Taiwan Only:\t\t\tYes" >> ${LOG_FILE};
        ;;
        -10403)
            echo -n -e "\r Bilibili Taiwan Only:\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Bilibili Taiwan Only:\t\t\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r Bilibili Taiwan Only:\t\t\t${Font_Red}Failed (${result})${Font_Suffix}\n" && echo " Bilibili Taiwan Only:Failed (${result})" >> ${LOG_FILE};
        ;;
    esac
}

# 流媒体解锁测试-Abema.TV
#
function MediaUnlockTest_AbemaTV_IPTest() {
    echo -n -e " Abema.TV:\t\t\t\t->\c";
    #
    local result=`curl --user-agent "${UA_Dalvik}" -${1} -fsL --write-out %{http_code} --max-time 30 "https://api.abema.io/v1/ip/check?device=android" 2>&1`;
    if [[ "${result}" == "000" ]]; then
        echo -n -e "\r Abema.TV:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Abema.TV:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result=`curl --user-agent "${UA_Dalvik}" -${1} -fsL --max-time 30 "https://api.abema.io/v1/ip/check?device=android" 2>&1`;
    if [ ! -n "$result" ]; then
        echo -n -e "\r Abema.TV:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Abema.TV:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi

    local result=$(PharseJSON "${result}" "isoCountryCode");
    if [[ "${result}" == "JP" ]];then
        echo -n -e "\r Abema.TV:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Abema.TV:\t\t\t\tYes" >> ${LOG_FILE};
        return;
    fi
    echo -n -e "\r Abema.TV:\t\t\t\t${Font_Yellow}Oversea Only${Font_Suffix}\n" && echo -e " Abema.TV:\t\t\t\tOversea Only" >> ${LOG_FILE};
}

function MediaUnlockTest_PCRJP() {
    echo -n -e " Princess Connect Re:Dive Japan:\t->\c";
    local result=`curl --user-agent "${UA_Dalvik}" -${1} -fsL --write-out %{http_code} --output /dev/null --max-time 30 https://api-priconne-redive.cygames.jp/ 2>&1`;
    case $result in
        000)
            echo -n -e "\r Princess Connect Re:Dive Japan:\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Princess Connect Re:Dive Japan:\tFailed (Network Connection)" >> ${LOG_FILE};
        ;;
        404)
            echo -n -e "\r Princess Connect Re:Dive Japan:\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Princess Connect Re:Dive Japan:\tYes" >> ${LOG_FILE};
        ;;
        403)
            echo -n -e "\r Princess Connect Re:Dive Japan:\t${Font_Red}No${Font_Suffix}\n" && echo -e " Princess Connect Re:Dive Japan:\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r Princess Connect Re:Dive Japan:\t${Font_Red}Failed (Unexpected Result: $result)${Font_Suffix}\n" && echo -e " Princess Connect Re:Dive Japan:\tFailed (Unexpected Result: $result)" >> ${LOG_FILE};
        ;;
    esac
}

function MediaUnlockTest_UMAJP() {
    echo -n -e " Pretty Derby Japan:\t\t\t->\c";
    local result=`curl --user-agent "${UA_Dalvik}" -${1} -fsL --write-out %{http_code} --output /dev/null --max-time 30 https://api-umamusume.cygames.jp/`;
    case ${result} in
        000)
            echo -n -e "\r Pretty Derby Japan:\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Pretty Derby Japan:\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        ;;
        404)
            echo -n -e "\r Pretty Derby Japan:\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Pretty Derby Japan:\t\t\tYes" >> ${LOG_FILE};
        ;;
        403)
            echo -n -e "\r Pretty Derby Japan:\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Pretty Derby Japan:\t\t\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r Pretty Derby Japan:\t\t\t${Font_Red}Failed (Unexpected Result: $result)${Font_Suffix}\n" && echo -e " Pretty Derby Japan:\t\t\tFailed (Unexpected Result: $result)" >> ${LOG_FILE};
        ;;
    esac
}

function MediaUnlockTest_Kancolle() {
    echo -n -e " Kancolle Japan:\t\t\t->\c";
    local result=`curl --user-agent "${UA_Dalvik}" -${1} -fsL --write-out %{http_code} --output /dev/null --max-time 30 http://203.104.209.7/kcscontents/ 2>&1`;
    case ${result} in
        000)
            echo -n -e "\r Kancolle Japan:\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Kancolle Japan:\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        ;;
        200)
            echo -n -e "\r Kancolle Japan:\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Kancolle Japan:\t\t\tYes" >> ${LOG_FILE};
        ;;
        403)
            echo -n -e "\r Kancolle Japan:\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Kancolle Japan:\t\t\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r Kancolle Japan:\t\t\t${Font_Red}Failed (Unexpected Result: $result)${Font_Suffix}\n" && echo -e " Kancolle Japan:\t\t\tFailed (Unexpected Result: $result)" >> ${LOG_FILE};
        ;;
    esac
}

function MediaUnlockTest_BBC() {
    echo -n -e " BBC:\t\t\t\t\t->\c";
    local result=`curl --user-agent "${UA_Browser}" -${1} -fsL --write-out %{http_code} --output /dev/null --max-time 30 http://ve-dash-uk.live.cf.md.bbci.co.uk/`;
    if [ "${result}" = "000" ]; then
        echo -n -e "\r BBC:\t\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " BBC:\t\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        elif [ "${result}" = "403" ]; then
        echo -n -e "\r BBC:\t\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " BBC:\t\t\t\t\tNo" >> ${LOG_FILE};
        elif [ "${result}" = "404" ]; then
        echo -n -e "\r BBC:\t\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " BBC:\t\t\t\t\tYes" >> ${LOG_FILE};
    else
        echo -n -e "\r BBC:\t\t\t\t\t${Font_Red}Failed (Unexpected Result: $result)${Font_Suffix}\n" && echo -e " BBC:\t\t\t\t\tFailed (Unexpected Result: $result)" >> ${LOG_FILE};
    fi
}

function MediaUnlockTest_Netflix() {
    echo -n -e " Netflix:\t\t\t\t->\c";
    local result=`curl -${1} --user-agent "${UA_Browser}" -sSL "https://www.netflix.com/" 2>&1`;
    if [ "$result" == "Not Available" ];then
        echo -n -e "\r Netflix:\t\t\t\t${Font_Red}Unsupport${Font_Suffix}\n" && echo -e " Netflix:\t\t\t\tUnsupport" >> ${LOG_FILE};
        return;
    fi
    
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r Netflix:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Netflix:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result=`curl -${1} --user-agent "${UA_Browser}" -sL "https://www.netflix.com/title/80018499" 2>&1`;
    if [[ "$result" == *"page-404"* ]] || [[ "$result" == *"NSEZ-403"* ]];then
        echo -n -e "\r Netflix:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Netflix:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi
    
    local result1=`curl -${1} --user-agent "${UA_Browser}" -sL "https://www.netflix.com/title/70143836" 2>&1`;
    local result2=`curl -${1} --user-agent "${UA_Browser}" -sL "https://www.netflix.com/title/80027042" 2>&1`;
    local result3=`curl -${1} --user-agent "${UA_Browser}" -sL "https://www.netflix.com/title/70140425" 2>&1`;
    local result4=`curl -${1} --user-agent "${UA_Browser}" -sL "https://www.netflix.com/title/70283261" 2>&1`;
    local result5=`curl -${1} --user-agent "${UA_Browser}"-sL "https://www.netflix.com/title/70143860" 2>&1`;
    local result6=`curl -${1} --user-agent "${UA_Browser}" -sL "https://www.netflix.com/title/70202589" 2>&1`;
    
    if [[ "$result1" == *"page-404"* ]] && [[ "$result2" == *"page-404"* ]] && [[ "$result3" == *"page-404"* ]] && [[ "$result4" == *"page-404"* ]] && [[ "$result5" == *"page-404"* ]] && [[ "$result6" == *"page-404"* ]];then
        echo -n -e "\r Netflix:\t\t\t\t${Font_Yellow}Only Homemade${Font_Suffix}\n" && echo -e " Netflix:\t\t\t\tOnly Homemade" >> ${LOG_FILE};
        return;
    fi
    
    local region=`tr [:lower:] [:upper:] <<< $(curl -${1} --user-agent "${UA_Browser}" -fs --write-out %{redirect_url} --output /dev/null "https://www.netflix.com/title/80018499" | cut -d '/' -f4 | cut -d '-' -f1)` ;
    
    if [[ ! -n "$region" ]];then
        region="US";
    fi
    echo -n -e "\r Netflix:\t\t\t\t${Font_Green}Yes(Region: ${region})${Font_Suffix}\n" && echo -e " Netflix:\t\t\t\tYes(Region: ${region})" >> ${LOG_FILE};
    return;
}

function MediaUnlockTest_YouTube_Region() {
    echo -n -e " YouTube Region:\t\t\t->\c";
    local result=`curl --user-agent "${UA_Browser}" -${1} -sSL "https://www.youtube.com/" 2>&1`;
    
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r YouTube Region:\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " YouTube Region:\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result=`curl --user-agent "${UA_Browser}" -${1} -sL "https://www.youtube.com/red" | sed 's/,/\n/g' | grep "countryCode" | cut -d '"' -f4`;
    if [ -n "$result" ]; then
        echo -n -e "\r YouTube Region:\t\t\t${Font_Green}${result}${Font_Suffix}\n" && echo -e " YouTube Region:\t\t\t${result}" >> ${LOG_FILE};
        return;
    fi
    
    echo -n -e "\r YouTube Region:\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " YouTube Region:\t\t\tNo" >> ${LOG_FILE};
    return;
}

function MediaUnlockTest_DisneyPlus() {
    echo -n -e " DisneyPlus:\t\t\t\t->\c";
    local result=`curl -${1} --user-agent "${UA_Browser}" -sSL "https://global.edge.bamgrid.com/token" 2>&1`;
    
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local previewcheck=`curl -sSL -o /dev/null -L --max-time 30 -w '%{url_effective}\n' "https://disneyplus.com" 2>&1`;
    if [[ "${previewcheck}" == "curl"* ]];then
        echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    if [[ "${previewcheck}" == *"preview"* ]];then
        echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi
    
    local result=`curl -${1} --user-agent "${UA_Browser}" -fs --write-out '%{redirect_url}\n' --output /dev/null "https://www.disneyplus.com" 2>&1`;
    if [[ "${website}" == "https://disneyplus.disney.co.jp/" ]];then
        echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Green}Yes(Region: JP)${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tYes(Region: JP)" >> ${LOG_FILE};
        return;
    fi
    
    local result=`curl -${1} -sSL --user-agent "$UA_Browser" -H "Content-Type: application/x-www-form-urlencoded" -H "${DisneyHeader}" -d "${DisneyAuth}" -X POST  "https://global.edge.bamgrid.com/token" 2>&1`;
    PharseJSON "${result}" "access_token" 2>&1 > /dev/null;
    if [[ "$?" -eq 0 ]]; then
        local region=$(curl -${1} -sSL https://www.disneyplus.com | grep 'region: ' | awk '{print $2}')
        if [ -n "$region" ];then
            echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Green}Yes(Region: $region)${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tYes(Region: $region)" >> ${LOG_FILE};
            return;
        fi
        echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi
    echo -n -e "\r DisneyPlus:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " DisneyPlus:\t\t\t\tNo" >> ${LOG_FILE};
}

function MediaUnlockTest_Dazn() {
    echo -n -e " Dazn:\t\t\t\t\t->\c";
    local result=`curl -${1} -sSL --max-time 30 -X POST -H "Content-Type: application/json" -d '{"LandingPageKey":"generic","Languages":"zh-CN,zh,en","Platform":"web","PlatformAttributes":{},"Manufacturer":"","PromoCode":"","Version":"2"}' "https://startup.core.indazn.com/misl/v5/Startup" 2>&1`;
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r Dazn:\t\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Dazn:\t\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi

    local region=`tr [:lower:] [:upper:] <<<$(PharseJSON "${result}" "Region.GeolocatedCountry")`;
    if [ ! -n "${result}" ]; then
        echo -n -e "\r Dazn:\t\t\t\t\t${Font_Red}Unsupport${Font_Suffix}\n" && echo -e " Dazn:\t\t\t\t\tUnsupport" >> ${LOG_FILE};
        return;
    fi

    if [[ "${region}" == "NULL" ]];then
        echo -n -e "\r Dazn:\t\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Dazn:\t\t\t\t\tNo" >> ${LOG_FILE}
        return;
    fi
    echo -n -e "\r Dazn:\t\t\t\t\t${Font_Green}Yes(Region: ${region})${Font_Suffix}\n" && echo -e " Dazn:\t\t\t\t\tYes(Region: ${region})" >> ${LOG_FILE}
}

function MediaUnlockTest_HuluJP() {
    echo -n -e " Hulu Japan:\t\t\t\t->\c";
    local result=`curl -${1} -sSL -o /dev/null --max-time 30 -w '%{url_effective}\n' "https://id.hulu.jp" 2>&1`;
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r Hulu Japan:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Hulu Japan:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    if [[ "$result" == *"login"* ]];then
        echo -n -e "\r Hulu Japan:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Hulu Japan:\t\t\t\tYes" >> ${LOG_FILE};
        return;
    fi
    echo -n -e "\r Hulu Japan:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Hulu Japan:\t\t\t\tNo" >> ${LOG_FILE};
}

function MediaUnlockTest_MyTVSuper() {
    echo -n -e " MyTVSuper:\t\t\t\t->\c";
    local result=`curl -sSL -${1} --max-time 30 "https://www.mytvsuper.com/iptest.php" 2>&1`;
    
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r MyTVSuper:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " MyTVSuper:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    if [[ "$result" == *"HK"* ]];then
        echo -n -e "\r MyTVSuper:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " MyTVSuper:\t\t\t\tYes" >> ${LOG_FILE};
        return;
    fi
    echo -n -e "\r MyTVSuper:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " MyTVSuper:\t\t\t\tNo" >> ${LOG_FILE};
}

function MediaUnlockTest_NowE() {
    echo -n -e " Now E:\t\t\t\t\t->\c";
    local result=`curl -${1} -sSLk --max-time 30 -X POST -H "Content-Type: application/json" -d '{"contentId":"202105121370235","contentType":"Vod","pin":"","deviceId":"W-60b8d30a-9294-d251-617b-c12f9d0c","deviceType":"WEB"}' "https://webtvapi.nowe.com/16/1/getVodURL" 2>&1`;
    if [[ "${result}" == "curl"* ]];then
        echo -n -e "\r Now E:\t\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Now E:\t\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result=$(PharseJSON "${result}" "responseCode");
    case ${result} in
        SUCCESS)
            echo -n -e "\r Now E:\t\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Now E:\t\t\t\t\tYes" >> ${LOG_FILE};
        ;;
        GEO_CHECK_FAIL)
            echo -n -e "\r Now E:\t\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Now E:\t\t\t\t\tNo" >> ${LOG_FILE};
        ;;
        *)
            echo -n -e "\r Now E:\t\t\t\t\t${Font_Red}Failed (Unexpected Result: $result)${Font_Suffix}\n" && echo -e " Now E:\t\t\t\t\tFailed (Unexpected Result: $result)" >> ${LOG_FILE};
        ;;
    esac
}

function MediaUnlockTest_ViuTV() {
    echo -n -e " Viu TV:\t\t\t\t->\c";
    local result=`curl -${1} -sSLk --max-time 30 -X POST -H "Content-Type: application/json" -d '{"callerReferenceNo":"20210603233037","productId":"202009041154906","contentId":"202009041154906","contentType":"Vod","mode":"prod","PIN":"password","cookie":"3c2c4eafe3b0d644b8","deviceId":"U5f1bf2bd8ff2ee000","deviceType":"ANDROID_WEB","format":"HLS"}' "https://api.viu.now.com/p8/3/getVodURL" 2>&1`;
    if [[ "${result}" == "curl"* ]];then
        echo -n -e "\r Viu TV:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Viu TV:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result=$(PharseJSON "${result}" "responseCode");
    if [[ "$result" == "SUCCESS" ]]; then
        echo -n -e "\r Viu TV:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Viu TV:\t\t\t\tYes" >> ${LOG_FILE};
        return
    fi
    
    if [[ "$result" == "GEO_CHECK_FAIL" ]]; then
        echo -n -e "\r Viu TV:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Viu TV:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi
    
    echo -n -e "\r Viu.TV:\t\t\t\t${Font_Red}Failed (Unexpected Result: $result)${Font_Suffix}\n" && echo -e " Viu TV:\t\t\t\tFailed (Unexpected Result: $result)" >> ${LOG_FILE};
}

function MediaUnlockTest_UNext() {
    echo -n -e " U Next:\t\t\t\t->\c";
    local result=`curl -${1} -sSL --max-time 30 "https://video-api.unext.jp/api/1/player?entity%5B%5D=playlist_url&episode_code=ED00148814&title_code=SID0028118&keyonly_flg=0&play_mode=caption&bitrate_low=1500" 2>&1`;
    if [[ "${result}" == "curl"* ]];then
        echo -n -e "\r U Next:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " U Next:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    local result=$(PharseJSON "${result}" "data.entities_data.playlist_url.result_status");
    if [[ "${result}" == "475" || "${result}" == "200" ]]; then
        echo -n -e "\r U Next:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " U Next:\t\t\t\tYes" >> ${LOG_FILE};
        return;
    fi
    
    if [[ "${result}" == "467" ]]; then
        echo -n -e "\r U Next:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " U Next:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi
    echo -n -e "\r U Next:\t\t\t\t${Font_Red}Failed (Unexpected Result: ${result})${Font_Suffix}\n" && echo -e " U Next:\t\t\t\tFailed (Unexpected Result: ${result})" >> ${LOG_FILE};
}

function MediaUnlockTest_Paravi() {
    echo -n -e " Paravi:\t\t\t\t->\c";
    local result=`curl -${1} -sSL --max-time 30 -H "Content-Type: application/json" -d '{"meta_id":71885,"vuid":"3b64a775a4e38d90cc43ea4c7214702b","device_code":1,"app_id":1}' "https://api.paravi.jp/api/v1/playback/auth" 2>&1`;
    if [[ "$result" == "curl"* ]];then
        echo -n -e "\r Paravi:\t\t\t\t${Font_Red}Failed (Network Connection)${Font_Suffix}\n" && echo -e " Paravi:\t\t\t\tFailed (Network Connection)" >> ${LOG_FILE};
        return;
    fi
    
    if [[ "$(PharseJSON "${result}" "error.code" | awk '{print $2}' | cut -d ',' -f1)" == "2055" ]]; then
        echo -n -e "\r Paravi:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Paravi:\t\t\t\tNo" >> ${LOG_FILE};
        return;
    fi
    
    local result=$(PharseJSON "${result}" "playback_validity_end_at");
    if [[ "${result}" != "null" ]]; then
        echo -n -e "\r Paravi:\t\t\t\t${Font_Green}Yes${Font_Suffix}\n" && echo -e " Paravi:\t\t\t\tYes" >> ${LOG_FILE};
        return;
    fi
    echo -n -e "\r Paravi:\t\t\t\t${Font_Red}No${Font_Suffix}\n" && echo -e " Paravi:\t\t\t\tNo" >> ${LOG_FILE};
}

function ISP(){
    local result=`curl -sSL -${1} "https://api.ip.sb/geoip" 2>&1`;
    if [[ "$result" == "curl"* ]];then
        return
    fi
    local ip=$(PharseJSON "${result}" "ip" 2>&1)
    local isp="$(PharseJSON "${result}" "isp" 2>&1) [$(PharseJSON "${result}" "country" 2>&1) $(PharseJSON "${result}" "city" 2>&1)]";
    if [ $? -eq 0 ];then
        echo " ** IP: ${ip}"
        echo " ** ISP: ${isp}" && echo " ** ISP: ${isp}" >> ${LOG_FILE};
    fi
}

function MediaUnlockTest() {
    ISP ${1};
    MediaUnlockTest_HBONow ${1};
    MediaUnlockTest_BBC ${1};
    
    MediaUnlockTest_MyTVSuper ${1};
    MediaUnlockTest_NowE ${1};
    MediaUnlockTest_ViuTV ${1};
    MediaUnlockTest_BahamutAnime ${1};
    MediaUnlockTest_BilibiliChinaMainland ${1};
    MediaUnlockTest_BilibiliHKMCTW ${1};
    MediaUnlockTest_BilibiliTW ${1};
    
    MediaUnlockTest_AbemaTV_IPTest ${1};
    MediaUnlockTest_Paravi ${1};
    MediaUnlockTest_UNext ${1};
    MediaUnlockTest_HuluJP ${1};
    MediaUnlockTest_PCRJP ${1};
    MediaUnlockTest_UMAJP ${1};
    MediaUnlockTest_Kancolle ${1};
    
    MediaUnlockTest_Dazn ${1};
    MediaUnlockTest_Netflix ${1};
    MediaUnlockTest_YouTube_Region ${1};
    MediaUnlockTest_DisneyPlus ${1};
    GameTest_Steam ${1};
}

curl -V > /dev/null 2>&1;
if [ $? -ne 0 ];then
    echo -e "${Font_Red}Please install curl${Font_Suffix}";
    exit;
fi

jq -V > /dev/null 2>&1;
if [ $? -ne 0 ];then
    InstallJQ;
fi
echo " ** 正在测试IPv4解锁情况" && echo " ** 正在测试IPv4解锁情况" >> ${LOG_FILE};
check4=`ping 1.1.1.1 -c 1 2>&1`;
if [[ "$check4" != *"unreachable"* ]] && [[ "$check4" != *"Unreachable"* ]];then
    MediaUnlockTest 4;
else
    echo -e "${Font_SkyBlue}当前主机不支持IPv4,跳过...${Font_Suffix}" && echo "当前主机不支持IPv4,跳过..." >> ${LOG_FILE};
fi

echo " ** 正在测试IPv6解锁情况" && echo " ** 正在测试IPv6解锁情况" >> ${LOG_FILE};
check6=`ping6 240c::6666 -c 1 2>&1`;
if [[ "$check6" != *"unreachable"* ]] && [[ "$check6" != *"Unreachable"* ]];then
    MediaUnlockTest 6;
else
    echo -e "${Font_SkyBlue}当前主机不支持IPv6,跳过...${Font_Suffix}" && echo "当前主机不支持IPv6,跳过..." >> ${LOG_FILE};
fi
echo -e "";
echo -e "${Font_Green}本次测试结果已保存到 ${LOG_FILE} ${Font_Suffix}";
cat ${LOG_FILE} | PasteBin_Upload;

```





# YY

```
https://github.com/tgbot-collection/YYeTsBot
https://github.com/ffffffff0x/Dork-Admin  # hack
https://github.com/hudunkey/Red-Team-links # hack
```



