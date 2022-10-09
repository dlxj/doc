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



# 关闭后台进程

```

// 数据库备份时卡了，就会不响应
// ps aux |grep mysql  
// insert into imgs(`md5`,api,ip,userID)VALUES('2ef5f105b39f12a67749a55fd321b671','aliyun','127.0.0.1',0) on duplicate key update ip='127.0.0.1'

(async () => {

    let fs = require('fs')
    let md5 = require('md5')

    let bytes = fs.readFileSync("1032.jpg")  // 'binary'
    let buf = Buffer.from(bytes)
    let m5 = md5(buf)
    let b64 = buf.toString('base64')


    let json = {
        md5: m5,
        imgData: b64,
        guid: '1049a596-fea6-4f0f-863f-62d0b0a2ea55',
        userID:11,
        bookNO: 'lrx333',
        imgName: '1032.jpg',
        originImgData: b64
    }

    // json = {
    //     md5: '7468efae7d7ab7333d0197a8ca1bf32c',
    //     imgData: 'hasTest',
    //     guid: 'abc346eb-aeb1-4759-b885-68052ec34810',
    //     bookNO: 'lrx333',
    //     imgName: '1032.jpg'
    // }

    let bent = require('bent')
    let formurlencoded = require('form-urlencoded')

    let formurlencoded_body = formurlencoded(json)

    //let post = bent('http://192.168.2.88:11112', 'POST', 'json', 200)
    let post = bent('http://127.0.0.1:11112', 'POST', 'json', 200)
    let response = await post('/aliyun/ocr', json)



    data = JSON.parse(response).data.test

    let s = JSON.stringify(response)

    console.log(response)

})()

```



