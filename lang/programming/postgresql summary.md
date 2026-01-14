## Install PG

```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目
```



```
# alma linux 8
# https://www.postgresql.org/download/linux/redhat/
cat /etc/os-release && \
dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
dnf -qy module disable postgresql && \
dnf -y install postgresql13 postgresql13-server

systemctl restart postgresql-13

vi /etc/environment
LANG=en_US.utf-8
LC_ALL=en_US.utf-8

vi /etc/environment
LANG=en_US.utf-8
LC_ALL=en_US.utf-8
	# 添加这两项 

source /etc/environment

export LANG="en_US.utf-8" && \
export LC_ALL="en_US.utf-8"

echo "LC_ALL=en_US.UTF-8" >> /etc/environment
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
locale-gen en_US.UTF-8
	# ubuntu only

dnf install glibc-all-langpacks
localectl set-locale LANG=en_US.utf-8
	localectl set-locale LANG=en_US.utf8@ampm
		# 成功
		
en_US.utf8
en_US.utf8@ampm

echo "export LC_ALL=en_US.utf8@ampm" >> /etc/profile

source /etc/profile

locale -a

/usr/pgsql-13/bin/postgresql-13-setup initdb && \
cat /var/lib/pgsql/13/initdb.log && \
cat /var/lib/pgsql/13/data/postgresql.conf




```



### AlmaLinux 9.3

```

cat /etc/redhat-release

AlmaLinux release 9.3 (Shamrock Pampas Cat)


# Install the repository RPM:
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Disable the built-in PostgreSQL module:
sudo dnf -qy module disable postgresql

# Install PostgreSQL:
sudo dnf install -y postgresql17-server

# Optionally initialize the database and enable automatic start:
sudo /usr/pgsql-17/bin/postgresql-17-setup initdb
sudo systemctl enable postgresql-17
sudo systemctl start postgresql-17


sudo -u postgres psql
select version();
\password postgres  # 修改密码
\q

postgres 	pt41
	# 用户名 密码

psql -h 127.0.0.1 -p 5432 -U postgres
	# 成功登录

mkdir /home/psqldata

chown -R postgres:postgres /home/psqldata



 systemctl stop postgresql-17

cp -R /var/lib/pgsql/17/data /home/psqldata   # 只能透亮换柱了

mv /var/lib/pgsql/17/data /var/lib/pgsql/17/data__link__to_home_psqldata

ln -s  /home/psqldata/data  /var/lib/pgsql/17/data
			# unlink 取消软链用这个

chown -R postgres:postgres /home/psqldata



systemctl start postgresql-17

systemctl status postgresql-17



# 允许运程连接
vi /var/lib/pgsql/17/data/postgresql.conf
	listen_addresses = '*' # 改成这个
vi /var/lib/pgsql/17/data/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  md5  
	# hostnossl    all          all            0.0.0.0/0  trust  # 任何密码都能连
	# 加在最后面，接受所有远程IP


systemctl restart postgresql-17
systemctl status postgresql-17



yum groupinstall "Development Tools" && \
yum install llvm-toolset-7-clang && \
yum install postgresql17-devel && \
yum install postgresql17-contrib && \
yum install systemtap-sdt-devel


git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-17/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install

make USE_PGXS=1 installcheck && \
psql DB -c "CREATE EXTENSION rum;"



CREATE TABLE IF NOT EXISTS test_vector (
    ID integer generated always as identity,
    AppID integer NOT NULL,
    TestID integer NOT NULL,
    ChildTableID integer NOT NULL,
    S_Test text NOT NULL,
    V_Test tsvector,
    Enabled boolean,
    UNIQUE(ID),  
    PRIMARY KEY (AppID, TestID, ChildTableID) 
);

CREATE INDEX idx_appid ON test_vector (AppID);



```



### Ubuntu 22.04

```

# see huggingface/NLPP_Audio/vector.py

proxychains4 apt install -y postgresql-common && 
proxychains4 (sleep 1; echo "\n";) | bash /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

proxychains4 (sleep 1; echo "Y";) | apt install curl ca-certificates &&
install -d /usr/share/postgresql-common/pgdg && 
curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc




sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

proxychains4 apt update && 
proxychains4 apt -y install postgresql-17 postgresql-server-dev-17 libpq-dev postgresql-contrib 



/etc/postgresql/17/main/pg_hba.conf

sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'post4321';"


sudo -u postgres psql
select version();
\password postgres  # 修改密码
\q

postgres 	pt41
	# 用户名 密码

psql -h 127.0.0.1 -p 5432 -U postgres
	# 成功登录


echo 'hostnossl    all          all            0.0.0.0/0  md5' >> /etc/postgresql/17/main/pg_hba.conf
	# >> 表示追加在最后

# 允许运程连接
vi /etc/postgresql/17/main/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  md5  
	# hostnossl    all          all            0.0.0.0/0  trust  # 任何密码都能连
	# 加在最后面，接受所有远程IP

#local   all             postgres                                peer
local   all             postgres                                password
	# 改成这样

see huggingface/NLPP_vector_server/Dockerfile
	# sed -i 's/\(local[[:space:]]\+all[[:space:]]\+postgres[[:space:]]\+\)peer/\1password/' /etc/postgresql/17/main/pg_hba.conf 
	# 能自动修改成功

PGPASSWORD=post4321 psql -U postgres  -c "SELECT pg_reload_conf()"
	# 能执行成功的前提是上一行改好了


pg_ctlcluster 17 main restart
pg_ctlcluster 17 main status
	# 成功重启
	# 但是在 docker 中不知道怎么运行它

systemctl restart postgresql


http://ｘｘ.ｘｘ.ｘｘ.57:7851/wsproxy/admin
	# ali57 添加远程端口  54322 转到　wsl2 5432




// https://github.com/pgvector/pgvector 先安装

proxychains4 apt install postgresql-17-pgvector
	# 安装向量插件

git clone https://github.com/postgrespro/rum && 
cd rum &&
make USE_PGXS=1 PG_CONFIG=/usr/bin/pg_config &&
make USE_PGXS=1 PG_CONFIG=/usr/bin/pg_config install
$ psql DB -c "CREATE EXTENSION rum;
	# 安装　RUM 插件


CREATE DATABASE nlppvector
WITH OWNER = postgres 
ENCODING = 'UTF8' 
TABLESPACE = pg_default 
CONNECTION LIMIT = -1 
TEMPLATE template0;

CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgroonga;
CREATE TABLE IF NOT EXISTS nlpp_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    JPMD5 CHAR(32) NOT NULL,
    name text NOT NULL,
    S_JP text NOT NULL,
    V_JP vector(1536) NOT NULL,
    S_CN text DEFAULT '' NOT NULL,
    S_EN text DEFAULT '' NOT NULL,
    metadata jsonb NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (JPMD5, name) 
);
CREATE INDEX IF NOT EXISTS index_pgvector_VJP ON nlpp_vector USING hnsw (V_JP vector_cosine_ops);
CREATE INDEX IF NOT EXISTS index_pgroonga_SJP ON nlpp_vector USING pgroonga (S_JP);



mkdir /home/psqldata

chown -R postgres:postgres /home/psqldata

```



```

# see huggingface/NLPP_Audio/vector.py

proxychains4 pip install --upgrade pip && 
proxychains4 pip install "psycopg[binary]"  


proxychains4 apt install postgresql-17-pgvector
	# 安装向量插件

git clone https://github.com/postgrespro/rum && 
cd rum &&
make USE_PGXS=1 PG_CONFIG=/usr/bin/pg_config &&
make USE_PGXS=1 PG_CONFIG=/usr/bin/pg_config install &&
make USE_PGXS=1 installcheck &&
$ psql DB -c "CREATE EXTENSION rum;
	# 安装  RUM 插件

# see https://pgroonga.github.io/install/ubuntu.html
proxychains4 apt install -y software-properties-common && 
proxychains4 add-apt-repository -y universe && 
proxychains4 add-apt-repository -y ppa:groonga/ppa &&
proxychains4 apt install -y wget lsb-release && 
proxychains4 wget https://packages.groonga.org/ubuntu/groonga-apt-source-latest-$(lsb_release --codename --short).deb && 
proxychains4 apt install -y -V ./groonga-apt-source-latest-$(lsb_release --codename --short).deb && 
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release --codename --short)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list && 
proxychains4 wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && 
proxychains4 apt update && 
proxychains4 apt install -y -V postgresql-17-pgdg-pgroonga && 
proxychains4 apt install -y -V groonga-tokenizer-mecab

CREATE EXTENSION pgroonga;
	# 成功

see https://pgroonga.github.io/tutorial/
    # 用法很详细

DROP DATABASE IF EXISTS nlppvector;
CREATE DATABASE nlppvector
WITH OWNER = postgres 
ENCODING = 'UTF8' 
TABLESPACE = pg_default 
CONNECTION LIMIT = -1 
TEMPLATE template0;
    # 整完 nvcat 重连一次，选这个库再运行下面的语句

# see https://github.com/pgvector/pgvector  各类型向量的长度说明
CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS nlpp_vector;
CREATE TABLE IF NOT EXISTS nlpp_vector (
    id bigint generated always as identity (START WITH 1 INCREMENT BY 1),
    guid uuid DEFAULT uuid_generate_v4(),
    name text NOT NULL,
    s_jp text NOT NULL,
    s_zh text NOT NULL,
    v_jp tsvector NOT NULL,
    v_zh tsvector NOT NULL,
    metadata jsonb NOT NULL,
    embed_jp vector(1024) NOT NULL,
    embed_zh vector(1024) NOT NULL,
    audio bytea DEFAULT NULL,
    image bytea DEFAULT NULL,
    addtime timestamp DEFAULT CURRENT_TIMESTAMP,
    updatetime timestamp DEFAULT NULL,
    enable boolean DEFAULT '1',
    UNIQUE(ID),
    PRIMARY KEY (GUID)
);
CREATE INDEX index_halfvec_embed_jp ON nlpp_vector USING hnsw (embed_jp vector_cosine_ops);
CREATE INDEX index_halfvec_embed_zh ON nlpp_vector USING hnsw (embed_zh vector_cosine_ops);
CREATE INDEX fts_rum_v_jp ON nlpp_vector USING rum (v_jp rum_tsvector_ops);
CREATE INDEX fts_rum_v_zh ON nlpp_vector USING rum (v_zh rum_tsvector_ops);
CREATE INDEX index_btree_name ON nlpp_vector (name);
CREATE INDEX index_btree_name_section ON nlpp_vector (name, (metadata->>'section'));
```





### 免安装配置

```
Postgresql免安装配置方法
一、下载
https://www.enterprisedb.com/download-postgresql-binaries
进入网址，选择适合自己系统的版本

二、下载好的zip包解压，并创建一个data文件用来存放数据

三、初始化数据库
命令行进入bin目录，执行以下代码：

cd D:\usr\postgresql-13\pgsql\bin
./initdb.exe -D E:\pgsqldata -E UTF-8 --locale=chs -U postgres -W

./pg_ctl -D E:\pgsqldata -l logfile start

注：
-D ：指定数据库簇的存储目录D:\tools\postgres\pgsql\data
-E ：指定DB的超级用户的用户名postgres
–locale：关于区域设置（chinese-simplified-china）
-U ：默认编码格式chs
-W ：为超级用户指定密码的提示
注：命令上的地址如果输入错误，再次执行可能提示不能给data文件夹权限，删除data重新创建即可

四、启动数据库

pg_ctl -D D:\tools\postgres\pgsql\data -l logfile start

五、注册成系统服务

pg_ctl register -N PostgreSQL -D D:\tools\postgres\pgsql\data
```



## supabase

https://supabase.com/docs/guides/self-hosting/docker#securing-your-services  配置重要的 key

https://console.cloud.tencent.com/lighthouse/instance

https://vonng.com/pigsty/v4.0/

https://pigsty.cc/docs/setup/install/

https://pigsty.cc/docs/app/supabase/

- ```
  Supabase 很好，拥有属于你自己的 supabase 则好上加好。 Pigsty 可以帮助您在自己的服务器上（物理机/虚拟机/云服务器），一键自建企业级 supabase —— 更多扩展，更好性能，更深入的控制，更合算的成本。
  
  推荐使用 RockyLinux 9.6、Debian 12.11 或 Ubuntu 24.04.5 作为默认操作系统选项
  
  
  
  ```





```

console.cloud.tencent.com
	# tencent 海外云控制台
	
https://lightsail.aws.amazon.com/
	# amazon 控制台

http://xx.xx.xx.xx:3000
	点进去 Dashboards -> PGSQL -> Database
		# 能看到现有数据库和已安装插件


bash -c 'version=$(lsb_release -cs) && cp /etc/apt/sources.list /etc/apt/sources.list.bak && cat << EOF > /etc/apt/sources.list
deb http://archive.ubuntu.com/ubuntu/ $version main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ $version-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ $version-backports main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu/ $version-security main restricted universe multiverse
EOF' \
  && apt update

	# tencent 海外云用 4G 内存


nmap 43.xxx.xxx.xx -p 8000
	# Supabase Studio 图形管理界面
		http://xx.xx.xx.xx:8000
		
	

apt install -y ansible python3-jmespath
	# ubuntu 
	dnf install -y ansible python3.12-jmespath python3-cryptography
		# EL 8/9 企业版
	# 好像不用，一键安装已经有了


localedef -i en_US -f UTF-8 en_US.UTF-8 \
  && localectl set-locale LANG=en_US.UTF-8
  # 强烈建议 使用全新安装的操作系统环境，并将 en_US 设置为主要语言
  

curl -fsSL https://repo.pigsty.io/get | bash; cd ~/pigsty  # 海外
curl -fsSL https://repo.pigsty.cc/get | bash; cd ~/pigsty  # 国内
./configure -c supabase    # 使用 supabase 配置（请在 pigsty.yml 中更改凭据）
vi pigsty.yml              # 编辑域名、密码、密钥...
	# 前面那命令运行完再改密码，因为会被覆盖
./deploy.yml              # 安装 pigsty
./docker.yml               # 安装 docker compose 组件
./app.yml                  # 使用 docker 启动 supabase 无状态部分（可能较慢）
vi pigsty.yml
	# 自已先手动设置密码！除非内网环境
	
	不用下面这个了
	./configure; ./install.yml; 
	# 生成配置文件，执行安装剧本！
		# 默认密码会在 configure -g 时自动被替换为随机强密码
			# 实测 -g 参数无效
			cat ~/pigsty/pigsty.yml | grep pg_admin_password

通过 http://<your_ip_address>:8000 访问到 Supabase Studio 图形管理界面了。 默认的用户名与密码分别是： supabase 与 pigsty。

需要使用的对象存储功能，那么需要通过域名与 HTTPS 访问 Supabase，否则会出现报错。


Supabase 部分的凭据修改后，您可以重启 Docker Compose 容器以应用新的配置：
./app.yml -t app_config,app_launch   # 使用剧本
cd /opt/supabase; make up            # 手工执行



dbuser_dba	DBUser.DBA	  超级用户	 数据库管理
dbuser_meta	DBUser.Meta	  业务管理员 应用读写
dbuser_view	DBUser.Viewer 只读用户	 数据查看
	# 默认数据库密码
	
    #----------------------------------------------#
    # PASSWORD : https://doc.pgsty.com/config/security
    #----------------------------------------------#
    grafana_admin_password: pigstyxX
    	# admin 是这个用户名 xx.xx.xx.xx:3000/login
    pg_admin_password: DBUser.DBAxX
    pg_monitor_password: DBUser.MonitorxX
    pg_replication_password: DBUser.ReplicatorxX
    patroni_password: Patroni.APIxX
    haproxy_admin_password: pigstyxX
    minio_secret_key: minioadminxX

              PGADMIN_DEFAULT_EMAIL: admin@pigsty.cc
              PGADMIN_DEFAULT_PASSWORD: pigstyxX


        # define business users/roles : https://doc.pgsty.com/pgsql/user
        pg_users:
          - { name: dbuser_meta ,password: DBUser.MetaxX   ,pgbouncer: true ,roles: [dbrole_admin   ] ,comment: pigsty admin user }
          - { name: dbuser_view ,password: DBUser.ViewerxX ,pgbouncer: true ,roles: [dbrole_readonly] ,comment: read-only viewer  }


nmap 10.7.0.9 -p 5432
	# 是不是这个是集群默认结点 ?
	# vi pigsty.yml 找到的


export PGPASSWORD='DBUser.DBAxX'
psql -h 10.7.0.9 -p 5432 -U dbuser_dba -d postgres
	# 连接成功
		psql 要退出安装 pigsty 的 shell 重进后才可见
		-d meta 会提示没有这个数据库
	\l	列出所有数据库				  
	\c dbname  切换到指定数据库

	\dx                            -- psql 元命令，列出已经安装的扩展
	TABLE pg_available_extensions; -- 查询已经安装，可以启用的扩展
	CREATE EXTENSION postgis;      --  启用 postgis 扩展


vi /etc/nginx/nginx.conf
stream {
    upstream pg_5432 {
        server 10.7.0.9:5432;
    }

    server {
        listen 54322;
        proxy_pass pg_5432;
    }
}
nginx -t
systemctl status nginx
nginx -s reload
	# 配置 nginx 转发
	# navicat 成功连上了
	


postgres://dbuser_dba:DBUser.DBA@10.7.0.9:5432/meta
postgres://dbuser_meta:DBUser.Meta@10.7.0.9:5432/meta
postgres://dbuser_view:DBUser.View@10.7.0.9:5432/meta
	# 使用三个不同的用户连接到 pg-meta 集群的 meta 数据库
	# https://pigsty.cc/docs/setup/pgsql/
		psql -h 10.7.0.9 -p 5432 -U dbuser_dba -d meta
			export PGPASSWORD='DBUser.DBA'
			psql -h 10.7.0.9 -p 5432 -U dbuser_dba -d meta




FATAL: no pg_hba.conf entry for host"xx.xx.xx.xx" user postgres database
	# 连 PG 数据库出错，应该是没有允许远程连接



Ctrl+C	中断查询				Ctrl+D	退出 psql
\?	显示所有元命令帮助			 \h	显示 SQL 命令帮助
\l	列出所有数据库				  \c dbname	切换到指定数据库
\d table	查看表结构		   \d+ table	查看表的详细信息
\du	列出所有用户/角色		     \dx	列出已安装的扩展
\dn	列出所有的模式				  \dt	列出所有表


-- 查看 PostgreSQL 版本
SELECT version();

-- 查看当前时间
SELECT now();

-- 创建一张测试表
CREATE TABLE test (id SERIAL PRIMARY KEY, name TEXT, created_at TIMESTAMPTZ DEFAULT now());

-- 插入数据
INSERT INTO test (name) VALUES ('hello'), ('world');

-- 查询数据
SELECT * FROM test;

-- 删除测试表
DROP TABLE test;



Restarting services...

Service restarts being deferred:
 systemctl restart networkd-dispatcher.service
 systemctl restart unattended-upgrades.service




 如果您只是希望尝尝鲜，不在乎安全，并且希望一切越简单越好，那么您可以仅对外部用户按需开放 5432 端口（ PostgreSQL 数据库） 与 3000 端口（Grafana 可视化界面）。


 

```





