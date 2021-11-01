

```
npm install --dependencies
```







## Get

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



# Syntax



## typeof



```javascript
            if (typeof content == 'object') {

            } else if (typeof content == 'string') {
                var j = { "title":title, "content":content, childs:[] }
                
            }
```





# Regex



> https://javascript.info/regexp-groups



## matchAll

- 相当于python 的 finditer

```javascript
const string = 'black*raven lime*parrot white*seagull';
const regex = /(?<color>.*?)\*(?<bird>[a-z0-9]+)/;
for (const match of string.matchAll(regex)) {
    let value = match[0];
    let index = match.index;
    let input = match.input;
    console.log(`${value} at ${index} with '${input}'`);
console.log(match.groups.color);
    console.log(match.groups.bird);
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



## replace



```
var strs = fs.readFileSync(fdoc, "utf8")

strs = strs.replace(/\*\*\*\*\*\*\*\*\*\*/g, '').replace(/\r\n/g, '\n').replace(/\t/g, '  ').trim()
strs = '\n\n' + strs +  '\n\n'
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







# String



## 不转义



```javascript
String.raw `Hi\u000A!`;
```



## 动态计算



```javascript
`${type}Mid`
`Found ${match[0]} start=${match.index} end=${match.index + match[0].length}.`
```



# Array



## 遍历



```
arr.forEach(element => {
  console.log(element);
});
```





## sort



```javascript
// Lodash 4.x:
_.orderBy(data, [
  function (item) { return item.sortData.a; },
  function (item) { return item.sortData.b; }
], ["asc", "desc"]);
```





# json



## 遍历



```javascript
1238

Under ECMAScript 5, you can combine Object.keys() and Array.prototype.forEach():

var obj = { first: "John", last: "Doe" };

Object.keys(obj).forEach(function(key) {
    console.log(key, obj[key]);
});
ECMAScript 6 adds for...of:

for (const key of Object.keys(obj)) {
    console.log(key, obj[key]);
}
ECMAScript 8 adds Object.entries() which avoids having to look up each value in the original object:

Object.entries(obj).forEach(
    ([key, value]) => console.log(key, value)
);
You can combine for...of, destructuring, and Object.entries:

for (const [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
Both Object.keys() and Object.entries() iterate properties in the same order as a for...in loop but ignore the prototype chain. Only the object's own enumerable properties are iterated.
```



## exist



```javascript
if ( !(keyParent in menus) ) {
```



# File



```
require('fs').writeFileSync('menu.json', JSON.stringify(menujson) )
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







# 随机



```
arr[Math.floor(Math.random() * arr.length)] // 从数组里随机选择一个  Math.random 最小值是0， 最大值小于1
```





# redist



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







# Chrome



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





