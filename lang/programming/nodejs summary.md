

```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7
systemctl enable postgresql-13 # 自启动

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目

pm2 delete processID  // 删除一项  

# 关闭防火墙
systemctl stop firewalld

# atuto run when reboot
chmod +x /etc/rc.d/rc.local
vi /etc/rc.d/rc.local
mount /dev/sda1 /mnt  # 加一句，挂载存储块



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





# Syntax



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



```
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

```
export default {

	funtion a {
	
	},
	function b {
		this.a()
	}
}
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



```
# 连续判断
	const color = d.added ? 'green' :
        d.removed ? 'red' : 'grey'
```





# Regex



> https://javascript.info/regexp-groups



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



### <= 向后查找

- < 前面必须匹配，但不吃掉它(consume)



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



## split

```javascript
const splits = myString.split(' ', 3)
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





# Array



## join



```
# 连成字符串，中间加空格
const arr = ['Fire', 'Air', 'Water'];
console.log(arr.join(' '));
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



## includes

```
const pets = ['cat', 'dog', 'bat']
console.log(pets.includes('cat'))
// expected output: true
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



## Object.assign



```javascript
let data = {}
Object.assign(data, query) // 赋值
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
fs.mkdirSync(targetDir, { recursive: true })
```



## read write



```
require('fs').writeFileSync('menu.json', JSON.stringify(menujson) )
```

```
require('fs').readFileSync('./input.txt',{encoding:'utf8', flag:'r'})
```



## 去掉扩展名



```
imgName = path.parse(imgName).name  // 去掉扩展名
let { base,dir,ext,name,root} = path.parse(mlpath)
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



## Grup



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





# pm2



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
、下载

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





# Vue



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

package.json 下的devDependencies 加入开发依赖包(必须是这下面)
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





