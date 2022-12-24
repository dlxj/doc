import cv2
import numpy as np


class HashTracker:
    def __init__(self, path):
        # 初始化图像
        self.img = cv2.imread(path)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def cal_hash_code(self, cur_gray):
        s_img = cv2.resize(cur_gray, dsize=(8, 8))
        img_mean = cv2.mean(s_img)
        return s_img > img_mean[0]

    def cal_phash_code(self, cur_gray):
        # 缩小至32*32
        m_img = cv2.resize(cur_gray, dsize=(32, 32))
        # 浮点型用于计算
        m_img = np.float32(m_img)
        # 离散余弦变换，得到dct系数矩阵
        img_dct = cv2.dct(m_img)
        img_mean = cv2.mean(img_dct[0:8, 0:8])
        # 返回一个8*8bool矩阵
        return img_dct[0:8, 0:8] > img_mean[0]

    def cal_dhash_code(self):
        cur_gray = self.gray
        # dsize=(width, height)
        m_img = cv2.resize(cur_gray, dsize=(9, 8))
        m_img = np.int8(m_img)
        # 得到8*8差值矩阵
        m_img_diff = m_img[:, :-1] - m_img[:, 1:]
        return np.piecewise(m_img_diff, [m_img_diff > 0, m_img_diff <= 0], [1, 0])

    def cal_hamming_distance(self, model_hash_code, search_hash_code):
        # 返回不相同的个数
        diff = np.uint8(model_hash_code - search_hash_code)
        return cv2.countNonZero(diff)


def main():
    #读入图片
    h1 = HashTracker('1.jpg')
    h2 = HashTracker('2.jpg')
    #计算汉明距离
    diff = h1.cal_dhash_code() - h2.cal_dhash_code()
    print(np.sum(np.abs(diff)))



if __name__ == '__main__':
    main()
