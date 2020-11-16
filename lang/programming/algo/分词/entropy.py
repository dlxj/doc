

# https://kexue.fm/archives/3491

import numpy as np
import pandas as pd
import re
from numpy import log,min

def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

# f = open('data.txt', 'r') #读取文章
# s = f.read() #读取为一个字符串

s = readstring('data.txt')
s = unchinese_remove(s)

s = s[:1000]

#定义要去掉的标点字
# drop_dict = [u'，', u'\n', u'。', u'、', u'：', u'(', u')', u'[', u']', u'.', u',', u' ', u'\u3000', u'”', u'“', u'？', u'?', u'！', u'‘', u'’', u'…']
# for i in drop_dict: #去掉标点字
#     s = s.replace(i, '')

#为了方便调用，自定义了一个正则表达式的词典
myre = {2:'(..)', 3:'(...)', 4:'(....)', 5:'(.....)', 6:'(......)', 7:'(.......)'}

min_count = 10 # 10 #录取词语最小出现次数
min_support = 30 # 30 #录取词语最低支持度，1代表着随机组合  # 凝合程度 = 词概率 / 里面所有字随机拼在一起的概率
min_s = 0.1 #录取词语最低信息熵，越大说明越有可能独立成词
max_sep = 5 #候选词语的最大字数
t=[] #保存结果用。


counts = pd.Series(list(s)).value_counts() # 每个字出现多少次
totol = counts.sum()  # 总共有多少个字

t.append(pd.Series(list(s)).value_counts()) #逐字统计
tsum = t[0].sum() #统计总字数
rt = [] #保存结果用

"""
以出现次数、凝合程度、自由运用程度，这三个条件来对所有词进行筛选
    凝合程度 = 词概率  /  里面所有字随机拼在一起的概率

    定义“电影院”的凝合程度就是 p(电影院) 与 p(电) · p(影院) 比值和 p(电影院) 与 p(电影) · p(院) 的比值中的较小值
"""

for m in range(2, max_sep+1):
    print(u'正在生成%s字词...'%m)
    t.append([])
    for i in range(m): #生成所有可能的m字词
        t[m-1] = t[m-1] + re.findall(myre[m], s[i:])
    
    t[m-1] = pd.Series(t[m-1]).value_counts() #逐词统计
    t[m-1] = t[m-1][t[m-1] > min_count] #最小次数筛选  
    tt = t[m-1][:]
    """
    tt 是出现大于一定次数的N-gram词，及其出现次数
    tt.index 是所有大于一定次数的N-gram词
    ms 是一个大于一定次数的N-gram词
    t[m-1] 是m-Gram 的 词-次数 字典
    t[m-2-k] 是 字-次数 字典
    t[k] 是 字-次数 字典? 2-Gram 词-次数 字典？

    """

    list(map(lambda ms: ms, tt.index))

    """
    m = 2  # 2-Gram
    k = 0...m-2
    ms[:m-1-k] = N-gram 的第一字 if m ==2；                N-gram 的第一二字          if m ==3； 
    ms[m-1-k:] = N-gram 的第二到尾部的所有字 if m ==2；    N-gram 的第三到尾部的所有字 if m ==3； 


    总字数 * 候选词出现的次数 / 词切分组合左出现的次数 / 词切分组合右出现的次数  # 是根据词频的定义化简得到的结果
        是每一种切分都算一个qq，然后用qq去筛选，每个n-gram都要经过n-1个qq去筛选

        “电影院”的凝合程度就是 p(电影院) 与 p(电) · p(影院) 比值和 p(电影院) 与 p(电影) · p(院) 的比值中的较小值
        “的电影”的凝合程度则是 p(的电影) 分别除以 p(的) · p(电影) 和 p(的电) · p(影) 所得的商的较小值。”

    总字数 * 词次数 / 词的第一字次数

    """

    for k in range(m-1):
        qq = np.array(list(map(lambda ms: tsum*t[m-1][ms]/t[m-2-k][ms[:m-1-k]]/t[k][ms[m-1-k:]], tt.index))) > min_support # 最小支持度筛选。  #凝合程度
        tt = tt[qq]
    rt.append(tt.index)

def cal_S(sl): # 信息熵计算函数
    return -((sl/sl.sum()).apply(log)*sl/sl.sum()).sum()

for i in range(2, max_sep+1):
    print(u'正在进行%s字词的最大熵筛选(%s)...'%(i, len(rt[i-2])))
    pp = [] #保存所有的左右邻结果
    for j in range(i+2):
        pp = pp + re.findall('(.)%s(.)'%myre[i], s[j:])
    pp = pd.DataFrame(pp).set_index(1).sort_index() # 先排序，这个很重要，可以加快检索速度
    print( type(pp.index) )
    index = np.sort(np.intersect1d(rt[i-2], pp.index)) # 作交集
    # 下面两句分别是左邻和右邻信息熵筛选
    index = index[np.array(list(map(lambda s: cal_S(pd.Series(pp[0][s]).value_counts()), index))) > min_s]
    rt[i-2] = index[np.array(list(map(lambda s: cal_S(pd.Series(pp[2][s]).value_counts()), index))) > min_s]

#下面都是输出前处理
for i in range(len(rt)):
    t[i+1] = t[i+1][rt[i]]
    t[i+1].sort_values(ascending = False)

#保存结果并输出
pd.DataFrame(pd.concat(t[1:])).to_csv('result.txt', header = False)



