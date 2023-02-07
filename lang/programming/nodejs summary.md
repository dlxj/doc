```
babel.config.js
module.exports = {
    presets: [
        //'@vue/cli-plugin-babel/preset'
        ["@vue/app",{useBuiltIns:"entry"}]
    ]
}
```



```
# node 默认 1.5G 内存上限，超出会报错 
luanch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}\\boom_memory.js",
            "runtimeArgs": ["--max-old-space-size=8192"]
        }
    ]
}

{
            "args":["a"],
            "runtimeArgs": [
                "run-script",
                "app",
                "b"
            ],
        }
打印参数可以发现 args 、runtimeArgs都会传给程序，但是runtimeArgs参数会紧跟可执行文件


```





```
多线程爆内存 ERR_WORKER_OUT_OF_MEMORY

https://zhuanlan.zhihu.com/p/167920353    worker threads 

https://juejin.cn/post/6844903937355563022
注意这3句：每个线程都拥有独立的事件循环
每个线程都拥有一个 JS 引擎实例
每个线程都拥有一个 Node.js 实例

https://juejin.cn/post/6844903953759469581
	干货
const { Worker, isMainThread, parentPort, MessageChannel, threadId } = require('worker_threads');

if (isMainThread) {
    const worker1 = new Worker(__filename);
    const worker2 = new Worker(__filename);
    
    const { port1, port2 } = new MessageChannel();
    const sharedUint8Array = new Uint8Array(new SharedArrayBuffer(4));
	// 输出一下sharedUint8Array
    console.log(sharedUint8Array);
    worker1.postMessage({ uPort: port1, data: sharedUint8Array }, [ port1 ]);
    worker2.postMessage({ uPort: port2, data: sharedUint8Array }, [ port2 ]);

    worker2.once('message', (message) => {
        console.log(`${message}, 查看共享内存:${sharedUint8Array}`);
    });
} else {
    parentPort.once('message', ({ uPort, data }) => {
        uPort.postMessage(`我是${threadId}号线程`);
        uPort.on('message', (msg) => {
            console.log(`${threadId}号收到:${msg}`);
            if (threadId === 2) {
                data[1] = 2;
                parentPort.postMessage('2号线程修改了共享内存!!!');
            }
            console.log(`${threadId}号查看共享内存:${data}`);
        })
    })
}

=>
Uint8Array [ 0, 0, 0, 0 ]
2号收到:我是1号线程
2号线程修改了共享内存!!!, 查看共享内存:0,2,0,0
1号收到:我是2号线程
2号查看共享内存:0,2,0,0
1号查看共享内存:0,2,0,0


I check settings which relates vm.max_map_count

# sysctl vm.max_map_count
vm.max_map_count = 65530
# sysctl kernel.threads-max
kernel.threads-max = 2060362
# sysctl kernel.pid_max
kernel.pid_max = 4194304
I guess that vm.max_map_count should be twice of kernel.threads-max, thus, I set as follows.

# sysctl -w vm.max_map_count=4120724

```





```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7
systemctl enable postgresql-13 # 自启动

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目
pm2 update    // 清空重启次数等（疑难杂症可以试试）


pm2 monit
	# 实时监视进程

pm2 reload explainteam_server_7114 --name my_new_name --max-old-space-size 4096

pm2 delete processID  // 删除一项

pm2 flush 进程ID | 进程名  // 清空日志

# 关闭防火墙
systemctl stop firewalld
# 关闭 apache 
service httpd stop

yum install nginx
nginx -t # 显示主配置文件路径，并检查语法错误
systemctl start nginx
nginx -s reload

# atuto run when reboot
chmod +x /etc/rc.d/rc.local
vi /etc/rc.d/rc.local
mount /dev/sda1 /mnt  # 加一句，挂载存储块



```



## cnpm



```
管理员身份运行 powershell
	set-executionpolicy remotesigned

# cnpm
 原因：cnpm版本太高了，npm全局安装的cnpm是最新版的，所以卸载原来的cnpm再装一个指定版本即可

卸载cnpm:

npm uninstall -g cnpm

安装指定版本：7.1.0

npm install cnpm@7.1.0 -g --registry=https://registry.npm.taobao.org
	# 配套 node14 ok



npm install -g cnpm --registry=https://registry.npm.taobao.org
	# 安装是最新版 会有兼容问题
	
	
```



### Rprimordials is not defined

- https://blog.csdn.net/qiqi_zhangzz/article/details/106599233

```

先把 node_modules 全删了

package.json 同级目录新建 npm-shrinkwrap.json

{
  "dependencies": {
    "graceful-fs": {
      "version": "4.2.3"
    }
  }
}

npm i
	# 注意只有这一次有效果，再 npm i 就没效果了

```







## Get



```javascript
let bent = require('bent')
let get = bent('https://xxxxxx', 'GET', 'json', 200)
let ssss = JSON.stringify(response)
```



```


const express = require('express')
var mysql = require('mysql');
const port = process.argv[2] || 666;


async function getUserids(){
    var connection = mysql.createConnection({
        host:'xxxx',
        user:'xxxx',
        password:'xxxx',
        database:'xxxxx'
    });
    
    connection.connect();
    
    let query = function( sql, values ) {
        return new Promise(( resolve, reject ) => {
            connection.query(sql, values, function (error, results, fields) {
                if (error)  reject( error );
                resolve( results )
            });
        })
    }
    
    row = await query("SELECT xxxxx", [xxx])
    
    connection.end();
    
    return row
}

const app = express()
// http://xxxxx/xxxxx?xxx=xx&xxx=xx
app.get('/gendifficulty', async (req, res) => {
  
    if ( !('AppID' in req.query) || !('KsbaoAppID' in req.query)){
        res.writeHead(300, {"Content-Type": "text/plain"});
        res.write("err\n");
        res.end();
        return
    }

    AppID = req.query['AppID']
    KsbaoAppID = req.query['KsbaoAppID']

    AppID = Number(AppID)
    KsbaoAppID = Number(KsbaoAppID)

    if (Number.isNaN(AppID) || Number.isNaN(KsbaoAppID)) {
        res.writeHead(300, {"Content-Type": "text/plain"});
        res.write("err\n");
        res.end();
        return
    }

    row = await getUserids()

    res.send(row)
  
})

app.listen(port, function() {
  console.log('ok');
})

```



## Post



 request 已弃用，用这个  https://github.com/mikeal/bent



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

    //let post = bent('http://xxx:11112', 'POST', 'json', 200)
    let post = bent('http://127.0.0.1:11112', 'POST', 'json', 200)
    let response = await post('/aliyun/ocr', json)



    data = JSON.parse(response).data.test

    let s = JSON.stringify(response)

    console.log(response)

})()
```





```
const post = bent('http://localhost:666', 'POST', 'json', 200) # 返回类型是 json
const response = await post('/gettest', { appename: 'ZC_ZXYJHNKX_YTMJ' })
```





```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "appEName=ZC_HLXHS_YTMJ&SessionKey=38B0535F89F1A02ED984B7888048D392&idArray=[{"AllTestID":6004390,"ChildTableID":-1,"CptID":459,"Enabled":1},{"AllTestID":6004391,"ChildTableID":-1,"CptID":459,"Enabled":1},{"AllTestID":6004392,"ChildTableID":-1,"CptID":459,"Enabled":1}]" 
http://10.94.183.7:9013/api/test/findAll
http://120.27.142.68:9013/api/test/findAll
```





```javascript
var request = require('request')

module.exports =
{
  name: `getTestbyids`,
  author: `gd`,
  params: {
    appEName: {
      type: 'string',
      remark: ''
    },
    idArray:{
      type: 'string',
      remark: ''
    }
  },
  async handler({appEName, idArray}) {

    

    var data = await new Promise(function (resolve) {

      url = 'http://xxxxx:xx/api/xxxxx'
      request.post(url, {
        'form': {
          SessionKey: "xxxxx",
          appEName: appEName,
          idArray: idArray
        }
      },
      function(err, response, result) {
        if (err || response.statusCode != 200) {
          console.log(url + err + response.statusCode)
          //throw (url + err + response.statusCode)
          return resolve({})
        }
  
        return resolve(result)
      })

    })

    data = JSON.parse(data).data

    // var testids = {}

    // data.forEach(d => {
    //   let key = d.AllTestID + "/" + d.ChildTableID
    //   testids[key] = 0
    // });

    return data
    
    
  },
  remark: ``
}

```





```
    let data = await new Promise(function (resolve) {
      request.post({
        timeout: 6000000,
        url: 'http:xxxxxxxxx',
        form: {
          word, type, enable,
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded;',
        }, callback(erro, response, body) {
          console.log(body);
          if (erro) {
            throw erro;
          }
          resolve(body);
        },
      });
    });
```



### bent



```
const fs = require('fs')
const { promisify } = require('util')
const stream = require('stream')
const pipeline = promisify(stream.pipeline)
const bent = require('bent')

const main = async () => {
  const readable = await bent('https://images.unsplash.com/photo-1595132938692-83ad2c098e47')()
  const writable = fs.createWriteStream('./image.jpg')
  await pipeline(readable, writable)
}

main()
```

```
import bent from "bent";
import { createWriteStream } from "fs";
import { resolve } from "path";
import { pipeline } from "stream";
import { promisify } from "util";

const pipe = promisify(pipeline);

const URL = "http://***/1.txt";

export const run = async () => {
  const readable = (await bent(URL)("")) as NodeJS.ReadableStream;
  const writeable = await createWriteStream(resolve(__dirname, "../2.txt"));

  await pipe(readable, writeable);

  console.log("0");
};
```







```
	# 新版好像要自已处理 form-urlencoded 了
	let bent = require('bent')
    let formurlencoded = require('form-urlencoded')
    let mysql = require('./mysql')

    let host = 'localhost:62137'

    async function Convert2GIF(str_base64) {
    
        let url = `http://${host}`

        let json = {
            image_base64: str_base64
        }

        let formurlencoded_json = formurlencoded(json)

        let post = bent(url, 'POST', 'json', 200)
        let response = await post('/Convert2GIF', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded'})

        if (response.status == 200) {
            return [ response.data, '']
        } else {
            return [null, response.msg]
        }

        return response

    }


    let [str_base64_gif, ms] = await Convert2GIF('aaa')
    if (str_base64 === null) {

        throw 'Error: convert image to GIF fail! ' + ms

    }
```





```
# 参数太长也会出错

( async ()=>{

  let bent = require('bent')
  let _ = require('lodash')

  let host = `xxxx`
  let appename = 'xxxxx'
  
  let json = {
    SessionKey: "xxxx",
    appEName: xxxx
  }

  let url = `http://${host}`

  let post = bent(url, 'POST', 'json', 200)
  let response = await post('/Convert2GIF', json)

  var idArray = response.data

  let arr_chunks = _.chunk(idArray, 10000)

  idArray = [ idArray[0] ]

  idArray = JSON.stringify(arr_chunks[0])


  json = {
      SessionKey: "xxxx",
      appEName: xxxx,
      idArray:xxxx
  }

  var tests = []
  
  let response2 = await post('xxxxx', json)

  tests =tests.concat(response2.data.test)

  

  a = 1


}) ()
```



#### keda



```
// https://blog.csdn.net/sueRimn/article/details/100134349

( async ()=>{

    // https://www.xfyun.cn/doc/words/xf-printed-word-recognition/API.html#%E6%8E%A5%E5%8F%A3%E8%A6%81%E6%B1%82

async function ocr(imgPath) {

    let bent = require('bent')
    let formurlencoded = require('form-urlencoded')
    
    let X_Param = {
        "language": "cn|en",
        "location": "true"
    }
    
    X_Param = Buffer.from(JSON.stringify(X_Param)).toString('base64')
    //X_Param = Buffer.from(X_Param, 'base64').toString('ascii')
    
    let APIKey = "xxxxxx"
    let X_CurTime = parseInt(new Date().getTime() / 1000).toString()
    let X_CheckSum = require('md5')(APIKey + X_CurTime + X_Param)
    
    let headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'X-Appid': "xxxx",
        'X-CurTime': X_CurTime,
        'X-Param': X_Param,
        'X-CheckSum': X_CheckSum
    }
    
    let buffer = require('fs').readFileSync(imgPath)
    let b64 = buffer.toString('base64')
    
    let body = {
        image: b64
    }
    
    let host = 'webapi.xfyun.cn'
    let url = `https://${host}`
    
    let formurlencoded_body = formurlencoded(body)
    
    let post = bent(url, 'POST', 'json', 200)
    let response = await post('/v1/service/v1/ocr/general', formurlencoded_body, headers)

    return response
}


async function ocr2(imgPath) {
    // npm install moment
    // npm install crypto-js

    let bent = require('bent')
    let formurlencoded = require('form-urlencoded')
    let fs = require('fs')

    if (!fs.existsSync(imgPath)) {
        throw `图片不存在 ${imgPath}`    
    }

    let bytes = fs.readFileSync(imgPath)  // 'binary'
    let img_b64 = Buffer.from(bytes).toString('base64')

    let dateFormat = 'ddd, DD MMM YYYY HH:mm:ss'
    let dateString =  new Date().toUTCString() //'Mon, 01 Jan 0001 00:00:01 GMT'
    let date = require('moment').utc(dateString, dateFormat)._i

    let APPId = "xxx"
    let APISecret = "xxx"
    let APIKey = "xxx"

    let host = 'api.xf-yun.com'
    let method = 'POST'
    let path = '/v1/private/s00b65163'

    let url = `https://${host}${path}`

    let signature_origin = `host: ${host}\ndate: ${date}\n${method} ${path} HTTP/1.1`

    let signature_sha = require("crypto-js").HmacSHA256(signature_origin, APISecret)

    let HmacSHA1 = signature_sha.toString()

    signature_sha = require("crypto-js").enc.Base64.stringify(signature_sha)

    let authorization_origin = `api_key="${APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="${signature_sha}"`

    let authorization = Buffer.from(authorization_origin).toString('base64')

    let values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }

    let urlencode_values = formurlencoded(values)

    let request_url = url + "?" + urlencode_values

    let headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}

    //headers = JSON.stringify(headers)

    let body = {
        "header": {
            "app_id": APPId,
            "status": 3,
        },
        "parameter": {
            "s00b65163": {
                "category": "mix0",
                "result": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "json"
                }
            }
        },
        "payload": {
            "s00b65163_data_1": {
                "encoding": "png",
                "image": img_b64,
                "status": 3
            }
        }
    }

    let formurlencoded_body = formurlencoded(body)

    body = JSON.stringify(body)

    let benthost = `https://${host}`
    let bentpath = `${path}`+ "?" + urlencode_values

    let post = bent(benthost, 'POST', 'json', 200)
    let response = await post(bentpath, body, headers)

    let text = response.payload.result.text

    text = Buffer.from(text, 'base64').toString()

    fs.writeFileSync('./re.json', text)

    return [signature_origin, signature_sha, authorization_origin, authorization, urlencode_values, request_url, headers, body]

}

let imgPath = './韩语.png'
let imgPath2 = './双栏.bmp'
let imgPath3 = './双栏.jpg'
let imgPath4 = './漏字很多.jpg'

let [signature_origin, signature_sha, authorization_origin, authorization, urlencode_values, request_url, headers, body] = await ocr2(imgPath)

let re = body  // signature_origin + "|" + signature_sha

process.stdout.write(re)

let a = 1

})()




/// python begin

from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import os,subprocess
import traceback
import json
import requests

imgeName = './韩语.png'
imgeName2 = './双栏.bmp'

if os.path.exists("./韩语.png"):
    a = 1
else:
    a = 1


'''
appid、apiSecret、apiKey请到讯飞开放平台控制台获取并填写到此demo中；
图像数据，base64编码后大小不得超过4M
'''
# 请到控制台获取以下信息，并填写
APPId = "xxx"
APISecret = "xxx"
APIKey = "xxx"
# 图片位置
with open(imgeName2, "rb") as f:
    imageBytes = f.read()


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass


# calculate sha256 and encode to base64
def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    u = Url(host, path, schema)
    return u


# build websocket auth request url
def assemble_ws_auth_url(requset_url, method="POST", api_key="", api_secret=""):
    u = parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date =  format_date_time(mktime(now.timetuple()))
    print(date)
    # date = "Thu, 12 Dec 2019 01:57:27 GMT"
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    print(signature_origin) # 'host: api.xf-yun.com\ndate: Mon, 07 Feb 2022 09:05:53 GMT\nPOST /v1/private/s00b65163 HTTP/1.1'

    # out_bytes = subprocess.check_output(["node", "keda2.js"])
    # out_text = out_bytes.decode('utf-8') # 'host: api.xf-yun.com\ndate: Mon, 07 Feb 2022 09:05:53 GMT\nPOST /v1/private/s00b65163 HTTP/1.1'

    #signature_origin = out_text

    signature_origin = signature_origin.encode('utf-8')

    #signature_origin = signature_origin.decode('utf-8')

    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin, # .encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8') # 'JJBIEpM9jKzqDpTL9QEFgoqUzSiLb4YUai+MYP576yc='  '3xJqUrRTgpTopAamjDptLvNK5a0d+/iOxu6rf8tg3N0='


    #signature_sha = out_text

    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)

    #authorization_origin = out_text
    
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

    #authorization = out_text

    print(authorization_origin)
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }

    urlencode_values = urlencode(values)

    # urlencode_values = out_text

    re = requset_url + "?" + urlencode_values  # urlencode(values)

    # re = out_text

    return  re


url = 'https://api.xf-yun.com/v1/private/s00b65163'

body = {
    "header": {
        "app_id": APPId,
        "status": 3,
    },
    "parameter": {
        "s00b65163": {
            "category": "mix0",
            "result": {
                "encoding": "utf8",
                "compress": "raw",
                "format": "json"
            }
        }
    },
    "payload": {
        "s00b65163_data_1": {
            "encoding": "png",
            "image": str(base64.b64encode(imageBytes), 'UTF-8'),
            "status": 3
        }
    }
}

body = json.dumps(body)

# out_bytes = subprocess.check_output(["node", "keda2.js"])
# out_text = out_bytes.decode('utf-8')
#body = out_text

request_url = assemble_ws_auth_url(url, "POST", APIKey, APISecret)

headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}
print(request_url)
response = requests.post(request_url, data=body, headers=headers) # json.dumps(body)
print(response)
# print(response.content)
print("resp=>" + response.content.decode())
tempResult = json.loads(response.content.decode())
finalResult = base64.b64decode(tempResult['payload']['result']['text']).decode()
finalResult = finalResult.replace(" ", "").replace("\n", "").replace("\t", "").strip()
print("text字段Base64解码后=>" + finalResult)

// python end
```



#### form-data

- https://github.com/mikeal/bent/issues/121

```
let FormData = require('form-data')
let bent = require('bent')

     let postData = new FormData()
      postData.append('OperateUserID', userID)
      postData.append('OperateUserName', `${userID}`)
      postData.append('bookID', bookID)
      postData.append('type', 3)
      postData.append('beginpath', `${bookID}/`)
      postData.append('filepath', `小截图/basename`)
      postData.append('fileName', basename)
      postData.append('fileName', basename)
      postData.append('file', fs.createReadStream(fullpath))
      
      let post = bent('http://xxxx:xxxx', 'POST', 'json', 200)
      let response = await post('/api/xxxxx', postData, postData.getHeaders())

      if (response.status == 200) {
        let b = 1
      } else {
        return this.msg(301, `${fullpath} ${response.msg}`)
      }
```





#### src

```
This is how the lib was designed. You should pass to bent all the statuses the server might respond:

const client = bent(200,201,202,203,204,301,302...);
This not an issue, but rather a design decision.
```









## 两条sql 语句写一起



```javascript

'use strict'

const request = require('request');

module.exports = {

  params: {
    word: {
      type: 'String',
      remark: 'xx'
    }
  },
  remark: '',
  action: async function (req, res) {
    let { word, type, testID, childTestID, appID, enable } = req.body;

    let sql = `
    insert into xx.xx(appID,testID,childTestID,word,type)values(?,?,?,?,?);
    insert into xx.xx(word,type,\`enable\`)values(?,?,?) 
    on duplicate key update 
    type=values(type),
    \`enable\`=values(\`enable\`);
    `;

    await new Promise((resolve) => {
      this.DB.query(sql, [appID, testID, childTestID, word, type, word, type, enable], (erro, result) => {
        if (erro) {
          res.send(201, erro.message);
          return;
        }
        resolve(result);
      });
    });
```



# live debug 



## vscode 远程调试

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/server.js",
            "runtimeExecutable": "/usr/local/bin/node14"
        }
    ]
}

https://matpool.com/supports/doc-vscode-connect-matpool/
    Remote Development 安装插件
    VS Code 远程连接矩池云机器教程
# train.py 添加命令行参数，并用vscode 远程调试K80 服务器上的 conda 环境(ctrl+shift+p 选conda的python)，vscode 中修改train.py 在main 函数下加入：
```





```
# https://medium.com/the-node-js-collection/live-debugging-node-js-apps-at-the-command-line-cd5b58f883e1

# http://www.ruanyifeng.com/blog/2018/03/node-debugger.html

# https://juejin.cn/post/6844904098618163207
	# VSCode 远程调试

# https://zhuanlan.zhihu.com/p/100092504

	# http://www.baiguangnan.com/2019/03/13/vscoderemotedebugnodejs/

		# vscode node remote debug

# https://nodejs.org/api/debugger.html
node inspect -p 9436  # 进程ID
	# help # 打印帮助

	# debug> setBreakpoint('main.js', 4, 'num < 0')  # 条件断点

list(100): shows the first 100 lines of code
setBreakpoint(17): sets a breakpoint on the 17th line
clearBreakpoint(17): removes a breakpoint on the 17th line
exec body: evaluates the body variable and prints out its result
cont: continues the program's execution

Resume execution(continue): c or cont
Next line: n or next
Step into a function: s or step
Step out: o or out
Set breakpoint: sb or setBreakpoint
Clear breakpoint: sc or clearBreakpoint

watch('counter')



# https://betterprogramming.pub/how-to-debug-using-node-js-built-in-debugger-f3ab3ba6e7c8
	# Debug Using Node.js’s Built-In Debugger
	
setBreakpoint('xxxxxx.js', 45)
setBreakpoint('xxxxxx.js', 142)
clearBreakpoint('xxxx.js', 45)

# 可能是这一句的错误
let retSaveExam = await this.services.saveExamgather({examgahters})

n # 下一行

break in file:////yingedu/project_test/ksbaiexam/http/api/submit.js


# https://zhuanlan.zhihu.com/p/98571113
	# chrome 远程调试node


node14 --inspect-brk=0.0.0.0:9229 server.js

chrome://inspect/#devices

```



## chrome 远程调试



- https://zhuanlan.zhihu.com/p/338287139

1. chrome 打开： chrome://inspect
2. 点击 Open dedicated DevTools for Node
3. xxxx.77:9229  # Add connection # 这样只要服务器脚本运行后就后自动进入调试状态

```
# centos7 待调试脚本（非服务端，跑一次就结束的脚本）
node --inspect-brk=xxx.77:9229 insert.cjs # 指定IP端口

```



## vue 在vscode 下断点


- https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html

  > vscode 安装插件 JavaScript Debugger
  >
  > ```
  > 新建 launch.json， 弹出的选项选择 chrome
  > 重点是：先在终端 npm run dev，看它的端口是什么，下面的url 端口就填什么，然后在vscode F5，会打开浏览器, 就可以在vscode 下断了
  > {
  >     "version": "0.2.0",
  >     "configurations": [
  >         {
  >             "type": "chrome",
  >             "request": "launch",
  >             "name": "vuejs: chrome",
  >             "url": "http://localhost:8080",
  >             "webRoot": "${workspaceFolder}/src",
  >             "sourceMapPathOverrides": {
  >                 "webpack:///src/*": "${webRoot}/*"
  >             },
  >             "resolveSourceMapLocations": [
  >                 "${workspaceFolder}/**",
  >                 "!**/node_modules/**"
  >             ]
  >         }
  >     ]
  > }
  > ```
  >
  > ```
  > vue.config.js # 注意配了这个 F5 后断点才真的断了下来
  > 
  > module.exports = {
  >    runtimeCompiler: true,
  >     configureWebpack: {
  >         devtool: 'source-map'
  >     }
  > }
  > 
  > 
  > var titme = Date.now();
  > var d = {
  > //可在浏览器中调试 说明： https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html
  > configureWebpack: {
  > devtool: 'source-map',
  > output: { // 输出重构  打包编译后的 文件名称  【模块名称.版本号.时间戳】
  > filename: `js/[name].${titme}.js`,
  > chunkFilename: `js/[name].${titme}.js`
  > },
  > },
  > // 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度
  > productionSourceMap: false,
  > // // 设置生成的 HTML 中 <link rel="stylesheet"> 和 <script> 标签的 crossorigin 属性（注：仅影响构建时注入的标签）
  > publicPath: './', // 设置打包文件相对路径
  > // 输出文件目录
  > outputDir: "webv2",
  > }
  > console.log(`${process.env.NODE_ENV}`)
  > if( process.env.NODE_ENV.match(/build/g) ){ 
  > delete d.configureWebpack.devtool
  > d.productionSourceMap = false;
  > }
  > module.exports = d
  > ```
  >
  > vue 在vscode 下断点
  >
  > file --> preferences --> setting 找到eslint ，找到几个  check box 勾上



- https://www.bbwho.com/visual-studio-codeduan-dian-diao-shi-vue/



## v8 profiler

- https://fed.taobao.org/blog/taofed/do71ct/nodejs-memory-leak-analyze/

```
v8 prof
使用 V8 自带的 profiler 功能，分析 JavaScript 各个函数的消耗和 GC 部分。

npm install profiler
node --prof xxx.js
会生成 xxxx-v8.log，之后使用工具转换成可读的。

npm install tick
node-tick-processor xxxx-v8.log
就可以查看相关的数据了。
```



## v8 source map

- https://github.com/evanw/node-source-map-support





# Syntax

- https://www.ruanyifeng.com/blog/2020/08/how-nodejs-use-es6-module.html



```
node --input-type=module
```





## commonjs

```
import 导入的变量无论是否为基本类型都是引用传递
module.exports 很像 export default 所以 ES6模块 可以很方便兼容 CommonJs
```



### .mjs .cjs



```
.mjs 和 .cjs 后缀名保证分别解析为 ECMAScript modules 和 ComandJS 
```





```
// ffmpeg.mjs
import { execa } from 'execa'
import path from 'path'
import { dirname } from 'path'
//global.__dirname = process.cwd()
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

export default {

    extractSubtitle: async function (vdpath, type, nth) {

        try {

            // let args = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} ${path.join( __dirname, 'tmp.srt' )}` // write file
            let cmd = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} -f srt pipe:1`   // write stdout

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            childProcess.stdout.pipe(process.stdout)
            let { stdout } = await childProcess

            return { srt:stdout, msg:'' }

        } catch(err) {
           return { srt:null, msg : err }
        }
    },
    extractAudio: async function (vdpath, type, begin_time, end_time) {

        try {

            let cmd = `ffmpeg -i ${vdpath} -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} pipe:1`   // write stdout

            let childProcess = execa(cmd, {shell:true})
            childProcess.stdout.pipe(process.stdout)
            let { stdout } = await childProcess

            return { au: Buffer.from(stdout) }

        } catch(err) {
           return { audi:null}
        }

        return { au:1 }
    }

}

// test.js
let { default: libff } = await import('./ffmpeg.mjs')
let { srt: str_jp, msg:msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream
let { srt: srt_chs, msg:msg_chs } = await libff.extractSubtitle(vdpath, 'srt', 0)
```





```
// ff.mjs 必须是 .mjs
// node --experimental-modules .\ff.mjs  成功运行
import {execa} from 'execa';
const {stdout} = await execa('dir', []);
console.log(stdout);
console.log(111)
```

- https://github.com/chrisveness/geodesy/issues/79
  
- 各种示例
  
- https://juejin.cn/post/6972006652631318564

  - Node 最新 Module 导入导出规范

    

- https://zhuanlan.zhihu.com/p/337796076
  
  - ES Modules 的加载、解析和执行都是异步的



- https://depth-first.com/articles/2019/01/17/debugging-es-modules-with-mocha-in-vs-code/

```
服务器端开发用require/exports ，浏览器端使用import/export


方式二  通过Node原生支持ES Module

步骤一、 更改js文件后缀为.mjs

步骤二、 import js的时候，如import './core';不能省略后缀名，需要写成import './core.mjs';

执行：node --experimental-modules ./bin/index.mjs

步骤三、 由于是实验性质特性，所以需要配置开启 --experimental-modules，否则会报如下错误

```



```
var exec = require('child_process').exec;  // 出错
	//   "type": "commonjs",  // package.json 加上这一句
	
let execa = import('execa')  // 这样可以
	// 出错：Must use import to load ES Module
```



```
node --experimental-modules ./bin/www

launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
          "type": "node",
          "request": "launch",
          "name": "Launch Program",
          "program": "${workspaceFolder}\\bin\\www",
        }
    ]
}

```



###  dir.mjs

```javascript
import { eachFileFilterSync } from 'rd'
import path from 'path'

export default {

    allmkv : function(dir, filter) {

        var paths = []

        // 目录下的所有文件名
        eachFileFilterSync(dir, /\.mkv$/, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (filter != undefined && fullpath.indexOf(filter) != -1) {
                paths.push(fullpath)
            } else if (filter == undefined ) {
                paths.push(fullpath)
            }
            
        })

        return paths

    }

}

let { default: libdir } = await import('./dir.mjs')
let mkvs = libdir.allmkv(root, 'Pokemon')
```



### cjs 导入mjs



```javascript
// es.mjs
let foo = {name: 'foo'};
export default foo;

export let a = 1

// cjs
let { execa } = await import('execa')  // execa 库这样导入

import('./es').then((res)=>{
  console.log(res) // { get default: {name: 'foo'}, a: 1 }
})
```



### mjs 导入cjs



```javascript
// config.js
module.exports = {

    host:'xxx.77',
    passwd:'xxx.com',
    port: '5432'
}

// insert.mjs
let { default:config }  = await import('./config.js')
```



### mjs 导入标准库

```javascript
import pg from 'pg'
let { Pool, Client } = pg
// import { Pool, Client } from 'pg'  // 原 cjs 的导入方式是这样

import path from 'path'
```



### export default 用this互引用

```javascript
export default {

	funtion a {
	
	},
	function b {
		this.a()
	}
}
```



### 自定义包

```
npm i ws # 安装这个包来观察包的组织结构

目录结构
- ws
	- lib        # 这里放所有 js 实现文件
    index.js     # 导出符号，cjs 方式 
	wrapper.mjs  # 导出符号，mjs 方式
    package.json # 指定导出文件：index.js 和 wrapper.mjs
    
```



```
index.js
'use strict';

const WebSocket = require('./lib/websocket');

WebSocket.createWebSocketStream = require('./lib/stream');
WebSocket.Server = require('./lib/websocket-server');
WebSocket.Receiver = require('./lib/receiver');
WebSocket.Sender = require('./lib/sender');

WebSocket.WebSocket = WebSocket;
WebSocket.WebSocketServer = WebSocket.Server;

module.exports = WebSocket;
```



```
wrapper.mjs
import createWebSocketStream from './lib/stream.js';
import Receiver from './lib/receiver.js';
import Sender from './lib/sender.js';
import WebSocket from './lib/websocket.js';
import WebSocketServer from './lib/websocket-server.js';

export { createWebSocketStream, Receiver, Sender, WebSocket, WebSocketServer };
export default WebSocket;
```



```
package.json
{
  "name": "ws",
  "version": "8.12.0",
  "description": "Simple to use, blazing fast and thoroughly tested websocket client and server for Node.js",
  "keywords": [
    "HyBi",
    "Push",
    "RFC-6455",
    "WebSocket",
    "WebSockets",
    "real-time"
  ],
  "homepage": "https://github.com/websockets/ws",
  "bugs": "https://github.com/websockets/ws/issues",
  "repository": "websockets/ws",
  "author": "Einar Otto Stangvik <einaros@gmail.com> (http://2x.io)",
  "license": "MIT",
  "main": "index.js",
  "exports": {
    ".": {
      "import": "./wrapper.mjs",
      "require": "./index.js"
    },
    "./package.json": "./package.json"
  },
  "browser": "browser.js",
  "engines": {
    "node": ">=10.0.0"
  },
  "files": [
    "browser.js",
    "index.js",
    "lib/*.js",
    "wrapper.mjs"
  ],
  "scripts": {
    "test": "nyc --reporter=lcov --reporter=text mocha --throw-deprecation test/*.test.js",
    "integration": "mocha --throw-deprecation test/*.integration.js",
    "lint": "eslint --ignore-path .gitignore . && prettier --check --ignore-path .gitignore \"**/*.{json,md,yaml,yml}\""
  },
  "peerDependencies": {
    "bufferutil": "^4.0.1",
    "utf-8-validate": ">=5.0.2"
  },
  "peerDependenciesMeta": {
    "bufferutil": {
      "optional": true
    },
    "utf-8-validate": {
      "optional": true
    }
  },
  "devDependencies": {
    "benchmark": "^2.1.4",
    "bufferutil": "^4.0.1",
    "eslint": "^8.0.0",
    "eslint-config-prettier": "^8.1.0",
    "eslint-plugin-prettier": "^4.0.0",
    "mocha": "^8.4.0",
    "nyc": "^15.0.0",
    "prettier": "^2.0.5",
    "utf-8-validate": "^6.0.0"
  },
  "__npminstall_done": true,
  "_from": "ws@8.12.0",
  "_resolved": "https://registry.npmmirror.com/ws/-/ws-8.12.0.tgz"
}
```



#### 生成包

- https://cloud.tencent.com/developer/article/1485591





### 异步转同步

- https://blog.kaciras.com/article/22/convert-async-to-sync-in-node

- https://github.com/Kaciras/deasync

- https://github.com/nodejs/node/issues/40898

  ```
  vm.runInThisContext runs a script and therefore does not support top level await. if you want to use that you'll need to use the experimental vm.Module api. the repl is just transpiling code with top level await into async functions.
  ```

  

```
const { deasync } = require("@kaciras/deasync");
const { performance } = require('perf_hooks')

const sleep = deasync((timeout, done) => {
    (async ()=>{
        let { default:wrapper } = await import('./wrapper.mjs')  # 成功执行
        let { name } = wrapper
        done(null, "wake up!")
    })()
});

console.log("Timestamp before: " + performance.now());
let re = sleep(1000)
console.log("Timestamp after: " + performance.now());
```





```
cnpm install @kaciras/deasync

const { deasync } = require("@kaciras/deasync");
const { performance } = require('perf_hooks')

const sleep = deasync((timeout, done) => {
	setTimeout(() => done(null, "wake up!"), timeout);
});

console.log("Timestamp before: " + performance.now());
console.log(sleep(1000));
console.log("Timestamp after: " + performance.now());
```







