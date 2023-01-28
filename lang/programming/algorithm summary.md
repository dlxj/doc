



# 基于AC自动机的快速分词

- https://kexue.fm/archives/3908



在KMP算法中，对于模式串”abcabcacab”，我们知道非前缀子串abc(abca)cab是模式串的一个前缀(abca)bcacab，而非前缀子串ab(cabca)cab不是模式串abcabcacab的前缀，根据此点，我们构造了next数组，实现在匹配失败时的跳转。

而在多模式环境中，AC自动是使用前缀树来存放所有模式串的前缀，然后通过失配指针来处理失配的情况。它大概分为三个步骤：**构建前缀树（生成goto表），添加失配指针（生成fail表），模式匹配（构造output表）**。下面，我们拿模式集合[say, she, shr, he, her]为例，构建一个AC 自动机。



# 同构——用数论指纹寻找子串排列

- https://www.ituring.com.cn/article/509742



