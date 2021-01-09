



[TOC]

# Python 3  Summary



VSCode   Alt + <-     Alt +   ->   前跳  回跳

F11 切换全屏



## Anaconda [u](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

```bash
conda config --set auto_activate_base true
```

```bash
conda create -n tensorflow_cpu pip python=3.6
conda activate tensorflow_cpu
conda install pytorch-cpu==1.0.0 torchvision-cpu==0.2.1 cpuonly -c pytorch
pip install stanfordnlp
pip install tensorflow==1.15
conda deactivate
conda info -e
conda env remove -n tensorflow_cpu

python -m spacy download en
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
nlp = spacy.load("en_core_web_sm")
```

pip install tensorflow==1.12 -i https://pypi.tuna.tsinghua.edu.cn/simple

```
install_requires=['numpy', 'tensorflow-gpu==1.12', 'tensorflow-hub', "tqdm", "spacy", "jieba",
                        "stanfordnlp"],
```



**基于论文的实现**  [u](https://github.com/17zuoye/pyirt)

- IRT Parameter Estimation using the EM Algorithm By Brad Hanson 2000

  - Github 实现 [u](https://github.com/17zuoye/pyirt/blob/master/pyirt/solver/model.py)

    > **创建环境**
    >
    > conda create -n irt  python=3.8
    >
    > conda activate irt
    >
    > cd ~/pyirt-master
    >
    > pipenv --three
    > make
    >
    > pipenv shell
    >
    > **使用环境**
    >
    > conda activate irt
    >
    > cd ~/pyirt-master
    >
    > pipenv shell





## Source install on CentOS

[How to Install Python 3.8 on CentOS 8](https://linuxize.com/post/how-to-install-python-3-8-on-centos-8/)



```python
yum update -y
yum groupinstall -y 'Development Tools'
yum install -y gcc libffi-devel bzip2-devel expat-devel gdbm-devel \
ncurses-devel openssl-devel readline-devel \
sqlite-devel tk-devel xz-devel zlib-devel wget
```

```python
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



```python
pm2 start run.sh
pm2 restart id --name assist 
```





```
python -m pip install --upgrade pip
pip install wheel
pip install jupyter
- pip install --user jupyter  出错就用这个
python -m jupyter notebook --version
python -m pip install -U matplotlib
```



### 使用临时源

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple panda
```



## Julia



**高斯求积简介** [u](https://discourse.juliacn.com/t/topic/1024) [u2](GitHub\doc\lang\programming\高斯求积简介.pdf)



```python
>pip3 install pycall # for julia to using sympy package

from sympy import  integrate ,cos,sin
from sympy.abc import  a,x,y

print( integrate(sin(x)/x,(x,-float("inf"),float("inf"))) ) # 积分结果是pi
print( integrate(1+15*x+2*x**2+12*x**3,(x,float(-1),float(1))) ) # 3.333
```



```julia
# 全程开全局代理 Proxifier
julia>import Pkg; Pkg.add("SymPy")
julia>using SymPy
julia>sympy.sqrt(3)

# vscode
using SymPy
x = symbols("x")
println( integrate(sin(x)/x, (x, -oo, oo)) )
println( integrate(1+15*x+2*x^2+12*x^3, (x, -1.0, 1.0)) )

```





## 绘图的重要参考

### 深入理解神经网络：从逻辑回归到CNN.md

GitHub\doc\lang\programming\深入理解神经网络：从逻辑回归到CNN.md



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



```python
import sys
sys.path.append('../..')
import jieba
import std.seg.iSeg as iSeg

print(iSeg.segment('苯巴比妥显效慢的主要原因是脂溶性较小'))
```



### args parse  [u](https://github.com/jplalor/py-irt)

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--num-epochs', default=1000, type=int)
parser.add_argument('--gpu', action='store_true')
parser.add_argument('--priors', help='[vague, hierarchical]', default='hierarchical')
parser.add_argument('--model', help='[1PL,2PL(coming soon)]', default='1PL')  # 2pl not implemented yet
args = parser.parse_args()

device = torch.device('cpu')
if args.gpu:
    device = torch.device('cuda')
    
for name in pyro.get_param_store().get_all_param_names():
    print(name)
    val = pyro.param(name).data.numpy()
    print(val)
    if name == 'loc_diff':
        print('mse: {}'.format(np.mean((val - real_diff) ** 2)))
    elif name == 'loc_ability':
        print('mse: {}'.format(np.mean((val - real_theta) ** 2)))    
```







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
currDir = os.getcwd() # 兼容jupyter 
currDir = os.path.dirname(os.path.abspath(__file__)) # 不兼容jupyter
os.path.abspath(__file__)                   # current file
os.path.dirname(os.path.abspath(__file__))  # current file directory
os.path.dirname(os.path.abspath(__name__))  # ?? directory
```

## File



```python
f = file('data/lsat.csv')
score = np.loadtxt(f, delimiter=",")
```



```python
import re
import glob

# 语料生成器，并且初步预处理语料
# 这个生成器例子的具体含义不重要，只需要知道它就是逐句地把文本yield出来就行了
def text_generator():
    txts = glob.glob('/root/thuctc/THUCNews/*/*.txt')
    for txt in txts:
        d = open(txt).read()
        d = d.decode('utf-8').replace(u'\u3000', ' ').strip()
        yield re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z ]+', '\n', d)
 # https://kexue.fm/archives/6920
```

```python
def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)
```



递归遍历

```python
xmls = glob.glob('./db/economist/**/article.xml', recursive=True)
for xml in xmls:
	with open(xml, "r", encoding="utf-8") as fp:
		data = fp.read()
```





### basename

```python
os.path.basename
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

```python
# -*- coding: utf-8 -*-
from .util import *
```

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



## 语法

```python
# 换行写法
def _lik(scores, p_val):
    # 似然函数
    loglik_val = np.dot(np.log(p_val + 1e-200), scores.transpose()) + \
                    np.dot(np.log(1 - p_val + 1e-200), (1 - scores).transpose())
    return np.exp(loglik_val)
# GitHub\doc\lang\programming\algo\EM.py
```



### Class

#### 属性

```python
class EAPIrt2PLModel(object):

    def __init__(self, score, slop, threshold): # 得分，区分度，阀值
        self.x_nodes, self.x_weights = get_gh_point(21)
        z = Z(slop, threshold, self.x_nodes)
        p = P(z)
        self.lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1) 
        """
        计算所有元素的乘积，按行连乘(维度变成n*1)。
        如果不指定轴，则不管是几维都展平成一维然后连乘
        """

    @property
    def g(self):
        x = self.x_nodes[:, 0]
        weight = self.x_weights[:, 0]
        return np.sum(x * weight * self.lik_values)

    @property
    def h(self):
        weight = self.x_weights[:, 0]
        return np.sum(weight * self.lik_values)

    @property
    def res(self):
        return round(self.g / self.h, 3)
```







## OP



### logic



```python
if x is not None
a-b if a>b else a+b
```



### round

```python
round(2.145,2) # 四舍六入五成双 # 它的作用是让统计数据更公平，降低舍入的误差
> 2.15 # 保留两位小数
```



### sigmoid



输入正数，值域在0.5 ~ 1 之间

  $h(x)=\frac{1}{1+e^{-x}}$

```python
exp(-x)
```



### log

```python
np.log(x) 以e为底的对数(自然对数)
np.log10(x) 以10为底的对数
np.log2(x) 以2为底的对数
np.log1p(x) 等价于：np.log(x + 1)
备注：np.expm1(x) 等价于 np.exp(x) - 1，也是np.log1p(x)的逆运算。
```

```
math.pi：圆周率，值为3.141592653589793.
math.e：自然对数，值为2.718281828459045.
math.inf：正无穷大，负无穷大为-math.inf.
math.nan：Not a Number，非正常值
```







## 递归方法



```python
#  收集所有Childs 的大纲outline，挂到结点下
def collectAllChildsOutline(tree):

    def walk(d, father, cur, maxIter):
        if cur > maxIter:
            return

        if "Childs" not in d:  # 叶子结点，给它的父数组贡献大纲
            if "Outlines" not in father:
                father["Outlines"] = []
            if "level" in d:
                if d["level"] != '-':
                    father["Outlines"].append(replaceOutline(d["level"])) # 父数组加子结点大纲

        if "Childs" in d:                    # 非叶子结点
           for dd in d["Childs"]:            # 遍历孩子
               walk(dd, d, cur+1, maxIter)   # 递归孩子
               if "Outlines" not in d:       # 递归结束后，叶子结点的上一层已经有了大纲
                    d["Outlines"] = []       # d  是当前非叶子
               if "Outlines" in dd:          # dd 是当前非叶子的孩子
                    if "level" in dd and dd["level"] != '-':        # 如果当前孩子有大纲 
                        d["Outlines"] += [ replaceOutline(dd["level"]) ] + dd["Outlines"]   # 当前非叶子大纲数组  加上  当前孩子大纲，当前孩子大纲数组
                    else:                    # 如果当前孩子无大纲
                        d["Outlines"] += dd["Outlines"]                     # 当前非叶子大纲数组  加上  当前孩子大纲数组
    for d in tree:
        walk(d, d, 1, 5)
    
    return tree
```







## 静态函数 构造函数 析构函数

```python
 @staticmethod
 def connect():
 
 def __init__(self):
 def __del__(self):
```



## 变长参数

> *args 与 **kwargs 的区别，两者都是 python 中的可变参数：
>
> - *args 表示任何多个无名参数，它本质是一个 tuple
> - **kwargs 表示关键字参数，它本质上是一个 dict
>
> 如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前。
>
> ```python
> >>> def fun(*args, **kwargs):
> 	print('args=', args)
> 	print('kwargs=', kwargs)
> args= (1, 2, 3, 4)
> kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
> ```

> a, b, *c = 0, 1, 2, 3  
>
> --> c  
>
> [2, 3]



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
sorted(results, key=lambda l: l[3], reverse=True) # 按相似度高到低排序
list(filter(lambda w: not bool(re.match(r'[^\u4e00-\u9fa5]', w)), words)) # 过滤非中文词
{k: v for k, v in points.items() if v[0] < 5 and v[1] < 5}
lambda 返回true 的保留
```



## List



### range



```python
list( range(5, 0, -1) )  # begin, stop, step
[5, 4, 3, 2, 1]
```





### Map

```python
__version_info__ = (0, 1, 1, 0)
__version__ = '.'.join(map(str,__version_info__))
```



###  iterate with index



```python
for i, name in enumerate(names):
    print(i, name)
```



### slice

```python
To slice a list, there's a simple syntax: array[start:stop:step]
You can omit any parameter. These are all valid: array[start:], array[:stop], array[::step]
```



```python
x = x_nodes[:, 0] # 行全要,列只要第0列.结果是二维变一维
# (11,1) -> (11,)
```





product 笛卡尔集



### delete 

```python
        for t, l in tests_segs.items():  # t: 'BTEST', 'XTEST'，l: [ {'ChildTestID': '27001584'...} ]
            removes = []
            for i in range(len(l)):
                d = l[i]
                key = f"{d['TestID']},{d['ChildTestID']}"
                if key in dicDup:
                    removes.append(i)  # 记录待删除的项
            print('before del: ', len(l))
            for i in sorted(removes, reverse = True):  # 排序，从后面开始删起。前面的索引是不会变的
                del l[i]
            print('after del:', len(l))
```





### delete_duplicates



```python
from collections import OrderedDict

def delete_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))
```



```
sum( list( map(lambda k: len( tests_segs[k] ), tests_segs) ) )
```



### copy

```python
import copy
tests_segsNew = copy.deepcopy(tests_segs)
```





### ordering



```python
sorted(results, key=lambda l: l[3], reverse=True) # 按相似度高到低排序

math.log(len(arr[6])) # 可以近似认为后一项的值域是 [0, 10]

```



```python
index = np.sort(np.intersect1d(rt[N-2], pp2.index)) # 作交集
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



### intersect

```python
index = np.sort(np.intersect1d(rt[N-2], pp2.index)) # 作交集
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



### trick

```python
def weights_replaceinto(ls):
    sqls = []
    for d in ls:
        columns = ",".join( list(d.keys()) )
        values = ",".join( ( map(lambda w: r"'" + w + r"'" ,list(d.values()) ) ) )
        sqls.append(f"INSERT INTO weights ({columns}) VALUES({values}) ON DUPLICATE KEY UPDATE updateTime=now();")
```



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
d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = sorted(d.items(), key=lambda x: x[1])    
print(a)
```





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



### Max value

```python
dic={0: 1.4984074067880424, 1: 1.0984074067880423, 2: 1.8984074067880425, 3: 2.2984074067880425, 4: 2.2984074067880425}
max_value = max(dic.values())  # maximum value
max_keys = [k for k, v in dic.items() if v == max_value] # getting all keys containing the `maximum`

print(max_value, max_keys)
```



### 递归生成知识点目录

```python

import os, sys; sys.path.append( os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) )  # std 包在此模块的上上上级目录
import math
import std.iFile as iFile
import std.iJson as iJson
import std.iList as iList
#import std.seg.iSeg as iSeg
import std.iSql as iSql
import util.saveTempData as saveTempData
import util.fectchData as fectchData

#from reg import inverseQuestionQ
#from optimization import similarOfSentsWithMedWords
#from optimization import medWords

import pandas as pd
import re

appid = 16629

# SELECT * from appinfo a WHERE a.AppEname = 'ZC_ZGHS_YTMJ_TEST';
# 16629  ZC_ZGHS_YTMJ_TEST  2020版主管护师考试宝典(护理学)特训密卷［专业代码：368］

"""

查出所有根结点
    SELECT ID AS menuID, PID, `name` FROM trialexampointmenus ts WHERE ts.appid = 16629 AND ts.`enable` = 1 AND ID IN (13394,15859,17852,19629,21271,22383,22660,22897);
        # 本来条件应该是 PID == -1, 但是根结点有很多重复，所以指定了ID

得到根结点再递归遍历它们的子结点


TODO:
    构造两颗树
        1. 基于trialexampointmenus 表的知识点目录树
        2. 基于护理学（中级）大纲.xls 导出文本的目录树
    
    对比两颗树，找出需要掌握的熟练度   


Pandas处理Excel - 复杂多列到多行转换（三十八）
https://blog.csdn.net/qq_41706810/article/details/106042694

Pandas | 表格整合三大神技之CONCATENATE
https://zhuanlan.zhihu.com/p/24892205


SELECT ID AS menuID, PID, `name` FROM trialexampointmenus ts WHERE ts.appid = 16629 AND ts.`enable` = 1;

PID = -1 的是root, 否则它的father 是menuID = 它的PID 的结点

"""

rootids = [13394,15859,17852,19629,21271,22383,22660,22897]

def addChilds(menus, rootnode):
    def add(menus, node, cur, maxIter):
        if cur > maxIter:
            return
        mid = node["menuID"]
        for d in menus: 
            if d["PID"] == mid:
                if "Childs" not in node:
                    node["Childs"] = []
                newd = d.copy()
                node["Childs"].append(newd)
                add(menus, newd, cur+1, maxIter)

    add(menus, rootnode, 1, 5)

def menuTree(menus):
    tree = []
    for d in menus:
        if d["menuID"] in rootids:
            tree.append( d.copy() )
    #print(tree)
    for d in tree:
        addChilds(menus, d)
    #print(tree)
    return tree

def readCSV():
    currDir = os.path.dirname(os.path.abspath(__file__))
    fname_csv = os.path.join(currDir, '护理学（中级）大纲.csv') # '护理学（中级）大纲.xls'
    ds = pd.read_csv(fname_csv, usecols= ['无'], encoding='gbk') # utf-8
    print(ds.shape, ds.size)
    for l in ds.values:
        if type(l[0]) == str:
            print(l[0])
    

if __name__ == "__main__":
    currDir = os.path.dirname(os.path.abspath(__file__))
    fname_tree = os.path.join(currDir, 'tree.json')
    fname_menus = os.path.join(currDir, 'menus.json')
    menus = fectchData.query('SELECT ID AS menuID, PID, `name` FROM trialexampointmenus ts WHERE ts.appid = 16629 AND ts.`enable` = 1;')
    #print(menus)
    tree = menuTree(menus)
    iJson.save_json(fname_tree, tree)
    iJson.save_json(fname_menus, menus)
    #readCSV()
```







## Str



### raw string

```\
r''
```

### format

irt [u](https://github.com/17zuoye/pyirt/blob/master/tests/test_model_wrapper.py)

```python
c = [0.5, 0, 0, 0, 0.5, 0, 0, 0, 0.5]

guess_param = {}
for t in range(T):
    guess_param['q%d' % t] = c[t]
--> {'q0': 0.5, 'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0.5, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 0.5}
```

```python
print(f"{name} is {age} years old")
print (item, end=" ")
```

```
ax.text(n[0], n[1], n[2], "法向量" + r"$=\left({:.2f},{:.2f},{:.2f}\right)^{:s}$".format(g[0], g[1], -1, T), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
doc\lang\programming\python\深入理解神经网络：从逻辑回归到CNN\neural_network-neural_network_code-master\neural_network_code\画图脚本
```

```python
print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
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



### jieba



#### 自定义词典

1、加载自定义字典jieba.load_userdict()
参数filename：为文件类对象或自定义词典的路径
词典格式分为3个部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。
file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。

2、从字典中添加或删除词汇add_word、del_word
add_word(word,freq=None,tag=None)，add_word有3个参数，添加词名称，词频，词性
del_word(word)，del_word只有一个参数词语名称

3、词频调整suggest_freq
suggest_freq（segment,tune=True）
调节单个词语的词频，可以使其能（或不能）被分出来，词频越高在分词时，能够被分出来的概率越大。



```python
import jieba

#载入自定义词典
jieba.load_userdict('word_dict.txt')

#查看用户自定义词典中的内容
print(jieba.user_word_tag_tab)

#往自定义词典中添加新词
jieba.add_word('人民广场',freq=5,tag='n')

#添加新词后的结果
print(jieba.user_word_tag_tab)

string='上海市浦东新区世纪大道100号楼501'
text_cut=jieba.cut(string)
print(" ".join(text_cut))

#调整词频，重新分词
jieba.suggest_freq(('上海市','浦东新区'),tune=True)
text_cut=jieba.cut(string)
print(" ".join(text_cut))
```



- 用法： `jieba.load_userdict(file_name)` # file_name为自定义词典的路径
- 词典格式和`dict.txt`一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开

示例

```text
宜信普惠 7
宜信 10
极速模式 20
```



```python
同样的问题，比如：
jieba.add_word("弗里德里克·泰勒",freq=888888); jieba.add_word("冯·诺伊曼",freq=888888); jieba.suggest_freq(('弗里德里克·泰勒', '冯·诺伊曼'), True); txt = "这个外国人叫弗里德里克·泰勒，是美国前国防部部长。冯·诺伊曼是公认的计算机发明人"; print(" | ".join(jieba.cut(txt, HMM=True, cut_all=False)))
结果还是：
'这个 | 外国人 | 叫 | 弗里德里克 | · | 泰勒 | ， | 是 | 美国 | 前 | 国防部 | 部长 | 。 | 冯 | · | 诺伊曼 | 是 | 公认 | 的 | 计算机 | 发明人'
大家有什么好办法？

代码里面有如下的正则表达式，用来提取中文

re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&._%]+)", re.U)
也就是说对于”弗里德里克·泰勒”中的“·”不认为是中文，而是作为类似逗号和句号来处理。

一个不太好但是可以用的办法就是，修改上面的正则表达式，将“·”加入。其中\xb7就是“·”。

re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&.\xb7%]+)", re.U)

测试结果：
》 这个 | 外国人 | 叫 | 弗里德里克·泰勒 | ， | 是 | 美国 | 前 | 国防部 | 部长 | 。 | 冯·诺伊曼 | 是 | 公认 | 的 | 计算机 | 发明人

```



## Class



### 继承和静态方法

```python
# https://zhuanlan.zhihu.com/p/29887184
# GitHub\doc\lang\programming\项目反应理论\irt_zhihu.py
class BaseIrt(object):

    def __init__(self, scores=None):
        self.scores = scores

    @staticmethod
    def p(z):
        # 回答正确的概率函数
        e = np.exp(z)
        p = e / (1.0 + e)
        return p

    def _lik(self, p_val):
        # 似然函数
        scores = self.scores
        loglik_val = np.dot(np.log(p_val + 1e-200), scores.transpose()) + \
                     np.dot(np.log(1 - p_val + 1e-200), (1 - scores).transpose())
        return np.exp(loglik_val)

    def _get_theta_dis(self, p_val, weights):
        # 计算theta的分布人数
        scores = self.scores
        lik_wt = self._lik(p_val) * weights
        # 归一化
        lik_wt_sum = np.sum(lik_wt, axis=0)
        _temp = lik_wt / lik_wt_sum
        # theta的人数分布
        full_dis = np.sum(_temp, axis=1)
        # theta下回答正确的人数分布
        right_dis = np.dot(_temp, scores)
        full_dis.shape = full_dis.shape[0], 1
        # 对数似然值
        print(np.sum(np.log(lik_wt_sum)))
        return full_dis, right_dis
```



### 属性

```python
class EAPIrt2PLModel(object):

    def __init__(self, score, slop, threshold, model=Irt2PL):
        self.x_nodes, self.x_weights = model.get_gh_point(21)
        z = model.z(slop, threshold, self.x_nodes)
        p = model.p(z)
        self.lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1)

    @property
    def g(self):
        x = self.x_nodes[:, 0]
        weight = self.x_weights[:, 0]
        return np.sum(x * weight * self.lik_values)

    @property
    def h(self):
        weight = self.x_weights[:, 0]
        return np.sum(weight * self.lik_values)

    @property
    def res(self):
        return round(self.g / self.h, 3)
# https://zhuanlan.zhihu.com/p/29887184
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

提取中文部分

```python
print(re.compile(r'\d+\s+(.+?)\s+').sub(r'\1', '1 跨膜  ') )  
	# 只取第一个分组 r'\1'
print(re.findall(r"\d+\s+(.+?)\s+", "0 跨膜激活物、钙调节物、亲环蛋白配体相互作用物   1  1"))
	# findall 得到的结果是数组，不如前一种方法好用

```







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



### split



```python
# 对文本进行分句
def splitSentences(text):
    sents = re.split(u'[\n。*+@+]', text) # 以句号或换行符作为分句标准
    sents = [sent for sent in sents if len(sent) > 0]  # 去除只包含\n或空白符的句子
    return sents
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



### book_2_json



```python
import math
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname( os.path.dirname(os.path.abspath(__file__)))))  # std 包在此模块的上上上级目录
sys.path.append( os.path.dirname(os.path.abspath(__file__) ) )

import re
import util.fectchData as fectchData
import util.seg as seg
import util.saveTempData as saveTempData
import std.iSql as iSql
import std.seg.iSeg as iSeg
import std.iList as iList
import std.iJson as iJson
import std.iFile as iFile
import std.iTextrank as iTextrank

from joblib import Parallel, delayed
import itertools


regs = [
        r'(@@第[一二三四五六七八九十]+章.+?)\n',
        r'(@@第[一二三四五六七八九十]+节.+?)\n',
        r'@@[一二三四五六七八九十]+、.+?\n',
        r'@@（[一二三四五六七八九十]+）.+?\n',
        r'@@[1-9]+.+?\n'
    ]


# 输入字符串，标题正则
# 返回标题、标题位置(strat, end), 标题下的文本
def extractPattern(strs, regs, idx):
    #ss =  re.findall(reg, strs, re.DOTALL)
    iters = re.finditer(regs[idx], strs, re.DOTALL)
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

def walks(arr, regs, idx):
    if idx >= len(regs) or len(arr) <= 0:
        return

    for l in arr:
        strs = l[3]
        rs = extractPattern(strs, regs, idx)
        if len(rs) > 0:
            l[3] = rs
            walks(l[3], regs, idx+1)
        else:
            walks([l], regs, idx+1)

        #print(rs)


if __name__ == "__main__":
    
    currDir = os.path.dirname(os.path.abspath(__file__))

    fname_book = os.path.join(currDir, '药二20200617.txt')
    fname_results = os.path.join(currDir, 'results.json')
    

    book = iFile.readfile_line_by_line(fname_book)
    strs = "\n".join(book)
    
    print( len(strs), '@@第十六章' in strs )


    rs = extractPattern(strs, regs, 0)
    #iJson.save_json(fname_results, rs)
    #print(rs)

    walks(rs, regs, 1)
    iJson.save_json(fname_results, rs)
    #print(rs[0])


"""
https://zhuanlan.zhihu.com/p/42944600
"""
```





## Sort

```python
sorted(trank_res, key=lambda x: x['index'], reverse=False)
```



## Numpy



```python
x = x_nodes[:, 0] # 行全要,列只要第0列.结果是二维变一维
# (11,1) -> (11,)
```





### 维度不同的减法

```python
"""
两个1*2 减一个1*2
(2*2) - (1*2) = ( (1*2) - (1*2),
                  (1*2) - (1*2)
                )
= (2*2)
"""
a = np.array(
    [
        [-0.51632716, -0.51632716],
        [-0.56524826, -0.56524826]
    ])

b = np.array(
    [
        [-0.1491838, 2.63128067]
    ])

c = a - b
print(c)
"""
shoud be:
[[-0.36714335 -3.14760782]
 [-0.41606446 -3.19652893]]
"""
```



a, b 的列数相同，a行更多，**按列来减**



### 维度不同的乘法



```python
(2,) * (11,1) -> (11,2)
# (2,) 表示一维，两个元素
	# 2个0有序对，11个1有序对，11个2有序对

(11,2) + (2,) -> (11,2)
```



```python
x = x_nodes[:, 0] # 行全要,列只要第0列.结果是二维变一维
# (11,1) -> (11,)
```



#### 乘方

```python
# 按列乘方
array([[2, 2],
       [2, 2]])
>>> b=np.array(b)
>>> b
array([0, 1])
>>> a**b
array([[1, 2],
       [1, 2]], dtype=int32)
"""
    tmp1 = p**score
    tmp2 = (1.0 - p)**(1-score)

    lik_values = np.prod(tmp1*tmp2, axis=1)
"""
```





### 取样

```python
# 模拟参数
a = np.random.uniform(1, 3, 1000)  # 均匀分布
b = np.random.normal(0, 1, size=1000)
z = Irt2PL.z(a, b, 1)
p = Irt2PL.p(z)
score = np.random.binomial(1, p, 1000)
# D:\workcode\algo\项目反应理论\irt_zhihu.py
```



### 均方误差

```python
print('mse: {}'.format(np.mean((val - real_diff) ** 2)))
```

```python
print(np.mean(np.abs(est_slop - a[0]))) # 平均误差
```



### 计算所有元素的乘积



```python
np.prod([...]) # 不指定轴，则不管是几维都展平成一维然后连乘
np.prod([...], axis=1) # 按行连乘(维度变成??)
np.prod([...], axis=0) # 按列连乘
```





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

```python
# 一维变二维
sc = simScores[:, i]  # 取一列
sc.reshape(sc.shape[0],-1)
```





#### flatten

```
ndarray.flatten(order='C') # c by row; f by column
```



#### tile 复制列

```python
true_theta = np.random.normal(loc=0, scale=1, size=(n_persons,1))   # 5个人的能力 (5*1)
true_theta = np.tile(true_theta, n_questions)                       # 5个人每道题的能力都一样，列复制5次 (5*1) -> (5*5)
true_beta = np.random.normal(loc=0, scale=1, size=(1,n_questions))  # 5个问题的难度 (1*5)
```



#### 取第一列

```python
a[:,0]
```







### transpose

```
numpy.ndarray.T
.T is just np.transpose() 
# If the matrix has less than 2 dimensions it returns the original. 
```



### matrix op

```
np.dot(W, TR) * 0.85 + C
```



### append

```python
np.append(0, (radii*np.cos(angles)).flatten())
```



### matrix show



```
import numpy as np
import matplotlib.pyplot as plt

v = np.array([[1.5, -1.5, 2.7]]).T
plt.matshow(v, cmap=plt.cm.hot)
plt.show()
```





### loadtext

```
f = 'lsat.csv'
score = np.loadtxt(f, delimiter=",")
```



### universal function

```
ufunc是universal function的缩写，意思是这些函数能够作用于narray对象的每一个元素上，而不是针对narray对象操作，numpy提供了大量的ufunc的函数。
```



### 归一化数据集



```python
def scaleData(dataMat):
    max = dataMat[:,0].max()
    min = dataMat[:,0].min()
    dataMat[:,0] = (dataMat[:,0] - min) / (max - min)
    return dataMat
```

> Max 为所有数据中最大的值，min 为所有数据中最小的值，对每个数据减去最小值然后除以最大值和最小值的差，从而进行归一化，**使得每一个数据在 0 到 1 范围内**。



### 概率分布



```
"""
概率编程语言入门指南

有偏差的掷硬币(a biased coin toss)

随机函数被叫做模型，表达模型的方法，和正常的Python方法没有区别
模型（model）和变分分布（guide）的参数。【注：所谓变分就是将原始函数换作另一（易处理的）函数的数学技巧】
最大化证据（evidence）  证据下限”ELBO（evidence lower bound）


https://colab.research.google.com/drive/1SZDm5ppWBFIpowO8KIATfoYZXEVbuVGr#scrollTo=tdhST1QE8MuX

Fitting a Distribution with Pyro: Part 2 - Beta
https://www.richard-stanton.com/2020/05/03/fit-dist-with-pyro_2.html


A Gentle Introduction to Probabilistic Programming Languages
https://medium.com/swlh/a-gentle-introduction-to-probabilistic-programming-languages-bf1e19042ab6
"""
answers = np.random.binomial(size=(n_persons, n_questions), p=likelihood, n=1) # calculate answers based on theta and likelihood function
```



np.random.binomial(size=(n_persons, n_questions), p=likelihood, n=1)

> size 和 p 的维度相同
>
> **二项分布，值为1 的概率由p 给出**



### 阶乘



```python
import numpy as np

# n 选k 的组合数
def C(n, k):
    return np.math.factorial(n) / ( np.math.factorial(k) * np.math.factorial(n - k) )

```





### assert_equal

```python
# test if samples are 0 or 1
sm = rm.sample().flatten()
assert_equal(np.all((sm == 0) | (sm == 1)),True)
```





## System



### OS Type



```python
try:
    test = os.uname()
    if test[0] == "Linux":
        OS = "Linux"
except Exception as e:
    OS = "Windows"

indir = 'F:/11/*/*.txt' if OS == "Windows" else '/home/data/11/*.txt'
otdir = 'E:/11' if OS == "Windows" else '/home/data/22'
# D:\workcode\python\std\iEncoding.py
```





### stdout

```
sys.stdout.flush() # Updating the text.
sys.stdout.write("\rIteration: {} and {}".format(i + 1, j + 1))
```



### 子进程

```python
import subprocess
out_bytes = subprocess.check_output([r"C:\Program Files\R\R-4.0.3\bin\x64\Rscript.exe", r"C:\Program Files\R\R-4.0.3\bin\x64\op.R"])
out_text = out_bytes.decode('utf-8')
```

```R
`op` <-
function(x){
  y <- list(name=x)
  y
}

o <- op(1)
class(o)
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



```python
@echo off
cd /d D:
cd %cd%
jupyter notebook
cmd.exe
```





```python
python -m pip install --upgrade pip
pip install wheel
```



pip install jupyter

- pip install --user jupyter  出错就用这个



python -m jupyter notebook --version

```
python -m pip install -U matplotlib
pip install seaborn
pip install sklearn
pip install scikit-image
```



Ctrl + Shift + P -> Python: Select interpreter

Ctrl + Shift + P -> Python: Select interpreter to start Jupyter server

Python: Select interpreter to start Jupyter server



**Ctrl+Shift+P** -> **Python: Create New Blank Jupyter Notebook**

> 注意大小写都要正确





### 不用print 打印



#### **其他技巧**

**1. 不用print即可输出多个变量**

比如下面一段代码

```text
a, b = 1, 2
a
b
```

运行结果只会展示`b`的值，如果要同时展示`a b`的值，需要使用`print`，如下所示

```text
a, b = 1, 2
print(a)
print(b)
```

如果希望不需要`print`即可同时输出`a b`的值，则可以先运行下面这两行代码，则之后在这个笔记本中执行代码都不需要`print`

```text
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

如果不喜欢这个配置，要改回来只需要

```text
InteractiveShell.ast_node_interactivity = "last"
```



题外话：如果想直接打变量名不输出，只需要在后面加一个`;`，这个在`plt.hist()`的使用中比较有用。

**2. 默认执行代码**

本节分为两个部分：修改默认配置，默认执行代码。

像上一节的`print`配置，如果希望对所有notebook都适用，不用每次都重新指定，可以在配置文件中修改。只需要在`~/.ipython/profile_default/ipython_config.py`文件中添加

```text
c = get_config()
c.InteractiveShell.ast_node_interactivity = "all"
```

保存后重新打开notebook会发现这些配置自动生效。

（如果该路径下没有这个文件则创建一个，用这条命令`ipython profile create`）

配置这个文件的另一个功能是执行默认代码，即有一些代码希望在每一个notebook都默认执行时，可以像这样写入配置文件

```text
c.InteractiveShellApp.exec_lines = [
 'import sys; sys.path.append("C:\\Miniconda3\\Lib\\site-packages")',
 'import matplotlib.pyplot as plt; %matplotlib inline'
]
```

**3. 将ipynb文件转化为py文件**

文本内容全部变成注释

```text
ipython nbconvert --to python abc.ipynb
```

另一种方式：在notebook页面菜单中选择 `File-->Download as-->py`





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



## trick



```
def weights_replaceinto(ls):
    sqls = []
    for d in ls:
        columns = ",".join( list(d.keys()) )
        values = ",".join( ( map(lambda w: r"'" + w + r"'" ,list(d.values()) ) ) )
        sqls.append(f"INSERT INTO weights ({columns}) VALUES({values}) ON DUPLICATE KEY UPDATE updateTime=now();")
```





### Insert into



```
f"INSERT INTO trialexampointrelevanttest (examPointID, appID, testID, childTestID, isMachine, similarity ) VALUES ({examPointID}, {appID}, {testID}, {childTestID}, 1, {similarity} ) ON DUPLICATE KEY UPDATE similarity={similarity}, updateTime=now();"

```





## pymysql




### debug


```python
    q = iSql.db88(db="temp")
    for sql in sqls:
        try:
            q.query(sql)
        except Exception as e:
            print(sql)
            print(str(e))
            q.close()
            raise RuntimeError('some err')
    q.close()
```



## Excel



```python
import pandas as pd
seg = pd.DataFrame(wordlist,columns=['word','length','fre','pmi','entropy'])
seg.to_csv(fname_results, index=False ,encoding="utf-8")
```



### xlsx



```
pip install openpyxl
pip install xlrd
```



扩展名 xlsx 才是真excel，csv 不是

```python
    csv = pd.DataFrame(data,columns=['知识点ID', '考频', '考频分类', '考试大纲', '关联真题数', '关联非真题数', '知识点内容'])
    csv.to_excel(fname_csv, index=False ,encoding="utf-8")
```






### read csv



#### encoding

```python
ds = pd.read_csv(fname_csv, usecols= ['列名'], encoding='gbk') # utf-8
```







```python
    csvs = ['药学专业知识一-考频.csv', '药学专业知识二-考频.csv', '药事管理与法规-考频.csv', '药学综合知识与技能-考频.csv']
    currDir = os.path.dirname(os.path.abspath(__file__))
    
    dic_pl = {}  # Point Level

    for fname in csvs:
        fname_csv = os.path.join(currDir, DIRNAME, fname)
        print(fname_csv)
        ds = pd.read_csv(fname_csv, usecols= ['知识点ID', '考频分类']) # header=None
        print(ds.shape, ds.size)
        for l in ds.values:
            examPoinID = str(l[0])
            level = l[1]
            if examPoinID not in dic_pl:                
                dic_pl[examPoinID] = level
                #print(examPoinID, level)
            else:
                raise RuntimeError('something wrong.')  # 不同科目不应该有相同的知识点ID
```





If you only want to read the first 999,999 (non-header) rows:

```py
read_csv(..., nrows=999999)
```

If you only want to read rows 1,000,000 ... 1,999,999

```py
read_csv(..., skiprows=1000000, nrows=999999)
```

***nrows\*** : int, default None Number of rows of file to read. Useful for reading pieces of large files*

***skiprows\*** : list-like or integer Row numbers to skip (0-indexed) or number of rows to skip (int) at the start of the file

and for large files, you'll probably also want to use chunksize:

***chunksize\*** : int, default None Return TextFileReader object for iteration









### multiple dataframes



```python
import pandas as pd

# Create some Pandas dataframes from some data.
df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
```



```python
writer = pd.ExcelWriter(filepath)
companydf.to_excel(excel_writer=writer,sheet_name='公司维度表')
goodsdf.to_excel(excel_writer=writer, sheet_name='货物维度表')
writer.save()
writer.close()
```





[geeks4geeks](https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/)

[read csv](https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58)

[使用 Python 读写 CSV 文件（三）](https://zhuanlan.zhihu.com/p/40946024)



## Word



[Python读取word文本](https://blog.csdn.net/woshisangsang/article/details/75221723)

[用python-docx模块读写word文档](https://www.jianshu.com/p/94ac13f6633e)



```python
# coding:utf-8
# 写word文档文件
import sys

from docx import Document
from docx.shared import Inches

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    # 创建文档对象
    document = Document()
    
    # 设置文档标题，中文要用unicode字符串
    document.add_heading(u'我的一个新文档',0)
    
    # 往文档中添加段落
    p = document.add_paragraph('This is a paragraph having some ')
    p.add_run('bold ').bold = True
    p.add_run('and some ')
    p.add_run('italic.').italic = True
    
    # 添加一级标题
    document.add_heading(u'一级标题, level = 1',level = 1)
    document.add_paragraph('Intense quote',style = 'IntenseQuote')
    
    # 添加无序列表
    document.add_paragraph('first item in unordered list',style = 'ListBullet')
    
    # 添加有序列表
    document.add_paragraph('first item in ordered list',style = 'ListNumber')
    document.add_paragraph('second item in ordered list',style = 'ListNumber')
    document.add_paragraph('third item in ordered list',style = 'ListNumber')
    
    # 添加图片，并指定宽度
    document.add_picture('e:/docs/pic.png',width = Inches(1.25))
    
    # 添加表格: 1行3列
    table = document.add_table(rows = 1,cols = 3)
    # 获取第一行的单元格列表对象
    hdr_cells = table.rows[0].cells
    # 为每一个单元格赋值
    # 注：值都要为字符串类型
    hdr_cells[0].text = 'Name'
    hdr_cells[1].text = 'Age'
    hdr_cells[2].text = 'Tel'
    # 为表格添加一行
    new_cells = table.add_row().cells
    new_cells[0].text = 'Tom'
    new_cells[1].text = '19'
    new_cells[2].text = '12345678'
    
    # 添加分页符
    document.add_page_break()
    
    # 往新的一页中添加段落
    p = document.add_paragraph('This is a paragraph in new page.')
    
    # 保存文档
    document.save('e:/docs/demo1.docx')
    
if __name__ == '__main__':
    main()

```



## Panda



### DataFrame 

> "dict-like" Series **container** for **Series objects**
>
> - **是序列对象的容器，能够以字典方式存取数据**



```python
    for N in range(2, MAX_N+1): # MAX_N+1
        print(f'正在进行{N}-Gram词的最大熵筛选({len(rt[N-2])})...')
        pp = []
        for i in range(0,len(s)):
            if i+N+2 <= len(s):  # +2 是因为一个左邻字，一个右邻字
                pp.append( [ s[i:i+1], s[i+1:N+i+1], s[N+i+1:N+i+2] ] )
        pp2 = pd.DataFrame(pp).set_index(1).sort_index() # 排序，可以加快检索速度
        """
        现在输入N-Gram 词，可以得到它的左邻右邻字
        """

        index = np.sort(np.intersect1d(rt[N-2], pp2.index)) # 作交集
        
        left = pp2[0][word]                            # word 的所有左邻字
        right = pp2[2][word]                           # word 的所有右邻字
```





## Series [u](https://towardsdatascience.com/gaining-a-solid-understanding-of-pandas-series-893fb8f785aa)

>  Series 可以是**数据集**的行，也可以是数据集的列 



bigdataEntropy.py

```python
tt = tt.drop(labels=will_drops)  # 第二次筛选：凝合程度
rt.append( tt.index )
```





### 转有转字典

```python
from collections import OrderedDict, defaultdict
cs = pd.Series(list(s)).value_counts().to_dict(OrderedDict)
```



```python
dic_tosave = {
        'total_alphabets':0,
        't':[],
        'tt':[]
    }

    cs = pd.Series(list(s)).value_counts()              # 所有字的出现次数 
    dic_tosave['total_alphabets'] = int( cs.sum() )     # 总共有多少个字
    dic_tosave['t'].append( cs.to_dict(OrderedDict) )   # Series 转成有序字典才能保存JSON
```





### 统计每个字出现次数

```python
counts = pd.Series(list(s)).value_counts() # 每个字出现多少次
totol = counts.sum()  # 总共有多少个字
```

```python
    ls = list(s)
    for N in range(2, MAX_N+1):
        print(f'正在生成{N}-Gram词...')
        t.append([])
        for i in range(0,len(ls)):
            if i+N <= len(ls):
                t[N-1].append( "".join(ls[i:N+i]) )  # array[start:stop:step]
            
        t[N-1] = pd.Series(t[N-1]).value_counts()  # 所有N-Gram 词出现次数
        t[N-1] = t[N-1][t[N-1] > min_count]        # 最小次数筛选
        tt = t[N-1][:]
```





```python
revenue = pd.Series([1000, 1200, 1500, 800, 900], index=['2014', '2015', '2016', '2017', '2018'])
```

```python
revenue.sort_values(ascending=False).index[0]
```

















## Matplotlib

### 绘图的重要参考

#### 深入理解神经网络：从逻辑回归到CNN.md

GitHub\doc\lang\programming\深入理解神经网络：从逻辑回归到CNN.md



[readthedocs.io matplotlib](https://mlhowto.readthedocs.io/en/latest/matplot.html)

[mtri.Triangulation](https://matplotlib.org/3.1.1/api/tri_api.html)

[Numpy中Meshgrid函数介绍及2种应用场景](https://zhuanlan.zhihu.com/p/29663486)



#### 记得调用plt.show() 秀图

````
plt.show()
````

普通的 .py 文件这样出来的图是可以3d 旋转的



### 绘制平面



```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')
ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# 生成等间距的n 个数的list, 包含尾端的数
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x1 = [-1.5  1.5]
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x2 = [-1.5  1.5]
x1, x2 = np.meshgrid(x1, x2)  # x1 作为行复制两次（行数是len(x2)），返回这个新矩阵
                              # x2 作为列复制两次（列数是len(x1)），返回这个新矩阵

"""
两个新矩阵是：

 [[-1.5  1.5]
 [-1.5  1.5]] 

 [[-1.5 -1.5]
 [ 1.5  1.5]]
 
 两个矩阵叠在一起，就是网格
 
 (-1.5, -1.5) (1.5, -1.5)
 (-1.5,  1.5) (1.5,  1.5)
 
"""
print(x1, "\n\n",x2)

x1, x2 = x1.flatten(), x2.flatten()  # 网格子矩阵flatten 后就可以传给plot_trisurf 绘制平面
ax.plot_trisurf(x1, x2, [ -2,-2,-2,-2], antialiased=True, alpha=LIGHT_ALPHA, color="black")
```

<img src="Python 3  Summary.assets/image-20200812093025409.png" alt="image-20200812093025409" style="zoom:50%;" />



### 绘制散点

```python
ax.scatter(x1, x2, [ -2,-2,-2,-2], c=[ -2,-2,-2,-2], cmap='viridis', linewidth=0.5)
```

<img src="Python 3  Summary.assets/image-20200812095330608.png" alt="image-20200812095330608" style="zoom:50%;" />

### 平面四个角的高度

#### 高度指定的顺序是：从左到右，从下到上

> [左下，右下，左上，右上]



<img src="Python 3  Summary.assets/image-20200812101606934.png" alt="image-20200812101606934" style="zoom:50%;" />



```python
ax.plot_trisurf(x1, x2, [ -2,0,-2,-2], antialiased=True, alpha=LIGHT_ALPHA, color="black")
ax.scatter(x1, x2, [ -2,0,-2,-2], c=[ -2,-2,-2,-2], cmap='viridis', linewidth=0.5)
```

<img src="Python 3  Summary.assets/image-20200812101505894.png" alt="image-20200812101505894" style="zoom:50%;" />



```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')
ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x1 = [-1.5  1.5]
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x2 = [-1.5  1.5]
x1, x2 = np.meshgrid(x1, x2)  # x1 作为行复制两次（行数是len(x2)），返回这个新矩阵
                              # x2 作为列复制两次（列数是len(x1)），返回这个新矩阵
x3 = w[0] * x1 + w[1] * x2
 
    
"""
两个新矩阵是：

 [[-1.5  1.5]
 [-1.5  1.5]] 

 [[-1.5 -1.5]
 [ 1.5  1.5]]
 
 两个矩阵叠在一起，就是网格
 
 (-1.5, -1.5) (1.5, -1.5)
 (-1.5,  1.5) (1.5,  1.5)
 
 计算四个角的高度
 x3 = w[0] * x1 + w[1] * x2  # x1, x2 = x1.flatten(), x2.flatten() 注意是展平后的值 
 
 相当于：
 (-1.5 * w1 +  -1.5 * w2) (1.5 * w1 +  -1.5 * w2)
 (-1.5 * w1 +   1.5 * w2) (1.5 * w1 +   1.5 * w2)
 其中w1 = 0.1, w2 = -0.2，所以：
 (0.15)  (0.45)
 (-0.45) (-0.15)
 
 四个角的高度既可以直接以二维矩阵的形式传给画散点或平面的函数，也可以展平成一维的形式再传
 
"""
print(x1, "\n\n",x2, "\n\n\n")

print(x1 * 0.1, "\n\n", x2 *(-0.2), "\n\n\n")

print(x3)

x1, x2 = x1.flatten(), x2.flatten()  # 网格子矩阵flatten 后就可以传给plot_trisurf 绘制平面
ax.plot_trisurf(x1, x2, [ 0.15,0.45,-0.45,-0.15], antialiased=True, alpha=LIGHT_ALPHA, color="black")
ax.scatter(x1, x2, [ 0.15,0.45,-0.45,-0.15], c=[ 0.15,0.45,-0.45,-0.15], cmap='viridis', linewidth=0.5)  # 绘制散点
```

<img src="Python 3  Summary.assets/image-20200812105520835.png" alt="image-20200812105520835" style="zoom:50%;" />



#### 观察平面角上的点和向量w 的关系



$$
(-1.5, -1.5)^T  \ \  \text{左下角绿色的那个点} \\
w = (0.1, -0.2)^T \ \ \text{决定平面上所有点的高度}
$$



```
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

SQUARE_FIG_SIZE = (10 ,10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
ALPHA = 0.3
LIGHT_ALPHA = 0.1


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"

ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

"""
法向量W
两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, 
    A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
"""
w = [0.1, -0.2]

# 从原点(0, 0, 0)指向(0.1, -0.2, -1)
pts = np.array([ [0, 0, 0], [w[0], w[1], -1] ], np.float).T  
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


# 从原点(0, 0, 0)指向(0.1, -0.2, 0)
pts = np.array([ [0, 0, 0], [w[0], w[1], 0] ], np.float).T
arrow = Arrow3D([0, w[0]],[0, w[1]],[0, 0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1, w[1], 0.1, r"$\left({:.1f},{:.1f},0\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


ax.plot((w[0], w[0]), (w[1], w[1]), (-1, 0), "k--", alpha=ALPHA)    
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = w[0] * x1 + w[1] * x2

print(x1, x2, x3)
print(x1*0.1)
print(x2*(-0.2))
ax.scatter(x1, x2, x3, c=x3, cmap='viridis', linewidth=0.5)

#ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

ax.plot_trisurf(x1, x2, [ -2,-2,-2,-2], antialiased=True, alpha=LIGHT_ALPHA, color="black")
```

<img src="Python 3  Summary.assets/image-20200812113924159.png" alt="image-20200812113924159" style="zoom:50%;" />



### 自定义Plot 类

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

# 返回ax 对象，可以进行各种绘制
class Plot():
    def __init__(self):
        self.SQUARE_FIG_SIZE = (10 ,10)
        self.AXIS_LABEL_FONT_SIZE = 16
        self.TEXT_FONT_SIZE = 16
        self.ALPHA = 0.3
        self.LIGHT_ALPHA = 0.1
        self.fig = plt.figure(figsize=np.array(self.SQUARE_FIG_SIZE) * 2, facecolor='white')
        self.T = "\mathrm{T}"
        self.ax = self.fig.add_subplot(2, 2, 1, projection="3d")
        self.ax.set_xlim([-2, 2])
        self.ax.set_ylim([-2, 2])
        self.ax.set_zlim([-2, 2])
        
        # ax.set_title(r"$Lorenz\ Attractor$")
        self.ax.set_xlabel(r"$x_1$", fontsize=self.AXIS_LABEL_FONT_SIZE)
        self.ax.set_ylabel(r"$x_2$", fontsize=self.AXIS_LABEL_FONT_SIZE)
        self.ax.set_zlabel(r"$y$",   fontsize=self.AXIS_LABEL_FONT_SIZE)

        # 画简头，从p1 指向p2        
    def drawArrow(self, p1, p2):
        pts = np.array([ p1, p2 ], np.float).T  
        arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
        self.ax.add_artist(arrow)

    def drawText(self, w):
        self.ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], self.T), fontsize=self.TEXT_FONT_SIZE)

    def show(self):
        plt.show()

if __name__ == "__main__":
    p = Plot()
    w = [0.1, -0.2]
    p.drawArrow([0, 0, 0], [w[0], w[1], -2])
    p.drawText( w )
    p.show()
```





### 可以拖动的图形

#### plot_trisurf

[plot_trisurf](https://matplotlib.org/3.1.1/tutorials/toolkits/mplot3d.html#mpl_toolkits.mplot3d.Axes3D.plot_trisurf)

```python
trisurf3d.py
'''
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
'''

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


n_radii = 8
n_angles = 36

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Compute z to make the pringle surface.
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```









### ax.plot AND ax.add_artist(Arrow3D)



#### 三维点(0, 0, 2)到点(0, 0, -2) 画线的两种方法

```python
pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.float).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]))
```

```python
# 两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.float).T
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
```



### 画虚线 



```python
# 画虚线 p1 [x, y, z] 坐标 p2 [x, y, z] 坐标 
def drawDashe(p1, p2, ax):
    pts = np.array([ p1, p2 ], np.float).T
    ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)

drawDashe([0, 0, 2], [0, 0, -2], ax)
```







```python
from book_draw_util import *
import numpy as np

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)
"""
坐标系的原点在一楼中心
"""

pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.float).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
"""
楼顶中心指向地下室中心
"""
```

<img src="Python 3  Summary.assets/image-20200804112140778.png" alt="image-20200804112140778" style="zoom: 33%;" />



```