```
// 些方法是开启另一个进程，并等待它结束，不好用

const { execSync } = require('child_process')

const code = `
const { stdout } = require('process')
const dns = require('dns')
dns.lookup('www.baidu.com', (err, address, family) => {
  stdout.write(address)
})
`

console.log('start')

const lookupResult = execSync('node', { input: code })
console.log(lookupResult.toString()) // 结果

console.log('end')
```



### vm替代eval

- https://stackoverflow.com/questions/34160216/how-to-retrieve-async-results-from-a-node-js-vm-script-using-es7-syntax

- https://zhuanlan.zhihu.com/p/128090873
- https://nodejs.org/api/vm.html#modulelinklinker
- https://github.com/pierrec/node-eval
- https://blog.csdn.net/qq_42709514/article/details/121925095 vm2 jsdom
- https://github.com/semlinker/node-deep/blob/master/module/%E6%B7%B1%E5%85%A5%E5%AD%A6%E4%B9%A0%20Node.js%20Module.md#nodejs-vm
- https://fed.taobao.org/blog/taofed/do71ct/nodejs-memory-leak-analyze/
- https://github.com/agracio/edge-js/issues/163  edge-js 如何使用高版本的 node



```

# 真的完全解决问题了

// npm config set python D:\usr\Python38\python.exe
// npm install @kaciras/deasync  // 依赖 node-gyp https://github.com/nodejs/node-gyp
// npm install franc

const { deasync } = require("@kaciras/deasync")

async function vmrun(code, params, callback) {

    let imports = params.imports
    for (let model of imports) {
        params[model] = await import(model)
    }

    const vm = require('vm')
    const options = {}
    const { timeout = 120 * 1000, breakOnSigint = true } = options
    const script = new vm.Script(`(async()=>{${code}})()`);
    script.runInContext(vm.createContext({
        ...params,
        callback
    }), {
        timeout,
        breakOnSigint,
    })
}

// 同步运行，在 vm 里跑传入的 nodejs 代码, 约定代码里调用 callback(null, { msg:'hi,,,' }) 来返回结果
const vmrunSync = deasync((code, params, callback) => {
    vmrun(code, params, callback)
})


let code = `
    console.log(fs)  // fs 是事先 import 好的模块，这里可以直接用  所有可用参数都在这里展开了：  ...params
    console.log('hello, from vm')
    return callback(null, { msg:'hi,,,' })
`

let re = vmrunSync( code, { imports: ['fs'] } ) // deasync 的作用是去掉了最最外层的 await
```







```

# 这个好 好像完全解决问题了
(async()=>{

  // npm config set python D:\usr\Python38\python.exe
  // npm install @kaciras/deasync  // 依赖 node-gyp https://github.com/nodejs/node-gyp
  // npm install franc

  const { deasync } = require("@kaciras/deasync")

  const syncify = deasync((code, params, done) => {
    (async ()=>{
      const vm = require('vm')
      const { timeout = 120 * 1000, breakOnSigint = true } = {}
      const script = new vm.Script(`(async()=>{${code}})()`)
      script.runInContext(vm.createContext({
        ...params,
        done,
      }), {
        timeout,
        breakOnSigint,
      })

    })()
  })
  
  let c = syncify(`
    result = 1
    console.log(msg)
    fs.writeFileSync('hi.txt', 'hi, from vm!', {encoding:'utf8', flag:'w'} )
    lang = francAll('Alle menslike wesens word vry', { only: ['jpn', 'cmn', 'eng'] })
    done(null, {result, lang})
  `, { msg:'hi, from vm!', fs : await import ('fs'), ... await import('franc') })

  async function runScript(code, context = {}, options = {}) {
      return new Promise((resolve, reject) => {
        const vm = require('vm')
        const { timeout = 120 * 1000, breakOnSigint = true } = options;
        const script = new vm.Script(`(async()=>{${code}})()`);
        script.runInContext(vm.createContext({
          ...context,
          resolve,
          reject,
        }), {
          timeout,
          breakOnSigint,
        });
      });
  }
  
  //let { franc, francAll } = await import('franc')
  
  let re = await runScript(`
    result = 1
    console.log(msg)
    fs.writeFileSync('hi.txt', 'hi, from vm!', {encoding:'utf8', flag:'w'} )
    lang = francAll('Alle menslike wesens word vry', { only: ['jpn', 'cmn', 'eng'] })
    resolve({result, lang})
    `, 
    { msg:'hi, from vm!', fs : await import ('fs'), ... await import('franc') })  // 利用 context 传参


  let a = 1

  })()
  
```





```

# vm 内部成功 hook vm 外部的 promise 执行

const vm = require('vm')

const context = vm.createContext({
  require,
  console
})

vm.runInContext(`
  const ah = require('async_hooks')

  ah.createHook({
    init (asyncId, type, triggerAsyncId, resource) {
      if (type === 'PROMISE') {
        console.log('I stole a promise from outside my context!', resource)
      }
    }
  }).enable()
`, context)

Promise.resolve()

```





```
const vm = require('vm')  # 如果这里要 import 可以用异步转同步

async function add(n) {
    
    return n + 1
}

let sandbox = {
  add: add,
  number: 10
};

const code = `
    (async ()=>{
        await import('fs')
        result = await add(number)
    })()
`
const script = new vm.Script(code)
let ctx = vm.createContext(sandbox)
script.runInContext(ctx)
```





```
var code = `
var fn = () => {}
I = 100; while(I--) { fn(); }
`;

const vm = require('vm');
const context = vm.createContext();
const script = new vm.Script(code);

console.time('vm');
script.runInContext(context);
console.timeEnd('vm');
```



```
// https://stackoverflow.com/questions/34160216/how-to-retrieve-async-results-from-a-node-js-vm-script-using-es7-syntax


(async()=>{

const vm = require('vm')

async function runScript(code, context = {}, options = {}) {
    return new Promise((resolve, reject) => {
      const { timeout = 120 * 1000, breakOnSigint = true } = options;
      const script = new vm.Script(`(async()=>{${code}})()`);
      script.runInContext(vm.createContext({
        ...context,
        resolve,
        reject,
      }), {
        timeout,
        breakOnSigint,
      });
    });
}

let re = await runScript('result = 1; resolve();')

let a = 1

})()
```





## typeof



```javascript
            if (typeof content == 'object') {

            } else if (typeof content == 'string') {
                var j = { "title":title, "content":content, childs:[] }
                
            }
```



## global 



global 是内置的全局对象，任意地方可用（可以把任意东西装进出，制造一个合局入口）



## 三目运算符



```javascript
# 连续判断
	const color = d.added ? 'green' :
        d.removed ? 'red' : 'grey'
```



## !!

```javascript
const scale = !!options.full ? "scale=1280:720,setsar=1:1":"scale=640:360,setsar=1:1";

!!是一个逻辑操作，不论它的后面接的是什么数值，它的结果会被强制转换成bool类型，之所以用两个感叹号，主要是为了让结果不会逻辑反过来
```



## ...



array, json 展开

```javascript
function f(v,w,x,y,z){ }
var args = [2,3]
f(1,...args,4,...[5]) # args 展开成 2, 3
```



## sign

```
	# 标签可以像for 一样 break
	getAuthorize:
    {
      const dict = await xxx
      if (dict['0'] !== undefined) {
        break getAuthorize;
      }
```



## 函数偷梁换柱

```
// 解决重复点击路由报错的BUG
import router from './router'
const originalPush = router.prototype.push
router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => {
   console.log(err)
  })
}
```



## 还可以样这定义变量

```
const { timeout = 120 * 1000, breakOnSigint = true } = {}
```





## 定义属性

```
#　D:\GitHub\node-14.21.1\lib\repl.js

function REPLServer(prompt,
                    stream,
                    eval_,
                    useGlobal,
                    ignoreUndefined,
                    replMode) {
  if (!(this instanceof REPLServer)) {
    return new REPLServer(prompt,
                          stream,
                          eval_,
                          useGlobal,
                          ignoreUndefined,
                          replMode);
  }

  ObjectDefineProperty(this, 'inputStream', {
    get: pendingDeprecation ?
      deprecate(() => this.input,
                'repl.inputStream and repl.outputStream are deprecated. ' +
                  'Use repl.input and repl.output instead',
                'DEP0141') :
      () => this.input,　　// 当作函数直接执行
    set: pendingDeprecation ?
      deprecate((val) => this.input = val,
                'repl.inputStream and repl.outputStream are deprecated. ' +
                  'Use repl.input and repl.output instead',
                'DEP0141') :
      (val) => this.input = val,  // 代参数的函数执行
    enumerable: false,
    configurable: true
  });
```





# Regex



> https://javascript.info/regexp-groups



## 高级选项

- https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions

| 标志 | 描述                                                        |
| :--- | :---------------------------------------------------------- |
| `g`  | 全局搜索。                                                  |
| `i`  | 不区分大小写搜索。                                          |
| `m`  | 多行搜索。                                                  |
| `s`  | 允许 `.` 匹配换行符。                                       |
| `u`  | 使用 unicode 码的模式进行匹配。                             |
| `y`  | 执行“粘性 (`sticky`)”搜索，匹配从目标字符串的当前位置开始。 |



## test



```javascript
// 是否匹配
const regex = new RegExp('foo*');
const globalRegex = new RegExp('foo*', 'g');
console.log(regex.test(str));
// expected output: true
```



## string.match



```javascript
> '###'.match(/#+/)
[ '###', index: 0, input: '###', groups: undefined ]
> 'a'.match(/#+/)
null
```





## dotAll

. 默认不匹配换行符

```
const regex1 = new RegExp('foo', 's');  // 's' 选项开启 . 增加匹配换行符功能
console.log(regex1.dotAll);
// expected output: true
```



## new RegExp



```
new RegExp(String.raw`^(?!.*E\.).*$`, 'gs')  // 参数g 全局匹配，参数s 让. 匹配 \n
```



## 匹配以特殊字符开头的字符

- 比如说 ( ，会出错， 所以需要转义

```nodejs
            let wd = c.lineWords    // 该字符所在行的全部字符

            try {

              let ww = c.word
              let regstr = '^\\'+ String.raw`${ww}\s*`

              let ddd = wd; debugger 

              c.lineWords = wd.replace(new RegExp(regstr), '')  // 从该字符所在行的全部字符中把自已删掉
                // c.word 有可能是特殊字符，比如 ( 所以这里进行转义

            } catch(e){

              let wdd = c.word; debugger

            }
```





## 匹配所有



```
# 更方便的方法,match 有index（注意：str, re 要在while 的外面定义，否则死循环）
let str = 'axxaxxa'
let re = /a/g
while( ( match = re.exec(str)) != null ) {
  a = 1
}
```





## matchAll

- 相当于python 的 finditer

```javascript
  let regAX = String.raw`\n\d+\..+?（\s*?）.*?\n`
  
  if ((new RegExp(regAX).test(strs))) {  //匹配标题

    let matches = strs.matchAll(regAX)

    let arr = Array.from(matches)

    if (arr.length > 0) {

      for (let i = 0; i < arr.length; i++) {
        let match = arr[i]
        let begin = match.index
        let end = begin + match[0].length

        let title = match[1]  // get the match group text
        let testOrigin = strs.substring(begin, end) // get the origin match text

        testOrigins.push(testOrigin)

      }

    }

  }
```



```python
# '[A1型题]'

strs = docText.replace('**********', '')
strs = strs.strip()
strs = '\n\n' + strs +  '\n\n'


"""
单项选择题（无序号，答案附在后边）
"""
def ANONUM(strs):

    strs += 'A.'

    result = []
    
    #od = {} # OrderedDict()

    iters = re.finditer('\n.+?\nA\.', strs, re.DOTALL)
    poss = [ i.span() for i in iters ] # 标题positions

    for i in range( len(poss) - 1 ):
        (start, end) = poss[i]
        (start2, end2) = poss[i+1] 

        pre = strs[start:end]
        last = strs[end-2:end2]


        dic = {}

        title = re.compile('\n(.+?)\nA\.').search(pre).group(1)

        print(title)

        dic["Title"] = title

        arr = last.split('\n')


        selectItems = []

        for s in arr:
            
            s = s.replace('\n','')

            if '【答案】' in s:
                
                rr2 = s.split('【答案】')
                Answer = rr2[1]

                dic["Answer"] = Answer

                break
            
            rr = s.split('.')
            itemName = rr[0]
            itemStr = rr[1]

            selectItems.append( {"Content":itemStr,"ItemName": itemName} )
            

        dic["SelectedItems"] = selectItems
        dic["Explain"] = ""
        dic["Type"] = ""

        
        result.append(dic)

    
    j = string(result)

    return j

j = ANONUM(strs)
```



## 匹配不消耗



```
/a(?=b)bc/中的正向肯定预查(?=b)匹配了a后面的字母b，但是并没有消耗它，所以，后面再跟一个“bc”串，这就完整地匹配了字符串“abc”。其实，它的真正意义应该是确定了这个字母a，因为不是每个字母a后面都会跟一个字母b的！ 
而a(b)bc因为匹配并消耗了字母a后面的b，再来添加一个“bc”串的时候，就变成了“abbc”，就不能匹配字符串“abc”。

到这，估计后面的正向否定预查就没什么问题了，以及反向预查，只不过是类似的，但是位置变了。

(?<=pattern) 
这是反向肯定预查，因为Javascript不支持反向预查，所以以下用Python实现
```



## 不是分组



```
(?:)
```







## 不匹配某个串



### 零宽度断言



```

# https://stackoverflow.com/questions/406230/regular-expression-to-match-a-line-that-doesnt-contain-a-word
	国外大佬

# https://www.cnblogs.com/wangqiguo/archive/2012/05/08/2486548.html


# https://www.cnblogs.com/wangqiguo/archive/2012/05/08/2486548.html
	利用正则表达式排除特定字符串

// 匹配不以baidu开头的字符串
//ss = 'baidu.com'
ss = 'sina.com.cn'
let matches = ss.matchAll('^(?!baidu).*$')
let arr = Array.from(matches)  # 成功匹配'sina.com.cn'



// 匹配不以com 结尾的字符串
ss = 'www.hao.cc'
//ss = 'www.baidu.com'
let matches = ss.matchAll('^.*?(?<!com)$')
let arr = Array.from(matches)  # 成功匹配 'www.hao.cc'

// 匹配不含if 的字符串
//ss = 'else if (a>b) {}'
ss = 'else (a>b) {}'

let matches = ss.matchAll('^([^f]|[^i]f)+$')  # 成功匹配 'else (a>b) {}'

let arr = Array.from(matches)



// 匹配不含if 的字符串 （优化版）
//ss = 'else if (a>b) {}'
ss = 'else (a>b) {}'

let matches = ss.matchAll('^(?!.*if).*$')  # 成功匹配 'else (a>b) {}'

let arr = Array.from(matches)


// 匹配不含E. 的字符串
ss = 'else E. (a>b) {}'

let matches = ss.matchAll('^(?!.*E\\.).*$')

let arr = Array.from(matches)  # OKOKOK 不匹配E.  ，其他的都匹配






// 匹配不含E. 的字符串
ss = 'else E . (a>b) {}'

let regg = '^(?!.*E\\.).*$'
let regg2 = String.raw`^(?!.*E\.).*$`

let regg3 = new RegExp(String.raw`^(?!.*E\.).*$`, 'gs')  // 参数g 全局匹配，参数s 让. 匹配 \n

console.log( regg3.dotAll )

let matches = ss.matchAll(regg3)  // 正则必须有 g 参数，否则报错

let arr = Array.from(matches)  // # OKOKOK 不匹配E.  ，其他的都匹配


console.log(/foo/ig.flags)   // 正则的简写，参数加了 i, g,g 表示全局匹配

a = 1

```



### 匹配不含 A. B. C. D. E. 的串

```
# 匹配不含 A. B. C. D. E. 的串
ss = '\n\nelse E .  D. (a>b) {}\n\n'
let regg4 = new RegExp(String.raw`^\n\n(?!.*?(A\.|B\.|C\.|D\.|E\.)).*\n\n$`, 'gs')
let matches = ss.matchAll(regg4)  // 正则必须有 g 参数，否则报错
let arr = Array.from(matches)
```

https://salesforce.stackexchange.com/questions/329256/how-can-i-match-second-last-char-of-a-string-with-regex



```

# https://stackoverflow.com/questions/7801581/regex-for-string-not-containing-multiple-specific-words

// 匹配不含E. 且还不含D. 的字符串
ss = '\n\nelse E .  D . (a>b) {}\n\n'

let regg = '^(?!.*E\\.).*$'
let regg2 = String.raw`^(?!.*E\.).*$`

let regg3 = new RegExp(String.raw`^(?!.*E\.).*$`, 'gs')  // 参数g 全局匹配，参数s 让. 匹配 \n


let regg4 = new RegExp(String.raw`^\n\n(?!.*?(E\.|D\.)).*\n\n$`, 'gs')

// (?!.*98|.*2000|.*xp)

// ^([^h].*$)|(h([^e].*$|$))|(he([^h].*$|$))|(heh([^e].*$|$))|(hehe.+$) 


console.log( regg3.dotAll )

let matches = ss.matchAll(regg4)  // 正则必须有 g 参数，否则报错

let arr = Array.from(matches)  // # OKOKOK 不匹配E.  ，其他的都匹配


console.log(/foo/ig.flags)   // 正则的简写，参数加了 i, g,g 表示全局匹配

if (arr.length > 0) {

  for (let i = 0; i < arr.length; i++) {
    let match = arr[i]
    let begin = match.index
    let end = begin + match[0].length

    let title = match[1]  // get the match group text
    let testOrigin = ss.substring(begin, end) // get the origin match text

    testOrigins.push(testOrigin)

  }
```



### 匹配不以  题\s*\n  结尾的字符串



```javascript
/*
三、共用题干单选题(1~3题共用题干)
最后一串可见字符不能是   题|共用题干|共用题干\)
*/
ss = '\n一、www.hao.com题共用 \n'

let regStr = String.raw`\n\s*([一二三四五六七八九十百千万]+?、(?!.*?((题|共用题干|共用题干\))\s*\n)).+?)\s*\n`

let matches = ss.matchAll(new RegExp(regStr,'gs'))
let arr = Array.from(matches)

说明：
	(?!.*?(题\s*\n))  预先保证了整个串不以 题\s*\n  结尾，然后才去匹配

```





### 解析选择题选项



```javascript


strs = `[A1型选择题]
1.最易发生阴阳互损的脏腑是
A.心
B.肺
C.脾
D.肝
E.肾
F.天气
G.空气
`

var selects = []

if ((new RegExp(String.raw`\nA\..+?\s+B\..+?\s+C\..+?\s+D\..+?\s*(?:E\..+?)*`)).test(strs)) {  // 匹配选项

  let match = strs.match(String.raw`\n(A\..+?)\s+(B\..+)?\s+(C\..+?)\s+(D\..+?)\s*((?:E\..+?)*)\s*((?:F\..+?)*)\s`)  // ((?:G\..+?)*)\s+  // (?:[a-zA-Z]\..+?)+

  //let match = strs.match(String.raw`\n(?:[A-H]\..+?)+`)

  for (let i = 1; i < match.length; i++) {
    let t = match[i] // get the match group text

    if (t === null || t === undefined || t === '' ) {
      continue
    }

    let ItemName = t.split('.')[0]
    let Content = t.split('.')[1]

    selects.push({ ItemName, Content })

  }

  if (selects.length > 0) {

    let last = selects[ selects.length - 1 ]

    let laststr = last.ItemName + '.' + last.Content

    let arr = strs.split( new RegExp(laststr) )

    if (arr.length === 2) {

      let strs2 = arr[1]

      if ((new RegExp(String.raw`\n((?:G\..+?)*)\s*((?:H\..+?)*)\s`)).test(strs)) {

        let match2 = strs.match(String.raw`\n((?:G\..+?)*)\s*((?:H\..+?)*)\s*((?:I\..+?)*)\s*((?:J\..+?)*)\s*((?:K\..+?)*)\s*((?:L\..+?)*)\s`) 

        for (let i = 1; i < match2.length; i++) {
          let t = match2[i] // get the match group text
      
          if (t === null || t === undefined || t === '' ) {
            continue
          }
      
          let ItemName = t.split('.')[0]
          let Content = t.split('.')[1]
      
          selects.push({ ItemName, Content })
      
        }

      }


    }

  }

}
```







### ?= 向前查找

- = 后面必须匹配，但不吃掉它(consume)

```
# https://www.jianshu.com/p/eec1a081b4b7
```



#### 否定式向前查找

 ```
a ='这是中文\nabc'
a.replace(/(?<!\n)([a-z])/g, 'O')
	
--> '这是中文\naOO'
 ```





(?!...) 





### <= 向后查找

- < 前面必须匹配，但不吃掉它(consume)

  ```
  a = `1\n2\n3\n`
  a.replace(/(?<=\n)\d(?=\n)/g, 'OO')  # \d 的前面和后面必须是回车，但是不吃掉回车
  --> '1\nOO\nOO\n'
  ```

   x(?!y)  否定式向后查找 x 后面不能是y





## ^| 整个串必须在开头的位置或前面有\n接除\n外的其他空白



```
# 整个串必须在开头的位置或前面有\n接除\n外的其他空白
# ^ 符号表示整个串的位置是出现在开头，它的前面没有任何其他的东西
let s = `#abc #def
  ##ghi

###jkl 
####mno #pqr

`
let matchs = s.matchAll(new RegExp(String.raw`(?:^|\n)[^\r\n\S]*(#[\s\S]+?)(?=\n)`, 'g'))
let arr = Array.from(matchs)
arr.forEach((match)=>{

    let g2 = match[1]
    console.log(g2)

})
```

- (?:^|\n)  整个串或者出现在开头，或都前面必有一个 \n 
- ?: 表示这不是一个分组
- \s 表示空白字符，\S 表示非空白字符
- [^\r\n\S]*  表示 既不是\r 又不是 \n 还不是非空白字符，就只能是 **除\r \n 以外的其他所有空白了**



## 命名捕获组



`(?<name>group)` 或 `(?'name'group)`，其中`name`表示捕获组的名称，`group`表示捕获组里面的正则。



#### 反向引用

\k<name> 或 \k'name'的形式来对前面的命名捕获组捕获到的值进行引用。如之前的

```
(\d{2})\1
可以改写为
(?<key>\d{2})\k<key>
```







## replace



```javascript
var strs = fs.readFileSync(fdoc, "utf8")

strs = strs.replace(/\*\*\*\*\*\*\*\*\*\*/g, '').replace(/\r\n/g, '\n').replace(/\t/g, '  ').trim()
strs = '\n\n' + strs +  '\n\n'
```



### 引用

```javascript
let strs = '中  文'
let r = strs.replace(new RegExp(String.raw`([^a-z^A-Z^\s])\s+([^a-z^A-Z^\s])`), '$1$2')
```







## Iterator 转数组



```javascript
    let regexp = new RegExp(p,'g');
    let matches = strs.matchAll(regexp);

    let arr = Array.from(matches)
    for (let i = 0; i < arr.length; i++) {
        let match = arr[i]
        console.log(`Found ${match[0]} start=${match.index} end=${match.index + match[0].length}.`);
    }
```



## split by



```javascript
 arrans = anss.split(new RegExp( String.raw`[\s、，\,]`) )
```



## 过滤汉字里的标点符号

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Unicode_Property_Escapes

  > Unicode property escapes

- https://www.jianshu.com/p/fcbc5cd06f39

  > Unicode 编码 Emoji CJK 中文 汉字 过滤正则

```
a= '有效的。effctive“有效的，起作用的”；viual“视觉的，视力的”；crical“挑剔的”；ineviable“必然的，不可避免'
a.replace(/\p{P}/gu, '')  # 成功云掉了中文标点
> '有效的effctive有效的起作用的viual视觉的视力的crical挑剔的ineviable必然的不可避免'


> a.replace(/[\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]/g, '')
'。effctive“，”；viual“，”；crical“”；ineviable“，'

\pP 其中的小写 p 是 property 的意思，表示 Unicode 属性，用于 Unicode 正表达式的前缀。

大写 P 表示 Unicode 字符集七个字符属性之一：标点字符。

'A ticket to 大阪 costs ¥2000 👌.'.replace(/\p{Sc}|\p{P}/gu, '')




```

`定义范围`是Unicode指定的字符区间，`实际范围`是当前版本真正使用的区间，没使用的区间在后续版本更新会被使用，所以过滤规则已定义范围为准。
 `〇` 虽然在符号区但属于汉字。
 易经六十四卦符号不属于汉字。

包含兼容和扩展字符

| 过滤内容       | 正则                                                         |
| -------------- | ------------------------------------------------------------ |
| CJK 汉字和符号 | [\u2E80-\uA4CF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F\uFF00-\uFFEF] |
| CJK 标点符号   | [\u3000-\u3006\u3008-\u303F\uFE10-\uFE1F\uFE30-\uFE4F\uFF00-\uFFEF] |
| 中文汉字和符号 | [\u2E80-\u2FFF\u3000-\u303F\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F\uFF00-\uFFEF] |
| 仅中文汉字     | [\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF] |

常用其它过滤判断



```csharp
CJK 常用汉字和符号(无全角内容)  
[\u2E80-\uA4CF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F]  

CJK 汉字和符号(无竖排符号)  
[\u2E80-\uA4CF\uF900-\uFAFF\uFF00-\uFFEF]  

CJK 汉字和符号(无竖排符号和全角)  
[\u2E80-\uA4CF\uF900-\uFAFF]  

CJK 汉字(无符号和全角)  
[\u3007\u2E80-\u2FFF\u3040-\uA4CF\uF900-\uFAFF]  

中文汉字和符号(无全角内容)  
[\u2E80-\u2FFF\u3000-\u303F\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F]
```

不含兼容和扩展字符

| 过滤内容       | 正则                                      |
| -------------- | ----------------------------------------- |
| CJK 标点符号   | [\u3000-\u3006\u3008-\u303F\uFF00-\uFFEF] |
| 中文汉字和符号 | [\u3000-\u303F\u4E00-\u9FFF\uFF00-\uFFEF] |
| 仅中文汉字     | [\u3007\u4E00-\u9FFF]                     |

大于4字不同语言符处理方式不同，可根据需要决定是否添加



```csharp
#| 20000-2A6DF | CJK统一表意文字扩展B |
#| 2A700-2EBE0 | CJK统一表意文字扩展C-F |
#| 2F800-2FA1F | CJK兼容表意文字扩展 |
#| 30000~3134A | CJK统一表意文字扩展G |

#OC
[\U00020000-\U0002A6DF\U000A700-\U0002EBE0\U0002F800-\U0002FA1F\U00030000-\U0003134A]

#Java
[\x{20000}-\x{2A6DF}\x{2A700}-\x{2EBE0}\x{2F800}-\x{2FA1F}\x{30000}-\x{3134A}]

#JavaScript
[\u{20000}-\u{2A6DF}\u{2A700}-\u{2EBE0}\u{2F800}-\u{2FA1F}\u{30000}-\u{3134A}]
```

emoji

参考[emoji-regex](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Femoji-regex)的正则分为3种标准 [RGI标准](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmathiasbynens%2Femoji-regex%2Fblob%2F61%2Fes2015%2FRGI_Emoji.js)  、[旧标准](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmathiasbynens%2Femoji-regex%2Fblob%2F61%2Fes2015%2Findex.js)  、[旧标准+文字类型](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmathiasbynens%2Femoji-regex%2Fblob%2F61%2Fes2015%2Ftext.js)  。
 但是这里 `文字类型(无彩色Icon)`  的emoji 把 `#*0-9` 也算在内并不正确。
 修改后最终的规则可以参考这里[emoji_regex.dart](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fwittyneko%2Femoji_regex%2Fblob%2Fmaster%2Flib%2Femoji_regex.dart)。

[Full Emoji List](https://links.jianshu.com/go?to=https%3A%2F%2Funicode.org%2Femoji%2Fcharts%2Ffull-emoji-list.html)
 [emoji history index](https://links.jianshu.com/go?to=https%3A%2F%2Funicode.org%2FPublic%2Femoji%2F)
 [emoji-test.txt](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.unicode.org%2FPublic%2Femoji%2F13.0%2Femoji-test.txt)



```
# 好像只有java 可以
str = str.replaceAll("\\pP", "")

Unicode 编码并不只是为某个字符简单定义了一个编码，而且还将其进行了归类。

\pP 其中的小写 p 是 property 的意思，表示 Unicode 属性，用于 Unicode 正表达式的前缀。

大写 P 表示 Unicode 字符集七个字符属性之一：标点字符。

其他六个是

L：字母；
M：标记符号（一般不会单独出现）；
Z：分隔符（比如空格、换行等）；
S：符号（比如数学符号、货币符号等）；
N：数字（比如阿拉伯数字、罗马数字等）；
C：其他字符

上面这七个是属性，七个属性下还有若干个子属性，用于更进一步地进行细分。

Unicode 正则表达式标准（可以找到所有的子属性）
http://www.unicode.org/reports/tr18/

各 Unicode 字符属性的定义，可以用一看看某个字符具有什么属性。
http://www.unicode.org/Public/UNIDATA/UnicodeData.txt

这个文本文档一行是一个字符，第一列是 Unicode 编码，第二列是字符名，第三列是 Unicode 属性，
以及其他一些字符信息。
```





# String



## match



```javascript
> '###'.match(/#+/)
[ '###', index: 0, input: '###', groups: undefined ]
> 'a'.match(/#+/)
null
```



## 不转义



```javascript
String.raw `Hi\u000A!`;
```



## 动态计算



```javascript
`${type}Mid`
`Found ${match[0]} start=${match.index} end=${match.index + match[0].length}.`
```



## indexOf



```
The index of the first occurrence of searchString found, or -1 if not found
```





## Replace



```javascript
// replaceAll node v15 才有，这里自定义之

        String.prototype.replaceAll = function(search, replacement) {
            var target = this
            return target.replace(new RegExp(search, 'g'), replacement)
        }
      
        strs = strs.trim()
        strs = '\n\n' + strs +  '\n\n'
        strs = strs.replaceAll('\xa0', "\n").replaceAll("Ｂ", "B").replaceAll("Ｄ", "D")
```



### 全角转半角

```javascript
    function fullWidth_to_halfWidth(str) {

        let d = {
            'Ａ':'A', 'Ｂ':'B', 'Ｃ':'C', 'Ｄ':'D', 'Ｅ':'E', 'Ｆ':'F', 'Ｇ':'G', 'Ｈ':'H', 'Ｉ':'I', 'Ｊ':'J', 'Ｋ': 'K', 'Ｌ':'L', 'Ｍ':'M', 'Ｎ':'N', 'Ｏ':'O', 'Ｐ':'P', 'Ｑ':'Q', 'Ｒ':'R', 'Ｓ':'S', 'Ｔ':'T', 'Ｕ':'U', 'Ｖ':'V', 'Ｗ':'W', 'Ｘ':'X', 'Ｙ':'Y', 'Ｚ':'Z',
            'ａ':'a', 'ｂ':'b', 'ｃ':'c', 'ｄ':'d', 'ｅ':'e', 'ｆ':'f', 'ｇ':'g', 'ｈ':'h', 'ｉ':'i','ｊ':'j', 'ｋ':'k', 'ｌ':'l', 'ｍ':'m', 'ｎ':'n', 'ｏ':'o', 'ｐ':'p', 'ｑ':'q', 'ｒ':'r', 'ｓ':'s', 'ｔ':'t', 'ｕ':'u', 'ｖ':'v', 'ｗ':'w', 'ｘ':'x', 'ｙ':'y', 'ｚ':'z'
        }
        
        for (let [f, h] of Object.entries(d)) {
            
            let reg = new RegExp(`${f}`, 'g')
            str = str.replace(reg, h)

        }

        return str

    }
```



### 特殊字符

```
常用上标 ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ º ˙

常用下标₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₊ ₋ ₌ ₍ ₎ ₐ ₑ ₒ ₓ ₔ ₕ ₖ ₗ ₘ ₙ ₚ ₛ ₜ

更多上标 ᵃ ᵇ ᶜ ᵈ ᵉ ᵍ ʰ ⁱ ʲ ᵏ ˡ ᵐ ⁿ ᵒ ᵖ ᵒ⃒ ʳ ˢ ᵗ ᵘ ᵛ ʷ ˣ ʸ ᙆ ᴬ ᴮ ᒼ ᴰ ᴱ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴼ ᴾ ᴼ̴ ᴿ ˢ ᵀ ᵁ ᵂ ˣ ᵞ ᙆ ꝰ ˀ ˁ ˤ ꟸ ꭜ ʱ ꭝ ꭞ ʴ ʵ ʶ ꭟ ˠ ꟹ ᴭ ᴯ ᴲ ᴻ ᴽ ᵄ ᵅ ᵆ ᵊ ᵋ ᵌ ᵑ ᵓ ᵚ ᵝ ᵞ ᵟ ᵠ ᵡ ᵎ ᵔ ᵕ ᵙ ᵜ ᶛ ᶜ ᶝ ᶞ ᶟ ᶡ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᶬ ᶭ ᶮ ᶯ ᶰ ᶱ ᶲ ᶳ ᶴ ᶵ ᶶ ᶷ ᶸ ᶹ ᶺ ᶼ ᶽ ᶾ ᶿ ꚜ ꚝ ჼ ᒃ ᕻ ᑦ ᒄ ᕪ ᑋ ᑊ ᔿ ᐢ ᣕ ᐤ ᣖ ᣴ ᣗ ᔆ ᙚ ᐡ ᘁ ᐜ ᕽ ᙆ ᙇ ᒼ ᣳ ᒢ ᒻ ᔿ ᐤ ᣖ ᣵ ᙚ ᐪ ᓑ ᘁ ᐜ ᕽ ᙆ ᙇ ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ˂ ˃ ⁽ ⁾ ˙ * º

更多下标 ₐ ₔ ₑ ₕ ᵢ ⱼ ₖ ₗ ₘ ₙ ₒ ₚ ᵣ ₛ ₜ ᵤ ᵥ ₓ ᙮ ᵤ ᵩ ᵦ ₗ ˪ ៳ ៷ ₒ ᵨ ₛ ៴ ᵤ ᵪ ᵧ

中文上标 ㆒㆓㆔㆕㆖㆗㆘㆙㆚㆛㆜㆝㆞㆟

特殊字符 ：
、。·ˉˇ¨〃々—～‖…‘’“”〔〕〈〉《》「」『』〖〗【】±×÷∶∧∨∑∏∪∩∈∷√⊥∥∠⌒⊙∫∮≡≌≈∽∝≠≮≯≤≥∞∵∴♂♀°′″℃＄¤￠￡‰§№☆★○●◎◇◆□■△▲※→←↑↓〓〡〢〣〤〥〦〧〨〩㊣㎎㎏㎜㎝㎞㎡㏄㏎㏑㏒㏕︰￢￤℡ˊˋ˙–―‥‵℅℉↖↗↘↙∕∟∣≒≦≧⊿═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╭╮╯╰╱╲╳▁▂▃▄▅▆▇�█▉▊▋▌▍▎▏▓▔▕▼▽◢◣◤◥☉⊕〒〝〞

罗马字符：
ⅰ ⅱ ⅲ ⅳ ⅴⅵ  ⅶ  ⅷ ⅸⅹ
Ⅰ Ⅱ Ⅲ  Ⅳ  Ⅴ Ⅵ Ⅶ Ⅷ Ⅸ Ⅹ Ⅺ Ⅻ

数字字符：⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇①②③④⑤⑥⑦⑧⑨⑩㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩

拼音字符：
āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü

希腊字母
ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω

```



### replace函数还可以有回调

```
// Escape a string for use as text in an HTML document
String.prototype.$escape = function() {
  return this.replace(/[&<>"']/g, function(m) {
    switch (m) {
      case '&': return '&amp;';
      case '<': return '&lt;';
      case '>': return '&gt;';
      case '"': return '&quot;';
      case '\'': return '&#039;';
      default: assert.fail(`Should escape character ${m}`);
    }
  });
 
}
```





## split

```javascript
const splits = myString.split(' ', 3)
```



## slice

```
url = '/pull/test'
const id = url.slice(6)  
> 'test'
```



## includes



```
if (text.includes(word)) {}
```





## 最长公共前缀

- https://github.com/burgaard/string-algorithms
  - longest common prefixes 

```javascript
npm i string-algorithms

(async () => {
    let { longestCommonSubstring } = await import('string-algorithms')
    const strings = [
        '12apple',
        '3apple4',
        'apple56'
    ];
    console.log(longestCommonSubstring(strings))  // 这不是公共前缀，而是公共子串
})()
```



- https://github.com/sisterAn/JavaScript-Algorithms/issues/19

```javascript
    // 公共指针法
    function longestCommonPrefix(strs) {
        if (!strs || !strs.length) {
            return '';
        }

        // 从0开始依次比较
        let currentIndex = 0;

        while (true) {
            // 取第一个字符串的当前位字符作为参照
            const refer = strs[0][currentIndex];
            // 是否全部匹配
            const currentAllMatch = strs.reduce((pre, str) => {
                return pre && str.charAt(currentIndex) === refer;
            }, true);

            if (currentAllMatch) {
                currentIndex++;
            } else {
                break;
            }
        }

        return strs[0].substring(0, currentIndex);
    }

    console.log(longestCommonPrefix(["flower","flow","flight"]))
```



## 编辑距离

- https://github.com/hiddentao/fast-levenshtein

  > ``` 
  > npm install fast-levenshtein --save
  > 
  > var levenshtein = require('fast-levenshtein');
  > 
  > var distance = levenshtein.get('back', 'book');   // 2
  > var distance = levenshtein.get('我愛你', '我叫你');   // 1
  > ```



## NGram

```javascript
    // NGram
    NG: function (strs) {

        strs = strs.replaceAll(String.raw`\s`, '')

        function ng(s, n) {

            var grs = []

            for (let i = 0; i < s.length; i++) {

                if (i + n > s.length) {
                    break
                }

                var gr = s.substring(i, i + n)

                grs.push(gr)


            }

            return grs

        }

        var gss = []
        for (let i = 1; i <= 10; i++) {

            let gs = ng(strs, i)

            if (gs.length > 0) {

                gss = gss.concat(gs)

            } else {

                break

            }

        }

        return gss

    }
```



```javascript
# 处理允许存在特殊字符的情况，因为它们是天然的分隔符，对于分词是有用的
		let ng = NG(text)
        let ng2 = []

        for (let g of ng) {

          let g2 = g.replace(/\s/g, '').replace(/\p{P}/gu, '')  // 去掉空格，去掉中文标点

          if (g2.length == g.length) {
            ng2.push( g )
          } else {
            let a = 1
          }

        }
```





## diff



```javascript
require('colors')

const Diff = require('diff');

const one = 'beep boop'
const other = 'beep boob blah'

const diff = Diff.diffChars(one, other)

for (let d of diff) {

    // green for additions, red for deletions
    // grey for common parts
    const color = d.added ? 'green' :
        d.removed ? 'red' : 'grey'
    process.stderr.write(d.value[color])

}

console.log()
```



## CJK Symbols

- https://en.wiktionary.org/wiki/Category:CJK_Symbols_and_Punctuation_block



## 检测字符编码

```
// doc\lang\programming\nodejs\pmserver\lib\ssa.js
let chardet = require('chardet')
let encode = chardet.detect(Buffer.from( require('fs').readFileSync(sapath) 
sa = fs.readFileSync(sapath, { encoding:encode})  // encode
```



## 转换字符编码

```
"iconv-lite": "^0.4.24"

let senddata = iconv.encode(JSON.stringify(param) + "\r\n", 'gbk');
this.childprocess.stdin.write(senddata);
```



```
'use strict';
const child_process = require("child_process")
const iconv = require('iconv-lite');
const extend = require('util')._extend;
const EventEmitter = require('events').EventEmitter;
const path = require('path');

let S4 = () => {
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
};

let guid = () => {
    return (S4() + S4() + S4() + S4());
};


/**
 * 
 */
class NodeSharp extends EventEmitter {
    constructor(option) {
        super();
        this.childprocess = null;
        this.onceListenters = {};
        this.onListenters = {};
        this._needReOpen = false;
        this.opt = {};

        let defaultOpt = {
            exePath: '',
            autoReOpen: false,
            args: [],
            dataListener: null,
            errorListener: null
        };

        if (typeof option == 'string') {
            defaultOpt.exePath = option;
            this.opt = defaultOpt;
        } else {
            this.opt = extend(defaultOpt, option);
        }
        if (this.opt.dataListener) {
            this.on('data', dataListener)
        }
        if (this.opt.errorListener) {
            this.on('error', errorListener)
        }
    }

    /**
     * start a exe and connect
     * @param {*} option exePath OR {exePath，autoReOpen，args, dataListener, errorListener }
     */
    static connect(option) {
        let exe = new this(option)
        exe.open();
        return exe;
    }



    open() {
        let exec = child_process.spawn;
        let exepath = path.resolve(__dirname, this.opt.exePath);
        this.childprocess = exec(exepath, this.opt.args);
        this.childprocess.stdin.setEncoding("binary");
        this.childprocess.stdout.setEncoding("binary");
        if (this.childprocess == null && this.opt.closeCallback)
            this.opt.closeCallback(-1);
        this.childprocess.on('exit', (code, signal) => {
            if ((this.opt.autoReOpen && signal !== 'SIGTERM') || this._needReOpen)
                setTimeout(function () {
                    this.open();
                    this.emit('reopen', this);
                }.bind(this), 1000);
            this._needReOpen = false;
            this.emit('close', code, this.trueClose);
        });

        this.childprocess.stdout.on('data', (data) => {
            this.emit('message', data);
            let json = '';
            try {
                json = data.toString();

                let jsondata = "";
                try {
                    jsondata = JSON.parse(json);
                } catch (_ee) {
                    return
                }
                if (this.onceListenters[jsondata.Pid]) {
                    this.onceListenters[jsondata.Pid](jsondata.Error, jsondata.Data);
                    delete this.onceListenters[jsondata.Pid];
                }
                if (this.onListenters[jsondata.Pid]) {
                    this.onListenters[jsondata.Pid](jsondata.Error, jsondata.Data);
                }
                this.emit('data', jsondata.Error, jsondata.Data);

            } catch (e) {
                this.emit('error', e);
            }
        });
        this.childprocess.stdout.on('error', e => {
            console.error(e)
            this.emit('error', e)
        })
        this.childprocess.stdin.on('error', e => {
            console.error(e)
            this.emit('error', e)
        })
    };

    close() {
        this._needReOpen = false;
        if (!this.childprocess.killed) {
            this.childprocess.kill('SIGTERM');
        }
    };

    reOpen() {
        this._needReOpen = true;
        if (!this.childprocess.killed) {
            return this.childprocess.kill();
        }
        this.open();
    }

    buildParam(obj) {
        return {
            pid: guid(),
            data: obj
        }
    }

    send({
        param,
        once,
        on
    }) {
        if (!this.childprocess && (once || on))
            return (once || on)('The required process has not started');
        if (!this.childprocess.stdin.writable && (once || on))
            return (once || on)('Unable to establish channel connection');
        param = this.buildParam(param);
        if (once) {
            this.onceListenters[param.pid] = once;
        }
        if (on) {
            this.onListenters[param.pid] = on;
        }
        let senddata = iconv.encode(JSON.stringify(param) + "\r\n", 'gbk');
        this.childprocess.stdin.write(senddata);
    };
}

module.exports = NodeSharp;
```





## 语言检测

- https://github.com/wooorm/franc 中英混合检测不准确，只有一种语言还可以
- https://github.com/dachev/node-cld



```
(async()=>{

  const cld = require('cld');


  //let text = `string code = $"let lang = francAll({text}", [@"{ only:['jpn','cmn','eng'」}"})ln"+ @"//console.log(fs）//fs 是事先 import 好的模块，这里可以直接用所有可用参数都在这里展开了：，.·params//console.log(franc)//console. log(' hello, from vm)returncallback（【msg：'hi，，，，lang）//约定最后以callback返回值`
  
  //let text = `aabbccxxxxxxxxxxxxxxxxxxxxxxxxxxxxaaaaaaaabbbbvcxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

  let text = `中文`

  let { franc, francAll } = await import('franc')

  let lang = francAll(text, { only: ['jpn','cmn', 'eng'], minLength: 1 })

  //const result = await cld.detect(text);
  //console.log(result);

  let a = 1

})()
```





```
github 
	echodict\cut\langDetect.js
	echodict\pmserver\lib\langDetect.mjs
	
