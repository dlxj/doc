
import math
import numpy as np

"""
功能：文本摘要算法实现(TextRank for Text Summarization)
TextRank 从PageRank 发展而来，PageRank 是计算网站重要性的算法，这里将用一个通俗的比喻来解释它的含义： 极简“个人价值模型” 
	在这个模型里面，PageRank 是说：个人价值与自身努力无关，也不靠拼爹，完全由你的朋友数量决定。朋友越多你的价值越高，
		价值计算过程很简单，假设你有N 个朋友，那么你要把自身价值均分给你的每一个朋友，既你的每一个朋友都得到你个人价值的 1/N，并且所有人都要这么做，均分自已的价值，所以这是一个循环计算的过程。
		细节：
			1. 所有人的价值都初始化为0.15
			2. 每个人都有一个基础价值0.15，如果一个人完全没有朋友，那么他的价值就是0.15
			3. 所有均分出去的价值都要抽税，既对方能得到的值是：  0.85 * 1/N * 你的价值
			4. 所以你对你的每一个朋友的贡献值都是： 0.85 * 1/N * 你的价值
			5. 你的价值等于所有朋友对你的贡献总和再加上基础价值0.15
			6. 循环计算所有人的价值，经过若干次计算以后结果会收敛到稳定值
	
	TextRank 是说：朋友里面也还分好朋友和一般的朋友，关系好的就要多分一点。 
		对应文本摘要算法，“关系好”就是句子之间的相似度高，把相似度作为边的权重
		TextRank 和PangeRank 的唯一差别就在那个 1/N 上面，TextRank 用某种方法替换了 1/N,
			1/N 的替换方法是： 你和某个朋友的相似度  /  你和所有朋友之间的相似度总和 
		细节：
			替换了那个1/N 以后，所有计算过程和PageRank 相同
"""

# 相似度计算公式参见原始论文：《TextRank: Bringing Order into Texts》by: Rada Mihalcea and Paul Tarau

def similarOfSents(words1, words2):
	"""
	words1:句子1的词list
	words2:句子2的词list
	"""
	intersects = [] # 两个词集合words1，words2 的交集
	for w in words1:
		if w in words2:
			if w not in intersects:
				intersects.append(w)
	numerator = len(intersects)  # 分子是交集的元素个数
	if numerator == 0:
		return 0.0
	denominator = math.log(len(words1)) + math.log(len(words2))  # 分母是句子对应的词集长度分别求对数，然后相加
	if denominator < 1e-12:
		return 0.0

	return numerator / denominator

# 构造相似度邻接矩阵
# wordsList: 句子词向量列表 example: [ ['a', 'b', 'c'], ['a', 'b', 'f'], ['a', 'h', 'i'] ]
def similarMatrix(wordsList):
	n = len(wordsList)
	adjacentMatrix = np.zeros((n, n))
	"""
	邻接矩阵，里面存的是相似度，相似度可以用作graph 边的权值
	"""
	for i in range(0, n):
		for j in range(i+1, n):
			sim = similarOfSents(wordsList[i], wordsList[j])
			adjacentMatrix[i, j] = sim
			adjacentMatrix[j, i] = sim
	return adjacentMatrix


# 构造权值邻接矩阵
# simMatrix: 相似度邻接矩阵
def weightMatrix(simMatrix):
	"""
	graph 是一个有向图，结点是句子， \
		边的意义是两句子相似，箭头指向的意义是价值传递的方向，  \
		权值的意义是你愿意把自已价值的百分之几传递给箭头指向的那个结点。 \
		计算A -> B 的权值的方法是：  \
			先算A 和所有结点相似度的总和，这是分母  \
			再算A 和B 的相似度，这是分子  \
			两者的比值既是A -> B的边的权值
		注意：严格说来，这里的相似度才是论文中所指的权重， \
			而这里的权值实际上是论文公式后半段带小求和的分子除以分母的部分，  \
			但考虑到权值的意义这么定义更清晰，所以是值得的
	"""
	n = len(simMatrix)
	weightMtrx = np.zeros((n, n))
	
	for i in range(0, n):
		sumsim = sum( simMatrix[i] )  # 句子i 和其他所有结点相似度的总和
		for j in range(0, n):
			if i != j and simMatrix[i][j] > 0.001 and sumsim > 1e-12:  # 相似度小于一定值，认为结点之间没有边
				weightMtrx[i][j] = simMatrix[i][j] / sumsim
	
	return weightMtrx			

# 计算句子textrank 值(价值，或者说“重要性”)
# wordsList: 句子词向量列表 example: [ ['a', 'b', 'c'], ['a', 'b', 'f'], ['a', 'h', 'i'] ]
def textrank(wordsList):
	"""
	这个版本的实现是networkx 库的实现，和Matlab 中内置的算法实现结果是一至的，  \
		但是和论文公式的计算过程有差异，严格按照论文的实现在textrank2 函数
	"""
	N = len(wordsList)

	simMatrix = similarMatrix(wordsList) # 相似度邻接矩阵
	print("similary matrix:\n ", simMatrix, "\n\n")

	W = weightMatrix(simMatrix)  # 权值邻接矩阵
	print("weight matrix:\n ", W, "\n\n")

	WS = np.full(N, 1/N) # TextRank 初始值  list ，1*N 维，初值1/N
	for _ in range(0, 100):
		WS_last = WS
		WS = [0, 0, 0]
		for i in range(0, N):
			for j in range(0, N):
				if i != j and W[i][j] > 0:
					WS[j] += 0.85 * WS_last[i] * W[i][j]  # 先算i 为别人做了多少贡献
			WS[i] += 0.15 * 1 / N  # 再算别人为i 做了多少贡献
	
	print ("textrank值：\n", WS, "\n", sum(WS))
	return WS


# 严格按照论文公式计算
def textrank2(wordsList):

	N = len(wordsList)

	simMatrix = similarMatrix(wordsList) # 相似度邻接矩阵
	print("similary matrix:\n ", simMatrix, "\n\n")

	W = weightMatrix(simMatrix)  # 权值邻接矩阵
	print("weight matrix:\n ", W, "\n\n")

	WS = np.full(N, 0.15) # TextRank 初始值  list ，1*N 维，初值0.15
	
	for _ in range(100):
		for i in range(0, N):
			s = 0 # 其他结点给句子i 的贡献总和
			for j in range(0, N):
				if i != j and W[i][j] > 0:
					s += W[j][i] * WS[j]  # 句子j 的价值是WS[j]，把自已的价值按百分比贡献给句子i，这个比值是边的权值 W[j][i] (j -> i)
			WS[i] = 0.15 + 0.85 * s

	print ( WS )

	"""
	评论：得到的结果和前一个实现有差异，Matlab 原生实现和前一个实现版本是一至的，  \
		因为其他实现相当于对结果作了归一化，使得所有句子TextRank 值的总和为1，也就是百分百。  \
		如果我们也对最后的结果WS 作一次归一化就会发现和它们的结果是一模一样的,  \
			归一化的方法是：所有TextRank 值分别除以TextRank 总和
	"""

	return WS


if __name__ == "__main__":
	textrank( [ ['a', 'b', 'c'],
				 ['a', 'b', 'f'],
				 ['a', 'h', 'i']
		  	   ])

	textrank2( [ ['a', 'b', 'c'],
				 ['a', 'b', 'f'],
				 ['a', 'h', 'i']
		  	   ])
	print ( 1.11038961 / (1.11038961 + 1.11038961 + 0.77922078), 0.77922078 / (1.11038961 + 1.11038961 + 0.77922078) )  # 比较归一化后的结果