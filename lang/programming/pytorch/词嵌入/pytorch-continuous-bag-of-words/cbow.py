

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

raw_text = """We are about to study the idea of a computational process.
Computational processes are abstract beings that inhabit computers.
As they evolve, processes manipulate other abstract things called data.
The evolution of a process is directed by a pattern of rules
called a program. People create programs to direct processes. In effect,
we conjure the spirits of the computer with our spells.""".split()


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
            词嵌入类: 
                用于存储词嵌入, 以及支持通过索引列表取回词嵌入
            初始化参数:
                num_embeddings (int): 词个数
                embedding_dim (int):  嵌入向量的维度(通常在100 ~ 200 维之间)
        """

        #out: 1 x emdedding_dim
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)  # 49 个词, 每个词100 维
        self.linear1 = nn.Linear(embedding_dim, 128)               # 输入层100 维，隐层一 128 维
        self.activation_function1 = nn.ReLU()                      # 激活函数RELU
        
        #out: 1 x vocab_size
        self.linear2 = nn.Linear(128, vocab_size)                  # 隐层二 49 维
        self.activation_function2 = nn.LogSoftmax(dim = -1)        # 激活函数LogSoftmax
        

    def forward(self, inputs):
        embeds = sum(self.embeddings(inputs)).view(1,-1)
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

        log_probs = model(context_vector)

        total_loss += loss_function(log_probs, torch.tensor([word_to_ix[target]]))

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
