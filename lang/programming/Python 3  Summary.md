

[TOC]

# Python 3  Summary



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

## Dictionary



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




# Filter

[filter](https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000)

```python
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```

- filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list



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

