
import math
import numpy as np

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
		注意：严格说来，这里的相似度才是论文中所指的权值， \
			而这里的权值实际上是论文公式后半段带小求和的分子除以分母的部分，  \
			但考虑到权值的意义这么定义更清晰，所以是值得的
	"""
	n = len(simMatrix)
	weightMtrx = np.zeros((n, n))
	
	for i in range(0, n):
		sumsim = sum( simMatrix[i] )  # 句子i 和其他所有结点相似度的总和
		for j in range(0, n):
			if i != j and simMatrix[i][j] > 0.001 and sumsim != 0:  # 相似度小于一定值，认为结点之间没有边
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
	"""
	没有考虑孤立结点的贡献值(没有边的结点)
	"""
	N = len(wordsList)

	simMatrix = similarMatrix(wordsList) # 相似度邻接矩阵
	print("similary matrix:\n ", simMatrix, "\n\n")

	W = weightMatrix(simMatrix)  # 权值邻接矩阵
	print("weight matrix:\n ", W, "\n\n")

	WS = np.full(N, 0.15) # TextRank 初始值  list ，1*N 维，初值1/N
	
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
		实际上这个实现一点问题没有，因为其他实现相当于对结果作了归一化，使得所有句子TextRank 值的总和为1，也就是百分百。  \
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