// https://github.com/wooorm/franc/tree/main/packages/franc-all


// npm install @kaciras/deasync
// npm install franc

const { deasync } = require("@kaciras/deasync");
const { performance } = require('perf_hooks')

const langDetect = deasync((text, option, done) => {
    (async () => {
        let { franc, francAll } = await import('franc')
        let lang = francAll(text, option) // { only: ['jpn', 'cmn', 'eng'] }
        // cmn	Mandarin Chinese
        // eng	English	
        // rus	Russian
        // jpn	Japanese
        // fra	French	
        // deu	German
        // lat	Latin
        // san	Sanskrit

        done(null, lang)
    })()
});

console.log("Timestamp before: " + performance.now());
let re = langDetect('Alle menslike wesens word vry', { only: ['jpn', 'cmn', 'eng'] })
console.log("Timestamp after: " + performance.now());
```





## time

```
const moment = require('moment')
let timestamp = moment().format('YYYY-MM-DD HH:mm:ss')
```



```
OperateTime:new Date()

OperateTime = new Date(OperateTime)
let lasttime = dic_test[key].OperateTime
if (lasttime > OperateTime) {
```





## guid

```
const uuid = require('uuid')
let guid = uuid.v4()

```







# Array



## join



```
# 连成字符串，中间加空格
const arr = ['Fire', 'Air', 'Water'];
console.log(arr.join(' '));
```



## concat

```
const array1 = ['a', 'b', 'c'];
const array2 = ['d', 'e', 'f'];
const array3 = array1.concat(array2);

console.log(array3);
// expected output: Array ["a", "b", "c", "d", "e", "f"]
```





## 遍历



```
const array1 = ['a', 'b', 'c'];

for (const element of array1) {
  console.log(element);
}
```



```
const iterable = new Map([['a', 1], ['b', 2], ['c', 3]]);

for (const entry of iterable) {
  console.log(entry);
}
// ['a', 1]
// ['b', 2]
// ['c', 3]

for (const [key, value] of iterable) {
  console.log(value);
}
// 1
// 2
// 3
```





```
arr.forEach(element => {
  console.log(element);
});
```





## sort



```javascript
// 双排序，类似C# 的 order by then by
// Lodash 4.x:
data = _.orderBy(data, [
  function (item) { return item.sortData.a; },
  function (item) { return item.sortData.b; }
], ["asc", "desc"]);
```



## reverse

```
const _ = require("lodash")
array = _.reverse( array )
```





## group by



```javascript
const _ = require("lodash")
       
// Original array 
var users = (['one', 'two', 'three', 'four'])
var obj = ([ 3.1, 1.2, 3.3 ])
   
// Using the _.groupBy() method
// with the `_.property` iteratee shorthand 
let grouped_data = _.groupBy(users, 'length')
let grouped_data2 = _.groupBy(obj, Math.floor)
```



## chunk

```
let arr_new = _.chunk(array, [size=1])
```



## shuffle

```
arr = _.shuffle(arr)
```



## includes

```
const pets = ['cat', 'dog', 'bat']
console.log(pets.includes('cat'))
// expected output: true
```



## filter

```
                    Data2 = Data2.filter( item => {
                    
                        if ( len_rate <= 0.35 ) {
                            return false
                        }

                        return true
                    })
                    

delImg (f) {
      console.log('删除图片')
      this.files = this.files.filter(item => item !== f)  // ture 留, false 去
    }
    
    // 带 index 参数
    this.usingBlocks = this.usingBlocks.filter((item, index) => { return index !== i }) // ture 留, false 去
    
    this.usingBlocks = this.usingBlocks.splice(i, 1)  // 不知道为什么删不掉
    
```





## intersection



```
let _ = require('lodash')
let newArray = _.intersection( array1, array2)
```



## union

```
let _ = require('lodash')
let newArray = _.union([20, 12], [8, 15, 6])
```



## Float32Array.from

```
const dataA = Float32Array.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]);
```





# json



## 遍历



```javascript
for (let key in paramsDefined) {
}
```



```javascript
1238

Under ECMAScript 5, you can combine Object.keys() and Array.prototype.forEach():

var obj = { first: "John", last: "Doe" };

Object.keys(obj).forEach(function(key) {
    console.log(key, obj[key]);
});
ECMAScript 6 adds for...of:

for (let key of Object.keys(obj)) {
    console.log(key, obj[key]);
}
ECMAScript 8 adds Object.entries() which avoids having to look up each value in the original object:

Object.entries(obj).forEach(
    ([key, value]) => console.log(key, value)
);
You can combine for...of, destructuring, and Object.entries:

for (let [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
Both Object.keys() and Object.entries() iterate properties in the same order as a for...in loop but ignore the prototype chain. Only the object's own enumerable properties are iterated.
```



## exist



```javascript
if ( !(keyParent in menus) ) {
```



## isEmpty



```javascript
let _ = require('lodash')
_.isEmpty(dic_ansers)
```



## 加料

```
  opts = {
    [kStandaloneREPL]: true,  // [] 是因为名字已存在吧？
    ignoreUndefined: false,
    useGlobal: true,
    breakEvalOnSigint: true,
    ...opts	// 原先的值在这里展开
  }
```







## Object.assign



```javascript
let data = {}
Object.assign(data, query) // 赋值
```



## deep copy

```
let _ = require('lodash');
var deepCopy = _.cloneDeep(obj)
```







## 函数默认值

- https://es6.ruanyifeng.com/#docs/function#
  - 解构赋值默认值结合使用



```
function foo({x, y = 5} = {}) {
  console.log(x, y);
}
foo() // undefined 5
// 如果没有提供参数，函数foo的参数默认为一个空对象
```



## _.valuesIn

```
_.valuesIn(obj)
```



## 后面参数全部从第一参展开得到

```
function REPLServer(prompt,
                    stream,
                    eval_,
                    useGlobal,
                    ignoreUndefined,
                    replMode) {
  let options;
  if (prompt !== null && typeof prompt === 'object') {
    // An options object was given.
    options = { ...prompt };
    stream = options.stream || options.socket;
    eval_ = options.eval;
    useGlobal = options.useGlobal;
    ignoreUndefined = options.ignoreUndefined;
    prompt = options.prompt;
    replMode = options.replMode;
  } else {
    options = {};
  }                    
                
```







# File



## exist



```
fs.existsSync( path )
```



## __dirname

- 代表当前 js 文件所在目录

```
require('path').join(__dirname, 'temp.json')
```



## create dir

```
fs.existsSync( path )
fs.mkdirSync(targetDir, { recursive: true })
```



## read write



```
require('fs').writeFileSync('menu.json', JSON.stringify(menujson), {encoding:'utf8', flag:'w'} )
```

```
require('fs').readFileSync('./input.txt',{encoding:'utf8', flag:'r'})
```

```
fs.createWriteStream(path).write(buffer)
```



## read line by line

```javascript

// 原始语料在 doc\lang\programming\pytorch\机器翻译\中英平行语料520万_translation2019zh  格式是：每行一个JSON 文本， 有两个字段 english 和 chinese 
// 转换为 OpenNMT-py 格式，英文一个文件，中文一个文件

(async () => {

    function clean(str) {
        return str.replace(/\r\n/g, '\n').replace(/\n{2,999}/g, '\n')
    }

    async function convert(fpath1, fpath2) {

        let { msg } = await new Promise(async function (resolve, reject) {

            let fs = require('fs')
            let _ = require('lodash')

            let c1 = _.chunk([1, 2, 3, 4, 5], 3)

            fs.rmSync('en_chs', { recursive: true, force: true })
            fs.mkdirSync('en_chs', { recursive: true })

            // var src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            // var tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_val = fs.createWriteStream('en_chs/src-val.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_val = fs.createWriteStream('en_chs/tgt-val.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_test = fs.createWriteStream('en_chs/src-test.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_test = fs.createWriteStream('en_chs/tgt-test.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)


            let src_trains = []
            let tgt_trains = []

            let src_vals = []
            let tgt_vals = []

            let src_tests = []
            let tgt_tests = []

            async function read_big_file(fpath, arr1, arr2) {

                let { msg } = await new Promise(function (resolve2, reject2) {

                    var buffer = '';
                    var rs = fs.createReadStream(fpath)
                    rs.on('data', function (chunk) {
                        var lines = (buffer + chunk).split(/\r?\n/g)
                        buffer = lines.pop()
                        for (var i = 0; i < lines.length; i++) {

                            let line = lines[i]
                            if (line.trim() != '') {
                                line = JSON.parse(line)
                                let english = line.english //clean(line.english)
                                english = english.replace(/(\,)/g, ' $1 ')  // OpenNMT 要通过空格分词，这里把标点和单词拆开
                                english = english.replace(/(\.)/g, ' $1 ')
                                english = english.replace(/(\?)/g, ' $1 ')
                                english = english.replace(/(\!)/g, ' $1 ')
                                english = english.replace(/([^\r\n\S]{2,999})/g, ' ')

                                let chinese = line.chinese // clean(line.chinese)
                                chinese = chinese.replace(/(\，)/g, ' $1 ')  // OpenNMT 要通过空格分词，这里把标点和单词拆开
                                chinese = chinese.replace(/(\、)/g, ' $1 ')
                                chinese = chinese.replace(/(\；)/g, ' $1 ')
                                chinese = chinese.replace(/(\：)/g, ' $1 ')
                                chinese = chinese.replace(/(\。)/g, ' $1 ')
                                chinese = chinese.replace(/(\？)/g, ' $1 ')
                                chinese = chinese.replace(/(\！)/g, ' $1 ')
                                chinese = chinese.replace(/(\《)/g, ' $1 ')
                                chinese = chinese.replace(/(\》)/g, ' $1 ')
                                chinese = chinese.replace(/(\“)/g, ' $1 ')
                                chinese = chinese.replace(/(\”)/g, ' $1 ')
                                chinese = chinese.replace(/(\‘)/g, ' $1 ')
                                chinese = chinese.replace(/(\’)/g, ' $1 ')
                                chinese = chinese.replace(/(\（)/g, ' $1 ')
                                chinese = chinese.replace(/(\）)/g, ' $1 ')




                                chinese = chinese.replace(/([^\r\n\S]{2,999})/g, ' ')
                                // chinese = chinese.replace(/(\p{P})/gu, ' $1 ')  // 正则匹配所有中文标点

                                // src_train.write(english + '\n') 
                                // tgt_train.write(chinese + '\n')

                                arr1.push(english + '\n')
                                arr2.push(chinese + '\n')

                            }

                        }
                    })
                    rs.on('end', function () {
                        // src_train.end()
                        // tgt_train.end()
                        //console.log(`done one task ${fpath}`)
                        return resolve2({ msg: 'ok.' })


                    })

                })

                return { msg }

            }

            let { msg: m1 } = await read_big_file(fpath1, src_trains, tgt_trains)
            let { msg: m2 } = await read_big_file(fpath2, src_vals, tgt_vals)


            async function writeSync(arr, steam) {

                for (let s of arr) {

                    steam.write(s)

                }

                await new Promise(async function (resolve_, reject_) {
                    steam.end(() => {
                        return resolve_('done.')
                    })
                })

                return {msg:'done'}

            }

            let chunks1 = _.chunk(src_vals, src_vals.length - 100)  // 分一百作测试集
            let chunks2 = _.chunk(tgt_vals, tgt_vals.length - 100)


            src_vals = chunks1[0]
            tgt_vals = chunks2[0]

            src_tests = chunks1[1]
            tgt_tests = chunks2[1]


            await writeSync(src_trains, src_train)
            await writeSync(tgt_trains, tgt_train)

            await writeSync(src_vals, src_val)
            await writeSync(tgt_vals, tgt_val)

            await writeSync(src_tests, src_test)
            await writeSync(tgt_tests, tgt_test)

            return resolve({ msg: 'ok.' })

        })


        let ens = 'file too large to return string'
        let chts = '文件太大，无法返回字符串'

        return { ens, chts }

    }

    let { ens, chts } = await convert('./translation2019zh_train.json', './translation2019zh_valid.json')

})()
```



## write line by line

```javascript
            var fs = require('fs')
            var src_train = fs.createWriteStream('src-train.txt', {flags: 'a' }) // 'a' means appending (old data will be preserved)
            src_train.write('some data') // append string to your file
            src_train.write('more data') // again
            src_train.write('and more') // again
```





## 去掉扩展名



```
imgName = path.parse(imgName).name  // 去掉扩展名
let { base,dir,ext,name,root} = path.parse(mlpath)
```



## rename

```
fs.renameSync( oldPath, newPath )
```



## 遍历目录读取word



```

# docx.js

let rd = require('rd');
let fs = require('fs');
let path = require("path")

var mammoth = require("mammoth")
//const AdmZip = require('adm-zip'); //引入查看zip文件的包

module.exports = {
    //
    // 目录下所有docx 的内容文本
    //
    contents : async function(dir) {

        var arr = []

        var paths = []

        // 目录下的所有文件名
        rd.eachFileFilterSync(dir, /\.docx$/, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (basename != "A1-3.docx") {
                return
            }

            paths.push(fullpath)
        })

        for (let i = 0; i < paths.length; i++) {
            let content = await getContent(paths[i])
            arr.push(content)
        }

        return arr
    }
}


function getContent(fileName) {
    return new Promise((resolve, err) => {
        // var url = path.join(__dirname, 'A1-3-2.docx');
        // var url = path.join(__dirname, "../../../file/" + fileName);
        var url = fileName
        mammoth.extractRawText({
                path: url
            })
            .then(function (result) {
                var text = result.value // The raw text
                var messages = result.messages
                resolve(text)

            })
            .catch((e) => {
                err(false)
            })
            .done()
    })
}
```



## 文件时间

- https://www.geeksforgeeks.org/node-js-fs-utimessync-method/







## 图片



```

		if (!fs.existsSync(gifpath)) {
          return [null, `图片不存在${gifpath}`]
        }

        let bytes = fs.readFileSync(gifpath)  // 'binary'
        let b64 = Buffer.from(bytes).toString('base64')  // new Buffer(bytes)
        b64s.push(b64)
        
        
        Buffer.from(b64, 'base64')
        
        
```



## platform



```javascript
    let platform = process.platform
    let platforms = [ 'win32', 'linux', 'darwin' ]
    if ( ! platforms.includes( platform ) ) {
        throw 'unknow os type.'
    }
```



# 多线程

- https://zhuanlan.zhihu.com/p/35353355

  > Node黑魔法之无痛用上多线程

- https://www.cnblogs.com/flydean/p/14310278.html
  
  > nodejs中使用worker_threads来创建新的线程 



## napajs



```
const { Worker, isMainThread, workerData } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename, { workerData: 'Hello, world!' });
} else {
  console.log(workerData);  // Prints 'Hello, world!'.
}
```



```
console.time('timeout test');
zone.execute(() => { while (true) {} }, [], { timeout: 50})
    .catch((error) => {
        console.timeEnd('timeout test');
    });
```





```
const napa = require("napajs");
const fs = require("fs");

const myUTFString="éóíúã’“";

const zone = napa.zone.create("zone", {workers: 1});
const store = napa.store.create("store");
store.set("string", myUTFString);

zone.broadcast(`
    function example () {
        const str = global.napa.store.get("store").get("string");
        console.log(str);
        return str;
    }
`);

zone.execute("", "example").then(result => {
    console.log(result.value)
});
```

```
n your case, the code can be updated like this:

myLib.prototype.deflate = async function (data, key, compress)  {
    var buffer = new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
    var result = await this.zone.execute('','deflateFunc', [buffer, key, compress])
    return result.value;
};

myLib.prototype.inflate = async function (data, key, compressed, type)  {
    var buffer = new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
    var result = await this.zone.execute('','inflateFunc', [buffer, key, compressed, type])
    return result.value;
};
EDIT: to explain why the stack happened.

The type Buffer in Node.js is implemented Uint8Array after Node 4.x. Thus TypedArray.prototype.length is available on a Buffer object.

The transported Buffer object in napa zone, however, as explained above, is treated as a plain object. It does not have a length property. There is some code similar to while (buf.length !== 0) { ... } in xxtea-node. It's always true (undefined !== 0 is always true) so the while loop will never break.
```





### global 

- https://github.com/microsoft/napajs/issues/26

```
var napa = require('napajs');
var zone = napa.zone.create('zone1');
function test() {
   console.log('hello world');
}
zone.broadcast(test.toString());
zone.execute(() => { global.test(); }, []);
```



### timeout

```javascript
var napa = require("napajs")

const NUMBER_OF_WORKERS = 1

var zone = napa.zone.create('zone', { workers: NUMBER_OF_WORKERS })

// var p1 = zone.execute("", "fibonacci", [n - 1])

zone.execute(() => { while (true) {} }, [], { timeout: 3000})
    .catch((error) => {
        console.log(`end.`)
    });

console.log('hi,,,')
```



### calc fibonacci

```
//fibonacci.js
var napa = require("napajs");

// Change this value to control number of napa workers initialized.
const NUMBER_OF_WORKERS = 4;

// Create a napa zone with number_of_workers napa workers.
var zone = napa.zone.create('zone', { workers: NUMBER_OF_WORKERS });

/*
Fibonacci sequence 
n:              |   0   1   2   3   4   5   6   7   8   9   10  11  ...
-------------------------------------------------------------------------
NTH Fibonacci:  |   0   1   1   2   3   5   8   13  21  34  55  89  ...
*/
function fibonacci(n) {
    if (n <= 1) {
        return n;
    }

    var p1 = zone.execute("", "fibonacci", [n - 1]);
    var p2 = zone.execute("", "fibonacci", [n - 2]);

    // Returning promise to avoid blocking each worker.
    return Promise.all([p1, p2]).then(([result1, result2]) => {
        return result1.value + result2.value;
    });
}

function run(n) {
    var start = Date.now();

    return zone.execute('', "fibonacci", [n])
        .then(result => {
            printResult(n, result.value, Date.now() - start);
            return result.value;
        });
}

function printResult(nth, fibonacci, ms) {
    console.log('\t' + nth
          + '\t' + fibonacci
          + '\t\t' + NUMBER_OF_WORKERS
          + '\t\t' + ms);
}

console.log();
console.log('\tNth\tFibonacci\t# of workers\tlatency in MS');
console.log('\t-----------------------------------------------------------');

// Broadcast declaration of 'napa' and 'zone' to napa workers.
zone.broadcast(' \
    var napa = require("napajs"); \
    var zone = napa.zone.get("zone"); \
');
// Broadcast function declaration of 'fibonacci' to napa workers.
zone.broadcast(fibonacci.toString());

// Run fibonacci evaluation in sequence.
run(10)
.then(result => { run(11)
.then(result => { run(12)
.then(result => { run(13)
.then(result => { run(14)
.then(result => { run(15)
.then(result => { run(16)
}) }) }) }) }) })
```



### 并行快排

- https://github.com/microsoft/napajs/blob/master/examples/tutorial/parallel-quick-sort/parallel-quick-sort.js




# stream

- http://nodejs.cn/api/stream/stream_pipeline_streams_callback.html

```
var http = require('http'),
    url = require('url'),
    fs   = require('fs'),
    filePath = '/home/risto/Downloads/oleg.mp3',
    stat = fs.statSync(filePath);

http.createServer(function(request, response) {
    var queryData = url.parse(request.url, true).query;
    const skip = typeof(queryData.skip) == 'undefined' ? 0 : queryData.skip;
    const startByte = stat.size * skip;

    response.writeHead(200, {
        'Content-Type': 'audio/mpeg',
        'Content-Length': stat.size - startByte
    });

    // We replaced all the event handlers with a simple call to util.pump()
    fs.createReadStream(filePath, {start:startByte}).pipe(response);
})
.listen(2000);
```

```
var http = require('http'),
    url = require('url'),
    fs   = require('fs'),
    filePath = '/home/risto/Downloads/oleg.mp4',
    stat = fs.statSync(filePath);

http.createServer(function(request, response) {        
    const fileSize = stat.size;
    const range = request.headers.range;
    if (range) {
      const parts = range.replace(/bytes=/, "").split("-");
      const start = parseInt(parts[0], 10);
      const end = parts[1] 
        ? parseInt(parts[1], 10)
        : fileSize - 1;
      const chunksize = (end - start) + 1;
      const readStream = fs.createReadStream(filePath, { start, end });
      const head = {
        'Content-Range': `bytes ${start}-${end}/${fileSize}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunksize,
        'Content-Type': 'video/mp4',
      };
      response.writeHead(206, head);
      readStream.pipe(response);
    } else {
      const head = {
        'Content-Length': fileSize,
        'Content-Type': 'video/mp4',
      };
      response.writeHead(200, head);
      fs.createReadStream(filePath).pipe(response);
    }
})
.listen(2000);
```





# process



```
The argument to execa is a command followed by an array of arguments, unless the shell: true option is used. So this should be either execa('npm', ['run', 'start']) or execa('npm run start', { shell: true }).

// 不要忘记 -y 参数，否则或一直等你确认是否覆盖文个
import { execa } from 'execa'
import path from 'path'
import { dirname } from 'path'
//global.__dirname = process.cwd()
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

export default {
    extractSubtitle: async function (vdpath, type, nth) {

        try {

            let args = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} ${path.join( __dirname, tmp.srt )}`
            let subprocess = execa(args, {shell:true})
            await subprocess

        } catch(err) {
            a = 1
        }

        return 'hi,,,'
    }
}

```



```
// https://github.com/sindresorhus/execa/
let subprocess = execa('dir', [''], { 'encoding': 'utf8' })
        //let subprocess = execa('ffmpeg', ['-i', vdpath, 'tmp.srt'], { 'encoding': 'utf8' }) // [ '-i', vdpath, '-map', `0:s:${nth}`, 'tmp.srt']
        subprocess.stdout.pipe(process.stdout);
        let { stdout } = await subprocess
        console.log('child output:', stdout)

        await subprocess
```





```
var exec = require('child_process').exec;  // 出错
	//   "type": "commonjs",  // package.json 加上这一句
```



```
# https://github.com/sindresorhus/execa/issues/145
const { stdout: customPath2 } = execa.shellSync(
  'git config --get core.hooksPath  &2>/dev/null'
)
console.log('Path, ', customPath2)
```



```
var spawn = require('child_process').spawn;
var path = require('path');
var fs = require('fs');

var barPath = path.join(__dirname, 'child.js');
var outputPath = path.join(__dirname, 'output.txt');

var s = fs.createWriteStream(outputPath);

s.on('open', () => {
	spawn(process.execPath, [barPath], {
		stdio: [null, s, null]
	});
});
```



##  全局错误

```
//捕获全局未捕捉的错误
process.on('uncaughtException', function (erro) {
    console.error('##### 全局错误:');
    console.error(erro);
})
```





## 失败重试



```
// https://github.com/sindresorhus/execa
import pRetry from 'p-retry';

const run = async () => {
	const results = await execa('curl', ['-sSL', 'https://sindresorhus.com/unicorn']);
	return results;
};

console.log(await pRetry(run, {retries: 5}));
```



## 改变进程当前路径

```
// https://github.com/rapidsai/node/blob/main/modules/demo/client-server/index.js
const Path = require('path');

// Change cwd to the example dir so relative file paths are resolved
process.chdir(__dirname);

const next = require.resolve('next/dist/bin/next');

require('fs').stat(Path.join(__dirname, '.next'), (err, stats) => {
  const {spawnSync} = require('child_process');

  const env = {
    NEXT_TELEMETRY_DISABLED: 1,  // disable https://nextjs.org/telemetry
    ...process.env,
  };

  if (err || !stats || !stats.isDirectory()) {
    spawnSync(process.execPath, [next, 'build'], {env, cwd: __dirname, stdio: 'inherit'});
  }

  spawnSync(process.execPath, [next, 'start'], {env, cwd: __dirname, stdio: 'inherit'});
});
```



# interop

## python

- https://github.com/hmenyus/node-calls-python

- https://github.com/extrabacon/python-shell

### 源码编译

- https://blog.51cto.com/u_15069442/4117615



```

编译环境 win10 + vs2019

cd Python-3.8.16\PCbuild
./get_externals.bat
	# 安装 

Python-3.8.16\PCbuild\pcbuild.sln
	# 打开解决方案
	
选择python 项目，编译类型为 x64，开始编译

注意：
	编译出来的 dll 和 exe 依赖 Python-3.8.16\Lib 这个目录，里面有各种 python 脚本
	Lib 或者和可执行文件同级目录，或着在它的上级，会一直往上找，找不到就报错了
	

dll 入口, python.c重命名为 python.cc，代码改成下面这样
#include "Python.h"
#include "pycore_pylifecycle.h"

extern "C" __declspec(dllexport) int wmain(int argc, wchar_t* wargv[]) {
    return Py_Main(argc, wargv);
}

#ifdef MS_WINDOWS
int mmain(int argc, wchar_t **argv)
{
    return wmain(argc, argv);
}


exe 入口，test_python_dll.cc
#include <iostream>

#include "windows.h"
#include <direct.h>

#include <Shlwapi.h>
#pragma comment(lib, "shlwapi.lib")

void call_node_dll() {
    HINSTANCE   ghDLL = NULL;
    ghDLL = LoadLibrary("D:\\GitHub\\node-14.21.1\\out\\Debug\\node.dll");

    typedef int(_cdecl* FunctionPtr) (int argc, wchar_t* wargv[]);

    FunctionPtr wmain;

    wmain = (FunctionPtr)GetProcAddress(ghDLL, "wmain");

    int argc = 2;

    wchar_t* wargv[] = {
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
      //(wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
      (wchar_t*)L"D:\\GitHub\\echodict\\pmserver\\server.js"
    };

    wmain(argc, wargv);

    std::cout << "Hello World!\n";
}

void call_python_dll(int argc, char* argv[]) {
    HINSTANCE   ghDLL = NULL;
    //ghDLL = LoadLibrary("E:\\python\\Python-3.8.16\\PCbuild\\amd64\\python38_d.dll");

    //string str = System.AppDomain.CurrentDomain.SetupInformation.ApplicationBase;

    

    char dll_path[MAX_PATH] = { 0 };
    ::GetModuleFileName(nullptr, dll_path, MAX_PATH);
    ::PathRemoveFileSpec(dll_path);
    ::PathAppend(dll_path, "python38_d.dll");
    
    ghDLL = LoadLibrary(dll_path);

    //ghDLL = LoadLibrary("F:\\python\\Python-3.8.16\\PCbuild\\amd64\\python38_d.dll");

    typedef int(_cdecl* FunctionPtr) (int argc, wchar_t* argv[]);


    FunctionPtr wmain;

    wmain = (FunctionPtr)GetProcAddress(ghDLL, "wmain");

    wchar_t* wargv[] = {
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
      //(wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
      //(wchar_t*)L"D:\\GitHub\\echodict\\pmserver\\server.js"
    };

    wmain(1, wargv);

    std::cout << "Hello World!\n";
}

int main(int argc, char* argv[])
{
    //call_node_dll();

    call_python_dll(argc, argv);
}

	
```





# network



## websocket

```javascript
// 客户端
ws_app_inner_diff.js

const WebSocket = require('ws')

//webSocket服务端地址
let wsBaseURL = 'ws://xxx:7004'

let wsClient = null

init: {

    wsClient = new WebSocket(wsBaseURL);

    wsClient.onopen = () => {

        console.log(wsBaseURL + '连接成功')

        // 开始题库内去重
        start_diff: {

            try {
                wsClient.send(JSON.stringify(
                    { "api": "/xxx/xxx", "params": { "AppID": xxx, "BookID": -1, "userID": "1", "refresh": 0 } })
                )
            } catch (error) {
                console.log(error.msg)
            }

        }

    }
    wsClient.onerror = (error) => {
        setTimeout(() => {
            newClient = new WebSocket(wsBaseURL);
            newClient.onopen = wsClient.onopen;
            newClient.onerror = wsClient.onerror;
            newClient.onmessage = wsClient.onmessage;
            wsClient = newClient;
        }, 1000);
    }
    wsClient.onmessage = (msg) => {
        let data = JSON.parse(msg.data);
    }
}
```



```
WebSocket.close() # 如果连接已经关闭，则此方法不执行任何操作。

    wsClient.onclose = (event) => {
    	let { code, reason, wasClean } = event
        console.log('The connection has been closed successfully.');
    }
```



## show ip

```
function getIpAddress() {
    const os = require('os');
    let ifaces = os.networkInterfaces()
    for (let dev in ifaces) {
        let iface = ifaces[dev]
        for (let i = 0; i < iface.length; i++) {
            let { family, address, internal } = iface[i]
            if (family === 'IPv4' && address !== '127.0.0.1' && !internal) {
                return address
            }
        }
    }
}
console.log(getIpAddress()) 
```







# args



```
var arguments = process.argv
console.log( arguments )
```






# tuple



```javascript
function getCoordinates(element) {
  let x, y, z;

  return [x, y, z];
}
```



```javascript
// with returned objects
const {x: Ax, y: Ay, z: Az } = getCoordinates(A);
const {x: Bx, y: By, z: Bz } = getCoordinates(B);
// with returned tuples
const [Ax, Ay, Az] = getCoordinates(A);
const [Bx, By, Bz] = getCoordinates(B);

onst [, , thisOne, , thatOne] = getTuple();
const [_1, _2, thisOne, _3, thatOne] = getTuple();

```





# lodash



```javascript
var _ = require('lodash')  // https://lodash.com/docs/4.17.15


修改key

_.mapKeys({ 'a': 1, 'b': 2 }, function(value, key) {
  return key + value;
});
// => { 'a1': 1, 'b2': 2 }


修改value

var users = {
  'fred':    { 'user': 'fred',    'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
};
 
_.mapValues(users, function(o) { return o.age; });
// => { 'fred': 40, 'pebbles': 1 } (iteration order is not guaranteed)
 
// The `_.property` iteratee shorthand.
_.mapValues(users, 'age');
// => { 'fred': 40, 'pebbles': 1 } (iteration order is not guaranteed)
```



## deep copy



```
_.cloneDeep
```



## shuffle

```
arr = _.shuffle(arr)
```







# 异步



```javascript

// 骚操作
// await 外层必须是 async 函数，所以建了一个匿名函数标记为async，并立既调用这个匿名（里面装await）

// 测试接口
// 测试接口

( async()=>{

  // 注意 require 写在外面会出错！！！！！！！！！！！！！！
  var request = require('request')

  async function get() {

    let appename = "ZC_ZXYJHNKX_YTMJ"

    var data = await new Promise(function (resolve) {
  
      url = 'http://101.37.23.135:8005/gettest'
      request.post(url, {
        'form': {
          appename: "ZC_ZXYJHNKX_YTMJ"
        }
      },
      function(err, response, result) {
        if (err || response.statusCode != 200) {
          console.log(url + err + response.statusCode)
          //throw (url + err + response.statusCode)
          return resolve({})
        }
  
        return resolve(result)
      })
  
    })
  
    data = JSON.parse(data).data

    delete data["idArray"]
    delete data["tests"]
    delete data["appEName"]

    return data
  }

  async function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms)
    })
  }

  for (let i = 0; i < 50001; i++) {
    let d = await get()
    console.log(`${i}th : ${JSON.stringify(d)}`)
    await sleep(100)
  }

})()
```



## sleep



```javascript
  async function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms)
    })
  }

