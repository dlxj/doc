
import os
#os.chdir('/content/NTU_MachineLearning/HW8_Seq2Seq')

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.utils.data as torch_data
import torch.utils.data.sampler as sampler
import torchvision
from torchvision import datasets, transforms

import numpy as np
import sys
import os
import random
import json
import heapq as pq
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # 判斷是用 CPU 還是 GPU 執行運算

import numpy as np

def get_dictionary(data_path, language):
    # 載入字典
    with open(os.path.join(data_path, f'word2int_{language}.json'), "r", encoding='UTF-8') as f:
      word2int = json.load(f)
    with open(os.path.join(data_path, f'int2word_{language}.json'), "r", encoding='UTF-8') as f:
      int2word = json.load(f)
    return word2int, int2word

def Data(data_path, type='training'):
    data = []
    with open(os.path.join(data_path, f'{type}.txt'), "r", encoding='UTF-8') as f:
      for line in f:
        data.append(line)
    print (f'{type} dataset size: {len(data)}')
    return data

class LabelTransform(object):
  def __init__(self, size, pad):
    self.size = size
    self.pad = pad

  def __call__(self, label):
    label = np.pad(label, (0, (self.size - label.shape[0])), mode='constant', constant_values=self.pad)
    return label

class TrainDataset(torch_data.Dataset):
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        return len(self.data)

if  __name__ == "__main__": 

    input_path = './HW8_Seq2Seq/cmn-eng'
    batch_size = 60
    emb_dim = 256                   # 嵌入向量的维度，即用多少维来表示一个单词
    hid_dim = 512
    n_layers = 3
    dropout = 0.5                    # dropout 是決定有多少的機率會將某個節點變為 0，主要是為了防止 overfitting ，一般來說是在訓練時使用，測試時則不使用
    learning_rate = 0.00005
    max_output_len = 50              # 最後輸出句子的最大長度
    num_steps =  1 # 12000                # 總訓練次數
    store_steps = 300                # 訓練多少次後須儲存模型
    summary_steps = 300              # 訓練多少次後須檢驗是否有overfitting
    load_model = False               # 是否需載入模型
    store_model_path = "./"          # 儲存模型的位置
    load_model_path = None           # 載入模型的位置 e.g. "./ckpt/model_{step}" 
    data_path = input_path           # 資料存放的位置
    attention = True                 # 是否使用 Attention Mechanism

    # 載入字典
    word2int_en, int2word_en = get_dictionary(data_path, 'en')
    word2int_cn, int2word_cn = get_dictionary(data_path, 'cn')
    
    en_vocab_size = len(word2int_en)
    cn_vocab_size = len(word2int_cn)

    # 加载训练数据


    transform = LabelTransform(max_output_len, word2int_en['<PAD>'])
    

    train_loader = torch_data.DataLoader(TrainDataset(Data(data_path, type='training')), batch_size = batch_size, shuffle=True)

    val_dataset = torch_data.DataLoader(TrainDataset(Data(data_path, type='validation')), batch_size = batch_size, shuffle=True)
    


    #embedding = nn.Embedding(en_vocab_size, emb_dim)

    a = 1


