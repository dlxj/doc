nohup node xx.js >outlog &

\#!/bin/bash

kill -9 $(lsof outlog | tail -n +2  | awk '{print $2}' | tr '\n' ' ')

kill -9 $(lsof -i:8077 | tail -n +2  | awk '{print $2}' | tr '\n' ' ')



jobs -l 查看后台运行程序

```bash
fg %n 让后台运行的进程n到前台来 
bg %n 让进程n到后台去；   
PS:"n"为jobs查看到的进程编号.
```





nohup python iEncoding.py >outlog &

> ```bash
> ps -aux|grep iEncoding.py| grep -v grep # 显示后台进程
> ```