```










### np.float，注意数据类型！别让小数变整数了！

```python
# 绘制法向量
w = [0.1, -0.2]
pts = np.array([ [0, 0, 0], [w[0], w[1], -1] ], np.float).T  # 从原点(0, 0, 0)指向(0.1, -0.2, -1)
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
"""
两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, 
    A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
"""
```





等间隔数字

Return **evenly spaced numbers** over a specified interval.

> even 等，均等
>
> space 间隔，距离，空隙



```python
# 生成等间距的n 个数的list, 包含尾端的数
np.linspace(-1.5, 1.5, endpoint=True, num=2)
```



```python
# 以行向量x1 构建新矩阵，行数是len(x2)
# 以列向量x2 构建新矩阵，列数是len(x1)
# 既len(x1) 定所有新矩阵的行数，len(x2) 定所有新矩阵的列数
# 生成形状一样的两个矩阵是为了待会把它们“叠”到一起，形成有序对(pair), (x1,y1), (x2,y1)
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
```

<img src="Python 3  Summary.assets/image-20200731184147007.png" alt="image-20200731184147007" style="zoom:50%;" />



### meshgrid 用N个坐标轴上的点在空间中画网格

>```python
># 用两个坐标轴的点画网格
>x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
>x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
>[-1.5  1.5] [-1.5  1.5]
>```

```python
# 两个点，生成两个2*2 的矩阵
# x1当成行向量，行复制len(x2) 次，生成新矩阵。这是第一个返回值
# x2当成列向量，列复制len(x1) 次，生成新矩阵。这是第一个返回值
x1, x2 = np.meshgrid(x1, x2) 

