

[TOC]



# Python 3  Summary



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



## Exception

```python
    try:
        json.loads( dic["TestJson"], strict=False )
    except Exception as e:
        print ( str(e) )
        print ('testjson err: \n\n', dic["TestJson"])

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

