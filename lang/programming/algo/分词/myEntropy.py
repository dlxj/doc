

# https://kexue.fm/archives/3491

"""
N-Gram 要经过三次筛选：
    第一次：出现次数要大于一定次数
    第二次：凝合程度要大于一定值
    第三次：左邻右邻信息熵足够丰富
筛剩下的N-Gram 可以认为是真正的“词”
"""

import numpy as np
import pandas as pd
import re
from numpy import log, min

def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

"""
读取中文文本，去掉所有非中文内容
"""
s = readstring('data.txt')
s = unchinese_remove(s)

s = s[:10000]

MAX_N = 5 # N-Gram 词的最大长度
min_count = 10 #录取词语最小出现次数
min_sticky = 30 # 30 #录取词语最低支持度，1代表着随机组合  # 凝合程度 = 词概率 / 里面所有字随机拼在一起的概率
min_s = 3 #录取词语最低信息熵，越大说明越有可能独立成词
t = []    # 保存结果
rt = []   # 保存结果
"""
t[0]：  1-Gram 所有词出现次数
t[1]：  2-Gram 所有词出现次数
.
.
.
t[N-1]  N-Gram 所有词出现次数
"""

t.append(pd.Series(list(s)).value_counts()) # 所有字的出现次数
total_alphabets = t[0].sum() # 总共有多少个字

# print(list(s))

if __name__ == "__main__":
    for N in range(2, MAX_N+1):
        print(f'正在生成{N}-Gram词...')
        t.append([])
        for i in range(0,len(s)):
            if i+N <= len(s):
                t[N-1].append( s[i:N+i] )
            
        t[N-1] = pd.Series(t[N-1]).value_counts()  # 所有N-Gram 词出现次数
        t[N-1] = t[N-1][t[N-1] > min_count]        # 第一次筛选：最小出现次数
        tt = t[N-1][:]


        """
        为了算出一个文本片段的凝合程度，我们需要枚举它的凝合方式——这个文本片段是由哪两部分组合而来的
        取所有组合中凝合程度最小的作为N-Gram 词的凝合程度

        “电影院”的凝合程度就是 p(电影院) 与 p(电) · p(影院) 比值和 p(电影院) 与 p(电影) · p(院) 的比值中的较小值
        “的电影”的凝合程度则是 p(的电影) 分别除以 p(的) · p(电影) 和 p(的电) · p(影) 所得的商的较小值。”
        """

        """
        自运用程度定义为它的左邻字信息熵和右邻字信息熵中的较小值

        “吃葡萄不吐葡萄皮不吃葡萄倒吐葡萄皮”，“葡萄”一词出现了四次，其中左邻字分别为 {吃, 吐, 吃, 吐} ，右邻字分别为 {不, 皮, 倒, 皮} 。根据公式，“葡萄”一词的左邻字的信息熵为 – (1/2) · log(1/2) – (1/2) · log(1/2) ≈ 0.693 ，它的右邻字的信息熵则为 – (1/2) · log(1/2) – (1/4) · log(1/4) – (1/4) · log(1/4) ≈ 1.04

        """

        will_drops = []

        # 算凝合程度
        for word in tt.index:
            
            n_word = t[N-1][word]              # 某个N-Gram 词出现次数
            p_word = n_word / total_alphabets  # 该N-Gram 词在所有字中出现的概率
            """
            把某个N-Gram 拆成两部分，算这两部分随机“粘” 在一起的概率，N-Gram 在所有字中出现的概率 / 那个“粘” 在一起的概率 就是凝合程度
            枚举所有拆成两部分的可能，算出全部凝合程度，取其中的最小值作为N-Gram 词的凝合程度
            """

            stickys = []
            # 把word 拆成两部分
            for k in range(N-1):
                left = word[:k+1]
                right = word[k+1:]
                n_left = t[ len(left) - 1 ][ left ]     # 左边词出现次数
                n_right = t[ len(right) - 1 ][ right ]  # 右边词出现次数
                
                # sticky =  (n_word / total_alphabets) / ( ( n_left / total_alphabets ) * ( n_right / total_alphabets )  )
                # = (n_word  * total_alphabets) / (n_left * n_right)
                # = n_word  * total_alphabets / n_left / n_right

                sticky = (n_word / n_left) * (total_alphabets / n_right)
                stickys.append( sticky )

            sticky = min( stickys )
            if sticky < min_sticky:
                will_drops.append( word )

        tt = tt.drop(labels=will_drops)  # 第二次筛选：凝合程度
        rt.append( tt.index )


    for N in range(2, MAX_N+1):
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


    print(',,')







