# Mecab 日语分词
​	https://pypi.org/project/mecab-python3/



## 安装Mecab



### OSX

```
rm - rf /usr/local/var/homebrew/locks
brew search mecab
brew install mecab
brew install mecab-ipadic
# pip install mecab-python3  # 装完找不到可执行文件
```



To enable mecab-ipadic dictionary, add to /usr/local/etc/mecabrc:

 dicdir = /usr/local/lib/mecab/dic/ipadic

/usr/local/Cellar/mecab-ipadic/2.7.0-20070801



##  命令行执行



```
echo "じゃあランタン点けていいですか" | mecab
```