[[-1.5  1.5]
 [-1.5  1.5]] 

[[-1.5 -1.5]
 [ 1.5  1.5]]
```

```python
# 网格矩阵降维成1 维
x1, x2 = x1.flatten(), x2.flatten()
# ？？
x3 = w[0] * x1 + w[1] * x2
```

```python
# 画垂直于法向量的平面
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")
```



### 画垂直于向量的平面

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

SQUARE_FIG_SIZE = (10 ,10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
ALPHA = 0.3
LIGHT_ALPHA = 0.1


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"

ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

"""
法向量W
两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, 
    A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
"""
w = [0.1, -0.2]
pts = np.array([ [0, 0, 0], [w[0], w[1], -1] ], np.float).T  # 从原点(0, 0, 0)指向(0.1, -0.2, -1)
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


# 从原点(0, 0, 0)指向(0.1, -0.2, 0)
pts = np.array([ [0, 0, 0], [w[0], w[1], 0] ], np.float).T
arrow = Arrow3D([0, w[0]],[0, w[1]],[0, 0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1, w[1], 0.1, r"$\left({:.1f},{:.1f},0\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


ax.plot((w[0], w[0]), (w[1], w[1]), (-1, 0), "k--", alpha=ALPHA)    
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = w[0] * x1 + w[1] * x2

print(x1, x2, x3)
ax.scatter(x1, x2, x3, c=x3, cmap='viridis', linewidth=0.5)

ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")
```

