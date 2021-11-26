

```
npm install --dependencies
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
  let response = await post('xxxxx', json)

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



## test



```javascript
// 是否匹配
const regex = new RegExp('foo*');
const globalRegex = new RegExp('foo*', 'g');
console.log(regex.test(str));
// expected output: true
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
// 匹配不以    题\s*\n    结尾的字符串
ss = '\n一、www.hao.题com \n'

let regStr = String.raw`(\n\s*[一二三四五六七八九十百千万]+?、(?!.*?(题\s*\n)).+?\n)`

let matches = ss.matchAll(new RegExp(regStr,'gs'))
let arr = Array.from(matches)
```









### ?= 向前查找

- = 后面必须匹配，但不吃掉它(consume)

```
# https://www.jianshu.com/p/eec1a081b4b7
```



### <= 向后查找

- < 前面必须匹配，但不吃掉它(consume)









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





# Array



## 遍历



```
arr.forEach(element => {
  console.log(element);
});
```





## sort



```javascript
// 双排序，类似C# 的 order by then by
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



## isEmpty



```javascript
let _ = require('lodash')
_.isEmpty(dic_ansers)
```







# File



```
require('fs').writeFileSync('menu.json', JSON.stringify(menujson) )
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
	
setBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 45)
setBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 142)
setBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 164)
setBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 208)
setBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 219)
setBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 226)
clearBreakpoint('/yingedu/project_test/ksbaiexam/http/api/submit.js', 45)

# 可能是这一句的错误
let retSaveExam = await this.services.saveExamgather({examgahters})

n # 下一行

break in file:////yingedu/project_test/ksbaiexam/http/api/submit.js


# https://zhuanlan.zhihu.com/p/98571113
	# chrome 远程调试node


node14 --inspect-brk=0.0.0.0:9229 server.js

chrome://inspect/#devices

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



## 时区转换



```
select NOW();
SELECT convert_tz(now(),@@session.time_zone,'+08:00')


# 24小时制
let u = re[0].updateTime
let tt = new Date(u).toLocaleString('chinese',{hour12:false})

```



# time



## 24 小时制



```javascript
select NOW();
SELECT convert_tz(now(),@@session.time_zone,'+08:00')


# 24小时制
let u = re[0].updateTime
let tt = new Date(u).toLocaleString('chinese',{hour12:false})
```









# pm2



## rename



```
pm2 restart id --name newName
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





