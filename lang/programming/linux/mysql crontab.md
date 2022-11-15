
service mysql.server [status|start|stop]

*/1 * * * * /mntt/ksbao/proxyserver/server_ossvideo_wjw4/crontab_run.sh

每隔五分钟，如果mysql 是停上状态则自动启动mysql

crontab -e

\#*/5 * * * * /mntt/ksbao/mysqlautostart.sh

 

\#!/bin/bash

pgrep mysqld &> /dev/null

if [ $? -ne 0 ]

then

echo "`date` mysql is stop" >> /mntt/ksbao/mysql_listen.log

service mysql.server start

else

echo "`date` mysql running" >> /mntt/ksbao/mysql_listen.log

fi



# crontab

```
crontab -e # 定时任务
00   00    26      01   *   echo 'hi from crontab.' > /root/sayhi.txt
分	时	  日	     月	 年

@reboot  /root/auto_mount.sh # 重启自动执行
crontab -l

```