<img src="Python 3  Summary.assets/image-20200811102936920.png" alt="image-20200811102936920" style="zoom:50%;" />



#### 先画散点，再画平面

##### ax.scatter，plot_trisurf 

```python
# 画散点
print(x1, x2, x3)
ax.scatter(x1, x2, x3, c=x3, cmap='viridis', linewidth=0.5)
```

<img src="Python 3  Summary.assets/image-20200811101543133.png" alt="image-20200811101543133" style="zoom: 50%;" />

```
[-1.5  1.5 -1.5  1.5] [-1.5 -1.5  1.5  1.5] [ 0.15  0.45 -0.45 -0.15]
```

**z轴是 0.15到-0.15，是平面的厚度**



> numpy.meshgrid（ \*xi，\*\* kwargs ）
>
> xi 是变长参数，可传$x_1, x_2,...,x_n$ 代表n 个坐标轴的点
>
> - 每一个都是**一维数组**
>
> indexing 是可选参数，默认值'xy' 代表笛卡尔；'ij' 代表矩阵
>
> - 'xy' 返回的shape 是(M,N)，Y 定行数，X 定列数
> - ‘ij’ 返回的shape 是(N,M)，X 定行数，Y 定列数
>
> 返回值 是N 个N 维矩阵
>
> - 每一个**矩阵的shape 由indexing 参数决定**





