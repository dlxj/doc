
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # std 包在此模块的上上上级目录
import math
import std.iFile as iFile
import std.iJson as iJson
import std.iList as iList
import std.seg.iSeg as iSeg
import std.iSql as iSql
import util.saveTempData as saveTempData
import util.fectchData as fectchData

import requests

import hashlib
import re

# 提取专业词
def prowords(s, url="xxxxx.splitAll"):

    re = requests.post(url="xxxxxx.splitAll", data={'array':"""[{"id":"1","context":"$"}]""".replace('$', s)}, headers={'Content-Type':'application/x-www-form-urlencoded'}).json()

    if re['status'] == 200:
        data = re['data']
        wls = data[0]['words']
        prowords = [ d['word'] for d in wls if d['type'] == 'pro' ]
        return prowords
    else:
        return []

def rmspace(s):
    s = s.replace('\r\n', '\n')
    s = s.replace('\n\n', '\n')
    return s

def splitSentence(s):
    return re.compile('[\n|]').split(s)


if __name__ == "__main__":

    inp = 'GeeksforGeeks'
    result = hashlib.md5( bytes(inp, encoding='utf-8') )
    print("The byte equivalent of hash is : ", end ="")
    print(result.hexdigest())


    currDir = os.path.dirname(os.path.abspath(__file__))
    fname_pointTexts = os.path.join(currDir, 'pointTexts.json')
    fname_train = os.path.join(currDir, 'datasets', 'train.json')
    fname_user_dict = os.path.join(currDir, 'datasets', 'user_dict.txt')
    fname_user_dict2 = os.path.join(currDir, 'datasets', 'user_dict_2.txt')

    


    pointTexts = iJson.load_json( fname_pointTexts )

    datasets = []

    wordss = []
    wordss2 = []

    for k, v in pointTexts.items():
        k = rmspace(k)
        v = rmspace(v)
        v = v.replace('。', '。|')

        words = iSeg.segment(v)
        words = iSeg.unchinese_filter(words)
        words2 = list( filter(lambda s : len(s) == 2,words) )
        words = list( filter(lambda s : len(s) > 2,words) )
        words = list( set(words) )
        wordss += words

        words2 = list( set(words2) )
        wordss2 += words2
        

        sentences = splitSentence(v)
        sentences = list( filter(lambda s : s != '', sentences) )

        dataset = {"id": hashlib.md5( bytes(k, encoding='utf-8') ).hexdigest(),  "summary":k, "text": []}

        for s in sentences:
            dataset["text"].append( {"sentence": s, "label": 0} )

        datasets.append( dataset )

        # break


    wordss = list( set(wordss) )
    wordss2 = list( set(wordss2) )

    user_dict = list( map(lambda s : s+" 2000 n" , wordss ) )
    user_dict = "\n".join( user_dict )

    user_dict2 = "\n".join(wordss2)


    with open(fname_train, 'w', encoding='utf-8') as fp:
        for ds in datasets:
            js = iJson.string(ds)
            fp.write(js)
            fp.write('\n')

    with open(fname_user_dict, 'w', encoding='utf-8') as fp:
        fp.write(user_dict)
    
    with open(fname_user_dict2, 'w', encoding='utf-8') as fp:
        fp.write(user_dict2)

    print(1)