```
https://blog.csdn.net/techshrimp/article/details/154450227
	＃ 后端代码不用写了？前端操作数据库？一文精通Supabase，实战教程+本地部署


https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/user-guide/supabase/
	https://developer.aliyun.com/article/1674339?spm=a2c4g.11186623.0.0.36e373465XM2FV  
	＃ supabase 阿里云的版本  RDS 全托管 Supabase服务：小白轻松搞定开发AI应用！
	

https://vonng.com/pigsty/v3.1/   Pigsty v3.1：Supabase一键自建，PG17上位，ARM与Ubuntu24支持，MinIO改进
	Supabase 的口号是：“花个周末写写，随便扩容至百万”。在试用之后，我觉得此言不虚。 这是一个低代码的一站式后端平台，能让你几乎告别大部分后端开发的工作，只需要懂数据库设计与前端即可快速出活了！


https://www.ob-tutorial.org/blog/private-deploy-supabase-on-cloud-server  在云服务器上私有部署 Supabase 完整指南
	https://www.cnblogs.com/aopstudio/p/19134256  Supabase：无需后端代码的 Web 开发完整解决方案
	https://pigsty.cc/blog/db/supabase/  自建 Supabase：创业出海的首选数据库
	https://vonng.com/pigsty/v3.7/ Pigsty v3.7：PG万磁王，PG18深度支持
	https://www.ffeeii.com/supabase.html  阿里、腾讯、字节、n8n都选择了Supabase，可见Supabase的战略地位
		https://www.ffeeii.com/trae-solo-skill.html  Trae SOLO：3分钟解决Hugo博客3年Github兼容问题，SOLO太强了！
	https://www.zyzy.info/post/U2przPrt1a_n-y-AqeoUE  Supabase Edge Functions 本地开发与原理详解
	https://vonng.com/pg/just-use-pg/  技术极简主义：一切皆用Postgres
	hangge.com/blog/cache/detail_3408.html
		# supabase私有化部署


https://zhuanlan.zhihu.com/p/1969746342847948293
	https://github.com/kuafuai/aipexbase
	https://blog.vonng.com/cloud/aliyun-supabase  阿里云“借鉴”Supabase：开源与云的灰色地带
			# https://blog.vonng.com/pg/ai-db-king  PG将主宰AI时代的数据库
			# https://blog.vonng.com/db/google-mcp/
				https://github.com/googleapis/genai-toolbox
					https://github.com/gemini-cli-extensions/postgres
			# https://www.zyzy.info/post/50ef5896-3b82-4bd2-b278-34deb7fc6170  从零开始构建私人MCP服务器：让AI助手直接创建博客文章
			# https://blog.vonng.com/db/pg-kiss-duckdb/  数据库火星撞地球：当PG爱上DuckDB
		# Supabase 卡脖子？这个国产开源项目让 AI Coding 真正闭环了

		await supabase.from(“users”).select(‘*’).eq(“id”, userId).single()
		await pool.query(‘SELECT * FROM users WHERE id = $1 LIMIT 1’, [userId])

	我个人非常喜欢这些 BaaS 项目，并且都试过了（Supabase, Pocketbase, Appwrite 等）。每个都有优点和缺点

	我推荐自托管Appwrite（MariaDB）。它是最相似的替代方案，并且拥有类似于Supabase边缘函数的自托管函数，而且支持你喜欢的编程语言。
```



### Trae 代理连远程主机

```

Host tencent_tokyo
  HostName xx.xx.xx.xx
  Port 22
  User root
  ProxyCommand "C:\Program Files\Git\mingw64\bin\connect.exe" -H 172.22.112.93:7890 %h %p

```



### 源码构建

https://github.com/orgs/supabase/discussions/33178

- https://blog.csdn.net/m0_52537869/article/details/153853387 Supabase 自部署完整指南
- https://github.com/supabase-community/supabase-mcp  

```

git clone --depth 1 https://github.com/supabase/supabase \
  && cd supabase/docker \
  && snap install docker \
  && cp .env.example .env \
  && docker compose pull




```



```

卡在supabase-selfhost好几个星期了。

总算运行起来了（公司YouTube故意不显示终端命令行，这帮家伙藏得挺巧）。多亏 chatgpt 帮我生成了命令行，谢天谢地，终于成功了。

访问了自托管Supabase的管理区域（Digital Ocean EC2实例）。

然后你猜怎么着——好多功能都缺失，连查询/函数都改不了名，也删不掉（Supabase不是有这个功能吗？）

最基本的API获取完全没法用。一直超时，根本没地方调试。

长话短说：Supabase自称开源，但他们开源的是个半成品项目，目的就是为了让你用他们的付费Supabase平台。

别浪费时间了，换家公司吧。Supabase只在乎钱。




Supabase 是开源的，但它的 Edge Functions 管理后台（FaaS Backend）并未开源。这意味着：

您可以在本地使用 supabase start 运行边缘函数（模拟环境）；

也可以部署一个包含 edge-runtime 的容器；

但您无法通过 Studio 创建、编辑或部署函数；

也无法通过 CLI 将代码推送到自建实例；

许多企业在尝试自建 Supabase 时，发现 Edge Functions 功能“不可用”或“只能靠手动脚本部署”，最终放弃使用这一核心能力。



```





### 安装前提

```

安装前提：
  具有免密 ssh 和 sudo 权限的 管理用户

要求：ssh root@127.0.0.1  这个命令能登录本机


apt update && sudo apt install openssh-server -y

vi /etc/ssh/sshd_config
PermitRootLogin yes
PasswordAuthentication yes

systemctl restart ssh \
  && systemctl status ssh


ssh root@127.0.0.1
	# 现在应该能不要密码登录了

```



### ubuntu24.04 换源

```

cp /etc/apt/sources.list.d/ubuntu.sources /etc/apt/sources.list.d/ubuntu.sources.bak  \
  && vi  /etc/apt/sources.list.d/ubuntu.sources

# 阿里云镜像源配置示例
Types: deb
URIs: https://mirrors.aliyun.com/ubuntu/
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: https://mirrors.aliyun.com/ubuntu/
Suites: noble-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

curl -fsSL https://repo.pigsty.cc/get | bash; cd ~/pigsty  # 国内
./configure -c supabase    # 使用 supabase 配置（请在 pigsty.yml 中更改凭据）
vi pigsty.yml              # 编辑域名、密码、密钥...
./install.yml              # 安装 pigsty
./docker.yml               # 安装 docker compose 组件
./app.yml                   # 使用 docker 启动 supabase 无状态部分（可能较慢）
vi pigsty.yml
	# 自已先手动设置密码！除非内网环境

# IMPORTANT: CHANGE JWT_SECRET AND REGENERATE CREDENTIAL ACCORDING!!!!!!!!!!!
              # https://supabase.com/docs/guides/self-hosting/docker#securing-your-services

Generate and configure API keys#

JWT_SECRET: Used by PostgREST and GoTrue to sign and verify JWTs.
9wvi0AlFWkvZKsdBsUxcMHbAlRk04SsIWbUcDClx

ANON_KEY: Client-side API key with limited permissions (anon role). Use this in your frontend applications.
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3NzE1MjAwLCJleHAiOjE5MjU0ODE2MDB9.nJblK0q4I3djqRSk0qwkr3XKwVplqO-lqk6MIeww7DM

SERVICE_ROLE_KEY: Server-side API key with full database access (service_role role). Never expose this in client code.
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaXNzIjoic3VwYWJhc2UiLCJpYXQiOjE3Njc3MTUyMDAsImV4cCI6MTkyNTQ4MTYwMH0.dzJyYBEJhWIm2h6SgK7gfYhE8PkJDGqxi3kiUC5AAPU


# postgres connection string (use the correct ip and port)
              POSTGRES_HOST: 192.168.1.7      # point to the local postgres node
              POSTGRES_PORT: 5436             # access via the 'default' service, which always route to the primary postgres
              POSTGRES_DB: postgres           # the supabase underlying database
              POSTGRES_PASSWORD: DBUser.SupaxX  # password for supabase_admin and multiple supabase users
这个是 supabaser 专用的 db 连接方法


安装前提：
  具有免密 ssh 和 sudo 权限的 管理用户

要求：ssh root@127.0.0.1  这个命令能登录本机


apt update && sudo apt install openssh-server -y

vi /etc/ssh/sshd_config
PermitRootLogin yes
PasswordAuthentication yes

systemctl restart ssh \
  && systemctl status ssh



```



### 配置修改

```

vi /root/pigsty/roles/minio/tasks/config.yml
	line 72
	      loop:
        - { src: "{{ playbook_dir }}/files/pki/ca/ca.crt"                       ,dest: "/home/{{ minio_user }}/.minio/certs/CAs/ca.crt"  ,owner: "{{ minio_user }}", group: "minio" ,mode: "0644" }
        - { src: "{{ playbook_dir }}/files/pki/minio/{{ minio_instance }}.crt"  ,dest: "/home/{{ minio_user }}/.minio/certs/public.crt"  ,owner: "{{ minio_user }}", group: "minio" ,mode: "0644" }
        - { src: "{{ playbook_dir }}/files/pki/minio/{{ minio_instance }}.key"  ,dest: "/home/{{ minio_user }}/.minio/certs/private.key" ,owner: "{{ minio_user }}", group: "minio" ,mode: "0600" }
	# 这三行改成这样



$ hostname -I
10.7.0.9 172.17.0.1 172.18.0.1 192.168.122.1 192.168.121.1 10.10.10.1 

(TraeAI-4) /opt/supabase [0] $ ss -tuln | grep 5436
tcp   LISTEN 0      4096          0.0.0.0:5436       0.0.0.0:* 


vi /root/pigsty/pigsty.yml

        app: supabase                                     # specify app name (supa) to be installed (in the apps)
        apps:                                             # define all applications
          supabase:                                       # the definition of supabase app
            conf:                                         # override /opt/supabase/.env

              # postgres connection string (use the correct ip and port)
              POSTGRES_HOST: 172.17.0.1      # point to the local postgres node
              	# ip 从 127.0.0.1 改成这个了
              POSTGRES_PORT: 5436             # access via the 'default' service, which 

	# ./app.yml 运行出错才这样改的



```



### 能登录 supabase 下一步怎么做

```

Based on the configuration files in /opt/supabase , the Supabase Studio dashboard is protected by Basic Authentication via the Kong gateway. The "Unauthorized" error you are seeing is because you need to log in.

Here is the information you need to proceed:

### 1. Access the Dashboard
When you visit http://xx.xx.xx.xx:8000/project/default , your browser should prompt you for a username and password. Use the following credentials found in your .env file:

- Username : supabase
- Password : pigsty
### 2. API Keys for Development
Once you have access to the dashboard, you will need API keys to connect your applications to Supabase. These are also defined in your .env file:

- anon key (public, for frontend use):
  
```
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
  eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1
  NjgwMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc
  ```
- service_role key (private, for backend admin use - keep secret ):
  
  ```
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
  eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaXNzIjoic3VwYWJhc2UiLCJpYXQiOjE3Njc4MDE2MDAsImV4
  cCI6MTkyNTU2ODAwMH0.JHimTs0hXELAEp1FtwPp2SXq-l8Dzfv8oHoGJ9oWvF8
  ```
### 3. Next Steps
1. Log in to the dashboard using the credentials above.
2. Verify that you can see the "Default Project".
3. If you need to change the password , you can edit the /opt/supabase/.env file, update DASHBOARD_PASSWORD , and run docker-compose up -d to apply changes.
<todo_status>
{"todos":[{"id":"check_config","status":"completed","content":"Check Supabase installation and configuration in /opt/supabase","priority":"high","created_at":1767836783},{"id":"check_docker","status":"completed","content":"Check running Docker containers for Supabase services","priority":"high","created_at":1767836783},{"id":"resolve_access","status":"completed","content":"Resolve "Unauthorized" error or provide access instructions","priority":"high","created_at":1767836783}]}
</todo_status>

  ```



### Dashboard 是什么还可以新建 project 吗？

```

Dashboard 是什么 Supabase Dashboard (Supabase Studio) 是 Supabase 的可视化管理界面。你可以通过它来：

- 管理数据库表结构 (Table Editor)
- 编写和执行 SQL (SQL Editor)
- 管理用户认证和权限 (Authentication)
- 管理对象存储 (Storage)
- 查看 API 文档
除了默认 project 还可以新建 project 吗 不可以 。
在自托管 (Self-Hosted) 的 Docker 环境下，Supabase Studio 与底层的 Docker 服务容器（Kong, GoTrue, PostgREST 等）以及 Postgres 数据库是 1 对 1 绑定 的。

- "Default Project" 直接对应你当前的这套 Docker 服务和 Postgres 数据库。
- Studio 界面上显示的 "Default Project" 只是一个通过环境变量配置的名称 ( STUDIO_DEFAULT_PROJECT=Pigsty )。
- 如果你需要另一个 "Project"（即另一套完全隔离的 Supabase 环境），你需要部署另一套 Supabase Docker 容器栈，并监听不同的端口。

```





### 修改默认 Project 名称的方法

```

sed -i 's/STUDIO_DEFAULT_PROJECT=Pigsty/STUDIO_DEFAULT_PROJECT=MyNewProject/' /opt/supabase/.env

cd /opt/supabase && docker compose up -d


修改 Supabase 默认 Project 名称需要修改环境变量配置文件，并重启相关容器。

1. 修改配置文件 修改 /opt/supabase/.env 文件中的 STUDIO_DEFAULT_PROJECT 变量。
   
```
   /opt/supabase/.env
   STUDIO_DEFAULT_PROJECT=MyNewProject  # 将原来的 Pigsty 修改为你想要的名称

   ```
   (我已经帮你执行了这一步，将名称修改为了 MyNewProject )
2. 重启 Supabase 修改配置后，必须重启 Supabase 服务（主要是 Studio 容器）才能生效。
   
   ```
   cd /opt/supabase
   docker compose up -d
   ```
   (我已经帮你执行了这一步， supabase-studio 容器已重建)
现在你可以刷新浏览器访问 Dashboard，应该能看到 Project 名称已经变成了 MyNewProject 。

   ```





### 新建的用户可以有自已的各种 key 吗

```

`http://xx.xx.xx.xx:8000/project/default/auth/users`  我在这里新建了一个 user ，这个用户可以有自已的各种 key 吗

在 Supabase 中，用户（User）和 项目（Project）的 Key 是完全不同的概念。

简单来说： 你在 Auth 页面新建的用户，不会拥有类似 anon 或 service_role 那样的永久 API Key。

### 1. 项目级 Key (Project Keys)
这是你之前在 .env 文件里看到的，属于整个项目的“大门钥匙”。

- anon key : 公钥。给前端用的，权限很低，必须配合 Row Level Security (RLS) 使用。
- service_role key : 私钥。拥有上帝权限，可以绕过所有 RLS 规则。 绝对不能给普通用户 。
### 2. 用户级 Token (User Access Token / JWT)
当你在 http://xx.xx.xx.xx:8000/project/default/auth/users 创建一个用户后，这个用户是用来 登录你的应用 的。

- 用户没有永久 Key ：用户登录（通过 Email/密码, OAuth 等）成功后，Supabase 会发给前端一个临时的 Access Token (JWT) 。
- Token 代表身份 ：前端在请求 Supabase 数据库或 API 时，会在 Header 里带上这个 Token。
- RLS 决定权限 ：Postgres 数据库会解析这个 Token，知道“这是 User A”，然后根据你设置的 RLS (Row Level Security) 规则，决定 User A 能查哪些数据，能改哪些数据。
### 总结
- Project Keys ( anon / service_role ) ：是给 开发者 用来连接 Supabase 服务的。
- User Users ：是你的 App 的最终用户 。他们通过登录获取 临时 Token 来证明身份，而不是拥有永久 Key。
如果你需要给某个程序（而不是人）分配一个长期有效的凭证，通常的做法是：

1. 创建一个特定的 User。
2. 在数据库中手动生成一个长期有效的 JWT（不推荐，有安全风险）。
3. 或者，只使用 service_role key 并在后端代码中控制权限（这是作为管理员的操作方式）。



```





### SQL Editor 查用户信息

```

SELECT * 
FROM auth.users 
WHERE email = 'your_email@example.com';

```



### 前端用户如何完成注册

```

`\root\pigsty\pigsty.yml` 分析 Supabase 新用户注册方面的配置，配好后在前端用户如何完成注册

### 配置分析
查看 /opt/supabase/.env 文件，当前的注册配置如下：

1. 允许邮箱注册 ( ENABLE_EMAIL_SIGNUP=true )：开启。
2. 自动确认邮箱 ( ENABLE_EMAIL_AUTOCONFIRM=true )： 开启 。
   - 这是一个非常关键的配置。因为你的 SMTP 邮件服务配置的是假的 ( fake_mail_user )，如果关闭自动确认，Supabase 会尝试发送验证邮件但失败，导致用户无法激活。
   - 现状 ：用户注册后 立即激活 ，无需点击邮件验证链接。
3. SMTP 配置 ：目前是默认的假配置 ( fake_sender 等)。由于开启了自动确认，这暂时不会影响注册流程。
### 前端注册实现
由于配置了自动确认，前端注册流程非常简单。你只需要使用 supabase-js 客户端库。
 1. 安装依赖
​```
npm install @supabase/supabase-js
​``` 2. 注册代码示例
你需要用到之前获取的 SUPABASE_URL (你的公网 IP + 端口) 和 ANON_KEY 。

​```
import { createClient } from '@supabase/supabase-js'

// 1. 初始化客户端
const supabaseUrl = 'http://xx.xx.xx.xx:8000'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1Njg
wMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc' // 填入你的 anon key
const supabase = createClient(supabaseUrl, supabaseKey)

// 2. 注册函数
async function signUpNewUser() {
  const { data, error } = await supabase.auth.signUp({
    email: 'example@email.com',
    password: 'example-password',
  })

  if (error) {
    console.error('注册失败:', error.message)
    return
  }

  // 因为开启了 ENABLE_EMAIL_AUTOCONFIRM=true
  // data.user 会立即返回，且 data.session 也会有值（表示已自动登录）
  console.log('注册成功:', data)
  console.log('用户 ID:', data.user.id)
  console.log('Access Token:', data.session.access_token)
}

signUpNewUser()
​```
### 总结
目前的配置非常适合开发环境： 注册即登录，无需邮件验证 。如果你将来要上线生产环境并要求真实的邮件验证，你需要：

1. 在 .env 中配置真实的 SMTP 服务（如 SendGrid, AWS SES 等）。
2. 将 ENABLE_EMAIL_AUTOCONFIRM 改为 false 。
3. 重启 Supabase 服务。


```



### 前端用户如何完成登录

```

前端用户登录同样非常简单，使用 supabase.auth.signInWithPassword 方法即可。

### 前端登录代码示例
​```
import { createClient } from '@supabase/supabase-js'

// 1. 初始化客户端 (与注册时相同)
const supabaseUrl = 'http://xx.xx.xx.xx:8000'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1Njg
wMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc'
const supabase = createClient(supabaseUrl, supabaseKey)

// 2. 登录函数
async function signInUser() {
  const { data, error } = await supabase.auth.signInWithPassword({
    email: 'example@email.com',
    password: 'example-password',
  })

  if (error) {
    console.error('登录失败:', error.message)
    return
  }

  // 登录成功
  console.log('登录成功，Session 信息:', data.session)
  console.log('Access Token (JWT):', data.session.access_token)
  
  // 你可以将 access_token 存储起来，或者由 supabase-js 自动管理（默认存储在 
  localStorage）
}

signInUser()
​```
### 关键点说明
1. Session 管理 ： supabase-js 默认会自动将 Session 信息（包括 Token）保存在浏览器的 localStorage 中。这意味着用户刷新页面后，依然保持登录状态。
2. 获取当前用户 ：在应用的任何地方，你可以通过 supabase.auth.getUser() 来检查当前是否已登录以及获取用户信息。
3. 登出 ：使用 supabase.auth.signOut() 即可登出，这会清除本地的 Session。


