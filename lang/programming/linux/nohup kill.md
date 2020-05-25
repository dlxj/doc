nohup node xx.js >outlog &

\#!/bin/bash

kill -9 $(lsof outlog | tail -n +2  | awk '{print $2}' | tr '\n' ' ')

kill -9 $(lsof -i:8077 | tail -n +2  | awk '{print $2}' | tr '\n' ' ')



jobs 查看后台运行程序