```python
xv, yv = np.meshgrid( x, y )
```

<img src="Python 3  Summary.assets/image-20200803091424334.png" alt="image-20200803091424334" style="zoom:50%;" />



<img src="Python 3  Summary.assets/image-20200803091622368.png" alt="image-20200803091622368" style="zoom: 50%;" />



<img src="Python 3  Summary.assets/image-20200803092919491.png" alt="image-20200803092919491" style="zoom:50%;" />



https://matplotlib.org/3.1.1/api/tri_api.html

matplotlib.tri.Triangulation(x, y, triangles=None, mask=None)



得到三维数据，接着使用散点图观察大致形状，然后使用 plot_trisurf 绘图，plot_trisurf 使用三角形来构造表面并填充配色



```python
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(x) * np.cos(y) * 2

theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))

z = f(x, y)

fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(1, 2, 1, projection='3d', title='scatter')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)

ax = fig.add_subplot(1, 2, 2, projection='3d', title='trisurf')
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
```



<img src="Python 3  Summary.assets/image-20200803174755594.png" alt="image-20200803174755594" style="zoom: 67%;" />





### 楼房坐标系



```
from book_draw_util import *
import numpy as np

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)
"""
坐标系的原点在一楼中心
"""

# 两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
#pts = np.array([ [0, 0, 0], [0, 0, -1] ], np.int32).T # 从一楼的中心指向地下室的中心
#pts = np.array([ [2, 0, 0], [-2, 0, 0] ], np.int32).T
#ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)

pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.int32).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
"""
楼顶中心指向地下室中心
"""

pts = np.array([ [-2, 0, 2], [0, 0, 2]], np.int32).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
pts = np.array([ [0, 2, 2], [0, 0, 2]], np.int32).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
"""
两块楼顶地板
"""
```