```



### 面对复杂的业务逻辑是否还需要单独写后端代码

```

这是一个非常经典的问题。Supabase 提供了多种方式来处理复杂逻辑，通常你 不需要 像传统开发那样写一个完整的、独立的后端（如 Spring Boot 或 Express），但你依然需要写“后端逻辑”。

你可以根据业务复杂度选择以下三种方案：

### 方案一：Postgres 数据库函数 (Database Functions) —— 适合“数据密集型”逻辑
如果你的逻辑主要是对数据的增删改查组合，或者需要强事务保证（例如：转账，A扣钱B必须加钱），直接在数据库里写 SQL 函数（PL/pgSQL）是最高效的。

- 优点 ：速度极快（数据不出数据库），强一致性，可以直接通过 API ( rpc ) 调用。
- 缺点 ：SQL 语言编写复杂逻辑（如调用第三方 API、复杂的字符串处理）体验较差，调试困难。
### 方案二：Supabase Edge Functions —— 适合“现代全栈”逻辑 (推荐)
这是 Supabase 提供的 Serverless 函数服务（基于 Deno）。你可以用 TypeScript/JavaScript 编写逻辑。

- 场景 ：
  - 调用第三方支付接口 (Stripe/Alipay)。
  - 发送复杂的通知 (邮件/短信)。
  - 数据清洗、复杂的算法计算。
  - Webhooks 处理。
- 优点 ：使用熟悉的 TS/JS，开发体验好，易于扩展，与 Supabase Auth 无缝集成。
- 缺点 ：有冷启动时间（虽然 Deno 很快），比数据库内部函数慢一点点。
### 方案三：独立的后端服务 —— 适合“极度复杂/遗留”系统
只有在以下情况你才需要单独起一个后端服务（Go/Java/Node等）：

1. 你有现成的遗留系统需要集成。
2. 你需要长时间运行的任务（Edge Functions 通常有执行时间限制）。
3. 逻辑极度复杂，依赖大量特殊的系统库。
### 总结建议
对于 90% 的新项目，推荐的组合是：

1. 简单的 CRUD ：直接在前端用 supabase-js 调用，配合 RLS 保证安全。
2. 复杂业务/第三方集成 ：使用 Edge Functions 。
3. 高性能数据处理 ：使用 Database Functions 。
不需要 专门写一个传统的后端服务。

```



### 如果 Edge Functions 里的 javascript 代码报错了有单步调试的方法吗

```

Supabase Edge Functions 的调试体验取决于你是在 本地开发 还是 部署到云端 。

### 1. 本地开发环境 (推荐)
这是唯一支持类似“单步调试”体验的方式。你需要使用 Supabase CLI 在本地运行函数。

- 运行函数 ：
```
  supabase functions serve --debug
  ``` 加上 --debug 参数后，你可以通过 Chrome DevTools 或 VS Code 进行调试。
- VS Code 调试 ：
  你可以配置 VS Code 的 launch.json 来连接到本地运行的 Deno 进程，从而设置断点、查看变量和单步执行。
  - Supabase 底层使用 Deno，所以本质上是调试 Deno 程序。
  - 你需要在 VS Code 中安装 "Deno" 插件。
### 2. 部署后 (生产/预览环境)
一旦函数部署到服务器（无论是官方云还是你的自托管环境）， 不支持 传统的断点单步调试。你主要依赖以下方式排查问题：

- 日志 (Logs) ：
  这是最主要的手段。在 Dashboard 的 "Edge Functions" -> "Logs" 页面查看。
  - 善用 console.log() , console.error() 。
  - 在代码中打印关键变量的值和执行路径。
- 本地重现 ：
  如果线上报错，尝试提取线上的输入参数（Request Body/Headers），在本地用 curl 或 Postman 调用本地运行的函数 ( localhost:54321/functions/v1/xxx ) 来复现并单步调试。
### 总结
- 单步调试 ： 仅限本地开发环境 (通过 Supabase CLI + VS Code/Chrome)。
- 线上排查 ：依赖 日志 和 错误监控 (Sentry 等)。
建议的开发流程是：先在本地编写并充分调试（利用断点），确认无误后再部署。

  ```



### 为什么 DASHBOARD_PASSWORD 和 .env 里的定义不一至

```

`\root\pigsty\app\supabase\.env` `\root\pigsty\pigsty.yml` `\root\pigsty\pigsty.yml#L137-137` 为什么 DASHBOARD_PASSWORD 和 .env 里的定义不一至

这是一个非常敏锐的观察！你看到的差异是因为文件角色的不同：

1. \root\pigsty\app\supabase\.env
   - 角色 ：这是 源代码模板 或默认示例文件。
   - 内容 ：它包含的是 Pigsty 项目的默认初始值（例如 DASHBOARD_PASSWORD=pigsty ），仅仅是为了占位或演示。
2. \root\pigsty\pigsty.yml
   - 角色 ：这是你的 基础设施配置中心 (Source of Truth) 。
   - 内容 ：这里定义的是 你真正想要使用的值 。当你运行 Pigsty 的安装脚本（如 ./app.yml 或 ./install.yml ）时，Ansible 会读取这个文件里的配置。
3. 最终结果 ( /opt/supabase/.env )
   - 角色 ：这是 实际运行环境 的配置文件。
   - 生成过程 ：Pigsty 的自动化脚本会把 pigsty.yml 里的值（ pigstyxX ）填入到模板中，生成最终部署在 /opt/supabase/.env 的文件。
总结 ：

- 以 pigsty.yml 为准 。
- 安装过程会将 pigsty.yml 的值覆盖到最终的 .env 中。
- app/supabase/.env 只是一个静态的模板文件，部署后它的内容不会影响运行中的服务，除非你手动去引用它。
目前的运行状态（我们在 /opt/supabase/.env 里看到的）已经正确应用了 pigsty.yml 里的 pigstyxX ，所以一切正常。



```





### 私有化部署 login_with_aliyun 不能以 await supabase.auth.login_with_aliyun 这种方式调用吗

```

私有化部署 login_with_aliyun 不能以 await supabase.auth.login_with_aliyun 这种方式调用吗

不可以。

在 Supabase 的客户端 SDK ( @supabase/supabase-js ) 中， supabase.auth 下的方法（如 signInWithPassword , signUp 等）是 官方固定的原生方法 。

您自己编写的 Edge Function (如 login_with_aliyun ) 属于自定义的后端逻辑，不能自动“挂载”到 supabase.auth 对象上。

### 1. 正确的调用方式
调用 Edge Function 的标准方式是使用 supabase.functions.invoke ：

​```
const { data, error } = await supabase.functions.invoke('login_with_aliyun', {
  body: {
    email: 'user@example.com',
    password: 'password',
    captchaVerifyParam: 'aliyun_token_xxx'
  }
})
​```
### 2. 为什么不能直接用 auth.login_with_aliyun？
- 命名空间不同 ： supabase.auth 专门用于与 Supabase 的 GoTrue (Auth) 服务通信。
- 服务不同 ：您的函数运行在 Edge Functions 服务中，而 auth 方法请求的是 Auth 服务。两者的 API 路径完全不同（ /functions/v1/... vs /auth/v1/... ）。
### 3. 如果您非常想要这种写法 (封装建议)
如果您希望在前端代码中保持整洁，或者为了统一调用风格，您可以自己封装一个辅助函数，或者扩展 supabase 实例（虽然不推荐直接修改 SDK 原型，但在应用层封装是很好的实践）。

创建一个 auth_helper.js :

​```
// utils/auth.js

/**
 * 封装自定义的阿里云登录逻辑
 */
export async function loginWithAliyun(supabase, { email, password, 
captchaVerifyParam }) {
  // 调用 Edge Function
  const { data, error } = await supabase.functions.invoke('login_with_aliyun', {
    body: { email, password, captchaVerifyParam }
  })

  if (error) return { data: null, error }

  // 核心步骤：如果函数返回了 session，我们需要手动在客户端设置它
  // 这样 supabase.auth.getUser() 等方法才能获取到登录状态
  if (data?.session) {
    const { error: sessionError } = await supabase.auth.setSession(data.session)
    if (sessionError) return { data: null, error: sessionError }
  }

  return { data, error: null }
}
​```
在业务代码中使用:

​```
import { loginWithAliyun } from './utils/auth'

// 使用起来就像原生的一样方便
const { data, error } = await loginWithAliyun(supabase, {
  email: '...',
  password: '...',
  captchaVerifyParam: '...'
})
​```
### 总结
- 原生 SDK 不支持 supabase.auth.login_with_aliyun 这种魔法。
- 必须使用 supabase.functions.invoke 。
- 关键点 ：Edge Function 返回 session 后，前端必须调用 supabase.auth.setSession(data.session) 才能真正完成“登录态”的建立。


```





### supabase 怎么知道去哪里找 login_with_aliyun 这个函数

```

这是一个非常好的问题。在私有化部署（Docker）环境中，Supabase Edge Runtime 找到您的函数完全依赖于 docker-compose.yml 中的配置 。

它不像 Supabase Cloud 那样有自动的路由注册中心，而是通过以下 3 个关键步骤“物理连接”起来的：

### 1. 挂载目录 (Mapping)
首先，通过 Docker 的 volumes 配置，把您电脑上的代码目录“映射”到了容器内部。

请看您的 docker-compose.yml ：

​```
    volumes:
      # 左边是宿主机路径 (./functions) -> 右边是容器内路径 (/usr/services)
      - ./functions:/usr/services
​```
这意味着：

- 宿主机的 Supabase/docker_functions/functions/ 目录
- 变成了容器内的 /usr/services/ 目录
所以容器里现在有了 /usr/services/login_with_aliyun 这个文件夹。

### 2. 指定启动入口 (Command)
然后，通过 command 指令明确告诉 Edge Runtime 去运行哪个文件夹。

请看您的 docker-compose.yml ：

​```
    # --main-service 参数指定了具体要运行的函数路径
    command: start --main-service /usr/services/login_with_aliyun
​```
- Edge Runtime 启动时，会去读取 /usr/services/login_with_aliyun 目录。
- 它默认会在该目录下寻找 index.ts 文件作为入口（这就是为什么您的代码文件名必须是 index.ts ）。
### 3. 路由匹配 (Routing)
在您目前的配置中（使用 --main-service ），Edge Runtime 会将这个函数作为 主服务 运行。
这意味着：

- 根路径 ( / ) 的所有请求都会被转发给这个函数。
- 您不需要在 URL 里写 /functions/v1/login_with_aliyun 。
- 直接访问 http://localhost:10000/ 就等于在调用这个函数。
### 总结
Supabase 知道去哪找，是因为您在 docker-compose.yml 里：

1. 把代码 放进去了 ( volumes )。
2. 手指 指过去了 ( command: ... /usr/services/login_with_aliyun )。

```



### self-hosted supabase 如何部署函数，效果类似 supabase functions deploy login_with_aliyun --no-verify-jwt 这个命令一样

```

针对 Self-Hosted Supabase (私有化部署) 环境，部署 login_with_aliyun 并实现类似 supabase functions deploy ... --no-verify-jwt 的效果，主要通过修改 docker-compose.yml 来配置 Edge Runtime 容器。

我已经为您完成了相关配置修改，以下是详细操作步骤：

### 1. 核心配置修改
我已修改了 docker-compose.yml 文件：

- 指定运行函数 : 将启动命令从默认的 hello-world 修改为 login_with_aliyun 。
- 配置 JWT 验证 : 添加 VERIFY_JWT=false 环境变量，这等同于 --no-verify-jwt 标志，允许未登录用户调用此接口。
- 预留密钥位置 : 添加了阿里云 Access Key 的环境变量占位符。
### 2. 您需要执行的操作
请打开 Supabase/docker_functions/docker-compose.yml 文件，填入您真实的阿里云密钥：

​```
    environment:
      # ...
      # 请填入您的真实密钥
      - ALIYUN_ACCESS_KEY_ID=您的AccessKeyId
      - ALIYUN_ACCESS_KEY_SECRET=您的AccessKeySecret
      # 已设置为 false，无需修改
      - VERIFY_JWT=false 
​```
### 3. 部署/重启服务
修改完成后，在终端中运行以下命令重启服务：

​```
cd /root/huggingface_echodict/Supabase/docker_functions
docker compose up -d
​```
### 4. 调用说明
在自托管模式下，Edge Runtime 直接运行该函数。假设您的 Docker 宿主机 IP 为 YOUR_IP ，调用地址通常为：

http://YOUR_IP:10000/

前端调用代码示例：

​```
// 注意：自托管直接调用 Edge Runtime 时，URL 需要指向您的 Docker 服务端口
const response = await fetch('http://YOUR_IP:10000/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password',
    captchaVerifyParam: 'aliyun_token'
  })
})
​```
我已经将上述自托管部署说明添加到了 README.md 的末尾，供您随时参考。

```



### 如果需要这个配置只针对 login_with_aliyun 这一个函数怎么办

```

针对只需要对 login_with_aliyun 函数禁用 JWT 验证的需求，Supabase Edge Runtime 提供了一个专门的环境变量配置方式。

我已为您更新了 docker-compose.yml 和 README.md ，采用了更精细的配置：

### 1. 使用 Per-Function 配置 (已修改)
在 docker-compose.yml 中，我移除了全局的 VERIFY_JWT=false ，改为：

​```
    environment:
      # ...
      # 格式: PER_FUNCTION_JWT_VERIFY_<function_name>=<true|false>
      - PER_FUNCTION_JWT_VERIFY_login_with_aliyun=false
​```
这样配置后：

- login_with_aliyun : 任何人都可以调用（公开接口）。
- 其他函数 : 仍然需要有效的 JWT 才能调用（受保护）。
### 2. 关于入口配置 (Main Service)
为了让这个改动更合理，我也顺便调整了 command 。
此前是将 login_with_aliyun 作为主服务 ( --main-service )，这会导致所有请求都由它处理。
我现在创建了一个简单的 main 函数作为默认入口，并将 command 指向它：

​```
    command: start --main-service /usr/services/main
​```
这为未来支持多个函数留出了空间。但在 单函数模式 下，您也可以改回直接指向 login_with_aliyun 。

### 总结
您现在只需确保 docker-compose.yml 中包含： - PER_FUNCTION_JWT_VERIFY_login_with_aliyun=false 即可实现仅针对该函数的免鉴权访问。


```





### 修改 docker-compose 让它融入 Supabase 网络

```

docker-compose down && docker-compose up -d

docker ps --filter "name=docker_functions-edge-runtime-1"

docker ps --filter "name=supabase-kong"

ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1NjgwMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc"
curl -i -X POST http://localhost:8000/functions/v1/login_with_aliyun \
  -H "Authorization: Bearer $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com", "password":"password"}'
  
  
 ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1NjgwMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc"

echo "Testing Direct Access:"
curl -i -X POST http://localhost:10000/login_with_aliyun \
  -H "Authorization: Bearer $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com", "password":"password"}'

echo -e "\n\nTesting via Kong:"
curl -i -X POST http://localhost:8000/functions/v1/login_with_aliyun \
  -H "Authorization: Bearer $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com", "password":"password"}'


### 网络集成完成
我已经修改了您的 docker-compose.yml ，将独立的 Edge Runtime 容器成功加入了 Supabase 的主网络 ( supabase_default )。

主要变更：

1. 加入网络 ：配置容器连接到外部的 supabase_default 网络。
2. 设置别名 ：给容器设置了网络别名 functions 。这非常关键，因为 Kong 网关默认配置就是转发给 http://functions:9000 。
3. 无缝集成 ：现在您的容器虽然是独立部署的，但在网络层面表现得就像是 Supabase 官方堆栈的一部分。
修改后的配置片段： docker-compose.yml

​```
services:
  edge-runtime:
    # ... 其他配置保持不变 ...
    networks:
      supabase_default:
        aliases:
          - functions  # 让 Kong 认为这就是那个 "functions" 服务

networks:
  supabase_default:
    external: true     # 使用 Supabase 主堆栈已创建的网络
​```
### 验证结果
1. 容器状态 ：容器已重启并正常运行。
2. 直接访问测试 ： curl http://localhost:10000/login_with_aliyun -> 成功 (返回 400 Bad Request，证明服务可达)。
3. Kong 网关测试 ： curl http://localhost:8000/functions/v1/login_with_aliyun -> 连接建立成功 。
### 现在您可以：
直接在前端代码中使用标准调用方式，无需任何额外配置：

​```
const { data, error } = await supabase.functions.invoke('login_with_aliyun', {
  body: { 
    email: 'user@example.com', 
    password: 'password', 
    captchaVerifyParam: 'aliyun_token_xxx' 
  }
})
​```
原理解释 ：
当您调用 invoke 时，请求发送给 Kong (端口 8000) -> Kong 根据路由规则转发给内部主机名 functions (端口 9000) -> Docker 网络将其解析到您的新容器 -> 您的 main/index.ts 接收请求并路由到 login_with_aliyun 。

```



### edge function 正常登录

```

curl --location 'http://43.153.xx.xx:8000/functions/v1/login_with_aliyun' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1NjgwMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc' \
  --data-raw '{
    "email": "123456@qq.com",
    "password": "123456",
    "captchaVerifyParam": "dummy_token"
  }'

```





### Cloudflare Turnstile 身份验证

- https://github.com/WonderLand33/prompt-optimizer

1. 访问 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 "Turnstile" 部分
3. 创建新的站点
4. 获取 Site Key 和 Secret Key
5. 将密钥添加到环境变量中



#### Edge function 实现验证

https://juejin.cn/post/7560879441485217818  Supabase **Edge Functions 开发指南**

- https://juejin.cn/post/7568796644349018112  **Supabase CLI** 本地开发与数据库操作指南

https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile

- https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/  cf 文档



```

supabase functions new cloudflare-turnstile
	# poject 里新建函数

And add the code to the index.ts file:

import { corsHeaders } from '../_shared/cors.ts'

console.log('Hello from Cloudflare Trunstile!')

function ips(req: Request) {
  return req.headers.get('x-forwarded-for')?.split(/\s*,\s*/)
}

Deno.serve(async (req) => {
  // This is needed if you're planning to invoke your function from a browser.
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  const { token } = await req.json()
  const clientIps = ips(req) || ['']
  const ip = clientIps[0]

  // Validate the token by calling the
  // "/siteverify" API endpoint.
  let formData = new FormData()
  formData.append('secret', Deno.env.get('CLOUDFLARE_SECRET_KEY') ?? '')
  formData.append('response', token)
  formData.append('remoteip', ip)

  const url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
  const result = await fetch(url, {
    body: formData,
    method: 'POST',
  })

  const outcome = await result.json()
  console.log(outcome)
  if (outcome.success) {
    return new Response('success', { headers: corsHeaders })
  }
  return new Response('failure', { headers: corsHeaders })
})


Deploy the server-side validation Edge Functions#

supabase functions deploy cloudflare-turnstile
supabase secrets set CLOUDFLARE_SECRET_KEY=your_secret_key




前端
const { data, error } = await supabase.functions.invoke('cloudflare-turnstile', {
  body: { token },
})


```





#### 验证关键配置

```

