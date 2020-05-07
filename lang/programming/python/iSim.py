
import math
import numpy as np
import networkx as nx

# 相似度计算公式参见原始论文：《TextRank: Bringing Order into Texts》by: Rada Mihalcea and Paul Tarau

def cal_sim(wordlist1, wordlist2):
    """
    给定两个句子的词列表，计算句子相似度。计算公式参考Textrank论文
    :param wordlist1:
    :param wordlist2:
    :return:
    """
    co_occur_sum = 0
    wordset1 = list(set(wordlist1))
    wordset2 = list(set(wordlist2))
    for word in wordset1:
        if word in wordset2:
            co_occur_sum += 1.0
    if co_occur_sum < 1e-12:  # 防止出现0的情况
        return 0.0
    denominator = math.log(len(wordset1)) + math.log(len(wordset2))
    if abs(denominator) < 1e-12:
        return 0.0
    return co_occur_sum / denominator


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

def pagerank(G, alpha=0.85, personalization=None,
             max_iter=100, tol=1.0e-6, nstart=None, weight='weight',
             dangling=None):
    """Returns the PageRank of the nodes in the graph.
    PageRank computes a ranking of the nodes in the graph G based on
    the structure of the incoming links. It was originally designed as
    an algorithm to rank web pages.
    Parameters
    ----------
    G : graph
      A NetworkX graph.  Undirected graphs will be converted to a directed
      graph with two directed edges for each undirected edge.
    alpha : float, optional
      Damping parameter for PageRank, default=0.85.
    personalization: dict, optional
      The "personalization vector" consisting of a dictionary with a
      key some subset of graph nodes and personalization value each of those.
      At least one personalization value must be non-zero.
      If not specfiied, a nodes personalization value will be zero.
      By default, a uniform distribution is used.
    max_iter : integer, optional
      Maximum number of iterations in power method eigenvalue solver.
    tol : float, optional
      Error tolerance used to check convergence in power method solver.
    nstart : dictionary, optional
      Starting value of PageRank iteration for each node.
    weight : key, optional
      Edge data key to use as weight.  If None weights are set to 1.
    dangling: dict, optional
      The outedges to be assigned to any "dangling" nodes, i.e., nodes without
      any outedges. The dict key is the node the outedge points to and the dict
      value is the weight of that outedge. By default, dangling nodes are given
      outedges according to the personalization vector (uniform if not
      specified). This must be selected to result in an irreducible transition
      matrix (see notes under google_matrix). It may be common to have the
      dangling dict to be the same as the personalization dict.
    Returns
    -------
    pagerank : dictionary
       Dictionary of nodes with PageRank as value
    Examples
    --------
    >>> G = nx.DiGraph(nx.path_graph(4))
    >>> pr = nx.pagerank(G, alpha=0.9)
    Notes
    -----
    The eigenvector calculation is done by the power iteration method
    and has no guarantee of convergence.  The iteration will stop after
    an error tolerance of ``len(G) * tol`` has been reached. If the
    number of iterations exceed `max_iter`, a
    :exc:`networkx.exception.PowerIterationFailedConvergence` exception
    is raised.
    The PageRank algorithm was designed for directed graphs but this
    algorithm does not check if the input graph is directed and will
    execute on undirected graphs by converting each edge in the
    directed graph to two edges.
    See Also
    --------
    pagerank_numpy, pagerank_scipy, google_matrix
    Raises
    ------
    PowerIterationFailedConvergence
        If the algorithm fails to converge to the specified tolerance
        within the specified number of iterations of the power iteration
        method.
    References
    ----------
    .. [1] A. Langville and C. Meyer,
       "A survey of eigenvector methods of web information retrieval."
       http://citeseer.ist.psu.edu/713792.html
    .. [2] Page, Lawrence; Brin, Sergey; Motwani, Rajeev and Winograd, Terry,
       The PageRank citation ranking: Bringing order to the Web. 1999
       http://dbpubs.stanford.edu:8090/pub/showDoc.Fulltext?lang=en&doc=1999-66&format=pdf
    """
    max_iter = 100
    if len(G) == 0:
        return {}

    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G

    # Create a copy in (right) stochastic form
    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()

    print("weight: ", W[0][1][weight], W[0][2][weight])
    # Choose fixed starting vector if not given
    if nstart is None:
        x = dict.fromkeys(W, 1.0 / N)
    else:
        # Normalized nstart vector
        s = float(sum(nstart.values()))
        x = {k: v / s for k, v in nstart.items()}

    if personalization is None:
        # Assign uniform personalization vector if not given
        p = dict.fromkeys(W, 1.0 / N)
    else:
        s = float(sum(personalization.values()))
        p = {k: v / s for k, v in personalization.items()}

    if dangling is None:
        # Use personalization vector if dangling vector not specified
        dangling_weights = p
    else:
        s = float(sum(dangling.values()))
        dangling_weights = {k: v / s for k, v in dangling.items()}
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

    # power iteration: make up to max_iter iterations
    for _ in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
        for n in x:
            # this matrix multiply looks odd because it is
            # doing a left multiply x^T=xlast^T*W
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights.get(n, 0) + (1.0 - alpha) * p.get(n, 0)
        # check convergence, l1 norm
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N * tol:
            return x
    raise nx.PowerIterationFailedConvergence(max_iter)