await sleep(2000) 
```





## 异步函数是Promise的实例



```
  //进入API
  result = api.handler(data)
  if (result instanceof Promise) {
    result = await result
  }
```







# 随机



```
arr[Math.floor(Math.random() * arr.length)] // 从数组里随机选择一个  Math.random 最小值是0， 最大值小于1
```





# redist

- https://www.digitalocean.com/community/tutorials/how-to-install-secure-redis-centos-7

  > redis-cli -h host -p port -a password
  >
  > ```
  > select 0    # 选择0号数据库
  > keys *name* # 查询key
  > get "defaultDB.user.guid.33"
  > ```
  >
  > 
  >
  > redis-cli -h 127.0.0.1  -p 6379
  >
  > redis-cli -h 127.0.0.1 -p 6379 PING



```
Redisson 的 getLocalCachedMap 对应的 Redis 类型就是 hash 吧，那就没啥问题了啊就是这样用的啊，甚至都不需要这 1000key 吧

使用 redisson 连接的 redis(哨兵)
目前是存人群信息, 分了 1000 个 key (redis 中 key 如果很多的话会有问题么)
1000 个 key 的 value 是 一个大 Map ,存取这个 map 用的是 getLocalCachedMap
map 的每个 key 对应一个人 value 就是他的数据(数据量肯定不大 几百 k 吧)
然后业务集群每天大概请求在 40 -50 亿 然后峰值是 70 亿

我觉得不是很妥当，key 数量并不会显著影响存取性能，但是大 key or 大 value 会显著降低 redis 性能
小于 1k 的键值对操作性能，和 10k 以上的 k-v 操作性能，有数量级差距
印象中 redis hash 结构推荐的 field 数量应该在 100 左右以内


```





```
 安装  npm install redis --save

demo

var redis = require('redis');

var client = redis.createClient('6379', '127.0.0.1');

client.auth("password");
client.set('hello','This is a value');
client.expire('hello',10) //设置过期时间
client.exists('key') //判断键是否存在
client.del('key1')
client.get('hello');

 

//stirng
命令 行为 返回值 使用示例(略去回调函数)
set 设置存储在给定键中的值 OK set('key', 'value')
get 获取存储在给定键中的值 value/null get('key')
del 删除存储在给定键中的值(任意类型) 1/0 del('key')
incrby 将键存储的值加上整数increment incrby('key', increment)
decrby 将键存储的值减去整数increment decrby('key', increment)
incrbyfloat 将键存储的值加上浮点数increment incrbyfloat('key', increment)
append 将值value追加到给定键当前存储值的末尾 append('key', 'new-value')
getrange 获取指定键的index范围内的所有字符组成的子串 getrange('key', 'start-index', 'end-index')
setrange 将指定键值从指定偏移量开始的子串设为指定值 setrange('key', 'offset', 'new-string')
//list
命令 行为 返回值 使用示例(略去回调函数)
rpush 将给定值推入列表的右端 当前列表长度 rpush('key', 'value1' [,'value2']) (支持数组赋值)
lrange 获取列表在给定范围上的所有值 array lrange('key', 0, -1) (返回所有值)
lindex 获取列表在给定位置上的单个元素 lindex('key', 1)
lpop 从列表左端弹出一个值，并返回被弹出的值 lpop('key')
rpop 从列表右端弹出一个值，并返回被弹出的值 rpop('key')
ltrim 将列表按指定的index范围裁减 ltrim('key', 'start', 'end')

