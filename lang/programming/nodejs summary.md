

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
// http://127.0.0.1:666/gendifficulty?AppID=8911&KsbaoAppID=1202
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



## Regex



> https://javascript.info/regexp-groups



### matchAll

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



### replace



```
var strs = fs.readFileSync(fdoc, "utf8")

strs = strs.replace(/\*\*\*\*\*\*\*\*\*\*/g, '').replace(/\r\n/g, '\n').replace(/\t/g, '  ').trim()
strs = '\n\n' + strs +  '\n\n'
```







## 不转义



```javascript
String.raw `Hi\u000A!`;
```





## Docx



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





