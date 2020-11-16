
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

s = readstring('data.txt')
s = unchinese_remove(s)

#为了方便调用，自定义了一个正则表达式的词典
myre = {2:'(..)', 3:'(...)', 4:'(....)', 5:'(.....)', 6:'(......)', 7:'(.......)'}

min_count = 2 # 10 #录取词语最小出现次数
min_support = 30 # 30 #录取词语最低支持度，1代表着随机组合  # 凝合程度 = 词概率 / 里面所有字随机拼在一起的概率
min_s = 3 #录取词语最低信息熵，越大说明越有可能独立成词
max_sep = 4 #候选词语的最大字数
t=[] #保存结果用。


t.append(pd.Series(list(s)).value_counts()) #逐字统计
tsum = t[0].sum() # 总共有多少个字
rt = [] #保存结果用
"""
t[0] 存所有的字，还有每个字出现的次数，降序
"""

for N in range(2, 4+1): # max_sep+1
    print(f'正在生成{N}-Gram词...')
    t.append([])
    for i in range(N): #生成所有可能的m字词
        t[N-1] = t[N-1] + re.findall(myre[N], s[i:])
    
    t[N-1] = pd.Series(t[N-1]).value_counts() #逐词统计
    t[N-1] = t[N-1][t[N-1] > min_count] #最小次数筛选
    tt = t[N-1][:]
    """
    tt 是出现大于一定次数的N-gram词，及其出现次数
    tt.index 是所有大于一定次数的N-gram词
    NS 是一个大于一定次数的N-gram词

        N in 2...4
            K in 0...N-2
                ms[:N-1-k] = N-gram 的第一字 if N ==2；                N-gram 的第一二字          if N ==3； 
                ms[N-1-k:] = N-gram 的第二到尾部的所有字 if N ==2；    N-gram 的第三到尾部的所有字 if N ==3；
    

    NS[:N-1-k], for N in 2...4, K in 0...N-2
        N-1-k in [ (1...1), (2...1), (3...1) ]
        # N-Gram 的(第一字)，(第一二字，第一字)，(第一二三字，第一二字，第一字) 

    ms[m-1-k:]
        # N-Gram 的(第二字)，(第三字，第二三字)，(第四字，第三四字，第二三四字)  
    
    """

    for k in range(N-1):
        qq = np.array(list(map(lambda ms: tsum*t[N-1][ms]/t[N-2-k][ms[:N-1-k]]/t[k][ms[N-1-k:]], tt.index))) > min_support #最小支持度筛选。  #凝合程度

if __name__ == "__main__":

    

    print(',,,')







