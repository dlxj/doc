

# 功能：最小编辑距离(Levenshtein)
# https://zhuanlan.zhihu.com/p/43009353

def minDistance(word1, word2):
    if not word1:
        return len(word2 or '') or 0

    if not word2:
        return len(word1 or '') or 0

    size1 = len(word1)
    size2 = len(word2)

    last = 0
    tmp =  [ 0 for _ in range(size2 + 1)]
    value = None

    for i in range(size1):
        tmp[0] = i + 1
        last = i
        # print word1[i], last, tmp
        for j in range(size2):
            if word1[i] == word2[j]:
                value = last
            else:
                value = 1 + min(last, tmp[j], tmp[j + 1])
                # print(last, tmp[j], tmp[j + 1], value)
            last = tmp[j+1]
            tmp[j+1] = value
        # print tmp
    return value

# # 根据编缉距离算相似度
# def similarityBydistance(s1, s2):
#     d = minDistance(s1, s2)  # 编缉距离
#     l = min(s1, s2)
#     if d >= l:
#         return 0
#     return 0



if __name__ == "__main__":
    assert minDistance(None, None) == 0
    assert minDistance(None, '') == 0
    assert minDistance('', None) == 0
    assert minDistance(None, '1') == 1
    assert minDistance('22', None) == 2

    assert minDistance('', '') == 0
    assert minDistance('h', '') == 1
    assert minDistance('', 'r') == 1

    assert minDistance('horse', '') == 5
    assert minDistance('', 'ros') == 3

    assert minDistance('h', 'r') == 1
    assert minDistance('horse', 'ros') == 3

    print(minDistance("我们在上班", "我们aa在，上班"))