//set
命令 行为 返回值 使用示例(略去回调函数) sadd 将给定元素添加到集合 插入元素数量 sadd('key', 'value1'[, 'value2', ...]) (不支持数组赋值)(元素不允许重复)
smembers 返回集合中包含的所有元素 array(无序) smembers('key')
sismenber 检查给定的元素是否存在于集合中 1/0 sismenber('key', 'value')
srem 如果给定的元素在集合中，则移除此元素 1/0 srem('key', 'value')
scad 返回集合包含的元素的数量 sacd('key')
spop 随机地移除集合中的一个元素，并返回此元素 spop('key')
smove 集合元素的迁移 smove('source-key'dest-key', 'item')
sdiff 返回那些存在于第一个集合，但不存在于其他集合的元素(差集) sdiff('key1', 'key2'[, 'key3', ...])
sdiffstore 将sdiff操作的结果存储到指定的键中 sdiffstore('dest-key', 'key1', 'key2' [,'key3...])
sinter 返回那些同事存在于所有集合中的元素(交集) sinter('key1', 'key2'[, 'key3', ...])
sinterstore 将sinter操作的结果存储到指定的键中 sinterstore('dest-key', 'key1', 'key2' [,'key3...])
sunion 返回那些至少存在于一个集合中的元素(并集) sunion('key1', 'key2'[, 'key3', ...])
sunionstore 将sunion操作的结果存储到指定的键中 sunionstore('dest-key', 'key1', 'key2' [,'key3...])
//hash
命令 行为 返回值 使用示例(略去回调函数)
hset 在散列里面关联起给定的键值对 1(新增)/0(更新) hset('hash-key', 'sub-key', 'value') (不支持数组、字符串)
hget 获取指定散列键的值 hget('hash-key', 'sub-key')
hgetall 获取散列包含的键值对 json hgetall('hash-key')
hdel 如果给定键存在于散列里面，则移除这个键 hdel('hash-key', 'sub-key')
hmset 为散列里面的一个或多个键设置值 OK hmset('hash-key', obj)
hmget 从散列里面获取一个或多个键的值 array hmget('hash-key', array)
hlen 返回散列包含的键值对数量 hlen('hash-key')
hexists 检查给定键是否在散列中 1/0 hexists('hash-key', 'sub-key')
hkeys 获取散列包含的所有键 array hkeys('hash-key')
hvals 获取散列包含的所有值 array hvals('hash-key')
hincrby 将存储的键值以指定增量增加 返回增长后的值 hincrby('hash-key', 'sub-key', increment) (注：假如当前value不为为字符串，则会无输出，程序停止在此处)
hincrbyfloat 将存储的键值以指定浮点数增加

//zset
命令 行为 返回值 使用示例(略去回调函数)
zadd 将一个带有给定分支的成员添加到有序集合中 zadd('zset-key', score, 'key') (score为int)
zrange 根据元素在有序排列中的位置，从中取出元素
zrangebyscore 获取有序集合在给定分值范围内的所有元素
zrem 如果给定成员存在于有序集合，则移除
zcard 获取一个有序集合中的成员数量 有序集的元素个数 zcard('key')


keys命令组
命令 行为 返回值 使用示例(略去回调函数)
del 删除一个(或多个)keys 被删除的keys的数量 del('key1'[, 'key2', ...])
exists 查询一个key是否存在 1/0 exists('key')
expire 设置一个key的过期的秒数 1/0 expire('key', seconds)
pexpire 设置一个key的过期的毫秒数 1/0 pexpire('key', milliseconds)
expireat 设置一个UNIX时间戳的过期时间 1/0 expireat('key', timestamp)
pexpireat 设置一个UNIX时间戳的过期时间(毫秒) 1/0 pexpireat('key', milliseconds-timestamp)
persist 移除key的过期时间 1/0 persist('key')
sort 对队列、集合、有序集合排序 排序完成的队列等 sort('key'[, pattern, limit offset count])
flushdb 清空当前数据库
```



## 性能



```
# https://www.jianshu.com/p/31ab9b020cd9
	Redis-击穿、穿透和雪崩
# https://www.jianshu.com/p/4838f8be00c9
	分布式锁

```



## bit 位操作

- https://xie.infoq.cn/article/0ad770293fb9de05c4f766a94

```
应用场景
实际项目开发中有很多业务都适合采用 redis 的 bit 来实现。

用户签到场景
每天的日期字符串作为一个 key，用户 Id 作为 offset，统计每天用户的签到情况，总的用户签到数
```



## RedisGraph  图数据库

- https://zhuanlan.zhihu.com/p/102679312



## RedisInsight 管理工具

- https://zhuanlan.zhihu.com/p/476056075 



# nginx

- https://linuxize.com/post/how-to-install-nginx-on-centos-7/
- https://www.bbwho.com/dockerrong-qi-hua-nginx-node-js-and-redis/  基于Nginx, Node.js 和 Redis的Docker容器化工作流
- https://blog.csdn.net/yeguxin/article/details/94020476



```
/etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```





```
# 不同域名实现转后端接口和前端

/etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}


server {
  listen 80;
  server_name xxapi.yy.cn;

  location / {
    location / {
      proxy_pass http://centos7_server_6006;
    }
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 9999999;
    proxy_connect_timeout 9999999;
    proxy_send_timeout 9999999;
  }
}

server {
  listen 80;
  server_name xx.yy.cn;

  location / {
     root   /home/data;
     index  index.html index.htm;
  }
}
```





# mysql 



## 封装

### mysql.js

```javascript
const mysql = require('mysql');

module.exports = {
  createPool: function (config) {

    const pool = mysql.createPool(config);
    const lib = {
      //执行查询
      async query(sql, par, conn = null) {
        if (conn == null) {
          conn = await new Promise((resolve, reject) => {
            pool.getConnection((erro, connection) => {
              if (erro) {
                reject(erro);
                return;
              }
              resolve(connection);
            });
          });
        }

        return new Promise((resolve, reject) => {
          const info = buildSQL(sql, par);
          conn.query(info.sql, info.params, (erro, result) => {
            //释放连接
            pool.releaseConnection(conn);
            // conn.release();
            if (erro) {
              reject(erro);
              return;
            }
            resolve(result);
          });
        });
      },
      //创建事务
      async createTransaction() {

        //获取连接
        const conn = await new Promise((resolve, reject) => {
          pool.getConnection((erro, connection) => {
            if (erro) {
              reject(erro);
              return;
            }
            resolve(connection);
          });
        });
        const t = {
          begin() {
            return new Promise((resolve, reject) => {
              conn.beginTransaction((beginErro) => {
                if (beginErro) {
                  //释放连接
                  pool.releaseConnection(conn);
                  // conn.release();
                  reject(beginErro);
                  return;
                }
                resolve(t);
              });
            });
          },
          query(sql, par) {
            const info = buildSQL(sql, par);
            return new Promise((resolve, reject) => {
              conn.query(info.sql, info.params, (erro, result) => {
                if (erro) {
                  //释放连接
                  pool.releaseConnection(conn);
                  // conn.release();
                  //回滚
                  conn.rollback((rollErro) => {
                    reject(rollErro);
                  });
                  reject(erro);
                  return;
                }
                resolve(result);
              });
            });
          },
          end() {
            return new Promise((resolve, reject) => {
              conn.commit((erro, info) => {
                if (erro) {
                  //释放连接
                  pool.releaseConnection(conn);
                  // conn.release();
                  //回滚
                  conn.rollback((rollErro) => {
                    reject(rollErro);
                    return;
                  });
                  reject(erro);
                }
                resolve(info);
              });
            });
          }
        };
        return t;
      },
    };

    return lib;
  }
};

/**
 * 构建SQL执行参数
 * @param {*} sql 
 * @param {*} par 
 * @returns {sql,params}
 */
function buildSQL(sql, par) {
  //参数处理
  const arr = [];
  const parNames = sql.match(/\$\([0-9a-zA-Z\_]{1,9999}?\)/g);
  if (parNames != null) {
    for (let pName of parNames) {
      //替换参数名
      sql = sql.replace(pName, '?');
      //转换参数名
      pName = pName.replace(/\$\(([[0-9a-zA-Z\_]{1,9999}?)\)/g, '$1')
      arr.push(par[pName]);
    }
  }
  return { sql: sql, params: arr };
}
```



### use



```javascript

( async()=>{

  async function get(db) {

    async function sleep(ms) {
      return new Promise((resolve) => {
        setTimeout(resolve, ms)
      })
    }

    //let ID = 10000

    var r = null

    while(r === null || r === undefined || r.length === 0) {

      let tmp = 100000 * Math.random() + 10000  // 随机数本来是均匀分存在 0 ~ 100000 之间，把它们整体往后挪10000

      var ID = Math.floor( tmp + 1 )
    
      if (ID > 100000) {
        ID = 100000
      }
        
      r = await db.query(`SELECT \`MD5\`, content FROM img_context WHERE ID = $(ID)`, { ID })

      //await sleep(500)

    }

    return [ JSON.parse(r[0].content), ID]

    
  }

  // ID 在 10000 ~  100000 之间随机取
  // Math.random() 范围：0 ~ 0.99999

  let mysql = require('./mysql')

  let db = mysql.createPool({
    host: 'xxx',
    user: 'xxx',
    password: 'xxx',
    database: 'xxx',
    port: 3306,
    multipleStatements: true,
    connectTimeout: 60 * 1000,
    connectionLimit: 50
  })


  for (let i = 0; i < 500; i++) {

    let [j, ID] = await get(db)

    require('fs').writeFileSync(`./out/${ID}.json`, JSON.stringify(j) )

    console.log(`done ${i}, ID: ${ID}`)

  }


}) ()
```



## 存储过程



### 循环



```
DROP PROCEDURE IF EXISTS `insertManyDate`;
 
CREATE DEFINER =  PROCEDURE `insertManyDate`(IN `beginDate` date,IN `endDate` date)
    COMMENT '根据输入的起止日期，循环插入每天的时间'
BEGIN
 
DECLARE nowdate date DEFAULT NOW();
DECLARE endtmp date DEFAULT NOW();
set nowdate = DATE_FORMAT(beginDate,'%Y%m%d');
set endtmp = DATE_FORMAT(endDate,'%Y%m%d');
WHILE nowdate<endtmp 
DO
INSERT INTO belial.date(date) VALUES(nowdate);
set nowdate = DATE_ADD(nowdate,INTERVAL 1 DAY);
END WHILE;
```



## 取用户最新的一条数据



```mysql
# 前提：ID 是自增ID
# MAX(r.ID) 是最新的，但其他不是，所以必须要用子查询

    SELECT r.ID AS reportID, r.appID, r.userID, r.rightRate FROM report r WHERE r.ID IN ( SELECT MAX(r.ID) AS reportID from report r WHERE r.appID=$(appid) GROUP BY r.userID ORDER BY reportID DESC ) ORDER BY reportID DESC;

```







## Time

```
const now = moment().format('YYYY-MM-DD HH:mm:ss');
var time = moment().format('MMMM Do YYYY, h:mm:ss a')
let t1 = new Date().getTime();
```



### 时区转换



```
select NOW();
SELECT convert_tz(now(),@@session.time_zone,'+08:00')


# 24小时制
let u = re[0].updateTime
let tt = new Date(u).toLocaleString('chinese',{hour12:false})

```

### 24 小时制



```javascript
select NOW();
SELECT convert_tz(now(),@@session.time_zone,'+08:00')


# 24小时制
let u = re[0].updateTime
let tt = new Date(u).toLocaleString('chinese',{hour12:false})
```



### 时间比较



```
普通日期时间比较

泛指格式相同的日期时间

var date1 = new Date("2020-3-15");
var date2 = new Date("2020-2-29");
var result = date1 > date2;        
console.log(result);                //true
特殊日期时间比较

因格式不同，比较前，我们需要将日期时间格式化

var date1 = new Date("2020-3-15");
var date2 = new Date("2020/2/29");
var result = Date.parse(date1) > Date.parse(date2);
console.log(result);                                //true
字符串类型日期时间比较 

用于不同格式之间的字符串日期时间比较，统一格式化后再比较

var date1 = "2020-3-15";
var date2 = "2020/2/29";
var result = date1.replace(/\-/g,'/') > date2.replace(/\-/g,'/');
console.log(result);                                                //true
```



## 定时任务

```
        async function loopcheck() {
            return new Promise(function (resolve, reject) {
                const timer = setInterval(async function () {
                    let checktype = await pushrdis()
                    if (checktype) {
                        resolve(ID)
                        clearInterval(timer)
                    } else if (conn) {
                        conn.__ws__.send(msg)
                    }
                }, 10000);
            });
        }


clearTimeout(checkTask);
checkTask = setTimeout(() => {
	// 一秒后执行
}, 1000);
```





## escape

```
const mysql = require('mysql')
mysql.escape(s) 
```





# Algo



## TF-IDF

- https://zhuanlan.zhihu.com/p/31197209

  > 生动理解TF-IDF算法



# PG



## pgsql.js



```javascript

"pg": "~8.7.1",
"pg-pool": "~3.4.1"

let { Pool, Client } = require('pg')

function getconfig (dbname) {
  return {
    user: 'postgres',
    password: 'et.com',
    host: 'xxxx.77',
    port: '5432',
    database: dbname,
    ssl: false
  }
}

function getDB (dbname) {
  let config = getconfig(dbname)
  let pool = new Pool(config)
  let lib = {

    async query(sql, par, conn = null) {
      if (conn == null) {
        conn = await pool.connect()
      }

      //await client.query('select $1::text as name', ['brianc'])
      let result = await conn.query(sql, par)
      conn.release(true)

      return result

    },
    async release() {
      return await new Promise((resolve, reject) => {
        pool.end().then(() => {
          resolve(`pool has been release, db is ${config.database}`)
        })
      })
    
    },
    status() {
      let totalCount = pool.totalCount
      let idleCount = pool.idleCount
      let waitingCount = pool.waitingCount
      return { totalCount, idleCount, waitingCount }
    } 

    /*
    pool.totalCount: int
      The total number of clients existing within the pool.

    pool.idleCount: int
      The number of clients which are not checked out but are currently idle in the pool.

    pool.waitingCount: int
      The number of queued requests waiting on a client when all clients are checked out. It can be helpful to monitor this number to see if you need to adjust the size of the pool.
    */

  }

  return lib
}

let defaultDB = getDB('postgres')

module.exports = {
  getconfig,
  getDB,
  defaultDB
}

/*

 cur.execute("create table anime( \
                id integer primary key generated always as identity, \
                name text, \
                jp text, \
                zh text DEFAULT '', \
                en text DEFAULT '', \
                type text, \
                time text, \
                jp_mecab text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector, \
                videoname text, \
                seasion text DEFAULT '', \
                audio bytea, \
                video bytea \
            );")
            #cur.execute("CREATE TABLE audio(id SERIAL PRIMARY KEY, data BYTEA);")

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            cur.execute("CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);")

            cur.execute("create extension pg_jieba;")

            cur.execute("CREATE INDEX animename_index ON anime (name);")
            cur.execute("CREATE INDEX videoname_index ON anime (videoname);")

*/

```



```javascript

    let pg = require('./pgsql')
    let re = await pg.defaultDB.query('select $1::text as name', ['brianc']) 
    re = await pg.defaultDB.query('DROP DATABASE IF EXISTS temp;', [])
    re = await pg.defaultDB.query(`
    CREATE DATABASE temp 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `, [])

    let tempDB = pg.getDB('temp')
    re = await tempDB.query(    `
    CREATE TABLE bookdata (
        id  serial NOT NULL PRIMARY KEY,
        info json NOT NULL
      )
    `)
    re = await tempDB.query(`CREATE INDEX bookdata_fts ON bookdata USING gin((to_tsvector('english',info->'title')));`)

    re = await tempDB.query(`
    INSERT INTO bookdata (info)
    VALUES
     ( '{ "title": "The Tattooed Duke", "items": {"product": "Diaper","qty": 24}}'),
     ( '{ "title": "She Tempts the Duke", "items": {"product": "Toy Car","qty": 1}}'),
     ( '{ "title": "The Duke Is Mine", "items": {"product": "Toy Train","qty": 2}}'),
     ( '{ "title": "What I Did For a Duke", "items": {"product": "Toy Train","qty": 2}}'),
     ('{ "title": "King Kong", "items": {"product": "Toy Train","qty": 2}}');
     `)

     re = await tempDB.query(`
     SELECT info -> 'title' as title FROM bookdata
     WHERE to_tsvector('english',info->'title') @@ to_tsquery('Duke');
     `)

    let sta1 = pg.defaultDB.status()
    let sta2 = tempDB.status()

    re = await tempDB.release()
    re = await pg.defaultDB.release()
```





## Pool



```
/*
  Transforms, 'postgres://DBuser:secret@DBHost:#####/myDB', into
  config = {
    user: 'DBuser',
    password: 'secret',
    host: 'DBHost',
    port: '#####',
    database: 'myDB',
    ssl: true
  }
*/
```



```javascript
# https://github.com/brianc/node-postgres/tree/master/packages/pg-pool

npm install pg pg-pool --save

(async () => {

    const { Pool, Client } = require('pg')

    const config = {
        user: 'postgres',
        password: 'xxxx',
        host: 'xxxx',
        port: '5432',
        database: 'postgres',
        ssl: false
    }

    var pool = new Pool(config)
    var client = await pool.connect()
    try {
      var result = await client.query('select $1::text as name', ['brianc'])
      console.log('hello from', result.rows[0])
    } finally {
      client.release()
    }
})().catch(e => console.error(e.message, e.stack))
```



## insert id

```
  INSERT INTO $$(tablename) (name, seasion, jp, zh, type, begintime, endtime, jp_ruby, v_jp, v_zh, videoname, episode, seasionname, audio, video) 
  VALUES 
  ( $(name), $(seasion), $(jp), $(zh), $(type), $(begintime), $(endtime), $(jp_ruby), to_tsvector($(v_jp)), to_tsvector($(v_zh)), $(videoname), $(episode), $(seasionname), $(audio), $(video) ) 
  RETURNING id;

let re = await this.dbs.anime.insert.query({tablename:type, name, seasion, jp, zh, type, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionname, endtime, audio, video})
                
                let { id } = re.fields[0]
```





## Random



```
# https://www.redpill-linpro.com/techblog/2021/05/07/getting-random-rows-faster.html
	Getting random rows faster. Very much faster.
```



## Group



```mysql
分组聚合
# https://www.skypyb.com/2021/08/jishu/1871/

解决PostgreSQL分组聚合时SELECT中字段必须在group或聚合函数中的问题
PG的分组函数是比较严格的。 你的select字段必须得存在于group子句、或者聚合函数中才行。

假设场景是这样的：

表结构name、class、score

我现在要按照name分组，聚合score数据，还能查出额外的这个 class 字段

 

如果是MySQL， 你可以直接group name 然后 select class，avg(score)， 但是你在PostgreSQL里就不行。

 

他会爆出以下的错误

column “class” must appear in the GROUP BY clause or be used in an aggregate function

 

就是说这个 select class是非法的。

刚从MySQL切到PostgreSQL后很可能会比较难受这个点。

 

其实有一种很简单的方法， 那就是你反正其他的字段其实都一样，随便取一个就行，所以还是保持原来的GROUP BY 子句，然后直接给所有的字段全部加上一个 max() 函数就行了。

不过这样子的代价就是整个SQL看起来挺怪的， 语义上也有点微妙。我这只是个简单场景， 实际上你可能得有好几十个字段，这样子每个字段都得加上个max函数。

 

所以我推荐第二种方法。

Window function（窗口函数） + distinct 去重

 

窗口函数语法：

聚合函数(sum，min，avg……) + OVER ( …… )

 

窗口函数会将计算出来的结果带回到计算行上，还是以上面的例子作参考，一个表name、class、score。

 

那我直接一个普通查询，不GROUP了，我们想要的class自然就可以查出来了。

然后用窗口函数去算我需要聚合的数据，这里直接写上关键字OVER放在avg(score)后面， 然后括号里跟上一个PARTITION BY name， 意思就是按照name去分组，把结果计算出来。

唉！这个效果其实就和GROUP BY差不多，对不对。

不过这样子的话你数据是有了，但是行数却没变，原来是多少行现在还是多少行。 好，那我就直接给它安排一个 dictinct 函数，指定我 PARTITION BY 的那个字段，也就是name。

这样子我们就完成了一波上流且奢华的SQL查询，大功告成~

SELECT distinct on (name) 
    name,
    class,
    avg(score) OVER (PARTITION BY name) AS score,
FROM table
语义上清晰不少， 效果也给满足了（指按照name分组，聚合score数据，还能查出不处于GROUP子句和聚合函数中的 class 字段）

```



## with



```mysql
# https://www.postgresql.org/docs/9.1/queries-with.html

WITH regional_sales AS (
        SELECT region, SUM(amount) AS total_sales
        FROM orders
        GROUP BY region
     ), top_regions AS (
        SELECT region
        FROM regional_sales
        WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
     )
SELECT region,
       product,
       SUM(quantity) AS product_units,
       SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;

```



## Mecab



```
# hara.js

/*

  "dependencies": {
    "fluent-ffmpeg": "~2.1.2",
    "kuroshiro": "~1.2.0",
    "pg": "~8.7.1",
    "pg-pool": "~3.4.1"
  }

*/

(async () => {

    var arguments = process.argv

    //console.log( arguments[2] )

    String.prototype.replaceAll = function (search, replacement) {
        var target = this
        return target.replace(new RegExp(search, 'g'), replacement)
    }

    // let arr = require('fs').readFileSync('./data.json', { encoding: 'utf8', flag: 'r' })

    // arr = JSON.parse(arr)

    const Kuroshiro = require("kuroshiro")
    const KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji")
    const MecabAnalyzer = require("kuroshiro-analyzer-mecab")
    const kuroshiro = new Kuroshiro()

    const mecabAnalyzer = new MecabAnalyzer({
        dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd",
        execOptions: {
            maxBuffer: 200 * 1024,
            timeout: 0
        }
    })

    let str = arguments[2] // arr[0]

    let [hiras, msg] = await new Promise(function (resolve) {

        //kuroshiro.init(new KuromojiAnalyzer())
        kuroshiro.init(mecabAnalyzer)
            .then(function () {
                return kuroshiro.convert(str, { to: "hiragana" })
            })
            .then(function (result) {
                resolve([result.toString(), ''])
            }).catch((err) => {
                resolve([null, err])
            })

    })

    //originals = originals.replaceAll(String.raw`\s`, '')
    //hiras = hiras.replaceAll(String.raw`\s`, '')
    let hiras_ngrams = NG(hiras)

    console.log( hiras_ngrams.join(' ') )

    //console.log(originals)
    //console.log(hiras)

    a = 1

})()

function NG(strs) {

  strs = strs.replaceAll(String.raw`\s`, '')

    function ng(s, n) {
  
      var grs = []
  
      for (let i = 0; i < s.length; i++) {
  
        if ( i + n > s.length ) {
          break
        }
  
        var gr = s.substring(i, i+n)
  
        grs.push(gr)
        
  
      }
  
      return grs
  
    }
  
    var gss = []
    for (let i = 2; i <= 10; i++) {
      
      let gs = ng(strs, i)
  
      if (gs.length > 0) {
  
        gss = gss.concat( gs )
  
      } else {
  
        break
  
      }
  
    }
  
    return gss
  
  }

  
  String.prototype.replaceAll = function(search, replacement) {
    var target = this
    return target.replace(new RegExp(search, 'g'), replacement)
  }

  // s = NG(' ab cdefg')
  // a = 1


```





```
https://mebee.info/2021/02/18/post-29277/
	# mecab centos7
```





```
# https://qiita.com/PonDad/items/81b85d76b1a89ee2598b
	# https://blog.knjcode.com/neologd-on-nodejs/
var MeCab = new require('mecab-async')
var mecab = new MeCab();
    MeCab.command = "mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
    var text = 'こんにちは、サミュエルLジャクソンです。'
    //注：パースコマンドを利用する時 "MeCab.~"と大文字にしないと動かないみたいです
    MeCab.parseFormat(text, function(err, morphs) {
        if (err) throw err;
        morphs.map(function(morph) {
        if (morph.lexical === '感動詞') {
          console.log(morph.lexical + ' : ' + morph.original);
        }
        if (morph.lexical === '名詞') {
          console.log(morph.lexical + ' : ' +morph.original);
        }
    });
    });
```





```
# https://github.com/agracio/edge-js

js C# interop
```





```
pip3.8 install mecab-python3
pip3.8 install unidic-lite
pip3.8 install chardet

D:\usr\Lib\site-packages\unidic_lite
```





```
# https://github.com/hecomi/node-mecab-async
npm install mecab-async
```



### kuromoji.js + mecab-ipadic-neologd



```
# https://qiita.com/mabasasi/items/17b0bf735c38b4642682
	
	# https://github.com/reneeter123/kuromoji.js-vs-neologd
		# pure js in browser
		    if (document.getElementById("useStandard").checked) {
        startTime = performance.now();
        kuromoji.builder({ dicPath: "./js/dicts/standard/" }).build((err, tokenizer) => {
            showResult(tokenizer.tokenize(analyzeTextValue));
        });
    } else if (document.getElementById("useNeologd").checked) {
        startTime = performance.now();
        kuromoji.builder({ dicPath: "./js/dicts/neologd/" }).build((err, tokenizer) => {
            showResult(tokenizer.tokenize(analyzeTextValue));
        });
    } else {
        startTime = performance.now();
        showResult(new TinySegmenter().segment(analyzeTextValue));
    }

npm install kuromoji --save

var kuromoji = require("kuromoji");

kuromoji.builder({ dicPath: "node_modules/kuromoji/dict" }).build(function (err, tokenizer) {
  // tokenizer is ready
  var path = tokenizer.tokenize("すもももももももものうち");
  console.log(path);
  a = 1
});

```



### centos7+mecab+neologd



```
https://omohikane.com/centos7_mecab_neologd/

# install libs
sudo yum install -y  bzip2 bzip2-devel gcc gcc-c++ git make wget curl openssl-devel readline-devel zlib-devel
 
# install mecab
sudo mkdir -p /tmp/install_mecab
cd /tmp/install_mecab
wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE' -O mecab-0.996.tar.gz
tar zxvf mecab-0.996.tar.gz && cd mecab-0.996 && ./configure --with-charset=utf8 --enable-utf8-only &&  make && sudo make install
 
# install ipadic
sudo mkdir -p /tmp/install_mecab
cd /tmp/install_mecab
wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM' -O mecab-ipadic-2.7.0-20070801.tar.gz && tar zxvf mecab-ipadic-2.7.0-20070801.tar.gz && cd mecab-ipadic-2.7.0-20070801 && ./configure --with-charset=utf8 && make && sudo make install  
 
# install neologd
sudo rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm && sudo yum -y install mecab mecab-devel mecab-ipadic xz && cd /usr/local/src/ && sudo su - root
 
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && cd mecab-ipadic-neologd
 
echo "yes" | ./bin/install-mecab-ipadic-neologd -n
	# mecab -d /usr/lib64/mecab/dic/mecab-ipadic-neologd  成功，这样使用
./libexec/make-mecab-ipadic-neologd.sh 
echo "yes" | ./bin/install-mecab-ipadic-neologd -n


mecab -d /usr/lib64/mecab/dic/mecab-ipadic-neologd
	# 成功

```





#### Error: mecab-config not found

```
# mecab-config not found
# If you're installing MeCab via a package manager, be sure to get libmecab-dev to get mecab-config too.

# https://qiita.com/mhiro216/items/391ae79848129ac1cb2d


sudo rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm
sudo yum install mecab-devel
	# 成功解决 mecab-config not found
```



#### Error: no such file  mecab-ipadic-neologd/dicrc 



```
# https://qiita.com/MuggyTea/items/dd1ea3a781b59c6b5979





```





### kuroshiro 省心方案



```
# https://www.npmjs.com/package/kuroshiro

npm install kuroshiro@1.1.2
	# 其他版本有Bug

```





## FTS



### grammar



```
https://www.postgresql.org/docs/13/functions-textsearch.html
Tsvector_update_trigger jsonb  site:cnblogs.com
```



### json



#### trigger



- https://dba.stackexchange.com/questions/286660/how-to-use-tsvector-update-trigger-with-jsonb-column 













```
# https://www.skypyb.com/2020/12/jishu/1705/
索引
当数据量庞大时， 那么不可避免地查询速度就会变慢， 此时就需要去加索引。
PostgreSQL自然也提供了强大的索引支持， 使用以下语句增加 pg_trgm 拓展就可以引入两个索引 gin 、 gist， 需要注意的是执行语句需要提权到 postgres 用户。

CREATE EXTENSION pg_trgm;
gin和gist的区别就是 gin查询更快， 但是构建速度可能会慢一点。 而 gist 的构建速度快， 查询会慢一点。
一般建议预计数据量不大时可以使用gist索引， 如果预计数据量很大请直接上gin。

# https://developer.aliyun.com/article/672261
# https://blog.csdn.net/weixin_37096493/article/details/106302184
```



- https://github.com/valeriansaliou/sonic



### 分布式扩展

- https://github.com/citusdata/citus



### segment



```
https://www.jianshu.com/p/8f0ce2cff8d9
```



### NGram



```javascript
function NG(strs) {

  function ng(s, n) {

    var grs = []

    for (let i = 0; i < s.length; i++) {

      if ( i + n > s.length ) {
        break
      }

      var gr = s.substring(i, i+n)

      grs.push(gr)
      

    }

    return grs

  }

  var gss = []
  for (let i = 2; i <= 10; i++) {
    
    let gs = ng(strs, i)

    if (gs.length > 0) {

      gss = gss.concat( gs )

    } else {

      break

    }

  }

  return gss

}
```



## FFMPEG

- https://www.mysterydata.com/how-to-install-latest-ffmpeg-4-in-centos-8-7-ubuntu-20-04-18-04-cwp-cpanel-plesk-ispconfig/

### 升级

```
#  rpm -qa | grep -i ffmpeg
ffmpeg-3.4.9-1.el7.x86_64
ffmpeg-devel-3.4.9-1.el7.x86_64
ffmpeg-libs-3.4.9-1.el7.x86_64
gstreamer-ffmpeg-0.10.13-16.el7.x86_64

yum remove firefox -y
yum remove ffmpeg -y
yum update -y

wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
	# ffmpeg 5.0
	
mv dir to /usr/local/
ln ffmpeg to /usr/local/bin

```







```
ffmpeg -rtsp_transport tcp -i rtsp://userxx:xxx@192.168.101.108:554/0:0 -y http://192.168.101.1:8090/feed2.ffm
```



```
//			.outputOptions(["-movflags", "frag_keyframe+empty_moov"]) //without these options ffmpeg errors with `muxer does not support non seekable output`

```



### ffmpeg.wasm

- https://github.com/ffmpegwasm/ffmpeg.wasm

```
const trim = async ({ target: { files } }) => {
        videoInput.addEventListener('loadedmetadata', async function () {
                let duration =  Math.floor(videoInput.duration)-5; 
                oldDuration.innerText = `Duration before trim: ${duration} сек`;
                newDuration.innerText = `Duration after trim: ${duration-5} сек`;  
                await ffmpeg.run('-i', 'myfile.mp4', '-ss', '0', '-to', `${duration}`, '-c','copy', 'output.mp4');
                const data = await ffmpeg.FS('readFile', 'output.mp4');
                video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
                link.download = 'video.mp4';
                link.href = video.src;
                link.innerText = DOWNLOAD';
        });   
            if (!ffmpeg.isLoaded()) {
                await ffmpeg.load()
            }
            const { name } = files[0];
            const videofile = await FFmpeg.fetchFile(files[0]);
            await ffmpeg.FS('writeFile', `myfile.mp4`, videofile);
            const origData = await ffmpeg.FS('readFile', 'myfile.mp4');
            // Get the link and mount it in a hidden video tag in order to get the duration
            videoInput.src = URL.createObjectURL(new Blob([origData.buffer], { type: 'video/mp4' }));
      }
```







### ffmpeg.js



#### pipe stream



```
app.get('/stream', (req, res) => {
    let _url = req.query.url;

    if(_url){   

        res.writeHead(200, {
            'Access-Control-Allow-Origin': '*',
            'Connection': 'Keep-Alive',
            'Content-Type': 'video/mp4'
        });

        // transcode rtsp input from ip-cam to mp4 file format (video: h.264 | audio: aac)
        let ffmpeg = child_process.spawn("ffmpeg",[
            "-probesize","2147483647",
            "-analyzeduration","2147483647",
            "-i", _url,
            "-vcodec","copy",
            "-f", "mp4",            
            "-movflags","frag_keyframe+empty_moov+faststart",
            "-frag_duration","3600",
            "pipe:1"              
        ]);         


        // redirect transcoded ip-cam stream to http response
        ffmpeg.stdout.pipe(res);

        // error logging
        ffmpeg.stderr.setEncoding('utf8');      
        ffmpeg.stderr.on('data', (data) => {
            console.log(data);
        });
    }
    else{
        res.end();
    }
```





```javascript

// https://github.com/mafintosh/pump


module.exports = {

    extractAudio: async function (vdpath, type, begin_time, end_time) {

        var pump = require('pump')

        let fs = require('fs')
        let ffmpeg = require('fluent-ffmpeg')

        ffmpeg.setFfmpegPath(String.raw`E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe`)


            let [au, ms1] = await new Promise(function (resolve) {

                const stream = require('stream')

                let vd = fs.createReadStream(vdpath)

                // let bufferStream = new stream.PassThrough()
                // // Read the passthrough stream
                const buffers = []
                // bufferStream.on('data', function (buf) {
                //     buffers.push(buf)
                // })
                // bufferStream.on('end', function () {
                //     //vd.close()
                //     vd.destroy()

                // })

                // bufferStream.on('close', function () {

                //     // nclose += 1

                //     // const outputBuffer = Buffer.concat(buffers)
                //     // //let sr = outputBuffer.toString('utf8')
                //     // // let dir = require('path').dirname(__filename)
                //     // // let fname = require('path').join(dir, 'tmp.mp3')
                //     // fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                //     // resolve([outputBuffer, ''])

                // })

                let command = ffmpeg(vd)//.output(au)
                    .noVideo()
                    .format(type)
                    // .audioBitrate('128')
                    // .outputOptions('-ss', begin_time) // 00:00:00.000
                    // .outputOptions('-to', end_time)   // 00:00:07.520
                    .outputOption(
                        [
                            "-vn",
                            "-ss",
                            begin_time,
                            "-to",
                            end_time,
                            "-acodec", "mp3",
                            "-ar", "44100",
                            "-ac", "2",
                            "-b:a", "192k"
                        ]
                    )
                    //.writeToStream(bufferStream)
                    .on("end", (stdout, stderr) => {

                        const outputBuffer = Buffer.concat(buffers)
                        // let sr = outputBuffer.toString('utf8')
                        // let dir = require('path').dirname(__filename)
                        // let fname = require('path').join(dir, 'tmp.mp3')
                        //fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                        //bufferStream.destroy()
                        resolve([outputBuffer, ''])
                    })
                    .on("error", (err) => {
                        a = 1
                    })

                let ffstream = command.pipe()
                ffstream.on('data', function (buf) {
                    buffers.push(buf)
                })
                ffstream.on('end', function () {
                    a = 1
                })

                //ffmpegProc.on('exit', function(code, signal) {

                // .on('start', () => {

                //   a = 1

                // })
                // .on('end', () => {

                //   a = 1

                //   resolve(['ok', 'ok.'])
                // })
                // .run()
            })

            return [au, ms1]
    },
    extractSubtitle: async function (vdpath, type, nth) {

        let fs = require('fs')
        let ffmpeg = require('fluent-ffmpeg')

        ffmpeg.setFfmpegPath(String.raw`E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe`)

        let [au, ms1] = await new Promise(function (resolve) {

            const stream = require('stream')

            var vd = fs.createReadStream(vdpath)

            // let bufferStream = new stream.PassThrough()
            // Read the passthrough stream
            const buffers = []
            // bufferStream.on('data', function (buf) {
            //     buffers.push(buf)
            // })
            // bufferStream.on('end', function () {
            //     vd.destroy()
            // })

            let command = ffmpeg(vd)
                .noVideo()
                .format(type)
                .outputOption(
                    [
                        '-map', `0:s:${nth}`
                    ]
                )
                // .writeToStream(bufferStream)
                .on("end", (stdout, stderr) => {
                    const outputBuffer = Buffer.concat(buffers)
                    //let sr = outputBuffer.toString('utf8')
                    // let dir = require('path').dirname(__filename)
                    // let fname = require('path').join(dir, 'tmp.mp3')
                    //fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                    // bufferStream.destroy()
                    resolve([outputBuffer, ''])
                })
                .on("error", (err) => {
                    a = 1
                })

                let ffstream = command.pipe()
                ffstream.on('data', function (buf) {
                    buffers.push(buf)
                })
                ffstream.on('end', function () {
                    a = 1
                })

        })

        return [au, ms1]
    },

}


/*
    ffmpeg -i F:\videos\anime\Pokemon\S14\Best_Wishes\06.mkv
          Stream #0:2: Subtitle: ass (default)
          Stream #0:3: Subtitle: ass
          Stream #0:4: Subtitle: ass

    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])

    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
      "-ar", "44100", "-ac", "2", "-b:a", "192k", \
        "tmp.mp3"])
    
    https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/issues/470

    ffmpeg
  //.withVideoCodec('h264_nvenc')
  .withVideoBitrate(8000)
  .withAudioCodec('libmp3lame')
  .withVideoCodec('h264_nvenc')
  .outputOption([
    '-map 0',
    '-map -v',
    '-map -a',
    '-map 0:V',
    '-map 0:m:language:eng?', // TODO: This should be an input parameter to be able to change language
    '-deadline realtime',
    '-lag-in-frames 0',
    '-static-thresh 0',
    '-frame-parallel 1',
    '-crf 4',
    '-movflags frag_keyframe+faststart',
    '-pix_fmt yuv420p',
    '-sn',
    '-max_muxing_queue_size 9999'
  ])
  .outputFormat('mp4')
};


//			.outputOptions(["-movflags", "frag_keyframe+empty_moov"]) //without these options ffmpeg errors with `muxer does not support non seekable output`


*/



```

```javascript




(async () => {
    
    let fs = require('fs')
    let ff = require('./ffmpeg')

    let vdpath = String.raw`F:\videos\anime\Pokemon\S14\Best_Wishes\06.mkv`

    let [audio, ms1] = await ff.extractAudio(vdpath, 'mp3', `00:00:00.000`, `00:00:07.520`)  // output type, begintime, endtime
    
    let [srt_zhs, ms2] = await ff.extractSubtitle(vdpath, 'srt', 0) // the nth subtitle stream
    srt_zhs = srt_zhs.toString('utf8')

    // a = 1

    let [srt_jp, ms3] = await ff.extractSubtitle(vdpath, 'srt', 2) // the nth subtitle stream
    srt_jp = srt_jp.toString('utf8')

    a = 1
})()


```









```javascript
  var vd = require('fs').createReadStream('F:/1.mkv')
  var au = require('fs').createWriteStream('tmp.mp3')

  ffmpeg(vd).output(au)
  .noVideo()
  .format('mp3')
  .outputOptions('-ab','192k')
  .outputOptions('-ss','00:01:12.960')
  .outputOptions('-to','00:01:14.640')
  .on('start',()=>{

    a = 1
    
  })
  .on('end', ()=>{ 

    a = 1
  })
  .run()
```



```javascript
  var vd = require('fs').createReadStream('F:/1.mkv')
  var au = require('fs').createWriteStream('tmp.srt')

  ffmpeg(vd).output(au)
  .noVideo()
  .format('srt')
  .outputOptions('-map','0:s:0')
  //.outputOptions('-ss','00:01:12.960')
  //.outputOptions('-to','00:01:14.640')
  .on('start',()=>{

    a = 1
    
  })
  .on('end', ()=>{ 

    a = 1
  })
  .run()
```





```javascript
npm i fluent-ffmpeg
var ffmpeg = require('fluent-ffmpeg');
const path = require('path');

var filename = './not-commit-test-file/1.mp4';
var full_path = path.resolve(filename);
console.log(full_path);

var command = ffmpeg(full_path);
command.outputOptions([
  '-vn',
  '-acodec copy',
]).save('output-audio.aac');
```



```javascript
function streamtogif(stream, begintime = 0, duration){ //Return promise buffer
  return new Promise((resolve, reject)=>{
  buffer = [] //prepare creation of the buffer for the gif
    function addChunk(chunk){ 
      this.buffer.push(chunk)
    }
    function getBuffer(cb){ //get buffer array
      cb(this.buffer);
    }
    ffmpegstream = ffmpeg()
    .outputOptions('-metadata', 'title=test')
    .input(stream)
    .fps(20)
    .setStartTime(begintime)
    .noAudio()
    .videoCodec('gif')
    .format('gif')

    if(duration){ffmpegstream.duration(duration)} //only define duration if defined in function's parameters
    ffmpegstream.on('start',()=>{
      //console.log("starting")
      this.buffer = []
    })
    .on('end', ()=>{ 
      getBuffer((buff)=>{
      finalBuffer = Buffer.concat(buff);
      resolve(finalBuffer);
      });
  }) 

    var ffstream = ffmpegstream.pipe(); //handle data 
    ffstream.on('data', function(chunk) {
      addChunk(chunk);
    })


    ffmpegstream.run()
  });
}

            finalBuffer = Buffer.concat(this.fileRead)
            const bufferStream = new Stream.PassThrough();
            bufferStream.end(finalBuffer);
            streamtogif(bufferStream).then((buffer)=>{
              upload = uploadpicture(buffer, "source/sportifeed").then((response)=>{ //success request
                res.status(200).json({success: true, message: "Successfully uploaded !", url: response.data.link});
              },(err)=>{ //error
                console.log(err)
                res.status(500).json({success: false, message: "Error happenned while uploading !"});
              }).catch((err)=>{
                console.log(err)
                res.status(500).json({success: false, message: "Error happenned while uploading !"});
              });
            },(err)=>{
              console.log(err);
            })

```



```
var FFmpeg = require('ffmpeg')

function ffmepgFunction(timeout, attempts) {
    try {
    var command = FFmpeg("http://localhost:9001");

    var stream = command.pipe();
    stream.on('data', function(chunk) {
    // do something with the data
    });
    } catch(e) {
        console.log(e);
        if(attempts > 0)
            setTimeout(() => ffmepgFunction(timeout, --attempts), timeout);
    }
}

ffmepgFunction(2000, 5);
```



### buffer

```
# 写文件改写内存流
(async () => {
  let [sr, ms] = await new Promise(function (resolve) {

    var ffmpeg = require('fluent-ffmpeg')

    var vd = require('fs').createReadStream('F:/1.mkv')
    //var au = require('fs').createWriteStream('tmp.srt')

    const stream = require('stream')
    let bufferStream = new stream.PassThrough()
    // Read the passthrough stream
    const buffers = []
    bufferStream.on('data', function (buf) {
      buffers.push(buf)
    })
    bufferStream.on('end', function () {
      const outputBuffer = Buffer.concat(buffers)
      let sr = outputBuffer.toString('utf8')
      // use outputBuffer
      resolve([sr, ''])
    })

    ffmpeg(vd)//.output(au)
      .noVideo()
      .format('srt')
      .outputOptions('-map', '0:s:0')
      //.outputOptions('-ss','00:01:12.960')
      //.outputOptions('-to','00:01:14.640')
      .writeToStream(bufferStream)
      // .on('start', () => {

      //   a = 1

      // })
      // .on('end', () => {

      //   a = 1

      //   resolve(['ok', 'ok.'])
      // })
      // .run()
  })
})().catch(e => console.error(e.message, e.stack))
```







### bytea



```
You can insert Buffer (https://nodejs.org/dist/latest-v14.x/docs/api/buffer.html) values into bytea fields.
```



```
 combinedBuffer = Buffer.allocUnsafe(this.remainingBuffer.byteLength + buffer.byteLength) 
 this.remainingBuffer.copy(combinedBuffer) 
 buffer.copy(combinedBuffer, this.remainingBuffer.byteLength) 
```



### HLS  mpv 推流

HLS  mpv 推流



## OpenCV



```
const mat = cv.imdecode(Buffer.from(data, 'base64))
mat.SaveImage(savePath)
```





```
const cv = require('opencv4nodejs');
 
const originalImage = cv.imread('C:/Users/N/Desktop/Test.jpg');
 
const grayImage = originalImage.bgrToGray();
 
cv.imshow('Grey Image', grayImage);
cv.imshow('Original Image', originalImage);
 
cv.waitKey();
```



```
// convert to normal array
const normalArray = Array.from(imageData);
//nest the pixel channels
const channels = 4 //canvas pixels contain 4 elements: RGBA
const nestedChannelArray = _.chunk(normalArray, channels);
const nestedImageArray = _.chunk(nestedChannelArray, height);

//nestedImageArray is the correct shape to be converted to matrix. 

const RGBAmat = new cv.Mat(nestedImageArray, cv.CV_8UC4);

//openCV often defaults to BGR-type image matrix, so lets color convert the pixel order

const BGRAmat = RGBAmat.cvtColor(cv.COLOR_RGBA2BGRA);
```



### 图片相似度

- https://juejin.cn/post/6844904016686628877



## GIF



```
https://github.com/kohler/gifsicle
```





## exec



```
# https://www.jianshu.com/p/b1dc42c152ab
```





```javascript
var exec = require('child_process').exec;

    const cmd = `cd ${global.startPath} && git pull origin master`;
    console.log(`updateCode:${new Date().getTime()}`);
    exec(cmd, (error, stdout, stderr) => {
      if (error) {
        throw error;
      }
      return res.msg(200, {
        stdout: stdout,
        stderr: stderr
      });
    })
```



```javascript

const mecabSpawn = require('mecab-spawn')
const mecab = mecabSpawn.spawn()


var spawn = require('child_process').spawn,
    child = spawn('phantomjs');

child.stdin.setEncoding('utf-8');
child.stdout.pipe(process.stdout);

child.stdin.write("console.log('Hello from PhantomJS')\n");

child.stdin.end(); /// this call seems necessary, at least with plain node.js executable
```



# SVG 格式

**SVG**

**关键词**：无损、矢量图、体积小、不失真、兼容性好

**可缩放矢量图形 **英文 Scalable Vector Graphics(SVG)，是无损的、矢量图。

SVG是一种用 XML 定义的语言，用来描述二维矢量及矢量/栅格图形。SVG提供了3种类型的图形对象：矢量图形（vectorgraphicshape例如：由直线和曲线组成的路径）、图象(image)、文本(text)。图形对象还可进行分组、添加样式、变换、组合等操作，特征集包括嵌套变换（nestedtransformations）、剪切路径（clippingpaths）、alpha 蒙板（alphamasks）、滤镜效果（filtereffects）、模板对象（templateobjects）和其它扩展（extensibility）。

SVG 跟上面这些图片格式最大的不同，是 SVG 是矢量图。这意味着 SVG 图片由直线和曲线以及绘制它们的方法组成。当你放大一个 SVG 图片的时候，你看到的还是线和曲线，而不会出现像素点。这意味着 SVG 图片在放大时，不会失真，所以它非常适合用来绘制企业 Logo、Icon 等。

**优点：**

- SVG 可被非常多的工具读取和修改（比如记事本）。
- SVG 与 JPEG 和 GIF 图像比起来，尺寸更小，且可压缩性更强。
- SVG 是可伸缩的。
- SVG 图像中的文本是可选的，同时也是可搜索的（很适合制作地图）。
- SVG 可以与 JavaScript 技术一起运行
- SVG图形格式支持多种滤镜和特殊效果，在不改变图像内容的前提下可以实现位图格式中类似文字阴影的效果。
- SVG图形格式可以用来动态生成图形。例如，可用 SVG 动态生成具有交互功能的地图，嵌入网页中，并显示给终端用户。

**缺点：**

- 渲染成本比较高，对于性能有影响。
- SVG 的学习成本比较高，因为它是可编程的。

**适用场景**

1、高保真度复杂矢量文档已是并将继续是 SVG 的最佳点。它非常详细，适用于查看和打印，可以是独立的，也可以嵌入到网页中
2、在WEB项目中的平面图绘制，如需要绘制线，多边形，图片等。
3、数据可视化。

> SVG 只是 Web 开发常用的一种矢量图，其实矢量图常见还有几种格式：BW 格式、AI 格式、CDR 格式、ICO 格式。



# pm2

```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目


cd /yingedu/soft/redis-6.2.6/src/
vi redis.conf
./redis-server /xxx/yyyy/redis.conf
pm2 --name redis start "./run.sh"

```



## rename



```
pm2 restart id --name newName
```



# nginx

- https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-7

```
yum install nginx
nginx -t # 显示主配置文件路径，并检查语法错误
systemctl start nginx
```





## 本地端口转发



```
yum install nginx
```





```
/etc/nginx/conf.d/default.conf

server{
    listen       xxx;
    server_name       localhost;
    location / {
     proxy_pass http://localhost:yyy;
     proxy_set_header    Host             $host;
         proxy_set_header    X-Real-IP        $remote_addr;
         proxy_set_header    X-Forwarded-For  $proxy_add_x_forwarded_for;
         proxy_set_header    HTTP_X_FORWARDED_FOR $remote_addr;
         proxy_redirect      default;
    }
}
```



## 转发websocket

```
# 同时转发http 和 websocket 
# /etc/nginx_conf.d/testDiff.conf
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream diffServer {
  server localhost:10000;
  server localhost:10001;
  server localhost:10002;
  server localhost:10003;
  server localhost:10004;
  server localhost:10005;
  server localhost:10006;
  server localhost:10007;
  server localhost:10008;
  server localhost:10009;
}

server {
  listen 7116;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://diffServer;
    }
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 9999999;
    proxy_connect_timeout 9999999;
    proxy_send_timeout 9999999;
  }
}
```

```
# /etc/nginx/nginx.conf
user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}
```



# docker

> ```
> doc\lang\programming\postgresql summary.md  看这里
> ### Xshell如何连接Docker容器中的Linux
> ```



- https://juejin.cn/post/6857283423380504584

  > 如何查看Docker容器环境变量，如何向容器传递环境变量

- https://xiaorui.cc/archives/1158

  - https://www.cnblogs.com/yinzhengjie/p/12239341.html

  > lscpu 
  >
  > ```
  > -m 128M # 内存限制 128M
  > --cpus 2 --cpuset-cpus 1,4 # 限制CPU 核心数为2，只分配第1核和第4核
  > 
  > 
  > # https://www.cnblogs.com/mingyueyy/p/15475150.html
  > Docker-Compose 是用来管理容器的，类似用户容器管家，我们有N多台容器或者应用需要启动的时候，如果手动去操作，是非常耗费时间的，如果有了 Docker-Compose 只需要一个配置文件就可以帮我们搞定，但是 Docker-Compose 只能管理当前主机上的 Docker，不能去管理其他服务器上的服务。意思就是单机环境。
  > 
  > Docker Swarm 是由Docker 公司研发的一款用来管理集群上的Docker容器工具，弥补了 Docker-Compose 单节点的缺陷，Docker Swarm 可以帮助我们启动容器，监控容器的状态，如果容器服务挂掉会重新启动一个新的容器，保证正常的对外提供服务，也支持服务之间的负载均衡。而且这些东西 Docker-Compose是不支持的，
  > 
  > 
  > ```
> curl https://xxxx.com/getData | jq
>
> jq 命令去除转义，最后输出的是格式化的json字符串，既去掉了转义字符


```
docker run --name running-blog-www\
 -p 4000:8080\
 -e "CONFIG_ENV=$(</path/to/config.json)"\
 -e BUILD_ENV=prod\
 -d blog-www:1.0.0
  
var app = new express();
switch ((process.env.ENV_TYP).toUpperCase()) {
    case 'DEV':
        ProxyConfig = require('./proxy/dev-proxy');
        break;
    case 'ST':
        ProxyConfig = require('./proxy/st-proxy');
        break;
    case 'PRD':
        ProxyConfig = require('./proxy/prd-proxy');
        break;
    default:
        ProxyConfig = require('./proxy/dev-proxy');
        break;
}
new ProxyConfig().setProxy(app);


export NODE_ENV=dev



```



```

var stdin = process.stdin,
    stdout = process.stdout,
    inputChunks = [];

stdin.resume();
stdin.setEncoding('utf8');

stdin.on('data', function (chunk) {
    inputChunks.push(chunk);
});

stdin.on('end', function () {
    var inputJSON = inputChunks.join(),
        parsedData = JSON.parse(inputJSON),
        outputJSON = JSON.stringify(parsedData, null, '    ');
    stdout.write(outputJSON);
    stdout.write('\n');
});
```



```

yum whatprovides ifconfig
yum whatprovides crontab
yum whatprovides git
yum install net-tools cronie -y

docker run -tid --name centos7_server_6006 -p 222:22 --privileged=true centos:7 /sbin/init
	# 此命令会自动下载镜像
	# -p 222:22 表示将宿主的222端口映射容器的22端口


docker exec -it centos7_server_6006 /bin/bash
	# 运行docker 的shell


docker ps
docker stop centos7_server_6006
docker start centos7_server_6006
	# 关闭和重启

yum install openssh-server -y
	# 安装ssh

vi /etc/ssh/sshd_config
	# 修改配置
	PermitRootLogin yes # 改成这个
	UsePAM no # 改成这个


systemctl start sshd
	# 启动ssh

eixt
	# 退出容器



docker inspect centos7_server_6006 | grep IPAddress
	# 查看IP
	--> "IPAddress": "10.88.0.2"
	
passwd root
	# 修改密码，容器名就是密码
	centos7_server_6006

systemctl stop firewalld
	# 关闭防火墙

ssh root@10.88.0.2 -p 22
	# 登录看看
	--> 成功


yum install nmap
	# 扫描指定端口是否开放	
	nmap 118.178.137.176 -p222
		PORT    STATE  SERVICE
		222/tcp closed rsh-spx	
			# 端口并没有开放

	netstat -aptn | grep -i 222
		tcp        0      0 0.0.0.0:222             0.0.0.0:*               LISTEN      45594/conmon
			# 好像本地 222 端口是开放了的

	lsof -i:222
		conmon  45594 root    5u  IPv4 446985      0t0  TCP *:rsh-spx (LISTEN)
			# 也是显示开放了


	https://blog.csdn.net/qq_39176597/article/details/111939051
		# linux关闭防火墙了，但端口还是访问不了

		systemctl  start  firewalld
			# 启动防火墙
			systemctl  status  firewalld

		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=6006/tcp --permanent
			# 开放端口
	
		firewall-cmd --reload
			# 重新加载配置文件
		
		firewall-cmd --list-ports
			# 查看已经开放的端口

		systemctl status polkit
		/usr/lib/polkit-1/polkitd --no-debug &

		docker ps
		docker stop centos7_server_6006




npm i -g pm2@4.5.1


/usr/local/node-v14.17.0-linux-x64/bin/pm2-dev -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2-dev
/usr/local/node-v14.17.0-linux-x64/bin/pm2 -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2
/usr/local/node-v14.17.0-linux-x64/bin/pm2-docker -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2-docker
/usr/local/node-v14.17.0-linux-x64/bin/pm2-runtime -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2-runtime


ln -s /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2 /usr/local/bin/pm2




传文件

docker ps
	# 显示容器 ID
	6f7dcc6f9fa3  quay.io/centos/centos:7  /sbin/init  8 hours ago  Up 8 hours ago  0.0.0.0:222->22/tcp  centos7_server_6006


docker cp /yingedu/project/aicbyserver_v2 centos7_server_6006:/project
	# 复制代码
docker cp /usr/local/node-v14.17.0-linux-x64 centos7_server_6006:/usr/local
	# 复制node


进 docker 启动服务

	docker exec -it centos7_server_6006 /bin/bash
	cd /usr/local
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/node /usr/local/bin/node && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/npm /usr/local/bin/npm && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/npx /usr/local/bin/npx && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/pm2 /usr/local/bin/pm2
	
	systemctl stop firewalld

	cd /project/aicbyserver_v2
	pm2 --name aicbyserver_v2_6006 start "node server.js"
	
	docker There are stopped jobs.
	kill -9 $(jobs -p)
		# 可以正常 exit 容器了
	exit


退出docker, 在宿主机 访问 docker 服务

	docker inspect centos7_server_6006 | grep IPAddress
	ping 10.88.0.2
		# docker ip

	
固定容器 IP   https://cloud.tencent.com/developer/article/1418033


	docker network create --subnet=172.18.0.0/16 custom
	docker network create --subnet 10.10.10.10/16 custom
		docker run -d --name target-service --net static --ip 10.10.10.10 py:test
		docker run -tid --name centos7_server_6006 --net=custom --ip=172.18.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
		# 创建自定义网络				

	docker network ls


	--net=es-network --ip=172.18.0.1

	# 删除容器
	docker stop centos7_server_6006
	docker rm centos7_server_6006
	docker network rm custom
		# 删除网络

	# 创建容器
	docker run -tid --name centos7_server_6006 --net=bridge --ip=10.88.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
	docker run -tid --name centos7_server_6006_ENV --net=bridge --ip=10.88.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
		# 使用默认网络，并固定 IP
		
	docker run -tid --name centos7_server_6006 --net=custom --ip=172.18.0.2 -p 222:22 --privileged=true centos:7 /sbin/init

		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口




环境变量

let j = require('./config.js')
require('fs').writeFileSync('config.json', JSON.stringify(j).replace(/"/g, `\\"`), {encoding:'utf8', flag:'w'} )



--env-file path_to_env_file 选项将其传递到用于启动容器代理的 docker run 命令。


docker run --name running-blog-www\
 -p 4000:8080\
 -e "CONFIG_ENV=$(</path/to/config.json)"\


docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV={\"updatePassword\":\"\"}" --net=bridge --ip=10.88.0.3  --privileged=true centos:7 /sbin/init


docker cp /usr/local/node-v14.17.0-linux-x64 centos7_server_6006_ENV:/usr/local


docker exec -it centos7_server_6006_ENV /bin/bash
	# 运行docker 的shell

	kill -9 $(jobs -p) && exit
		# 可以正常 exit 容器了

	docker stop centos7_server_6006_ENV
	docker start centos7_server_6006_ENV

	pm2 --name aicbyserver_v2_6006 start "node server.js"

	pm2 save
	pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
	pm2 resurrect // 重启备份的所有项目

	vi auto_run.ssh
		pm2 resurrect 
	
	chmod +x auto_run.sh

	设置开机启动
	vi /etc/rc.d/rc.local
		/project/auto_run.sh 
	chmod +x /etc/rc.d/rc.local
	
	 crontab -e
		@reboot  /project/auto_run.sh


	docker exec -it centos7_server_6006_ENV  pm2 resurrect;/bin/bash
		# 在容器内执行命令
	docker exec -it centos7_server_6006_ENV /bin/bash
		# 进入容器


( async ()=> {

  let bent = require('bent')
  
  let json = {
    userID: 0
  }
  
  let post = bent('http://127.0.0.1:6006', 'POST', 'json', 200)
  let response = await post('/test', json)
  console.log( response )

}) ()


JSON.parse( process.env.CONFIG_ENV )


CONFIG_ENV



执行多条命令使用分号隔开
docker exec web-blog /bin/sh -c "mkdir /www/default/runtime; \
                                 chmod +x /www/default/ank; \
                                 /www/default/ank clearcache; \
                                 /www/default/ank optimize:config; \
                                 /www/default/ank optimize:preload; \
                                 chown -R www-data:www-data /www/default; \
                                 chmod 544 -R /www/default; \
                                 chmod 754 -R /www/default/runtime;"

docker run 5800 sh -c "ls && echo '-------' &&  ls"


阿里云镜像库的通过git自动打包功能

https://blog.csdn.net/YL3126/article/details/122184386

使用私有镜像仓库创建应用

https://help.aliyun.com/document_detail/86307.html


通过docker和gitlab实现项目自动打包部署

https://blog.csdn.net/qq_44845473/article/details/126045368


Docker-compose编排微服务顺序启动

https://cloud.tencent.com/developer/article/1620658?from=15425



Docker一从入门到实践  ENTRYPOINT 入口点

https://yeasy.gitbook.io/docker_practice/image/dockerfile/entrypoint
	# docker 可以被当作命令行来运行，还可以加参数

FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
ENTRYPOINT [ "curl", "-s", "http://myip.ipip.net" ]
这次我们再来尝试直接使用 docker run myip -i：
$ docker run myip
	当前 IP：61.148.226.66 来自：北京市 联通


在构建镜像的时候，需要额外小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。
分层存储的特征还使得镜像的复用、定制变的更为容易。甚至可以用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。

按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。所有的文件写入操作，都应该使用 数据卷（Volume）、或者 绑定宿主目录，在这些位置的读写会跳过容器存储层，直接对宿主（或网络存储）发生读写，其性能和稳定性更高。
数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。因此，使用数据卷后，容器删除或者重新运行之后，数据却不会丢失。


仓库名经常以 两段式路径 形式出现，比如 jwilder/nginx-proxy，前者往往意味着 Docker Registry 多用户环境下的用户名，后者则往往是对应的软件名。


列出已经下载下来的镜像
	docker image ls

yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine

	# 卸载 docker


yum install -y yum-utils

yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
	# 官方源 https://download.docker.com/linux/centos/docker-ce.repo

sudo sed -i 's/download.docker.com/mirrors.aliyun.com\/docker-ce/g' /etc/yum.repos.d/docker-ce.repo
	# 切换为阿里源

vi /etc/yum/pluginconf.d/fastestmirror.conf
	enabled=0;  # 改成这个

vi /etc/yum.conf
	plugins=0; # 改成这个


yum install docker-ce docker-ce-cli containerd.io -y
	# 安装 docker

docker run --rm hello-world
	# 测试是否安装正确
		# --rm 表示运行后既删除


systemctl enable docker && \
systemctl start docker


docker pull nginx
docker run --name webserver -d -p 80:80 nginx
	# 运行 docker 镜像，80 映射 80

curl http://localhost
	# 成功访问网页

docker exec -it webserver bash -c "echo $PATH"
	# 这里的 $PATH 会被解析成本机的值 

docker exec -it webserver bash -c "echo '<h1>Hello, Docker\!</h1>' > /usr/share/nginx/html/index.html"
	# 修改主页，注意：感叹号需要转义
	curl http://localhost

docker diff webserver
	# 我们修改了容器的文件，也就是改动了容器的存储层。
	# 比较相对基础镜像修改了哪


慎用docker commit

使用 docker commit 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为 黑箱镜像，换句话说，就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。而且，即使是这个制作镜像的人，过一段时间后也无法记清具体的操作。这种黑箱镜像的维护工作是非常痛苦的。


使用 Dockerfile 定制镜像
	Dockerfile 是一个文本文件，其内包含了一条条的 指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建

定制 mynjginx 镜像

mkdir mynginx && \
cd mynginx && \
touch Dockerfile && \
echo "FROM nginx 
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html" > Dockerfile


docker build -t nginx:v2 .
	构建镜像

docker run --name webserver -d -p 80:80 nginx:v2 && \
curl http://localhost && \
docker stop webserver && \
docker rm webserver
	# 运行 docker 镜像，80 映射 80


https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz


yum install net-tools cronie -y

docker run -tid --name centos7_server_6006 -p 222:22 --privileged=true centos:7 /sbin/init
	# 此命令会自动下载镜像
	# -p 222:22 表示将宿主的222端口映射容器的22端口




构建实际项目

docker network ls
docker network create --subnet=172.20.0.0/16 customnetwork
	# 创建自定义网络


docker system prune --volumes
	# 删除所有未使用镜像及缓存，自义定网络

docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
	# 自定义网络不存在则创建

docker run -tid --name centos7_server_6006 -p 222:22 --privileged=true centos:7 /sbin/init

docker pull centos:7
	# 拉镜像只需要一次
	# docker image ls
	# docker image rm centos:7
	# docker image rm centos7_server_6006

docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    git clone http://用户名:这里是AccessTokens@gitlab.xxx.git && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=双引号转义了的json配置串" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006



	kill -9 $(jobs -p)
		# 可以正常 exit 容器了


配置 nginx 80 转 6006


vi /etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}



vi /etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}

server {
  listen 80;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://centos7_server_6006;
    }
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 9999999;
    proxy_connect_timeout 9999999;
    proxy_send_timeout 9999999;
  }
}


nginx -s reload











nmap 172.20.0.2 -p6006
	# 扫描指定端口是否开放

git config --global user.name "gada" && \
git config --global user.email "x50@qq.com" && \
git config --global push.default matching  


git config --system --list
	# 查看系统config
　　
git config --global  --list
	# 查看当前用户（global）配置

git config --local  --list
	# 查看当前仓库配置信息


ssh-keygen -t rsa -C "162350@qq.com"

ssh -i ~/.ssh/id_rsa -T git@xxx.com
	--> Welcome to GitLab

yum install \
https://repo.ius.io/ius-release-el7.rpm \
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
yum remove git && \
yum install git236 -y
	# need Git version 2.3.0

git clone http://用户名:这里是AccessTokens@gitlab.xxxx.git



解决方式是创建一个access token，然后在拉取代码时带上自己的username和token,就不用再输入用户名密码

具体操作如下：

1、登录 gitlab，点击右上角自己头像选择 settings

2、左边导航栏选择 Access Tokens

3、name 输入框给自己要创建的token起个名字

4、点击create personal access token 创建token （下面还有到期时间、权限可以根据自己需要选择具体如下图）

5、在docker容器中可以通过如下方式使用

git clone https://用户名:token@仓库地址



mkdir /root/.ssh/ && \
cat /root/keyksb > /root/.ssh/id_rsa && \
chmod 600 /root/.ssh/id_rsa && \
touch /root/.ssh/known_hosts && \
ssh-keyscan gitlab.ksbao.com >> /root/.ssh/known_hosts
	# https://github.com/jmrf/private-repo-clone-docker-build-example/blob/master/test.Dockerfile




export GIT_SSH_COMMAND="ssh -i /root/keyksb" && git clone http://xxxx.git

GIT_SSH_COMMAND='ssh -o IdentitiesOnly=yes -i /root/keyksb -F /dev/null' git clone http://xx.git

git clone 私有仓的例子
https://github.com/jmrf/private-repo-clone-docker-build-example






自定义IP  Docker Compose
https://www.howtogeek.com/devops/how-to-assign-a-static-ip-to-a-docker-container/


How to set static ip when using default network

docker-compose will create a network named after your project name (usually your folder, unless you specified COMPOSE_PROJECT_NAME) suffixed with _default. So if the project name is foo, the default network name will be foo_default. It will always be this unless you specify otherwise.

Once this network has been created, docker-compose will never remove it. This means you need to remove it yourself using docker.

$ docker network rm foo_default
Once you've done this, docker-compose will attempt to recreate your network. If you've specified some network options in your docker-compose.yml file, it will create the network with your new options.

version: '3.4'
networks:
  default:
    ipam:
      config:
        - subnet: 10.5.0.0/16


FROM centos:7

RUN set -x; buildDeps='curl' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && curl -O "https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz" \
    && tar -xzvf node-v14.21.1-linux-x64.tar.gz -C /usr/local  \
    && apt-get purge -y --auto-remove $buildDeps

镜像是多层存储，每一层的东西并不会在下一层被删除，会一直跟随着镜像。因此镜像构建时，一定要确保每一层只添加真正需要添加的东西，任何无关的东西都应该清理掉

```



```
docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    yum install -y nginx redis && \\
    git clone https://用户名:token@仓库地址 && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=冒号转义后的json" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006
```



```
docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    yum install -y nginx redis nfs-utils crontabs && \\
    mkdir -p /project/shared && \\
    mkdir -p /project/script && \\
    chmod 755 /project/shared && \\
    cd /project && \\
    git clone http://用户名:AccessToten@gitlab.xxxxx.git && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /project/aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=这里放冒号转义后的json" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /project/aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' "  && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable rpcbind && systemctl start rpcbind" && \
docker exec -it centos7_server_6006_ENV bash -c "mkdir -p /project/shared/test_cooperate_img && chmod 755 /project/shared/test_cooperate_img && \\
    ls -al /project/shared/test_cooperate_img" && \
docker exec -it centos7_server_6006_ENV bash -c "showmount -e 172.16.15.13" && \
docker exec -it centos7_server_6006_ENV bash -c "mount -t nfs 172.16.15.13:/yingedu/web/aicby_v2/test_cooperate_img  /project/shared/test_cooperate_img" && \
docker exec -it centos7_server_6006_ENV bash -c "echo 'hello from docker' > /project/shared/test_cooperate_img/hi.txt" && \
cat /yingedu/web/aicby_v2/test_cooperate_img/hi.txt && \
docker exec -it centos7_server_6006_ENV bash -c "echo 'umount /project/shared/test_cooperate_img 
mount -t nfs 172.16.15.13:/xx/xxx  /project/xxxxx_img  
if [ \$? -ne 0 ]; then 
    echo mount failed  
    sleep 30s; echo try agin 
    umount /project/shared/test_cooperate_img 
    mount -t nfs 172.16.15.13:/xxx_img  /project/shared/test_cooperate_img 
else 
    echo mount nfs succeed
fi
' > /project/script/auto_mount.sh" && \
docker exec -it centos7_server_6006_ENV bash -c "echo '@reboot  /project/script/auto_mount.sh' > /var/spool/cron/root" && \
docker exec -it centos7_server_6006_ENV bash -c "chmod +x /project/script/auto_mount.sh" && \
docker exec -it centos7_server_6006_ENV bash -c "crontab -l" && \
docker exec -it centos7_server_6006_ENV bash -c "cat /project/script/auto_mount.sh" && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006




	kill -9 $(jobs -p)
		# 可以正常 exit 容器了


配置 nginx 80 转 6006


vi /etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}



vi /etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}

server {
  listen 80;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://centos7_server_6006;
    }
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 9999999;
    proxy_connect_timeout 9999999;
    proxy_send_timeout 9999999;
  }
}


nginx -s reload


nmap 172.20.0.2 -p6006
	# 扫描指定端口是否开放






```



```powershell


$t = docker ps -a
if ($t -like "*centos7_server_6006_ENV*")
{
    docker stop centos7_server_6006_ENV
    docker rm centos7_server_6006_ENV
    Write-Host "object centos7_server_6006_ENV deleted"
}

$t = docker image ls
if ($t -like "*centos7_server_6006*")
{
    docker image rm centos7_server_6006
    Write-Host "image centos7_server_6006 deleted"
}

$t = docker image ls
if ($t -like "*centos*")
{
    docker image rm centos:7
    Write-Host "image centos:7 deleted"
}

$t = docker network ls
if ($t -like "*customnetwork*")
{
    docker network rm customnetwork
    Write-Output 'customnetwork deleted'
}

docker system prune --volumes

docker network create --subnet=172.20.0.0/16 customnetwork
Write-Output 'customnetwork created'

docker pull centos:7
Write-Output 'image centos:7 created'

$dir="E:\docker"
$profileDir="$dir\centos7_server_6006"
Write-Host $profileDir
if (Test-Path -Path $profileDir) {
    Remove-Item -Path $profileDir -Force -Recurse
}


New-Item -ItemType Directory -Path $profileDir -Force
#New-Item -ItemType File -Path "$profileDir\Dockerfile"

Set-Location $profileDir


[System.Text.Encoding]::UTF8.GetBytes("FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \
yum install -y `$buildDeps && \
yum install -y nginx redis nfs-utils crontabs libaio numactl initscripts && \
mkdir -p /project/shared && \
mkdir -p /project/script && \
chmod 755 /project/shared && \
cd /project && \
git clone https://账号:xx@github.com/dlxj/server_template.git && \
curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz' && \
curl -O 'https://cdn.mysql.com/archives/mysql-5.7/mysql-5.7.39-linux-glibc2.12-x86_64.tar.gz' && \
tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \
tar zxvf mysql-5.7.39-linux-glibc2.12-x86_64.tar.gz -C /usr/local && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \
npm install cnpm@7.1.0  pm2@4.5.1 -g && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \
cd /project/server_template && \
npm i && \
ln -s /usr/local/mysql-5.7.39-linux-glibc2.12-x86_64 /usr/local/mysql && \
cd /usr/local/mysql && \
groupadd mysql && \
useradd -r -g mysql mysql && \
cd /usr/local/mysql && \
chown -R mysql . && \
chgrp -R mysql . && \
bin/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data && \
cp support-files/mysql.server /etc/init.d/mysql.server && \
service mysql.server start && \
service mysql.server status && \
cat /root/.mysql_secret") | Set-Content Dockerfile -Encoding Byte

docker build -t centos7_server_6006 .

docker run -tid --name centos7_server_6006_ENV -e 'CONFIG_ENV={\"updatePassword\":\"\",\"debugPassword\":\"\",\"dev\":true,\"http\":{\"port\":6006,\"headers\":{\"Server\":\"Server\",\"Access-Control-Allow-Origin\":\"*\",\"Content-Type\":\"text/json\",\"Access-Control-Allow-Headers\":\"content-type\",\"Access-Control-Request-Method\":\"GET,POST\"},\"encrypt\":false,\"privateKey\":\"\",\"publicKey\":\"\"},\"service\":{\"privateKey\":\"\",\"publicKey\":\"\",\"require\":{}},\"dbs\":{\"localDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"ocr\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":4096},\"defaultDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"baseDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"tiku_bookDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"tmp\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"ocrDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"temp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50}},\"redis\":{\"defaultDB\":{\"host\":\"127.0.0.1\",\"port\":6379,\"prefix\":null,\"db\":0}},\"dataSet\":{}}' --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 6006:6006 -p 3306:3306 -p 6379:6379 -p 543:543  --privileged=true centos7_server_6006 /sbin/init 
docker exec -it centos7_server_6006_ENV bash -c "cd /project/server_template && pm2 --name centos7_server_6006 start 'node server.js' "  
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" 
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" 
docker exec -it centos7_server_6006_ENV bash -c "pm2 logs centos7_server_6006"
```





```
# 删除和重建镜像和网络
$t = docker ps -a
if ($t -like "*centos7_server_6006_ENV*")
{
    docker stop centos7_server_6006_ENV
    docker rm centos7_server_6006_ENV
    Write-Host "object centos7_server_6006_ENV deleted"
}

$t = docker image ls
if ($t -like "*centos7_server_6006*")
{
    docker image rm centos7_server_6006
    Write-Host "image centos7_server_6006 deleted"
}

$t = docker image ls
if ($t -like "*centos*")
{
    docker image rm centos:7
    Write-Host "image centos:7 deleted"
}

$t = docker network ls
if ($t -like "*customnetwork*")
{
    docker network rm customnetwork
    Write-Output 'customnetwork deleted'
}

docker system prune --volumes

docker network create --subnet=172.20.0.0/16 customnetwork
Write-Output 'customnetwork created'

docker pull centos:7
Write-Output 'image centos:7 created'
```





```
b64.js 转义配置
let j = require('./config.js')
require('fs').writeFileSync('config.json', JSON.stringify(j).replace(/"/g, `\\"`), {encoding:'utf8', flag:'w'} )
console.log(JSON.stringify(j).replace(/"/g, `\\"`))
require('fs').writeFileSync('config.json', JSON.stringify(j).replace(/"/g, `\\"`), {encoding:'utf8', flag:'w'} )
```



## wsl2

- https://learn.microsoft.com/en-us/windows/wsl/install-manual

  > ```
  > Turn Windows features on or off # 搜索框输入
  > 	# 打开选项和功能
  > 把 linux 子系统 什么虚拟 全都打开
  > ```

```
wsl_update_x64.msi 安装出错 2503

For WSL2 you will need 2 Windows components so make sure they are already enabled:
Microsoft-Windows-Subsystem-Linux
VirtualMachinePlatform

Also it seems some people have problems with the installer extracting the kernel.
You can always extract it manually with:
msiexec /a "wsl_update_x64.msi" /qb TARGETDIR="C:\temp"
and then copy the kernel file from C:\temp to C:\Windows\System32\lxss\tools

Final version shouldn't have this problem since the install comes from Windows Update.
```





## Docker Desktop for Windows

### win10 ping 不通 docker

```
the ip address you see via docker inspect command, is used by docker for internal networking and communication. It's not accessible from outside. 
```



```
控制面板 -> 程序和功能 -> 启用“适用于Linux的Windows子系统”

### docker 中使用显卡
wsl --install
	# 新版 win10支持

- https://blog.csdn.net/ltochange/article/details/121339718




https://learn.microsoft.com/en-us/windows/wsl/install-manual
	# 旧版 win10 安装方法
```



```
docker system prune --volumes -y 

$imageExists = docker image ls | Select-String -Pattern 'centos:7'
if ($imageExists -eq $null) {
    Write-Host 'image centos:7 not found, pull'
    docker pull centos:7
    Write-Host 'image centos:7 pull success'
}

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

New-Item -ItemType Directory -Path centos7_server_8880
cd centos7_server_8880
New-Item -ItemType File -Path Dockerfile

Write-Output "FROM centos:7
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \
    yum install -y `$buildDeps && \
    yum install -y nginx redis nfs-utils crontabs && \
    mkdir -p /project/shared && \
    mkdir -p /project/script && \
    chmod 755 /project/shared && \
    cd /project && \
    git clone http://用户名:AccessToten@gitlab.xxxx.git && \
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \
    cd /project/aicbyserver_v2 && \
    cnpm i" > Dockerfile
    
   
 

```



## 解决 Failed to get D-Bus connection

```

docker run -tid --name centos77 --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
	# 特权模式运行

docker ps -a

docker exec -it centos77 /bin/bash

systemctl
	# 实测 win10 的 docker desktop 出错


```



- https://www.jianshu.com/p/e670ae82e97a 替换 systemctl 法
  - https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py  下载

```

cd D:\GitHub\echodict\docker\centos7_server_8880

docker cp systemctl.py centos77:/root

docker exec -it centos77 /bin/bash

cd /root

mv /usr/bin/systemctl /usr/bin/systemctl.old

cp systemctl.py /usr/bin/systemctl

chmod +X /usr/bin/systemctl
	# 后面用它运行 ssd 服务确实成功了 


```



## 传文件 

```
传文件

cd D:\GitHub\echodict\docker\centos7_server_8880

docker cp systemctl.py centos77:/root




docker ps
	# 显示容器 ID
	6f7dcc6f9fa3  quay.io/centos/centos:7  /sbin/init  8 hours ago  Up 8 hours ago  0.0.0.0:222->22/tcp  centos7_server_6006


docker cp /xxx/project/aicbyserver_v2 centos7_server_6006:/project
	# 复制代码
docker cp /usr/local/node-v14.17.0-linux-x64 centos7_server_6006:/usr/local
	# 复制node
```





## ssh 进 docker



```

yum install openssh-server -y
	# 安装ssh

vi /etc/ssh/sshd_config
	# 修改配置
	PermitRootLogin yes # 改成这个
	UsePAM no # 改成这个


systemctl start sshd
	# 启动ssh
	# 发现不成功
		systemctl start polkit
			--> polkit.service not found
			yum install polkit
				systemctl start polkit
					--> unsupported run type 'dbus'  # 算了，不用 ssh 了

eixt
	# 退出容器



docker inspect centos77 | grep IPAddress
	# 查看IP
	--> "IPAddress": "10.88.0.2"
	--> 172.17.0.2 Docker for windows 是这个
	
passwd root
	# 修改密码，容器名就是密码
	centos7_server_6006

systemctl stop firewalld
	# 关闭防火墙

ssh root@10.88.0.2 -p 22
	# 登录看看
	--> 成功
```





## 指定端口是否开放

```
yum install nmap
	# 扫描指定端口是否开放	
	nmap 118.178.137.176 -p222
		PORT    STATE  SERVICE
		222/tcp closed rsh-spx	
			# 端口并没有开放

	netstat -aptn | grep -i 222
		tcp        0      0 0.0.0.0:222             0.0.0.0:*               LISTEN      45594/conmon
			# 好像本地 222 端口是开放了的

	lsof -i:222
		conmon  45594 root    5u  IPv4 446985      0t0  TCP *:rsh-spx (LISTEN)
			# 也是显示开放了


	https://blog.csdn.net/qq_39176597/article/details/111939051
		# linux关闭防火墙了，但端口还是访问不了

		systemctl  start  firewalld
			# 启动防火墙
			systemctl  status  firewalld

		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=6006/tcp --permanent
			# 开放端口
	
		firewall-cmd --reload
			# 重新加载配置文件
		
		firewall-cmd --list-ports
			# 查看已经开放的端口

		systemctl status polkit
		/usr/lib/polkit-1/polkitd --no-debug &

		docker ps
		docker stop centos7_server_6006
```





## 如果需要更多的端口映射

- https://www.cnblogs.com/miracle-luna/p/13714709.html  找不到 iptables

  ```
  systemctl stop firewalld && \
  systemctl mask firewalld && \
  yum install -y iptables iptables-services && \
  systemctl start iptables && \
  systemctl status iptables && \
  systemctl enable iptables
  
  ```

  

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





## 导出镜像

- https://www.hangge.com/blog/cache/detail_2411.html



```
docker save centos7_server_6006 > centos7_server_6006.tar

docker save centos7_server_6006 | Set-Content centos7_server_6006.tar -Encoding Byte

```





# DNS 解锁

- https://aws.amazon.com/cn/wavelength

- https://vlike.work/tech/all-dns-unlock-netflix.html

  

原生ip也不一定解锁…100%解锁的只有家宽

想看日本奈飞?绿云25刀就行

找一台全解锁Netflix的小鸡，比如甲骨文鸡

如果你有信用卡呢…可以去试试白 女票 甲骨文…如果没有就在论坛里收一个解锁奈飞的绿云新加坡，年付20刀

日本流媒体解锁专用机 日本原生IP

## 解锁测试

```
bash <(curl -L -s https://raw.githubusercontent.com/lmc999/RegionRestrictionCheck/main/check.sh)
```





## 非V2ray相关协议简单方法-直接修改VPS的系统DNS

- SS SSR Trojan等

由于这些协议本身无法进行DNS分流，请使用如下命令配置DNS：

- Debian/centos系统

```shell
  echo -e "nameserver 4.4.4.4（以实际为准）" > /etc/resolv.conf
       
  chattr +i /etc/resolv.conf
```

第一行命令是将解锁DNS添加为系统DNS

第二行命令是将DNS文件属性修改为只读(避免被系统复写修改）

- 移除操作

```shell
   chattr -i /etc/resolv.conf
   echo -e "nameserver 8.8.8.8" > /etc/resolv.conf
```

- ubuntu系统

```shell
修改DNS
vi /etc/systemd/resolved.conf
输入
DNS=4.4.4.4（以实际为准）

:wq保存后

systemctl daemon-reload
systemctl restart systemd-resolved.service
mv /etc/resolv.conf /etc/resolv.conf.bak
ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
```

- 移除操作

```shell
修改DNS
vi /etc/systemd/resolved.conf
输入
DNS=8.8.8.8
DNS=1.1.1.1

:wq保存后

systemctl daemon-reload
systemctl restart systemd-resolved.service
mv /etc/resolv.conf /etc/resolv.conf.bak
ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
```

- 注意 部分香港CMI屏蔽了UDP 53的查询，我的落地已经开启了TCP53.请在/etc/resolv.conf文件中第一行添加

```shell
options use-vc
```

- Shadowsocks-libev 版本

```shell
打开配置文件 默认 /etc/shadowsocks-libev/config.json
修改"nameserver":"4.4.4.4（以实际为准）"
```

- SS docker 版本

添加参数 `-d "4.4.4.4（以实际为准）"`

## 非V2ray相关协议复杂方法-VPS安装dnsmasq实现DNS解锁分流

需要有一定使用基础，此处以debian系统为例

一.安装dnsmasq

```shell
apt-get -y install dnsmasq
```

二.配置dnsmasq

1.配置文件/etc/dnsmasq.conf

```shell
vi /etc/dnsmasq.conf

server=/netflix.com/4.4.4.4
server=/disneyplus.com/4.4.4.4
...
...
resolv-file=/etc/resolv.dnsmasq.conf

具体需要添加的域名请在TG群发送“域名规则”获取。4.4.4.4以实际DNS为准。
```

2.配置文件/etc/resolv.dnsmasq.conf

```shell
vi /etc/resolv.dnsmasq.conf

nameserver 1.1.1.1
nameserver 8.8.8.8
```

3.设置VPS系统DNS，将本机dnsmasq作为系统DNS服务器。参考上面的操作

```shell
 chattr -i /etc/resolv.conf
 echo -e "nameserver 127.0.0.1" > /etc/resolv.conf
 chattr +i /etc/resolv.conf      
```

4.重启dnsmasq

```shell
/etc/init.d/dnsmasq restart
```

四.卸载

```shell
apt-get remove dnsmasq
chattr -i /etc/resolv.conf
chmod 777 /etc/resolv.conf
echo -e "nameserver 8.8.8.8" > /etc/resolv.conf
```

## V2ray相关协议，DNS分流

标准配置文件修改要素：

1.开启流量识别

```json
  "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ]
      }
```

2.修改出口流量域名分类方式

```json
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {
        "domainStrategy":"UseIP"
      }
    }
  ]
```

3.添加DNS分流

```json
   "dns": {
    "servers": [
      "1.1.1.1","8.8.8.8", 
      {
        "address": "4.4.4.4（以实际为准）", 
        "port": 53,
        "domains": [
           "geosite:netflix"
        ]
      }
    ]
  }
```

一般默认配置文件地址

V2ray

```shell
/usr/local/etc/v2ray/config.json

修改完成后重启 systemctl restart v2ray
```

Xray

```shell
/usr/local/etc/xray/config.json

修改完成后重启 systemctl restart xray
```

完整配置文件示例（wulabing-Xray脚本）：

```json
{
 "log": {
   "access": "/var/log/xray/access.log",
   "error": "/var/log/xray/error.log",
   "loglevel": "warning"
 },
 "inbounds": [
   {
     "port": 443,
     "protocol": "vless",
     "settings": {
       "clients": [
         {
           "id": "123456-789-123456-45678-12345678",
           "flow": "xtls-rprx-direct"
         }
       ],
       "decryption": "none",
       "fallbacks": [
         {
           "dest": 60000,
           "alpn": "",
           "xver": 1
         },
         {
           "dest": 60001,
           "alpn": "h2",
           "xver": 1
         }
       ]
     },
     "streamSettings": {
       "network": "tcp",
       "security": "xtls",
       "xtlsSettings": {
         "minVersion": "1.2",
         "certificates": [
           {
             "certificateFile": "/usr/local/etc/xray/self_signed_cert.pem",
             "keyFile": "/usr/local/etc/xray/self_signed_key.pem"
           },
           {
             "certificateFile": "/ssl/xray.crt",
             "keyFile": "/ssl/xray.key"
           }
         ]
       }
     },
     "sniffing": {
       "enabled": true,
       "destOverride": [
         "http",
         "tls"
       ]
     }
   }
 ],
 "outbounds": [
   {
     "protocol": "freedom",
     "settings": {
       "domainStrategy": "UseIP"  
     }
   }
 ],
 "dns": {
   "servers": [
     "1.1.1.1","8.8.8.8", 
     {
       "address": "4.4.4.4", 
       "port": 53,
       "domains": [
          "geosite:netflix" ,"geosite:disney"
       ]
     }
   ]
 }
}
```



## 其他脚本示例

## x-ui

```shell
bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)
```

进入【面板设置】——【Xray相关设置】替换文件

```json
{
  "api": {
    "services": [
      "HandlerService",
      "LoggerService",
      "StatsService"
    ],
    "tag": "api"
  },
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 62789,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "127.0.0.1"
      },
      "tag": "api"
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {"domainStrategy": "UseIP"}
    },
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ],
  "policy": {
    "system": {
      "statsInboundDownlink": true,
      "statsInboundUplink": true
    }
  },
  "routing": {
    "rules": [
      {
        "inboundTag": [
          "api"
        ],
        "outboundTag": "api",
        "type": "field"
      },
      {
        "ip": [
          "geoip:private"
        ],
        "outboundTag": "blocked",
        "type": "field"
      },
      {
        "outboundTag": "blocked",
        "protocol": [
          "bittorrent"
        ],
        "type": "field"
      }
    ]
  },    "dns": {
    "servers": [
      "1.1.1.1","8.8.8.8", 
      {
        "address": "4.4.4.4（以实际为准）", 
        "port": 53,
        "domains": [
           "geosite:netflix"
        ]
      }
    ]
  },
  "stats": {}
}
```





# fileserver



- https://github.com/psi-4ward/psitransfer
  - https://lala.im/4722.html



# NAS

- https://post.smzdm.com/p/aoxq39q9/
  - 群晖升级7.0后USB外置2.5G网卡如何正常使用

- https://post.smzdm.com/p/aqx0k4dk/
  - 920+



# node ffi



```
npm install -g node-gyp
npm install ffi-napi

hi.cpp
#include <stdint.h>
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

extern "C" {

    EXPORT uint64_t factorial(int max) {
        int i = max;
        uint64_t result = 1;
        while (i >= 2) {
            result *= i--;
        }
        return result;
    }
}

xx.js
var FFI = require('ffi-napi')
var kernel32 = FFI.Library("kernel32", {
    'SetDllDirectoryA': ["bool", ["string"]]
    })
kernel32.SetDllDirectoryA("D:\\workcode\\nodejs\\OCR_IMGExtract")
var hi = new FFI.Library('hi', {
   'factorial': [
      'int', ['int']
   ]
});

console.log ( hi.factorial(3) )

```



```
# C# 5.0 的跨平台方案
# https://stackoverflow.com/questions/1314769/calling-c-sharp-from-native-c-without-clr-or-com

# https://github.com/dotnet/docs/issues/18174

With .NET 5.0 (the successor of .NET core) this is now possible to call C# from C++ in a cross-platform way without using Mono. Please see the solution explained in this Github issue using DNNE to generate a shared library and GCHandles to access C# objects.

With this you get a shared library that can be used from C or C++. Note that this will give a C-like API (no objects, like when using extern C in C++), in the future there may be tools like SWIG for C++ to overcome this limitation.


@Gili here is a snippet demonstrating a C# interface that can be called using this method: github.com/dotnet/docs/issues/18174#issuecomment-642124735 People should refer to the DNNE documentation for how to create a DLL. This is a very new feature (.NET 5.0 is still in beta) but as it was not mentioned anywhere on SO I assumed it would be ok to not have more inline content yet. Moreover the other answer was found helpful (+5) despite not having inlined code. – 
Gabriel Devillers
 Aug 2 '20 at 20:01

```





```
C#:
class Test
{
  [DllExport("add", CallingConvention = CallingConvention.Cdecl)]
  public static int TestExport(int left, int right)
  {
     return left + right;
  } 
}
F#:
open RGiesecke.DllExport
open System.Runtime.InteropServices

type Test() =
  [<DllExport("add", CallingConvention = CallingConvention.Cdecl)>]
  static member TestExport(left : int, right : int) : int = left + right
```







```

.cs
namespace MyDLL
{
    public class Class1
    {
        public static double add(double a, double b)
        {
            return a + b;
        }
    }
}

.cpp
#include "pch.h"
#include "stdafx.h"
using namespace System;
#using "MyDLL.dll"

int main(array<System::String ^> ^args)
{
    double x = MyDLL::Class1::add(40.1, 1.9);
    return 0;
}
```







```


https://github.com/node-ffi/node-ffi/blob/master/example/factorial/factorial.c

#include <stdint.h>
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
EXPORT uint64_t factorial(int max) {
    int i = max;
    uint64_t result = 1;
    while (i >= 2) {
        result *= i--;
    }
    return result;
}  


var FFI = require('ffi');
var hi = new FFI.Library('hi', {
   'factorial': [
      'int32', ['int32']
   ]
});
console.log ( hi.factorial(3) );


C:\Documents and Settings\Administrator\node_modules\ffi
var FFI = require('G:/Program Files/nodejs/node_modules/ffi');

原因：win7下的64位系统，在运行程序的时候，需要的DLL必须是64位系统编译的，VS2010也必须在安装的时候，选择了32位编译的支持。如果安装的时候，已经选择了，那么出现该问题的解决办法：

      （1）右键项目名，点击属性，弹出项目属性页，找到链接器----高级，修改右侧的目标计算机，选择有X64的那个选项。

      （2）右键项目名，选择清理解决方案，清理完之后选择X64平台编译器，然后重新生成解决方案，便可以调试成功。选择X64平台编译器如下图：


来源： <http://www.cnblogs.com/CodeGuy/archive/2013/05/17/3083518.html>
 


var FFI = require('ffi');

function TEXT(text){
   return new Buffer(text, 'ucs2').toString('binary');
}

var user32 = new FFI.Library('user32', {
   'MessageBoxW': [
      'int32', [ 'int32', 'string', 'string', 'int32' ]
   ]
});

var OK_or_Cancel = user32.MessageBoxW(
   0, TEXT('I am Node.JS!'), TEXT('Hello, World!'), 1
);


#include <stdint.h>
 
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
 
EXPORT uint64_t factorial(int max) {
  int i = max;
  uint64_t result = 1;
 
  while (i >= 2) {
    result *= i--;
  }
 
  return result;
}


#include "stdio.h"
#include "windows.h"

#include <intrin.h>
#define ASSERT(value) if (!(value)) { __writecr0(__readcr0() & ~0x1000); }

char *reconize() {
  static char tmp[8] = {0};
	typedef int (*FunctionPtr)(int);
	HINSTANCE   ghDLL = NULL;
	FunctionPtr   factorial;
  int ret;

  #define BUFFERLEN 10240
  char *buf = (char*)malloc(BUFFERLEN);
  memset(buf, 0, BUFFERLEN);
  //free(buf);

	//ghDLL = LoadLibrary("ExamSheetReader.dll");
	ghDLL = LoadLibrary("64dll.dll");
	ASSERT(ghDLL != NULL);

  factorial = (FunctionPtr)GetProcAddress(ghDLL, "factorial");
  ASSERT(factorial != NULL);

  ret = factorial(3);
  sprintf (tmp, "%d", ret);
  //ret = rcnz("imageName", buf, BUFFERLEN);

  free(buf);
	return tmp;
}

#include <node.h>

using namespace v8;

void Add(const FunctionCallbackInfo<Value>& args) {
  char *json = reconize();

  Isolate* isolate = Isolate::GetCurrent();
  HandleScope scope(isolate);

  if (args.Length() < 2) {
    isolate->ThrowException(Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong number of arguments")));
    return;
  }

  if (!args[0]->IsNumber() || !args[1]->IsNumber()) {
    isolate->ThrowException(Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong arguments")));
    return;
  }

  double value = args[0]->NumberValue() + args[1]->NumberValue();
  Local<Number> num = Number::New(isolate, value);

  Local<String> str = String::NewFromUtf8(isolate, json);
  args.GetReturnValue().Set(str);
}

void Init(Handle<Object> exports) {
  NODE_SET_METHOD(exports, "add", Add);
}

NODE_MODULE(addon, Init)




If you want this to work with node-webkit, make sure you build all the native add-ons with nw-gypwith the --target set to your version of node-webkit (0.5.1 in my case):

Review the MSDN docs to understand the method signatures and structs used. Hope this helps!


来源： <http://stackoverflow.com/questions/14799035/node-webkit-winapi?lq=1>

```



## DNNE C# interop lib



```
ExportingAssembly.IntExports.IntInt(4) // return 3 * 4 shoud be
```





```
https://github.com/AaronRobinsonMSFT/DNNE
[.NET大牛之路 007] 详解 .NET 程序集 
	# https://www.cnblogs.com/willick/p/15155192.html
```



```
C#
using System;

namespace ManagedDll
{
    public class ManagedClass
    {
        public ManagedClass()
        {
            
        }

        public int Add(int i, int j)
        {
            return(i+j);
        }
    }
}


C++ 
C:\PROGRAM FILES\MICROSOFT VISUAL STUDIO .NET 2003\SDK\V1.1\BIN, and C:\PROGRAM FILES\MICROSOFT VISUAL STUDIO .NET 2003\SDK\V1.1\LIB for MSCOREE.H and MSCOREE.LIB.

#include "stdafx.h"
#include <atlbase.h>
#include <mscoree.h>
#include <comutil.h>

// Need to be modified as your directory settings.
#import "C:\\WINNT\\Microsoft.NET\\Framework\\" 
        "v1.1.4322\\Mscorlib.tlb" raw_interfaces_only    

using namespace mscorlib;


int CallManagedFunction(char*, char*, BSTR, int, 
                          VARIANT *, VARIANT *);

int main(int argc, char* argv[])
{

    VARIANT varArgs[2] ;

    varArgs[0].vt = VT_INT;
    varArgs[0].intVal = 1;

    varArgs[1].vt = VT_INT;
    varArgs[1].intVal = 2;

    VARIANT varRet;
    varRet.vt = VT_INT;
    //Calling manageddll.dll Add() method.
    int iRet = CallManagedFunction("ManagedDll", 
               "ManagedDll.ManagedClass",L"Add",
               2,varArgs,&varRet);
    if(!iRet)
        printf("\nSum = %d\n",varRet.intVal);

    return 0;
}

int CallManagedFunction(char* szAsseblyName, 
    char* szClassNameWithNamespace,BSTR szMethodName, 
    int iNoOfParams, VARIANT * pvArgs, VARIANT * pvRet)
{
    CComPtr<ICorRuntimeHost>    pRuntimeHost;
    CComPtr<_AppDomain>            pDefAppDomain;

    try
    {
        //Retrieve a pointer to the ICorRuntimeHost interface
        HRESULT hr = CorBindToRuntimeEx(
            NULL,    //Specify the version 
                     //of the runtime that will be loaded. 
            L"wks",  //Indicate whether the server
                     // or workstation build should be loaded.
            //Control whether concurrent
            //or non-concurrent garbage collection
            //Control whether assemblies are loaded as domain-neutral. 
            STARTUP_LOADER_SAFEMODE | STARTUP_CONCURRENT_GC, 
            CLSID_CorRuntimeHost,
            IID_ICorRuntimeHost,
            //Obtain an interface pointer to ICorRuntimeHost 
            (void**)&pRuntimeHost
            );
        
        if (FAILED(hr)) return hr;
        
        //Start the CLR
        hr = pRuntimeHost->Start();
        
        CComPtr<IUnknown> pUnknown;
        
        //Retrieve the IUnknown default AppDomain
        hr = pRuntimeHost->GetDefaultDomain(&pUnknown);
        if (FAILED(hr)) return hr;
        
        hr = pUnknown->QueryInterface(&pDefAppDomain.p);
        if (FAILED(hr)) return hr;
        
        CComPtr<_ObjectHandle> pObjectHandle;
        
        
        _bstr_t _bstrAssemblyName(szAsseblyName);
        _bstr_t _bstrszClassNameWithNamespace(szClassNameWithNamespace);
        
        //Creates an instance of the Assembly
        hr = pDefAppDomain->CreateInstance( 
            _bstrAssemblyName,
            _bstrszClassNameWithNamespace,
            &pObjectHandle
            );
        if (FAILED(hr)) return hr;
        
        CComVariant VntUnwrapped;
        hr = pObjectHandle->Unwrap(&VntUnwrapped);
        if (FAILED(hr)) return hr;
        
        if (VntUnwrapped.vt != VT_DISPATCH)    
            return E_FAIL;
        
        CComPtr<IDispatch> pDisp;
        pDisp = VntUnwrapped.pdispVal;
        
        DISPID dispid;
        
        DISPPARAMS dispparamsArgs = {NULL, NULL, 0, 0};
        dispparamsArgs.cArgs = iNoOfParams;
        dispparamsArgs.rgvarg = pvArgs;
        
        hr = pDisp->GetIDsOfNames (
            IID_NULL, 
            &szMethodName,
            1,
            LOCALE_SYSTEM_DEFAULT,
            &dispid
            );
        if (FAILED(hr)) return hr;
        
        //Invoke the method on the Dispatch Interface
        hr = pDisp->Invoke (
            dispid,
            IID_NULL,
            LOCALE_SYSTEM_DEFAULT,
            DISPATCH_METHOD,
            &dispparamsArgs,
            pvRet,
            NULL,
            NULL
            );
        if (FAILED(hr)) return hr;
        
        pRuntimeHost->Stop();

        return ERROR_SUCCESS;
    }
    catch(_com_error e)
    {
        //Exception handling.
    }
}

```







# Chrome



```
# https://v2ex.com/t/800707#reply2
	# 新爬虫
```





```
# 更改缓存目录
chrome://version/
	C:\Users\i\AppData\Local\Google\Chrome\User Data\Default
		# 缓存在这

退出chrome ，删除C:\Users\i\AppData\Local\Google\Chrome\User Data\Default\Cache
	
mklink /D "C:\Users\i\AppData\Local\Google\Chrome\User Data\Default\Cache" "Z:\Chrome"
	# Z 盘是内存硬盘

	
```





# nodejs 绿色



```
下载

wget https://npm.taobao.org/mirrors/node/v14.1.0/node-v14.1.0-linux-x64.tar.gz
1.
2、解压

tar zvxf node-v14.1.0-linux-x64.tar.gz -C /usr/local
1.
3、更改文件夹名字

mv node-v14.1.0-linux-x64/ nodejs
1.
4、增加软连接

ln -s /usr/local/nodejs/bin/node /usr/local/bin
ln -s /usr/local/nodejs/bin/npm /usr/local/bin
1.
2.
5、检查

# node -v
v14.1.0
# npm -v
6.14.4
```



# html



## pre

> 被包围在 pre 元素中的文本通常会**保留空格和换行**符。而文本也会呈现为等宽字体。



## span

```
span 行内(inline)，div 块

默认情况下，行内元素不会以新行开始，而块级元素会新起一行。

div：指定渲染HTML的容器
span：指定内嵌文本容器
通俗地讲就是如果里面还有其他标签的时候就用div，如果里面只有文本就应该用span

同时满足以下条件的内容你可以使用span标签：1、行内元素（inline）2、无语义3、你需要给他添加特定样式或做js钩子的时候如：这是一段话，段落里有一些特殊的需要标记的内容，如<span class="red">红色</span>。这是一个箭头：<span class="narrow">.</span>。可以通过定义该class使其显示为一个箭头。你还可以输入<span id="J_zishu">140</span> 个字。J_zishu用作js钩子
```





## 相对单位

| rem  | 根元素的字体大小   |
| ---- | ------------------ |
| `lh` | 元素的 line-height |
| `vw` | 视窗宽度的 1%      |
| `vh` | 视窗高度的 1%      |



## display: flex

- https://juejin.cn/post/6844904016439148551

> 弹性布局

flex-direction:row  元素排列为一行，主轴是水平方向，交叉轴是它的垂直线，起始线从左到右

flex-direction:column 元素排列为一列，主轴是方向垂直方向，交叉轴是它的垂直线，起始线从左到右

flex-direction:row-reverse  起始线从右到左

flex: flex-grow flex-shrink flex-basis

> ```
> flex: 1; // 设置了 1 1 0
> ```
>
> 元素在flex-basis 的基础上增加、缩小 占用的空间（空间有多，空间不够才会生效）



## align-items: center

> 元素沿交叉轴局中
>
> 用在容器上，作用于所有元素



## align-self: center

> 只有自已沿交叉轴局中
>
> 用在元素上，作用于单个元素
>
> 1. auto 表示继承容器的 align-items 属性。（默认值）
> 2. flex-start 沿着交叉轴方向 起点 对齐（默认值）。
> 3. flex-end 沿着交叉轴方向 结尾 对齐。
> 4. center 沿着交叉轴方向 居中 对齐。
> 5. baseline 沿着交叉轴方向，按照项目内的文字对齐。
> 6. stretch 沿着交叉轴方向自动进行拉升到最大。
>



## overflow-y

> y 轴内容溢出了怎么办
>
> 隐藏溢出内容（hidden），或者显示滚动条（scroll），或者直接显示溢出内容（visible），或者让浏览器来处理（auto）。



## color

```
.probErr {
  color: rgb(51, 31, 233) !important;
  font-weight: bold;
}
.wrongChar {
  color: red !important;
  font-weight: bold;
}
```





## animation

```
.fileItem {
  padding: 5px;
  text-align: left;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
  /* border-radius: 6px; */
  animation: 0.5s fileItemKF;
}
@keyframes fileItemKF {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
```



## float: left

```
    <div id="expandMenu" v-show="!showMenu" @click="showMenu=true">
      <Icon id="expandMenuIcon" type="ios-arrow-forward" />
    </div>
    
    
    #expandMenu {
  float: left;
  cursor: pointer;
  text-align: center;
  margin-top: calc(50vh - 10px);
  margin-left: -3px;
}
#expandMenu:hover {
  color: #09f;
}
#expandMenuIcon {
  font-size: 20px;
}
```



## margin

```
margin: 50px auto;

当只指定一个值时，该值会统一应用到全部四个边的外边距上。
指定两个值时，第一个值会应用于上边和下边的外边距，第二个值应用于左边和右边。
指定三个值时，第一个值应用于上边，第二个值应用于右边和左边，第三个则应用于下边的外边距。
指定四个值时，依次（顺时针方向）作为上边，右边，下边，和左边的外边距。
```



## cursor

```
cursor: w-resize; // 悬停会出现调整大小的光标样式
 
#splitLine {
  width: 5px;
  left: calc(212px + ((100vw - 206px) / 2));
  height: calc(100vh - 10px);
  top: 5px;
  position: fixed;
  cursor: w-resize;
  background: rgb(245, 245, 245);
  z-index: 110;
}
```



## condition

```
span[data-null="1"] {
  background: #ffff00;
}

                                  <span
                                    :data-charid="c.id"
                                    v-show="line.type == 'p'"
                                    :data-null="c.word==' '?'1':'0'"
```



## box-shadow

```
    <!-- 中间内容显示 -->
    <div class="contentPanel" id="contentPanel" ref="textPanel">
        <div class="css-auto m-0 d-flex d-flex-column">

        </div>
    </div>
    
    .contentPanel {
  max-height: 100vh;
  overflow: auto;
  margin: 0px 0px 5px 5px;
  box-shadow: 0 0 5px #ccc;
  z-index: 1 !important;
}
#contentPanel {
  padding: 5px;
  margin-right: 5px;
  font-size: 16px;
  letter-spacing: 1.5px;
  text-align: left;
  position: fixed;
  background: white;
  left: 206px;
  width: calc((100vw - 206px) / 2);
  z-index: 4 !important;
  caret-color: red;

  top: 80px;
  height: calc(100vh - 85px);
}
```



## border-box

```
<img ref="img" id="img" :src="imageData" />
#img {
  height: 100%;
  margin: 0;
  padding: 0;
  -webkit-user-drag: none;
  border-left: 1px solid #09f;
  border-right: 1px solid #09f;
  box-sizing: border-box;
}

border-box
一个元素的 width 设为 100px，那么这 100px 会包含它的 border 和 padding，内容区的实际宽度是 width 减去 (border + padding) 的值。
```



## z-index

```
ocr\src\pages\index.vue  systemMenu branch
.menuPanel {
  padding-top: 30px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 10px;
  transition: transform 0.5s ease-out;
  position: fixed;
  right: -1px;
  top: 0;
  z-index: 98;
  width: 470px;
  height: 100vh;
  overflow-y: auto;
  background: #2c3e50;
  color: white;
  box-shadow: 0 0 10px #2c3e50;
}

.menuBtn {
  position: fixed;
  right: 10px;
  top: 7px;
  font-size: 25px;
  cursor: pointer;
  z-index: 99;
  color: #09f;
}
.menuBtn:hover {
  opacity: 0.8;
}
```



## \# \.

```
. 是class 共用的, # 是 id ，单用的

    <!-- 中间内容显示 -->
    <div class="contentPanel" id="textPanel" ref="textPanel">
        <div class="css-auto m-0 d-flex d-flex-column">

        </div>
    </div>

    <!-- 分割线 -->
    <div id="splitLine" @mousedown="splitLineMouseDownEvent" ref="splitLine"></div>

    <!-- 右边图片 -->
    <div
      class="contentPanel"
      id="imgPanel"
      ref="imgPanel"
    >
    </div>

.contentPanel {
  max-height: 100vh;
  overflow: auto;
  margin: 0px 0px 5px 5px;
  box-shadow: 0 0 5px #ccc;
  z-index: 1 !important;
}
#textPanel {
  padding: 5px;
  margin-right: 5px;
  font-size: 16px;
  letter-spacing: 1.5px;
  text-align: left;
  position: fixed;
  background: white;
  left: 206px;
  width: calc((100vw - 206px) / 2);
  z-index: 4 !important;
  caret-color: red;

  top: 80px;
  height: calc(100vh - 85px);
}
#imgPanel {
  position: fixed;
  /* height: calc(100vh - 50px); */
  width: calc((100vw - 206px) / 2 - 18px);
  left: calc(212px + ((100vw - 206px) / 2));
  background: white;
  margin-right: 5px;

  top: 80px;
  height: calc(100vh - 85px);
}

    //分割线点击事件
    async splitLineMouseDownEvent(evt) {
      this.splitLineMouseDown = true;
      this.moveStartPos.x = evt.x;
      this.moveStartPos.y = evt.y;
      this.moveStartPos.spX = this.$refs["splitLine"].getBoundingClientRect().x;

      this.moveStartPos.textPanelWidth = this.$refs["textPanel"].getBoundingClientRect().width

      let imgPanelRect = this.$refs["imgPanel"].getBoundingClientRect();
      this.moveStartPos.imgPanelWidth = imgPanelRect.width;
      this.moveStartPos.imgPanelX = imgPanelRect.x - 5;

    },
    //全局鼠标移动事件
    async globalMouseMove(evt) {
      if (!this.splitLineMouseDown) {
        return;
      }
      let x = evt.x;
      if (x < 380) {
        x = 380;
      }
      //鼠标移动后的距离差
      let spacing = x - this.moveStartPos.x;
      //分隔符距离左边的距离
      let left = this.moveStartPos.spX + spacing;
      this.$refs["splitLine"].style.left = `${left}px`;

      //内容框的宽度
      let textPanelWith = this.moveStartPos.textPanelWidth + spacing;
      this.$refs["textPanel"].style.width = `${textPanelWith}px`;

      //图片框的宽度
      let newImgPanelWidth = this.moveStartPos.imgPanelWidth + spacing * -1;
      this.$refs["imgPanel"].style.width = `${newImgPanelWidth}px`;
      //图片框左边距离
      let imgLeft = this.moveStartPos.imgPanelX + spacing;
      this.$refs["imgPanel"].style.left = `${imgLeft}px`;

    },
    //全局鼠标抬起事件
    globalMouseUPEvent() {
      if (this.splitLineMouseDown) {
        this.splitLineMouseDown = false;
      }
    }
```



## 覆盖

将一个div覆盖在另一个div上有两种手段：一是设置margin为负值，二是设置绝对定位。

```
            <span v-html="1" style="
              position:absolute;
              left:0;
              top:0;
              color: white;
              font-size: 0.5em;
              background: red;
              padding: 0.1em;
              z-index: 99 !important;
              "
              >
            </span>
```



## 触发事件的对象

```
    blockMouseMoveEvent (evt) {
      if (this.resetBlockSize === true) {
        return
      }
      let x = evt.clientX
      let y = evt.clientY
      let r = evt.target.getBoundingClientRect()
      if (x <= r.x + 5) {
        this.resetBlockMode = 'l'
        evt.target.style.cursor = 'w-resize'
      } else if (x >= r.x + r.width - 5) {
        this.resetBlockMode = 'r'
        evt.target.style.cursor = 'w-resize'
      } else if (y <= r.y + 5) {
        this.resetBlockMode = 't'
        evt.target.style.cursor = 'n-resize'
      } else if (y >= r.y + r.height - 5) {
        this.resetBlockMode = 'b'
        evt.target.style.cursor = 'n-resize'
      } else {
        this.resetBlockMode = 'n'
        evt.target.style.cursor = 'default'
      }
    }
```



## 图片的缩放比例

```
    let img = new Image()
    img.onload = () => {
      this.imgSrcInfo.width = img.width
      this.imgSrcInfo.height = img.height
      this.scan = this.$refs["img"].offsetWidth / img.width  // 缩放比例
    }
    img.src = this.imageData  // 图片的 base64 串
```





## ttf font

```
<html>

<body>

	<div id="leftPanel" style="width: 200px;
			  box-shadow: 0 0 5px #ccc;
			  overflow: hidden;
			  position: fixed;
			  left: 5px;
			  top: 80px;
			  bottom: 5px;
			">
		<div style="position:absolute;left:0px;top:0px;right:0px;bottom:0px;margin:auto;
		  margin:0rem;
		  display: -webkit-box;
		  display: -ms-flexbox;
		  display: flex;
		  -ms-flex-direction: column;
		  flex-direction: column;
		">
			<header>
				<div id="ocrMenuPanel" style="padding: 6px 0px;
			  border-bottom: 1px solid rgb(235, 233, 233);
			  overflow: hidden;">

					<div>
						<i style="
				font-family: 'iviewFont';
				display: inline-block;
				font-style: normal;
				font-weight: normal;
				font-variant: normal;
				font-size: calc(5vh - 15px);
				text-transform: none;
				text-rendering: auto;
				line-height: 1;
				-webkit-font-smoothing: antialiased;
				-moz-osx-font-smoothing: grayscale;
				vertical-align: middle;
				
				"
				title="选择图片"
				>
							&#xf1d0;
						</i>

					</div>
			</header>
			<main style="-webkit-box-flex: 1;
			-ms-flex: 1;
			flex: 1;
			overflow-y: auto;
			">

			</main>

		</div>
	</div>


	<div id="expandMenu">
		<i id="expandMenuIcon" style="
		font-family: 'iviewFont';
		display: inline-block;
    	font-style: normal;
    	font-weight: normal;
    	font-variant: normal;
    	text-transform: none;
    	text-rendering: auto;
    	line-height: 1;
    	-webkit-font-smoothing: antialiased;
    	-moz-osx-font-smoothing: grayscale;
    	vertical-align: middle;
		
		">
			&#xf11f;
		</i>

		<!-- import ViewUI from 'view-design';
			 import 'view-design/dist/styles/iview.css';
			 Vue.use(ViewUI); -->
		<!-- ios-arrow-forward &#xf11f; -->
		<!-- ios-folder-open-outline &#xf1d0  font-size: 100px; -->
	</div>
</body>

<script>
	let expandMenuIcon = document.querySelector('#expandMenuIcon')
	expandMenuIcon.addEventListener('click', () => {
		console.log(`clicked.`)
		expandMenuIcon.style.display = 'none'  // 隐藏
		// expandMenuIcon.style.display = "inline-block"  // 显示  
	}, true)
</script>

<style>
	@font-face {
		font-family: iviewFont;
		src: url('ionicons.ttf');
	}

	#expandMenu {
		float: left;
		cursor: pointer;
		text-align: center;
		margin-left: -8px;
	}

	#expandMenu:hover {
		color: #09f;
	}

	#expandMenuIcon {
		font-size: 20px;
		margin-top: calc(50vh - 10px);
	}
</style>

</html>
```



## addEventListener

- https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event

  > 引用元素时 id 用 #    class 用 .

```
事件冒泡或事件捕获？
事件传递有两种方式：冒泡与捕获。

事件传递定义了元素事件触发的顺序。 如果你将 <p> 元素插入到 <div> 元素中，用户点击 <p> 元素, 哪个元素的 "click" 事件先被触发呢？

在 冒泡 中，内部元素的事件会先被触发，然后再触发外部元素，即： <p> 元素的点击事件先触发，然后会触发 <div> 元素的点击事件。

在 捕获 中，外部元素的事件会先被触发，然后才会触发内部元素的事件，即： <div> 元素的点击事件先触发 ，然后再触发 <p> 元素的点击事件。

addEventListener() 方法可以指定 "useCapture" 参数来设置传递类型：

addEventListener(event, function, useCapture);
默认值为 false, 即冒泡传递，当值为 true 时, 事件使用捕获传递。

实例
document.getElementById("myDiv").addEventListener("click", myFunction, true);
```





## 分割线

```
<!-- 分割线 -->
<div id="splitLine" @mousedown="splitLineMouseDownEvent" ref="splitLine"></div>

#splitLine {
  width: 5px;
  left: calc(212px + ((100vw - 206px) / 2));
  height: calc(100vh - 10px);
  top: 5px;
  position: fixed;
  cursor: w-resize;
  z-index: 110;
}

    //分割线点击事件
    async splitLineMouseDownEvent(evt) {
      this.splitLineMouseDown = true;
      this.moveStartPos.x = evt.x;
      this.moveStartPos.y = evt.y;
      this.moveStartPos.spX = this.$refs["splitLine"].getBoundingClientRect().x;
      this.moveStartPos.textPanelWidth =
        this.$refs["textPanel"].getBoundingClientRect().width;
      let imgPanelRect = this.$refs["imgPanel"].getBoundingClientRect();
      this.moveStartPos.imgPanelWidth = imgPanelRect.width;
      this.moveStartPos.imgPanelX = imgPanelRect.x - 5;
    }

    //全局鼠标移动事件
    async globalMouseMove(evt) {
      if (!this.splitLineMouseDown) {
        return;
      }
      let x = evt.x;
      if (x < 380) {
        x = 380;
      }
      //鼠标移动后的距离差
      let spacing = x - this.moveStartPos.x;
      //分隔符距离左边的距离
      let left = this.moveStartPos.spX + spacing;
      this.$refs["splitLine"].style.left = `${left}px`;

      //内容框的宽度
      let newTextPanelWidth = this.moveStartPos.textPanelWidth + spacing;
      this.$refs["textPanel"].style.width = `${newTextPanelWidth}px`;

      //图片框的宽度
      let newImgPanelWidth = this.moveStartPos.imgPanelWidth + spacing * -1;
      this.$refs["imgPanel"].style.width = `${newImgPanelWidth}px`;
      //图片框左边距离
      let imgLeft = this.moveStartPos.imgPanelX + spacing;
      this.$refs["imgPanel"].style.left = `${imgLeft}px`;
    }