vi /opt/supabase/.env
## Captcha Config
GOTRUE_SECURITY_CAPTCHA_ENABLED=true
GOTRUE_SECURITY_CAPTCHA_PROVIDER=turnstile
GOTRUE_SECURITY_CAPTCHA_SECRET=0x4AAAAAACLZlc1yWo0Ukxxxxxxxxxxx
GOTRUE_SECURITY_CAPTCHA_SITE_KEY=0x4AAAAAACLZxxxxxxxxx
	# 加在最后


vi /opt/supabase/docker-compose.yml
      GOTRUE_EXTERNAL_PHONE_ENABLED: ${ENABLE_PHONE_SIGNUP}
      ## Captcha Config
      GOTRUE_SMS_AUTOCONFIRM: ${ENABLE_PHONE_AUTOCONFIRM}
      GOTRUE_SECURITY_CAPTCHA_ENABLED: ${GOTRUE_SECURITY_CAPTCHA_ENABLED}
      GOTRUE_SECURITY_CAPTCHA_PROVIDER: ${GOTRUE_SECURITY_CAPTCHA_PROVIDER}
      GOTRUE_SECURITY_CAPTCHA_SECRET: ${GOTRUE_SECURITY_CAPTCHA_SECRET}
      GOTRUE_SECURITY_CAPTCHA_SITE_KEY: ${GOTRUE_SECURITY_CAPTCHA_SITE_KEY}
      	# 加在这里
      # Uncomment to enable custom access token hook.
      	




    environment:
      # Binds nestjs listener to both IPv4 and IPv6 network interfaces
      HOSTNAME: "::"
      
      # 1. 指向内部 meta 服务
      STUDIO_PG_META_URL: http://meta:8080
      
      POSTGRES_PORT: ${POSTGRES_PORT}
      POSTGRES_HOST: ${POSTGRES_HOST}
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      PG_META_CRYPTO_KEY: ${PG_META_CRYPTO_KEY}
      DEFAULT_ORGANIZATION_NAME: ${STUDIO_DEFAULT_ORGANIZATION}
      DEFAULT_PROJECT_NAME: ${STUDIO_DEFAULT_PROJECT}
      OPENAI_API_KEY: ${OPENAI_API_KEY:-}
      
      # 2. 指向内部 kong 网关
      SUPABASE_URL: http://kong:8000
      
      # 3. 这个保持公网地址不变 (给前端用的)
      SUPABASE_PUBLIC_URL: ${SUPABASE_PUBLIC_URL}
      
      SUPABASE_ANON_KEY: ${ANON_KEY}
      SUPABASE_SERVICE_KEY: ${SERVICE_ROLE_KEY}
      AUTH_JWT_SECRET: ${JWT_SECRET}
      LOGFLARE_PRIVATE_ACCESS_TOKEN: ${LOGFLARE_PRIVATE_ACCESS_TOKEN}
      
      # 4. 指向内部 analytics 服务 (假设服务名叫 analytics，请核对 depends_on 里的名字)
      LOGFLARE_URL: http://analytics:4000
      
      NEXT_PUBLIC_ENABLE_LOGS: true
      NEXT_ANALYTICS_BACKEND_PROVIDER: postgres
      
  说明 :

     - SUPABASE_PUBLIC_URL : 这个变量通常用于生成外部可访问的链接（如邮件中的链接），所以它 必须 保持为公网地址 ( http://echoplayer.com:8000 )。
     - SUPABASE_URL (无 PUBLIC): 这是 Studio 后端去连接 API 的地址，走内部网络更安全。


docker compose -f /opt/supabase/docker-compose.yml up -d
	或着 cd /opt/supabase && docker compose up -d
	
docker compose -f /opt/supabase/docker-compose.yml stop

```





#### Supabase 3000 8000 端口

```

Supabase 包含多个服务，通常运行在不同的端口（以标准 Docker 部署为例）：

- API Gateway (Kong) : 默认端口 8000 (这是前端代码应该连接的地址)。
- Supabase Studio (Dashboard) : 默认端口 3000 (这是你在浏览器访问的管理界面)。



############ 
 # Domain 
 # YOU MUST CHANGE THESE WHEN ACCESS VIA DOMAIN NAME 
 ############ 
 # replace if you intend to use Studio outside of localhost 
 # 必须指向 Kong API 网关 (端口 8000)
 SUPABASE_PUBLIC_URL=http://echopxxx.com:8000
 API_EXTERNAL_URL=http://echoxxx.com:8000

 # SITE_URL 是你的前端网站地址，用于重定向
 # 如果你的论坛前端也部署在 80 端口（替代了 Pigsty 页面），则填 http://echopxxx.com
 # 如果还在开发中，可能是 http://localhost:5173 或其他
 SITE_URL=http://echoxxx.com:5173



最快速让验证通过的办法是使用 Cloudflare 官方提供的测试 Key 。

我已经将你的 .env 文件中的 VITE_TURNSTILE_SITE_KEY 替换为了测试专用的 "Always Pass" (永远通过) Key：

​```
VITE_TURNSTILE_SITE_KEY=1x00000000000000000000AA
​```
现在你可以刷新页面重试 ，Turnstile 应该会立即显示绿色的对勾，并且你可以正常进行注册或登录流程。

### 💡 为什么之前的 Key 无法通过？
既然你是在 http://echopxxxx.com:5173 访问，而之前的 Key 一直失败，可能有以下原因：

1. Hostname 限制 : 你的 Cloudflare 后台可能只配置了 echoxxxx.com ，但 Turnstile 在某些环境下可能会校验端口或具体的子环境。
2. 环境风控 : 浏览器环境（如无头模式、频繁刷新、开发者工具打开）可能被 Cloudflare 判定为机器人。
3. 配置生效延迟 : Cloudflare 的配置修改有时需要几分钟生效。
### ⚠️ 上线前必做
目前的测试 Key 仅用于开发调试，任何人都可以通过验证。 在正式上线前，请务必换回你的真实 Site Key ( 0x4AAAAAAxxxxxx )，并确保 Cloudflare 后台的 Hostname 配置正确包含了你的所有访问域名。




VITE_TURNSTILE_SITE_KEY=1x00000000000000000000AA 换这个就通过了，说明之前是什么问题


使用测试 Key 能通过，说明你的 代码实现是完全正确 的（Widget 渲染、回调函数、Token 提交逻辑都没问题）。

问题 100% 出在 Cloudflare 后台的配置或环境校验上。 具体来说，最可能是以下原因之一：

### 1. Hostname 白名单不匹配 (最常见)
你之前填的 Hostname 是 echoxxx.com ，但你访问的地址可能是：

- IP 访问 : http://123.123.123.123:5173
- Localhost : http://localhost:5173 或 http://127.0.0.1:5173
- 子域名 : http://www.echoxxx.com 或 http://dev.echoxxx.com
如果访问地址和后台配置的 Hostname 不完全一致（或者是其子域名），Turnstile 就会直接拦截。

- 解决方法 : 在 Cloudflare 后台 Hostname 列表里把 localhost , 127.0.0.1 以及你所有可能用到的域名都加进去。
### 2. Widget Mode 设置过严
如果你的模式选了 Invisible (隐形模式)，但它判定你的浏览器环境（可能是因为开了开发者工具、插件干扰、或者是刚注册的域名）“可疑”，它会尝试弹出一个交互验证。但如果你的代码或 UI 容器 ( #turnstile-widget ) 没留够空间显示这个交互框，验证就会卡死在 "Unsolved"。

- 解决方法 : 建议先选 Managed (智能模式)，让它自动决定是否显示复选框。
### 3. 域名解析/SSL 问题
Cloudflare 可能会校验请求的 Origin。如果你的 echoplayer.com 还没有正确解析，或者你在本地用 hosts 强行指向但 SSL 证书不对，也可能导致校验失败。

### 结论
既然测试 Key 能过，你可以放心地继续开发后续功能。 等到要正式上线时 ，再换回正式 Key，并确保那时的域名（如 echoxxx.com ）是真实可访问的，且在 Cloudflare 后台配置无误即可。






Turnstile 网站上 Challenges unsolved 为什么看不到验证失败的原因

Cloudflare Turnstile 的设计理念是 隐私优先 和 极简主义 ，它确实不像传统的防火墙或 WAF 那样提供详细的“错误日志”。

你无法在仪表盘看到“失败原因”主要有以下几个设计原因：

1. 安全隐患 (Security through Obscurity) :
   如果 Cloudflare 详细告诉攻击者（或你的调试工具）“失败是因为 IP 信誉低”或者“失败是因为鼠标轨迹异常”，那么攻击者就可以针对性地优化他们的脚本来绕过验证。因此，它只返回一个模糊的“Unsolved”。
2. 前端验证 vs 后端日志 :
   
   - 前端 (Dashboard) : 这里看到的 Challenges Issued vs Challenges Solved 只是一个统计数字。
   - 客户端 (浏览器) : 真正的错误详情其实在 你浏览器的 Console 里。当验证失败时，Turnstile 的 JS SDK 会在控制台打印错误代码（如 Error 300xxx ）。
     - 300030 : 域名不匹配 (Hostname Mismatch) —— 这是你之前最可能遇到的问题 。
     - 600010 : 验证超时。
   - 后端 (API) : 如果你的后端调用了 siteverify 接口，API 响应里会包含 error-codes 字段（如 invalid-input-response ），这才是查看具体原因的地方。但在你的场景下（纯前端组件未通过），请求还没到后端，所以只能看浏览器控制台。
### 此时你该如何排查？
既然 Dashboard 不显示，你唯一的“调试窗口”就是 浏览器开发者工具 ：

1. 把 .env 改回你的真实 Site Key。
2. 打开 Chrome 开发者工具 (F12) -> Console 标签页。
3. 刷新页面，触发验证失败。
4. 仔细看 Console 里的红色报错 。
   - 如果看到 [Cloudflare Turnstile] Invalid site key -> Key 填错了。
   - 如果看到 [Cloudflare Turnstile] Hostname mismatch -> 域名白名单没配对。
总结 ：Cloudflare Dashboard 永远不会 显示具体的失败原因，它只负责统计。具体的“为什么挂了”，必须在发生错误的那个客户端（浏览器控制台）里看。






Console 里的报错信息表示什么：api.js?render=explicit:1 [Cloudflare Turnstile] Error: 300010.
b	@	api.js?render=explicit:1
O	@	api.js?render=explicit:1
content.js:2 2026-01-12T02:26:36.098Z [KISS-Translator] [INFO] TranslatorManager started.
normal?lang=auto:1 [[[ERROR]]]: Uncaught TypeError: Q[rq(...)] is not a function
normal?lang=auto:1 Uncaught TypeError: Q[rq(...)] is not a function
    at wZ.wy (normal?lang=auto:1:204844)
    at wZ.wh (normal?lang=auto:1:98371)
    at wZ.wy (normal?lang=auto:1:204867)
    at wZ.wh (normal?lang=auto:1:98371)
    at wZ.wy (normal?lang=auto:1:204844)
    at wZ.wh (normal?lang=auto:1:98371)
normal?lang=auto:1 Uncaught Error: Uncaught TypeError: Q[rq(...)] is not a function
    at wZ.wi (normal?lang=auto:1:208069)
    at wZ.wh (normal?lang=auto:1:98371)


Error: 300010 是最关键的信息。

它的含义是： Invalid Hostname (域名不匹配) 。

### 详细解释
这个错误明确告诉你，你当前访问的域名（浏览器地址栏里的那个，比如 echoxxx.com:5173 或 localhost ） 不在 你 Cloudflare Turnstile 后台配置的 Hostname 白名单 里。

### 为什么之前一直找不到原因？
- Cloudflare Dashboard 不显示这个，是为了防止攻击者枚举你的配置。
- 下方的那些 normal?lang=auto 报错是你的浏览器插件（翻译插件或类似工具）引起的，和 Turnstile 无关，属于噪音。
### ✅ 解决方案
请执行以下操作，问题将立即解决：

1. 登录 Cloudflare Dashboard。
2. 进入你的 Turnstile Site Settings。
3. 找到 Hostnames (域名管理)。
4. 添加 你当前正在使用的 所有 访问地址：
   - echoxxx.com (如果你用这个域名访问)
   - localhost (如果你在本地调试)
   - 127.0.0.1 (如果你用 IP 访问)
5. 保存。等待 1-2 分钟生效。
6. 刷新你的网页。
配置正确后， Error: 300010 就会消失，Turnstile 就能正常加载了。






这是一个非常典型的 配置陷阱 。虽然看起来你都填对了，但还有一个极其关键的细节可能被忽略了： 端口号 。

虽然 Cloudflare 文档说 Hostname 不需要填端口，但在实际运行中，如果你的应用运行在 非标准端口 （比如 :5173 ）且处于 开发模式 或 IP 直接访问 （即使有域名映射），Cloudflare 的安全机制可能会判定为“来源不匹配”。

### 终极排查清单 (按优先级)
请依次检查以下 3 点，只要有一点不对就会导致验证失败：

1. Site Key 类型不匹配 (最可能原因)
   
   - 请检查你在 Cloudflare 后台申请的 Site Key 类型。
   - 如果是 "Invisible" (隐形) 模式 : 这种模式对环境要求极高。如果你的前端代码没有完美处理异步加载，或者浏览器有一些插件，它会直接判定失败 (Challenges unsolved)。
   - 建议 : 一定要先改成 "Managed" (托管) 模式 。Managed 模式会显示那个“我是人类”的复选框，这最容易调试，也最不容易被误杀。
2. Hostname 的隐形限制
   
   - 你填了 echoxxx.com ，但如果你的浏览器实际解析 echoxxx.com 是指向 127.0.0.1 或局域网 IP（通过 hosts 文件），Cloudflare 有时会检测到这一点并拦截。
   - 关键测试 : 为了彻底排除这个问题，请在 Cloudflare 后台的 Hostname 列表里， 把 127.0.0.1 和 localhost 也加进去 。
   - 原因 : 即使你用域名访问，如果底层连接是回环地址，某些浏览器行为可能会让 Cloudflare 认为你是从本地发起的攻击。
3. Secret Key 没配 (后端拦截)
   
   - 前端显示“验证失败”有时是因为后端（Supabase）拒绝了。
   - 前端拿到 Token 后发给 Supabase，如果 Supabase 里的 Turnstile Secret Key 配错了，或者根本没配，Supabase 会告诉前端“验证失败”。
   - 请确认 : 你是否已经在 Supabase Dashboard (Auth -> Security -> Bot Protection) 里填入了对应的 Secret Key ？
### 建议操作步骤
为了立马解决问题，请按这个顺序做：

1. 第一步 (Cloudflare 后台) :
   
   - 把 Widget Mode 改为 Managed (如果不是的话)。
   - 在 Hostnames 里添加一行： 127.0.0.1 。
   - 在 Hostnames 里添加一行： localhost 。
   - 保存。
2. 第二步 (代码) :
   
   - 在 Login.svelte 中，给 render 函数添加 action 参数（虽然不是必须，但有助于通过风控）：
```
     window.turnstile.render('#turnstile-widget', {
       sitekey: import.meta.env.VITE_TURNSTILE_SITE_KEY,
       action: 'login', // 添加这一行
       // ... 其他回调
     });
     ```
3. 第三步 (测试) :
   
   - 等待 2 分钟让配置生效。
   - 强制刷新 浏览器 (Ctrl+F5) 再试。
如果做完这三步还不行，那 99% 是 Supabase 后端的 Secret Key 配置问题，或者 Supabase 的 Docker 环境变量没生效。

```







#### Supabase 配置

```

I have:

1. Modified /opt/supabase/.env to include the Turnstile keys (placeholders).
2. Modified /opt/supabase/docker-compose.yml to inject these variables into the auth service.
3. Modified /root/pigsty/pigsty.yml to ensure these settings persist in future Pigsty deployments.
4. Restarted the auth service.

vi /opt/supabase/.env
#### Captcha Config
```
GOTRUE_SECURITY_CAPTCHA_ENABLED=true
GOTRUE_SECURITY_CAPTCHA_PROVIDER=turnstile
GOTRUE_SECURITY_CAPTCHA_SECRET=这里填Secret Key
GOTRUE_SECURITY_CAPTCHA_SITE_KEY=这里填Site Key
	# 加在最后


vi /root/pigsty/pigsty.yml
              DASHBOARD_USERNAME: supabase
              DASHBOARD_PASSWORD: pigsty

              # Captcha Config
              GOTRUE_SECURITY_CAPTCHA_ENABLED: true
              GOTRUE_SECURITY_CAPTCHA_PROVIDER: turnstile
              GOTRUE_SECURITY_CAPTCHA_SECRET: 这里填Secret Key
              GOTRUE_SECURITY_CAPTCHA_SITE_KEY: 这里填Site Key


vi /opt/supabase/docker-compose.yml 
      # use absolute URLs for mailer URL paths
      GOTRUE_MAILER_URLPATHS_INVITE: "${SUPABASE_PUBLIC_URL}/${MAILER_URLPATHS_INVITE}"
      GOTRUE_MAILER_URLPATHS_CONFIRMATION: "${SUPABASE_PUBLIC_URL}/${MAILER_URLPATHS_CONFIRMATION}"
      GOTRUE_MAILER_URLPATHS_RECOVERY: "${SUPABASE_PUBLIC_URL}/${MAILER_URLPATHS_RECOVERY}"
      GOTRUE_MAILER_URLPATHS_EMAIL_CHANGE: "${SUPABASE_PUBLIC_URL}/${MAILER_URLPATHS_EMAIL_CHANGE}"
      GOTRUE_EXTERNAL_PHONE_ENABLED: ${ENABLE_PHONE_SIGNUP}
      GOTRUE_SMS_AUTOCONFIRM: ${ENABLE_PHONE_AUTOCONFIRM}
      GOTRUE_SECURITY_CAPTCHA_ENABLED: ${GOTRUE_SECURITY_CAPTCHA_ENABLED}
      GOTRUE_SECURITY_CAPTCHA_PROVIDER: ${GOTRUE_SECURITY_CAPTCHA_PROVIDER}
      GOTRUE_SECURITY_CAPTCHA_SECRET: ${GOTRUE_SECURITY_CAPTCHA_SECRET}
      GOTRUE_SECURITY_CAPTCHA_SITE_KEY: ${GOTRUE_SECURITY_CAPTCHA_SITE_KEY}
		# 注意后面的新增部分


sed -i '/GOTRUE_SMS_AUTOCONFIRM: ${ENABLE_PHONE_AUTOCONFIRM}/a \      GOTRUE_SECURITY_CAPTCHA_ENABLED: ${GOTRUE_SECURITY_CAPTCHA_ENABLED}\n      GOTRUE_SECURITY_CAPTCHA_PROVIDER: ${GOTRUE_SECURITY_CAPTCHA_PROVIDER}\n      GOTRUE_SECURITY_CAPTCHA_SECRET: ${GOTRUE_SECURITY_CAPTCHA_SECRET}\n      GOTRUE_SECURITY_CAPTCHA_SITE_KEY: ${GOTRUE_SECURITY_CAPTCHA_SITE_KEY}' /opt/supabase/docker-compose.yml 


 cd /opt/supabase && docker compose up -d auth
```


 #### 重启 docker，启用 auth





```

 grep -A 5 "Captcha Config" /opt/supabase/.env

 我已经为你配置好了 Cloudflare Turnstile。你需要完成最后一步：填入你自己的密钥。
 

### 1. 修改配置文件

请打开 /opt/supabase/.env 文件，找到文件末尾我新添加的 Captcha Config 部分，并将 <YOUR_TURNSTILE_...> 替换为你从 Cloudflare 获取的真实密钥：


# /opt/supabase/.env

## Captcha Config

GOTRUE_SECURITY_CAPTCHA_ENABLED=true
GOTRUE_SECURITY_CAPTCHA_PROVIDER=turnstile
GOTRUE_SECURITY_CAPTCHA_SECRET=your_secret_key_here  # 替换这里
GOTRUE_SECURITY_CAPTCHA_SITE_KEY=your_site_key_here  # 替换这里


### 2. 重启服务

修改完 .env 后，请在终端执行以下命令使配置生效：



cd /opt/supabase/ && docker compose up -d auth


### 3. 持久化配置 (可选但推荐)

我已经同步修改了 pigsty.yml 。如果你未来重新运行 Pigsty 的安装脚本，请确保也在 pigsty.yml 中填入真实的密钥，否则它会覆盖回占位符。

配置详情：

- Provider : Turnstile
- Enabled : True
- 涉及文件 :
  - .env (已添加)
  - docker-compose.yml (已注入环境变量)
  - pigsty.yml (已备份配置)



通过分析你的项目（Svelte + Supabase），我为你制定并实施了集成 Cloudflare Turnstile 的方案。相比传统的图形验证码，Turnstile 用户体验更好（通常只需点击一下或完全无感），且隐私保护更强。

### 已经完成的前端修改

我修改了两个文件来集成前端验证逻辑：

1. index.html :
   - 引入了 Cloudflare Turnstile 的 SDK 脚本。
2. src/lib/Login.svelte :
   - 添加了 Turnstile 组件容器。
   - 实现了验证码的渲染和 Token 获取逻辑。
   - 在 handleLogin 和 handleSignUp 中，将获取到的 captchaToken 传递给 Supabase。
   - 注意 ：代码中目前使用的是 Cloudflare 的 测试 Site Key ( 1x00000000000000000000AA )，它总是会验证通过。你需要替换为你自己的 Key。

### 你需要做的配置（关键）

为了让这套机制真正生效，你需要在 Cloudflare 和 Supabase 后台进行配置：

  1. Cloudflare 端 (获取 Keys)
 2. 登录 Cloudflare Dashboard 。
 3. 进入 Turnstile 菜单，点击 "Add Site"。
 4. 填写站点名称和你的域名（本地测试填 localhost ）。
 5. 创建后，你会获得 Site Key 和 Secret Key 。
 6. 替换代码 ：打开 src/lib/Login.svelte ，找到第 16 行，将 sitekey 的值替换为你申请到的 Site Key 。 2. Supabase 端 (开启保护)
    这是防止刷接口的关键步骤，开启后 Supabase 会拒绝没有有效 Token 的注册/登录请求。

 7. 登录 Supabase Dashboard 。
 8. 进入你的项目，点击左侧菜单的 Authentication -> Security -> Bot Protection (或者叫 Captcha Protection)。
 9. 在 Cloudflare Turnstile 部分开启开关。
 10. 填入你在 Cloudflare 申请到的 Secret Key (注意是 Secret Key，不是 Site Key)。
 11. 保存设置。

### 它是如何工作的？

1. 用户操作 ：用户在前端点击登录/注册前，必须完成 Turnstile 验证（通常是自动的）。
2. 获取 Token ：验证通过后，Cloudflare 返回一个临时的 captchaToken 。
3. 发送请求 ：前端将这个 Token 连同邮箱密码一起发给 Supabase。
4. 后端验证 ：Supabase 收到请求后，自动拿着 Token 去 Cloudflare 验证。
   - 如果 Token 有效：允许注册/登录。
   - 如果 Token 无效或缺失：直接拒绝请求，返回错误。
     这样就实现了从前端到后端的完整防刷和人机验证。


​```


#### Supabase 沙盒为什么没看到 Turnstile 选项

​```

cd /opt/supabase && docker compose up -d auth   执行这个命令后，Supabase 8000 端口沙盒里的 Authentication 面面为什么没有看到有  Cloudflare Turnstile 选项

这是一个正常的现象， 请不用担心 。

### 原因解释

Supabase 的自托管版本（Self-Hosted）与官方云端版本（Cloud）在 Dashboard（控制面板）上有一些区别：

1. UI 不完全同步 ：自托管的 Studio 面板主要用于管理数据和可视化，但对于许多 基础设施级别的配置 （如 Auth 配置、SMTP、Captcha），它往往 不会 在界面上显示配置选项。

2. 配置即代码 (Config-as-Code) ：在自托管模式下，这些功能完全依赖环境变量（ .env ）控制，而不是通过 UI 点击开关。

3. 已验证生效 ：我刚刚检查了运行中的容器，确认配置已经生效：

   # 容器内部实际生效的环境变量

   GOTRUE_SECURITY_CAPTCHA_ENABLED=true
   GOTRUE_SECURITY_CAPTCHA_PROVIDER=turnstile

### 下一步：前端集成

既然后端已经开启了验证，你需要在 前端代码 中加入 Cloudflare Turnstile 的组件。

1. 在 HTML/React 中引入 Turnstile Widget ：
   你需要获取 Turnstile 的 token 。
2. 调用 Supabase Auth API 时带上 Token ：
   在使用 supabase-js 注册或登录时，传入 captchaToken 。

​```
   // 注册示例
   const { data, error } = await supabase.auth.signUp({
     email: 'example@email.com',
     password: 'example-password',
     options: {
       captchaToken: '这里填入从Turnstile组件获取到的token'
     }
   })
​```

```
   // 登录示例 (如果登录也开启了验证)
   const { data, error } = await supabase.auth.signInWithPassword({
     email: 'example@email.com',
     password: 'example-password',
     options: {
       captchaToken: '这里填入从Turnstile组件获取到的token'
     }
   })
   ```

只要前端传了 Token，后端就会自动去 Cloudflare 验证。如果验证失败或没传 Token，后端会返回错误。

   ```





### 阿里云验证码 2.0

https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/user-guide/implement-supabase-sms-login

- 基于Supabase实现短信验证登录



```

阿里云确实有对应的服务，叫做 阿里云验证码 2.0 (Aliyun Captcha 2.0) 。它在国内的加载速度和稳定性确实优于 Cloudflare，但在 Supabase 项目中集成它会 复杂很多 。

### 核心差异对比

特性 Cloudflare Turnstile (当前方案) 阿里云验证码 2.0 Supabase 支持 原生支持 (后台直接配置) 不支持 (原生 Auth 接口无法验证) 开发成本 🟢 低 (仅前端修改) 🔴 高 (需要编写后端 Edge Function) 国内体验 🟡 尚可 (可用但稍慢) 🟢 极佳 (国内节点) 原理 Token 直接传给 Supabase 验证 需通过自定义后端中转验证

### 如果一定要用阿里云，要怎么做？

因为 Supabase 的 supabase.auth.signUp 接口只认 Cloudflare 和 hCaptcha 的 Token，你无法直接把阿里云的 Token 传进去。

如果你决定切换到阿里云，我们需要彻底重构登录流程，架构如下：

1. 前端改造 ( Login.svelte ) :

   - 移除 Turnstile 代码，换成阿里云验证码 SDK。
   - 不再调用 supabase.auth.signUp 。
   - 改为调用 一个自定义的 Supabase Edge Function（例如 rpc/login_with_aliyun ）。
2. 后端开发 (Supabase Edge Function) :

   - 你需要创建一个 Edge Function（类似后端 API）。
   - 这个 Function 接收 email , password , 和阿里云的 verify_token 。
   - 第一步 ：服务器端调用阿里云 API 验证 Token 是否有效。
   - 第二步 ：如果验证通过，使用 Supabase Admin 权限 ( service_role key) 帮用户创建账户或登录。
   - 第三步 ：把登录后的 Session 返回给前端。

### 建议

建议先试用 Cloudflare Turnstile。 Cloudflare Turnstile 在中国大陆通常是可以正常使用的（虽然速度不如阿里云）。鉴于 Supabase 对它的原生支持非常完美，能为你节省大量的后端开发和维护工作。

只有当你发现大量国内用户无法加载验证码时，再考虑切换到阿里云验证码 + Edge Function 的方案。

​```




### capjs.js.org 开源方案

https://github.com/tiagozip/cap

- https://juejin.cn/post/7515072021506293795  基于PoW的Cap验证码

https://www.v2ex.com/t/1149062 

- ```
  
  不太懂，验证几乎无交互，真的能完全阻止机器人吗？ 阻止机器人做什么行为？
  由于 pow ，单一用户无法短时间内多次频繁通过验证，但是多个不同用户是不是可以慢慢通过验证？
  
  无论是什么样的验证码都无法 100%阻止所有机器人，而是增加其操作成本。虽然验证本身无交互，但通过 PoW （工作量证明）机制，可以限制单个用户高频请求；多个不同用户确实可以慢慢通过，但只要你设置足够的难度，就能有效防止批量滥用，比如刷接口、薅羊毛、撞库等。本质上就是一种手段通过提高操作成本（ PoW 计算需要时间）来放慢访问的速度，实现类似于速率限制，防止 DDOS 的效果
  
​```

```





### 邮箱验证

```

http://43.153.153.16:8000/project/default/auth/

Configuration 下面只有 Policies 

在Dashboard侧边栏单击Authentication -> Emails
	# 目标是让 AI 给加上这里的 EMails


```



### 树形目录的设计

```

Supabase 里如果要存树形目录结构的数据，要怎样设计更合理？前端拿到数据自已组装成树形结构，还是 Supabase 直接返回结构化的 JSON

在 Supabase (PostgreSQL) 中设计树形结构，最推荐且最灵活的方案是 Adjacency List (邻接表) 模式，即在表中添加 parent_id 字段。

关于“前端组装 vs 后端直接返回”，通常建议 前端组装，除非数据量巨大。

以下是详细的设计建议和对比：

1. 数据库设计方案 (推荐 Adjacency List)
这是最标准的设计，利用 Postgres 强大的递归查询能力。

SQL



create table categories (  id bigint generated by default as identity primary key,  parent_id bigint references categories(id), -- 指向父节点  name text not null,  created_at timestamp with time zone default timezone('utc'::text, now()) not null);-- 可选：添加索引以加速查询create index idx_categories_parent_id on categories(parent_id);
备选方案：ltree 扩展 如果你需要频繁查询“某个节点下的所有子孙节点”（不仅仅是直接子节点），Postgres 的 ltree 扩展非常强大，但学习曲线稍高。对于大多数应用，parent_id 足够了。

2. 数据获取策略对比
方案 A：后端返回扁平数据，前端组装 (最推荐)
Supabase 直接返回所有节点（或按需筛选），前端将其转换为树。

优点：
数据库负载低：SQL 查询非常简单 (select * from categories).
类型安全：Supabase 生成的 TypeScript 类型直接对应扁平结构，易于处理。
灵活性：前端可以根据 UI 需求（如 Antd Tree, dnd-kit）自由转换结构。
缓存友好：扁平列表更容易缓存和更新（增删改只需操作单个条目）。
缺点：
如果数据量达到数万条，前端处理可能会有微小的性能损耗（但在现代浏览器中通常忽略不计）。
前端组装代码示例 (TypeScript):

TypeScript



// 1. 从 Supabase 获取扁平数据const { data: categories } = await supabase.from('categories').select('*');// 2. 转换工具函数function buildTree(items: any[]) {  const map = new Map();  const roots: any[] = [];  // 初始化 Map，并在每个 item 上加个 children 数组  items.forEach(item => {    map.set(item.id, { ...item, children: [] });  });  items.forEach(item => {    if (item.parent_id) {      // 如果有父节点，在这个父节点的 children 里加入当前节点      const parent = map.get(item.parent_id);      if (parent) {        parent.children.push(map.get(item.id));      }    } else {      // 没有 parent_id，则是根节点      roots.push(map.get(item.id));    }  });  return roots;}const treeData = buildTree(categories || []);
方案 B：Supabase 直接返回嵌套 JSON (Postgres 侧组装)
利用 Postgres 的 json_agg 或递归 CTE，在数据库层完成组装。

优点：
前端拿到即用，逻辑简单。
节省带宽（如果只需要树的一部分）。
缺点：
SQL 复杂：需要编写复杂的 Postgres Function 或 View。
性能隐患：随着深度增加，数据库计算压力变大。
类型定义麻烦：Supabase 自动生成的类型通常是扁平的，你需要手动定义递归类型。
后端组装代码示例 (RPC Function):

如果你坚持要后端返回，可以创建一个 Postgres Function：

SQL

create or replace function get_category_tree()returns jsonlanguage sqlas $$with recursive tree_path as (    -- 1. 基础情况：获取根节点    select         id,         parent_id,         name,         jsonb_build_object('id', id, 'name', name, 'children', '[]'::jsonb) as         node_json    from categories    where parent_id is null        union all        -- 2. 递归部分：获取子节点    select         c.id,         c.parent_id,         c.name,         jsonb_build_object('id', c.id, 'name', c.name, 'children', '[]'::jsonb)    from categories c    join tree_path tp on c.parent_id = tp.id)-- 注意：纯 SQL 递归组装成嵌套 JSON 非常繁琐，通常建议只用递归查出路径，或者如下简单聚合：-- 实际上在 SQL 里做 "无限层级嵌套 JSON" 极其痛苦且性能差。-- 通常我们只用 Postgres 做 "有限层级" (比如关联查询) 的嵌套。$$;
(注：Postgres 并不擅长直接输出无限递归的 JSON 结构，写起来非常晦涩。通常所谓的“后端返回结构化”是指固定层级的 select *, children:categories(...)，这在 Supabase 中通过外键容易实现，但仅限固定层数。)

总结建议
首选方案：数据库存 parent_id，API 返回 扁平数组，前端组装。这是现代 SPA 应用的标准做法。
特殊情况：如果树非常深且庞大（如文件系统，数百万节点），不要一次性加载。改为 懒加载 (Lazy Load)：
点击父节点时，请求 supabase.from('categories').select('*').eq('parent_id', nodeId)。






用 Supabase Edge Functions 完成目录组装可行吗？

使用 Supabase Edge Functions 完成目录组装是 完全可行且非常合理 的方案。

这实际上是一个“黄金中间地带”：它结合了 SQL 查询的高效（直接 select * ）和 JavaScript/TypeScript 处理复杂逻辑的灵活性（组装树），同时避免了在数据库中写复杂递归 SQL 的痛苦。

### 核心优势
1. 多端逻辑复用 ：如果你有 Web、iOS、Android 多个端，不需要在每个端都写一遍“组装树”的算法，逻辑统一维护在 Edge Function 里。
2. 比 SQL 更容易维护 ：用 TS 写递归或循环组装 JSON 比写 Postgres 的递归 CTE 要直观得多，调试也方便。
3. 减轻客户端负担 ：虽然组装树的计算量通常不大，但如果数据结构复杂（比如还需要做权限过滤、字段裁剪），放在服务端处理更干净。
### 实现代码示例
假设你已经初始化了 Supabase Edge Function (例如名为 get-categories-tree )。

文件: supabase/functions/get-categories-tree/index.ts

​```
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

// 定义数据类型
interface Category {
  id: number
  parent_id: number | null
  name: string
  children?: Category[]
}

// 核心组装函数 (时间复杂度 O(n))
function buildTree(items: Category[]) {
  const map = new Map<number, Category>()
  const roots: Category[] = []

  // 1. 初始化所有节点，建立 id -> node 的映射
  items.forEach(item => {
    // 浅拷贝对象，并初始化 children
    map.set(item.id, { ...item, children: [] })
  })

  // 2. 组装树
  items.forEach(item => {
    const node = map.get(item.id)!
    
    if (item.parent_id) {
      const parent = map.get(item.parent_id)
      if (parent) {
        // 如果有父节点，加入父节点的 children
        parent.children!.push(node)
      } else {
        // 边缘情况：如果父节点 ID 存在但找不到父节点数据（比如父节点被删了），
        // 视具体业务决定是丢弃还是作为根节点。这里暂作根节点处理或忽略。
        console.warn(`Orphan node found: ${item.id}`)
      }
    } else {
      // 没有 parent_id，则是根节点
      roots.push(node)
    }
  })

  return roots
}

serve(async (req) => {
  try {
    // 1. 创建 Supabase Client (使用 Service Role Key 绕过 RLS，或者使用 Anon Key 配合 
    RLS)
    // 通常读取公开目录用 Anon Key 即可；如果是私有目录，需传递用户 Auth Header
    const authHeader = req.headers.get('Authorization')!
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_ANON_KEY') ?? '',
      { global: { headers: { Authorization: authHeader } } }
    )

    // 2. 从数据库获取扁平数据
    // 这里只取需要的字段，减少传输体积
    const { data: categories, error } = await supabase
      .from('categories')
      .select('id, parent_id, name')
      .order('id') // 排序通常对树的顺序也很重要

    if (error) throw error

    // 3. 在 Edge Function 内存中组装树
    const treeData = buildTree(categories as Category[])

    // 4. 返回组装好的 JSON
    return new Response(JSON.stringify(treeData), {
      headers: { 
        "Content-Type": "application/json",
        // 可选：添加缓存控制，比如缓存 60 秒
        "Cache-Control": "public, max-age=60, s-maxage=60" 
      },
      status: 200,
    })

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { "Content-Type": "application/json" },
      status: 500,
    })
  }
})
​```
### 最佳实践建议
1. 利用缓存 (Cache-Control) ：
   目录结构通常不会频繁变化。Edge Functions 部署在全球边缘节点，你可以通过设置响应头 "Cache-Control": "public, max-age=300" 让 CDN 缓存结果 5 分钟。这样后续的请求直接从最近的 CDN 节点返回，速度极快，且不消耗数据库资源。
2. 处理大量数据 ：
   Edge Functions 有内存限制（通常 128MB - 1GB 视套餐而定）。如果你的目录节点有几十万条，一次性加载进内存组装可能会 OOM (Out Of Memory)。
   
   - 几千条以内 ：毫无压力，上述代码即可。
   - 几万条以上 ：建议改回“前端组装”或“懒加载”（只请求某一层级的数据）。
3. 安全性 (RLS) ：
   在代码中，我使用了 req.headers.get('Authorization') 来透传用户的 Token。这很重要，这样 Supabase Client 在查询数据库时，依然会遵守你在数据库层设置的 RLS (Row Level Security) 规则。如果每个用户看到的目录树不同，这一点至关重要。




```





### PG

https://pigsty.cc/docs/setup/pgsql/

```

p
	# 指向了 psql


默认 单机安装 模板下，您将在当前节点上创建一个名为 pg-meta 的 PostgreSQL 数据库集群，只有一个主库实例。

PostgreSQL 监听在 5432 端口，集群中带有一个预置的数据库 meta 可供使用。

您可以在安装完毕后退出当前管理用户 ssh 会话，并重新登陆刷新环境变量后， 通过简单地敲一个 p 回车，通过命令行工具 psql 访问该数据库集群：

vagrant@pg-meta-1:~$ p
psql (18.1 (Ubuntu 18.1-1.pgdg24.04+2))
Type "help" for help.

postgres=#
您也可以切换为操作系统的 postgres 用户，直接执行 psql 命令，即可连接到默认的 postgres 管理数据库上。

连接数据库
想要访问 PostgreSQL 数据库，您需要使用 命令行工具 或者 图形化客户端 工具，填入 PostgreSQL 的 连接字符串：

psql postgres://dbuser_dba:DBUser.DBA@10.10.10.10/meta



在部署了 Pigsty 的服务器上，你可以直接使用 psql 连接本地数据库：

# 最简单的方式：使用 postgres 系统用户本地连接（无需密码）
sudo -u postgres psql

# 使用连接字符串（推荐，通用性最好）
psql 'postgres://dbuser_dba:DBUser.DBA@10.10.10.10:5432/meta'

# 使用参数形式
psql -h 10.10.10.10 -p 5432 -U dbuser_dba -d meta

# 使用环境变量避免密码出现在命令行
export PGPASSWORD='DBUser.DBA'
psql -h 10.10.10.10 -p 5432 -U dbuser_dba -d meta
成功连接后，你会看到类似这样的提示符：

psql (18.1)
Type "help" for help.

meta=#

```







### 自建论坛

```

使用 sveltejs 和 Supabase 开发一个论坛网站。 `
                  http://xx.xx.xx.xx:8000/
                  ` 这是自建 Supabase 的地址， ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzY3ODAxNjAwLCJleHAiOjE5MjU1NjgwMDB9.GtkruGMgbxm3kS_1eIHKyz0uaVjhvlWLvqUuS5b-DRc

npm install pg dotenv




node -v && npm -v
v24.12.0
11.6.2

npm create svelte@latest . -- --template skeleton --types ts --no-prettier --no-eslint --no-playwright --no-vitest

npx sv create . --template skeleton --types ts --no-prettier --no-eslint --no-playwright --no-vitest

npx sv create . --template minimal --types ts --no-add-ons --no-install

npm install && npm install @supabase/supabase-js




```







#### 集群中建数据库

https://pigsty.cc/docs/pgsql/config/db/

```

下面是 Pigsty 演示环境中默认集群 pg-meta 中的数据库定义：

pg-meta:
  hosts: { 10.10.10.10: { pg_seq: 1, pg_role: primary } }
  vars:
    pg_cluster: pg-meta
    pg_databases:
      - { name: meta ,baseline: cmdb.sql ,comment: pigsty meta database ,schemas: [pigsty] ,extensions: [{name: postgis, schema: public}, {name: timescaledb}]}
      - { name: grafana  ,owner: dbuser_grafana  ,revokeconn: true ,comment: grafana primary database }
      - { name: bytebase ,owner: dbuser_bytebase ,revokeconn: true ,comment: bytebase primary database }
      - { name: kong     ,owner: dbuser_kong     ,revokeconn: true ,comment: kong the api gateway database }
      - { name: gitea    ,owner: dbuser_gitea    ,revokeconn: true ,comment: gitea meta database }
      - { name: wiki     ,owner: dbuser_wiki     ,revokeconn: true ,comment: wiki meta database }
      - { name: noco     ,owner: dbuser_noco     ,revokeconn: true ,comment: nocodb database }
      
      
      
每个数据库定义都是一个 object，可能包括以下字段，以 meta 数据库为例：

- name: meta                      # 必选，`name` 是数据库定义的唯一必选字段
  state: create                   # 可选，数据库状态：create（创建，默认）、absent（删除）、recreate（重建）
  baseline: cmdb.sql              # 可选，数据库 sql 的基线定义文件路径（ansible 搜索路径中的相对路径，如 files/）
  pgbouncer: true                 # 可选，是否将此数据库添加到 pgbouncer 数据库列表？默认为 true
  schemas: [pigsty]               # 可选，要创建的附加模式，由模式名称字符串组成的数组
  extensions:                     # 可选，要安装的附加扩展： 扩展对象的数组
    - { name: postgis , schema: public }  # 可以指定将扩展安装到某个模式中，也可以不指定（不指定则安装到 search_path 首位模式中）
    - { name: timescaledb }               # 例如有的扩展会创建并使用固定的模式，就不需要指定模式。
  comment: pigsty meta database   # 可选，数据库的说明与备注信息
  owner: postgres                 # 可选，数据库所有者，不指定则为当前用户
  template: template1             # 可选，要使用的模板，默认为 template1，目标必须是一个模板数据库
  strategy: FILE_COPY             # 可选，克隆策略：FILE_COPY 或 WAL_LOG（PG15+），不指定使用 PG 默认
  encoding: UTF8                  # 可选，不指定则继承模板/集群配置（UTF8）
  locale: C                       # 可选，不指定则继承模板/集群配置（C）
  lc_collate: C                   # 可选，不指定则继承模板/集群配置（C）
  lc_ctype: C                     # 可选，不指定则继承模板/集群配置（C）
  locale_provider: libc           # 可选，本地化提供者：libc、icu、builtin（PG15+）
  icu_locale: en-US               # 可选，ICU 本地化规则（PG15+）
  icu_rules: ''                   # 可选，ICU 排序规则（PG16+）
  builtin_locale: C.UTF-8         # 可选，内置本地化提供者规则（PG17+）
  tablespace: pg_default          # 可选，默认表空间，默认为 'pg_default'
  is_template: false              # 可选，是否标记为模板数据库，允许任何有 CREATEDB 权限的用户克隆
  allowconn: true                 # 可选，是否允许连接，默认为 true。显式设置 false 将完全禁止连接到此数据库
  revokeconn: false               # 可选，撤销公共连接权限。默认为 false，设置为 true 时，属主和管理员之外用户的 CONNECT 权限会被回收
  register_datasource: true       # 可选，是否将此数据库注册到 grafana 数据源？默认为 true，显式设置为 false 会跳过注册
  connlimit: -1                   # 可选，数据库连接限制，默认为 -1 ，不限制，设置为正整数则会限制连接数。
  parameters:                     # 可选，数据库级参数，通过 ALTER DATABASE SET 设置
    work_mem: '64MB'
    statement_timeout: '30s'
  pool_auth_user: dbuser_meta     # 可选，连接到此 pgbouncer 数据库的所有连接都将使用此用户进行验证（启用 pgbouncer_auth_query 才有用）
  pool_mode: transaction          # 可选，数据库级别的 pgbouncer 池化模式，默认为 transaction
  pool_size: 64                   # 可选，数据库级别的 pgbouncer 默认池子大小，默认为 64
  pool_reserve: 32                # 可选，数据库级别的 pgbouncer 池子保留空间，默认为 32，当默认池子不够用时，最多再申请这么多条突发连接。
  pool_size_min: 0                # 可选，数据库级别的 pgbouncer 池的最小大小，默认为 0
  pool_connlimit: 100             # 可选，数据库级别的最大数据库连接数，默认为 100
唯一必选的字段是 name，它应该是当前 PostgreSQL 集群中有效且唯一的数据库名称，其他参数都有合理的默认值。      
      
    

```



#### admin 用户组

```

sudo usermod -aG admin <username>

```



#### 磁盘写满了如何抢救



```

如果磁盘写满了，连 Shell 命令都无法执行，rm -rf /pg/dummy 可以释放一些救命空间。

默认情况下，pg_dummy_filesize 设置为 64MB。在生产环境中，建议将其增加到 8GB 或更大。

它将被放置在 PGSQL 主数据磁盘上的 /pg/dummy 路径下。你可以删除该文件以释放一些紧急空间：至少可以让你在该节点上运行一些 shell 脚本来进一步回收其他空间。

```





### Supabase 执行 SQL

http://xx.xx.xx.xx:8000/project/default/sql/1

```

select * from
  (select version()) as version,
  (select current_setting('server_version_num')) as version_number;
  	# SQL Editor 里成功执行

```



```
postgres://dbuser_dba:DBUser.DBA@10.7.0.9:5432/meta
postgres://dbuser_meta:DBUser.Meta@10.7.0.9:5432/meta
postgres://dbuser_view:DBUser.View@10.7.0.9:5432/meta
	# 使用三个不同的用户连接到 pg-meta 集群的 meta 数据库
	# https://pigsty.cc/docs/setup/pgsql/
		psql -h 10.7.0.9 -p 5432 -U dbuser_dba -d meta
			export PGPASSWORD='DBUser.DBA'
			psql -h 10.7.0.9 -p 5432 -U dbuser_dba -d meta

psql postgres://dbuser_dba:DBUser.DBA@10.7.0.9:5432/meta
  -> error: connection to server at "10.7.0.9", port 5432 failed: FATAL:  database "meta" does not exist
	# 出错：没有 meta 这个数据库，数据源 pg-meta 是有的
	
psql postgres://dbuser_dba:DBUser.DBA@10.7.0.9:5432/postgres
	# 成功
	
psql postgres://dbuser_dba:DBUser.DBA@10.7.0.9:5433/meta
	
@pg-meta:5433/meta

psql postgres://dbuser_meta:DBUser.Meta@10.7.0.9:5433/meta
			
```





psql postgres://dbuser_dba:DBUser.DBA@10.10.10.10/meta



### 单节点开发箱（meta）

https://pigsty.cc/docs/deploy/sandbox/

**Grafana**

Pigsty [**`INFRA`**](https://pigsty.cc/docs/infra) 模块中自带了 [**Grafana**](https://pigsty.cc/docs/infra)，并预先配置好了 PostgreSQL 数据源（Meta）。 您可以直接通过 [**浏览器图形界面**](https://pigsty.cc/docs/setup/webui)，从 Grafana Explore 面板中使用 SQL 查询数据库，无需额外安装客户端工具。

Grafana 默认的用户名是 **`admin`**，密码可以在 [**配置清单**](https://pigsty.cc/docs/concept/iac/inventory) 中的 [**`grafana_admin_password`**](https://pigsty.cc/docs/infra/param#grafana_admin_password) 字段找到（默认 `pigsty`）。



Grafana Web GUI 

xx.xx.xx.xx:3000/login admin pigsty

点开 Dashboards -> PGSQL -> Database **可以看到数据源 pg-meta**



```

`f:\t\pigsty\Makefile` ubuntu22.04 执行命令出错，修复它：# make meta
./configure -s -c meta
configure pigsty v3.7.0 begin
[ OK ] region = default
[ OK ] kernel  = Linux
[ OK ] machine = x86_64
[ OK ] package = deb,apt
[ OK ] vendor  = ubuntu (Ubuntu)
[ OK ] version = 24 (24.04)
[ OK ] sudo = root ok
[ OK ] ssh = root@127.0.0.1 ok
[ OK ] primary_ip = skip
[ OK ] admin ssh = skip checking (due to --skip)
[ OK ] mode = meta (manually set)
[ OK ] skip ip replacement (due to --skip)
[WARN] replace oltp template with tiny due to cpu < 4
[ OK ] locale  = C.UTF-8
[ OK ] ansible = ready
[ OK ] pigsty configured
[WARN] don't forget to check it and change passwords!
proceed with ./install.yml 
cd vagrant && vagrant destroy -f
A Vagrant environment or target machine is required to run this
command. Run `vagrant init` to create a new Vagrant environment. Or,
get an ID of a target machine from `vagrant global-status` to run
this command on. A final option is to change to a directory with a
Vagrantfile and to try again.
make: *** [Makefile:259: del] Error


vi Makefile
del:
	# 209 行 cd vagrant && vagrant destroy -f
	cd vagrant && if [ -f Vagrantfile ]; then vagrant destroy -f; fi
		# 改成这个

del-test:
	# 271 行 cd vagrant && vagrant destroy -f node-1 node-2 node-3
	cd vagrant && if [ -f Vagrantfile ]; then vagrant destroy -f node-1 node-2 node-3; fi
		# 改成这个
		
后面 make meta 报错是因为 qemu 没有装得上

apt install qemu-system qemu-utils -y \
  && apt install libvirt-daemon-system libvirt-clients bridge-utils virt-manager -y
  
# kvm-ok
INFO: Your CPU does not support KVM extensions
KVM acceleration can NOT be used

# qemu-system-x86_64 --version
QEMU emulator version 8.2.2 (Debian 1:8.2.2+ds-0ubuntu1.11)
Copyright (c) 2003-2023 Fabrice Bellard and the QEMU Project developers

systemctl status libvirtd


cat /proc/cpuinfo
	# 这台 tencent 轻量主机不支持CPU硬件虚拟化
	# 1. 改用支持嵌套虚拟化的 CVM 实例（如标准型 S5、计算型 C5 等），并在控制台提交工单申请开启嵌套虚拟化。
      2.直接使用容器方案（Docker/LXD）替代传统虚拟机，轻量应用服务器已预装 Docker 环境，可运行容器实现隔离。
  


vi pigsty/vagrant/Vagrantfile.libvirt
  line 40 行增加：
                if !File.exist?('/dev/kvm')
                  v.driver = 'qemu'
                end

# 设置环境变量强制使用 libvirt 模板（包含刚才的修复）
export VM_PROVIDER=libvirt
make meta
	# 执行 make meta 时生成的 Vagrantfile 就会包含 driver = 'qemu' 配置，从而避开 "could not get preferred machine ... type=kvm" 的错误。
	
	
cd vagrant && vagrant destroy -f
export VM_PROVIDER=libvirt; make meta
  ==> meta: Waiting for domain to get an IP address...
		# 一直卡在这里

vagrant status; virsh list --all
vagrant ssh
touch /root/.ssh/config
make ssh
        (TraeAI-5) ~/pigsty [0] $ make ssh
        vagrant/ssh

        Vagrant nodes:

        10.10.10.10      meta



        cd /root/pigsty/vagrant && vagrant ssh-config
        this may take several seconds....
        [fog][WARNING] Unrecognized arguments: libvirt_ip_command
        # ssh access via nodename


        Host meta
          HostName 192.168.121.114
          User vagrant
          Port 22
          UserKnownHostsFile /dev/null
          StrictHostKeyChecking no
          PasswordAuthentication no
          IdentityFile /root/.vagrant.d/insecure_private_keys/vagrant.key.ed25519
          IdentityFile /root/.vagrant.d/insecure_private_keys/vagrant.key.rsa
          IdentitiesOnly yes
          LogLevel FATAL
          PubkeyAcceptedKeyTypes +ssh-rsa
          HostKeyAlgorithms +ssh-rsa




        # SSH Access via IP address

        Host 10.10.10.10
          HostName 192.168.121.114
          User vagrant
          Port 22
          UserKnownHostsFile /dev/null
          StrictHostKeyChecking no
          PasswordAuthentication no
          IdentityFile /root/.vagrant.d/insecure_private_keys/vagrant.key.ed25519
          IdentityFile /root/.vagrant.d/insecure_private_keys/vagrant.key.rsa
          IdentitiesOnly yes
          LogLevel FATAL
          PubkeyAcceptedKeyTypes +ssh-rsa
          HostKeyAlgorithms +ssh-rsa


        write extra ssh config [pigsty] to /root/.ssh/pigsty_config
        write include pigsty command to ~/.ssh/config

ssh meta uptime


make meta 执行已完成，并修复了期间遇到的所有问题。以下是处理过程的详细说明：

1. 环境适配 (Fix KVM Error)
   
   - 问题 ：首次运行 make meta 失败，提示 Call to virDomainDefineXML failed ，原因是当前环境不支持 KVM 硬件虚拟化。
   - 解决 ：通过设置环境变量 VM_PROVIDER=libvirt 强制使用 libvirt 提供程序，并利用其 QEMU 软件模拟模式（Fallback）来绕过硬件限制。
2. 启动虚拟机 (Start VM)
   
   - 执行 ：运行 export VM_PROVIDER=libvirt; make meta 。
   - 结果 ：由于 QEMU 模拟模式较慢，脚本在等待获取 IP 地址时超时（Exit 130），但经检查虚拟机 meta 实际上已成功启动并运行。
   - 验证 ：通过 vagrant status 确认虚拟机状态为 running ，通过 vagrant ssh 确认可正常登录。
3. 配置 SSH (Fix SSH Config)
   
   - 问题 ：后续运行 make ssh 配置免密登录时失败，提示找不到 ~/.ssh/config 文件。
   - 解决 ：手动创建了该配置文件，并重新运行 make ssh 成功写入配置。
4. 最终验证 (Verification)
   
  - 现已可以通过 ssh meta 直接登录虚拟机，命令 ssh meta uptime 执行成功。
您可以直接使用 ssh meta 访问该节点。


cd ~/pigsty/vagrant \
  && vagrant halt
	 # 优雅关机
	 # 完全关闭，释放资源




云服务器内部支持创建KVM虚拟机，这项技术通常被称为虚拟化嵌套或嵌套虚拟化。简单来说，就是你可以在云服务器（它本身可能就是一台虚拟机）上再安装虚拟化软件，从而创建出“虚拟机中的虚拟机”

检查虚拟化支持：首先，通过命令（如 sudo kvm-ok或检查 /proc/cpuinfo中的 vmx（Intel）或 svm（AMD）标志）确认云服务器的CPU支持硬件虚拟化。
安装KVM及相关组件：使用系统包管理器（如APT）安装 qemu-kvm、libvirt-daemon-system、libvirt-clients、bridge-utils等软件包


apt-get purge vagrant-libvirt \
  && apt-get update \
  && apt-get install -y qemu libvirt-daemon-system ebtables libguestfs-tools vagrant ruby-fog-libvirt



wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list \
  && apt update && apt install vagrant
	# 先安装 vagrant
		# 是用来创建虚拟机的  


apt-get install libvirt-dev


cd ~/pigsty

make meta       # 创建单节点开发箱
	make dual       # 创建 2 节点环境
	make trio       # 创建 3 节点环境


make simu       # 创建 20 节点生产仿真环境
    该环境包含：

    3 个基础设施节点（meta1, meta2, meta3）
    2 个 HAProxy 代理节点
    4 个 MinIO 节点
    5 个 ETCD 节点
    6 个 PostgreSQL 节点（2 个集群，每个 3 节点）


```







### 本地 HyperV 装好再上传阿里云

```

see doc\lang\programming\linux\Alpine Summary.md -> 阿里云安装 alpine


HyperV 新建一个代次为Gen1的虚拟机，然后挂载.vhd的磁盘和 alpine-standard x64 iso 镜像开机进行安装

ubuntu-22.04.5-desktop-amd64.iso
	# 用这个镜像


# 通过正常安装流程进行联网、镜像源设置，随后终止安装流程
setup-alpine
# 安装分区工具
apk add parted e2fsprogs
# 进行分区
parted -sa optimal /dev/sda mklabel msdos # 设置分区表为mbr格式
parted -sa optimal /dev/sda mkpart primary 512B 50MB # 划分boot分区
parted -sa optimal /dev/sda mkpart primary 50MB 100% # 划分所有容量至主分区
parted -sa optimal /dev/sda set 1 boot # 设置分区1启动卷标
mkfs.ext4 /dev/sda1 # 格式化boot分区
mkfs.ext4 /dev/sda2 # 格式化主分区
# 重启
reboot
# 挂载磁盘，注意先后及新建文件夹
mount /dev/sda2 /mnt
mount /dev/sda1 /mnt/boot

# 通过正常安装流程进行所有设置，到选择磁盘后终止
setup-alpine

# 安装
setup-disk /mnt

  	# 实测这个 vhd 上传阿里自定义镜像后，正常开机使用
  	

```





### 阿里云海外装完再导出镜像



这种方案比较麻烦



```

方案一：使用自定义镜像下载到本地
如果您希望将整个系统“打包”带走，在本地虚拟机或其它云平台运行，此方案是标准做法。
操作流程概述：
创建自定义镜像：在ECS控制台，为您的Linux实例创建一个自定义镜像。这个过程会为实例的系统盘和数据盘生成快照，并封装成镜像。
导出镜像到OSS：将创建好的自定义镜像导出到您指定的对象存储OSS的Bucket中。
从OSS下载到本地：登录OSS控制台，找到导出的镜像文件（通常为.raw格式），并生成下载链接将其下载到您的本地电脑。
格式转换与导入：下载的RAW格式镜像可能需要使用像qemu-img这样的工具转换成您本地虚拟化平台（如VMware、VirtualBox）支持的格式（如VMDK），然后即可导入并启动

```





### Docker 里面安装

https://www.cherryservers.com/blog/install-docker-ubuntu

它的离线安装还是太复杂，失败主要是因为网络问题。先在国外主机 Docker 里安装好，再把镜像导出来就好了。



测试不可行



```

# Ubutnu 24.04 安装 Docker

cat /etc/os-release
	# 显示版本号

lsb_release -a
	# 应该是有小版本号的 Ubuntu 24.04 LTS 应该代表 24.04.0?

sudo passwd
	# 改 root 默认密码
	
su -
	# 切成 root

apt update \
  && apt upgrade -y \
  && apt-get install ca-certificates curl \
  && install -m 0755 -d /etc/apt/keyrings \
  && curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc \
 && chmod a+r /etc/apt/keyrings/docker.asc


echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update \
  && apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y


service docker start \
  && service docker status 


docker search ubuntu


docker pull ubuntu:22.04 \
  && docker images \
  && docker run -tid --name ubuntu2204_ENV -p 222:22 --privileged=true ubuntu:22.04 bash


docker exec -it ubuntu2204_ENV bash
	# 进入 docker
	
	exit \
	&& docker logs ubuntu2204_ENV
		--> 有错误会在这里显示



```





### 离线安装

https://pigsty.cc/docs/setup/offline/

https://help.aliyun.com/zh/terraform/what-is-terraform

- https://help.aliyun.com/zh/terraform/use-terraform-in-cloud-shell

推荐使用 Ubuntu 22.04 / 24.04 LTS

- Ubuntu 24.04 在系统可靠性/稳定性与软件版本的新颖性/齐全性上取得了良好的平衡，推荐使用此系统。



当您使用云服务器部署 Pigsty 时，可以考虑在 **Terraform** 中使用以下操作系统基础镜像



| **x86_64**   | 镜像                                           |
| :----------- | :--------------------------------------------- |
| Rocky 8.10   | `rockylinux_8_10_x64_20G_alibase_20240923.vhd` |
| Rocky 9.6    | `rockylinux_9_6_x64_20G_alibase_20250101.vhd`  |
| Rocky 10.0   | `rockylinux_10_0_x64_20G_alibase_20251120.vhd` |
| Ubuntu 22.04 | `ubuntu_22_04_x64_20G_alibase_20240926.vhd`    |
| Ubuntu 24.04 | `ubuntu_24_04_x64_20G_alibase_20240923.vhd`    |
| Debian 12.11 | `debian_12_11_x64_20G_alibase_20241201.vhd`    |
| Debian 13.2  | `debian_13_x64_20G_alibase_20250101.vhd`       |



https://shell.aliyun.com/  

- 阿里云Cloud Shell是一款帮助您运维的免费产品，预装了Terraform的组件

- 建议您使用RAM用户登录，为确保您的阿里云账号的安全，如非必要，避免使用阿里云账号访问云资源。



```shell

terraform version
	# 查看 Terrafrom版本
	--> Terraform v0.12.31
	
tfenv list
  1.9.5
  1.5.7
  1.3.7
  0.13.7
* 0.12.31

tfenv use 1.9.5
	# 切换到 1.9.5 版本
	



```



### pg_graphql

https://github.com/supabase/pg_graphql

```



```



## NHost

https://github.com/nhost/nhost  Nhost is 100% open source





## Antigravity

Antigravity 需要在您的系统上本地安装。该产品适用于 Mac、Windows 和特定 Linux 发行版。除了您自己的机器之外，您还需要以下设备：

- Chrome 网络浏览器
- Gmail 账号（个人 Gmail 账号）。



C:\Users\Administrator\AppData\Local\Programs\Antigravity





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



## navicat 备份数据库

```
Navicat for PostgreSQL版本链接工具，专门为PostgreSQL定制使用，功能十分强大！
步骤：
1、工具-数据传输
2、源， 选择连接/数据库/模式 ，目标中可以选择直接连接的库，或者文件选择文件
3、下一步
4、数据库对象选择 全部 表/视图/函数/序列/类型
5、点击选项，配置详细参数
6、导出即可！
```



### 查看表大小

```
select pg_size_pretty(pg_relation_size('nlpp_vector')) as size;
 	# 单个表
select pg_size_pretty(pg_total_relation_size('nlpp_vector')) as size;
  	# 单个表包含索引大小
  	
select pg_size_pretty(pg_database_size('nlppvector')) as size;
	# 单个库大小

```



### 导出整个 PostgreSQL 实例

```
如果需要导出整个 PostgreSQL 实例并保留所有插件的声明，使用 pg_dumpall：
pg_dumpall -U postgres > /root/backup.sql
pg_dumpall 会包含所有用户、角色、权限以及 CREATE EXTENSION 命令。


psql -U 用户名 -d 数据库名 -f /path/to/backup.sql
	# 恢复

因为导出的 .sql 文件已经包括了 CREATE DATABASE 语句，当你导入时，备份会自动创建新数据库，所以 不需要手动创建一个空数据库。

pg_dumpall需要多次连接到PostgreSQL服务器（每个数据库一次）。如果您使用密码身份验证，它将每次都要求输入密码。~/.pgpass

```





## 重建数据库和表结构

```

navicat 备份数据库，然后再重建数据库和表结构（注意：id 字段不要导出）

还原数据库
  su postgres
  cd ~
    # /var/lib/pgsql 它的主目录是这里，先把备份好的数据库传到这里来  
    # F:\数据库备份\anime\japanese\Touch\Touch.sql
  cd /mnt/数据库备份/anime/japanese/Touch
  psql -d anime -U postgres -f Touch.sql

-- 在 postgres 数据库里运行
CREATE DATABASE anime
    WITH OWNER = postgres 
    ENCODING = 'UTF8' 
    TABLESPACE = pg_default 
    CONNECTION LIMIT = -1 
    TEMPLATE template0;


-- 在 anime 数据库里运行
create extension IF NOT EXISTS tsm_system_rows;
create extension IF NOT EXISTS tsm_system_time;
CREATE EXTENSION IF NOT EXISTS rum;
CREATE TABLE IF NOT EXISTS japanese (
        id integer primary key generated always as identity,
        gid text NOT NULL,
        pid text DEFAULT '' NOT NULL,
        name text,  
        jp text DEFAULT '' NOT NULL, 
        ch text DEFAULT '' NOT NULL, 
        en text DEFAULT '' NOT NULL, 
        kr text DEFAULT '' NOT NULL,
        ru text DEFAULT '' NOT NULL,
        fr text DEFAULT '' NOT NULL,
        de text DEFAULT '' NOT NULL,
        sp text DEFAULT '' NOT NULL,
        hi text DEFAULT '' NOT NULL,
        origin text CHECK (origin IN ('jp', 'ch', 'en', 'kr', 'ru', 'fr', 'de', 'sp', 'hi')),
        langs text DEFAULT '' NOT NULL,
        type text,
        begintime text,
        endtime text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector,
        v_ch  tsvector, 
        v_en  tsvector,
        v_kr  tsvector,
        v_ru  tsvector,
        v_fr  tsvector,
        v_de  tsvector,
        v_sp  tsvector,
        v_hi  tsvector,
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode integer NOT NULL,
        audio bytea DEFAULT NULL, 
        image bytea DEFAULT NULL, 
        video bytea DEFAULT NULL,
        videoname text,
        CONSTRAINT unique_index_gid unique (gid)
      );

      CREATE INDEX IF NOT EXISTS index_rum_jp ON japanese USING rum (v_jp rum_tsvector_ops);
      CREATE INDEX IF NOT EXISTS index_rum_kr ON japanese USING rum (v_kr rum_tsvector_ops);
      CREATE INDEX IF NOT EXISTS index_rum_ch ON japanese USING rum (v_ch rum_tsvector_ops);
      CREATE INDEX IF NOT EXISTS index_rum_en ON japanese USING rum (v_en rum_tsvector_ops);
      

      CREATE INDEX IF NOT EXISTS japanese_gid_index ON japanese (gid);
      CREATE INDEX IF NOT EXISTS japanese_pid_index ON japanese (pid);
      CREATE INDEX IF NOT EXISTS japanese_name_index ON japanese (name);
      CREATE INDEX IF NOT EXISTS japanese_episode_index ON japanese (episode);
      CREATE INDEX IF NOT EXISTS japanese_origin_index ON japanese (origin);
      CREATE INDEX IF NOT EXISTS japanese_langs_index ON japanese (langs);

```







## 备份表



```
PGPASSWORD="post4321" pg_dump -h 127.0.0.1 -U postgres -p 5432 -d nlppvector -t public.nlpp_vector --inserts | gzip -9 > /root/nlppvector_$(date +%Y-%m-%d).psql.gz
```





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



## openai embedding

```

# see huggingface/project/向量查询问题.txt

https://github.com/asg017/sqlite-vec
	# sqlie 向量插件

/*


text-embedding-3-small	1536    $0.020 / 1M tokens      $0.010 / 1M tokens
text-embedding-3-large  3072    $0.130 / 1M tokens      $0.065 / 1M tokens     
    # 后面是批处理接口的价格


https://platform.openai.com/docs/guides/batch
    # 批处理更便宜些


// https://github.com/pgvector/pgvector 先安装
// yum install pgvector_17 -y

CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS test_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    AppID integer NOT NULL,
    TestID integer NOT NULL,
    ChildTableID integer NOT NULL,
    TestCptID integer DEFAULT -1,
    OperateTime timestamp NOT NULL,
    S_Test text NOT NULL,
    V_Test vector(1536) NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    AddUserID integer DEFAULT -1,
    UpdateUserID integer DEFAULT -1,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (AppID, TestID, ChildTableID) 
);
CREATE INDEX IF NOT EXISTS idx_appid ON test_vector (AppID);
CREATE INDEX IF NOT EXISTS idx_appid_cptid ON test_vector (AppID, TestCptID);
CREATE INDEX ON test_vector USING hnsw (V_Test vector_cosine_ops);

*/



cat /etc/redhat-release

AlmaLinux release 9.3 (Shamrock Pampas Cat)


# Install the repository RPM:
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Disable the built-in PostgreSQL module:
sudo dnf -qy module disable postgresql

# Install PostgreSQL:
sudo dnf install -y postgresql17-server

# Optionally initialize the database and enable automatic start:
sudo /usr/pgsql-17/bin/postgresql-17-setup initdb
sudo systemctl enable postgresql-17
sudo systemctl start postgresql-17


sudo -u postgres psql
select version();
\password postgres  # 修改密码
\q

postgres 	post4321
	# 用户名 密码

psql -h 127.0.0.1 -p 5432 -U postgres
	# 成功登录

mkdir /home/psqldata

chown -R postgres:postgres /home/psqldata



 systemctl stop postgresql-17

cp -R /var/lib/pgsql/17/data /home/psqldata   # 只能透亮换柱了

mv /var/lib/pgsql/17/data /var/lib/pgsql/17/data__link__to_home_psqldata

ln -s  /home/psqldata/data  /var/lib/pgsql/17/data
			# unlink 取消软链用这个

chown -R postgres:postgres /home/psqldata



systemctl start postgresql-17

systemctl status postgresql-17



# 允许运程连接
vi /var/lib/pgsql/17/data/postgresql.conf
	listen_addresses = '*' # 改成这个
vi /var/lib/pgsql/17/data/pg_hba.conf
hostnossl    all          all            0.0.0.0/0  md5  
	# hostnossl    all          all            0.0.0.0/0  trust  # 任何密码都能连
	# 加在最后面，接受所有远程IP


systemctl restart postgresql-17
systemctl status postgresql-17



yum groupinstall "Development Tools" && \
yum install llvm-toolset-7-clang && \
yum install postgresql17-devel && \
yum install postgresql17-contrib && \
yum install systemtap-sdt-devel


git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-17/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install

make USE_PGXS=1 installcheck && \
psql DB -c "CREATE EXTENSION rum;"



yum install pgvector_17 -y
	# https://github.com/pgvector/pgvector 先安装

CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS test_vector (
    ID integer generated always as identity,
    AppID integer NOT NULL,
    TestID integer NOT NULL,
    ChildTableID integer NOT NULL,
    TestCptID integer DEFAULT -1,
    S_Test text NOT NULL,
    V_Test vector(1536) NOT NULL,
    AddedTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    AddUserID integer DEFAULT -1,
    UpdateUserID integer DEFAULT -1,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (AppID, TestID, ChildTableID) 
);
CREATE INDEX IF NOT EXISTS idx_appid ON test_vector (AppID);
CREATE INDEX IF NOT EXISTS idx_appid_cptid ON test_vector (AppID, TestCptID);
CREATE INDEX ON test_vector USING hnsw (V_Test vector_cosine_ops);


(async () => {
  let bent = require('bent')
  let post = bent("http://xxxx:xxx", 'POST', 'json', 200)
  
  let response = await post('/embeddings', JSON.stringify({"sentence":"什么什么向量"}), { 'Content-Type': "application/json;chart-set:utf-8" })

  if (response.status == 0) {
      return [response.data, '']
  } else {
      return [null, response.msg]
  }
})()

```





## 向量查询

    # see huggingface/NLPP_vector_server/readme.txt
    https://github.com/lanterndata/lantern  
        # pg 支持 but up to 16
https://liaoxuefeng.com/blogs/all/2023-08-10-ai-search-engine-by-postgres/

```
其中，embedding <=> %s是pgvector按余弦距离查询的语法，值越小表示相似度越高，取相似度最高的3个文档。

用Python配合psycopg2查询代码如下：

def db_select_by_embedding(embedding: np.array):
    sql = 'SELECT id, name, content, embedding <=> %s AS distance FROM docs ORDER BY embedding <=> %s LIMIT 3'
    with db_conn() as conn:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        values = (embedding, embedding)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        cursor.close()
        return results
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



## 查所有数据库名

```
SELECT datname FROM pg_database;
postgres
template1
template0
	# 排除这三个系统库，剩下的就是要找的
```



## create datebase if not exist

```
CREATE EXTENSION IF NOT EXISTS dblink;
DO $$
BEGIN
PERFORM dblink_exec('', 'CREATE DATABASE tt WITH OWNER = postgres ENCODING = ''UTF8'' TABLESPACE = pg_default CONNECTION LIMIT = -1 TEMPLATE template0');
EXCEPTION WHEN duplicate_database THEN RAISE NOTICE '%, skipping', SQLERRM USING ERRCODE = SQLSTATE;
END
$$;
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



## vector

```
# see huggingface/NLPP_Audio/vector.py
# see nodejs summary.md -> proxynt
# see huggingface\powershell\readme.txt -> proxynt 

# http://xxx.57:7851/wsproxy/admin
#  ali57:2222 -> homepc_wsl2_ssh:22
#  ali57:54322 -> homepc_wsl2_ssh:5432
```



```
const { Pool } = require('pg');
config = require('../../../config.js')

const pool = new Pool(config.db_vector)

async function getVectorIDs(appID, testIDs, childTableIDs) {

    const client = await pool.connect()
    try {
        let sq = `
            SELECT appid, testid, childtableid, testcptid, TO_CHAR(operatetime, 'YYYY-MM-DD HH24:MI:SS') AS operatetime FROM test_vector 
            WHERE appid = ${appID} and enabled = 't';
        `
        if (testIDs.length > 0) {
            sq = `
                SELECT appid, testid, childtableid, testcptid, TO_CHAR(operatetime, 'YYYY-MM-DD HH24:MI:SS') AS operatetime FROM test_vector 
                WHERE appid = ${appID} and testid in (${ testIDs.join(',') }) and enabled = 't';
            `
        }

        if (testIDs.length > 0 && childTableIDs.length > 0) {
            sq = `
                SELECT appid, testid, childtableid, testcptid, TO_CHAR(operatetime, 'YYYY-MM-DD HH24:MI:SS') AS operatetime FROM test_vector 
                WHERE appid = ${appID} and testid in (${ testIDs.join(',') }) and childtableid in ( ${ childTableIDs.join(',') } ) and enabled = 't';
            `
        }

        const re = await client.query(sq, [])
        return [re.rows, ""]
    } catch (err) {
        let errmsg = `### 查询向量失败. appid: ${appID} ${err}`
        console.error(errmsg)
        return [null, errmsg]
    } finally {
        client.release()
    }
}

async function insertVectors(list) {
    
    const client = await pool.connect()

    let t = []
    for (let {appid, testid, childtableid, testcptid, operatetime, s_test, v_test, userid} of list) {
        t.push(`(${appid}, ${testid}, ${childtableid}, ${testcptid}, '${operatetime}', '${s_test}', '${v_test}', ${userid})`)
    }
    t = t.join(',\n')

    
    try {
      const queryText = `
      INSERT INTO test_vector (appid, testid, childtableid, testcptid, operatetime, s_test, v_test, adduserid) 
      VALUES 
        ${t}
      ON CONFLICT (appid, testid, childtableid)
      DO UPDATE SET s_test = EXCLUDED.s_test, v_test = EXCLUDED.v_test, updatetime=now(), updateuserid=EXCLUDED.adduserid, enabled='t';
      `;
      const re = await client.query(queryText, [])
      console.log(`Inserted vectors. appid: ${list[0].appid} rowCount: ${re.rowCount}`)
      return [re, ""]
    } catch (err) {
      let errmsg = `### 插入向量失败: ${err}`
      console.error(errmsg)
      return [null, errmsg]
    } finally {
      client.release()
    }
}

async function disableVectors(appID, testIDs) {
    const client = await pool.connect()
    try {
        const queryText = `
            UPDATE test_vector SET enabled = 'f' 
            WHERE appid = ${appID} and testid in (${ testIDs.join(',') });
        `;
        const re = await client.query(queryText, [])
        return [re, ""]
      } catch (err) {
        let errmsg = `### 禁用向量失败: ${err}`
        console.error(errmsg)
        return [null, errmsg]
      } finally {
        client.release()
      }
}
```



```

// https://github.com/pgvector/pgvector 先安装
// yum install pgvector_17 -y

CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS test_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    AppID integer NOT NULL,
    TestID integer NOT NULL,
    ChildTableID integer NOT NULL,
    TestCptID integer DEFAULT -1,
    OperateTime timestamp NOT NULL,
    S_Test text NOT NULL,
    V_Test vector(1536) NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    AddUserID integer DEFAULT -1,
    UpdateUserID integer DEFAULT -1,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (AppID, TestID, ChildTableID) 
);
CREATE INDEX IF NOT EXISTS idx_appid ON test_vector (AppID);
CREATE INDEX IF NOT EXISTS idx_appid_cptid ON test_vector (AppID, TestCptID);
CREATE INDEX ON test_vector USING hnsw (V_Test vector_cosine_ops);
```



### cosine_similarity

```
from openai.embeddings_utils import get_embedding, cosine_similarity

def search_reviews(df, product_description, n=3, pprint=True):
   embedding = get_embedding(product_description, model='text-embedding-3-small')
   df['similarities'] = df.ada_embedding.apply(lambda x: cosine_similarity(x, embedding))
   res = df.sort_values('similarities', ascending=False).head(n)
   return res

res = search_reviews(df, 'delicious beans', n=3)
```



## jsonb

### 联合索引

```
CREATE TABLE my_table (
    id serial PRIMARY KEY,
    category text,
    data jsonb
);

CREATE INDEX my_btree_index ON my_table (category, (data->>'key'));

CREATE INDEX ON my_table USING GIN ((data->'key')), category;

SELECT * FROM my_table WHERE category = 'some_category' AND data->>'key' = 'some_value';



```



```
-- 创建一个包含 jsonb 属性的节点
SELECT * 
FROM cypher('your_graph', $$
    CREATE (n:Person {name: 'Alice', attributes: '{"age": 30, "hobbies": ["reading", "hiking"]}'::jsonb})
$$) AS (a agtype);

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
    value jsonb,
    EXCLUDE using hash (key with =)
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



## 查询转数据帧

```
# see huggingface/NLPP_Audio/vector.py
async def fetch_data(sql_query) -> pd.DataFrame:
    global async_pool
    await async_pool.open()

    async with async_pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql_query)
            rows = await cur.fetchall()
            df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    return df
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

https://www.skypyb.com/2020/12/jishu/1705/  提前分词方案

https://pgroonga.github.io/install/

https://groonga.org/docs/install/ubuntu.html



**TokenBigram** 将文本按 **二元组（bigrams）** 的方式进行分词，即将相邻的两个字符作为一个词元进行处理。

```
CREATE INDEX idx_content ON documents USING pgroonga (content pgroonga_text_full_text_search_config('TokenBigram'));

```





```
  SELECT unnest -> 'value' AS "value" FROM unnest(
  pgroonga_tokenize('This is a pen. これはペンです。你为什么学习普通话？',
                    'tokenizer', 'TokenMecab("include_class", true)',
                    'token_filters', 'TokenFilterNFKC100("unify_kana", true)')
  );
  
    SELECT unnest -> 'value' AS "value" FROM unnest(
  pgroonga_tokenize('This is a pen. これはペンです。你为什么学习普通话？',
                    'tokenizer', 'TokenBigram')
  );
```





```

# see huggingface/NLPP_Audio/vector.py

proxychains4 apt install -y software-properties-common && 
proxychains4 add-apt-repository -y universe && 
proxychains4 add-apt-repository -y ppa:groonga/ppa &&
proxychains4 apt install -y wget lsb-release && 
proxychains4 wget https://packages.groonga.org/ubuntu/groonga-apt-source-latest-$(lsb_release --codename --short).deb && 
proxychains4 apt install -y -V ./groonga-apt-source-latest-$(lsb_release --codename --short).deb && 
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release --codename --short)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list && 
proxychains4 wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && 
proxychains4 apt update && 
proxychains4 apt install -y -V postgresql-17-pgdg-pgroonga && 
proxychains4 apt install -y -V groonga-tokenizer-mecab

