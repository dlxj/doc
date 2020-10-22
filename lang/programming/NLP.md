

CS520 斯坦福大学2020公开课知识图谱Knowledge Graphs



LTP 4 哈工大  分词、词性标注、句法分析

https://github.com/HIT-SCIR/ltp



Gephi  可视化



mysql ->networkx ->gexf ->gephi



知识图谱—实体对齐

https://zhuanlan.zhihu.com/p/166497677



Facebook 人工智能团队已经创建并正在开放源代码 PyTorch Biggraph（PBG）。

PBG 是一个用于学习大规模图嵌入的分布式系统，特别适用于处理具有多达数十亿实体和数万亿条边的大型网络交互图。



动手学深度学习  PyTorch版

https://tangshusen.me/Dive-into-DL-PyTorch/#/



Word2Vec-知其然知其所以然

https://www.zybuluo.com/Dounm/note/591752



[NLP] 秒懂词向量Word2vec的本质

https://zhuanlan.zhihu.com/p/26306795


> 『Skip-gram 模型』：求某个中间词的可能**前后词**
>
> 『CBOW 模型』：求前后词的可能**中间词**



论文 word2vec Parameter Learning Explained

https://arxiv.org/abs/1411.2738



百度架构师手把手带你零基础入门深度学习

https://www.bookstack.cn/read/paddlepaddle-tutorials/8277f3a799031f9d.md



深度学习推荐系统-Embedding

https://zhuanlan.zhihu.com/p/266053280

> 一、为什么 Embedding 技术对于推荐系统如此重要?
>
> Embedding 向量间的运算能够揭示词之间的性别关系、词之间的时态关系。
>
> - **Embedding 是处理稀疏特征的利器**。可以将稀疏高维特征向量转换成稠密低维特征向量。
> - **Embedding 可以融合大量有价值信息，是极其重要的特征向量**。特别是 Graph Embedding 技术被提出后，Embedding 几乎可以引入任何信息进行编码，使其本身就包含大量有价值的信息，所以通过**预训练**得到的 Embedding 向量本身就是极其重要的特征向量。
>
> 二、经典的Embedding 方法有哪些？
>
> - Word2vec
> - item2vec
> - Graph Embedding
> 



2、Word2vec 的样本是怎么生成的？

以Skip-gram为例，选取“Embedding 技术对深度学习推荐系统的重要性”作为句子样本。首先，对它进行分词、去除停用词的过程，生成词序列，再选取大小为 3 的滑动窗口从头到尾依次滑动生成训练样本，然后我们**把中心词当输入，边缘词做输出**，就得到了训练 Word2vec 模型可用的训练样本。

3、Word2vec 模型的结构是什么样的？

本质上就是一个三层的神经网络

输入层和输出层的维度都是 V，这个 **V 其实就是语料库词典的大小**，这里的**输入向量是由输入词转换而来的 One-hot 编码向量**，**输出向量是由多个输出词转换而来的 Multi-hot 编码向量**，显然，基于 Skip-gram 框架的 Word2vec 模型解决的是一个多分类问题。

**隐层的维度是 N，N 的选择就需要一定的调参能力**，要对模型的效果和模型的复杂度进行权衡，来决定最后 N 的取值，最终每个词的 Embedding 向量维度也由 N 来决定。

**隐层神经元是没有激活函数的**，或者说采用了输入即输出的恒等函数作为激活函数，而**输出层神经元采用了 softmax 作为激活函数**。

4、怎样把词向量从 Word2vec 模型中提取出来？

Embedding 在 输入层到隐层的权重矩阵 WVxN 中，**输入向量矩阵 WVxN 的每一个行向量对应的就是我们要找的“词向量。**

在实际的使用过程中，我们往往会把输入向量矩阵转换成**词向量查找表**。在转换为词向量 Lookup table 后，每行的权重即成了对应词的 Embedding 向量



word2vec中，有一个默认程序distance，可以用来计算给定词的最相近的top 40个词



word2vec和BERT，都是语言表示中的**里程碑式的工作**，前者是词嵌入范式的代表，后者是预训练范式的代表。



