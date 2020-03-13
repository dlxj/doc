
\# linux 下 取进程占用 cpu 最高的前10个进程

ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3|head

 

 

\# linux 下 取进程占用内存(MEM)最高的前10个进程

ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head

The server quit without updating PID file (/mntt/ksbao/mysqldata/data/iZ2335r8wxoZ.pid).

/etc/init.d/mysql.server

USER    PID %CPU %MEM  VSZ  RSS TTY   STAT START  TIME COMMAND

mysql   2665 1.1 10.8 7136056 1761020 ?   Sl  14:05  0:14 /usr/local/mysql/bin/mysqld --basedir=/usr/local/mysql --datadir=/mntt/ksbao/mysqldata/data --plugin-dir=/usr/local/mysql/lib/plugin --user=mysql --log-error=/mntt/ksbao/mysqldata/data/iZ2335r8wxoZ.err --pid-file=/mntt/ksbao/mysqldata/data/iZ2335r8wxoZ.pid --port=3306