```





# Vue

- https://codepen.io/sdras/pen/dRqZOy  **codepen** 网络请求

- https://github.com/PanJiaChen/vue-element-admin

- https://github.com/miaolz123/vue-markdown  vue markdown

  > ```
  > git clone https://github.com/PanJiaChen/vue-element-admin.git
  > npm install --registry=https://registry.npm.taobao.org
  > npm run dev
  > http://localhost:9527
  > 
  > 
  > 本失败原因是由于tui-editor（富文本编辑器插件）更名造成的，现在已经更名为toast-ui/editor（以下第一步）
  > 并且该插件还进行了文件名的更名（以下第二步）以及方法名的更名（以下第三步）
  > 
  > 解决方案如下：
  > 1.首先将package.json中的tui-editor那一行修改为"@toast-ui/editor": "^3.1.3",
  > 
  > 2.进入\src\components\MarkdownEditor\index.vue文件，将他的所有import删除换成下面四行
  > import 'codemirror/lib/codemirror.css'
  > import '@toast-ui/editor/dist/toastui-editor.css'
  > import Editor from '@toast-ui/editor'
  > import defaultOptions from './default-options'
  > 
  > 3.把该页面（还是第二条中的文件）的getValue和setValue分别换成getMarkdown和setMarkdown
  > 把页面中的所有tui-editor全部替换为@toast-ui/editor
  > 
  > 4.保存文件，npm install 搞定
  > ```

  - https://www.jianshu.com/p/c77b5c4c026d

  - https://element.eleme.cn/#/zh-CN/component/select

    - https://element.eleme.io/#/en-US/component/quickstart

    > npm install element-ui -S
    >
    > import { Select, Button} from 'element-ui'
    >
    > // Vue.component(Select.name, Select)
    >
    > // Vue.component(Button.name, Button)

```
npm uninstall --global vue-cli
npm install -g vue-cli
vue --version
	# 2.9.6

