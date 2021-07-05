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