所有cell 的变量是共享的，全局变量放最前面运行一次

```
all_pic_path = "D:\GitHub\doc\lang\programming\python\高品质图片"
```



doc\lang\programming\python\深入理解神经网络：从逻辑回归到CNN\neural_network-neural_network_code-master\neural_network_code\画图脚本



### alpha 控制向量颜色浅淡

```
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k", alpha=ALPHA)
```



### linestyle 设置虚线风格

```python
ax.arrow(p[0], p[1], (p_next.A1-p)[0], (p_next.A1-p)[1], head_width=0.3, length_includes_head=True, color="k", linestyle="--", alpha=DARK_ALPHA)

linestyle="dashed"
```



### arrow

两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数

```
arrow = Arrow3D([0,0],[0,0],[-2,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
arrow = Arrow3D([-2,0],[0,0],[0,0], arrowstyle="-|>", linestyle="--", lw=1,mutation_scale=10,color="k", ALPHA=0.2)
ax.add_artist(arrow)
```





### probability distribution



```python
import os, sys;
currDir = os.getcwd()
sys.path.append( os.path.dirname( os.path.dirname( currDir ) ) ) # std 包在此模块的上上上级目录

import math
import std.iFile as iFile
import std.iJson as iJson
import std.iList as iList
import std.seg.iSeg as iSeg
import std.iSql as iSql
import util.fectchData as fectchData


import pandas as pd # 导入另一个包“pandas” 命名为 pd，理解成pandas是在 numpy 基础上的升级包
import numpy as np #导入一个数据分析用的包“numpy” 命名为 np
import matplotlib.pyplot as plt # 导入 matplotlib 命名为 plt，类似 matlab，集成了许多可视化命令


fname_results = os.path.join(currDir, '知识点关联试题2020.7.10.11.03.json')
fname_similarity = os.path.join(currDir, 'similarity.csv')
rs = iJson.load_json(fname_results)

sims = []
for ls in rs:
    for l in ls:
        sims.append( l[3] )

sims = sorted(sims, key=lambda x: x, reverse=True)

frame = pd.DataFrame(sims,columns=['similarity'])
frame.to_csv(fname_similarity, index=False ,encoding="utf-8")

print(max(sims), min(sims))



#jupyter 的魔术关键字（magic keywords）
#在文档中显示 matplotlib 包生成的图形
# 设置图形的风格
%matplotlib inline 
%config InlineBackend.figure_format = 'retina'

data = pd.read_csv(fname_similarity) #载入数据文件

print( data.head(3), '\n\n')
print('row num:', len(data) )


time = data["similarity"] #把数据集中的 time 定义为 time
mean = time.mean()  #mean均值，是正态分布的中心，把 数据集中的均值 定义为 mean
print('mean value: ', mean)

#S.D.标准差，把数据集中的标准差 定义为 std
std = time.std()

#正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf


# 设定 x 轴前两个数字是 X 轴的开始和结束，第三个数字表示步长，或者区间的间隔长度
x = np.arange(0.0,6.0,0.05) 
#设定 y 轴，载入刚才的正态分布函数
y = normfun(x, mean, std)
plt.plot(x,y)
#画出直方图，最后的“density”参数，是赋范的意思，数学概念
plt.hist(time, bins=50, rwidth=0.5, density=True)
plt.title('Time distribution')
plt.xlabel('Time')
plt.ylabel('Probability')

plt.savefig(os.path.join("D:\workcode\python\AUTOMATIC_TEXT_SUMMARIZATION\matchTestAndExampoint", 'distribution.png'), format='png', dpi=600)
#输出
plt.show()
```

