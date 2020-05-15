# -*- coding: GBK -*-
# coding: utf-8
# encoding=utf8

from __future__ import unicode_literals,print_function, absolute_import, division


import re
import copy
import chardet

import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import collections
from collections import defaultdict


from writemdict import MDictWriter, encrypt_key
from ripemd128 import ripemd128


head = 0
new_mean =[]
f=io.open('OALD4_azure.txt', 'r',encoding='utf-8')
#f=io.open('oxford2_original.txt', 'r',encoding='utf-8')
d = defaultdict(list) #建立一个空字典，也可使用{}建立。
for line in f: #每次从f中读入一行
    line=line.rstrip('\n')#去除行尾的换行符
    if line == '</>':
        if head == 2:
            new_mean[0:] = ["".join(new_mean[0:])]
            d[word].append(new_mean[0])
        head = 1;
        new_mean =[]
    elif head == 1:
        word = line
        head = 2
    elif head == 2:
        new_mean.append(line)
        head = 2
f.close()


ff=io.open('about_OX4.txt', 'r',encoding='utf-8')#词典about信息，txt文件请保存为utf-8
about=[]
for line in ff: #每次从f中读入一行
    about.append(line)
about[0:] = ["".join(about[0:])]


#outfile = open("example_output/新牛津Beta_V2.2.1.mdx", "wb")
#writer = MDictWriter(d, "新牛津Beta_V2.2.1", about[0])
outfile = open("output_ox4/OALD4_Ex.mdx", "wb")
writer = MDictWriter(d, "牛津高阶双解(第四版)", about[0])
writer.write(outfile)
outfile.close()