def nxtextrank(wordsList):
	# wordsList:  list[list] 一个句子的分词结果是list，所有句子的分词结果是list[list]
	numOfSents = len(wordsList)
	adjacentMatrix = np.zeros((numOfSents, numOfSents))  
	"""
	邻接矩阵 里面存的是相似度，相似度就是graph 中的边的权值
	"""
	for i in range(0, numOfSents):
		for j in range(i+1, numOfSents):
			sim = cal_sim(wordsList[i], wordsList[j])
			adjacentMatrix[i, j] = sim
			adjacentMatrix[j, i] = sim
    
    
	print("adjacentMatrix:\n ", adjacentMatrix)
	sorted_sentences = []
	nx_graph = nx.from_numpy_matrix(adjacentMatrix)
	scores = pagerank(nx_graph, **{'alpha': 0.85, })
	print ("scores:", scores)
	sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
	for index, score in sorted_scores:
		item = {"words": wordsList[index], 'TR': score, 'index': index}
		sorted_sentences.append(item)
	return sorted_sentences[:3]

"""
words1 = ['a', 'b', 'c']
words2 = ['a', 'b', 'c']
words3 = ['a', 'b', 'c']
"""

"""
words1 = ['a', 'b', 'c']
words2 = ['a', 'e', 'f']
words3 = ['g', 'h', 'i']
"""
""""
[0.465096961926178;  0.465096961926178;  0.069806076147643]
matlab 算出来的分数
"""
"""
scores: {0: 0.4651161545800183, 1: 0.4651161545800183, 2: 0.06976769083996354}
"""


words1 = ['a', 'b', 'c']
words2 = ['a', 'b', 'f']
words3 = ['a', 'h', 'i']




print ( cal_sim(words1, words2),  similarOfSents(words1, words2) )
print (  cal_sim(words1, words3),  similarOfSents(words1, words3) )
print ("networkx.pagerank 算的值：\n", nxtextrank([words1, words2, words3]))


"""
自已算的textrank，相比原算法没有考虑孤立结点的贡献值(没有边的结点)，并且
略去了相似度邻接矩阵如何转化为权值邻接矩阵的过程
本例中所有结点都有边相连
"""
WS = [1/3, 1/3, 1/3]  # TextRank 初始值
W = np.array([  [0, 0.6666666666666666, 0.3333333333333333],
                [0.6666666666666666, 0, 0.3333333333333333],
                [0.5, 0.5, 0]
             ], np.float)
# 权值邻接矩阵 

N = len(WS)


for _ in range(0, 1):
    WS_last = WS # 上一次的分数
    WS = [0, 0, 0]
    for i in range(0, N):
        for j in range(0, N):
            if i != j:
                WS[j] += 0.85 * WS_last[i] * W[i][j]
                # print(i, j, ":", W[i][j])
        WS[i] += 0.15 * 1 / N
        print("WS[i]:", WS[i])

print ("自已算的值：\n", WS, "\n", W)




"""

t = [1/3, 1/3, 1/3]
# TextRank 初始值

s = np.array([  [0, 0.6666666666666666, 0.3333333333333333],
                [0.6666666666666666, 0, 0.3333333333333333],
                [0.5, 0.5, 0]
             ], np.float)
# 相似度邻接矩阵

for _ in range(0,1):
	for i in range(0, 3):
		sum_max = 0 # 大求和
		for j in range(i+1, 3):
			sum_min = sum(s[j])  # 小求和
			wji = s[i, j] # 分子
			WSj = t[j]
			sum_max = sum_max + (wji / sum_min) * WSj
		WSi = 0.15 + 0.85 * sum_max
		t[i] = WSi

print (s, '\n', s[0][1])
print (t)


t = [1, 1, 1]
for i in range(0, 3):
	sum_max = 0
	for j in range(i+1, 3):
		sum_max = sum_max + 0.5 * t[j]
	t[i] = 0.15 + 0.85 * sum_max
print (t)
"""