<img src="Python 3  Summary.assets/image-20200710154652277.png" alt="image-20200710154652277" style="zoom:50%;" />



### logistic

```python
import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6)) # width, height in inches.  1英寸=2.54厘米
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")


sigma = np.arange(-8, 8, 0.01)
ax.grid(True)
ax.plot(sigma, logistic(sigma), c="k")
plt.xlim(-8, 8)
plt.ylim(-.21, 1.2)
ax.text(x=8.5 , y=-0.02, s=r"$a$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-1.2, y=1.3, s=r"$\mathrm{Logistic}\left(a\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

plt.savefig(os.path.join("D:\workcode\python\plot\高品质图片", '1-1.png'), format='png', dpi=600)
```



<img src="Python 3  Summary.assets/image-20200710103820788.png" alt="image-20200710103820788" style="zoom:50%;" />



### two vector

```
from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")



plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,-2,4, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")

ax.text(x=4.1, y=2.1, s=r"$\left(4,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=-2.5, y=4.1, s=r"$\left(-2,4\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-3.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710110902610.png" alt="image-20200710110902610" style="zoom:50%;" />



```python
from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")

plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,2,1, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,1,3, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,3,4, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")

ax.arrow(1,3,2,1, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=0.3)
ax.arrow(2,1,1,3, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=0.3)