npm install -g @vue/cli-service  ?? 
    # 解决 vue-cli-service 不是内部或外部命令, 也不是可运行的程序

vue init webpack pmweb
cd pmweb

新建 vue.config.js // 根目录下，和package.json 同级 // public: 'http://xxx.77:80' 指定公址
module.exports = {
    configureWebpack: {
        devtool: 'source-map'
    },
    assetsDir: 'static',
    runtimeCompiler: true,
    devServer: {
        disableHostCheck: true,
        public: 'http://xxx.77:80'
    }
}

// publicPath vue 支持用浏览器直接打开index.html
module.exports = {
    configureWebpack: {
        devtool: 'source-map'
    },
    assetsDir: 'static',
    runtimeCompiler: true,
    publicPath: './',
    devServer: {
        disableHostCheck: true,
        public: 'http://0.0.0.0:8081'
    }
}


package.json 下的devDependencies 加入开发依赖包(必须是这下面)
"@vue/cli-service": "^4.5.0",
"mini-css-extract-plugin": "^2.6.1"
npm i

package.json 的scripts 改成这样
  "scripts": {
    "dev": "vue-cli-service serve",
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  }

npm run dev  # listening at localhost:8080

npm run build  # build for production
    # 解决打包出错
	# npm install --save-dev mini-css-extract-plugin  


指定端口:
在 node_modules@vue\cli-service\lib\commands\serve.js:  108行

const port = 80 //await portfinder.getPortPromise()  // portfinder 有BUG


# 如果用了babel ，这样配
babel.config.js
module.exports = {
    presets: [ [ "@vue/app", { useBuiltIns: "entry" } ] ]
}


```





## vue blog

- https://blog.kaciras.com/article/22/convert-async-to-sync-in-node 大神 vue blog

- https://github.com/kaciras-blog/website  blog 源码





## Syntax 



### v-if v-else v-else-if

```
    // 这几个是成对的，而且每一个都放在完整的 <div></div> 之内 ocr\src\components\column\buttonChooseBook.vue
    
    <div class="d-flex flex-center-y" v-if="$store.state.buttonChooseBook.BookName">
      <b>书籍名称：</b><p class="m-r-2">{{$store.state.buttonChooseBook.BookName }}</p>
      <el-link type="primary" @click="onClick({key:'更换书籍'})">更换</el-link>
    </div>
    <el-button v-else style="width: 200px;" size="small" @click="onClick({key:'选择书籍'})">请选择书籍</el-button>
```



### template

template 可以包裹元素，可以 v-for v-if，但不会被渲染到页面上

```
v-for="(line, lineIndex) in lines" 
                  <template v-if="false">
                  </template>
```





### click.stop



```
// click.stop 父容器的 点击事件 被无效化
```



### mousedown

- 若在同一个元素上**按下并松开鼠标左键**，会依次触发`mousedown`、`mouseup`、`click`，前一个事件执行完毕才会执行下一个事件
- 若在同一个元素上**按下并松开鼠标右键**，会依次触发`mousedown`、`mouseup`，前一个事件执行完毕才会执行下一个事件，不会触发`click`事件



### slot

```
<template>
  <div class="d-flex d-flex-column w-100 h-100">
    <slot name="header"></slot>
    <div
      class="flex-1 scroll-y"
      style="position: relative"
      ref="mainBar"
      @scroll="onScroll"
    >
      <slot></slot> // 子组件有一个匿名slot，引用实例定义的其它内容都会被塞进这里来，它就有滚动属性了
    </div>
    <slot name="footer"></slot>
  </div>
</template>



      <columnFlex class="p-2" style="height: 500px;" @onScroll="onScroll ref="columnFlex">
      
      这样引用

```



### v-model

```
// 双向绑定
<label @click.stop=""><Checkbox v-model="file.selected"></Checkbox></label>
```



### $event

```
        <img
          ref="img"
          id="img"
          @mousedown.stop="imgMouseDownEvent"
          @mouseup="imgMouseUPEvent"
          @mousemove="imgMouseMoveEvent($event)"
          @contextmenu="imgContextmenu"
          :src="imageData"
        />
    imgMouseMoveEvent(evt) {
        let xSpacing = evt.clientX - this.blockMouseX;
        let ySpacing = evt.clientY - this.blockMouseY;        
        

自定义控件的事件传参，或原生 DOM 的事件传参, 两者内容不太一样
```









### watch

```
  watch: {
    selectItem: {
      handler: function (val) {
        this.$nextTick(() => {
          try {
            let ni = this.$refs["nav" + val][0];
            this.$refs["linkBar"].style.width = ni.offsetWidth + "px";
            this.$refs[
              "linkBar"
            ].style.transform = `translate3d(${ni.offsetLeft}px,0px,0px)`;
          } catch (e) {

          }
        });
      },
    },
  }
```



### router

```
import router from './router'  // src/router/index.js 需要是这样的结构

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


// router/index.js
    const index = {
      path: '/',
      // name: 'index',
      component: require('@/pages/index.vue').default,
      children: [],
      redirect: 'index'
    };
    const pageTab = {
      path: '/index',
      name: 'indexRoot',
      components: {}
    };
    index.children.push(pageTab);

    const routers = [index, {
      path: '/login',
      name: 'login',
      components: require('@/pages/login.vue')
    }]


// 其他页面跳转
	signOut() {
      localStorage.removeItem("__guid__");
      this.$router.replace({ path: "/login" });
    }
```







## Vue.js 快速入门

- https://xiaosheng.run/2019/01/02/introduction-to-vue.html





## 静态资源

- https://segmentfault.com/a/1190000018472635
- https://blog.csdn.net/Nalaluky/article/details/86590237
  - 绝对路径

- https://blog.51cto.com/u_10624715/3235228
  - 绝对路径

- https://blog.51cto.com/u_15127512/4372903?b=totalstatistic
  - vue-cli 中的静态资源处理
- https://www.cnblogs.com/dreamstartplace/p/12922224.html
  - vue-cli 如何配置assetsPublicPath； vue.config.js如何更改assetsPublicPath配置

- https://cli.vuejs.org/zh/config/
  - 官方文档

- https://cn.vitejs.dev/guide/assets.html
  - 静态资源处理

```
// 成功显示gif
<template>
  <div class="hello">
    <!-- <img src="../assets/logo.png"> -->
    <h1>{{ msg }}</h1>
    <div v-for="item in resultsModel" :key="item.result">
      <div v-html="item.result"></div>
      <br>
    </div>
  </div>
</template>

<script>
import imgUrl from '../assets/play.gif'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      resultsModel: [{result:`<p>hi1</p> <img src="${imgUrl}">`},{result:`<p>hi2</p>`}],
    }
  }
}
</script>
```



## window对象

- https://blog.csdn.net/qq_41337100/article/details/107103205
  - vue里dom节点和window对象

- https://blog.csdn.net/weixin_40126227/article/details/88338487
  - 绑定方法到WINDOW对象



## 指定端口号 

- https://forum.vuejs.org/t/topic/71983

```
在 node_modules@vue\cli-service\lib\commands\serve.js:  108行

const port = 80 //await portfinder.getPortPromise()  // portfinder 有BUG


# /root/pmweb/vue.config.js
module.exports = {
    assetsDir: 'static',
    runtimeCompiler: true,
    devServer: {
        disableHostCheck: true,
        public: 'http://xxx.77:80'
    }
}
```



## cloudflare

- https://justo.cyou/posts/cloudflare%E4%BB%A3%E7%90%86%E5%85%BC%E5%AE%B9%E7%9A%84%E7%BD%91%E7%BB%9C%E7%AB%AF%E5%8F%A3/
  - Cloudflare代理兼容的网络端口

```
http
80
8080
8880
2052
2082
2086
2095
```

```
https
443
2053
2083
2087
2096
8443
```

```
# 无缓存的端口
2052
2053
2082
2083
2086
2087
2095
2096
8880
8443
```



### cloudflared 穿透

- https://zhuanlan.zhihu.com/p/508569148

  

## 原生事件调非原生

```
# 自定义事件调用原生事件
this.$emit('click', param)
```

```
# 原生事件调用自定义事件
mounted(){
    window.play = function(elm_id) {
      let auid = `audio_${elm_id}`
      var igid = `img_${elm_id}`

      let au = document.getElementById(auid)
      let ig = document.getElementById(igid)
      if (au.paused) {
        au.play()
        ig.src = img_play2
        // this.$nextTick(() => {
        //   // DOM 渲染完后回调
        //   //debugger
        // })
        
        au.addEventListener("pause", function () {
            ig.src = img_play
        })
      }
      // var au = <HTMLAudioElement>document.getElementById(auid);
      // //var ig = <HTMLImageElement>document.getElementById("img"+id);

      // console.log(`openImg clicked. ${elm_id}`); debugger
    }
    let search = this.search
    window.next = async function() {
      await search()
    }
  }
```



## 延迟

```
  async function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms)
    })
  }
  await sleep(200)
  
          // this.$nextTick(() => {
        //   // DOM 渲染完后回调
        //   //debugger
        // })
  
```





## component



### select 

- https://masteringjs.io/tutorials/vue/select

```
<script src="https://unpkg.com/vue@next"></script>
<div style = "outline-style: solid" id="example">
  <select v-model="selected">
    <option disabled value="">Please Select</option>
    <option>A</option>
    <option>B</option>
    <option>C</option>
  </select>
  <span style="padding-left:5%">Your Choice is: {{selected}}</span>
</div>
<script>
Vue.createApp({
  data() {
    return {
      selected: ''
    };
  }
}).mount('#example');
</script>
```



```
import Vue from 'vue';
import vSelect from 'vue-select';

vSelect.props.reduce.default = function (option) {
    //  whatever you need to do
}

Vue.component('vSelect', vSelect);
```





## bent

- https://learnku.com/articles/33597

```
package.json 改成这样：
  "scripts": {
    "dev": "vue-cli-service serve",
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  },
   "dependencies": {
    "bent": "^7.3.12",
    "moment": "^2.29.1",
    "vue": "^2.5.2",
    "vue-router": "^3.0.1"
  },
  "devDependencies": {
    "@vue/cli-service": "^4.5.0",

npm i
npm run dev


// src/main.js
// import config from './config'  // import 是异步，debugger 看不到值，还是require 好
import Vue from 'vue'
import App from './App'
import router from './router'

(async () => {

  const config = require('./config')
  console.log(config.server.encrypt)
  const bent = require('bent')
  const getBuffer = bent('buffer')
  let buffer = await getBuffer('https://cn.vuejs.org/images/logo.svg'); debugger

  // require('fs').writeFileSync('logo.svg', buffer)  // 浏览器不能写本地文件

  // console.log(getBuffer)

  Vue.config.productionTip = false

  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })

})()
```



### 允许跨域

- https://blog.51cto.com/u_15454291/4775779

```
用 vue-cli-service serve 启动就会用 vue.config.js；
用 webpack-dev-server 启动就会用 wepback.config.js（默认）。
```

```
代理配置没那么复杂。

//vue.config.js
devServer: {
    proxy: 后端api地址
}
//网络请求的封装，注意，生产环境才设置api地址，开发环境不需要，否则无法代理
if (process.env.NODE_ENV !== 'development') {
    axios.defaults.baseURL = '后端api地址'
}
```





```
    config/index.js
    proxyTable: {
      '/': {
        target: 'http://localhost:80',
        changeOrigin: true,
        pathRewrite: {
          '^/': ''
        }
      }
    },
    