CREATE EXTENSION pgroonga;
	# 成功

see https://pgroonga.github.io/tutorial/
    # 用法很详细
    
-- 在 postgres 数据库里运行
CREATE DATABASE nlppvector
    WITH OWNER = postgres 
    ENCODING = 'UTF8' 
    TABLESPACE = pg_default 
    CONNECTION LIMIT = -1 
    TEMPLATE template0;



CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgroonga;
CREATE TABLE IF NOT EXISTS nlpp_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    JPMD5 CHAR(32) NOT NULL,
    S_JP text NOT NULL,
    V_JP vector(1536) NOT NULL,
    S_CN text NOT NULL,
    S_EN text NOT NULL,
    metadata jsonb NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (JPMD5) 
);
CREATE INDEX IF NOT EXISTS index_pgvector_VJP ON nlpp_vector USING hnsw (V_JP vector_cosine_ops);
CREATE INDEX IF NOT EXISTS index_pgroonga_SJP ON nlpp_vector USING pgroonga (S_JP);


```





```
    CREATE TABLE danganronpa (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        ch text DEFAULT '', 
        en text DEFAULT '', 
        type text, 
        begintime text,
        endtime text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector, 
        v_ch  tsvector, 
        v_en  tsvector, 
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode text DEFAULT '',
        audio bytea, 
        video bytea,
        videoname text 
      );
    create extension pgroonga;
    create extension pg_jieba;
    CREATE INDEX pgroonga_jp_index ON danganronpa USING pgroonga (jp);
    CREATE INDEX animename_index ON danganronpa (name);
    CREATE INDEX episode_index ON danganronpa (episode);
