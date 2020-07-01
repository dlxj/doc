
import re
import math
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname( os.path.dirname(os.path.abspath(__file__)))))  # std 包在此模块的上上上级目录
sys.path.append( os.path.dirname(os.path.abspath(__file__) ) )


link = """<a class="el-s-dl" href="ed2k://|file|%5B%E6%A3%92%E7%90%83%E8%8B%B1%E8%B1%AA%5D.%5Bzhbconan%5D%5BTouch%5D%5B001%5D%5BHDTVRip%5D%5B1440x1080%5D%5BAVC_AAC_AC3%5D%5BCHS%26JPN%5D.mkv|994442543|e0b66b719af16c5a1cdc469888f88434|h=qhx5ep62pnbqjzaya3f76i3hz5hybrle|/" ed2k="ed2k://|file|%5B%E6%A3%92%E7%90%83%E8%8B%B1%E8%B1%AA%5D.%5Bzhbconan%5D%5BTouch%5D%5B001%5D%5BHDTVRip%5D%5B1440x1080%5D%5BAVC_AAC_AC3%5D%5BCHS%26JPN%5D.mkv|994442543|e0b66b719af16c5a1cdc469888f88434|h=qhx5ep62pnbqjzaya3f76i3hz5hybrle|/">[棒球英豪].[zhbconan][Touch][001][HDTVRip][1440x1080][AVC_AAC_AC3][CHS&amp;JPN].mkv</a>"""

#r"""<a class="el-s-dl" href="(ed2k://|file|).+?">"""


def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def writestring(fname, strs):
    with open(fname, "w", encoding="utf-8") as fp:
        fp.write(strs)
        fp.close()

if __name__ == "__main__":

    currDir = os.path.dirname(os.path.abspath(__file__))
    fname_html = os.path.join(currDir, '《棒球英豪》(Touch)[台配国语_日语][101话全集][1080P] _ 漫步星尘大海.html')
    fname_results = os.path.join(currDir, 'results.txt')
    
    data = readstring(fname_html)

    #links = re.compile(r"""<a class="el-s-dl" href="(ed2k://|file|.+?)">""").findall(link)
    links = re.compile(r"""<a class="el-s-dl" href="(ed2k://|file|.+?)">""").findall(data)
    print('ed2k links num:', len(links))
    results = []
    for s in links:
        pair = re.compile(r"ed2k://\|file\|.*?\|/").findall(s)
        results.append(pair[0])
    
    print("\n".join(results))

    writestring(fname_results, "\n".join(results))

    
    

    #pair = re.compile(r"ed2k://\|file\|.*?\|/").findall(links[0])

    #print( pair[0] )


    #print(link)