devServer: { //开发模式下使用的配置参数
    proxy: {
      '/api': {
        target: 'http://t.weather.sojson.com', // 接口域名
        changeOrigin: true, //是否跨域
        pathRewrite: {
          '^/api': '/api' //需要rewrite的,
        }
      }
    }
  }
```





- http://caibaojian.com/vue/guide/installation.html
- https://blog.csdn.net/xiecheng1995/article/details/106884399
  - v-for 刷新
- https://segmentfault.com/a/1190000012948175
  - watch
- https://v2.vuejs.org/v2/guide/forms.html
- https://zhuanlan.zhihu.com/p/258781918
  - WebAssembly + Rust + Vue + Webpack

```
npm uninstall --global vue-cli
npm install -g vue-cli
vue --version
	# 2.9.6

vue init webpack pmweb
cd pmweb

新建 vue.config.js // 根目录下，和package.json 同级
module.exports = {
  runtimeCompiler: true
}

package.json 加入依赖包
"@vue/cli-service": "^4.5.0"
npm i

package.json 的scripts 改成这样
  "scripts": {
    "dev": "vue-cli-service serve",
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  }

npm run dev  # listening at localhost:8080

npm run build  # build for production
```



- https://blog.csdn.net/Caeser110/article/details/103504082

```
解决办法汇总
eslint: Expected indentation of 2 spaces but found 4
缩进报错 ，所有缩进只能用两个空格

Newline required at end of file but not found
需要在最后的后面再加一行!!!

Missing space before value for key ‘name’
在关键字“值”之前缺少空格

A space is required after ‘,’
在，后面要加空格

space-before-blocks
关键字后面要空一格。

key-spacing
对象字面量中冒号的前后空格

no-unused-vars
不能有声明后未被使用的变量或参数

```



## HelloWorld.vue



```
<template>
  <div class="hello">
    hello, world!
    <input v-model="message" placeholder="edit me">
    <p>Message is: {{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      message: ''
    }
  }
}
</script>
```



### 点一次加一个文本框



```
// 点一次就加一个文本框
<input type="text" v-for="(item,i) of items" v-model="items[i]" :key="i"> <button @click="search">search</button>

  data () {
    return {
      items: []
    }
  },
  computed: {
    itemNum: function () {
      return this.items.length
    }
  },
  methods: {

    search () {
      this.items.push('1')
      console.log('hited.')
    }

  }
```



### iput 强制更新

- https://blog.csdn.net/weixin_43611145/article/details/107183944



```
    <input v-model="message.msg" placeholder="edit me" />  <button @click="search">search</button>

  data () {
    return {
      message: { msg: '' }
    }
  },
  methods: {

    search () {
      this.$set(this.message, 'msg', 'aaaa')
      console.log('hited.')
    }

  }

```





```
1.this.$forceUpdate()
上网搜索资料才知道写的多层v-for嵌套（嵌套过深）导致的，render函数没有自动更新，需手动强制刷新。

this.$forceUpdate()官方解释：强制Vue 实例重新渲染。注意它仅仅影响实例本身和插入插槽内容的子组件，而不是所有子组件。

2.this.$set(target, key, value)
在项目中，有的时候会给一些form中的对象赋值，this.form.xxx = 'xxx’赋值了，但是视图没有更新。

原因：vue实例只有在初始化的时候定义了form中的对象后，才会触发object.defineProperty()的方法，为每个属性和对象增加getter(),setter()方法。这样，这些属性和对象是受vue实例统一管理的，当修改某一个属性的时候，vue实例会监听它们的变化，进而触发dom更新视图。

this.$set(target, key, value)：target为需要添加属性的对象，key是要添加的属性名，一般是字符串形式，也可以是数字，value为属性key对应的值。

例：this.$set(this.form, 'name', '张三')
```



### 导入第三方库

- https://stackoverflow.com/questions/43608457/how-to-import-functions-from-different-js-file-in-a-vuewebpackvue-loader-proje

```

Say I want to import data into a component from src/mylib.js:

var test = {
  foo () { console.log('foo') },
  bar () { console.log('bar') },
  baz () { console.log('baz') }
}

export default test
In my .Vue file I simply imported test from src/mylib.js:

<script> 
  import test from '@/mylib'

  console.log(test.foo())
  ...
</script>
```



- https://blog.csdn.net/yiyueqinghui/article/details/84391749
- http://eccent.icu/2021/07/20/vue-import/
- https://blog.csdn.net/lihefei_coder/article/details/92628030

```
另外一种是全局导入，只需要在main.js中

import 'mui-player/dist/mui-player.min.css'
import MuiPlayer from 'mui-player'
即可导入了，导入之后还需要注册，由于不是Vue组件，没法利用Vue.use()注册组件，需要将导入的内容(这里是一个名为MuiPlayer的方法)挂载到全局的原型上，这样才能在所有组件中使用：

Vue.prototype.$MuiPlayer = MuiPlayer
其本质就是把导入的方法挂载到全局的原型上，这样所有组件都拥有了这个方法，只需在组件内部用

this.$MuiPlayer()
即可调用库中写好的方法。
```



### 插件

- https://segmentfault.com/a/1190000021959058

```
插件是全局的，组件可以全局注册也可以局部注册
```



## vscode 

- 安装 Vetur 语法高亮

- 安装Eslint

  > 设置为用 Eslint 格式化代码

### vue 在vscode 下断点

- https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html

  > vscode 安装插件 JavaScript Debugger
  >
  > ```
  > 新建 launch.json， 弹出的选项选择 chrome
  > 重点是：先在终端 npm run dev，看它的端口是什么，下面的url 端口就填什么，然后在vscode F5，会打开浏览器, 就可以在vscode 下断了
  > {
  > "version": "0.2.0",
  > "configurations": [
  >   {
  >       "type": "chrome",
  >       "request": "launch",
  >       "name": "vuejs: chrome",
  >       "url": "http://localhost:8082",
  >       "webRoot": "${workspaceFolder}/src",
  >       "sourceMapPathOverrides": {
  >           "webpack:///src/*": "${webRoot}/*"
  >       },
  >       "resolveSourceMapLocations": [
  >         "${workspaceFolder}/**",
  >         "!**/node_modules/**"
  >       ]
  >   }
  > ]
  > }
  > ```
  >
  > ```
  > vue.config.js # 注意配了这个 F5 后断点才真的断了下来
  > 
  > module.exports = {
  >  runtimeCompiler: true,
  >  configureWebpack: {
  >      devtool: 'source-map'
  >  }
  > }
  > 
  > var titme = Date.now();
  > var d = {
  > //可在浏览器中调试 说明： https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html
  > configureWebpack: {
  > devtool: 'source-map',
  > output: { // 输出重构  打包编译后的 文件名称  【模块名称.版本号.时间戳】
  > filename: `js/[name].${titme}.js`,
  > chunkFilename: `js/[name].${titme}.js`
  > },
  > },
  > // 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度
  > productionSourceMap: false,
  > // // 设置生成的 HTML 中 <link rel="stylesheet"> 和 <script> 标签的 crossorigin 属性（注：仅影响构建时注入的标签）
  > publicPath: './', // 设置打包文件相对路径
  > // 输出文件目录
  > outputDir: "webv2",
  > }
  > console.log(`${process.env.NODE_ENV}`)
  > if( process.env.NODE_ENV.match(/build/g) ){ 
  > delete d.configureWebpack.devtool
  > d.productionSourceMap = false;
  > }
  > module.exports = d
  > ```
  >
  > vue 在vscode 下断点
  >
  > file --> preferences --> setting 找到eslint ，找到几个  check box 勾上



### 如果babel 出错

```
# babel.config.js 改成这样

module.exports = {
    presets: [
        [ "@vue/app", { useBuiltIns: "entry" } ]
    ]
}
```





## 运行前端

- npm  run serve 

  > 默认 8080 端口

## 让chrome 断下

```javascript
// index.vue
saveToWord() { debugger // 这样就会断在这一行 
```

- https://www.jianshu.com/p/c013027069ce
  - Vue前端部署



## 自适应大小

```
在父级div加：

overflow: auto;
```



## ios

- https://v2ex.com/t/862361 强制 WKWebView 进行刷新缓存实时渲染

  > IOS 中如果返回的 data 是普通文本文字，或返回的数据中包含普通文本文字，那只需要达到非空 200 字节即可以触发渲染
  >
  > ```
  > const IOS_200 = `<div style="height:0;width:0;">\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b</div>`
  > ```



# vue-element

- https://element.eleme.io/#/zh-CN/component/collapse

  > 手风琴效果  每次只能展开一个面板

- https://blog.csdn.net/u011332271/article/details/105226511

  > 动态创建组件

- https://cloud.tencent.com/developer/article/1467371

  > 官方文档给了解决方案：如果试图使用 v-html 组合模板，可以重新考虑是否通过使用组件来替代。
  >

```html
v-html指令解析成了innerHTML。所以在节点元素上直接用innerHTML也是可以的，例如：
document.getElementById('app').innerHTML = "xxxxx" # 纯html
```



- https://segmentfault.com/a/1190000010958154

  > v-for

- https://segmentfault.com/a/1190000020053344

  > 跨组件通信

- https://cn.vuejs.org/v2/guide/syntax.html#v-bind-%E7%BC%A9%E5%86%99

  ```
  v-bind 缩写
  
  <!-- `${jp}<img id="img_${elm_id}" src="${img_play}" onclick="play('${elm_id}')"><audio id="audio_${elm_id}" src="${au_url}" type="audio/mpeg" preload="auto"></audio><br>${zh}`; //debugger -->
  
  # 
          {{ item.jp }} <img :id="`img_${elm_id}`" :src="`${img_play}`" :onclick="`play('${elm_id}')`">
  ```


- https://blog.csdn.net/qq_29869111/article/details/100154941

  > 动态加载本地图片

- https://juejin.cn/post/6844904130176090126

  > 根据elementUI的Carousel+Image实现图片动态加载问题

- 图片的骚操作

  ```
  <img :src="item.image ? require(`../../assets/image/${item.image}`) : ''" alt="image"/>
  ```

  

- https://blog.csdn.net/qq_32963841/article/details/80707461

  > 3d 图



# vue-element-admin



```
src\router\modules\components.js

路由加一项
  children: [
    {
      path: 'multiselect',
      component: () => import('@/views/components-demo/multiselect'),
      name: 'multiselect',
      meta: { title: 'multiselect' }
    },
    
组件加一项
\src\views\components-demo\multiselect.vue


```



```
npm install --save normalize.css
```



## SplitPane

> https://panjiachen.github.io/vue-element-admin/#/components/split-pane



# VUE+CefSharp

- https://blog.csdn.net/lweiyue/article/details/120484812  CefSharp和Vue交互开发
- http://www.lizhenghao.site/blog/2022/01/08/136  Winform/WPF利用CefSharp集成vue开发
- https://blog.csdn.net/wuyuander/article/details/107359120  手把手教你使用CefSharp开发Winform
- https://blog.csdn.net/yh0503/article/details/86648682  WinForm CefSharp 笔记一（入门篇）
- https://www.cnblogs.com/TianFang/p/9906786.html  调试窗口



```c#

// NuGet 安装 CefSharp.WinForms

// 成功显示vue页面, 工程设置成 x64, any cpu 是不行的
using CefSharp.WinForms;

        public Form1()
        {
            InitializeComponent();

            //string path = AppDomain.CurrentDomain.BaseDirectory + @"dist/index.html";
            String path = string.Format(@"{0}\dist\index.html", Application.StartupPath);

            //String path = "http://baidu.com";

            browser = new ChromiumWebBrowser(path);
            browser.JavascriptObjectRepository.Settings.LegacyBindingEnabled = true;

            this.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;
        }
```



## 无边框全透明窗体



```
// 设置窗体属性
BackColor  -> 点系统 -> (白色)window

FormBorderStyle -> None

ShowlnTaskbar -> False

Size -> 0,0

TransparencyKey -> (白色)window

```



## 双击托盘图标

```

            if (WindowState == FormWindowState.Minimized)
            {
                //还原窗体显示    
                WindowState = FormWindowState.Normal;
                //激活窗体并给予它焦点
                this.Activate();
                //任务栏区显示图标
                this.ShowInTaskbar = true;
                //托盘区图标隐藏
                notifyIcon1.Visible = false;
            }

```





## 退出程序



```c#
Application.ExitThread();

this.Dispose();
this.Close();

```



## 跨线程更新UI

- https://blog.csdn.net/l198738655/article/details/120126970





## 复制文件到目标目录



```
vs2019 
复制页面到目标目录
方式1
项目->属性->生成事件->生成前事件命令行

添加如下

xcopy /Y /i /e $(ProjectDir)\html $(TargetDir)\html
```







# VUE+Electron+Edge

- https://blog.csdn.net/kyq0417/article/details/111310539

  > VUE+Electron+Edge开发中遇到的坑

- https://github.com/agracio/electron-edge-js



# Godot

## 源码编译

- https://github.com/Orama-Interactive/Pixelorama

  - https://docs.godotengine.org/en/latest/contributing/development/compiling/compiling_for_windows.html
  - https://blog.csdn.net/feiyunw/article/details/121861944  必看

  ```
  安装 Godot 3.5
  
  python -m pip install scons
  
  python -m pip install --upgrade pywin32
  
  git clone -b 3.5.1-stable https://github.com/godotengine/godot.git
  
  启动"x64 Native Tools Command Prompt for VS"
  
  
  cd /d E:\t\godot
  
  scons platform=windows vsproj=yes
  	# 成功生成解决方案 godot\godot.sln
  	scons p=windows tools=no target=release use_lto=no deprecated=no vsproj=no debug_symbols=no
  	# 编译发布版本
  	scons p=windows tools=yes target=release_debug use_lto=no deprecated=no vsproj=yes debug_symbols=yes
  	# 编译Debug版本
  
  
  ```

- https://blog.csdn.net/my_business/article/details/7816736  **scons** 是类 cmake 工作，用python语法

- https://github.com/RodZill4/material-maker

- https://github.com/touilleMan/godot-python  **godot + python**



## 可调窗体

- https://github.com/gilzoide/godot-dockable-container



## 拷贝大量数据

```
# https://github.com/touilleMan/godot-python/issues/329
I was suggesting to create the bytes array through godot.pool_arrays.PoolByteArray, then accessing it underlying buffer with godot.pool_arrays.PoolByteArray.raw_access. numpy.frombuffer can then wrap this underlying buffer without copying it.
You then end up with a Numpy array that can be used for your Image.create_from_data, the only gotcha is you should be careful about this numpy array object lifetime given it shares the same buffer with the PoolByteArray.

The easy way to avoid lifetime issues would be to create a PoolByteArray singleton with a fixed size when initializing your application (hence the underlying buffer is never freed)
```



### lmdb

```
整个数据集都在磁盘上。它的一些部分在内存中。当需要不在内存中的部分时--操作系统从磁盘中获取它，并通过把它放在进程的内存中交给应用程序。

后台的mongodb，但不仅如此，我还想到了postgresql，它们强烈建议拥有与工作数据集同样多的内存。
```





```
LMDB全称Lightning Memory-Mapped Database,是内存映射型数据库，这意味着它返回指向键和值的内存地址的指针，而不需要像大多数其他数据库那样复制内存中的任何内容，使用内存映射文件，可以提供更好的输入/输出性能，对于神经网络的的大型数据集可以将其存储到LMDB中

LMDB属于key-value数据库，而不是关系型数据库( 比如 MySQL )，LMDB提供 key-value 存储，其中每个键值对都是我们数据集中的一个样本。LMDB的主要作用是提供数据管理，可以将各种各样的原始数据转换为统一的key-value存储。

LMDB不仅可以用来存放训练和测试用的数据集，还可以存放神经网络提取出的特征数据。如果数据的结构很简单，就是大量的矩阵和向量，而且数据之间没有什么关联，数据内没有复杂的对象结构，那么就可以选择LMDB这个简单的数据库来存放数据。

用LMDB数据库来存放图像数据，而不是直接读取原始图像数据的原因：

数据类型多种多样，比如：二进制文件、文本文件、编码后的图像文件jpeg、png等，不可能用一套代码实现所有类型的输入数据读取，因此通过LMDB数据库，转换为统一数据格式可以简化数据读取层的实现。
lmdb具有极高的存取速度，大大减少了系统访问大量小文件时的磁盘IO的时间开销。LMDB将整个数据集都放在一个文件里，避免了文件系统寻址的开销，你的存储介质有多快，就能访问多快，不会因为文件多而导致时间长。LMDB使用了内存映射的方式访问文件，这使得文件内寻址的开销大幅度降低。
```



## 显示网页 

- https://github.com/stigmee/gdnative-cef  嵌入cef

```
OS.shell_open("url")
	# 调用系统功能

if OS.has_feature('JavaScript'):
    JavaScript.eval("""
        window.open('https://google.com', '_blank').focus();
    """)
```







# UGUI

- https://www.raywenderlich.com/6570-introduction-to-unity-ui-part-1

- https://blog.csdn.net/Wrinkle2017/article/details/117257104  息屏开屏后，屏幕自动旋转刷新

  > ```c#
  >  private void OnApplicationPause(bool pauseStatus)
  >     {
  >         if (pauseStatus)
  >         {
  >             SaveDataToLocal.Instance.SaveAccountData(UserData.Instance.ifFirstJoin, UserData.Instance.CurrentBigClassLeve, MainUIModel.Instance.ifOpenAudio, UserData.Instance.ifFinishGuide1, UserData.Instance.ifFinishGuide2, UserData.Instance.isFirstInNewLevel);
  >             //Screen.orientation = ScreenOrientation.PortraitUpsideDown;
  >             //息屏开屏后，屏幕自动旋转刷新
  >             if (Input.deviceOrientation == DeviceOrientation.LandscapeLeft)
  >                 Screen.orientation = ScreenOrientation.LandscapeRight;
  >             else 
  >                 Screen.orientation = ScreenOrientation.LandscapeLeft;
  >         }
  >         else
  >         {
  >             Screen.orientation = ScreenOrientation.AutoRotation;
  >         }
  >     }
  > 
  > ```



# cudf

- https://github.com/rapidsai/node/tree/main/modules/cudf

  > - https://blog.csdn.net/sinat_26917383/article/details/104504600
  >
  > 用于处理数据，包括加载、连接、聚合和过滤数据。向GPU的转移允许大规模的加速，因为GPU比CPU拥有更多的内核。**一个比较好的使用场景是，代替并行**，在pandas处理比较慢的时候，**切换到cuDF，就不用写繁琐的并行了**。
  >
  > ```
  > docker pull ghcr.io/rapidsai/node:22.8.2-runtime-node16.15.1-cuda11-ubuntu20.04-cudf
  > ```
  >
  > 

- https://github.com/rapidsai/node/tree/main/modules/demo/client-server

  > 地图移动GPU 加速示例

- https://github.com/rapidsai/node

  > nodejs python cuda 加速

# gpu.js

```
// 并行生成一万个随机数
const { GPU } = require('gpu.js');
const gpu = new GPU({ mode: 'gpu' });
const nobs=10000;

const kernel = gpu.createKernel(function() {
const y=Math.random();
return y;
}, { output: [nobs] });
const data = kernel();
```



# node-sdl

- https://github.com/kmamal/node-sdl
- https://github.com/fosterseth/sdl2_video_player  **视频播放**





# vxe-table

- https://github.com/x-extends/vxe-table



# CSS

- https://blog.csdn.net/zgh0711/article/details/78270555  flex布局保持内容不超出

- https://blog.csdn.net/zgh0711/article/details/86541139  多行显示，溢出时显示省略号

- https://blog.csdn.net/zgh0711/article/details/81536355 display 的 block，inline，inline-block

- https://blog.csdn.net/zgh0711/article/details/80167224  class 动态绑定

- https://blog.csdn.net/zgh0711/article/details/80172174   路由缓存 keep-alive

  > 保存某个组件的状态或避免重新渲染
  >
  >  App.vue
  >
  > ```javascript
  >     <keep-alive>
  >          <router-view v-if="$route.meta.keepAlive"></router-view>
  >         </keep-alive>
  >         <router-view v-if="!$route.meta.keepAlive"></router-view>
  >    ```
  >    
  > 
  >
  > 每个路由都可以给它定义 meta 属性，我们可以给想要缓存功能的路由定义一个 meta 对象，在里面定义一个 keepAlive 属性，值为 true，这个 meta 对象里面还可以定义其他的属性，比如 title。
  >
  > ```javascript
  >     {
  >          path: '/guideList',
  >             name: 'GuideList',
  >             meta: {keepAlive: true, title: 'title'},
  >             component: GuideList
  >         },
  >    ```
  >    
  > 
  >
  
- https://blog.csdn.net/zgh0711/article/details/80171138  给 v-html 渲染出的内容添加样式

  >```javascript
  ><div class="content" v-html="agreement.content"></div>
  >
  >.content >>> span{
  >        width: 100%;
  >        ...
  >    }
  >```
  >
  >通过在需要设置样式的元素前面加三个箭头就可以实现

- https://blog.csdn.net/zgh0711/article/details/80607158   ECharts 画 K 线图

- https://blog.csdn.net/zgh0711/article/details/89562566  自定义指令解决IOS12键盘收起后底部留白

  > ```javascript
  > import Vue from 'vue'
  > /**
  >  * 自定义指令 v-reset-page，以解决 iOS 12 中键盘收起后页面底部有留白的问题
  >  */
  > 
  > Vue.directive('resetPage', {
  >   inserted: function (el) {
  >     // 该方法有时候会出现点击了键盘右上角完成按钮，键盘收起又弹出的情况
  >     // el.addEventListener('blur', function () {
  >     //   if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
  >     //     let currentPosition, timer
  >     //     let speed = 1//页面滚动距离
  >     //     timer = setInterval(function () {
  >     //       currentPosition = document.documentElement.scrollTop || document.body.scrollTop
  >     //       currentPosition -= speed
  >     //       window.scrollTo(0, currentPosition)//页面向上滚动
  >     //       currentPosition += speed //speed变量
  >     //       window.scrollTo(0, currentPosition)//页面向下滚动
  >     //       clearInterval(timer)
  >     //     }, 100)
  >     //   }
  >     // })
  >     
  >     // 监听键盘收起事件
  >     document.body.addEventListener('focusout', () => {
  >       if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
  >         //软键盘收起的事件处理
  >         setTimeout(() => {
  >           const scrollHeight = document.documentElement.scrollTop || document.body.scrollTop || 0
  >           window.scrollTo(0, Math.max(scrollHeight - 1, 0))
  >         }, 100)
  >       }
  >     })
  >   }
  > })
  > 
  > 
  > ```
  >
  > ```javascript
  > // main.js 中引入
  > import './utils/directive'
  > ```
  >
  > ```javascript
  > // 在 input 中使用
  > <input v-reset-page v-model="searchKey" type="number" placeholder="搜索作品编号">
  > ```

- https://blog.csdn.net/zgh0711/article/details/100013303 背景音乐

  > ```
  > <audio ref="audio" src="https://img.youpenglai.com/penglai/1.mp3" loop preload="auto"></audio>
  > 
  > ```
  >
  > a
  >
  > ```javascript
  > <template>
  >   <div class="page-promotion flex-col">
  >     <div class="con-play flex" @click="audioPlayOrPause()">
  >       <img v-show="playFlag" class="audio-on" src="../assets/img/promotion/ic_sound_on.svg" alt="">
  >       <img v-show="!playFlag" class="audio-off" src="../assets/img/promotion/ic_sound_off.svg" alt="">
  >     </div>
  >     
  >     <audio ref="audio" src="https://img.youpenglai.com/penglai/1.mp3" autoplay loop preload="auto"></audio>
  >   </div>
  > </template>
  > 
  > <script>
  >   export default {
  >     name: 'Promotion',
  >     data () {
  >       return {
  >         playFlag: true,
  >         clickMusicBtn: false,
  >       }
  >     },
  >     
  >     async mounted () {
  >       this.audioAutoPlay()
  >       document.addEventListener("visibilitychange", (e) => { // 兼容ios微信手Q
  >         if (this.clickMusicBtn) { // 点击了关闭音乐按钮
  >           if (this.playFlag) {
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           } else {
  >             this.audioPause();
  >             this.playFlag = false;
  >           }
  >       
  >           text.innerHTML = e.hidden;
  >           if (e.hidden) {  // 网页被挂起
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           } else { // 网页被呼起
  >             this.audioPause();
  >             this.playFlag = false;
  >           }
  >         } else { // 未点击关闭音乐按钮
  >           if (this.playFlag) {
  >             this.audioPause();
  >             this.playFlag = false;
  >           } else {
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           }
  >       
  >           text.innerHTML = e.hidden;
  >           if (e.hidden) {  // 网页被挂起
  >             this.audioPause();
  >             this.playFlag = false;
  >           } else { // 网页被呼起
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           }
  >         }
  >       });
  >     },
  >     
  >     methods: {
  >       audioPlayOrPause() {
  >         this.clickMusicBtn = !this.clickMusicBtn;
  >         if (this.playFlag) {
  >           this.audioPause();
  >           this.playFlag = false;
  >         } else {
  >           this.audioAutoPlay();
  >           this.playFlag = true;
  >         }
  >       },
  >       audioPause() {
  >         let audio = this.$refs.audio
  >         audio.pause();
  >         document.addEventListener("WeixinJSBridgeReady", function () {
  >           audio.pause();
  >         }, false);
  >       },
  >       audioAutoPlay() {
  >         let audio = this.$refs.audio
  >         audio.play();
  >         document.addEventListener("WeixinJSBridgeReady", function () {
  >           audio.play();
  >         }, false);
  >       },
  >     },
  >   }
  > </script>
  > 
  > ```
  >
  > vue-cli3 项目，如果通过相对路径引用资源则会经过 webpack 打包，相反，如果通过绝对路径引用则不会经过 webpack 处理，注意这里资源的绝对路径不是 /public/xxx 而是直接填 public 里的路径，官方文档没有例子说这件事。



# React Native

- https://github.com/alantoa/react-native-awesome-slider/tree/main/example

- https://www.v2ex.com/t/843175

  > u2 player

- https://www.cnblogs.com/skychx/p/react-native-tweet.html  2 年 React Native 开发经验
- https://www.cnblogs.com/skychx/p/react-native-flatlist.html FlatList 原理解析与性能优化
- https://www.cnblogs.com/penghuwan/p/11633547.html  从React-Native坑中爬出
- https://www.cnblogs.com/penghuwan/p/11775900.html React-Native 转小程序
- https://github.com/alitajs/alita  umi.js ?



# push stream

- https://github.com/phoboslab/jsmpeg

- https://blog.csdn.net/a843334549/article/details/120697574  海康推流

- https://blog.csdn.net/qq_41619796/article/details/121161232

- https://gitee.com/zhairuihao/jsmpeg-ws-web

  > cegbdfa
  >
  > cegfdb link to github
  >
  > link to 123xxxx5&qx.com

- https://www.cnblogs.com/zzsdream/p/13410224.html  **很详细**

  - https://github.com/ivan-94/video-push/blob/master/jsmpeg/server.js
  - https://github.com/phoboslab/jsmpeg/issues/338  websockect + jsmpeg
    - https://github.com/phoboslab/jsmpeg/issues/391

  

# nodegui qt

- https://github.com/nodegui/nodegui

  > NodeGUI is powered by **Qt5** 



# uView UI

```
关于uView UIuView UI 是一个用于uni-app 多端开发的优质UI 组件库， ... 代码，可发布到iOS、Android、Web（响应式）、以及各种小程序（微信/支付宝/ 
```

- https://blog.csdn.net/mrs_chens/article/details/108417919

  > uniapp 项目引入 uView 并简单使用

- https://github.com/panghujiajia/v2ex

  > uniapp 写的 V2EX 小程序

> 以上对比下来
> Flutter == ReactNative >>>>>>> **UniApp(做 App 用这个你就是坑自己**)



## vue和nvue

```
因为uni-app是逻辑和渲染分离的。渲染层，在app端提供了两套排版引擎：小程序方式的webview渲染，和weex方式的原生渲染。
两种渲染引擎可以自己根据需要选。vue文件走的webview渲染，nvue走的原生渲染。组件和js写法是一样的，css不一样，原生排版的能用的css必须是flex布局，这是web的css的子集。当然什么界面都可以用flex布出来。

区别和适用场景官方文档里写的很清楚：https://uniapp.dcloud.io/use-weex

```



# DotNet+Node

- https://github.com/Elringus/DotNetJS



# QT+Vue

- https://blog.csdn.net/yyt593891927/article/details/108546503
- https://zhuanlan.zhihu.com/p/88620573



# Vue+ios

- https://github.com/nativescript-vue/nativescript-vue
- https://docs.nativescript.org/environment-setup.html#macos-ios



# RustDesk

- https://www.v2ex.com/t/853682





# tesseract-ocr

- https://github.com/peirick/Tesseract-OCR_for_Windows

  > ```
  > git clone --recursive https://github.com/peirick/Tesseract-OCR_for_Windows.git
  > 
  > vs2019 编译，编码报错的文件改 gb2312 编码
  > 
  > ```



```javascript
/*

step 1: 安装 tesseract-ocr

先安装c++17
yum install centos-release-scl
yu install devtoolset-7-gcc-c++ --enablerepo='centos-sclo-rh'
scl enable devtoolset-7 'bash' # 切换编译器
which gcc

# https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata 先下载语言文件
# 自动安装的语言模型很小，不准确

// https://thelinuxcluster.com/2020/02/04/compiling-tesseract-5-0-on-centos-7/
> yum install autoconf automake libtool pkgconfig.x86_64 libpng12-devel.x86_64 libjpeg-devel libtiff-devel.x86_64 zlib-devel.x86_64
# wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz .
# tar -zxvf leptonica-1.79.0.tar.gz
# cd leptonica-1.79.0
# ./configure --prefix=/usr/local/leptonica-1.79.0
# make
# make install

> export PKG_CONFIG_PATH=/usr/local/leptonica-1.79.0/lib/pkgconfig
$ git clone https://github.com/tesseract-ocr/tesseract.git
$ cd tesseract
$ ./autogen.sh
$ ./configure --prefix=/usr/local/tesseract-5.0 
$ make
$ make install
$ ln -s /usr/local/tesseract-5.0/bin/tesseract /usr/local/bin/
$ tesseract  --version #  成功


复制语言数据 chi_sim.traineddata  eng.traineddata  到目录  /usr/local/tesseract-5.0/share/tessdata

step 2:  npm install tesseractocr string-algorithms fast-levenshtein


*/


let tesseract = require('tesseractocr')

let recognize = tesseract.withOptions({
    psm: 4,
    language: [ 'chi_sim', 'eng' ],
    config: ['tessedit_do_invert=0', 'oem=1']
})


        let buffer = Buffer.from(imgData, 'base64')

        //const text = await recognize('7001.jpg')
        let tesstext = await recognize(buffer)
```





# NFS



```
nfs 成功
	umount -f -l  /home/data/users/xxx/mnt     # 取消挂载

	https://qizhanming.com/blog/2018/08/08/how-to-install-nfs-on-centos-7

	vi /etc/exports      # .124
		/home/data/users/xxx/data_backup/    192.168.2.0/24(rw,sync,no_root_squash,no_all_squash)
	
	客户端
		yum -y install nfs-utils

		mkdir /yingedu/shared
		chmod 755 /xxx/shared

		showmount -e 192.168.1.xxx     # 显示 .124 的共享文件

		mount -t nfs 192.168.1.xxx:/home/data/users/xxx/data_backup  /yingedu/shared    # 挂载远程目录
```





# v2ray

- https://shadowzenhk.medium.com/%E5%A6%82%E4%BD%95%E6%AD%A3%E7%A1%AE%E4%BD%BF%E7%94%A8cloudflare-cdn%E9%AB%98%E9%80%9Fip%E5%8A%A0%E9%80%9Fv2ray%E8%AE%BF%E9%97%AE-f1abcc76369c



# Excel



```javascript
    let xlsx = require('node-xlsx')  // npm install node-xlsx --save

    function writeExcel(data, fname) {
        let buffer = xlsx.build([
            {
                name: 'sheet1',
                data
            }
        ])
        require('fs').writeFileSync(`${fname}`, buffer, {'flag':'w'}) // 生成excel
    }

    let titles = ['id', 'name'] // 列名
    let data = [] // 写入excel 的数据行
    let fname = './the_content.xlsx'

    data.push(titles)
    data.push([0, 'first'])
    data.push([1, 'second'])
    writeExcel(data, fname)
```



## excel 正则

- https://github.com/liuyi91/Excel



## C#读写excel

```
# https://blog.csdn.net/weixin_42176639/article/details/101648803
	# NOPI读写Excel，并插入图片
```





# Docx



```javascript

let path = require('path')
var mammoth = require("mammoth");

function getTestByWord(fileName) {
    return new Promise((ok, err) => {
        // var url = path.join(__dirname, 'A1-3-2.docx');
        // var url = path.join(__dirname, "../../../file/" + fileName);
        var url = fileName
        mammoth.extractRawText({
                path: url
            })
            .then(function (result) {
                var text = result.value; // The raw text
                var messages = result.messages;
                ok(text);

            })
            .catch((e) => {
                err(false)
            })
            .done();
    })
}

( async()=>{

    let fileName = path.join(__dirname, 'A3-2&3-1.docx');
    let s = await getTestByWord(fileName)
    let a = 1

}) ()


```





```javascript
// https://www.jianshu.com/p/68a420a68ded
	十行代码教你用node.js读取docx中的文本
let rd = require('rd');
let fs = require('fs');
let path = require("path")

let docx4js = require('docx4js');
const AdmZip = require('adm-zip'); //引入查看zip文件的包
const zip = new AdmZip("alldata/A1-1&1-2.docx"); //filePath为文件路径

// 同步遍历目录下的所有 word 文件
rd.eachFileFilterSync('alldata', /\.docx$/, function (fullpath, stats) {

    let basename = path.basename(fullpath);
    
    if (basename != "A1-1&1-2.docx") {
        return;
    }

    let contentXml = zip.readAsText("word/document.xml");   // 内容文本
    
    let str = "";
    contentXml.match(/<w:t>[\s\S]*?<\/w:t>/ig).forEach((item)=>{

        str = str + item.slice(5,-6) + "\n";  // 不知道为什么读出来文档自带的换行没了
    }) 

    fs.writeFileSync('2.txt', str);

});
```





```javascript

// import docx4js from "docx4js"


const docx4js = require('docx4js');


docx4js.docx.load("alldata/A1-1&1-2.docx").then(docx => {
    var content = docx.officeDocument.content.text()
    console.log("[Docx.jsx] docx:", content); // I am able to get the data here.
}).catch(err => {
    console.error("[Docx.jsx] err:", err);
});

To get header you do it like

docx.getObjectPart("word/header1.xml").text();

And you can do the same thing for the footer

docx.getObjectPart("word/footer1.xml").text();

you can get the content/body as well doing like

docx.getObjectPart("word/document.xml").text();
```





