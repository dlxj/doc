```
import os
os.chdir("/content/gdrive/MyDrive")

import pdb; pdb.set_trace() # 调试， exit 退出
```



```
# google 网盘文件的下载方法
# 李宏毅2020 作业
# http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html
import sys
import pandas as pd
import numpy as np
from google.colab import drive 
!gdown --id '1wNKAxQ29G15kgpBy_asjTcZRRgmsCZRm' --output data.zip
!unzip data.zip
# data = pd.read_csv('gdrive/My Drive/hw1-regression/train.csv', header = None, encoding = 'big5')
data = pd.read_csv('./train.csv', encoding = 'big5')
```





```
i = []
while(True):   
i.append('a')
```



```
function KeepClicking(){
  console.log("Clicking");
  document.querySelector("colab-toolbar-button#connect").click()
}setInterval(KeepClicking,60000)
```



> 免费版的GPU一般是T4，运气差的时候就只能用K80（但是重启可以重新分配！），运气好的时候可以分配到Tesla P100。
>
> Colab Pro的话，官方说的是优先分配P100和T4，但是目前实际情况是pro版的GPU是Tesla P100和Tesla V100。并且一半以上概率是V100。P100功率250W，V100功率300W，应该V100还要好很多。



```
免费版仅提供12G的内存，而pro可以提供高达25G的内存，在实际使用中，少部分人会遇到因RAM满了而重启的现象，在pro版，这样的情况几乎不会出现。

另外磁盘大小也提升了约40G。
```



> **但使用信用卡（可以是国内的发卡行）和美国的邮政编码就可以购买了**。例如：纽约10001
>
> 费用的话：$9.9/月是不含税的价格，实际付的价格应该在$11左右。小颜买的是$10.88
>
> 大家一定要记住，按时还信用卡呀！！！



> 需要在“代码执行程序—更改运行时内存-运行时规格”里修改为“高内存”才可。





如果你还不知道Colab，那一定要体验一下，这个能在线编程、还能白嫖Google云TPU/GPU训练自己AI模型的工具早已圈了一大波粉丝。

但是，作为白嫖的福利，它总有限制，比如你不去碰它，过30分钟Colab就会自动掉线。

![img](https://pic1.zhimg.com/80/v2-b3bda69f1f565ceba6c8e90ceeba06d4_720w.jpg)

所以，程序员ShIvam Rawat在medium上贴出了一段代码：

```tex
function ClickConnect(){
console.log(“Working”);
document.querySelector(“colab-toolbar-button#connect”).click()
}
setInterval(ClickConnect,60000)
```

你只要把它放进控制台，它就会自动隔一阵儿调戏一下Colab页面，防止链接断掉。

是不是非常机智？

— 完 —

量子位 · QbitAI

