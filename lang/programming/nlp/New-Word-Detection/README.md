

时光荏苒 nlp dl【中文分词系列】 2. 基于切分的新词发现   [p](https://kexue.fm/archives/3913/comment-page-1) 

- [积分梯度：一种新颖的神经网络可视化方法](https://kexue.fm/archives/7533)
- [重新写了之前的新词发现算法：更快更好的新词发现](https://kexue.fm/archives/6920)



# **新词发现算法**(**New Word Detection**)   

Difference with the original fork: Updated to python 3

**参考：**  
**Reference:**  
  - 算法（Algorithm）：
    
    - >http://www.matrix67.com/blog/archives/5044  
  - 代码（Code）：  
    - > https://github.com/xiulonghan/wordSeg     
    
    - > https://github.com/Moonshile/ChineseWordSegmentation  

**代码说明：**  
**Code describing:**  
- extract.py:  
    提供文档中所有成词的可能组合，以及计算词的点互信息时的一个组合。  
    Providing all possible word combines in document, and computing all word combines of PMI.  
 - entropy.py:  
    计算左右邻居熵的大小  
    Computing left and right entropy of neighbors  
- wordseg.py:  
    根据计算出的频数、点互信息和左右熵来找出成词可能的组合，最后与词典对比找出新词。  
    Finding all possible word combines by frequency, PMI and left/right entropy of neighbors, then comparing with diction to detect new word.  