ax.text(x=2.2, y=1, s=r"$x=\left(2,1\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.4, y=3.4, s=r"$y=\left(1,3\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=3.1, y=4.1, s=r"$x+y=\left(3,4\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-4.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710163043611.png" alt="image-20200710163043611" style="zoom:50%;" />





```python
from book_draw_util import *


fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")



plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,1,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")


ax.arrow(1.6,0.8,-0.6,1.2, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)
ax.arrow(1.4,0.7,-0.1,0.2, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)
ax.arrow(1.3,0.9,0.2,0.1, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)

ax.text(x=4.1, y=2.1, s=r"$y=\left(4,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=1.1, y=2.1, s=r"$x=\left(1,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.2, y=0.2, s=r"$\theta$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.05, y=1.6, s=r"$\left||x\right||$", fontsize=TEXT_FONT_SIZE)
ax.annotate(s=r"$\left||x\right||\mathrm{cos}\theta=\frac{\left<x,y\right>}{\left||y\right||}$", 
        xy=(0.7,0.3), xytext=(2,0.25), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-8.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710170341783.png" alt="image-20200710170341783" style="zoom:50%;" />







```python
from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)

arrow = Arrow3D([0,3],[0,-1.5],[0,3], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(3, -1.5, 3, r"$w$", fontsize=TEXT_FONT_SIZE)


x1 = np.linspace(-0.6, 2, endpoint=True, num=2)
x2 = np.linspace(-2, 0.8, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = 2 - x1 + 0.5 * x2
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")


arrow = Arrow3D([0,0],[0,0],[0,2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(0, 0, 2, r"$x_a$", fontsize=TEXT_FONT_SIZE)
ax.text(-0.05, 0.2, 0.1, r"$\theta_a$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,2],[0,0],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(2, 0, 0, r"$x_b$", fontsize=TEXT_FONT_SIZE)
ax.text(0.2, 0, .05, r"$\theta_b$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,0],[0,2],[0,1], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(0, 2, 1, r"$x_c$", fontsize=TEXT_FONT_SIZE)
ax.text(0, 0.6, 0.12, r"$\theta_c$", fontsize=TEXT_FONT_SIZE)


ax.plot((8/7, 0), (-4/7, 0), (8/7, 2), "k--", alpha=ALPHA)
ax.plot((8/7, 2), (-4/7, 0), (8/7, 0), "k--", alpha=ALPHA)
ax.plot((8/7, 0), (-4/7, 2), (8/7, 1), "k--", alpha=ALPHA)
ax.scatter(8/7, -4/7, 8/7, s=POINT_SIZE, c="k")
ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")

ax.set_title(r"$||x_a||\mathrm{cos}\theta_a=||x_b||\mathrm{cos}\theta_b=||x_c||\mathrm{cos}\theta_c=\frac{x_a^\mathrm{T}w}{||w||}=\frac{x_b^\mathrm{T}w}{||w||}=\frac{x_c^\mathrm{T}w}{||w||}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-10.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710172303832.png" alt="image-20200710172303832" style="zoom:50%;" />



## Algo



### N-Gram

```python
myre = {2:'(..)', 3:'(...)', 4:'(....)', 5:'(.....)', 6:'(......)', 7:'(.......)'}
max_sep = 4 #候选词语的最大字数
for m in range(2, max_sep+1):
    print(u'正在生成%s字词...'%m)
    t.append([])
    for i in range(m): #生成所有可能的m字词
        t[m-1] = t[m-1] + re.findall(myre[m], s[i:])

```









# 爬虫



```python
有人爬清华的太过分了 服务器更新中=-=

---------------------
清华的比较简单 浏览器里会留缓存图片 python3 需要 pip install selenium img2pdf
from selenium import webdriver
import os,imghdr,shutil
import time,random
import img2pdf
from PIL import Image
def getpics(pdfidurl):
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=%s\wqbook"%os.getcwd())  # Path to your chrome profile
    driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    pdf_url = 'https://lib-nuanxin.wqxuetang.com/read/pdf/{}'.format(pdfid)
    driver.get(pdf_url)
    body=driver.find_element_by_css_selector('body')
    time.sleep(5)
    scrpositon=0
    height=driver.execute_script("return document.body.scrollHeight;")
    print(height)
    while scrpositon<height:
        scrpositon+=1500
        driver.execute_script("window.scrollTo(0,%s);"%scrpositon)
        time.sleep(4+random.randint(0,1))
    driver.quit()
def movefiles(pdfid):
    os.mkdir(pdfid)
    path = 'wqbook\Default\Cache\\'
    fileList = os.listdir(path)
    for i in fileList:
        print(imghdr.what(path + i))
        ext = imghdr.what(path + i)
        if ext == 'png':
            shutil.copyfile(path + i, '%s\\'%pdfid + i + '.' + ext)
        os.remove(path + i)
def changename(pdfid):
    fileList = os.listdir(pdfid)
    for i in fileList:
        name=i.split('.')[0]
        name=name.split('_')[1]
        os.rename(r'%s\%s'%(pdfid,i),r'%s\%s.png'%(pdfid,int(name, 16)))

if __name__ == '__main__':
    for pdfid in [
        '',#书的id
    ]:
        getpics(pdfid)
        movefiles(pdfid)
        changename(pdfid)
        for file in os.listdir(pdfid):
            filepath = '%s\\'%pdfid + file
            img = Image.open(filepath)
            img.convert('RGB').save(filepath)
        a = ['%s\\'%pdfid + i for i in os.listdir(pdfid) if i.endswith(".png")]
        a.sort(key=lambda x: int(x.split('\\')[1].split('.')[0]))
        with open("%s.pdf"%pdfid, "wb") as f:
            f.write(img2pdf.convert(a))
        print('%s已完成'%pdfid)


电子工业的似乎会banIP了

--------------------------

电子工业的一页一页截就行 一样用法
from selenium import webdriver
import time,os
from selenium.webdriver.common.action_chains import ActionChains
import img2pdf
from PIL import Image, ImageDraw, ImageFilter

def getbook(bookid):
    driver = webdriver.Chrome()
    driver.set_window_size(1456,2536)
    driver.get('https://yd.51zhy.cn/ebook/reader/index.html#/pdfReader?id=%s'%bookid)
    time.sleep(5)
    ActionChains(driver).move_by_offset(200, 100).click().perform()

    pdfboxes = driver.find_elements_by_class_name('pdf_box')
    pagenum = 0
    if os.path.exists(bookid):
        pagenum=len(os.listdir(bookid))
    else:
        os.mkdir(bookid)
    for box in pdfboxes[pagenum:]:
        driver.execute_script("arguments[0].scrollIntoView(true)", box)
        while box.get_attribute('style') != 'background: white;': time.sleep(1)
        with open(r'%s/%s.png' % (bookid,pagenum), 'wb') as f:
            f.write(box.find_element_by_class_name('page').screenshot_as_png)
        pagenum += 1
    driver.quit()

if __name__ == '__main__':
    for bookid in [
        '',
    ]:
        getbook(bookid)
        for file in os.listdir(bookid):
            filepath = '%s\\'%bookid + file
            img = Image.open(filepath)
            img.convert('RGB').save(filepath)
        a = ['%s\\'%bookid + i for i in os.listdir(bookid) if i.endswith(".png")]
        a.sort(key=lambda x: int(x.split('\\')[1].split('.')[0]))
        with open("%s.pdf"%bookid, "wb") as f:
            f.write(img2pdf.convert(a))
        print('%s已完成'%bookid)


还要下个chromedrive 看电脑上的chrome版本 是最新的话就下载这个
https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/


检查下 selenium调用chrome后 是不是没设置浏览器窗口大小
因为调用的是chrome的 capture node screenshot 可能node没显示全


跑的时候chrome里 开发者工具 alt+ctrl+p 然后 capture node screenshot 看看正不正常？

机械工业的，有人抓了电脑书的
```





