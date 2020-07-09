

[TOC]

# Python 3  Summary



VSCode   Alt + <-     Alt +   ->   前跳  回跳

F11 切换全屏



## Source install on CentOS

[How to Install Python 3.8 on CentOS 8](https://linuxize.com/post/how-to-install-python-3-8-on-centos-8/)



```
yum update -y
yum groupinstall -y 'Development Tools'
yum install -y gcc libffi-devel bzip2-devel expat-devel gdbm-devel \
ncurses-devel openssl-devel readline-devel \
sqlite-devel tk-devel xz-devel zlib-devel wget
```

```
VERSION=3.8.3
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz
tar -xf Python-${VERSION}.tgz
cd Python-${VERSION}
./configure --enable-optimizations
make -j 4
sudo make altinstall 
# Please do not use the standard make install as it-
# will overwrite the default system python binary.
python3.8 --version
pip3.8 --version
```



```
# Creating a Virtual Environment
# First, create the project directory and switch to it:
mkdir ~/flask_server && cd ~/flask_server
python3.8 -m venv server_venv
source server_venv/bin/activate  # 激活临时python 环境
python --version
pip --version
deactivate # 关闭临时python 环境
```

```
pip list
pip show jieba
```



```
python -m pip install --upgrade pip
pip install wheel
pip install jupyter
- pip install --user jupyter  出错就用这个
python -m jupyter notebook --version
python -m pip install -U matplotlib
```



## 优化



[Python编写循环的两个建议](https://zhuanlan.zhihu.com/p/68128557)

- “pythonic way”的方式来搜“地道”的写法，貌似stackoverflow上面讨论的多一些

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



#### CPU执行时间

```python
import time
tis1 =time.perf_counter()
print("等待5秒......")
time.sleep(5)
tis2=time.perf_counter()
print(tis2-tis1)
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



## OP



### logic



```python
if x is not None
a-b if a>b else a+b
```





## 静态函数 构造函数 析构函数

```python
 @staticmethod
 def connect():
 
 def __init__(self):
 def __del__(self):
```



## 当前函数名

```python
 print(sys._getframe().f_code.co_name)
 print(inspect.stack()[0][3])
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



## For



```python
 [x for x in range(11) if x%2 == 0]
 len([ k for k, _ in tasks.items()]) # 现有总任务数
```



## Filter



```python
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
list(filter(lambda w: not bool(re.match(r'[^\u4e00-\u9fa5]', w)), words)) # 过滤非中文词
{k: v for k, v in points.items() if v[0] < 5 and v[1] < 5}
lambda 返回true 的保留
```



## List



###  iterate with index



```python
for i, name in enumerate(names):
    print(i, name)
```



product 笛卡尔集



### delete_duplicates



```python
from collections import OrderedDict

def delete_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))
```



```
sum( list( map(lambda k: len( tests_segs[k] ), tests_segs) ) )
```



### ordering



```python
sorted(results, key=lambda l: l[3], reverse=True) # 按相似度高到低排序
```



### remove the value  first occur

a.remove(1)



### join as string



```python
l = ['1','2','3']
print(",".join(l))
```



### convert list to dict

```
def listToDict(lst):
    op = { i: lst[i] for i in range(0, len(lst), 1)}
    return op
```



### subtract

- list - list 是相同position 的值分别相减，构成一个新list

	if sum( WS - last_WS ) < 1e-12:  # 提前结束计算，如果误差值小于一定值
		print('break loop now. current iterate num: ', k+1, 'deviation sum is:', sum( WS - last_WS ))
		break



#### mean image

```
X -= np.mean(X, axis=0)  # 减去均值
```



### transpose

```python
np.transpose(arr)
```



### dot

```python
A = np.dot(X, W) + b
```



### flatten



```python
import itertools
list(itertools.chain(*abs(E)))
```



### sublist

```
def subLists(l, n):
    return [ l[i:i + n] for i in range(0, len(l), n)  ]
print( subLists(l, 0) )
```



### shape



```python
m = X.shape[0] # 样本数
```





### parallel



```python
from joblib import Parallel, delayed
def parallelCompare(func, l):
    def f(l, i):
        rs = []
        for j in range(i+1, len(l)):
            rs.append( (i, j) )
        return rs
    return Parallel(n_jobs=os.cpu_count(), verbose=10)(delayed(f)(l, i) for i in range(len(l)-1))
```







## Tuples

```
a, b = b, a 等价于 (a, b) = (b, a), list 没有这模式匹配特性
```

```
return 1 if probably >= 0.5 else 0, probably
```



### immutable

tuple对象不可改变



### hashable 

tuple 是hashable 类型（取决于里面放什么），所以tuple可以做dict的key



tuple还用来返回多值

> x, y = getPoint()



### tuple efficient than list

tuple以放弃对元素的增删为代价换取了性能上比list 更高的优点





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



### for k, v 



```python
for k, v in d.items():
```



###  Get first value



```python
list(d.values())[0]
tmp = sorted(tmp, key=lambda d: list(d.values())[0], reverse=True) # 按词频高到低排序
```



### Order



```python
    # 通过构造有序字典，根据词频排序
    for cptid in results:
        d = results[cptid]
        tmp = []
        for k, v in d.items():
            tmp.append({k:v})
        tmp = sorted(tmp, key=lambda d: list(d.values())[0], reverse=True) # 按词频高到低排序
        orderDic = collections.OrderedDict()
        for dd in tmp:
            for k, v in dd.items():
                orderDic[k] = v
        results[cptid] = dict( orderDic)
```





## Str



### raw string

```\
r''
```







### split string into list of characters

```
list(str)
```



### strip



```python
line.strip().split('\t')
```





### remove whitespace

```python
re.sub(r"\s+", "", astr, flags=re.UNICODE)
```



### remove not chinese

```python
def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)
```



```python
# 移除非中文、26个英文字母以外的字符
def unAZchinese_remove(s):
   return re.sub(r"[^\u4e00-\u9fa5^a-z^A-Z^0-9]", "", s, flags=re.UNICODE)
```





```python
class mydict(dict):
      def __str__(self):  # how to convert to string
          return json.dumps(self)
```



```python
要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
```





## Range



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
list(filter(lambda w: not bool(re.match(r'[^\u4e00-\u9fa5]', w)), words)) # 过滤非中文词
{k: v for k, v in points.items() if v[0] < 5 and v[1] < 5}
```

- filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list



## Regex

https://zhuanlan.zhihu.com/p/42944600

bool(re.match(r'\s+', '  '))   # 是否含空白符



### compile

```python
pattern = re.compile(r'\[.+?\.gif\]') # .+? 最短匹配
print( pattern.findall('β[XB3.gif]肾上腺素受体激动剂\xa0') )
```





### .匹配换行

```
re.DOTALL
```





### ? 最短匹配

```
ss =  re.findall(r'(@@第[一二三四五六七八九十]+章.+?)\n', strs, re.DOTALL)
```



### ^ not ^ at the begin



[^】]*?  不是字符】，重复0或多次，最短匹配

^ 是“在开始”，如果放在最前面

$ 是“在结尾”，如果放在最后面



```
print( re.compile(r'(【[^】]*?)(【[^】]*?】)([^【]*?】)(.*?\n)').sub(ps2[1][1], "【大剂量】常出现在【血清地高辛浓度【＞2ng/ml】】时，\n") )
```





```python
[^a-z]
So to match a string that does not contain "y", the regex is: ^[^y]*$

Character by character explanation:

^ means "beginning" if it comes at the start of the regex. Similarly, $ means "end" if it comes at the end. [abAB] matches any character within, or a range. For example, match any hex character (upper or lower case): [a-fA-F0-9]

* means 0 or more of the previous expression. As the first character inside [], ^ has a different meaning: it means "not". So [^a-fA-F0-9] matches any non-hex character.

When you put a pattern between ^ and $, you force the regex to match the string exactly (nothing before or after the pattern). Combine all these facts:

^[^y]*$ means string that is exactly 0 or more characters that are not 'y'. (To do something more interesting, you could check for non-numbers: ^[^0-9]$
```







### 捕获



捕获和非捕获属性 https://blog.csdn.net/Leonard_wang/article/details/79813425





### finditer 所有匹配的开始结束位置 

```
iters = re.finditer(r'[ab]', "abc", re.DOTALL)
poss =  [ i.span() for i in iters ]
```



```
ss =  re.findall(r'(@@第[一二三四五六七八九十]+章.+?)\n', strs, re.DOTALL)
iters = re.finditer(r'(@@第[一二三四五六七八九十]+章.+?)\n', strs, re.DOTALL)
poss =  [ i.span() for i in iters ]
for pos in poss:
    (start, end) = pos
    print(start, end)
    print (strs[start:end])
```



```
# 输入字符串，标题正则
# 返回标题、标题位置(strat, end), 标题下的文本
def extractPattern(strs, reg):
    #ss =  re.findall(reg, strs, re.DOTALL)
    iters = re.finditer(reg, strs, re.DOTALL)
    poss =  [ i.span() for i in iters ] # 标题positions
    rs = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        title = strs[start:end]
        contents = None
        if i == ( len(poss) - 1 ):
            contents = strs[ end : len(strs) ]
        else:
            contents = strs[ end : poss[i+1][0] ]
        rs.append( [ start, end, title, contents ] )

    return rs
```



### replace



```python
ps_text_summary.replace("【】","")
```



两层括号展平

```
print( re.compile(r'(【[^】]*?)(【[^】]*?】)([^【]*?】)(.*?\n)').sub(r'\1】\2【\3\4', "【a【b】c】d\n") )
-> 【a】【b】【c】d
```



```

notlr = r"([^【^】]*?)" # 非左非右，最短匹配

left = r'(【[^】]*?)'
midle = r'(【[^】]*?】)'
right = r'([^【]*?】)'
end = r'(.*?\n)'

# 注意依赖顺序，注释掉前面后面就可能不正确
# not perfect but can use
ps2 = [
        (r'(【[^】]*?)(【[^】]*?)(【[^】]*?】)([^【]*?】)([^【]*?】)(.*?\n)', r'\1】\2】\3【\4【\5\6'),  # 先把三个括号的展平了
        (r'(【[^】]*?)(【[^】]*?】)([^【]*?】)(.*?\n)', r'\1】\2【\3\4'),                                # 再把两个括号的展平
        ( left + midle + notlr + midle + right + notlr + end, r'\1】\2\3\4【\5\6\7' ),                   # 处理多层嵌套 "【a【b】c【d】e】f\n"
        (r"(【)(【[^】]*?】)(.+?)(】)(.*?)(\n)", r"\1】\2【\3】【\4【\5】\6"),
        (left+midle+notlr+midle+notlr+midle+right+notlr+end, r'\1】\2【\3】\4【\5】\6【\7【\8】\9'),
        (left+midle+notlr+midle+notlr+midle+notlr+midle+right+notlr+end, r'\1】\2【\3】\4【\5】\6【\7】\8【\9【\10】\11')
    ]
```









```
echo 'the blue dog and blue cat wore blue hats' | sed 's/blue \(dog\|cat\)/gray \1/g'
->the gray dog and gray cat wore blue hats
```



#### named groups



```
p = re.compile(r'blue (?P<animal>dog|cat)')
p.sub(r'gray \g<animal>','the blue dog and blue cat wore blue hats')
```



```
re.sub(
    pattern=r'(\d)(\w+)', 
    repl='word: \\2, digit: \\1', 
    string='1asdf'
)
```



```
p.sub('gray \g<1>',s)
```



```python
print ( re.sub(
    pattern=r'【【(【.+?】)】】(.*?)\n', 
    repl=r'\1\2', 
    string='【【【aa】】】bb【【【cc】】】dd【【ee】【ff】】\n'
) )
-> 【aa】bb【【【cc】】】dd【【ee】【ff】】

print ( re.sub(
    pattern=r'(【【(【.+?】)】】)(.*?)(\n)', 
    repl=r'\1\4\2\4\3', 
    string='【【【aa】】】bb【【【cc】】】dd【【ee】【ff】】\n'
) )
大外层是1 内层是2 其他是3
```



```
match = re.match(r"(?P<all>(?:-(?P<one>\w+))*)","-ab-cde-fghi-jkl-mn")
>>> re.findall(r"-(?P<one>\w+)", match.group("all"))
['ab', 'cde', 'fghi', 'jkl', 'mn']
```





```
re.match(r"(?:aaa)(_bbb)", string1).group(1)
result = re.sub(r"(\d.*?)\s(\d.*?)", r"\1 \2", string1)
```





```
pattern = re.compile(r'\[.+?\.gif\]') # .+? 最短匹配
print( pattern.findall('β[XB3.gif]肾上腺素受体激动剂\xa0') )
print( pattern.sub('', 'β[XB3.gif]肾上腺素受体激动剂\xa0') )  #替换成空串
```



```
ps= [
        ( r'\[.+?\.gif\]', "" ),  # pattern 和需要替换成为的串
    ]
"""
需要替换的pattern
"""

# 递归批量替换字符串
def replaceall(strs, ps, idx):
    if strs.strip() == "":
        return ""
    if (idx > len(ps) - 1):
        return strs.strip()

    (p, s) = ps[idx]
    pattern = re.compile(p)
    strs = pattern.sub(s, strs)
    return replaceall(strs, ps, idx + 1)
```







### subString

```
str = ’0123456789′
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取，具体啥意思没搞明白？
```



### escape

re. escape( )





## Sort

```python
sorted(trank_res, key=lambda x: x['index'], reverse=False)
```



## Numpy



### shape

```python
print (inputs.dtype, inputs.shape, expected_output.shape)
```



### Initialize

```python
np.array([[2, 4, 6], [6, 8, 10]], np.int32)
np.zeros((3, 3))
np.ones((8, 1))
np.full(shape, fill_value, dtype=None, order='C')
np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
```



### reshape

```
a1 = x.reshape(x.shape[0], 1) # Getting the training example as a column vector.
```





### matrix op

```
np.dot(W, TR) * 0.85 + C
```







## System



### stdout

```
sys.stdout.flush() # Updating the text.
sys.stdout.write("\rIteration: {} and {}".format(i + 1, j + 1))
```



## Multiprocessing 



Python 界有条不成文的准则： 计算密集型任务适合多进程，IO 密集型任务适合多线程

> 通常来说多线程相对于多进程有优势，因为创建一个进程开销比较大，然而因为在 python 中有 GIL 这把大锁的存在，导致执行计算密集型任务时多线程实际只能是单线程。而且由于线程之间切换的开销导致多线程往往比实际的单线程还要慢，所以在 python 中计算密集型任务通常使用多进程，因为各个进程有各自独立的 GIL，互不干扰。
>
> 而在 IO 密集型任务中，CPU 时常处于等待状态，操作系统需要频繁与外界环境进行交互，如读写文件，在网络间通信等。在这期间 GIL 会被释放，因而就可以使用真正的多线程。



[进程池的同步与异步用法Pool](https://blog.csdn.net/aaronthon/article/details/83422749)

```python
print(os.cpu_count())
from multiprocessing import cpu_count
print(cpu_count)
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
import sys
import os

# Version 1.0
# 需要配合 EBWin4 使用，词典分组需要设置好


def output(o):
    fullstr = '<meta charset="utf-8">'
    for l in o:
        fullstr += l
    # print(fullstr)
    sys.stdout.buffer.write(fullstr.encode('utf-8'))


s = sys.argv[1].strip()
# s = "organon"

result = os.popen(
    '"C:\Program Files (x86)\EBWin4\ebwinc.exe" /G=KL /C=1 /O=h ' + s).readlines()
output(result)
```



```
如果用的是 Windows 系统的话，可以参考我的帖子： [GoldenDict] GoldenDict 的下载、安装、使用[Windows] https://www.pdawiki.com/forum/fo ... hread&tid=14072# p( C0 a6 ]% n1 ~; r
几个关键点：6 s6 H1 L; [% E% E
1. 官网下载的GoldenDict 是不支持 EPWING 格式的，要从 http://sourceforge.net/projects/ ... %20access%20builds/ 这里下载最新版；% K% e- e% ?, t) ^) Y
2. 把 EPWING 词典文件放在 content 文件夹下；9 _: E; O" Z5 p) M/ `* }
3. 第一次打开 GoldenDict 时，迅速地前往【编辑】->【首选项】->【全文搜索】，关闭“全文搜索”（也就是如果有勾的话，就是把前面的勾去掉）！！！9 p/ N# O/ q: M3 t( e9 X
4. GoldenDict 对 EPWING 支持有些小问题的。
5. 关于单独字体指定，参考：[GoldenDict] 如何为某部词典指定字体？ https://www.pdawiki.com/forum/fo ... hread&tid=15900
```





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



```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
# Convert ShiftJIS to UTF-8
# Usage: cat ShiftJIS.txt | ./convert.py > UTF8.txt
# Alternative method: cat ShiftJIS.txt | iconv -f shift_jis -t utf8 > UTF8.txt
 
import sys
import codecs
 
ustdout = codecs.getwriter('utf_8')(sys.stdout)
jstdin = codecs.getreader('shift_jis')(sys.stdin)
 
for line in jstdin.readlines():
ustdout.write(line)


cat 学研国語大辞典ku00.txt | iconv -f SHIFT_JIS-2004 -t utf-8 > 学研国語大辞典ku00-utf8.txt
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
pip install sklearn
```







## networkx plot graph



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







## Win10提升管理权限删除顽固文件

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





## networkx plot graph



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



## Flask

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



## Mysql



### Insert into



```
f"INSERT INTO trialexampointrelevanttest (examPointID, appID, testID, childTestID, isMachine, similarity ) VALUES ({examPointID}, {appID}, {testID}, {childTestID}, 1, {similarity} ) ON DUPLICATE KEY UPDATE similarity={similarity}, updateTime=now();"

```





## Excel



```python
import pandas as pd
seg = pd.DataFrame(wordlist,columns=['word','length','fre','pmi','entropy'])
seg.to_csv(fname_results, index=False ,encoding="utf-8")
```