```





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



### TokenMecab + mecab-ipadic-neologd

```
apt install mecab libmecab-dev mecab-ipadic && 
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd && 
sudo ./bin/install-mecab-ipadic-neologd -n




```



### TokenBigramSplitSymbolAlpha 中文模糊搜索

适用小规模应用

```
-- 使用前缀索引提高准确性
CREATE INDEX idx_name ON table_name 
USING pgroonga (column_name) 
WITH (tokenizer='TokenBigramSplitSymbolAlpha("report_source_location", true)');

PGroonga 使用 TokenBigramSplitSymbolAlpha 的几种常用查询方式：

基础匹配查询 (pgroonga_match)：

-- 最基础的全文搜索
SELECT * FROM table_name 
WHERE column_name @@ '关键词';

-- 使用 pgroonga_match
SELECT * FROM table_name 
WHERE pgroonga_match(column_name, '关键词');
模糊查询 (pgroonga_query)：
sql

-- 支持查询语法，如 OR、AND 等
SELECT * FROM table_name 
WHERE pgroonga_query(column_name, '关键词1 OR 关键词2');

-- 使用通配符
SELECT * FROM table_name 
WHERE pgroonga_query(column_name, '关*词');
相似度查询：
sql

-- 返回相似度分数
SELECT *,
  pgroonga_score(tableoid, ctid) AS score 