word2vec由词义的分布式假设(**一个单词的意思由频繁出现在它上下文的词给出**)出发，最终得到的是一个look-up table，每一个单词被映射到一个唯一的稠密向量。这显然不是一个完美的方案，它无法处理一词多义(polysemy)问题





**词向量模型**

> 把词转换为向量
>
> 让向量具有语义信息



**Embedding Lookup**

> 输入词，得到词向量
>
> 实际场景中，我们**需要把Embedding Lookup的过程转换为张量计算**





<img src="NLP.assets/image-20201019174924755.png" alt="image-20201019174924755" style="zoom:50%;" />



> - 经过One-Hot Encoding后，句子“我，爱，人工，智能”就被转换成为了一个形状为 4 * 50000 的张量，记为
>
> ![如何把词转换为向量 - 图3](NLP.assets/ee7ce256f16a85ae1d2d17c0c6d3fef7.png) 。在这个张量里共有4行、50000列，从上到下，每一行分别代表了“我”、“爱”、“人工”、“智能”四个单词的One-Hot Encoding。最后，我们把这个张量 ![如何把词转换为向量 - 图4](NLP.assets/9a9408b824821df4aa6aea54f2598d1d.png) 和另外一个稠密张量 ![如何把词转换为向量 - 图5](NLP.assets/722dbac8bbd42242bde7acce7411d232.png) 相乘，其中 ![如何把词转换为向量 - 图6](NLP.assets/aa727e2ebd76069da36d193d16ef33ab.png) 张量的形状为50000 *128（50000表示词表大小，128表示每个词的向量大小）。经过张量乘法，我们就得到了一个4*128的张量，从而完成了把单词表示成向量的目的。





在自然语言处理任务中，词向量（word2vec）是表示自然语言里单词的一种方法，即**把每个词都表示为一个N维空间内的点，即一个高维空间内的向量**。通过这种方法，实现**把自然语言计算转换为向量计算**。

从而**达到让计算机像计算数值一样去计算自然语言的目的**。





word embedding  **词嵌入**

> 把词映射为实数域向量的技术也叫词嵌入（word embedding）
>
> > **让词和实数一一对应，或着和向量一一对应，这就是词嵌入**



word2vec 它将每个词表示成一个定长的向量，并使得这些向量能较好地**表达不同词之间的相似和类比关系**。

**Word2vec的模型以大规模语料库作为输入，然后生成一个向量空间（通常为几百维）。词典中的每个词都对应了向量空间中的一个独一的向量，而且语料库中拥有共同上下文的词映射到向量空间中的距离会更近**。





当模型训练完后，最后得到的其实是**神经网络的权重**，比如现在输入一个 x 的 one-hot encoder: [1,0,0,…,0]，对应刚说的那个词语『吴彦祖』，则在输入层到隐含层的权重里，只有对应 1 这个位置的权重被激活，这些权重的个数，跟隐含层节点数是一致的，从而这些权重组成一个向量 vx 来表示x，而因为每个词语的 one-hot encoder 里面 1 的位置是不同的，所以，这个向量 vx 就可以用来唯一表示 x。

**注意：上面这段话说的就是 Word2vec 的精髓！！**





**skip-gram 跳字模型**



**CBOW**（continuous bag of words）**连续词袋模型**
=======




**CBOW**（continuous bag of words）**连续词袋**



CBOW的全称是continuous bag of words。和传统的N-gram相比，CBOW会同时左右各看一部分词。也就是说，根据左右两边的词，猜测中间的词是什么。而传统的N-gram是根据前面的词，猜后面的词是什么。在PyTorch的官网上给出了N-gram的实现。因此我们只需要在这个基础上进行简单的修改就可以得到基于CBOW的W2V模型。





word2vec  **相似词发现**

基于PyTorch实现word2vec模型

**上下文相似的两个词,它们的词向量也应该相似**, 比如香蕉和梨在句子中可能经常出现在相同的上下文中，因此这两个词的表示向量应该就比较相似





















