\# run

\#!/bin/bash

nohup node launchcluster.js >outlog &

\# kill

\#!/bin/bash

kill -9 $(lsof outlog | tail -n +2  |  awk '{print $2}' | tr '\n' ' ') && \

kill -9 $(lsof -i:8001 | tail -n +2  |  awk '{print $2}' | tr '\n' ' ')

ps p $(cat /var/run/elasticsearch.pid)

kill -9 $(lsof -i:8888 | tail -n +2  |  awk '{print $2}' | tr '\n' ' ')



jobs 查看后台运行程序



进程所在路径

```
PID为1521，ls -al /proc/1521  , CWD 就是进程所在路径
```





# tmux

```
yum install epel-release
yum install tmux
```

```
tmux
tmux attach # default 0

tmux attach -t 0
Contol + b  后按 d 可以离开环境并不影响当前程序的执行（离开后可以断开 ssh 连接）
ctrl + D # 退出当前 session，中断程序执行
tmux kill-session -t 0 # 在没有进入 session 的情况下 kill 它

```