FROM table_name 
WHERE column_name &@ '关键词' 
ORDER BY score DESC;

-- 设置最小相似度阈值
SELECT * FROM table_name 
WHERE pgroonga_similarity_search(column_name, '关键词') > 0.5;
短语搜索：
sql

-- 精确短语匹配
SELECT * FROM table_name 
WHERE pgroonga_query(column_name, '"完整短语"');
结合其他条件：
sql

-- 组合多个条件
SELECT * FROM table_name 
WHERE pgroonga_query(column_name, '关键词')
  AND created_at > '2024-01-01'
  AND status = 'active';

```







## Install ffmpeg



```
# ffmpeg on centos7
sudo yum install epel-release && \
sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm && \
sudo yum install ffmpeg ffmpeg-devel
```



##  Install RUM

see huggingface/NLPP_Audio/vector.py

```
            """
            SELECT s_jp, v_jp <=> tsquery('まずは|どう|したら') as distance FROM nlpp_vector ORDER BY v_jp <=> tsquery('まずは|どう|したら') asc LIMIT 3;
                # | 表示只要命中其中一个就给分 (结果是距离)
            SELECT s_jp, v_jp <=> tsquery('まずは&どう&したら&○○') as distance FROM nlpp_vector ORDER BY v_jp <=> tsquery('まずは&どう&したら&○○') asc LIMIT 3;
                # & 表示必须全部命中，否则给 0 分 (结果是距离)
            """
            q = "|".join( mmsegjp("まずはどうしたら"))
            sql = f"SELECT v_jp <=> tsquery('{q}') as distance, name, s_jp, s_zh, v_jp, v_zh, metadata, TO_CHAR(AddTime, 'YYYY-MM-DD HH24:MI:SS') AS AddTime FROM nlpp_vector WHERE enable='t' ORDER BY v_jp <=> tsquery('{q}') ASC LIMIT 20;"
            sql = f"""
                WITH tmp AS (
                SELECT s_jp, v_jp <=> tsquery('{q}') as distance
                FROM nlpp_vector WHERE name = 'nlpp_姉ヶ崎'
                )
                SELECT * from tmp
                WHERE distance < 99999
                ORDER BY distance ASC
                LIMIT 10;
            """
