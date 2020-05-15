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
d = defaultdict(list) #����һ�����ֵ䣬Ҳ��ʹ��{}������
for line in f: #ÿ�δ�f�ж���һ��
    line=line.rstrip('\n')#ȥ����β�Ļ��з�
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


ff=io.open('about_OX4.txt', 'r',encoding='utf-8')#�ʵ�about��Ϣ��txt�ļ��뱣��Ϊutf-8
about=[]
for line in ff: #ÿ�δ�f�ж���һ��
    about.append(line)
about[0:] = ["".join(about[0:])]


#outfile = open("example_output/��ţ��Beta_V2.2.1.mdx", "wb")
#writer = MDictWriter(d, "��ţ��Beta_V2.2.1", about[0])
outfile = open("output_ox4/OALD4_Ex.mdx", "wb")
writer = MDictWriter(d, "ţ��߽�˫��(���İ�)", about[0])
writer.write(outfile)
outfile.close()

