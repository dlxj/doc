

[TOC]

# Python 3  Summary

[z](https://zhuanlan.zhihu.com/p/64893308)

1. 有\__init\__.py 文件的文件夹被认为是一个包，否则只是普通文件夹
   
- 普通文件夹不能 import, package 才可以
  
2.  .py 文件被认为是一个模块

- 单独一个py 文件就是一个module
  
3. import 后面必须是模块名

4. from 模块名 import 变量名 

5. import 包名.模块名

6. python l默认在sys.path 这个list 里的众多目录下找需要import 的模块，找不到就报错

7. \__file\__ 是模块自身的绝对路径

8. 要得到上层目录名可以连用两次os.path.dirname  

   - ```text
     os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     ```

9.   from package import *

   - \__init\__.py ： \__all\__ = [‘echo’, ‘effect’, ‘reverb’]

   - would be equivalent to

     ```
     from package import echo
     from package import effect
     from package import reverb
     ```

     

## Import



### 同级目录直接用文件名导入



```
from iJson import save_json
currDir = os.path.dirname(os.path.abspath(__file__))
fname_to_save = os.path.join(currDir, 'j.json')
save_json(fname_to_save, { 0:'a', 1:'b' })
```



### 上级目录的子目录



- 需要子目录里有空的 \__init\__.py

     1.  将上级目录加到sys.path
     2.  按照对下级目录模块的方式导入



```
#from __future__ import absolute_import
import os, sys
import sys
sys.path.append("..")
# import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from std import iJson
currDir = os.path.dirname(os.path.abspath(__file__))
fname_to_save = os.path.join(currDir, 'j.json')
iJson.save_json(fname_to_save, { 0:'a', 1:'b' })
print("hi,,,")
```





## Path

```python
os.path.abspath(__file__)                   # current file
os.path.dirname(os.path.abspath(__file__))  # current file directory
os.path.dirname(os.path.abspath(__name__))  # ?? directory
```

## package

```python
import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg
python3 -m mypackage.A.spam # Relative imports work
```
### 绝大部分时候让__init__.py空着就好

- 让每个目录都包含一个__init__.py，就可以import

###  \_\_init\_\_.py 可以为下层目录代为import 一些东西

> ```python
> # graphics/formats/__init__.py
> from . import jpg # 代替import graphics.formats.jpg
> from . import png # 以及import graphics.formats.png
> ```

```python
#-*- encoding:utf-8 -*-
from __future__ import absolute_import
# from .FastTextRank4Sentence import FastTextRank4Sentence
# from .TextRank4Sentence import TextRank4Sentence
from . import util
version = '0.2'
```

### 黑科技
```python
import os,sys
sys.path.append("./")
import demo2
from demo2.test_case import test_baidu
```




> 当一个文件夹下有   init   .py时，意为该文件夹是一个包（package），其下的多个模块（module）构成一个整体，而这些模块（module）都可通过同一个包（package）导入其他代码中。
>
> 其中   init   .py文件 用于组织包（package），方便管理各个模块之间的引用、控制着包的导入行为。
> 该文件可以什么内容都不写，即为空文件（为空时，仅仅用import [该包]形式 是什么也做不了的），存在即可，相当于一个标记。
> 但若想使用from pacakge_1 import *这种形式的写法，需在  init  .py中加上：   all    = [‘file_a’, ‘file_b’] #package_1下有file_a.py和file_b.py，在导入时   init   .py文件将被执行。
> 但不建议在   init   .py中写模块，以保证该文件简单。不过可在   init   .py导入我们需要的模块，以便避免一个个导入、方便使用。
>
> 其中，   all   是一个重要的变量，用来指定此包（package）被import *时，哪些模块（module）会被import进【当前作用域中】。不在   all   列表中的模块不会被其他程序引用。可以重写  all  ，如   all    = [‘当前所属包模块1名字’, ‘模块1名字’]，如果写了这个，则会按列表中的模块名进行导入。
>
> 在模糊导入时，形如from package import *，*是由__all__定义的。
>
> 精确导入，形如 from package import *、import package.class。
>
>    path   也是一个常用变量，是个列表，默认情况下只有一个元素，即当前包（package）的路径。修改   path   可改变包（package）内的搜索路径。
>
> 当我们在导入一个包（package）时（会先加载   init   .py定义的引入模块，然后再运行其他代码），实际上是导入的它的   init   .py文件（导入时，该文件自动运行，助我们一下导入该包中的多个模块）。我们可以在   init   .py中再导入其他的包（package）或模块 或自定义类。
> ————————————————
> [c](https://blog.csdn.net/weixin_38256474/java/article/details/81228492)



## 静态函数 构造函数 析构函数

```python
 @staticmethod
 def connect():
 
 def __init__(self):
 def __del__(self):
```





## Handle Error

```python
raise RuntimeError('some err')
```


## Exception

```python
    try:
        json.loads( dic["TestJson"], strict=False )
    except Exception as e:
        print ( str(e) )
        print ('testjson err: \n\n', dic["TestJson"])

```



## List

### delete_duplicates

```python
from collections import OrderedDict

def delete_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))
```



```
sum( list( map(lambda k: len( tests_segs[k] ), tests_segs) ) )
```



### Remove the value  first occur

a.remove(1)



## Set

```
list(set(a).intersection(set(b)))  # 交集  Or t & s
list(set(b).difference(set(a))) # 差集  Or t - s
t.union(s) # 并集 Or t | s  Or t ^ s
t.symmetric_difference(s) # 对称差集
```







## Dictionary

- map 一个字典会得到key



### Check if a given key already exists in a dictionary

```python
'key1' in dict  # will return True or False
```



## range



def listToDict(lst):
    op = { i: lst[i] for i in range(0, len(lst), 1)}
    return op



## String Template

new in Python 3
```python
print(f"{name} is {age} years old")
print (item, end=" ")
```




## Filter

[filter](https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000)

接受的函数是一参，函数返回True 就保留元素，否则丢弃

```python
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```

- filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list



## Regex



bool(re.match(r'\s+', '  '))   # 是否含空白符



## Sort

```python
sorted(trank_res, key=lambda x: x['index'], reverse=False)
```



## Numpy



### Initialize

```python
np.array([[2, 4, 6], [6, 8, 10]], np.int32)
np.zeros((3, 3))
np.ones((8, 1))
```



### Matrix Op

```
np.dot(W, TR) * 0.85 + C
```







## JSON

```python
# encoding=utf-8
import jieba
from __future__ import unicode_literals
import json
#import jsons
import pymysql
import decimal
import datetime

test_to_save_file = "test_from_mysql.json"
segs_test_file = "segs_test_from_mysql.json"

material_file = "5.json"  # 教材json
stopword_file = "stopwords.dat"

dic = {}

def jiba_segs(text):
    return list(jieba.cut(text,cut_all=False))

def listToDict(lst):
    op = { i: lst[i] for i in range(0, len(lst), 1)}
    return op

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

#按行读取文件，返回文件的行字符串列表
def read_file(file_name):
    fp = open(file_name, "r", encoding="utf-8")
    content_lines = fp.readlines()
    fp.close()
    #去除行末的换行符，否则会在停用词匹配的过程中产生干扰
    for i in range(len(content_lines)):
        content_lines[i] = content_lines[i].rstrip("\n")
    return content_lines

# 读停用词列表
stopwords = read_file(stopword_file)

with open(material_file, encoding='utf-8') as fh:
    js = json.load(fh)
    fh.close()

def word_frequency(seg_list):
    for w in seg_list:
        if (w not in stopwords) and (w in dic):
            dic[w] = dic[w] + 1
        elif w not in stopwords:
             dic[w] = 1
            
    # if dic.has_key():

    
    
def walk(j):
    if type(j) is list:
        if j == []:
            return
        for d in j:  # j is list, and list only has dicts
                if d["key"] != "" and d["key"] != "TEST111":
                    key = d["key"]
                    segs_key = list(jieba.cut(key,cut_all=False))
                    word_frequency(segs_key)
                    print (key, '----->', '|'.join( segs_key ) )
                if d["context"] != "" and d["context"] != "null": 
                    context = d["context"]
                    segs_context = list(jieba.cut(context,use_paddle=True))
                    print (context, '----->',  '|'.join( segs_context ) )
                walk(d['childs'])
    if type(j) is dict:
        if j["key"] != "" and j["key"] != "TEST111":
                print (j["key"])
        return walk(j['childs']) 

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
walk(js)
print (dic)


def conn():
    mydb=pymysql.Connect(host='',
                         port=3306,
                         user='',
                         password='',
                         db='',
                         charset='utf8', 
                         autocommit=True)
    return mydb.cursor(pymysql.cursors.DictCursor)

def db_exe(query,c):
    try:
        if c.connection:
            print("connection exists")
            c.execute(query)
            return c.fetchall()
        else:
            print("trying to reconnect")
            c=conn()
    except Exception as e:
        return str(e)

dbc=conn()

result_dics_list = load_json(test_to_save_file)
result_dics = listToDict(result_dics_list)

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

# 题目分词

new_seg_lst = []
for dic in result_dics_list:
    
    testjson = json.loads( dic["TestJson"], strict=False )
    
    if testjson["Type"] == 'ATEST':
        testjson["Title_segs"] = jiba_segs(testjson["Title"])
        for item in testjson["SelectedItems"]:
            item["Content_segs"] = jiba_segs(item["Content"])
        dic["TestJson"] = testjson


save_json(segs_test_file, result_dics_list)

print (result_dics_list[-1])

if dbc:
    if dbc.connection:
        try: 
            dbc.connection.close()
            print ('### db close success.')
        except Exception as e:
             print ( str(e) )
        
print (dbc.connection)



```





## UTF-8



```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import networkx as nx
import numpy as np
import math
import re
import os
import sys
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())  # python3的系统编码
print(sys.stdout.encoding)       # 标准输出的编码


adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)
G = nx.from_numpy_matrix(adjMat)
nx.draw(G, with_labels = True)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels = nx.get_edge_attributes(G,'weight'))
```





```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

import re
import jieba
import jieba.analyse
import jieba.posseg as pseg

def is_alpha(tok):
    try:
        return tok.encode('ascii').isalpha()
    except UnicodeEncodeError:
        return False


text = u'影响酶促反应速度的因素1.酶浓度 <br>2.底物浓度 <br>3.温度<br>4.酸碱度 <br>5.激活剂<br>6.抑制剂'

p2 = re.compile(ur'[^\u4e00-\u9fa5]') #中文的编码范围是：\u4e00到\u9fa5  
zh = " ".join(p2.split(text)).strip()                    
zh = "|".join(zh.split())  

# print zh

# text = [w for w in text if not is_alpha(w)]

print zh

'''

seg_list = jieba.cut(text, cut_all=True)
seg_list_tolist = list(seg_list)

# for w in seg_list_tolist:
    # print w


seg_list = jieba.cut(text, cut_all=True)
print("Full Mode: " + "|".join(seg_list))  # 全模式


for x, w in jieba.analyse.extract_tags(text, withWeight=True):
    print('%s %s %s' % (x, w, is_alpha(x)))

'''



#text = [w for w in text]


'''
if True:
    text = [w for w in text if not is_alpha(w)]
'''



'''
item = pseg.cut(text)
for i in list(item):
  print i.word


open('stopword.txt').readlines()

stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines() ]
'''

# print list(stop)



```



## Jupyter Notebook



```
python -m pip install --upgrade pip
pip install wheel
```



pip install jupyter

- pip install --user jupyter  出错就用这个



python -m jupyter notebook --version



python -m pip install -U matplotlib



Ctrl + Shift + P -> Python: Select interpreter

Ctrl + Shift + P -> Python: Select interpreter to start Jupyter server

Python: Select interpreter to start Jupyter server



**Ctrl+Shift+P** -> **Python: Create New Blank Jupyter Notebook**

> 注意大小写都要正确









```
python -m pip install -U matplotlib
```







# networkx plot graph



## 看权重和结点的图形


```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import networkx as nx
import numpy as np
import math
import re
import os
import sys
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())  # python3的系统编码
print(sys.stdout.encoding)       # 标准输出的编码


"""
此代码用于测试算法正确性
"""

adjacentMatrix = np.zeros((3, 3))
"""
	邻接矩阵 里面存的是相似度，相似度就是graph 中的边的权值
"""

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)

G = nx.from_numpy_matrix(adjMat)
# pos=nx.get_node_attributes(G,'pos')
pos = nx.spring_layout(G)
nx.draw(G, with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)

scores = nx.pagerank(G, **{'alpha': 0.85, })

print ( type(adjacentMatrix), type(adjMat) )
print (adjacentMatrix)
print (adjMat)
print (nx_graph)
print (scores)


```



## 看权重和结点的文本输出

```python
import networkx as nx
import numpy as np

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)
G = nx.from_numpy_matrix(adjMat)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
```

> {(0, 1): Text(0.36720620499242296, -0.46714047438761563, 
>
> "{'weight': 0.4}"), (0, 2): Text(-0.4999999999999998, 0.1325001701718984,
>
> "{'weight': 0.2}"), (1, 2): Text(0.13279379500757726, 0.3346403042157172, "{'weight': 0.1}")}







# Win10提升管理权限删除顽固文件

进入C:\Windows\System32文件夹下

找到cmd.exe 文件

右键-以管理员身份运行（重要）

输入：net user administrator /active:yes，开启超级管理员账号

win+r键打开运行对话框，输入 netplwiz ，重设administrator密码

重启-开始→切换账户→Administrator,就可以切换到管理员模式了。

重启后，屏幕上显示一个是本地用户、一个是administrator用户，这样可以来回切换。这样你找到要删除的文件或者文件夹就可以删除了

如果上面方法解决不了，试试下面这个---------电脑的安全模式。

点击开始，再点击设置，然后在设置页面点击“更新和安全“这一选项，再在左方的选项里面点击”恢复“，接着
在右边找到”高级启动“，并点击下方的”立即重新启动“，电脑将会重启进入高级启动，再点击“疑难解答”，
接着“高级选项”，再点击“启动设置”，最后店家右下方的“重启”，电脑将再次重启，并出现一个选择
界面，在选择里面找到“启用安全模式”并，按照提示点击相应的按键。就能进入安全模式了。
点击开始，再点击设置，然后在设置页面点击“更新和安全“这一选项，再在左方的选项里面点击”恢复“，接着
在右边找到”高级启动“，并点击下方的”立即重新启动“，电脑将会重启进入高级启动，再点击“疑难解答”，
接着“高级选项”，再点击“启动设置”，最后店家右下方的“重启”，电脑将再次重启，并出现一个选择
界面，在选择里面找到“启用安全模式”并，按照提示点击相应的按键。就能进入安全模式了。





## 完全卸载VSCode



> **注意**：以下步骤需要在执行 `VSCode` 自带卸载程序之后执行。

- `win + r` 打开运行
- %appdata% 回车
- 删除 `Code` 和 `Visual Studio Code` 文件夹
- 地址栏输入 %userprofile% 回车
- 删除 `.vscode` 文件夹



### 错误提示和格式化

Python 默认的语法提示工具是 PyLint，也可以选择其他的 linter 工具，比如 flake8。flake8 是 Python 官方发布的一款静态代码检查工具，如果想使用它的话首先在 Anaconda 的命令行工具中用 `pip install flake8` 安装；另外，在保存代码的时候 VSCode 可以自动进行 code formatting ，这个功能默认是关闭的且工具是 autopep8 , 如果想使用 yafp，则继续在命令行工具中用命令 `pip install yapf` 安装。 安装好这两个工具之后在 VSCode 的配置文件中进行设置：

```text
"python.linting.enabled": true
"python.linting.flake8Enabled": true,
"python.formatting.provider": "yapf"
```





# networkx plot graph



## 看权重和结点的图形


```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import networkx as nx
import numpy as np
import math
import re
import os
import sys
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())  # python3的系统编码
print(sys.stdout.encoding)       # 标准输出的编码


"""
此代码用于测试算法正确性
"""

adjacentMatrix = np.zeros((3, 3))
"""
	邻接矩阵 里面存的是相似度，相似度就是graph 中的边的权值
"""

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)

G = nx.from_numpy_matrix(adjMat)
# pos=nx.get_node_attributes(G,'pos')
pos = nx.spring_layout(G)
nx.draw(G, with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)

scores = nx.pagerank(G, **{'alpha': 0.85, })

print ( type(adjacentMatrix), type(adjMat) )
print (adjacentMatrix)
print (adjMat)
print (nx_graph)
print (scores)


```



## 看权重和结点的文本输出

```python
import networkx as nx
import numpy as np

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)
G = nx.from_numpy_matrix(adjMat)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
```

> {(0, 1): Text(0.36720620499242296, -0.46714047438761563, 
>
> "{'weight': 0.4}"),
>
> 
>
> (0, 2): Text(-0.4999999999999998, 0.1325001701718984,
>
> "{'weight': 0.2}"),
>
> 
>
> (1, 2): Text(0.13279379500757726, 0.3346403042157172, "{'weight': 0.1}")}



[

[0.  0.4 0.2],

[0.4 0. 0.1],

 [0.2 0.1 0. ]

]



https://reference.wolfram.com/language/GraphUtilities/ref/PageRanks.html

https://www.mathworks.com/help/textanalytics/ref/textrankscores.html

https://github.com/YevaGabrielyan/tldl





## Sublime Text 3

> Tools>Build System menu ->new build system
>
> 
>
> {
>
>   "shell_cmd": "node ${file}"
>
> }
>
> 
>
> build
>
>   command + b
>
> 
>
> module.paths.push('G:/Users/w7/AppData/Roaming/npm/node_modules');
>
> 
>
> {
>
> ​	"shell_cmd": "python3 -u ${file}"
>
> }



# Flask

```python
from flask import Flask, request, jsonify
import os,sys
sys.path.append(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))  # std 包在此模块的上级目录
import std.iJson as iJson

app = Flask(__name__)

# http://localhost:666/frequencyStatistics
# request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据
# request.json 的类型直接就是dict
@app.route('/frequencyStatistics', methods=['post'])
def frequencyStatistics():
    print(request.json, type(request.json))
    return jsonify(iJson.parse("[1,2,3]"))
https://blog.csdn.net/weixin_36380516/java/article/details/80008496
```



## Post 



```python
# -*- coding: utf-8 -*-
from flask import request, jsonify, json, Module
import logging
from web.utils.consts import POST, GET
from web.db.dbSession import DBManager
from web.db.models import Class

NAMESPACE = 'student'
student = Module(__name__, NAMESPACE)


@student.route('/add', methods=[POST])
def student_add():
    # request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据：对应图1
    # json.loads(request.dada) 能够同时接受方法为POST、Body为 raw类型的 Text 
    # 或者 application/json类型的值：对应图1、2
    params = request.json if request.method == "POST" else request.args
    try:
        session = DBManager.get_session()
        c = Class(name=params['name'])
        session.add(c)
        session.commit()
        session.close()
    except Exception, e:
        logging.exception(e)
    return jsonify(code=200, status=0, message='ok', data={})

```