```





```

# see huggingface/NLPP_Audio/vector.py

proxychains4 pip install --upgrade pip && 
proxychains4 pip install "psycopg[binary]"  


proxychains4 apt install postgresql-17-pgvector
	# 安装向量插件

git clone https://github.com/postgrespro/rum && 
cd rum &&
make USE_PGXS=1 PG_CONFIG=/usr/bin/pg_config &&
make USE_PGXS=1 PG_CONFIG=/usr/bin/pg_config install &&
make USE_PGXS=1 installcheck &&
$ psql DB -c "CREATE EXTENSION rum;
	# 安装  RUM 插件

# see https://pgroonga.github.io/install/ubuntu.html
proxychains4 apt install -y software-properties-common && 
proxychains4 add-apt-repository -y universe && 
proxychains4 add-apt-repository -y ppa:groonga/ppa &&
proxychains4 apt install -y wget lsb-release && 
proxychains4 wget https://packages.groonga.org/ubuntu/groonga-apt-source-latest-$(lsb_release --codename --short).deb && 
proxychains4 apt install -y -V ./groonga-apt-source-latest-$(lsb_release --codename --short).deb && 
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release --codename --short)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list && 
proxychains4 wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && 
proxychains4 apt update && 
proxychains4 apt install -y -V postgresql-17-pgdg-pgroonga && 
proxychains4 apt install -y -V groonga-tokenizer-mecab

CREATE EXTENSION pgroonga;
	# 成功

see https://pgroonga.github.io/tutorial/
    # 用法很详细
    DROP DATABASE IF EXISTS nlppvector;
CREATE DATABASE nlppvector
WITH OWNER = postgres 
ENCODING = 'UTF8' 
TABLESPACE = pg_default 
CONNECTION LIMIT = -1 
TEMPLATE template0;
    # 整完 nvcat 重连一次，选这个库再运行下面的语句


CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
DROP TABLE IF EXISTS nlppvector;
CREATE TABLE IF NOT EXISTS nlpp_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    JPMD5 CHAR(32) NOT NULL,
    Name text NOT NULL,
    S_jp text NOT NULL,
    S_zh text NOT NULL,
    Embed_rwkv_jp vector(1024) NOT NULL,
    V_jp tsvector NOT NULL,
    V_zh tsvector NOT NULL,
    Metadata jsonb NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),
    PRIMARY KEY (JPMD5, Name)
);
CREATE INDEX fts_rum_v_jp ON nlpp_vector USING rum (V_jp rum_tsvector_ops);
CREATE INDEX fts_rum_v_zh ON nlpp_vector USING rum (V_zh rum_tsvector_ops);





    

CREATE DATABASE nlppvector
WITH OWNER = postgres 
ENCODING = 'UTF8' 
TABLESPACE = pg_default 
CONNECTION LIMIT = -1 
TEMPLATE template0;


CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgroonga;
CREATE TABLE IF NOT EXISTS nlpp_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    JPMD5 CHAR(32) NOT NULL,
    name text NOT NULL,
    S_JP text NOT NULL,
    S_CN text DEFAULT '' NOT NULL,
    S_EN text DEFAULT '' NOT NULL,
    Embed_gpt_jp vector(1536) NOT NULL,
    Embed_rwkv_jp vector(1024) NOT NULL,
    V_JP vector(1536) NOT NULL,
    metadata jsonb NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),  
    PRIMARY KEY (JPMD5, name) 
);
CREATE INDEX IF NOT EXISTS index_pgvector_VJP ON nlpp_vector USING hnsw (V_JP vector_cosine_ops);
CREATE INDEX IF NOT EXISTS index_pgroonga_SJP ON nlpp_vector USING pgroonga (S_JP);
```





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
psql DB -c "CREATE EXTENSION rum;"
```





```
dnf install epel-release -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y

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
    
  - [PostgreSQL 百亿级数据范围查询, 分组排序窗口取值 极致优化 case](https://developer.aliyun.com/article/39680)
  
  - [PostgreSQL IN里面传入1w+值如何优化到极致？](https://zhuanlan.zhihu.com/p/342722338)
  
    - [postgres in查询优化](https://www.cnblogs.com/yb38156/p/11195727.html)
  
      > regexp_split_to_table 和 regexp_split_to_array 都是字符串分隔函数，可通过指定的表达式进行分隔。区别是 regexp_split_to_table 将分割出的数据转成行，regexp_split_to_array 是将分隔的数据转成数组。
  
    > 
  
    
  
    
  
    




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



```
DROP DATABASE IF EXISTS nlppvector;
CREATE DATABASE nlppvector
WITH OWNER = postgres 
ENCODING = 'UTF8' 
TABLESPACE = pg_default 
CONNECTION LIMIT = -1 
TEMPLATE template0;
    # 整完 nvcat 重连一次，选这个库再运行下面的语句


CREATE EXTENSION IF NOT EXISTS rum;
CREATE EXTENSION IF NOT EXISTS vector;
DROP TABLE IF EXISTS nlppvector;
CREATE TABLE IF NOT EXISTS nlpp_vector (
    ID bigint generated always as identity (START WITH 1 INCREMENT BY 1), 
    JPMD5 CHAR(32) NOT NULL,
    Name text NOT NULL,
    S_jp text NOT NULL,
    S_zh text NOT NULL,
    Embed_rwkv_jp vector(1024) NOT NULL,
    V_jp tsvector NOT NULL,
    V_zh tsvector NOT NULL,
    Metadata jsonb NOT NULL,
    AddTime timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdateTime timestamp DEFAULT NULL,
    Enabled boolean DEFAULT '1',
    UNIQUE(ID),
    PRIMARY KEY (JPMD5, Name)
);
CREATE INDEX fts_rum_v_jp ON nlpp_vector USING rum (V_jp rum_tsvector_ops);
CREATE INDEX fts_rum_v_zh ON nlpp_vector USING rum (V_zh rum_tsvector_ops);

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



# 图数据库

- https://github.com/apache/age  Apache AGE

  - https://github.com/apache/age/issues/2111  pg 17 支持

  - ```
    select * from cypher('graph1', $AnythingInsideDollars$
    Match(v:Persion{p_id:'safd$$bbb'}
    return v
    $AnythingInsideDollars$) as (v agtype);
    ```

  - ```
    So if you have the following in your db:
    
    (:City)-[:AirRoute]-(:City)
    (:City)-[:SeaRoute]-(:City)
    Being able to run a query and say 'Give me any Air OR Sea route between these two cities', which should be possible (in openCypher terms) via
    
    (:City { name: 'London' })-[:SeaRoute|AirRoute]-(:City { name: :'Rotterdam' })
    ```

  - ```
    issue1996=# SELECT * FROM cypher('issue1996', $$ CREATE (a:NODE {key1: "prop1", key2:"prop2"}) $$) as (a agtype);
     a 
    ---
    (0 rows)
    
    issue1996=# SELECT * FROM cypher('issue1996', $$ MATCH (a) return a$$) as (a json);
                                                 a                                              
    --------------------------------------------------------------------------------------------
     {"id": 844424930131969, "label": "NODE", "properties": {"key1": "prop1", "key2": "prop2"}}
    (1 row)
    issue1996=# SELECT cast(a as json) FROM cypher('issue1996', $$ MATCH (a) return a$$) as (a agtype);
                                                 a                                              
    --------------------------------------------------------------------------------------------
     {"id": 844424930131969, "label": "NODE", "properties": {"key1": "prop1", "key2": "prop2"}}
    (1 row)
    
    issue1996=# SELECT pg_typeof(a) FROM cypher('issue1996', $$ MATCH (a) return a$$) as (a json);
     pg_typeof 
    -----------
     json
    (1 row)
    ```

  - ```
    -- 创建一个包含 jsonb 属性的节点
    SELECT * 
    FROM cypher('your_graph', $$
        CREATE (n:Person {name: 'Alice', attributes: '{"age": 30, "hobbies": ["reading", "hiking"]}'::jsonb})
    $$) AS (a agtype);
    
    -- GIN 索引用于通用的 jsonb 查询
    CREATE INDEX idx_person_attributes_gin ON your_graph.ag_catalog.v_label USING GIN ((properties -> 'attributes'));
    
    -- 表达式索引用于优化针对 age 字段的查询
    CREATE INDEX idx_person_age_expr ON your_graph.ag_catalog.v_label USING BTREE ((properties -> 'attributes' ->> 'age'));
    
    查询：查找所有 hobbies 包含 "reading" 的人员。
    SELECT *
    FROM cypher('your_graph', $$
        MATCH (n:Person)
        WHERE n.attributes @> '{"hobbies": ["reading"]}'::jsonb
        RETURN n
    $$) AS (n agtype);
    
    查询：查找 age 等于 30 岁的人员。
    SELECT *
    FROM cypher('your_graph', $$
        MATCH (n:Person)
        WHERE (n.attributes->>'age')::int = 30
        RETURN n
    $$) AS (n agtype);
    
    按 age 从小到大排序人员。
    SELECT *
    FROM cypher('your_graph', $$
        MATCH (n:Person)
        RETURN n
        ORDER BY (n.attributes->>'age')::int ASC
    $$) AS (n agtype);
    	# BTREE 索引支持高效的排序操作。
    
    ```

  - ```
    SELECT *
    FROM cypher('your_graph', $$
        MATCH (n:Person)
        WHERE (n.attributes->>'age')::int > 25
        RETURN n
    $$) AS (n agtype);
    
    ```

  - 

- https://blog.csdn.net/qq_21090437/article/details/120292081 AgensGraph



# pg_duckdb

https://github.com/duckdb/pg_duckdb

https://github.com/abersheeran/r2-webdav  Cloudflare Workers + R2 免维护，10 GB 配置绰绰有余



# ltree

```
CREATE TABLE test (
  path ltree,
  EXCLUDE USING HASH ((path::text) WITH =)
);
```



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



## 普通查询返回json

```
select jsonb_agg(u) as user_data
from users u
where u.id = '1';

或着：
select jsonb_agg(jsonb_build_object('id', u.id, 'name', u.name)) as user_data
from users u
where u.id = '1';
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



# 连接池



```python
# see huggingface/NLPP_Audio/vector.py

import aiohttp
import asyncio
import json
import psycopg
import psycopg_pool
import pandas as pd

# 创建一个全局变量，用于存储连接池实例
async_pool = None

async def pool_connect():
    global async_pool
    if async_pool is None:
        async_pool = psycopg_pool.AsyncConnectionPool(
            conninfo="postgres://postgres:post4321@127.0.0.1/nlppvector",
            min_size=1,
            max_size=32,
            open=False  # Avoid automatic opening on initialization to handle manually
        )
        # Opening the pool
        await async_pool.open()
        logging.info("Database connection pool is initialized and open.")

async def fetch_data(sql_query) -> pd.DataFrame:
    global async_pool
    await async_pool.open()

    async with async_pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql_query)
            rows = await cur.fetchall()
            df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    return df
    
async def main():
    global async_pool
    await pool_connect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

```





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



# 模糊查询

https://www.cnblogs.com/xueqiuqiu/articles/10994428.html



# 正则查询

https://www.cnblogs.com/xueqiuqiu/articles/10994428.html

- https://github.com/digoal/blog/blob/master/201611/20161118_01.md 正则



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





# BM25高性能全文检索

https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/user-guide/usage-guide  BM25高性能全文检索



https://www.v2ex.com/t/1146080

- https://blog.hiripple.com/zh

  后端 supabase ，前端部署在 Vercel 



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



