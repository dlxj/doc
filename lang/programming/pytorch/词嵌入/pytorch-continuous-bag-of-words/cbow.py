

"""
cbow 用上下文猜中间的词
    数据: 一编英文文章, 以及由这编文章得到的总共49 个不同的词, 每一个词分配一个数(0 ~ 48)
    输入: tensor( [ 前词数2, 前词数1, 后词数1, 后词数2 ] )
    输出: tensor( [[ 词1的概率, 词2的概率, ...  词49的概率 ]] )

    doc\lang\programming\深入理解神经网络: 从逻辑回归到CNN.md
"""

import torch
import torch.nn as nn


CONTEXT_SIZE = 2  # 2 words to the left, 2 to the right
EMDEDDING_DIM = 100

# 生成以空白分隔的49 个不同的词(包括后面的标点符号, 既标点符号也算是词的一部分)
raw_text = """We are about to study the idea of a computational process.
Computational processes are abstract beings that inhabit computers.
As they evolve, processes manipulate other abstract things called data.
The evolution of a process is directed by a pattern of rules
called a program. People create programs to direct processes. In effect,
we conjure the spirits of the computer with our spells.""".split()

# raw_text.append("<PAD>")  # 因为输入的句子长度不一，有的长有的短。长的截断，短的补齐；这个补齐就用词 "<PAD>" 
    # nn.Embedding 的第三个参数这样传: padding_idx=word_to_id['<PAD>']

# By deriving a set from `raw_text`, we deduplicate the array
vocab = set(raw_text)       # 词集合
vocab_size = len(vocab)     # 词个数

# 总共49 个不同的词，每一个词分配一个数(0 ~ 48)
word_to_ix = {word:ix for ix, word in enumerate(vocab)}  # 词 到 数 的字典
ix_to_word = {ix:word for ix, word in enumerate(vocab)}  # 数 到 词 的字典

# 构建训练数据，由上下文(context, 前后各两个词) 和目标词(target, 机器需要根据上下文猜的词) 组成
data = []
for i in range(2, len(raw_text) - 2):
    context = [raw_text[i - 2], raw_text[i - 1],
               raw_text[i + 1], raw_text[i + 2]]
    target = raw_text[i]
    data.append((context, target))

# 由一个上下文构造上下文张量(原始输入上下文是词列表但是机器只认得数, 所以要把词变成由数组成的张量)
def make_context_vector(context, word_to_ix):       # context: [ 前词2, 前词1, 后词1, 后词2 ]
    idxs = [word_to_ix[w] for w in context]         # idxs: [ 前词数2, 前词数1, 后词数1, 后词数2 ]
    return torch.tensor(idxs, dtype=torch.long)     # 返回由idxs 构造的 torch 张量，各分量类型为长整型long


class CBOW(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOW, self).__init__()

        """
        torch.nn.Embedding
            嵌入层
                嵌入层是一个可训练的网络结构, 有自已的可训练权重参数。它位于整个网络的最前部, 它后面还可以有其它隐层用于输出最终想要的结果(通常是概率的列表) 
                嵌入层的目的是用于得到嵌入向量。输入N个词数张量 tensor([词数1, 词数2, ..., 词数N]) , 输出N 个词数的嵌入向量 shape:torch.Size([N, 100])
                    相比原始的one-hot "独热" 表示(每一个词都是一个独立维度, 每一个词分配一个基向量, 有多少词就有多少维), 
                    嵌入向量是一种将one-hot 这个很长很长的向量, 压缩到低维的表示。比如现在最常用的100 ~ 200维之间。
                    词嵌入word embedding 通过读海量的文档内容, 能够理解词的意思, 比如它能知道 The cat sat on the pat和The dog sat on the pat这两句话中 cat和dog 的意思是接近的,
                    这是因为它把意思相近的词尽量放在空间上接近的位置, 这样用余弦相似度就能算出两个词的距离

            训练过程
                输入: 上下文张量 tensor([ 前词数2, 前词数1, 后词数1, 后词数2 ])
                前向传播:
                    上下文张量经过嵌入层的运算, 得到上下文嵌入向量 shape:torch.Size([4, 100])

                嵌入层的权重参数在训练过程中会不断更新优化
            初始化参数:
                num_embeddings (int): 词个数
                embedding_dim (int):  嵌入向量的维度(通常在100 ~ 200 维之间)
        """

        #out: 1 x emdedding_dim
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)  # 总共49 个词, 每个词用100 维的向量表示(就是嵌入向量)
        self.linear1 = nn.Linear(embedding_dim, 128)               # 隐层一: 输入维度(1*100), 输出维度 (1*128)
        self.activation_function1 = nn.ReLU()                      # 激活函数RELU
        
        #out: 1 x vocab_size
        self.linear2 = nn.Linear(128, vocab_size)                  # 隐层二: 输入维度 (1*128), 输出 (1*49)
        self.activation_function2 = nn.LogSoftmax(dim = -1)        # 激活函数LogSoftmax
        

    def forward(self, inputs):        # inputs shape:torch.Size([4])  # 输入由4 个词数组成(对应上下文的四个词)
        ed = self.embeddings(inputs)  # shape:torch.Size([4, 100])    # 得到4 个100 维的嵌入向量
        ed_sum = sum(ed)              # shape:torch.Size([100])       # 4 个嵌入向量求和
        embeds = ed_sum.view(1,-1)    # shape:torch.Size([1, 100])     
            # tensor.view(no_of_rows,no_of_columns) 改变张量的维度 .view(1,-1) 表示展平成1 行，列数自适应
        out = self.linear1(embeds)
        out = self.activation_function1(out)
        out = self.linear2(out)
        out = self.activation_function2(out)
        return out

    def get_word_emdedding(self, word):
        word = torch.tensor([word_to_ix[word]])
        return self.embeddings(word).view(1,-1)


model = CBOW(vocab_size, EMDEDDING_DIM)

loss_function = nn.NLLLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

#TRAINING
for epoch in range(50):
    total_loss = 0

    for context, target in data:
        context_vector = make_context_vector(context, word_to_ix)  

        log_probs = model(context_vector)  # tensor([词数1的概率, 词数2的概率, ..., 词数49 的概率]) # shape:torch.Size([1, 49])
        target_4_loss = torch.tensor([word_to_ix[target]]) # tensor([目标词数]) # shape:torch.Size([1])  

        total_loss += loss_function(log_probs, target_4_loss)

    #optimize at the end of each epoch
    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()

#TESTING
context = ['People','create','to', 'direct']
context_vector = make_context_vector(context, word_to_ix)
a = model(context_vector)

#Print result
print(f'Raw text: {" ".join(raw_text)}\n')
print(f'Context: {context}\n')
print(f'Prediction: {ix_to_word[torch.argmax(a[0]).item()]}')
