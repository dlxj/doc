
import numpy as np

CONTEXT_SIZE = 2  # 2 words to the left, 2 to the right
EMDEDDING_DIM = 100

batch = 3

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

# 49 个词对应的 onehot
onehots = np.identity(vocab_size) # shape:(49, 49) , 每个词49 维；因为每个词都单独分配一个维度给它, 
    # 一个onhot 就是一个基向量, 而且彼此正交


"""

(1 * 49)  (49 * 100) -> (1 * 100)
  独热       嵌入层       嵌入向量

"""

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
    return np.array( idxs, np.float)                # 返回由idxs 构造的 torch 张量，各分量类型为长整型long

"""
()
"""

class CBOW():
    def __init__(self, vocab_size, embedding_dim):
        self.W = np.random.uniform(size=(3, 1))   # 3*1 权重





