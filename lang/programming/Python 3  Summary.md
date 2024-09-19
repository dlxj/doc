



[TOC]

# Python 3  Summary



https://imshuai.com/python-pip-install-package-offline-tensorflow  pip离线安装package



```
>>> import blinker
>>> blinker.__file__
'/usr/lib/python3/dist-packages/blinker/__init__.py'

rm -rf /usr/lib/python3/dist-packages/blinker*

```





## OSError: Missing dependencies for SOCKS support.

```
unset all_proxy && unset ALL_PROXY && \
pip install pysocks
```





VSCode   Alt + <-     Alt +   ->   前跳  回跳

F11 切换全屏



```
# 加 -u 才能看到打印的输出
nohup python3.8 -u anime_Danganronpa_version1.py >outlog &
```



```
# 不安装依赖
On some systems (like Termux), it is not possible to install pycryptodomex. In that case, install without dependancies:

python3 -m pip install --no-deps -U yt-dlp "
```



```
# 这样装就好好的，普通装就不对？
D:\usr\Python311\python.exe -m pip install -r .\requirements.txt
```





## chatgpt api

- https://github.com/acheong08/ChatGPT



## Install pip

```
apt update
apt install python3-pip

pip3 freeze > requirements.txt
	# 导出所有已安装的包名

```



```
临时使用
可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple
 例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent，这样就会从清华这边的镜像去安装gevent库。

永久修改
Linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url至tuna，内容如下：

 [global]
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple
复制
windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

 [global]
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```





### pip 一开代理就出错

- https://myblog.quantumcloud.top/2022/07/08/833fc93abede/  **必看**

- https://note.bobo.moe/2021/02/clash-for-windows-pip-proxyerror.html

```
powershell 执行：
	(get-command pip).Path
		# D:\usr\Python38\Scripts\pip.exe
	
	
```



### 无法卸载包

```python
>>> import blinker
>>> print(blinker.__file__)
--> /usr/lib/python3/dist-packages/blinker/__init__.py

rm -rf /usr/lib/python3/dist-packages/blinker*

```





## 升级pip

```
删除目录 D:\usr\Python38\Lib\site-packages\pip-xx.x.x.dist-info
python -m pip install --upgrade pip -i https://pypi.douban.com/simple
```



```
jupyter notebook能用，但是无法连接服务器？？
pip install --upgrade ipykernel -i https://pypi.douban.com/simple
```



## pip只下载不安装

```
# 看这里 nodejs summary.md chatglm2-6b-32k 这一节
git lfs install
git clone https://huggingface.co/THUDM/chatglm2-6b-32k
	# GIT_LFS_SKIP_SMUDGE=1 不要下载大文件
	
git restore --source=HEAD :/
	# 恢复下载


pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate -i https://pypi.tuna.tsinghua.edu.cn/simple some-package


pip3.9 cache purge
	# 删除所有缓存文件

/root/.cache/pip/
	# 缓存目录在这
	pip3.9 config list
		# 没有输出

pip3.9 config set global.cache-dir "/mnt/tmp"
	# 成功设置缓存目录
	--> Writing to /root/.config/pip/pip.conf
	


pip3.9 download -r requirements.txt -d /mnt/ChatGLM2-6B/whl 
	# pip3.9 uninstall -r requirements.txt -y
	


pip download -d /mnt/whl protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
	# 只下载不安装
```



### conda 仅下载

```
conda install --download-only pytorch==2.0.0 

```





## Python for ubuntu20.04

```

# pip freeze > freeze.txt

apt update && apt upgrade -y && \
(sleep 1; echo "Y";) | apt-get install build-essential
apt-get install p7zip-full vim curl lsof git wget 

https://blog.csdn.net/qq_20466211/article/details/128731196
apt-get install dialog apt-utils && \
apt install -y wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov


apt update && apt upgrade -y && \
apt install software-properties-common -y && \
add-apt-repository ppa:deadsnakes/ppa && \
apt install python3.10 -y && \
apt install python3.10-distutils -y && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
python3.10 get-pip.py && \
pip install --upgrade requests

```





## Python for colab

```

!apt-get install python3.8

!curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
!python3.8 get-pip.py

try these commands

!update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
then

!update-alternatives --list python
this must display your downloaded python version

after that

!sudo update-alternatives --config python
## !Set python3.8 as default.
finally

!sudo update-alternatives --set python /usr/bin/python3.8
then check your default python version on colab

!python3 --version
```





## Python for win10

```bash
python -m pip install --upgrade pip # 装完先升级pip
pip install selenium
pip install opencv-python  # import cv2  # win10要编译很久的
```



```
.gitignore
*.json
*.doc
*.docx
*.rar
*.zip
*.7z
*.csv
*.pyc
.DS_Store
*.pyc
__pycache__/
```



## Python for Mac

> which python3
> which python3.8
>
> which pip3.8
>
> pip3.8 install jieba
>
> sublim text 配置
>
> {
> 	"shell_cmd": "python3.8 ${file}"
> }
>
> \# encoding=utf-8
>
> \# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
>
> import sys
> import codecs
> sys.stdout.reconfigure(encoding='utf-8')
> print(sys.getdefaultencoding())  # python3的系统编码
> print(sys.stdout.encoding)          # 标准输出的编码





## Anaconda [u](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

```

# pip freeze > freeze.txt

wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
bash Miniforge3-Linux-x86_64.sh -b && \
~/miniforge3/bin/conda init && \
ln -s ~/miniforge3/bin/conda /usr/local/bin && \
ln -s ~/miniforge3/bin/activate /usr/local/bin && \
ln -s ~/miniforge3/bin/deactivate /usr/local/bin && \
source ~/miniforge3/etc/profile.d/conda.sh && \
conda config --set auto_activate_base false

vi ~/.condarc
proxy_servers:
  http: http://172.16.6.253:8118
  https: http://172.16.6.253:8118
ssl_verify: false
	# 康达设置代理

conda clean -a
	# 代理是OK 的，出错执行这个就可以了


# autodl
~/miniconda3/bin/conda init && \
ln -s ~/miniconda3/bin/conda /usr/local/bin && \
ln -s ~/miniconda3/bin/activate /usr/local/bin && \
ln -s ~/miniconda3/bin/deactivate /usr/local/bin && \
source ~/miniconda3/etc/profile.d/conda.sh

```



```bash
conda config --set auto_activate_base true # 开启或关闭自动激活
conda env list
conda activate xx
```

```bash

conda create -n  PaddleOCR_275 pip python=3.10


conda create -n tensorflow_cpu pip python=3.6
conda activate tensorflow_cpu
conda install pytorch-cpu==1.0.0 torchvision-cpu==0.2.1 cpuonly -c pytorch
pip install stanfordnlp
pip install tensorflow==1.15
conda deactivate
conda info -e
conda env remove -n tensorflow_cpu

python -m spacy download en
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
nlp = spacy.load("en_core_web_sm")
```

pip install **pymysql==0.9.3** # 高版本没有escape_string

pip install tensorflow==1.12 -i https://pypi.tuna.tsinghua.edu.cn/simple

```
install_requires=['numpy', 'tensorflow-gpu==1.12', 'tensorflow-hub', "tqdm", "spacy", "jieba",
                        "stanfordnlp"],
```



```bash
conda create -n tf114 pip python=3.7
conda activate tf114
pip install -i https://mirrors.aliyun.com/pypi/simple/ tensorflow==1.14
pip install -i https://mirrors.aliyun.com/pypi/simple/ bert4keras==0.9.8

```



```
# 清除dns缓存
ipconfig /flushdns
```



```bash
# flask_plank 124高配服务器，安装路径
./Anaconda3-2020.11-Linux-x86_64.sh
/home/data/users/weiqibang/project/flask_server/Anaconda3

conda create -n plan_evn pip python=3.8
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```



```
export PYTHONPATH=/root/flask_server/server_venv/lib/python3.8/site-packages
```



```bash
# on echo
conda deactivate
ls /usr/bin/python*
apt-get purge --auto-remove python2.7
apt-get purge --auto-remove python3.6
apt-get purge --auto-remove python3.8
pm2 --name "ftspg8085" start "flask run --host 0.0.0.0 --port 8085"
```



### pip

```
https://zhuanlan.zhihu.com/p/72480936
requirements.txt
```



### redist

```
# 安装
https://linuxize.com/post/how-to-install-and-configure-redis-on-centos-7/

pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
#requirements.txt
requests
Levenshtein
jieba
pymysql==0.9.3
numpy
flask
flask_cors
joblib
sklearn
pandas
redis

```





**基于论文的实现**  [u](https://github.com/17zuoye/pyirt)

- IRT Parameter Estimation using the EM Algorithm By Brad Hanson 2000

  - Github 实现 [u](https://github.com/17zuoye/pyirt/blob/master/pyirt/solver/model.py)

    > **创建环境**
    >
    > conda create -n irt  python=3.8
    >
    > conda activate irt
    >
    > cd ~/pyirt-master
    >
    > pipenv --three
    > make
    >
    > pipenv shell
    >
    > **使用环境**
    >
    > conda activate irt
    >
    > cd ~/pyirt-master
    >
    > pipenv shell





## Source install on CentOS

[How to Install Python 3.8 on CentOS 8](https://linuxize.com/post/how-to-install-python-3-8-on-centos-8/)



```python
yum update -y && \
yum groupinstall -y 'Development Tools' && \
yum install -y gcc libffi-devel bzip2-devel expat-devel gdbm-devel ncurses-devel openssl-devel readline-devel sqlite-devel tk-devel xz-devel zlib-devel wget
```

```
apt-get update && \
apt-get install -y build-essential checkinstall && \
apt -y install gdb lcov libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev
```

```python

https://github.com/actions/setup-python/issues/93
    https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username
    # ssl 可能要 username 安装

./configure --with-openssl=/home/username/openssl
python3 -m ssl and nothing outputs, it's ok.    
    
yum install openssl-devel
/usr/bin/openssl version

./configure --with-openssl="/usr"
	# checking for openssl/ssl.h in /usr... yes
    # 这样就能找到 ssl 了
	
    Python requires a OpenSSL 1.1.1 or newer
Custom linker flags may require --with-openssl-rpath=auto
	# 还是出错了
    
VERSION=3.8.3 && \
VERSION=3.10.9 && \
VERSION=3.11.3 && \
VERSION=3.10.13 && \
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && \
tar -xf Python-${VERSION}.tgz && \
cd Python-${VERSION} && \
./configure --with-openssl="/usr" && \
make clean && \
make -j 8 && \
sudo make altinstall 
# Please do not use the standard make install as it-
# will overwrite the default system python binary.
python3.8 --version
pip3.8 --version
```

```
yum -y install epel-release
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
yum install ffmpeg ffmpeg-devel -y
```





```
# Creating a Virtual Environment
# First, create the project directory and switch to it:
mkdir ~/flask_server && cd ~/flask_server
python3.8 -m venv server_venv
source server_venv/bin/activate  # 激活临时python 环境
python --version
pip --version
deactivate # 关闭临时python 环境
```



```
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目
```







### 明明pip 装了某个包却找不到

```python

# PaddleOCR_ali1k_det_rec_300epoch/tools/infer/predict_system.py

import os, sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, 'PaddleOCR_ali1k_det_rec_300epoch')))

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'



export PYTHONPATH=/root/flask_server/server_venv/lib/python3.8/site-packages
export PYTHONPATH=/root/anaconda3/lib/python3.8/site-packages

# see nodejs summary.md -> internlm
python tools/transformers/convert2hf.py --src_folder /root/saved/100 --tgt_folder hf_ckpt/ --tokenizer ./tools/V7_sft.model
	# 转成 hf 格式
	# https://github.com/InternLM/InternLM/issues/107
		# ~/InternLM# export PYTHONPATH=$PWD:$PYTHONPATH
		# 在 InternLM 根目录执行这一句它才不错

        
        
# exec('from paddlespeech.cli.tts import TTSExecutor')  # 不知道为什么一定要这样导入 # 必须在全局范围执行，放函数里执行是不行的
# TTSExecutor = locals()['TTSExecutor']   # 需要的符号已经在当前局部变量里面了，取出来用
# runtts = TTSExecutor()

        
```

#### 打印 site-packages 路径

```
/root/miniconda3/lib/python3.8/site-packages
	# autodl 只有 python3.8 + torch2.0，但需要 python3.10，
    # 打算从这里拷需要的包
    >>> from distutils.sysconfig import get_python_lib
	>>> print(get_python_lib())
/root/miniconda3/envs/internlm-env/lib/python3.10/site-packages
	# /usr/bin/cp -rf /root/miniconda3/lib/python3.8/site-packages /root/miniconda3/envs/internlm-env/lib/python3.10
		# 行不通，弃用
```






```
pip list
pip show jieba
```



```python
pm2 start run.sh
pm2 restart id --name assist 
```





```
python -m pip install --upgrade pip
pip install wheel
pip install jupyter
- pip install --user jupyter  出错就用这个
python -m jupyter notebook --version
python -m pip install -U matplotlib
```



### 使用临时源

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple panda
```



### 使用代理

```bash
pip install pysocks
pip install -r requirements.txt --proxy='socks5://127.0.0.1:4781'
pip3 --proxy 127.0.0.1:6152 install snowlp
```



```bash
使用pip命令全局配置pip 阿里云镜像源
pip config --global set global.index-url https://mirrors.aliyun.com/pypi/simple/
 
pip config --global set install.trusted-host mirrors.aliyun.com
复制代码不用找pip配置文件路径，pip会根据当前系统的环境变量自动完成配置
器通过代理临时上网：
执行命令行：
export http_proxy=http://136.15.2.3:909/ && export https_proxy=http://136.15.2.3:909/
复制代码取消代理：
unset http_proxy
unset https_proxy
```



```
set HTTP_PROXY=http://127.0.0.1:4780
set HTTPS_PROXY=https://127.0.0.1:4780
```



## Source install on Almalinux

[How to Install Python 3.10 on AlmaLinux 9](https://wiki.crowncloud.net/?How_to_Install_Python_3_10_on_AlmaLinux_9)

```
version=3.10.8 && \
dnf update && \
dnf install -y tar wget yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel && \
wget https://www.python.org/ftp/python/$version/Python-$version.tgz && \
tar xzf Python-$version.tgz && \
cd Python-$version && \
./configure --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions && \
make -j 4 && \
make altinstall 

```







## nohup

```bash
# 加 -u 才能看到打印的输出
nohup python3.8 -u anime_Danganronpa_version1.py >outlog &
tail -f outlog
jobs -l # 查看运行中的进程
ps -aux | grep "anime_Danganronpa_version1.py"

kill -9 $(lsof outlog | tail -n +2  | awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:8077 | tail -n +2  | awk '{print $2}' | tr '\n' ' ')

```



```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

flask run --host 0.0.0.0 --port 6002
kill -9 $(lsof -i:6002 | tail -n +2  |  awk '{print $2}' | tr '\n' ' ')
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```



## 远程调试

- https://zhuanlan.zhihu.com/p/43656542

  > VS Code的Python远程调试环境



```
# db\t.py
import sys

if __name__ == "__main__":
    argv = sys.argv
    a = 1
    print('hi,,')
```



```
# db\.vscode\launch.json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Python: Attach",
			"type": "python",
			"request": "attach",
			"connect": {
				"host": "localhost",
				"port": 5678
			}
		}
	]
}
```



```
# 终端运行(可以是远程主机)：
python -m debugpy --listen 5678 --wait-for-client t.py -arg1 ARG1 -arg2 ARG2

# vscode 打开db 文件夹, 下断点，F5 (这里是本地主机)

    argv = sys.argv  # 断下来后可以看到传进来的参数：ARG1 ARG2

前提是，本地主机和远程主机运行的代码是同一分代码，目录结构也一致
```



```
CUDA_VISIBLE_DEVICES=0 python -m debugpy --listen 5678 --wait-for-client train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1
```









```
pip3 install debugpy
import debugpy
debugpy.listen(5678)
debugpy.wait_for_client()
```



```
{

   "name": "Python: Attach",
"type": "python",
"request": "attach",
"connect": {

   "host": "localhost",
"port": 5678
}
}
```



```

cd /workspaces/pyt ; /usr/bin/env /usr/local/bin/python /home/vscode/.vscode-server/extensions/ms-python.python-2022.7.11332232/pythonFiles/lib/python/debugpy/launcher 41587 -- /workspaces/pyt/test.py \< input.txt

I've seen the above problem only in Python's debug config (launch.json).

The same approach in Python's build config (tasks.json) does work without any issues:
"args": ["${file}", "<", "${fileDirname}/input.txt"],
```



### vscode 远程调试

- https://matpool.com/supports/doc-vscode-connect-matpool/



#### 使用 conda 虚拟环境

ctrl + shift + p -> 选择 conda 虚拟环境DB 中的 python 解释器既可



## 异常堆栈跟踪

[捕获不到网络异常导至程序意外终止](https://www.v2ex.com/t/967308)

```
python -X faulthandler program.py

```





## Julia



**高斯求积简介** [u](https://discourse.juliacn.com/t/topic/1024) [u2](GitHub\doc\lang\programming\高斯求积简介.pdf)



```python
>pip3 install pycall # for julia to using sympy package

from sympy import  integrate ,cos,sin
from sympy.abc import  a,x,y

print( integrate(sin(x)/x,(x,-float("inf"),float("inf"))) ) # 积分结果是pi
print( integrate(1+15*x+2*x**2+12*x**3,(x,float(-1),float(1))) ) # 3.333
```



```julia
# 全程开全局代理 Proxifier
julia>import Pkg; Pkg.add("SymPy")
julia>using SymPy
julia>sympy.sqrt(3)

# vscode
using SymPy
x = symbols("x")
println( integrate(sin(x)/x, (x, -oo, oo)) )
println( integrate(1+15*x+2*x^2+12*x^3, (x, -1.0, 1.0)) )

```





## 绘图的重要参考

### 深入理解神经网络：从逻辑回归到CNN.md

GitHub\doc\lang\programming\深入理解神经网络：从逻辑回归到CNN.md



## 优化



[Python编写循环的两个建议](https://zhuanlan.zhihu.com/p/68128557)

- “pythonic way”的方式来搜“地道”的写法，貌似stackoverflow上面讨论的多一些

[z](https://zhuanlan.zhihu.com/p/64893308)

1. 有\__init\__.py 文件的文件夹被认为是一个包，否则只是普通文件夹
- 普通文件夹不能 import, package 才可以
2.  .py 文件被认为是一个模块

- 单独一个py 文件就是一个module
3. import 后面必须是模块名

4. from 模块名 import 变量名 

5. import 包名.模块名

6. python l默认在sys.path 这个list 里的众多目录下找需要import 的模块，找不到就报错

7. \__file\__ 是模块自身的绝对路径

8. 要得到上层目录名可以连用两次os.path.dirname  

   - ```text
     os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     ```

9.   from package import *

   - \__init\__.py ： \__all\__ = [‘echo’, ‘effect’, ‘reverb’]

   - would be equivalent to

     ```
     from package import echo
     from package import effect
     from package import reverb
     ```

     

## Import



```python
import sys
sys.path.append('../..')
import jieba
import std.seg.iSeg as iSeg

print(iSeg.segment('苯巴比妥显效慢的主要原因是脂溶性较小'))
```



### args parse  [u](https://github.com/jplalor/py-irt)

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--num-epochs', default=1000, type=int)
parser.add_argument('--gpu', action='store_true')
parser.add_argument('--priors', help='[vague, hierarchical]', default='hierarchical')
parser.add_argument('--model', help='[1PL,2PL(coming soon)]', default='1PL')  # 2pl not implemented yet
args = parser.parse_args()

device = torch.device('cpu')
if args.gpu:
    device = torch.device('cuda')
    
for name in pyro.get_param_store().get_all_param_names():
    print(name)
    val = pyro.param(name).data.numpy()
    print(val)
    if name == 'loc_diff':
        print('mse: {}'.format(np.mean((val - real_diff) ** 2)))
    elif name == 'loc_ability':
        print('mse: {}'.format(np.mean((val - real_theta) ** 2)))    
```







### 同级目录直接用文件名导入



```
from iJson import save_json
currDir = os.path.dirname(os.path.abspath(__file__))
fname_to_save = os.path.join(currDir, 'j.json')
save_json(fname_to_save, { 0:'a', 1:'b' })
```



### 上级目录的子目录



- 需要子目录里有空的 \__init\__.py

     1.  将上级目录加到sys.path
     2.  按照对下级目录模块的方式导入



```
#from __future__ import absolute_import
import os, sys
import sys
sys.path.append("..")
# import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from std import iJson
currDir = os.path.dirname(os.path.abspath(__file__))
fname_to_save = os.path.join(currDir, 'j.json')
iJson.save_json(fname_to_save, { 0:'a', 1:'b' })
print("hi,,,")
```



### import_module

```python
import importlib
currDir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(currDir)
googlee_protobuf = importlib.import_module('googlee.protobuf') # 绝对导入

_descriptor = importlib.import_module('.descriptor',package='googlee.protobuf') # 相对导入
_message = importlib.import_module('.message',package='googlee.protobuf')
_reflection = importlib.import_module('.reflection',package='googlee.protobuf')
_symbol_database = importlib.import_module('.symbol_database',package='googlee.protobuf')
descriptor_pb2 = importlib.import_module('.descriptor_pb2',package='googlee.protobuf')

```



```
https://evzs.com/2024/07/25/Python%EF%BC%9Aimportlib%E5%BA%93%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95%E4%B8%BE%E4%BE%8B%E5%92%8C%E5%BA%94%E7%94%A8%E8%AF%A6%E8%A7%A3.html

import importlib
import example_module  # 假设这是你正在开发并频繁修改的模块

# 场景：在不重启程序的情况下重新加载修改后的模块
def reload_example_module():
    importlib.reload(example_module)  # 重新加载模块
    print("example_module已重新加载")

# 修改example_module之后调用reload_example_module来应用新更改
reload_example_module()
示例 3：实现简单的插件系统

import importlib
import os

# 场景：动态加载插件并执行插件中的特定函数
plugins_directory = "./plugins"  # 插件目录
plugin_name = "example_plugin"  # 要加载的插件名

# 动态加载插件
def load_plugin(plugin_name):
    try:
        plugin = importlib.import_module(plugin_name)
        print(f"成功加载插件：{plugin_name}")
        return plugin
    except ImportError:
        print(f"插件{plugin_name}加载失败。")
        return None

# 执行插件中的特定函数
def execute_plugin_function(plugin, function_name):
    if plugin:
        func = getattr(plugin, function_name, None)  # 获取插件中的指定函数
        if func:
            func()  # 执行函数
        else:
            print(f"{plugin_name}中不存在函数{function_name}")
    else:
        print("插件未加载，无法执行函数")

# 主程序
plugin = load_plugin(plugin_name)  # 加载插件
execute_plugin_function(plugin, "plugin_function")  # 执行插件中的具体函数
```





## Syntax



### 添加命令行参数

```python
 	import argparse
 	
 	"""
    CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1
    """
    sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    sys.argv.append( '--num_gpus' )
    sys.argv.append( '1' )
    
    parser = argparse.ArgumentParser(description='Text Recognition Training')
    parser.add_argument('exp', type=str)
    parser.add_argument('--name', type=str)
    parser.add_argument('--batch_size', type=int, help='Batch size for training')
    
    parser.set_defaults(debug=False)
    parser.set_defaults(benchmark=True)

    args = parser.parse_args()
    args = vars(args)
    args = {k: v for k, v in args.items() if v is not None}
```



### 类的动态构建

```
# doc\lang\programming\pytorch\文本检测\DBNET\DBNet官方实现\DB\train.py
import importlib

    @staticmethod
    def extract_class_from_args(args):
        cls = args.copy().pop('class')  # args 是字典
        package, cls = cls.rsplit('.', 1) # 是字符串 xxx.xxx
        module = importlib.import_module(package)
        cls = getattr(module, cls)
        return cls
```



### 命名参数 *args

```
*args – Named arguments passed to the init function.
```



### 不定长参数字典**kwargs

```python

# 定义
def load_all(self, **kwargs):

# 调用
load_all(arg1=1, arg2=2, arg3=3)

```



```
** 可以表示展开

line = {'points':[[323.0, 621.0], [1186.0, 652.0], [1178.0, 864.0], [315.0, 833.0]]
'text':'0'
'ignore':False}

lines = []
lines.append({**line, 'points': poly}) # poly 是新的 points ，意思是更新points，其他该有的还有，保持不变？
```



```
# see echodict\transformer\transformer_jax.py
def train_reverse(max_epochs=10, **model_args):
    num_train_iters = len(rev_train_loader) * max_epochs
    # Create a trainer module with specified hyperparameters
    trainer = ReverseTrainer(model_name='ReverseTask',
                             exmp_batch=next(iter(rev_train_loader)),
                             max_iters=num_train_iters,
                             **model_args)
                             
reverse_trainer, reverse_result = train_reverse(model_dim=32,
                                                num_heads=1,
                                                num_classes=rev_train_loader.dataset.num_categories,
                                                num_layers=1,
                                                dropout_prob=0.0,
                                                lr=5e-4,
                                                warmup=50)
                   
**model_args 任意参数一层层往下传

```







### isinstance 多个

```python
isinstance(args, (int, float, str)) # 是否是其中任意一个？还是说是这个只读列表？
```



### 动态设置类的属性



```python
# 动态设置
    def load(self, state_name, **kwargs):
        # FIXME: kwargs should be filtered
        # Args passed from command line
        cmd = kwargs.pop('cmd', dict())
        if state_name in kwargs:
            setattr(self, state_name, self.create_member_from_config(
                (kwargs[state_name], cmd)))
        else:
            setattr(self, state_name, self.states[state_name].default)


# 静态定义
class EAPIrt2PLModel(object):

    def __init__(self, score, slop, threshold): # 得分，区分度，阀值
        self.x_nodes, self.x_weights = get_gh_point(21)
        z = Z(slop, threshold, self.x_nodes)
        p = P(z)
        self.lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1) 
        """
        计算所有元素的乘积，按行连乘(维度变成n*1)。
        如果不指定轴，则不管是几维都展平成一维然后连乘
        """

    @property
    def g(self):
        x = self.x_nodes[:, 0]
        weight = self.x_weights[:, 0]
        return np.sum(x * weight * self.lik_values)

    @property
    def h(self):
        weight = self.x_weights[:, 0]
        return np.sum(weight * self.lik_values)

    @property
    def res(self):
        return round(self.g / self.h, 3)
```



### 动态定义类的静态方法

```python
    def draw_polygons(self, image, polygons, ignore_tags):
        for i in range(len(polygons)):
            polygon = polygons[i].reshape(-1, 2).astype(np.int32)
            ignore = ignore_tags[i]
            if ignore:
                color = (255, 0, 0)  # depict ignorable polygons in blue
            else:
                color = (0, 0, 255)  # depict polygons in red

            cv2.polylines(image, [polygon], True, color, 1)
    polylines = staticmethod(draw_polygons)
```



### 声明成员类型

- https://colab.research.google.com/drive/1xoGwp40otsZfnyAfbBtFkUrteGICJppp#scrollTo=LvSpLCEmYsKE

```python
!pip install --quiet equinox

import jax
import jax.random as jr
import jax.numpy as jnp
import equinox as eqx

from typing import Callable

class Model(eqx.Module):
    linear: eqx.Module
    non_jax: Callable
    
    def __init__(self, key):
        self.linear = eqx.nn.Linear(3, 3, key=key)
        self.non_jax = lambda: 'this breaks pmap/vmap with out=None'

devices = jax.local_devices()
n_dev = len(devices)

model = Model(jr.PRNGKey(42))
```





### setter

```python
class Quad:
    def __init__(self, points, format='NP2'):
        self._rect = None
        self.tensorized = False
        self._points = None
        self.set_points(points, format)

    @property
    def points(self):
        return self._points

    def set_points(self, new_points, format='NP2'):
        order = (format.index('N'), format.index('P'), format.index('2'))

        if isinstance(new_points, torch.Tensor):
            self._points = new_points.permute(*order)
            self.tensorized = True
        else:
            points = np.array(new_points, dtype=np.float32)
            self._points = points.transpose(*order)

            if self.tensorized:
                self.tensorized = False
                self.tensor

    @points.setter
    def points(self, new_points):
        self.set_points(new_points)
```



### 1_000_000

```
num_steps=1_000_000,
```



### :=

```
	# 先赋值后判断？
	if (threads := args.pop("threads")) > 0:
        torch.set_num_threads(threads)
```





## 全局变量

```
global message_log
message_log = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Set a flag to keep track of whether this is the first request in the conversation
global first_request
first_request = True

def init_gpt():
    global message_log
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    global first_request
    first_request = True
```



## Path



```python
from pathlib import Path
import tempfile
        self.GRADIO_CACHE = str(
            Path(
                os.environ.get("GRADIO_TEMP_DIR")
                or str(Path(tempfile.gettempdir()) / "gradio")
            ).resolve()
        )
	# resolve 统一 linux windows 路径的写法
	

import pathlib
pathlib.Path("..").resolve()


    for entry in (pathlib.Path(root) / "js").iterdir():
        if (
            entry.is_dir()
            and not str(entry.name).startswith("_")
            
       
from pathlib import Path
base_root = Path(__file__).parent.resolve()
value=str(base_root / "dir1"),        
  
```





```python
currDir = os.getcwd() # 兼容jupyter 
currDir = os.path.dirname(os.path.abspath(__file__)) # 不兼容jupyter
os.path.abspath(__file__)                   # current file
os.path.dirname(os.path.abspath(__file__))  # current file directory
os.path.dirname(os.path.abspath(__name__))  # ?? directory
```



```python
# 递归创建目录
currDir = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'cache', str(appid) )

    if not os.path.exists( currDir ):
        os.makedirs( currDir )
        
       
from pathlib import Path 
	# /usr/local/lib/python3.10/dist-packages/gradio/cli/commands/components/create.py
 
    if directory.exists() and not overwrite:
        raise ValueError(
            f"The directory {directory.resolve()} already exists. "
            "Please set --overwrite flag or pass in the name "
            "of a directory that does not already exist via the --directory option."
        )
    elif directory.exists() and overwrite:
        _create_utils.delete_contents(directory)

    directory.mkdir(exist_ok=overwrite)
    
    
source_pyi_file = p / module / component.python_file_name.replace(".py", ".pyi")
	# 路径拼法，这东西还自义定了运算符
      
```



```python
# ./datasets/train.json --> ./datasets/train
data_random_order_json = data_json[:-5] + '_random_order.json'
```



### ``__all__``

```
__all__ 以”白名单“的形式暴露里面定义的符号

__init__.py
from .sampler import Sampler, ... xxx ...
__all__ = ['Sampler', 'SequentialSampler', ... xxx ...]

```



### \_\_file\_\_



```
current_dir = os.path.dirname(os.path.abspath(__file__))

SRC_DIR = os.path.dirname(os.path.realpath(__file__))

```



### which

```
import shutil
node = shutil.which("node")
	# 获得 node 的绝对路径
```





## File



### windows Long path

1. Open the Start menu and type “regedit.” Launch the application.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Right-click the value “LongPathsEnabled” and select Modify.
4. Change “Value data” from 0 to 1.
5. Click OK.



### exists

```
import os,shutil
if os.path.exists(path):
```



### mkdir

```
# create directory recursively
import os
 
# Leaf directory
directory = "ihritik"
 
# Parent Directories
parent_dir = "/home/User/Documents/GeeksForGeeks/Authors"
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory
# 'ihritik'
os.makedirs(path)
print("Directory '%s' created" %directory)
```





### soft link



```python
    tmpmkv = "tmp.mkv"
    if ( os.path.exists(tmpmkv) ):
      os.unlink("tmp.mkv")
    os.symlink(videopath, "tmp.mkv")
    
    
    
    os.symlink('./outputs/workspace\\DB', 'workspace') # 建出来的软链打开会出错？？ 
    
```





```python
f = file('data/lsat.csv')
score = np.loadtxt(f, delimiter=",")
```



```
  def get_dictionary(self, language):
    # 載入字典
    with open(os.path.join(self.root, f'word2int_{language}.json'), "r", encoding='UTF-8') as f:
      word2int = json.load(f)
    with open(os.path.join(self.root, f'int2word_{language}.json'), "r", encoding='UTF-8') as f:
      int2word = json.load(f)
    return word2int, int2word
```





```python
import re
import glob

# 语料生成器，并且初步预处理语料
# 这个生成器例子的具体含义不重要，只需要知道它就是逐句地把文本yield出来就行了
def text_generator():
    txts = glob.glob('/root/thuctc/THUCNews/*/*.txt')
    for txt in txts:
        d = open(txt).read()
        d = d.decode('utf-8').replace(u'\u3000', ' ').strip()
        yield re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z ]+', '\n', d)
 # https://kexue.fm/archives/6920
```

```python
def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)
```



### 删除目录

```
import shutil
shutil.rmtree(root)

os.rmdir(root) # 只能删除空目录
```



### 移动文件

```
dest = shutil.move(source, destination) 

dest = shutil.move(source, destination, copy_function = shutil.copytree) 
```





### read file



```python
    self.data = []
    with open(os.path.join(self.root, f'{set_name}.txt'), "r", encoding='UTF-8') as f:
      for line in f:
        self.data.append(line)
```



```python
def md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def read_string(path):
    with open(path, "r", encoding='UTF-8') as f:
        return f.read()
```



### read lines

```python
		# 按行读取文本	
		with open(label_path, encoding='utf-8') as f:
            data = f.readlines()
        # utf8 bom 带签名的utf8    
        with open(label_path, encoding='utf-8-sig') as f:
            data = f.readlines()
```



#### 读任意行

```
# huggingface/RWKV-LM/RWKV-v5_nlpp/load_jsonl.py

rnd_idx = random.randint(1, num_entries)
	# [1, num] 之间的随机数

import json
import torch
from torch.utils.data import Dataset, DataLoader
import linecache

class LargeJSONLDataset(Dataset):
    def __init__(self, file_path):
        self.file_path = file_path
        # 计算文件中的数据行数，该步骤需要时间，因为要遍历整个文件
        self.num_entries = sum(1 for line in open(file_path))
    
    def __getitem__(self, index):
        line = linecache.getline(self.file_path, index+1)
        data = json.loads(line)
        return data
    
    def __len__(self):
        return self.num_entries

dataset = LargeJSONLDataset('traindata_ak48_nlpp.jsonl')
data_loader = DataLoader(dataset, batch_size=4, shuffle=True)

for data in data_loader:
    pass

```





### write file

```
with open(label_path, 'w', encoding='utf-8') as f:
	f.write('hi,,')

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
  
# Writing a string to file
file1.write(s)
  
# Writing multiple strings
# at a time
file1.writelines(L)
  
# Closing file
file1.close()
```



#### write bytes

```

# see huggingface/myvideo/demo/app.py
	def change_ABT(evt: gr.EventData):
        [ begintime, endtime, videoBase64UrlEndcode ] = evt._data
        # if isDebug: print("### change_ABT hit.", evt.target, [ begintime, endtime, videoBase64UrlEndcode ])
        # data:video/mp4;base64, 需要去掉最前面这一段 mime 它才是纯 base64
        videoBase64 = re.compile(r'^data:.+?;base64,').sub('', videoBase64UrlEndcode)
        videoBytes = base64.b64decode(videoBase64)
        print('write bytes:')
        with open(os.path.join(os.path.dirname(__file__), "trim.mp4"), "wb") as f:
            f.write(videoBytes)
        
        return evt._data
    out.change_AB_time(change_ABT, None, [])
```





#### 追加写

```

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write(f'hi,,')

# see InternLM\tools\tokenizer.py
with open(text_input_path, "r") as text_file, open(bin_output_path, "ab") as bin_file:
            for line in text_file:
                # Strip any leading/trailing whitespace
                stripped_line = line.strip()
                bin_file.write(saved_bin) # b'something'
```



### bytes

```
type ( bytes(1) ) == bytes
	--> True


# 如果你只是想依次读取并处理每个 1024 字节的数据块
while data:
    chunk, data = data[:1024], data[1024:]
    # 处理 chunk
    print(f'Chunk size: {len(chunk)}')


```





### size

```
import os
 
file_size = os.stat('d:/file.jpg')
print("Size of file :", file_size.st_size, "bytes")
```



### 遍历

```
    for root, dirs, files in os.walk(args.datasetRootPath):
        for dir in dirs:
```



### 递归遍历

```python
import glob
xmls = glob.glob('./db/economist/**/article.xml', recursive=True)
for xml in xmls:
	with open(xml, "r", encoding="utf-8") as fp:
		data = fp.read()

fnames2 = glob.glob(root + '/**/*.mkv', recursive=True)

```



### list all image



```python
from imutils import paths

for imagePath in paths.list_images(args["images"]):
  image = cv2.imdecode(np.fromfile(imagePath, dtype=np.uint8), -1)
```



### basename

```python
os.path.basename
```



```
# without ext
from pathlib import Path

Path('/root/dir/sub/file.ext').stem
will return

'file'
```





```
# base path
import os
print(os.path.splitext("/path/to/some/file.txt")[0])
>/path/to/some/file
```





### MD5

```python
dataset = {"id": hashlib.md5( bytes(k, encoding='utf-8') ).hexdigest(),  "summary":k, "text": []}
```

```python
inp = 'GeeksforGeeks'
result = hashlib.md5( bytes(inp, encoding='utf-8') )
print("The byte equivalent of hash is : ", end ="")
print(result.hexdigest())
```



#### file md5

```python
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
```



### stream

```python
'''
    PIL 转 bytes
'''
img_bytes  = BytesIO() # 这就是内存流
img = Image.open('test.jpg', mode='r')
img.save(img_bytes, format='JPEG')
img_bytes = img_bytes.getvalue()
print(type(img_bytes))
```



### 管道

```
Langchain 通过重写类的魔法方法__or__来实现管道
```





### tempfile

```python
# see https://github.com/gradio-app/gradio/issues/1972
out_file = tempfile.NamedTemporaryFile(suffix="out.mp4", delete=False)
subprocess.run(f"ffmpeg -y -loglevel quiet -stats -i {output_fname} -c:v libx264 {out_file.name}".split())
return out_file.name
```





## pickle 序列化存储

支持任何类型

[OrderedDict](https://stackoverflow.com/questions/45860040/pickling-a-subclass-of-an-ordereddict)

```
# pip install pickle5
import pickle

	with open(filename + ".pkl", "wb") as f:
 		pickle.dump(vectors, f)
 		
	with open(filename + ".pkl", "rb") as f:
    	global vectores
        vectors = pickle.load(f)
	

```





## OS



### 软链接



```
# create

import os

src = r"""D:\GitHub\doc\lang\programming\haskell\supermario\Util.hs"""

dst = r"""G:\tmp.hs"""

os.symlink(src, dst)
  
print("Symbolic link created successfully")

```

```
# modify
os.symlink(target, tmpLink)
os.replace(tmpLink, linkName)
You can check to make sure it was updated correctly too:

if os.path.realpath(linkName) == target:
    # Symlink was updated
```



```
# delete
os.unlink(dst)
```



```py
# check type
if not os.path.islink(link_name) and os.path.isdir(link_name):
```



### 命令行参数解析

```
# doc\lang\programming\python\opencv\模糊检测\detect_blur.py

import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
  help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
  help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())
```



### 设置环境变量

```
os.environ['RWKV_FLOAT_MODE'] = 'fp32'
```




## package

```python
import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg
python3 -m mypackage.A.spam # Relative imports work
```
### 绝大部分时候让__init__.py空着就好

- 让每个目录都包含一个__init__.py，就可以import

###  \_\_init\_\_.py 可以为下层目录代为import 一些东西

```python
# -*- coding: utf-8 -*-
from .util import *
```

> ```python
> # graphics/formats/__init__.py
> from . import jpg # 代替import graphics.formats.jpg
> from . import png # 以及import graphics.formats.png
> ```

```python
#-*- encoding:utf-8 -*-
from __future__ import absolute_import
# from .FastTextRank4Sentence import FastTextRank4Sentence
# from .TextRank4Sentence import TextRank4Sentence
from . import util
version = '0.2'
```



### 黑科技



#### CPU执行时间

```python
import time
tis1 =time.perf_counter()
print("等待5秒......")
time.sleep(5)
tis2=time.perf_counter()
print(tis2-tis1)
```




> 当一个文件夹下有   init   .py时，意为该文件夹是一个包（package），其下的多个模块（module）构成一个整体，而这些模块（module）都可通过同一个包（package）导入其他代码中。
>
> 其中   init   .py文件 用于组织包（package），方便管理各个模块之间的引用、控制着包的导入行为。
> 该文件可以什么内容都不写，即为空文件（为空时，仅仅用import [该包]形式 是什么也做不了的），存在即可，相当于一个标记。
> 但若想使用from pacakge_1 import *这种形式的写法，需在  init  .py中加上：   all    = [‘file_a’, ‘file_b’] #package_1下有file_a.py和file_b.py，在导入时   init   .py文件将被执行。
> 但不建议在   init   .py中写模块，以保证该文件简单。不过可在   init   .py导入我们需要的模块，以便避免一个个导入、方便使用。
>
> 其中，   all   是一个重要的变量，用来指定此包（package）被import *时，哪些模块（module）会被import进【当前作用域中】。不在   all   列表中的模块不会被其他程序引用。可以重写  all  ，如   all    = [‘当前所属包模块1名字’, ‘模块1名字’]，如果写了这个，则会按列表中的模块名进行导入。
>
> 在模糊导入时，形如from package import *，*是由__all__定义的。
>
> 精确导入，形如 from package import *、import package.class。
>
>    path   也是一个常用变量，是个列表，默认情况下只有一个元素，即当前包（package）的路径。修改   path   可改变包（package）内的搜索路径。
>
> 当我们在导入一个包（package）时（会先加载   init   .py定义的引入模块，然后再运行其他代码），实际上是导入的它的   init   .py文件（导入时，该文件自动运行，助我们一下导入该包中的多个模块）。我们可以在   init   .py中再导入其他的包（package）或模块 或自定义类。
> ————————————————
> [c](https://blog.csdn.net/weixin_38256474/java/article/details/81228492)



## 语法

```python
# 换行写法
def _lik(scores, p_val):
    # 似然函数
    loglik_val = np.dot(np.log(p_val + 1e-200), scores.transpose()) + \
                    np.dot(np.log(1 - p_val + 1e-200), (1 - scores).transpose())
    return np.exp(loglik_val)
# GitHub\doc\lang\programming\algo\EM.py
```



### Class

#### 属性

```python
class EAPIrt2PLModel(object):

    def __init__(self, score, slop, threshold): # 得分，区分度，阀值
        self.x_nodes, self.x_weights = get_gh_point(21)
        z = Z(slop, threshold, self.x_nodes)
        p = P(z)
        self.lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1) 
        """
        计算所有元素的乘积，按行连乘(维度变成n*1)。
        如果不指定轴，则不管是几维都展平成一维然后连乘
        """

    @property
    def g(self):
        x = self.x_nodes[:, 0]
        weight = self.x_weights[:, 0]
        return np.sum(x * weight * self.lik_values)

    @property
    def h(self):
        weight = self.x_weights[:, 0]
        return np.sum(weight * self.lik_values)

    @property
    def res(self):
        return round(self.g / self.h, 3)
```



### isinstance

```python
            if not isinstance(dest_width, int):
                dest_width = dest_width.item()
                dest_height = dest_height.item() # 张量中加不加item()会有微妙的差别 
            # doc\lang\programming\pytorch\文本检测\DBNET\main.py
            
            
            elif isinstance(e, json.JSONDecodeError):
                print(f'##### Error: JSON parse fail. sleeping 15 minute and try again...')
                time.sleep(15*60)            

```



### 默认参数

```
    def __init__(self, data_dir=None, data_list=None, cmd={}, **kwargs):
		self.debug = cmd.get('debug', False)
```



### hasattr

```
# DB\data\processes\augment_data.py
# 是否有这个属性
if hasattr(base, 'states'):
	states.update(base.states)
```



### 0 维数组

```
What you create with

a = np.array(1)
is a zero-dimensional array, and these cannot be indexed. You also don't need to index it -- you can use a directly as if it were a scalar value. If you really need the value in a different type, say float, you can explicitly convert it with float(a). If you need it in the base type of the array, you can use a.item() or a[()].

Note that the zero-dimensional array is mutable. If you change the value of the single entry in the array, this will be visible via all references to the array you stored. Use a.item() if you want to store an immutable value.

If you want a one-dimensional array with a single element instead, use

a = np.array([1])
You can access the single element with a[0] now.
```



### 元类

拦截类的构造函数，调用元类的 \__new\__ 方法来给类加料（新增修改函数属性什么的）

```
class State:
    def __init__(self, autoload=True, default=None):
        self.autoload = autoload
        self.default = default


class StateMeta(type):
    def __new__(mcs, name, bases, attrs):
        current_states = []
        for key, value in attrs.items():
            if isinstance(value, State):
                current_states.append((key, value))

        current_states.sort(key=lambda x: x[0])
        attrs['states'] = OrderedDict(current_states)
        new_class = super(StateMeta, mcs).__new__(mcs, name, bases, attrs)

        # Walk through the MRO
        states = OrderedDict()
        for base in reversed(new_class.__mro__):
            if hasattr(base, 'states'):
                states.update(base.states)
        new_class.states = states

        for key, value in states.items():
            setattr(new_class, key, value.default)

        return new_class


class Configurable(metaclass=StateMeta):
    def __init__(self, *args, cmd={}, **kwargs):
        self.load_all(cmd=cmd, **kwargs)

    @staticmethod
    def construct_class_from_config(args):
        cls = Configurable.extract_class_from_args(args)
        return cls(**args)
```



### Annotated

```python
huggingface/myvideo/readme.txt
	    /root/miniforge3/envs/gradiomyvideo/lib/python3.10/site-packages/gradio/cli/commands/components/dev.py
    line 51 下断点
    component_directory = component_directory.resolve()
        # 成功断下
        
    app: Annotated[
        Path,
        typer.Argument(
            help="The path to the app. By default, looks for demo/app.py in the current directory."
        ),
    ] = Path("demo") / "app.py"
    
```





## OP



### logic



```python
if x is not None
a-b if a>b else a+b
```



### round

```python
round(2.145,2) # 四舍六入五成双 # 它的作用是让统计数据更公平，降低舍入的误差
> 2.15 # 保留两位小数
```



### sigmoid



输入正数，值域在0.5 ~ 1 之间

  $h(x)=\frac{1}{1+e^{-x}}$

```python
exp(-x)
```



### log

```python
np.log(x) 以e为底的对数(自然对数)
np.log10(x) 以10为底的对数
np.log2(x) 以2为底的对数
np.log1p(x) 等价于：np.log(x + 1)
备注：np.expm1(x) 等价于 np.exp(x) - 1，也是np.log1p(x)的逆运算。
```

```
math.pi：圆周率，值为3.141592653589793.
math.e：自然对数，值为2.718281828459045.
math.inf：正无穷大，负无穷大为-math.inf.
math.nan：Not a Number，非正常值
```







## 递归方法



```python
#  收集所有Childs 的大纲outline，挂到结点下
def collectAllChildsOutline(tree):

    def walk(d, father, cur, maxIter):
        if cur > maxIter:
            return

        if "Childs" not in d:  # 叶子结点，给它的父数组贡献大纲
            if "Outlines" not in father:
                father["Outlines"] = []
            if "level" in d:
                if d["level"] != '-':
                    father["Outlines"].append(replaceOutline(d["level"])) # 父数组加子结点大纲

        if "Childs" in d:                    # 非叶子结点
           for dd in d["Childs"]:            # 遍历孩子
               walk(dd, d, cur+1, maxIter)   # 递归孩子
               if "Outlines" not in d:       # 递归结束后，叶子结点的上一层已经有了大纲
                    d["Outlines"] = []       # d  是当前非叶子
               if "Outlines" in dd:          # dd 是当前非叶子的孩子
                    if "level" in dd and dd["level"] != '-':        # 如果当前孩子有大纲 
                        d["Outlines"] += [ replaceOutline(dd["level"]) ] + dd["Outlines"]   # 当前非叶子大纲数组  加上  当前孩子大纲，当前孩子大纲数组
                    else:                    # 如果当前孩子无大纲
                        d["Outlines"] += dd["Outlines"]                     # 当前非叶子大纲数组  加上  当前孩子大纲数组
    for d in tree:
        walk(d, d, 1, 5)
    
    return tree
```







## 静态函数 构造函数 析构函数

```python
 @staticmethod
 def connect():
 
 def __init__(self):
 def __del__(self):
```



## 变长参数

> *args 与 **kwargs 的区别，两者都是 python 中的可变参数：
>
> - *args 表示任何多个无名参数，它本质是一个 tuple
> - **kwargs 表示关键字参数，它本质上是一个 dict
>
> 如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前。
>
> ```python
> >>> def fun(*args, **kwargs):
> 	print('args=', args)
> 	print('kwargs=', kwargs)
> args= (1, 2, 3, 4)
> kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
> ```

> a, b, *c = 0, 1, 2, 3  
>
> --> c  
>
> [2, 3]



## 当前函数名

```python
 print(sys._getframe().f_code.co_name)
 print(inspect.stack()[0][3])
```





## Handle Error



```python
raise RuntimeError('some err')
```



## Exception

```python
    try:
        json.loads( dic["TestJson"], strict=False )
    except Exception as e:
        print ( str(e) )
        print ('testjson err: \n\n', dic["TestJson"])

```



## For



```python
 [x for x in range(11) if x%2 == 0]
 len([ k for k, _ in tasks.items()]) # 现有总任务数
```



```python
#  see gradio440/lib/python3.10/site-packages/jinja2/loaders.py
		for searchpath in self.searchpath:
            # Use posixpath even on Windows to avoid "drive:" or UNC
            # segments breaking out of the search directory.
            filename = posixpath.join(searchpath, *pieces)

            if os.path.isfile(filename):
                break
        else:
            raise TemplateNotFound(template)
```





## yield



```python
# see huggingface\rwkv5-jp-explain\gptchat.py
import openai
import json
import time
import streamlit as st

with open("config.json", "r", encoding='UTF-8') as f:
    api_key = json.load(f)["api_key"]

def chat_gpt4(api_key, q):
    import openai
    openai.api_key = api_key
    stream = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{q}"}],
        stream=True,
        timeout=30
    )
    for chunk in stream:
        text = chunk.choices[0].delta.content or ""
        yield text


st.title('Stream LLM responses')


prompt = st.text_input(label="Prompt: ", value="")

submit_button_exist = st.button('Submit', use_container_width=True)

answer=''
if submit_button_exist and prompt:
    c = st.empty()
    it = iter(chat_gpt4(api_key, prompt))
    for text in it:
        answer += text
        c.write(answer)
else: 
   st.write("")

```





```python
def infinite_iter(data_loader):
  it = iter(data_loader)
  while True:
    try:
      ret = next(it)
      yield ret
    except StopIteration:
      it = iter(data_loader)
```



```python
def custom_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# 使用iter来获取迭代器
my_iterator = iter(custom_range(0, 5))

# 迭代迭代器中的元素
for number in my_iterator:
    print(number)

```





```python
class Repeater:
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        self.count = 0

    def __iter__(self):
        # 每次迭代时都会调用这个方法
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.value

# 创建Repeater类的实例
repeater = Repeater('Hello', 3)

# 不直接使用yield，但通过iter和类的迭代器协议提供类似的行为
for item in repeater:
    print(item)

```





```python
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count
    return total,count,average

# 调用方
def main():
    calc_average = average_gen()
    next(calc_average)            # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

    # ----------------注意-----------------
    try:
        calc_average.send(None)
    except StopIteration as e:
        total, count, average = e.value
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))
    # ----------------注意-----------------

if __name__ == '__main__':
    main()
```







## Filter



```python
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
sorted(results, key=lambda l: l[3], reverse=True) # 按相似度高到低排序
list(filter(lambda w: not bool(re.match(r'[^\u4e00-\u9fa5]', w)), words)) # 过滤非中文词
{k: v for k, v in points.items() if v[0] < 5 and v[1] < 5}
lambda 返回true 的保留
```



## List



### 可变参数列表

```
in_axes = ['inputs', 'hidden', ...] # ... 意思是后面可以有其它东西，没有也行
print( in_axes )
```



### Select

#### 随机选择元素

```
# 不重复的抽
from random import sample
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(sample(l, 5)) # 随机抽取5个元素
```



```
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Grab a single random input
x = inputs[onp.random.choice(inputs.shape[0])]
# Compute the target output
y = np.bitwise_xor(*x)
```







### range



```python
list( range(5, 0, -1) )  # begin, stop, step
[5, 4, 3, 2, 1]
```



### group



```python
a = list(range(5))
[ a[i:i+2] for i in range(0, len(a), 2) ]
```





### Map

```python
__version_info__ = (0, 1, 1, 0)
__version__ = '.'.join(map(str,__version_info__))
```



### zip

#### 有序对

```
for sentence, target in zip(sentences, targets):
	sentence = cut_token(sentence)
	
	
for _, (url, filename) in enumerate(zip(urls, filenames)):
	# 前面是 index
	# urls, filenames 都是数组

```





###  iterate with index



```python
for i, name in enumerate(names):
    print(i, name)
```

```
# list 转字典
us_dic = { w:i for i, w in enumerate(us) }
```



### index



```
   doc\lang\programming\pytorch\数字识别\digit_torch_version2.ipynb
   
   # Output of the network are log-probabilities, need to take exponential for probabilities
    ps = torch.exp(logps)

    import pdb; pdb.set_trace() # 调试， exit 退出

    probab = list(ps.cpu().numpy()[0])
    pred_label = probab.index(max(probab))  # 这一句特别精髓
    	# 先求list 里的最大值，再求最大值在list 里的索引，索引既是手写数字的以预测值
```



### array[None, ...]

```python
# ... 表示全部要？  array[None, ...] 表示最外面添加一个维度 (1, 后面不变) ，后面维度不变
def v_replicate(maybe_array):
    if eqx.is_array(maybe_array):
        return jnp.repeat(maybe_array[None, ...], n_dev, 0)
    return maybe_array

v_model = jax.tree_map(
    v_replicate,
    model,
)
```



```python
# None 意思是添加一个维度？

import numpy as np

a = np.random.rand(3,2)


print(a[None,:].shape) # output: (1, 3, 2)
print(a[:,None].shape) # output: (3, 1, 2)
print(a[:,None,:,None].shape) # output: (3, 1, 2, 1)
print(a[:,None,None, :].shape) # output: (3, 1, 1, 2)

print(a[:,None,:,:]) # IndexError: too many indices for array: array is 2-dimensional, but 3 were indexed

it practically acts as np.expand_dims function to add a dummy axis where I want

```







### slice



```python
To slice a list, there's a simple syntax: array[start:stop:step]
You can omit any parameter. These are all valid: array[start:], array[:stop], array[::step]
```



```python
x = x_nodes[:, 0] # 行全要,列只要第0列.结果是二维变一维
# (11,1) -> (11,)
```



```python
self.std[:, None, None]  # 这是不要另外两维？
```







product 笛卡尔集



### delete 

```python
        for t, l in tests_segs.items():  # t: 'BTEST', 'XTEST'，l: [ {'ChildTestID': '27001584'...} ]
            removes = []
            for i in range(len(l)):
                d = l[i]
                key = f"{d['TestID']},{d['ChildTestID']}"
                if key in dicDup:
                    removes.append(i)  # 记录待删除的项
            print('before del: ', len(l))
            for i in sorted(removes, reverse = True):  # 排序，从后面开始删起。前面的索引是不会变的
                del l[i]
            print('after del:', len(l))
```





### delete_duplicates



```python
from collections import OrderedDict

def delete_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))
```



```
sum( list( map(lambda k: len( tests_segs[k] ), tests_segs) ) )
```



### copy

```python
import copy
tests_segsNew = copy.deepcopy(tests_segs)
```





### sorted



```python
    pths = sorted(pths, key=lambda p:(
        match := re.findall(r'.+?Siren14Voice_(.+?)\.(.+?)\.aac', p),
        number := int(match[0][0]),
        seasion := match[0][1],
        (seasion, number) # 如果第一项相等就会比较第二项
    ))
```





```python
sorted(results, key=lambda l: l[3], reverse=True) # 按相似度高到低排序

math.log(len(arr[6])) # 可以近似认为后一项的值域是 [0, 10]
```



```python
index = np.sort(np.intersect1d(rt[N-2], pp2.index)) # 作交集
```



```
In [36]: import random

In [37]: List = [1,2,3,4,5,6]
In [38]: random.shuffle(List)
In [39]: print(List)
[2, 1, 6, 4, 5, 3]
random.sample(sequence,k)
sample，样品，从有序列表中选k个作为一个片段返回。
```





### Shuffle two array



```python
# OR_JAX_vmap.py
# 以同样的顺序随机排序两个数组
import numpy as onp
import jax
import jax.numpy as np

X = np.array([
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]
             ], onp.float)

Y = np.array([
                [0],
                [1],
                [1],
                [1]
             ], onp.float)


randomize = onp.arange(len(X))
onp.random.shuffle(randomize)

X = X[ randomize ]
Y = Y[ randomize ]

print( X )
print( Y )
```



```
# 以同样的顺序随机排序两个数组
import random
 
# initializing lists
test_list1 = [6, 4, 8, 9, 10]
test_list2 = [1, 2, 3, 4, 5]
 
# printing lists
print(f"The original list 1 : {test_list1}")
print(f"The original list 2 : {test_list2}")
 
# Shuffle two lists with same order
# Using zip() + * operator + shuffle()
temp = list(zip(test_list1, test_list2))
random.shuffle(temp)
res1, res2 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
res1, res2 = list(res1), list(res2)
 
# Printing result
print(f"List 1 after shuffle :  {res1}")
print(f"List 2 after shuffle :  {res2}")
```





### remove the value  first occur

a.remove(1)



### join as string



```python
l = ['1','2','3']
print(",".join(l))
```



### convert 

#### convert list to dict

```
def listToDict(lst):
    op = { i: lst[i] for i in range(0, len(lst), 1)}
    return op
```



#### convert bool to int

```
ignore_tags = np.array(ignore_tags, dtype=np.uint8) # ignore_tags 原来是 bool list
```



### subtract

- list - list 是相同position 的值分别相减，构成一个新list

	if sum( WS - last_WS ) < 1e-12:  # 提前结束计算，如果误差值小于一定值
		print('break loop now. current iterate num: ', k+1, 'deviation sum is:', sum( WS - last_WS ))
		break



#### mean image

```
X -= np.mean(X, axis=0)  # 减去均值
```



### intersect

```python
index = np.sort(np.intersect1d(rt[N-2], pp2.index)) # 作交集
```

```
a = t | s          # t 和 s的并集  
b = t & s          # t 和 s的交集  
c = t – s          # 求差集（项在t中，但不在s中）  
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）  
```





### transpose

```python
np.transpose(arr)
```



### dot

```python
A = np.dot(X, W) + b
```



### flatten



```python
import itertools
list(itertools.chain(*abs(E)))
```



### 批量四舍五入

```python
# points 的shape 是(4,2) 的二维数组，浮点型 
points = np.round(points, decimals=0).astype(np.int32)
```



### reduce

```python
# 所有list of list 中的list 累加，效果是全部合并在一起 
from functools import reduce
fils = reduce(lambda ls1, ls2: ls1+ls2, fils)
```



### sublist

```
def subLists(l, n):
    return [ l[i:i + n] for i in range(0, len(l), n)  ]
print( subLists(l, 0) )
```



### shape



```python
m = X.shape[0] # 样本数
```



### random

```python
随机排列一个序列，返回一个排列的序列。
>>> np.random.permutation(10)
array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6])
>>> np.random.permutation([1, 4, 9, 12, 15])
array([15,  1,  9,  4, 12])
>>> arr = np.arange(9).reshape((3, 3))
>>> np.random.permutation(arr)
array([[6, 7, 8],
       [0, 1, 2],
       [3, 4, 5]])

np.random.shuffle(arr) #在原数组上改变顺序,无返回值 同random.shuffle()
arr = np.random.permutation([1, 4, 9, 12, 15]) #不在原数组上进行，返回新的数组，不改变自身数组
```



### 排列组合

- https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p09_iterate_over_combination_or_permutation.html



#### 排列

```python
items = ['a', 'b', 'c', 'd']
from itertools import permutations
for p in permutations(items, 3): # 4 选 3 的排列
	print(p)

perm = permutations(items, 3)
length = len(list(perm))  # 排列数

print(length)

```



#### 组合

```
items = ['a', 'b', 'c', 'd']
from itertools import permutations, combinations

for c in combinations(items, 3): # 4 选 3 的组合
    print(c)

perm = combinations(items, 3) # 组合数
length = len(list(perm))

print(length)
```



#### 允许重复选择

```
items = ['a', 'b']
from itertools import permutations, combinations, combinations_with_replacement

for c in combinations_with_replacement(items, 3): # 二选三的组合
    print(c)
```



```
# 有奇怪的问题
items = [0, 1]
from itertools import permutations, combinations, combinations_with_replacement

comb = combinations_with_replacement(items, 7)
for c in combinations_with_replacement(items, 7):  # 体现在打印和转list上，打印完转list后是空
    print(c)

ls_comb = list(comb)

length = len(ls_comb)

print(length)

for p in permutations([0,0,0,0,1,1,1]):
    print(p)
```









## parallel 进程



```python
# 多进程不能共享变量
from joblib import Parallel, delayed
def parallelCompare(func, l):
    def f(l, i):
        rs = []
        for j in range(i+1, len(l)):
            rs.append( (i, j) )
        return rs
    return Parallel(n_jobs=os.cpu_count(), verbose=10)(delayed(f)(l, i) for i in range(len(l)-1))

# 多线程可以共享变量，但要注意写入冲突
Parallel(n_jobs=4, backend="threading")
```



```python
# 异步回调
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

    def done(futures):
        print('############ call into callback function')
        global g_planktestsim_done
        sims_MultipleApp = futures.result()  #会得到一个返回值，这个返回值就是task函数的返回值
        del tasks_planktestsim[key] # 移除已完成任务

        data = simtests.tempResult()
        data["finished"] = True

        data = copy.deepcopy(data)
        simtests.saveTempResult(key2, data)
        simtests.resetTempResult()
        # g_planktestsim_done = True

    futures = executor.submit(simtests.calcSimtest, appids, threshold, MaxResults)
    futures.add_done_callback(done)

```



```python
    def parallelCompare(l, tests, origs):
        def f(l, i, ts, rgs):
            k = l[i][0]
            appid, TestID, ChildTestID = k.split(',')
            seg_titleright = ts[k]["seg_titleright"]
            titleright = ts[k]["titleright"]

            rs = []
            l2 = l[i][1]
            for k2 in l2:
                appid2, TestID2, ChildTestID2 = k2.split(',')
                seg_titleright2 = ts[k2]["seg_titleright"]
                titleright2 = ts[k2]["titleright"]

                

            return rs
        return Parallel(n_jobs=1, verbose=10)(delayed(f)(l, i, tests, origs) for i in range(len(l))) # os.cpu_count()

    results = parallelCompare(compare_tids, inverttests, ts_dic)
```



```
# 共享内存
https://joblib.readthedocs.io/en/latest/auto_examples/parallel_memmap.html#sphx-glr-auto-examples-parallel-memmap-py

https://zhuanlan.zhihu.com/p/146769255

对于cpu密集型的任务来说，线程数等于cpu数是最好的了

# 进程池
https://juejin.cn/post/6856222178250391560

```



```
# 全局锁
def send_request(data):
	api_url = 'http://api.xxxx.com/?data=%s'
	start_time = clock()
	print urllib2.urlopen(api_url % data).read()
	end_time = clock()
	lock.acquire()
	whit open('request.log', 'a+') as logs:
		logs.write('request %s cost: %s\n' % (data, end_time - start_time))
	lock.release()
def init(l):
	global lock
	lock = l
 
if __name__ == '__main__':
	data_list = ['data1', 'data2', 'data3']
	lock = Lock()
	pool = Pool(8, initializer=init, initargs=(lock,))
	pool.map(send_request, data_list)
	pool.close()
	pool.join()
```





```
# 线程池
from concurrent import futures

def task(n):
    print(n)

with futures.ThreadPoolExecutor(max_workers=2) as ex:
    print('main: starting')
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)

print('main: done')
```



#### 异步任务

```
    import asyncio

    async def my_task(name, delay):
        print(f"Task {name} started")
        await asyncio.sleep(delay)
        print(f"Task {name} completed")

    async def main():
        # 创建多个异步任务
        task1 = asyncio.create_task(my_task("A", 2))
        task2 = asyncio.create_task(my_task("B", 1))
        task3 = asyncio.create_task(my_task("C", 3))

        # 等待所有任务完成
        await asyncio.gather(task1, task2, task3)

    # 运行主异步函数
    asyncio.run(main())
```



#### 多线程

```
def rec():
    
    if os.path.exists(asrtxt):
        os.remove(asrtxt)
    
    import threading
    import time

    def task_soda_asr():
        def result_callback(s, type):
            """
            因为这个回调是传给 .so 库去执行的，它访问不到 python 的变量，只能通过文件写入识别结果了
            """
            with open(asrtxt, 'a', encoding='utf-8') as f:
                f.write(s+'\n')
            if type == 'end':
                print(s)
            else:
                print(s, end='\n')

        
        client = SodaClient()

        try:
            client.start(wav_path=wav, result_callback=result_callback)
        except KeyboardInterrupt:
            client.delete()

    # 创建线程
    thread = threading.Thread(target=task_soda_asr)

    # 启动线程
    thread.start()
    
    while thread.is_alive():
        print("Thread is still running...")
        time.sleep(1)

    print("Thread has completed")
    
    # thread.join() # 等待线程完成 阻塞模式
    
```



#### 管道通信

https://benpaodewoniu.github.io/2022/10/07/python172/  pipe 管道通信



```
# see /root/huggingface/rwkv5-jp-trimvd/appv2.py -> click_button_asr
# see /root/huggingface/rwkv5-jp-trimvd/asr.py
def rec2():
        
    import multiprocessing

    def task_soda_asr(conn2, wav_pth):
        def result_callback(s, type):
            """
            语音识别结果回调
            """
            conn2.send(s)
        
        client = SodaClient()

        try:
            client.start(wav_path=wav_pth, result_callback=result_callback)
        except KeyboardInterrupt:
            client.delete()
        
        client.delete()
        conn2.send('<|eNd|>')

    conn1, conn2 = multiprocessing.Pipe(False)
    	# True，表示该管道是双向的，即位于 2 个端口的进程既可以发送数据，也可以接受数据。
	    # False，则表示管道是单向的，conn1 只能用来接收数据，而 conn2 只能用来发送数据。
    process = multiprocessing.Process(target=task_soda_asr, args=(conn2, wav))
    process.start()
    while process.is_alive():
        s = conn1.recv()
        if s == '<|eNd|>':
            break
        yield s


if __name__ == '__main__':

    it = rec2()
    for s in it:
        print(s)
        
```





#### 进程池锁

```python

import os, sys
sys.path.append('../..')
import std.iJson as iJson

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity, paired_distances  # 余弦相似度

import numpy as np

import multiprocessing

def load(fname_invertedIndexs):
    if os.path.exists( fname_invertedIndexs ):
        print('loading exists invertedIndexs...')
        t = iJson.load_json(fname_invertedIndexs)
        return t[0], t[1], t[2]

def func( shared_wds, shared_ts, cmprs, shared_estids, k, i ):
    tids = [] # 所有可能需要比较的题id
    seg_titleright = shared_ts[k]["seg_titleright"]
    for w in seg_titleright:
        tids += shared_wds[w]
        
    tids = list( set(tids) ) # 去重
    if len(tids) > 0:
        cmprs.append( [k, tids] ) 

    print('\n task ', i, 'done.')



# 余弦相似度
def sim_cos(ws1, ws2):

    s1 = set(ws1)
    s2 = set(ws2)

    # 相同的词太少不比较
    ss1 = list( s1 )
    ss2 = list( s2 )
    longs = max( len(ss1), len(ss2) )

    sames = list( np.intersect1d(ss1, ss2) ) # list( np.intersect1d(s1, s2) ) # 求交集，得到相同词列表
    if len(sames) == 0:
        return -1
    if longs / len(sames) >= 4:
        return -1

    counts1 = pd.Series(ws1).value_counts() # 统计每个词出现多少次
    counts2 = pd.Series(ws2).value_counts()


    us = list( s1.union(s2) )
    idxs = { w:i for i, w in enumerate(us) }

    v1 = [ 0 for i in range( len(us) ) ]
    v2 = [ 0 for i in range( len(us) ) ]

    for w, c in counts1.items():
        v1[ idxs[w] ] = c

    for w, c in counts2.items():
        v2[ idxs[w] ] = c

    # 余弦相似度
    simi = cosine_similarity([v1], [v2])[0][0]

    return round(simi, 4)


def compare_parllel( shared_wds, shared_ts, cmprs, shared_estids, k, i, threshold = 0.9 ):

    # 长度差太多就不用比
    def skipQ(ws1, ws2):
        len1 = len(ws1)
        len2 = len(ws2)

        if len1 == 0 or len2 == 0:
            return True

        if max(len1, len2) / min(len1, len2) >= 4: # 长度差5倍以上不用比
            return True

        return False

    tids = [] # 所有可能需要比较的题id
    seg_titleright = shared_ts[k]["seg_titleright"]
    for w in seg_titleright:
        tids += shared_wds[w]
        
    tids = list( set(tids) ) # 去重


    appid, TestID, ChildTestID = k.split(',')

    tmp = []
    for k2 in tids:
        if k == k2:  # 不用和自已比
            continue
        
        appid2, TestID2, ChildTestID2 = k2.split(',')
        seg_titleright2 = shared_ts[k2]["seg_titleright"]
        
        if appid == appid2 and TestID == TestID2: # 相同大题不比较
            continue
        
        skQ = skipQ(seg_titleright, seg_titleright2)
        if skQ:
            continue
        
        sim = sim_cos(seg_titleright, seg_titleright2) # 余弦距离相似度

        if sim >= threshold:
            k3 = k + "," + k2
            k4 = k2 + "," + k
            if k3 not in shared_estids and k4 not in shared_estids:
                lock.acquire()
                shared_estids[k3] = True
                shared_estids[k4] = True
                lock.release()

                tmp.append( [ k2, round(sim, 4) ] )
    
    if len(tmp) > 0:
        tmp = [k] + tmp
        cmprs.append( tmp )

    print('\n task ', i, 'done.')



def init(l):
	global lock
	lock = l

if __name__ == "__main__":

    appids = [4468, 4469]

    currDir = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'cache' )   

    if not os.path.exists( currDir ):
        os.makedirs( currDir )

    tmp = ",".join( list( map(lambda n:str(n),appids) ) )
    fname_invertedIndexs = os.path.join(currDir, tmp+'invertedIndexs.json')

    invertwords, inverttests, ts_dic = load(fname_invertedIndexs)


    lock = multiprocessing.Lock()

    pool = multiprocessing.Pool(processes = os.cpu_count(), initializer=init, initargs=(lock,)) # os.cpu_count()

    # 多进程共享变量
    manager = multiprocessing.Manager()
    shared_invertwords = manager.dict(invertwords)
    shared_inverttests = manager.dict(inverttests)

    shared_existids = manager.dict() # 记录已存在id，防止重复添加


    cmprs = manager.list()

    
    keys = list( inverttests.keys() )
    keys = keys[:100]

    for i, k in enumerate(keys):
        pool.apply_async(compare_parllel, ( shared_invertwords, shared_inverttests, cmprs, shared_existids, k, i, 0.8 ))

    pool.close()
    pool.join()

    cmprs = list(cmprs)

    print('all task done. result num:', len(cmprs))

```







## Tuples

```
(0, )  # 这是tuples，逗号不能省略，否则它就是一个整数零
```

```
a, b = b, a 等价于 (a, b) = (b, a), list 没有这模式匹配特性
```

```
return 1 if probably >= 0.5 else 0, probably
```



### immutable

tuple对象不可改变



### hashable 

tuple 是hashable 类型（取决于里面放什么），所以tuple可以做dict的key



tuple还用来返回多值

> x, y = getPoint()



### tuple efficient than list

tuple以放弃对元素的增删为代价换取了性能上比list 更高的优点





## Set

```
list(set(a).intersection(set(b)))  # 交集  Or t & s
list(set(b).difference(set(a))) # 差集  Or t - s
t.union(s) # 并集 Or t | s  Or t ^ s
t.symmetric_difference(s) # 对称差集
```





## Dictionary

- map 一个字典会得到key



### **kwargs 展开合并字典

```
class ParamsDict:
    def __init__(self, dic_1, **kwargs):
        # kwargs 是一个字典，形参里面 k=2,j=3 这样传
        self.params = {**dic_1, **kwargs}
        	# **作用是展开字典，{**dic1, **dic2} 作用是合并两个字典

e = ParamsDict({'a':0, 'b':1}, k=2,j=3)
e.params['a'] = 0.0
```





### keys

```
mydict = {1: 'Geeks', 2: 'for', 3: 'geeks'}
keysList = list(mydict.keys())
print(keysList)


Accessing dict keys like an attribute

class AttributeDict(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        self[attr] = value

AttributeDict({"det_algorithm": "DB"})

```



### json

```python
import json
import decimal
import datetime

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json 
def parse(s):
    return json.loads(s, strict=False )

# convert dict to string
def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)

if __name__ == "__main__":
    dicts = { 0:'中文', 1:'b' }
    save_json('./j.json', dicts)
    print(string(dicts))
```



```python
out_json = dict()
out_json['images'] = []
```





### trick

```python
def weights_replaceinto(ls):
    sqls = []
    for d in ls:
        columns = ",".join( list(d.keys()) )
        values = ",".join( ( map(lambda w: r"'" + w + r"'" ,list(d.values()) ) ) )
        sqls.append(f"INSERT INTO weights ({columns}) VALUES({values}) ON DUPLICATE KEY UPDATE updateTime=now();")
```



### Check if a given key already exists in a dictionary



```python
'key1' in dict  # will return True or False

if "cc" in {"cc", "component"}:
    # 这个其实是集合 set

```



### for k, v 



```python
for k, v in d.items():
```



###  Get first value



```python
list(d.values())[0]
tmp = sorted(tmp, key=lambda d: list(d.values())[0], reverse=True) # 按词频高到低排序
```



### Get default if none

```
# doc\lang\programming\pytorch\李宏毅2020机器翻译\iAttention.py
word2int_en.get(word, UNK)  # key 不存在，则返回默认值UNK
```



### 灵活更新key,value

```

line = {'points':[[323.0, 621.0], [1186.0, 652.0], [1178.0, 864.0], [315.0, 833.0]]
'text':'0'
'ignore':False}

lines = []
lines.append({**line, 'points': poly}) # poly 是新的 points ，意思是更新points，其他该有的还有，保持不变？
```



### pop value

```python
# doc\lang\programming\pytorch\文本检测\DBNET\DBNet官方实现\DB\train.py
# 取值，然后从字典里面删除那个key
import importlib

    @staticmethod
    def extract_class_from_args(args):
        cls = args.copy().pop('class')  # args 是字典
        package, cls = cls.rsplit('.', 1) # 是字符串 xxx.xxx
        module = importlib.import_module(package)
        cls = getattr(module, cls)
        return cls
```



```python
    def load(self, state_name, **kwargs):
        # FIXME: kwargs should be filtered
        # Args passed from command line
        cmd = kwargs.pop('cmd', dict())  # 第二参的 dict() 是什么？
        if state_name in kwargs:
            setattr(self, state_name, self.create_member_from_config(
                (kwargs[state_name], cmd)))
        else:
            setattr(self, state_name, self.states[state_name].default)
```



### OrderedDict

```python
from collections import OrderedDict

	return OrderedDict(image=data['image'],
                           polygons=polygons,
                           ignore_tags=ignore_tags,
                           shape=shape,
                           filename=filename,
                           is_training=data['is_training'])


# OrderedDict 和 json 互转
import json
import collections

data =  {
        "id" : "de",
        "Key" : "1234567",
        "from" : "test@test.com",
        "expires" : "2018-04-25 18:45:48.3166159",
        "command" : "method.exec",
        "params" : {
          "method" : "cmd",
          "Key" : "default",
          "params" : {
            "command" : "testing 23"
          }
        }}

data_str = json.dumps(data)
result = json.loads(data_str, object_pairs_hook=collections.OrderedDict)
print(result)

```



### AttributeDict

```
class AttributeDict(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        self[attr] = value
	# 可以用 . 来访问 key

```





### Order



```python
d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = sorted(d.items(), key=lambda x: x[1])    
print(a)
```





```python
    # 通过构造有序字典，根据词频排序
    for cptid in results:
        d = results[cptid]
        tmp = []
        for k, v in d.items():
            tmp.append({k:v})
        tmp = sorted(tmp, key=lambda d: list(d.values())[0], reverse=True) # 按词频高到低排序
        orderDic = collections.OrderedDict()
        for dd in tmp:
            for k, v in dd.items():
                orderDic[k] = v
        results[cptid] = dict( orderDic)
```



### Key With Max vaule



```python
k = max(Outlines, key=Outlines.get) # 拥有最大值的键
```



### Max value

```python
dic={0: 1.4984074067880424, 1: 1.0984074067880423, 2: 1.8984074067880425, 3: 2.2984074067880425, 4: 2.2984074067880425}
max_value = max(dic.values())  # maximum value
max_keys = [k for k, v in dic.items() if v == max_value] # getting all keys containing the `maximum`

print(max_value, max_keys)
```



### update

```
# 批量修改 key, value
/root/DB/data/processes/make_seg_detection_data.py
		data.update(image=image,
                    polygons=polygons,
                    gt=gt, mask=mask, filename=filename)
```





### 递归生成知识点目录

```python

import os, sys; sys.path.append( os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) )  # std 包在此模块的上上上级目录
import math
import std.iFile as iFile
import std.iJson as iJson
import std.iList as iList
#import std.seg.iSeg as iSeg
import std.iSql as iSql
import util.saveTempData as saveTempData
import util.fectchData as fectchData

#from reg import inverseQuestionQ
#from optimization import similarOfSentsWithMedWords
#from optimization import medWords

import pandas as pd
import re

appid = 16629

# SELECT * from appinfo a WHERE a.AppEname = 'ZC_ZGHS_YTMJ_TEST';
# 16629  ZC_ZGHS_YTMJ_TEST  2020版主管护师考试宝典(护理学)特训密卷［专业代码：368］

"""

查出所有根结点
    SELECT ID AS menuID, PID, `name` FROM trialexampointmenus ts WHERE ts.appid = 16629 AND ts.`enable` = 1 AND ID IN (13394,15859,17852,19629,21271,22383,22660,22897);
        # 本来条件应该是 PID == -1, 但是根结点有很多重复，所以指定了ID

得到根结点再递归遍历它们的子结点


TODO:
    构造两颗树
        1. 基于trialexampointmenus 表的知识点目录树
        2. 基于护理学（中级）大纲.xls 导出文本的目录树
    
    对比两颗树，找出需要掌握的熟练度   


Pandas处理Excel - 复杂多列到多行转换（三十八）
https://blog.csdn.net/qq_41706810/article/details/106042694

Pandas | 表格整合三大神技之CONCATENATE
https://zhuanlan.zhihu.com/p/24892205


SELECT ID AS menuID, PID, `name` FROM trialexampointmenus ts WHERE ts.appid = 16629 AND ts.`enable` = 1;

PID = -1 的是root, 否则它的father 是menuID = 它的PID 的结点

"""

rootids = [13394,15859,17852,19629,21271,22383,22660,22897]

def addChilds(menus, rootnode):
    def add(menus, node, cur, maxIter):
        if cur > maxIter:
            return
        mid = node["menuID"]
        for d in menus: 
            if d["PID"] == mid:
                if "Childs" not in node:
                    node["Childs"] = []
                newd = d.copy()
                node["Childs"].append(newd)
                add(menus, newd, cur+1, maxIter)

    add(menus, rootnode, 1, 5)

def menuTree(menus):
    tree = []
    for d in menus:
        if d["menuID"] in rootids:
            tree.append( d.copy() )
    #print(tree)
    for d in tree:
        addChilds(menus, d)
    #print(tree)
    return tree

def readCSV():
    currDir = os.path.dirname(os.path.abspath(__file__))
    fname_csv = os.path.join(currDir, '大纲.csv') # '大纲.xls'
    ds = pd.read_csv(fname_csv, usecols= ['无'], encoding='gbk') # utf-8
    print(ds.shape, ds.size)
    for l in ds.values:
        if type(l[0]) == str:
            print(l[0])
    

if __name__ == "__main__":
    currDir = os.path.dirname(os.path.abspath(__file__))
    fname_tree = os.path.join(currDir, 'tree.json')
    fname_menus = os.path.join(currDir, 'menus.json')
    menus = fectchData.query('SELECT ID AS menuID, PID, `name` FROM trialexampointmenus ts WHERE ts.appid = 16629 AND ts.`enable` = 1;')
    #print(menus)
    tree = menuTree(menus)
    iJson.save_json(fname_tree, tree)
    iJson.save_json(fname_menus, menus)
    #readCSV()
```







## Str



### raw string

```\
r''
```



### utf-8

```
>>> text = "お誕生日おめでとう"
>>> text.encode("utf-8")
b'\xe3\x81\x8a\xe8\xaa\x95\xe7\x94\x9f\xe6\x97\xa5\xe3\x81\x8a\xe3\x82\x81\xe3\x81\xa7\xe3\x81\xa8\xe3\x81\x86'
>>> text.encode("utf-8").decode("utf-8")
```





### byte string

```
echodict\pandora\src\pandora\exts\token.py
__public_key = b'-----BEGIN PUBLIC KEY-----\n' \
               b'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA27rOErDOPvPc3mOADYtQ\n' \
               b'BeenQm5NS5VHVaoO/Zmgsf1M0Wa/2WgLm9jX65Ru/K8Az2f4MOdpBxxLL686ZS+K\n' \
               b'7eJC/oOnrxCRzFYBqQbYo+JMeqNkrCn34yed4XkX4ttoHi7MwCEpVfb05Qf/ZAmN\n' \
               b'I1XjecFYTyZQFrd9LjkX6lr05zY6aM/+MCBNeBWp35pLLKhiq9AieB1wbDPcGnqx\n' \
               b'lXuU/bLgIyqUltqLkr9JHsf/2T4VrXXNyNeQyBq5wjYlRkpBQDDDNOcdGpx1buRr\n' \
               b'Z2hFyYuXDRrMcR6BQGC0ur9hI5obRYlchDFhlb0ElsJ2bshDDGRk5k3doHqbhj2I\n' \
               b'gQIDAQAB\n' \
               b'-----END PUBLIC KEY-----'
```





### format

For Python 3.+, the same behavior can also be achieved with [`format`](https://docs.python.org/3/library/stdtypes.html#str.format):

```py
number = 1
print("{:02d}".format(number))
```

------

For Python 3.6+ the same behavior can be achieved with [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings):

```py
number = 1
print(f"{number:02d}")
```





irt [u](https://github.com/17zuoye/pyirt/blob/master/tests/test_model_wrapper.py)

```python
print ("\r", "train [{}] loss: {:.3f}, Perplexity: {:.3f}, teach: {:.3f}      ".format(total_steps + step + 1, loss_sum, np.exp(loss_sum), now_tf), end=" ")

```



```python
c = [0.5, 0, 0, 0, 0.5, 0, 0, 0, 0.5]

guess_param = {}
for t in range(T):
    guess_param['q%d' % t] = c[t]
--> {'q0': 0.5, 'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0.5, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 0.5}
```

```python
print(f"{name} is {age} years old")
print (item, end=" ")
```

```
ax.text(n[0], n[1], n[2], "法向量" + r"$=\left({:.2f},{:.2f},{:.2f}\right)^{:s}$".format(g[0], g[1], -1, T), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
doc\lang\programming\python\深入理解神经网络：从逻辑回归到CNN\neural_network-neural_network_code-master\neural_network_code\画图脚本
```

```python
print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
```

```python
print("Total probability of survival for all passengers --> {:.4f}".format(dataframe.Survived.mean()))
```

```python
print(u'输出路径：%s.npy' % data_extract_npy)
```



#### 彩色输出

```
pip3 install rich

    generated_text = Text(generated_text, style="green")
    print(Panel(generated_text, width=120, title="Reply"))
```



#### 代码格式化

```
import textwrap

# /usr/local/lib/python3.10/dist-packages/gradio/cli/commands/components/_create_utils.py

 readme_contents = textwrap.dedent(


```







### moment



```
if 'You have sent too many messages to the model' in err:
                match = re.search(r"clears_in':\s*([\d]+)", err)
                if match:
                    seconds = int(match.group(1))
                    clears_time = str( arrow.now('+08:00').shift(seconds=seconds) )

                    choice = int(sys.argv[-1])
                    account = accounts[choice-1]
                    account["clears_in"] = seconds
                    account["clears_time"] = clears_time
                    
                    # choice the account that has lessest clears_time
                    choice_new = -1
                    seconds_new = -1
                    min_time = arrow.get(clears_time)

                    for i in range(1, len(accounts)+1):
                        if i == choice:
                            continue
                        account = accounts[i-1]
                        t = account['clears_time']  # 未来时间, 过了这个时间就可用
                        if t:
                           t1 = arrow.get(t)
                           diff = t1.timestamp() - arrow.now('+08:00').timestamp() # 和现在相差多少秒
                           diff = int(diff+0.5)
                           if t1.__lt__(min_time):
                                min_time = t1
                                choice_new = i
                                if diff >= 0:
                                    seconds_new = diff
                                elif diff < 0:
                                    seconds_new = 0
                        else:
                           choice_new = i
                           seconds_new = 0
                           break

                    if choice_new == -1 and seconds_new == -1:
                        print(f'##### Attention: sleepping {math.ceil(seconds / 60)} minute now...')
                        time.sleep(seconds)
                    elif choice_new != -1 and seconds_new == 0:
                        # switch account, and go on
                        print(f'##### Attention: switch account: { accounts[choice_new-1]["username"] }, and go on...')
                        sys.argv[-1] = str(choice_new)
                    elif choice_new != -1 and seconds_new > 0:
                        sys.argv[-1] = str(choice_new)
                        print(f'##### Attention: switch account: { accounts[choice_new-1]["username"] }, and sleepping {math.ceil(seconds_new / 60)} minute now...')
                        time.sleep(seconds_new)
                    else:
                        raise Exception('unkonw err1.')

                else:
                    raise Exception('unkonw err2.')
            elif 'list models failed: internal server error' in err:
                print(f'##### Error: {err} sleeping 15 minute and try again...')
                time.sleep(15*60)
            else:
                print(f'##### Waring: sleeping 3.5 hour now.')
                time.sleep(3600*3.5)
```





```
# pip install moment

moment.now().add(seconds=3600)
	# 加一小时
	
# pip install -U arrow

arrow.now().__eq__(arrow.now())
	# 两个时间是否相等

arrow.now().shift(seconds=3600).__ge__(arrow.now())
	# lt 是小于

arrow.now().shift(seconds=1).timestamp() - arrow.now().timestamp()
	# 相差多少秒

arw.shift(weeks=+3)
	# hours minutes

https://arrow.readthedocs.io/en/latest/guide.html


https://github.com/arrow-py/arrow/blob/master/arrow/arrow.py#L1762-L1767
 # comparisons

    def __eq__(self, other: Any) -> bool:

        if not isinstance(other, (Arrow, dt_datetime)):
            return False

        return self._datetime == self._get_datetime(other)

    def __ne__(self, other: Any) -> bool:

        if not isinstance(other, (Arrow, dt_datetime)):
            return True

        return not self.__eq__(other)

    def __gt__(self, other: Any) -> bool:

        if not isinstance(other, (Arrow, dt_datetime)):
            return NotImplemented

        return self._datetime > self._get_datetime(other)

    def __ge__(self, other: Any) -> bool:

        if not isinstance(other, (Arrow, dt_datetime)):
            return NotImplemented

        return self._datetime >= self._get_datetime(other)

    def __lt__(self, other: Any) -> bool:

        if not isinstance(other, (Arrow, dt_datetime)):
            return NotImplemented

        return self._datetime < self._get_datetime(other)

    def __le__(self, other: Any) -> bool:

        if not isinstance(other, (Arrow, dt_datetime)):
            return NotImplemented

        return self._datetime <= self._get_datetime(other)

```





### in 是否包含

```
        if 'train' in self.data_list[0]:
            self.is_training = True
```



```
if gpu_info.find('failed') >= 0:
  print('Not connected to a GPU')
```



### split string into list of characters

```
list(str)
```



### strip



```python
line.strip().split('\t')

lstrip()
	# 只删左边空白
    
.strip(": ")
	# ?

```





### remove whitespace

```python
re.sub(r"\s+", "", astr, flags=re.UNICODE)
```



### remove not chinese

```python
def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)
```



```python
# 移除非中文、26个英文字母以外的字符
def unAZchinese_remove(s):
   return re.sub(r"[^\u4e00-\u9fa5^a-z^A-Z^0-9]", "", s, flags=re.UNICODE)
```





```python
class mydict(dict):
      def __str__(self):  # how to convert to string
          return json.dumps(self)
```



```python
要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
```



### jieba



#### 自定义词典

1、加载自定义字典jieba.load_userdict()
参数filename：为文件类对象或自定义词典的路径
词典格式分为3个部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。
file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。

2、从字典中添加或删除词汇add_word、del_word
add_word(word,freq=None,tag=None)，add_word有3个参数，添加词名称，词频，词性
del_word(word)，del_word只有一个参数词语名称

3、词频调整suggest_freq
suggest_freq（segment,tune=True）
调节单个词语的词频，可以使其能（或不能）被分出来，词频越高在分词时，能够被分出来的概率越大。



```python
import jieba

#载入自定义词典
jieba.load_userdict('word_dict.txt')

#查看用户自定义词典中的内容
print(jieba.user_word_tag_tab)

#往自定义词典中添加新词
jieba.add_word('人民广场',freq=5,tag='n')

#添加新词后的结果
print(jieba.user_word_tag_tab)

string='上海市浦东新区世纪大道100号楼501'
text_cut=jieba.cut(string)
print(" ".join(text_cut))

#调整词频，重新分词
jieba.suggest_freq(('上海市','浦东新区'),tune=True)
text_cut=jieba.cut(string)
print(" ".join(text_cut))
```



- 用法： `jieba.load_userdict(file_name)` # file_name为自定义词典的路径
- 词典格式和`dict.txt`一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开

示例

```text
宜信普惠 7
宜信 10
极速模式 20
```



```python
同样的问题，比如：
jieba.add_word("弗里德里克·泰勒",freq=888888); jieba.add_word("冯·诺伊曼",freq=888888); jieba.suggest_freq(('弗里德里克·泰勒', '冯·诺伊曼'), True); txt = "这个外国人叫弗里德里克·泰勒，是美国前国防部部长。冯·诺伊曼是公认的计算机发明人"; print(" | ".join(jieba.cut(txt, HMM=True, cut_all=False)))
结果还是：
'这个 | 外国人 | 叫 | 弗里德里克 | · | 泰勒 | ， | 是 | 美国 | 前 | 国防部 | 部长 | 。 | 冯 | · | 诺伊曼 | 是 | 公认 | 的 | 计算机 | 发明人'
大家有什么好办法？

代码里面有如下的正则表达式，用来提取中文

re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&._%]+)", re.U)
也就是说对于”弗里德里克·泰勒”中的“·”不认为是中文，而是作为类似逗号和句号来处理。

一个不太好但是可以用的办法就是，修改上面的正则表达式，将“·”加入。其中\xb7就是“·”。

re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&.\xb7%]+)", re.U)

测试结果：
》 这个 | 外国人 | 叫 | 弗里德里克·泰勒 | ， | 是 | 美国 | 前 | 国防部 | 部长 | 。 | 冯·诺伊曼 | 是 | 公认 | 的 | 计算机 | 发明人

```



## Class



### 继承和静态方法

```python
# https://zhuanlan.zhihu.com/p/29887184
# GitHub\doc\lang\programming\项目反应理论\irt_zhihu.py
class BaseIrt(object):

    def __init__(self, scores=None):
        self.scores = scores

    @staticmethod
    def p(z):
        # 回答正确的概率函数
        e = np.exp(z)
        p = e / (1.0 + e)
        return p

    def _lik(self, p_val):
        # 似然函数
        scores = self.scores
        loglik_val = np.dot(np.log(p_val + 1e-200), scores.transpose()) + \
                     np.dot(np.log(1 - p_val + 1e-200), (1 - scores).transpose())
        return np.exp(loglik_val)

    def _get_theta_dis(self, p_val, weights):
        # 计算theta的分布人数
        scores = self.scores
        lik_wt = self._lik(p_val) * weights
        # 归一化
        lik_wt_sum = np.sum(lik_wt, axis=0)
        _temp = lik_wt / lik_wt_sum
        # theta的人数分布
        full_dis = np.sum(_temp, axis=1)
        # theta下回答正确的人数分布
        right_dis = np.dot(_temp, scores)
        full_dis.shape = full_dis.shape[0], 1
        # 对数似然值
        print(np.sum(np.log(lik_wt_sum)))
        return full_dis, right_dis
```



### 属性

```python
class EAPIrt2PLModel(object):

    def __init__(self, score, slop, threshold, model=Irt2PL):
        self.x_nodes, self.x_weights = model.get_gh_point(21)
        z = model.z(slop, threshold, self.x_nodes)
        p = model.p(z)
        self.lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1)

    @property
    def g(self):
        x = self.x_nodes[:, 0]
        weight = self.x_weights[:, 0]
        return np.sum(x * weight * self.lik_values)

    @property
    def h(self):
        weight = self.x_weights[:, 0]
        return np.sum(weight * self.lik_values)

    @property
    def res(self):
        return round(self.g / self.h, 3)
# https://zhuanlan.zhihu.com/p/29887184
```







## Range



def listToDict(lst):
    op = { i: lst[i] for i in range(0, len(lst), 1)}
    return op



## String Template

new in Python 3
```python
print(f"{name} is {age} years old")
print (item, end=" ")
```




## Filter

[filter](https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000)

接受的函数是一参，函数返回True 就保留元素，否则丢弃

```python
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
list(filter(lambda w: not bool(re.match(r'[^\u4e00-\u9fa5]', w)), words)) # 过滤非中文词
{k: v for k, v in points.items() if v[0] < 5 and v[1] < 5}
```

- filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list



### 去除 list 中的空串

```python
# 去除 list 中的空串
sentences = list(filter(None, sentences)) 
```





## Regex

https://zhuanlan.zhihu.com/p/42944600

bool(re.match(r'\s+', '  '))   # 是否含空白符

提取中文部分

```python
print(re.compile(r'\d+\s+(.+?)\s+').sub(r'\1', '1 跨膜  ') )  
	# 只取第一个分组 r'\1'
print(re.findall(r"\d+\s+(.+?)\s+", "0 跨膜激活物、钙调节物、亲环蛋白配体相互作用物   1  1"))
	# findall 得到的结果是数组，不如前一种方法好用

```



### 非捕获分组 (?:)

[u](https://blog.csdn.net/okyoung188/article/details/53407021)

```
pattern = re.compile('[A-Z](?:、[A-Z])+')
print( pattern.findall('SDAFQ、W、D、W、D、W二个人个、D') )
```







### 不是特定字符



```python
r'@*?([1-9][0-9]*\.[^0-9a-zA-Z].+?)\n' # . 后面不能出现特定字符
```









### 提取

```python
print( re.compile('([一二三四五六七八九十]+)').search('三四五').group(1) )
```

```python
# python 3.8 新特性
if match := re.compile('([一二三四五六七八九十]+)').search('三四五'):  
	print( match.group(1) )
```





### compile

```python
pattern = re.compile(r'\[.+?\.gif\]') # .+? 最短匹配
print( pattern.findall('β[XB3.gif]肾上腺素受体激动剂\xa0') )
```





### .匹配换行

```
re.DOTALL
```





### ? 最短匹配

```
ss =  re.findall(r'(@@第[一二三四五六七八九十]+章.+?)\n', strs, re.DOTALL)
```



### ^ not ^ at the begin



[^】]*?  不是字符】，重复0或多次，最短匹配

^ 是“在开始”，如果放在最前面

$ 是“在结尾”，如果放在最后面



```
print( re.compile(r'(【[^】]*?)(【[^】]*?】)([^【]*?】)(.*?\n)').sub(ps2[1][1], "【大剂量】常出现在【血清地高辛浓度【＞2ng/ml】】时，\n") )
```





```python
[^a-z]
So to match a string that does not contain "y", the regex is: ^[^y]*$

Character by character explanation:

^ means "beginning" if it comes at the start of the regex. Similarly, $ means "end" if it comes at the end. [abAB] matches any character within, or a range. For example, match any hex character (upper or lower case): [a-fA-F0-9]

* means 0 or more of the previous expression. As the first character inside [], ^ has a different meaning: it means "not". So [^a-fA-F0-9] matches any non-hex character.

When you put a pattern between ^ and $, you force the regex to match the string exactly (nothing before or after the pattern). Combine all these facts:

^[^y]*$ means string that is exactly 0 or more characters that are not 'y'. (To do something more interesting, you could check for non-numbers: ^[^0-9]$
```







### 捕获



捕获和非捕获属性 https://blog.csdn.net/Leonard_wang/article/details/79813425





### finditer 所有匹配的开始结束位置 

```
iters = re.finditer(r'[ab]', "abc", re.DOTALL)
poss =  [ i.span() for i in iters ]
```



```
ss =  re.findall(r'(@@第[一二三四五六七八九十]+章.+?)\n', strs, re.DOTALL)
iters = re.finditer(r'(@@第[一二三四五六七八九十]+章.+?)\n', strs, re.DOTALL)
poss =  [ i.span() for i in iters ]
for pos in poss:
    (start, end) = pos
    print(start, end)
    print (strs[start:end])
```



```
# 输入字符串，标题正则
# 返回标题、标题位置(strat, end), 标题下的文本
def extractPattern(strs, reg):
    #ss =  re.findall(reg, strs, re.DOTALL)
    iters = re.finditer(reg, strs, re.DOTALL)
    poss =  [ i.span() for i in iters ] # 标题positions
    rs = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        title = strs[start:end]
        contents = None
        if i == ( len(poss) - 1 ):
            contents = strs[ end : len(strs) ]
        else:
            contents = strs[ end : poss[i+1][0] ]
        rs.append( [ start, end, title, contents ] )

    return rs
```



### replace



```python
s = "     1  0.D【解析】阿托品阻断M受体，交感神经相对亢奋，进而影响窦房结和房室结"
pattern = re.compile('(\d+)\s+?(\d)')
print( pattern.sub(r'\1\2', s) )
```





```python
ps_text_summary.replace("【】","")
```



两层括号展平

```
print( re.compile(r'(【[^】]*?)(【[^】]*?】)([^【]*?】)(.*?\n)').sub(r'\1】\2【\3\4', "【a【b】c】d\n") )
-> 【a】【b】【c】d
```



```

notlr = r"([^【^】]*?)" # 非左非右，最短匹配

left = r'(【[^】]*?)'
midle = r'(【[^】]*?】)'
right = r'([^【]*?】)'
end = r'(.*?\n)'

# 注意依赖顺序，注释掉前面后面就可能不正确
# not perfect but can use
ps2 = [
        (r'(【[^】]*?)(【[^】]*?)(【[^】]*?】)([^【]*?】)([^【]*?】)(.*?\n)', r'\1】\2】\3【\4【\5\6'),  # 先把三个括号的展平了
        (r'(【[^】]*?)(【[^】]*?】)([^【]*?】)(.*?\n)', r'\1】\2【\3\4'),                                # 再把两个括号的展平
        ( left + midle + notlr + midle + right + notlr + end, r'\1】\2\3\4【\5\6\7' ),                   # 处理多层嵌套 "【a【b】c【d】e】f\n"
        (r"(【)(【[^】]*?】)(.+?)(】)(.*?)(\n)", r"\1】\2【\3】【\4【\5】\6"),
        (left+midle+notlr+midle+notlr+midle+right+notlr+end, r'\1】\2【\3】\4【\5】\6【\7【\8】\9'),
        (left+midle+notlr+midle+notlr+midle+notlr+midle+right+notlr+end, r'\1】\2【\3】\4【\5】\6【\7】\8【\9【\10】\11')
    ]
```









```
echo 'the blue dog and blue cat wore blue hats' | sed 's/blue \(dog\|cat\)/gray \1/g'
->the gray dog and gray cat wore blue hats
```



## 空白符

```
re.sub(r'[ \t\r\f\v]', '', s) # 空格、制表符、回车符、换页符和垂直制表符
	# 去掉除换行以外的所有空白符
```





#### named groups



```
p = re.compile(r'blue (?P<animal>dog|cat)')
p.sub(r'gray \g<animal>','the blue dog and blue cat wore blue hats')
```



```
re.sub(
    pattern=r'(\d)(\w+)', 
    repl='word: \\2, digit: \\1', 
    string='1asdf'
)
```



```
p.sub('gray \g<1>',s)
```



```python
print ( re.sub(
    pattern=r'【【(【.+?】)】】(.*?)\n', 
    repl=r'\1\2', 
    string='【【【aa】】】bb【【【cc】】】dd【【ee】【ff】】\n'
) )
-> 【aa】bb【【【cc】】】dd【【ee】【ff】】

print ( re.sub(
    pattern=r'(【【(【.+?】)】】)(.*?)(\n)', 
    repl=r'\1\4\2\4\3', 
    string='【【【aa】】】bb【【【cc】】】dd【【ee】【ff】】\n'
) )
大外层是1 内层是2 其他是3
```



```
match = re.match(r"(?P<all>(?:-(?P<one>\w+))*)","-ab-cde-fghi-jkl-mn")
>>> re.findall(r"-(?P<one>\w+)", match.group("all"))
['ab', 'cde', 'fghi', 'jkl', 'mn']
```





```
re.match(r"(?:aaa)(_bbb)", string1).group(1)
result = re.sub(r"(\d.*?)\s(\d.*?)", r"\1 \2", string1)
```





```
pattern = re.compile(r'\[.+?\.gif\]') # .+? 最短匹配
print( pattern.findall('β[XB3.gif]肾上腺素受体激动剂\xa0') )
print( pattern.sub('', 'β[XB3.gif]肾上腺素受体激动剂\xa0') )  #替换成空串
```



```
ps= [
        ( r'\[.+?\.gif\]', "" ),  # pattern 和需要替换成为的串
    ]
"""
需要替换的pattern
"""

# 递归批量替换字符串
def replaceall(strs, ps, idx):
    if strs.strip() == "":
        return ""
    if (idx > len(ps) - 1):
        return strs.strip()

    (p, s) = ps[idx]
    pattern = re.compile(p)
    strs = pattern.sub(s, strs)
    return replaceall(strs, ps, idx + 1)
```



### split



```python
# 对文本进行分句
def splitSentences(text):
    sents = re.split(u'[\n。*+@+]', text) # 以句号或换行符作为分句标准
    sents = [sent for sent in sents if len(sent) > 0]  # 去除只包含\n或空白符的句子
    return sents
```





### subString

```
str = ’0123456789′
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取，具体啥意思没搞明白？
```



### escape

re. escape( )



### book_2_json



```python
import math
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname( os.path.dirname(os.path.abspath(__file__)))))  # std 包在此模块的上上上级目录
sys.path.append( os.path.dirname(os.path.abspath(__file__) ) )

import re
import util.fectchData as fectchData
import util.seg as seg
import util.saveTempData as saveTempData
import std.iSql as iSql
import std.seg.iSeg as iSeg
import std.iList as iList
import std.iJson as iJson
import std.iFile as iFile
import std.iTextrank as iTextrank

from joblib import Parallel, delayed
import itertools


regs = [
        r'(@@第[一二三四五六七八九十]+章.+?)\n',
        r'(@@第[一二三四五六七八九十]+节.+?)\n',
        r'@@[一二三四五六七八九十]+、.+?\n',
        r'@@（[一二三四五六七八九十]+）.+?\n',
        r'@@[1-9]+.+?\n'
    ]


# 输入字符串，标题正则
# 返回标题、标题位置(strat, end), 标题下的文本
def extractPattern(strs, regs, idx):
    #ss =  re.findall(reg, strs, re.DOTALL)
    iters = re.finditer(regs[idx], strs, re.DOTALL)
    poss =  [ i.span() for i in iters ] # 标题positions
    rs = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        title = strs[start:end]
        contents = None
        if i == ( len(poss) - 1 ):
            contents = strs[ end : len(strs) ]
        else:
            contents = strs[ end : poss[i+1][0] ]
        rs.append( [ start, end, title, contents ] )

    return rs

def walks(arr, regs, idx):
    if idx >= len(regs) or len(arr) <= 0:
        return

    for l in arr:
        strs = l[3]
        rs = extractPattern(strs, regs, idx)
        if len(rs) > 0:
            l[3] = rs
            walks(l[3], regs, idx+1)
        else:
            walks([l], regs, idx+1)

        #print(rs)


if __name__ == "__main__":
    
    currDir = os.path.dirname(os.path.abspath(__file__))

    fname_book = os.path.join(currDir, '药二20200617.txt')
    fname_results = os.path.join(currDir, 'results.json')
    

    book = iFile.readfile_line_by_line(fname_book)
    strs = "\n".join(book)
    
    print( len(strs), '@@第十六章' in strs )


    rs = extractPattern(strs, regs, 0)
    #iJson.save_json(fname_results, rs)
    #print(rs)

    walks(rs, regs, 1)
    iJson.save_json(fname_results, rs)
    #print(rs[0])


"""
https://zhuanlan.zhihu.com/p/42944600
"""
```





## Sort

```python
sorted(trank_res, key=lambda x: x['index'], reverse=False)
```



## 随机数



```
random.random()
用来随机生成一个0到1之间的浮点数，包括零。

In [1]: import random

In [2]: random.random()
Out[2]: 0.15790797219589303
randint(a, b)
用来生成[a,b]之间的随意整数，包括两个边界值。

In [12]: import random

In [13]: random.randint(1,6)
Out[13]: 1
random.uniform(a,b)
用来生成[a,b]之间的随意浮点数，包括两个边界值。

In [14]: import random

In [15]: random.uniform(1,6)
Out[15]: 5.497873150216069
choice(seq)
从一个非空序列选出随机一个元素。seq泛指list，tuple，字符串等

In [16]: import random

In [17]: List = [1,2,3,4,5,6]
In [18]: random.choice(List)
Out[18]: 1
randrange(start, stop[, step = 1])
这个就是random和range函数的合二为一了。但注意，range用法有变。

In [27]: import random

In [28]: random.randrange(1,6)
Out[28]: 3
random.shuffle(x[,random])
正如函数名所表示的意思，shuffle，洗牌，将一个列表中的元素打乱。

In [36]: import random

In [37]: List = [1,2,3,4,5,6]
In [38]: random.shuffle(List)
In [39]: print(List)
[2, 1, 6, 4, 5, 3]
random.sample(sequence,k)
sample，样品，从有序列表中选k个作为一个片段返回。

In [41]: import random

In [42]: List = [1,2,3,4,5,6]
In [43]: random.sample(List,3)
Out[43]: [4, 6, 3]
random.seed ( [x] )
x:改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。使用同一个种子，每次生成的随机数序列都是相同的。

In [48]: import random

In [49]: random.seed(10)
In [50]: print("Random number with seed 10: ", random.random())
Random number with seed 10:  0.5714025946899135

In [51]: random.seed(10)
In [52]: print("Random number with seed 10: ", random.random())
Random number with seed 10:  0.5714025946899135

In [53]: random.seed(10)
In [54]: print("Random number with seed 10: ", random.random())
Random number with seed 10:  0.5714025946899135
关于随机数种子，请参考：Python下探究随机数的产生原理和算法
```





## Numpy



```python
x = x_nodes[:, 0] # 行全要,列只要第0列.结果是二维变一维
# (11,1) -> (11,)
```



### numpy base64 互转

```python
see huggingface\rwkv_numpy\rwkv.py
    x = emb_weight[token]
    b64 = base64.b64encode(x)
    bytes = base64.decodebytes(b64)
    x__ = np.frombuffer(bytes, dtype=np.float32)


# numpy base64 互转
import base64
import numpy as np

t = np.arange(25, dtype=np.float64)
s = base64.b64encode(t)
r = base64.decodebytes(s)
q = np.frombuffer(r, dtype=np.float64)

print(np.allclose(q, t))
# True
```





### 维度不同的减法

```python
"""
两个1*2 减一个1*2
(2*2) - (1*2) = ( (1*2) - (1*2),
                  (1*2) - (1*2)
                )
= (2*2)
"""
a = np.array(
    [
        [-0.51632716, -0.51632716],
        [-0.56524826, -0.56524826]
    ])

b = np.array(
    [
        [-0.1491838, 2.63128067]
    ])

c = a - b
print(c)
"""
shoud be:
[[-0.36714335 -3.14760782]
 [-0.41606446 -3.19652893]]
"""
```



a, b 的列数相同，a行更多，**按列来减**



### 维度不同的乘法



```python
(2,) * (11,1) -> (11,2)
# (2,) 表示一维，两个元素
	# 2个0有序对，11个1有序对，11个2有序对

(11,2) + (2,) -> (11,2)
```



```python
x = x_nodes[:, 0] # 行全要,列只要第0列.结果是二维变一维
# (11,1) -> (11,)
```



#### 乘方

```python
# 按列乘方
array([[2, 2],
       [2, 2]])
>>> b=np.array(b)
>>> b
array([0, 1])
>>> a**b
array([[1, 2],
       [1, 2]], dtype=int32)
"""
    tmp1 = p**score
    tmp2 = (1.0 - p)**(1-score)

    lik_values = np.prod(tmp1*tmp2, axis=1)
"""
```





### 类型转换



```python
# doc\lang\programming\pytorch\李宏毅2020机器翻译\iAttention.py

a = np.array([1, 2], dtype=np.float32)
np.asarray(a, dtype=np.float32) is a
True
np.asarray(a, dtype=np.float64) is a
False

issubclass(np.recarray, np.ndarray)
True
a = np.array([(1.0, 2), (3.0, 4)], dtype='f4,i4').view(np.recarray)
np.asarray(a) is a
False
np.asanyarray(a) is a
True
```

```
# 填充物
class LabelTransform(object):
  def __init__(self, size, pad):
    self.size = size
    self.pad = pad

  def __call__(self, label):
    label = np.pad(label, (0, (self.size - label.shape[0])), mode='constant', constant_values=self.pad)
    return label
    
transform = LabelTransform(max_output_len, word2int_en['<PAD>'])


 # 用 <PAD> 將句子補到相同長度
 en, cn = transform(en), transform(cn)  # 就是在list 后面填0
 en, cn = torch.LongTensor(en), torch.LongTensor(cn)
	# en, cn 是list[int]，int 表示单词的唯一编号

```





### 小数变成它最接近的整数

```
# [-1, 1] 的小数规范到[0, 255]
import cv2
a = ((images[0].numpy().squeeze() + 1) / 2) * 255
b = np.rint(a) # 小数变成它最接近的整数
plt.imshow(b, cmap='gray_r')
b
```





### 取样

```python
# 模拟参数
a = np.random.uniform(1, 3, 1000)  # 均匀分布
b = np.random.normal(0, 1, size=1000)
z = Irt2PL.z(a, b, 1)
p = Irt2PL.p(z)
score = np.random.binomial(1, p, 1000)
# D:\workcode\algo\项目反应理论\irt_zhihu.py
```



### 均方误差

```python
print('mse: {}'.format(np.mean((val - real_diff) ** 2)))
```

```python
print(np.mean(np.abs(est_slop - a[0]))) # 平均误差
```



### 计算所有元素的乘积



```python
np.prod([...]) # 不指定轴，则不管是几维都展平成一维然后连乘
np.prod([...], axis=1) # 按行连乘(维度变成??)
np.prod([...], axis=0) # 按列连乘
```





### shape

```python
print (inputs.dtype, inputs.shape, expected_output.shape)
```



### Initialize

```python
np.array([[2, 4, 6], [6, 8, 10]], np.int32)
np.zeros((3, 3))
np.ones((8, 1))
np.full(shape, fill_value, dtype=None, order='C')
np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
```



### reshape

```
a1 = x.reshape(x.shape[0], 1) # Getting the training example as a column vector.
```

```python
# 一维变二维
sc = simScores[:, i]  # 取一列
sc.reshape(sc.shape[0],-1)
```





#### flatten

```
ndarray.flatten(order='C') # c by row; f by column
```



```
np.squeeze  # 也是起到降维的作用
```





#### tile 复制列

```python
true_theta = np.random.normal(loc=0, scale=1, size=(n_persons,1))   # 5个人的能力 (5*1)
true_theta = np.tile(true_theta, n_questions)                       # 5个人每道题的能力都一样，列复制5次 (5*1) -> (5*5)
true_beta = np.random.normal(loc=0, scale=1, size=(1,n_questions))  # 5个问题的难度 (1*5)
```



#### 取第一列

```python
a[:,0]
```







### transpose

```
numpy.ndarray.T
.T is just np.transpose() 
# If the matrix has less than 2 dimensions it returns the original. 
```



### matrix op

```
np.dot(W, TR) * 0.85 + C
```



### append

```python
np.append(0, (radii*np.cos(angles)).flatten())
```



### matrix show



```
import numpy as np
import matplotlib.pyplot as plt

v = np.array([[1.5, -1.5, 2.7]]).T
plt.matshow(v, cmap=plt.cm.hot)
plt.show()
```





### loadtext

```
f = 'lsat.csv'
score = np.loadtxt(f, delimiter=",")
```



### universal function

```
ufunc是universal function的缩写，意思是这些函数能够作用于narray对象的每一个元素上，而不是针对narray对象操作，numpy提供了大量的ufunc的函数。
```



### 归一化数据集



```python
def scaleData(dataMat):
    max = dataMat[:,0].max()
    min = dataMat[:,0].min()
    dataMat[:,0] = (dataMat[:,0] - min) / (max - min)
    return dataMat
```

> Max 为所有数据中最大的值，min 为所有数据中最小的值，对每个数据减去最小值然后除以最大值和最小值的差，从而进行归一化，**使得每一个数据在 0 到 1 范围内**。



### 概率分布



```
"""
概率编程语言入门指南

有偏差的掷硬币(a biased coin toss)

随机函数被叫做模型，表达模型的方法，和正常的Python方法没有区别
模型（model）和变分分布（guide）的参数。【注：所谓变分就是将原始函数换作另一（易处理的）函数的数学技巧】
最大化证据（evidence）  证据下限”ELBO（evidence lower bound）


https://colab.research.google.com/drive/1SZDm5ppWBFIpowO8KIATfoYZXEVbuVGr#scrollTo=tdhST1QE8MuX

Fitting a Distribution with Pyro: Part 2 - Beta
https://www.richard-stanton.com/2020/05/03/fit-dist-with-pyro_2.html


A Gentle Introduction to Probabilistic Programming Languages
https://medium.com/swlh/a-gentle-introduction-to-probabilistic-programming-languages-bf1e19042ab6
"""
answers = np.random.binomial(size=(n_persons, n_questions), p=likelihood, n=1) # calculate answers based on theta and likelihood function
```



np.random.binomial(size=(n_persons, n_questions), p=likelihood, n=1)

> size 和 p 的维度相同
>
> **二项分布，值为1 的概率由p 给出**



### 阶乘



```python
import numpy as np

# n 选k 的组合数
def C(n, k):
    return np.math.factorial(n) / ( np.math.factorial(k) * np.math.factorial(n - k) )

```





### assert_equal

```python
# test if samples are 0 or 1
sm = rm.sample().flatten()
assert_equal(np.all((sm == 0) | (sm == 1)),True)
```



## JAX



```
import numpy as np
q = np.arange(-5, 5)
q[q < 0] = 0
print(q)
# [0 0 0 0 0 0 1 2 3 4]

import jax.numpy as jnp
q = jnp.arange(-5, 5)
q = q.at[q < 0].set(0)  # NB: this does not modify the original array,
                        # but rather returns a modified copy.
print(q)
# [0 0 0 0 0 0 1 2 3 4]
```



```
# https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html
```





### Pytrees数据结构

[Pytrees数据结构](https://zhuanlan.zhihu.com/p/477870275)



Examples

```
>>> import jax.tree_util
>>> jax.tree_util.tree_map(lambda x: x + 1, {"x": 7, "y": 42})
{'x': 8, 'y': 43}
```



If multiple inputs are passed, the structure of the tree is taken from the first input; subsequent inputs need only have `tree` as a prefix:

```
>>> jax.tree_util.tree_map(lambda x, y: [x] + y, [5, 6], [[7, 9], [1, 2]])
[[5, 7, 9], [6, 1, 2]]
```



#### 自定义pytrees

[自定义pytrees](https://github.com/google/jax/issues/12319)

```python
from jax.tree_util import register_pytree_node_class
import jax.numpy as jnp
from jax.experimental import checkify
import jax

@register_pytree_node_class
class Boxes:
  def __init__(self, arr: jnp.ndarray):
    self.arr = arr
    assert arr.ndim > 1 and arr.shape[-1] == 4
  
  def area(self) -> jnp.ndarray:
    return (self.arr[..., 2] - self.arr[..., 0]) * (self.arr[..., 3] - self.arr[..., 1])

  def tree_flatten(self):
    return ((self.arr,), None)
  
  @classmethod
  def tree_unflatten(cls, _, children):
    return cls(children[0])

def func(x: Boxes):
  return x.area() + 3

jax.vmap(func)(Boxes(jnp.ones((2, 2, 4))))
```



### jax大规模并行计算

[Tensor Model Parallelism - xmap vs pjit](https://github.com/google/jax/discussions/11444)

[colab demo](https://colab.research.google.com/github/kingoflolz/mesh-transformer-jax/blob/master/colab_demo.ipynb#scrollTo=8CMw_dSQKfhT)

[打印ShapedArray](https://github.com/google/jax/issues/196 )

[一文彻底搞懂jax.vmap的使用](https://zhuanlan.zhihu.com/p/476098317)

[How to vmap over a batch of trees or dictionaries](https://github.com/google/jax/issues/7430)

```
import jax.numpy as jnp 
from jax import vmap

def f(x, params):
  return params['a']*x + params['b']

vmap(f, in_axes=(0, 0))(jnp.array([2, 2]), {'a': jnp.array([3, 3]), 'b': jnp.array([4, 4])})
```





```

in_axes=({0: 'left'}, {1: 'right'}) 做的事情类似这样：
	# 对第一个输入 每次取一行元素，对第二个输入 每次取一列元素，
	# 然后传函数给函数的形参

对矩阵第0轴索引，切出n个“行向量”，由于矩阵是3x2的，共计有3个行向量，切片shape为(2, )
# 对axes=0 索引：
for i in range(x.shape[0]):
    print(x[i,:])
    
    
  
```





```
# pip install jax==0.4.4
	# windows这样装
# github/segment/jax_pytrees.py
# https://jax.readthedocs.io/en/latest/notebooks/xmap_tutorial.html  需要仔细看的文档
# https://github.com/google/jax/issues/196  打印 ShapedArray
import jax
import jax.numpy as np
import jax.numpy as jnp
from typing import Any, Callable
from typing import Dict
from jax.experimental.maps import xmap
from jax import vmap, vjp, jvp
from jax.tree_util import Partial as partial
from jax.experimental.host_callback import call

"""
a={{1},{2}};a//MatrixForm
b= { {1, 2} }; b // MatrixForm
a.b // MatrixForm
c = { {1,3},{2,4} }; c//MatrixForm
c\[Transpose] // MatrixForm
c.c\[Transpose]//MatrixForm
"""
def dot(a, b):
  jax.debug.print("a={x} b={y}", x=a, y=b)  # require jax > 0.3.16
  return jnp.vdot(a, b)

# 向量内积实现矩阵乘
# x = jnp.arange(10).reshape((2, 5))
x = jnp.array( [ [1, 3], 
                 [2, 4]] )

x_T = jnp.array( [ [1, 2], 
                   [3, 4]] )

r = xmap(dot,
  in_axes=({0: 'left'}, {1: 'right'}),
  out_axes=['left', 'right', ...])(x, x_T) # x.T

```





### xmap 单机并行 map

[Named axes and easy-to-revise parallelism with xmap](https://jax.readthedocs.io/en/latest/notebooks/xmap_tutorial.html)

```\
jax.xmap is a function from the JAX library that applies a given function to each element of an iterable object in parallel. You should use it if you are using JAX and have computations that can be done in parallel, such as training a model on multiple GPUs.
```



### pmap 多机并行map

[通过pmap轻松实现数据并行](https://basicv8vc.github.io/posts/jax-tutorials-for-pytorchers-3/#pmapjaxlaxp-%e5%9c%a8%e5%8d%95%e6%9c%ba%e5%a4%9a%e5%8d%a1%e4%b8%8a%e8%bd%bb%e6%9d%be%e5%ae%9e%e7%8e%b0%e6%95%b0%e6%8d%ae%e5%b9%b6%e8%a1%8c)



### Apply pmap to a list of pytrees

[官方文档](https://jax.readthedocs.io/en/latest/_autosummary/jax.pmap.html)

[Apply pmap to a list of pytrees](https://github.com/google/jax/issues/2540)

[pmap on pytree (namedtuple) with various dimensions](https://github.com/google/jax/issues/3102)



### JAX-MD近邻表计算

[JAX-MD近邻表计算](https://www.cnblogs.com/dechinphy/p/jaxnb1.html)



### Hamming Distance计算

[Hamming Distance计算](https://www.cnblogs.com/dechinphy/p/jax-numpy.html)



### 计时器

```
# timer 被构造的时侯计时一次，被释放的时侯计时一次

# pip install git+https://github.com/deepmind/dm-haiku
import contextlib
import time
from typing import NamedTuple

import chex
import haiku as hk
import jax
import jax.numpy as jnp
import numpy as np
from absl import app, logging

@contextlib.contextmanager
def timer(name: str):
    begin = time.time_ns()
    try:
        yield begin
    finally:
        logging.info(f'Timer {name}[ms] {(time.time_ns() - begin) / int(1e6)}')
        
        
    with timer('pmap()'):
        v, p = p_update(params, Input(x + 0.1, a, b), lr)
        new_x = select(v, p).block_until_ready()

    with timer('jit(vmap())'):
        v, p = jv_update(params, Input(x + 0.1, a, b), lr)
        new_x = select(v, p).block_until_ready()
```





## CuPy



```python
>>> import cupy as cp
>>> x = cp.arange(6).reshape(2, 3).astype('f')
>>> x
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.]], dtype=float32)
>>> x.sum(axis=1)
array([  3.,  12.], dtype=float32)
```



```
前提：传统的数组和矩阵都是通过numpy来设定，然后numpy来调用cpu计算！
cupy的作用：数组和矩阵都是通过cupy来设定，然后cupy来调用gpu并行计算！

区别与联系：

区别：numpy自动调用cpu来进行"数组和矩阵间"的计算，计算任务默认单进程；cupy自动调用gpu来进行"数组和矩阵间"的计算，gpu中默认并行计算！
联系：二者的函数和实操的功能基本完全一样，一般只需把np.xxx()改成cp.xxx()即可。当然，cupy还未完全写完，有些numpy的函数它还未实现（基本用不到）。
cupy的优势：专门进行大型、高维数组/矩阵的快速计算（非常非常快）！
要想实现数组/矩阵的快速运算，要注意3点：

数组/矩阵的维度、尺寸一定要够大，计算量够大才行，否则gpu的初始化都耗的时间比计算时间都长！总之：计算量一定要够大，最好矢量化编程；
数组/矩阵间的运算，比如矩阵相加、相乘、点乘等，一定要直接使用cupy自带的函数（如加法：cupy.add(x1,x2)）！不要直接写一个：+ 运算符！即：能用自带函数就尽量用自带函数！
一定避免cpu和gpu混合编程：比如在一个循环计算中，每一步循环中的计算量不大，但是又有cpu计算（比如加减乘除赋值等），又用gpu矩阵计算。此时用cupy反而会降低运算效率！因为"cpu和gpu之间的切换、数据互通等一系列初始化非常耗时"（相比计算任务来说）！
下面用一个很简单的例子即可体现上面的内容：循环矩阵相加

import cupy as cp
import numpy as np
import time

# 高维矩阵/数组：
gpu = cp.ones( (1024,512,4,4) )
cpu = np.ones( (1024,512,4,4) )

# 纯numpy的cpu测试：
ctime1 = time.time()
for c in range(1024):
    cpu = np.add(cpu,cpu)   # 这里用np.add()和直接用 + 一样！内核都是cpu来算
ctime2 = time.time()
ctotal = ctime2 - ctime1
print('纯cpu计算时间：', ctotal)

# 纯cupy的gpu测试：
gtime1 = time.time()
for g in range(1024):
    gpu = cp.add(gpu,gpu)   # 自带的加法函数
gtime2 = time.time()
gtotal = gtime2 - gtime1
print('纯gpu计算时间：', gtotal)

# gpu和cpu混合编程：
ggtime1 = time.time()
for g in range(1024):
    gpu = gpu + gpu         # 手工加法：+ 默认回到cpu计算！！！
ggtime2 = time.time()
ggtotal = ggtime2 - ggtime1
print('混合的计算时间：', ggtotal)
三组循环矩阵相加的耗时结果：

纯cpu计算时间： 43.857738733291626
纯gpu计算时间： 0.02496480941772461
混合的计算时间： 1.4730699062347412
彼此差距非常明显！上文中需要注意的2、3点非常非常重要！
由本例也可看出，cupy的gpu并行计算潜力有多大！
本例的计算量还是太小，一个GTX-1050的笔记本显卡，都根本还没发挥其功力！如果将cupy应用到服务器上、应用到深度学习之中，潜力非常大！


```



## numba

- https://github.com/numba/numba





## Pytorch



#### TENSOR VIEWS



- views 是已存在张量的一个视图，内部共享同一份数据，但是可以有不同的维度，相当于一个子空间
- views 得到的结果是：元素的总数不变，对维度有全新的解释

```python
# handwritten_digit_recognition_GPU.ipynb
criterion = nn.NLLLoss()
images, labels = next(iter(trainloader))
images = images.view(images.shape[0], -1)
```



```python
# 强制copy data，不共享内存
c = t.contiguous()
t.is_contiguous()

# 是否是同一块数据
t.storage().data_ptr() == b.storage().data_ptr()

```







## System



### OS Type



```python
    OS = ''
    try:
      test = os.uname()
      if test[0] == "Linux":
        OS = "Linux"
      elif test[0] == 'Darwin':
        OS = "OSX"
    except Exception as e:
      OS = "Windows"

    root = r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    if OS == "Linux":
      root = r"/mnt/videos/anime/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    if OS == "OSX":
      #root = r"/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
      root = r"/Users/olnymyself/Downloads/d"
# D:\workcode\python\std\iEncoding.py
```



### Dir

```
names = os.listdir(root)
```





```
currDir = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'cache', str(appid) )   

    if not os.path.exists( currDir ):
        os.makedirs( currDir )
        RELOADQ = True
    else:
        RELOADQ = False
```



```
# removing directory
import shutil
shutil.rmtree(path)
```





### basename



```
# basename without extention
from pathlib import Path
Path('/root/dir/sub/file.ext').stem

```





### stdout

```
sys.stdout.flush() # Updating the text.
sys.stdout.write("\rIteration: {} and {}".format(i + 1, j + 1))
```



### 子进程



```python

see huggingface/myvideo/readme.txt
    /root/miniforge3/envs/gradiomyvideo/lib/python3.10/site-packages/gradio/cli/commands/components/dev.py
    line 51 下断点
    component_directory = component_directory.resolve()
        # 成功断下

import subprocess

node = '/usr/local/node-v20.11.1-linux-x64/bin/node'

gradio_node_path = '/root/miniforge3/envs/gradiomyvideo/lib/python3.10/site-packages/gradio/node/dev/files/index.js'

component_directory = '/root/huggingface/myvideo'

gradio_template_path = '/root/miniforge3/envs/gradiomyvideo/lib/python3.10/site-packages/gradio/templates/frontend'

app = 'demo/app.py'

host = 'localhost'

python_path = '/root/miniforge3/envs/gradiomyvideo/bin/python3'

gradio_path = '/root/miniforge3/envs/gradiomyvideo/bin/gradio'

    proc = subprocess.Popen(
        [
            node,
            gradio_node_path,
            "--component-directory",
            component_directory,
            "--root",
            gradio_template_path,
            "--app",
            str(app),
            "--mode",
            "dev",
            "--host",
            host,
            "--python-path",
            python_path,
            "--gradio-path",
            gradio_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    while True:
        proc.poll()
        text = proc.stdout.readline()  # type: ignore
        err = None
        if proc.stderr:
            err = proc.stderr.readline()

        text = (
            text.decode("utf-8")
            .replace("Changes detected in:", "[orange3]Changed detected in:[/]")
            .replace("Watching:", "[orange3]Watching:[/]")
            .replace("Running on local URL", "[orange3]Backend Server[/]")
        )

        if "[orange3]Watching:[/]" in text:
            text += f"'{str(component_directory / 'frontend').strip()}',"
        if "To create a public link" in text:
            continue
        print(text)
        if err:
            print(err.decode("utf-8"))

        if proc.returncode is not None:
            print("Backend server failed to launch. Exiting.")
            return


```







```python
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p06_executing_external_command_and_get_its_output.html
import subprocess
out_bytes = subprocess.check_output([r"C:\Program Files\R\R-4.0.3\bin\x64\Rscript.exe", r"C:\Program Files\R\R-4.0.3\bin\x64\op.R"])
out_text = out_bytes.decode('utf-8')


see  huggingface gradio/issues/1637/run.py
    cmd = f"ffprobe -i {input_video} -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1"
    out_bytes = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    total_time = float( out_bytes.decode('utf-8').strip() )

```

```R
`op` <-
function(x){
  y <- list(name=x)
  y
}

o <- op(1)
class(o)
```



### time

```python
import datetime
now = datetime.datetime.now()
print now.year, now.month, now.day, now.hour, now.minute, now.second
# 2015 5 6 8 53 40
```







## Multiprocessing 



Python 界有条不成文的准则： 计算密集型任务适合多进程，IO 密集型任务适合多线程

> 通常来说多线程相对于多进程有优势，因为创建一个进程开销比较大，然而因为在 python 中有 GIL 这把大锁的存在，导致执行计算密集型任务时多线程实际只能是单线程。而且由于线程之间切换的开销导致多线程往往比实际的单线程还要慢，所以在 python 中计算密集型任务通常使用多进程，因为各个进程有各自独立的 GIL，互不干扰。
>
> 而在 IO 密集型任务中，CPU 时常处于等待状态，操作系统需要频繁与外界环境进行交互，如读写文件，在网络间通信等。在这期间 GIL 会被释放，因而就可以使用真正的多线程。



[进程池的同步与异步用法Pool](https://blog.csdn.net/aaronthon/article/details/83422749)

```python
print(os.cpu_count())
from multiprocessing import cpu_count
print(cpu_count)
```

```
from joblib import Parallel, delayed
return Parallel(n_jobs=os.cpu_count(), verbose=10)(delayed(f)(ts, i) for i in range(len(ts)-1))  # 子循环多核并发执行，加速运算
```



## 分布式共享内存

- https://xijiz.github.io/post/naive-python-2-berkeley-ray.html
- Python + Memcached：分布式应用中的高效缓存

```
Berkeley Ray（以下简称Ray）是一个以大规模机器学习为目标的高性能分布式计算框架。Ray通过抽象系统状态到一个全局控制存储区和保持其它所有的组件无状态来实现可扩展性和容错能力。在数据调度方面，Ray使用了分布式共享内存存储来高效地处理大规模数据，它也使用了一个从下到上的层次化调度架构去实现低延迟和高吞吐。Ray也有着基于动态任务图的轻量级接口，可以灵活地应用到各种应用上。
```







## JSON



### dict、list和string 互转  



```python
import json
import decimal
import datetime
import numpy as np


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        elif isinstance(o, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):

            return int(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json 
def parse(s):
    return json.loads(s, strict=False )

# convert dict to string
def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)
```





```python
# encoding=utf-8
import jieba
from __future__ import unicode_literals
import json
#import jsons
import pymysql
import decimal
import datetime

test_to_save_file = "test_from_mysql.json"
segs_test_file = "segs_test_from_mysql.json"

material_file = "5.json"  # 教材json
stopword_file = "stopwords.dat"

dic = {}

def jiba_segs(text):
    return list(jieba.cut(text,cut_all=False))

def listToDict(lst):
    op = { i: lst[i] for i in range(0, len(lst), 1)}
    return op

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

#按行读取文件，返回文件的行字符串列表
def read_file(file_name):
    fp = open(file_name, "r", encoding="utf-8")
    content_lines = fp.readlines()
    fp.close()
    #去除行末的换行符，否则会在停用词匹配的过程中产生干扰
    for i in range(len(content_lines)):
        content_lines[i] = content_lines[i].rstrip("\n")
    return content_lines

# 读停用词列表
stopwords = read_file(stopword_file)

with open(material_file, encoding='utf-8') as fh:
    js = json.load(fh)
    fh.close()

def word_frequency(seg_list):
    for w in seg_list:
        if (w not in stopwords) and (w in dic):
            dic[w] = dic[w] + 1
        elif w not in stopwords:
             dic[w] = 1
            
    # if dic.has_key():

    
    
def walk(j):
    if type(j) is list:
        if j == []:
            return
        for d in j:  # j is list, and list only has dicts
                if d["key"] != "" and d["key"] != "TEST111":
                    key = d["key"]
                    segs_key = list(jieba.cut(key,cut_all=False))
                    word_frequency(segs_key)
                    print (key, '----->', '|'.join( segs_key ) )
                if d["context"] != "" and d["context"] != "null": 
                    context = d["context"]
                    segs_context = list(jieba.cut(context,use_paddle=True))
                    print (context, '----->',  '|'.join( segs_context ) )
                walk(d['childs'])
    if type(j) is dict:
        if j["key"] != "" and j["key"] != "TEST111":
                print (j["key"])
        return walk(j['childs']) 

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
walk(js)
print (dic)


def conn():
    mydb=pymysql.Connect(host='',
                         port=3306,
                         user='',
                         password='',
                         db='',
                         charset='utf8', 
                         autocommit=True)
    return mydb.cursor(pymysql.cursors.DictCursor)

def db_exe(query,c):
    try:
        if c.connection:
            print("connection exists")
            c.execute(query)
            return c.fetchall()
        else:
            print("trying to reconnect")
            c=conn()
    except Exception as e:
        return str(e)

dbc=conn()

result_dics_list = load_json(test_to_save_file)
result_dics = listToDict(result_dics_list)

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

# 题目分词

new_seg_lst = []
for dic in result_dics_list:
    
    testjson = json.loads( dic["TestJson"], strict=False )
    
    if testjson["Type"] == 'ATEST':
        testjson["Title_segs"] = jiba_segs(testjson["Title"])
        for item in testjson["SelectedItems"]:
            item["Content_segs"] = jiba_segs(item["Content"])
        dic["TestJson"] = testjson


save_json(segs_test_file, result_dics_list)

print (result_dics_list[-1])

if dbc:
    if dbc.connection:
        try: 
            dbc.connection.close()
            print ('### db close success.')
        except Exception as e:
             print ( str(e) )
        
print (dbc.connection)



```





## UTF-8



```python
import sys
import os

# Version 1.0
# 需要配合 EBWin4 使用，词典分组需要设置好


def output(o):
    fullstr = '<meta charset="utf-8">'
    for l in o:
        fullstr += l
    # print(fullstr)
    sys.stdout.buffer.write(fullstr.encode('utf-8'))


s = sys.argv[1].strip()
# s = "organon"

result = os.popen(
    '"C:\Program Files (x86)\EBWin4\ebwinc.exe" /G=KL /C=1 /O=h ' + s).readlines()
output(result)
```



```
如果用的是 Windows 系统的话，可以参考我的帖子： [GoldenDict] GoldenDict 的下载、安装、使用[Windows] https://www.pdawiki.com/forum/fo ... hread&tid=14072# p( C0 a6 ]% n1 ~; r
几个关键点：6 s6 H1 L; [% E% E
1. 官网下载的GoldenDict 是不支持 EPWING 格式的，要从 http://sourceforge.net/projects/ ... %20access%20builds/ 这里下载最新版；% K% e- e% ?, t) ^) Y
2. 把 EPWING 词典文件放在 content 文件夹下；9 _: E; O" Z5 p) M/ `* }
3. 第一次打开 GoldenDict 时，迅速地前往【编辑】->【首选项】->【全文搜索】，关闭“全文搜索”（也就是如果有勾的话，就是把前面的勾去掉）！！！9 p/ N# O/ q: M3 t( e9 X
4. GoldenDict 对 EPWING 支持有些小问题的。
5. 关于单独字体指定，参考：[GoldenDict] 如何为某部词典指定字体？ https://www.pdawiki.com/forum/fo ... hread&tid=15900
```





```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import networkx as nx
import numpy as np
import math
import re
import os
import sys
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())  # python3的系统编码
print(sys.stdout.encoding)       # 标准输出的编码


adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)
G = nx.from_numpy_matrix(adjMat)
nx.draw(G, with_labels = True)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels = nx.get_edge_attributes(G,'weight'))
```





```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

import re
import jieba
import jieba.analyse
import jieba.posseg as pseg

def is_alpha(tok):
    try:
        return tok.encode('ascii').isalpha()
    except UnicodeEncodeError:
        return False


text = u'影响酶促反应速度的因素1.酶浓度 <br>2.底物浓度 <br>3.温度<br>4.酸碱度 <br>5.激活剂<br>6.抑制剂'

p2 = re.compile(ur'[^\u4e00-\u9fa5]') #中文的编码范围是：\u4e00到\u9fa5  
zh = " ".join(p2.split(text)).strip()                    
zh = "|".join(zh.split())  

# print zh

# text = [w for w in text if not is_alpha(w)]

print zh

'''

seg_list = jieba.cut(text, cut_all=True)
seg_list_tolist = list(seg_list)

# for w in seg_list_tolist:
    # print w


seg_list = jieba.cut(text, cut_all=True)
print("Full Mode: " + "|".join(seg_list))  # 全模式


for x, w in jieba.analyse.extract_tags(text, withWeight=True):
    print('%s %s %s' % (x, w, is_alpha(x)))

'''



#text = [w for w in text]


'''
if True:
    text = [w for w in text if not is_alpha(w)]
'''



'''
item = pseg.cut(text)
for i in list(item):
  print i.word


open('stopword.txt').readlines()

stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines() ]
'''

# print list(stop)



```



```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
# Convert ShiftJIS to UTF-8
# Usage: cat ShiftJIS.txt | ./convert.py > UTF8.txt
# Alternative method: cat ShiftJIS.txt | iconv -f shift_jis -t utf8 > UTF8.txt
 
import sys
import codecs
 
ustdout = codecs.getwriter('utf_8')(sys.stdout)
jstdin = codecs.getreader('shift_jis')(sys.stdin)
 
for line in jstdin.readlines():
ustdout.write(line)


cat 学研国語大辞典ku00.txt | iconv -f SHIFT_JIS-2004 -t utf-8 > 学研国語大辞典ku00-utf8.txt
```





## Jupyter Notebook



```python
@echo off
cd /d D:
cd %cd%
jupyter notebook
cmd.exe
```





```python
python -m pip install --upgrade pip
pip install wheel
```



pip install jupyter

- pip install --user jupyter  出错就用这个



python -m jupyter notebook --version

```
python -m pip install -U matplotlib
pip install seaborn
pip install sklearn
pip install scikit-image
```



Ctrl + Shift + P -> Python: Select interpreter

Ctrl + Shift + P -> Python: Select interpreter to start Jupyter server

Python: Select interpreter to start Jupyter server



**Ctrl+Shift+P** -> **Python: Create New Blank Jupyter Notebook**

> 注意大小写都要正确





### 不用print 打印



#### **其他技巧**

**1. 不用print即可输出多个变量**

比如下面一段代码

```text
a, b = 1, 2
a
b
```

运行结果只会展示`b`的值，如果要同时展示`a b`的值，需要使用`print`，如下所示

```text
a, b = 1, 2
print(a)
print(b)
```

如果希望不需要`print`即可同时输出`a b`的值，则可以先运行下面这两行代码，则之后在这个笔记本中执行代码都不需要`print`

```text
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

如果不喜欢这个配置，要改回来只需要

```text
InteractiveShell.ast_node_interactivity = "last"
```



题外话：如果想直接打变量名不输出，只需要在后面加一个`;`，这个在`plt.hist()`的使用中比较有用。

**2. 默认执行代码**

本节分为两个部分：修改默认配置，默认执行代码。

像上一节的`print`配置，如果希望对所有notebook都适用，不用每次都重新指定，可以在配置文件中修改。只需要在`~/.ipython/profile_default/ipython_config.py`文件中添加

```text
c = get_config()
c.InteractiveShell.ast_node_interactivity = "all"
```

保存后重新打开notebook会发现这些配置自动生效。

（如果该路径下没有这个文件则创建一个，用这条命令`ipython profile create`）

配置这个文件的另一个功能是执行默认代码，即有一些代码希望在每一个notebook都默认执行时，可以像这样写入配置文件

```text
c.InteractiveShellApp.exec_lines = [
 'import sys; sys.path.append("C:\\Miniconda3\\Lib\\site-packages")',
 'import matplotlib.pyplot as plt; %matplotlib inline'
]
```

**3. 将ipynb文件转化为py文件**

文本内容全部变成注释

```text
ipython nbconvert --to python abc.ipynb
```

另一种方式：在notebook页面菜单中选择 `File-->Download as-->py`





## networkx plot graph



## 看权重和结点的图形


```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import networkx as nx
import numpy as np
import math
import re
import os
import sys
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())  # python3的系统编码
print(sys.stdout.encoding)       # 标准输出的编码


"""
此代码用于测试算法正确性
"""

adjacentMatrix = np.zeros((3, 3))
"""
	邻接矩阵 里面存的是相似度，相似度就是graph 中的边的权值
"""

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)

G = nx.from_numpy_matrix(adjMat)
# pos=nx.get_node_attributes(G,'pos')
pos = nx.spring_layout(G)
nx.draw(G, with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)

scores = nx.pagerank(G, **{'alpha': 0.85, })

print ( type(adjacentMatrix), type(adjMat) )
print (adjacentMatrix)
print (adjMat)
print (nx_graph)
print (scores)


```



## 看权重和结点的文本输出

```python
import networkx as nx
import numpy as np

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)
G = nx.from_numpy_matrix(adjMat)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
```

> {(0, 1): Text(0.36720620499242296, -0.46714047438761563, 
>
> "{'weight': 0.4}"), (0, 2): Text(-0.4999999999999998, 0.1325001701718984,
>
> "{'weight': 0.2}"), (1, 2): Text(0.13279379500757726, 0.3346403042157172, "{'weight': 0.1}")}







## Win10提升管理权限删除顽固文件

进入C:\Windows\System32文件夹下

找到cmd.exe 文件

右键-以管理员身份运行（重要）

输入：net user administrator /active:yes，开启超级管理员账号

win+r键打开运行对话框，输入 netplwiz ，重设administrator密码

重启-开始→切换账户→Administrator,就可以切换到管理员模式了。

重启后，屏幕上显示一个是本地用户、一个是administrator用户，这样可以来回切换。这样你找到要删除的文件或者文件夹就可以删除了

如果上面方法解决不了，试试下面这个---------电脑的安全模式。

点击开始，再点击设置，然后在设置页面点击“更新和安全“这一选项，再在左方的选项里面点击”恢复“，接着
在右边找到”高级启动“，并点击下方的”立即重新启动“，电脑将会重启进入高级启动，再点击“疑难解答”，
接着“高级选项”，再点击“启动设置”，最后店家右下方的“重启”，电脑将再次重启，并出现一个选择
界面，在选择里面找到“启用安全模式”并，按照提示点击相应的按键。就能进入安全模式了。
点击开始，再点击设置，然后在设置页面点击“更新和安全“这一选项，再在左方的选项里面点击”恢复“，接着
在右边找到”高级启动“，并点击下方的”立即重新启动“，电脑将会重启进入高级启动，再点击“疑难解答”，
接着“高级选项”，再点击“启动设置”，最后店家右下方的“重启”，电脑将再次重启，并出现一个选择
界面，在选择里面找到“启用安全模式”并，按照提示点击相应的按键。就能进入安全模式了。





## 完全卸载VSCode



> **注意**：以下步骤需要在执行 `VSCode` 自带卸载程序之后执行。

- `win + r` 打开运行
- %appdata% 回车
- 删除 `Code` 和 `Visual Studio Code` 文件夹
- 地址栏输入 %userprofile% 回车
- 删除 `.vscode` 文件夹



### 错误提示和格式化

Python 默认的语法提示工具是 PyLint，也可以选择其他的 linter 工具，比如 flake8。flake8 是 Python 官方发布的一款静态代码检查工具，如果想使用它的话首先在 Anaconda 的命令行工具中用 `pip install flake8` 安装；另外，在保存代码的时候 VSCode 可以自动进行 code formatting ，这个功能默认是关闭的且工具是 autopep8 , 如果想使用 yafp，则继续在命令行工具中用命令 `pip install yapf` 安装。 安装好这两个工具之后在 VSCode 的配置文件中进行设置：

```text
"python.linting.enabled": true
"python.linting.flake8Enabled": true,
"python.formatting.provider": "yapf"
```





## networkx plot graph



## 看权重和结点的图形


```python
# encoding=utf-8
# 使用 coding: utf-8 设置中文编码只在 Python 3 有效
import networkx as nx
import numpy as np
import math
import re
import os
import sys
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())  # python3的系统编码
print(sys.stdout.encoding)       # 标准输出的编码


"""
此代码用于测试算法正确性
"""

adjacentMatrix = np.zeros((3, 3))
"""
	邻接矩阵 里面存的是相似度，相似度就是graph 中的边的权值
"""

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)

G = nx.from_numpy_matrix(adjMat)
# pos=nx.get_node_attributes(G,'pos')
pos = nx.spring_layout(G)
nx.draw(G, with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)

scores = nx.pagerank(G, **{'alpha': 0.85, })

print ( type(adjacentMatrix), type(adjMat) )
print (adjacentMatrix)
print (adjMat)
print (nx_graph)
print (scores)


```



## 看权重和结点的文本输出

```python
import networkx as nx
import numpy as np

adjMat = np.array([[0, 0.4, 0.2], [0.4, 0, 0.1], [0.2, 0.1, 0]], np.float)
G = nx.from_numpy_matrix(adjMat)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
```

> {(0, 1): Text(0.36720620499242296, -0.46714047438761563, 
>
> "{'weight': 0.4}"),
>
> 
>
> (0, 2): Text(-0.4999999999999998, 0.1325001701718984,
>
> "{'weight': 0.2}"),
>
> 
>
> (1, 2): Text(0.13279379500757726, 0.3346403042157172, "{'weight': 0.1}")}



[

[0.  0.4 0.2],

[0.4 0. 0.1],

 [0.2 0.1 0. ]

]



https://reference.wolfram.com/language/GraphUtilities/ref/PageRanks.html

https://www.mathworks.com/help/textanalytics/ref/textrankscores.html

https://github.com/YevaGabrielyan/tldl





## Sublime Text 3

> Tools>Build System menu ->new build system
>
> 
>
> {
>
>   "shell_cmd": "node ${file}"
>
> }
>
> 
>
> build
>
>   command + b
>
> 
>
> module.paths.push('G:/Users/w7/AppData/Roaming/npm/node_modules');
>
> 
>
> {
>
> ​	"shell_cmd": "python3 -u ${file}"
>
> }



## Flask

```
https://github.com/greyli/bootstrap-flask
```





```
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085, debug=True)
```



```python
from flask import Flask, request, jsonify
import os,sys
sys.path.append(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))  # std 包在此模块的上级目录
import std.iJson as iJson

app = Flask(__name__)

# http://localhost:666/frequencyStatistics
# request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据
# request.json 的类型直接就是dict
@app.route('/frequencyStatistics', methods=['post'])
def frequencyStatistics():
    print(request.json, type(request.json))
    return jsonify(iJson.parse("[1,2,3]"))


```



### 异步

```python
https://zhuanlan.zhihu.com/p/30897711    
from flask import Flask
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/jobs')
def run_jobs():
    executor.submit(some_long_task1)
    executor.submit(some_long_task2, 'hello', 123)
    return 'Two jobs was launched in background!'


def some_long_task1():
    print("Task #1 started!")
    sleep(10)
    print("Task #1 is done!")


def some_long_task2(arg1, arg2):
    print("Task #2 started with args: %s %s!" % (arg1, arg2))
    sleep(5)
    print("Task #2 is done!")


if __name__ == '__main__':
    app.run()
```

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def task(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response

def download(futures):
    response = futures.result()  #会得到一个返回值，这个返回值就是task函数的返回值
    content = response.text
    tmp_list = response.url.split("/")
    filename = tmp_list[len(tmp_list)-1]
    print("正在下载：%s" %response.url)
    with open(filename,"w",encoding="utf-8") as f:
        f.write("%s\n%s" %(response.url,content))
        print("下载完成")

url_list = [
    "http://www.cnblogs.com/wupeiqi/articles/5713330.html",
    "http://blog.csdn.net/anzhsoft/article/details/19563091",
    "http://blog.csdn.net/anzhsoft/article/details/19570187"
]

thread_pool = ThreadPoolExecutor(max_workers=2) #生一个线程池对象，最大线程数为2个

for url in url_list:
    futures = thread_pool.submit(task,url)  #会得到一个Future对象
    #回调函数,会将futures本身当作参数传给download函数
    futures.add_done_callback(download)
```



### 模板

```
<html>
  <head>
    {% if title %}
    <title>{{title}} - microblog</title>
    {% else %}
    <title>microblog</title>
    {% endif %}
  </head>
  <body>
    <div>Microblog: <a href="/index">Home</a></div>
    <hr>
    {% block content %}{% endblock %}
  </body>
</html>
```



```
# 继承
{% extends "base.html" %}
{% block content %}
<h1>Hi, {{user.nickname}}!</h1>
{% for post in posts %}
<div><p>{{post.author.nickname}} says: <b>{{post.body}}</b></p></div>
{% endfor %}
{% endblock %}
```



```
# https://jinja.palletsprojects.com/en/2.11.x/templates/
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% else %}
    <li><em>no users found</em></li>
{% endfor %}
</ul>
```



#### 当作html 来渲染

```
# https://www.jianshu.com/p/765afe303bf8
# safe 是过滤器

	{% for r in enrows %}
        <br><br> {{ r[1] | safe }}  
    {% else %}
        no en......
    {% endfor %}
```



#### 继承



```
# base.html
<!doctype html>
    <head>
        {% if title %}
        <title>{{title}}</title>
        {% else %}
        <title>Default title</title>
        {% endif %}
    </head>
    
    <form action="/" method="post">
        keyword: <input type="text" name="keyword"><br>
        <select name="lang_select">
        <option value ="en">en</option>
        <option value ="jp">jp</option>
        </select>
        <button type="submit">Search</button>
    </form>

    {% block EnBlock %}{% endblock %}

```

```
# result.html
{% extends "base.html" %}
{% block EnBlock %}

{% for r in enrows %}
    <br><br> {{ r[1] | safe }}  
{% else %}
    {# no en...... #}
{% endfor %}

{% endblock %}


```

```
# templates.py

# https://www.jianshu.com/p/765afe303bf8

import subprocess
import re
import chardet

import MeCab
tagger = MeCab.Tagger()

from zhconv import convert


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlite3 as sqlite # Python 自带的

# from pymysql import escape_string  # pip install **pymysql==0.9.3** # 高版本没有escape_string
import glob

import json
import decimal
import datetime

# import xmltodict

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js


# out_bytes = subprocess.check_output([r"ffmpeg", "-i", "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv", "-map", "0:s:0", "out.srt"])
# out_text = out_bytes.decode('utf-8')

def readstring(fanme):
    with open(fanme, "r", encoding="utf-8") as fp:
        return fp.read()

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def chinese_remove(s):
    return re.sub(r"[\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def unjp_remove(s):
    return re.sub(r"[^\u0800-\u4e00]", "", s, flags=re.UNICODE)

def unhana_remove(s):
    return re.sub(r"[^\u3040-\u309F^\u30A0-\u30FF]", "", s, flags=re.UNICODE)

def jpQ(s):
    return len( unhana_remove(s) ) > 0

def chQ(s):
    return not jpQ(s) and len( chinese_remove(s) ) == 0
    

from flask import Flask, request, jsonify, redirect, render_template_string,session,Response,render_template


import datetime
import copy

from flask_cors import CORS, cross_origin
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


app.config['SECRET_KEY'] = 'STRONGSECRTKEY'

host = '111.229.53.195'
port1 = 5432
port2 = 54322

@app.route('/', methods=['get'])
@cross_origin(supports_credentials=True)
def default_get():

    #session['keyword'] = 'result'
    
    isEn = False
    isCh = False
    isJp = False

    if ('keyword' in session and len( session['keyword'].strip() ) > 0 ):
        keywd = session['keyword']
        keywd = keywd.strip()
        print(f'session is: {keywd}')
        
        if ( chQ(keywd)):
            #a = unhana_remove(keywd)
            print('### ch.')
            keywd = convert(keywd, 'zh-hant')
            isCh = True
        elif ( jpQ(keywd)):
            print('### jp.')
            isJp = True
        else:
            print('### en.')
            isEn = True


        with psycopg2.connect(database='studio', user='postgres', password='postgres',host=host, port=port1) as conn:
            with conn.cursor() as cur:

                sql = ""
                if (isEn):
                    print('### select en.')

                    sql = f"SELECT id, ts_headline(en, q) as en, zh, type \
                    FROM studio, to_tsquery('{keywd}')  q \
                    where en @@ to_tsquery('{keywd}') \
                    ORDER BY RANDOM() LIMIT 3; \
                    "

                    cur.execute(sql)
                    rows = cur.fetchall()

                    print('### rows num: %d' % len(rows))

                    return render_template('result.html', title='Welcom!', enrows=rows)
                    
    return render_template('result.html', title='Welcom!')
   
@app.route('/', methods=['post'])
@cross_origin(supports_credentials=True)
def default_post():
    keyword = request.values.get("keyword")
    print(f"keyword: {keyword}")
    select = request.values.get('lang_select')
    print(f"select: {select}")

    session['keyword'] = keyword
    session['select'] = select
    
    return redirect('/')


@app.route('/next', methods=['post'])
@cross_origin(supports_credentials=True)
def next():

    html = """
    <form action="/" method="post">
    keyword: <input type="text" name="keyword"><br>
    <option value ="en">en</option>
    <option value ="jp">jp</option>
    <button type="submit">Search</button>
    </form>
    """

    if 'keyword' in session and  session['keyword'].strip() != "":
        print('/next redirect.')
        return redirect('/')

    print('/next default page.')
    return render_template_string(html)


@app.route('/audio')
def stream_mp3():
    def generate():
        path = 't.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8085, debug=True)

```



### ftp



```python
@app.route('/iso', methods=['get'])
def stream_ISO():
    def generate():
        path = 'static/LaoMaoTao.iso'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    bytea = generate()
    return Response(bytea, mimetype="application/octet-stream")
```





## Post 



```python
import requests

# 设置API地址和密钥
api_url = "https://api.openai.com/v1/chat/completions"
api_key = "你的API密钥"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "告诉我关于streaming的更多信息。"}
    ],
    "stream": True  # 启用流式输出
}

response = requests.post(api_url, headers=headers, json=data, stream=True)

# 检查请求是否成功
if response.status_code == 200:
    # 逐行读取响应内容
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(f"Received Line: {decoded_line}")
else:
    print(f"请求失败: {response.status_code} - {response.text}")

```





```python
d = {"book":docText}
# d = {'book':'a'}
ret = requests.post(url="http://192.168.0.140:666/bookmenu", json=d, headers={'Content-Type':'application/json'}).json()

if ret['status'] == 200:
    data = ret["data"]
    iJson.save_json( 'post.json', data )
    pass
```





```python
def prowords(s, url="http://xxxxxxxxxx:6001/api/planckWord/splitAll"):

    re = requests.post(url="http://xxxxxx:6001/api/planckWord/splitAll", data={'array':"""[{"id":"1","context":"$"}]""".replace('$', s)}, headers={'Content-Type':'application/x-www-form-urlencoded'}).json()

    if re['status'] == 200:
        data = re['data']
        wls = data[0]['words']
        prowords = [ d['word'] for d in wls if d['type'] == 'pro' ]
        return prowords
    else:
        return []
```



```python
d = {"book":"\n@@第一章 执业药师与健康中国战略\n\n@@第二章 执业药师与健康中国战略\n"}
re = requests.post(url="http://192.168.0.140:666/bookmenu", json=d, headers={'Content-Type':'application/json'}).json()
```

```python
import requests
re = requests.post(url="http://192.168.0.140:6001/api/planckWord/splitAll", data={'array':"""[{"id":"1","context":"$"}]""".replace('$', '这里是内容')}, headers={'Content-Type':'application/x-www-form-urlencoded'}).json()
if re['status'] == 200
```





```python
# -*- coding: utf-8 -*-
from flask import request, jsonify, json, Module
import logging
from web.utils.consts import POST, GET
from web.db.dbSession import DBManager
from web.db.models import Class

NAMESPACE = 'student'
student = Module(__name__, NAMESPACE)


@student.route('/add', methods=[POST])
def student_add():
    # request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据：对应图1
    # json.loads(request.dada) 能够同时接受方法为POST、Body为 raw类型的 Text 
    # 或者 application/json类型的值：对应图1、2
    params = request.json if request.method == "POST" else request.args
    try:
        session = DBManager.get_session()
        c = Class(name=params['name'])
        session.add(c)
        session.commit()
        session.close()
    except Exception, e:
        logging.exception(e)
    return jsonify(code=200, status=0, message='ok', data={})

```



### 跨域

```python
"""
pip install flask-cors # 允许跨域
from flask_cors import CORS, cross_origin
CORS(app, supports_credentials=True) # 全局

@app.route('/')
@cross_origin(supports_credentials=True) # 单个接口
"""
```





### ajax

```javascript
ajax 前后向后台传递json 数据

contentType 默认值 "application/x-www-form-urlencoded" 适合于大多数请求json text xml 等都会自动进行解析；

contentType为application/json 适用于 向后台传递json字符串 ， 此时data 里面需要用 JSON.stringify()进行序列化，将其转为json形式的字符串。传递到后台！

<!DOCTYPE html>
<html>

<head>
<script type="text/javascript" src="jquery-3.5.1.min.js"></script>
<script>
    function loadDoc() {
        a = 1
        var data = {"book":"a"};
        $.ajax({
            url:"http://192.168.0.140:666/bookmenu",
            type:"post",
            data:JSON.stringify(data),
            contentType:"application/json", 
            dataType: "string", //返回的数据格式string
            success:function (result) {
                // 请求成功
            },
            error:function (XMLHttpRequest, textStatus, errorThrown) {
                // 很可能是参数错误
                re = JSON.parse(XMLHttpRequest.responseText)
                console.log(re)
            }
        });
    }
</script> 
</head>

<body>   

<div id="demo">
  <h2>Let AJAX change this text</h2>
  <button type="button" onclick="loadDoc()">Change Content</button>
</div>

</body>


</html>

```



### aria2



```
通过不断优化参数，最终最优的命令为：aria2c -j 10 -i test_url.csv -s 1 -q，其中-j 10表示10个进程同时下载，-i test_url.csv表示从文件中逐行读取URL进行下载，-s 1表示单个线程(主要是由于文件小，如果大文件则选用多线程会更快)，-q表示静默模式(不会逐行打印下载信息，节约时间)。

```

```
 https://github.com/aria2/aria2/
 Aria2 for Chrome
 https://github.com/dlxj/fake115
```







## Mysql



## trick



```
def weights_replaceinto(ls):
    sqls = []
    for d in ls:
        columns = ",".join( list(d.keys()) )
        values = ",".join( ( map(lambda w: r"'" + w + r"'" ,list(d.values()) ) ) )
        sqls.append(f"INSERT INTO weights ({columns}) VALUES({values}) ON DUPLICATE KEY UPDATE updateTime=now();")
```

```
# decimal 类型转换
cast(s.DifficultyScore as signed) AS '正确率'
```





### Insert into



```
f"INSERT INTO trialexampointrelevanttest (examPointID, appID, testID, childTestID, isMachine, similarity ) VALUES ({examPointID}, {appID}, {testID}, {childTestID}, 1, {similarity} ) ON DUPLICATE KEY UPDATE similarity={similarity}, updateTime=now();"

```



### pytorch tricks

- https://github.com/demuxin/pytorch_tricks



## pymysql




### debug


```python
    q = iSql.db88(db="temp")
    for sql in sqls:
        try:
            q.query(sql)
        except Exception as e:
            print(sql)
            print(str(e))
            q.close()
            raise RuntimeError('some err')
    q.close()
```



### 连接池



```python
import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=2,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=2,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=1,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    # 如：0 = None = never,
    # 1 = default = whenever it is requested,
    # 2 = when a cursor is created,
    # 4 = when a query is executed,
    # 7 = always
    host='xxxxxxx',
    port=3306,
    user='xxxxx',
    password='xxxxx',
    database='xxxxxx',
    charset='utf8'
)

conn = POOL.connection()
cursor = conn.cursor(pymysql.cursors.DictCursor)

if __name__ == '__main__':

    # 用户第一次答题的记录，计算IRT 试题难度

    cursor.execute("SELECT COUNT(*) FROM testds ts WHERE ts.KsbAppID = %s;", [1202])
    result = cursor.fetchone()

    
    cursor.execute("SELECT DISTINCT t.testID, t.childTestID  FROM  trialexampointrelevanttest t WHERE appid = %s ORDER BY t.testID;", [8911])
    result = cursor.fetchall() # 21451 题

    testID = result[0]['testID']
    childTestID = result[0]['childTestID']

    #cursor.execute("SELECT appID, allTestID, userID, childTableID, ReplyIsError FROM person_report.reply ry WHERE appID = %s AND allTestID = %s AND childTableID = %s;", [1202, testID, childTestID])
    #result = cursor.fetchall()     

    conn.close()
    cursor.close()
```























## Matplotlib



### 显示GIF 



```python
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_tight_layout(True)

print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))
line, = ax.plot(x, x - 5, 'r-', linewidth=2)

def update(i):
    label = 'timestep {0}'.format(i)
    line.set_ydata(x - 5 + i)
    ax.set_xlabel(label)
    return line, ax
anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=200)
anim.save('line.gif', dpi=80)
from IPython.display import HTML
HTML('<img src="line.gif">')
```



### 线性变换

```
# https://dododas.github.io/linear-algebra-with-python/posts/16-12-29-2d-transformations.html
```





### 绘图的重要参考

#### 深入理解神经网络：从逻辑回归到CNN.md

GitHub\doc\lang\programming\深入理解神经网络：从逻辑回归到CNN.md



[readthedocs.io matplotlib](https://mlhowto.readthedocs.io/en/latest/matplot.html)

[mtri.Triangulation](https://matplotlib.org/3.1.1/api/tri_api.html)

[Numpy中Meshgrid函数介绍及2种应用场景](https://zhuanlan.zhihu.com/p/29663486)



#### 记得调用plt.show() 秀图

````
plt.show()
````

普通的 .py 文件这样出来的图是可以3d 旋转的



### 显示灰度图



```python
# handwritten_digit_recognition_GPU.ipynb
dataiter = iter(trainloader)
images, labels = dataiter.next()  # images [64, 1, 28, 28]，64 张，1 通道，28 宽，28 高 的图片  # labels [64] 64个标签
plt.imshow(images[0].numpy().squeeze(), cmap='gray_r');  # squeeze 将 [1, 28, 28] 降维成 [28, 28]
```



```python
figure = plt.figure()
num_of_images = 60
for index in range(1, num_of_images + 1):
    plt.subplot(6, 10, index)  # 绘制  6 行，10 列 个对象
    plt.axis('off')            # 关闭坐标轴显示
    plt.imshow(images[index].numpy().squeeze(), cmap='gray_r')
```





### 绘制平面



```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')
ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# 生成等间距的n 个数的list, 包含尾端的数
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x1 = [-1.5  1.5]
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x2 = [-1.5  1.5]
x1, x2 = np.meshgrid(x1, x2)  # x1 作为行复制两次（行数是len(x2)），返回这个新矩阵
                              # x2 作为列复制两次（列数是len(x1)），返回这个新矩阵

"""
两个新矩阵是：

 [[-1.5  1.5]
 [-1.5  1.5]] 

 [[-1.5 -1.5]
 [ 1.5  1.5]]
 
 两个矩阵叠在一起，就是网格
 
 (-1.5, -1.5) (1.5, -1.5)
 (-1.5,  1.5) (1.5,  1.5)
 
"""
print(x1, "\n\n",x2)

x1, x2 = x1.flatten(), x2.flatten()  # 网格子矩阵flatten 后就可以传给plot_trisurf 绘制平面
ax.plot_trisurf(x1, x2, [ -2,-2,-2,-2], antialiased=True, alpha=LIGHT_ALPHA, color="black")
```

<img src="Python 3  Summary.assets/image-20200812093025409.png" alt="image-20200812093025409" style="zoom:50%;" />



### 绘制散点

```python
ax.scatter(x1, x2, [ -2,-2,-2,-2], c=[ -2,-2,-2,-2], cmap='viridis', linewidth=0.5)
```

<img src="Python 3  Summary.assets/image-20200812095330608.png" alt="image-20200812095330608" style="zoom:50%;" />

### 平面四个角的高度

#### 高度指定的顺序是：从左到右，从下到上

> [左下，右下，左上，右上]



<img src="Python 3  Summary.assets/image-20200812101606934.png" alt="image-20200812101606934" style="zoom:50%;" />



```python
ax.plot_trisurf(x1, x2, [ -2,0,-2,-2], antialiased=True, alpha=LIGHT_ALPHA, color="black")
ax.scatter(x1, x2, [ -2,0,-2,-2], c=[ -2,-2,-2,-2], cmap='viridis', linewidth=0.5)
```

<img src="Python 3  Summary.assets/image-20200812101505894.png" alt="image-20200812101505894" style="zoom:50%;" />



```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')
ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x1 = [-1.5  1.5]
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)  # x2 = [-1.5  1.5]
x1, x2 = np.meshgrid(x1, x2)  # x1 作为行复制两次（行数是len(x2)），返回这个新矩阵
                              # x2 作为列复制两次（列数是len(x1)），返回这个新矩阵
x3 = w[0] * x1 + w[1] * x2
 
    
"""
两个新矩阵是：

 [[-1.5  1.5]
 [-1.5  1.5]] 

 [[-1.5 -1.5]
 [ 1.5  1.5]]
 
 两个矩阵叠在一起，就是网格
 
 (-1.5, -1.5) (1.5, -1.5)
 (-1.5,  1.5) (1.5,  1.5)
 
 计算四个角的高度
 x3 = w[0] * x1 + w[1] * x2  # x1, x2 = x1.flatten(), x2.flatten() 注意是展平后的值 
 
 相当于：
 (-1.5 * w1 +  -1.5 * w2) (1.5 * w1 +  -1.5 * w2)
 (-1.5 * w1 +   1.5 * w2) (1.5 * w1 +   1.5 * w2)
 其中w1 = 0.1, w2 = -0.2，所以：
 (0.15)  (0.45)
 (-0.45) (-0.15)
 
 四个角的高度既可以直接以二维矩阵的形式传给画散点或平面的函数，也可以展平成一维的形式再传
 
"""
print(x1, "\n\n",x2, "\n\n\n")

print(x1 * 0.1, "\n\n", x2 *(-0.2), "\n\n\n")

print(x3)

x1, x2 = x1.flatten(), x2.flatten()  # 网格子矩阵flatten 后就可以传给plot_trisurf 绘制平面
ax.plot_trisurf(x1, x2, [ 0.15,0.45,-0.45,-0.15], antialiased=True, alpha=LIGHT_ALPHA, color="black")
ax.scatter(x1, x2, [ 0.15,0.45,-0.45,-0.15], c=[ 0.15,0.45,-0.45,-0.15], cmap='viridis', linewidth=0.5)  # 绘制散点
```

<img src="Python 3  Summary.assets/image-20200812105520835.png" alt="image-20200812105520835" style="zoom:50%;" />



#### 观察平面角上的点和向量w 的关系



$$
(-1.5, -1.5)^T  \ \  \text{左下角绿色的那个点} \\
w = (0.1, -0.2)^T \ \ \text{决定平面上所有点的高度}
$$



```
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

SQUARE_FIG_SIZE = (10 ,10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
ALPHA = 0.3
LIGHT_ALPHA = 0.1


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"

ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

"""
法向量W
两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, 
    A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
"""
w = [0.1, -0.2]

# 从原点(0, 0, 0)指向(0.1, -0.2, -1)
pts = np.array([ [0, 0, 0], [w[0], w[1], -1] ], np.float).T  
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


# 从原点(0, 0, 0)指向(0.1, -0.2, 0)
pts = np.array([ [0, 0, 0], [w[0], w[1], 0] ], np.float).T
arrow = Arrow3D([0, w[0]],[0, w[1]],[0, 0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1, w[1], 0.1, r"$\left({:.1f},{:.1f},0\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


ax.plot((w[0], w[0]), (w[1], w[1]), (-1, 0), "k--", alpha=ALPHA)    
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = w[0] * x1 + w[1] * x2

print(x1, x2, x3)
print(x1*0.1)
print(x2*(-0.2))
ax.scatter(x1, x2, x3, c=x3, cmap='viridis', linewidth=0.5)

#ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

ax.plot_trisurf(x1, x2, [ -2,-2,-2,-2], antialiased=True, alpha=LIGHT_ALPHA, color="black")
```

<img src="Python 3  Summary.assets/image-20200812113924159.png" alt="image-20200812113924159" style="zoom:50%;" />



### 自定义Plot 类

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

# 返回ax 对象，可以进行各种绘制
class Plot():
    def __init__(self):
        self.SQUARE_FIG_SIZE = (10 ,10)
        self.AXIS_LABEL_FONT_SIZE = 16
        self.TEXT_FONT_SIZE = 16
        self.ALPHA = 0.3
        self.LIGHT_ALPHA = 0.1
        self.fig = plt.figure(figsize=np.array(self.SQUARE_FIG_SIZE) * 2, facecolor='white')
        self.T = "\mathrm{T}"
        self.ax = self.fig.add_subplot(2, 2, 1, projection="3d")
        self.ax.set_xlim([-2, 2])
        self.ax.set_ylim([-2, 2])
        self.ax.set_zlim([-2, 2])
        
        # ax.set_title(r"$Lorenz\ Attractor$")
        self.ax.set_xlabel(r"$x_1$", fontsize=self.AXIS_LABEL_FONT_SIZE)
        self.ax.set_ylabel(r"$x_2$", fontsize=self.AXIS_LABEL_FONT_SIZE)
        self.ax.set_zlabel(r"$y$",   fontsize=self.AXIS_LABEL_FONT_SIZE)

        # 画简头，从p1 指向p2        
    def drawArrow(self, p1, p2):
        pts = np.array([ p1, p2 ], np.float).T  
        arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
        self.ax.add_artist(arrow)

    def drawText(self, w):
        self.ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], self.T), fontsize=self.TEXT_FONT_SIZE)

    def show(self):
        plt.show()

if __name__ == "__main__":
    p = Plot()
    w = [0.1, -0.2]
    p.drawArrow([0, 0, 0], [w[0], w[1], -2])
    p.drawText( w )
    p.show()
```





### 可以拖动的图形

#### plot_trisurf

[plot_trisurf](https://matplotlib.org/3.1.1/tutorials/toolkits/mplot3d.html#mpl_toolkits.mplot3d.Axes3D.plot_trisurf)

```python
trisurf3d.py
'''
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
'''

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


n_radii = 8
n_angles = 36

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Compute z to make the pringle surface.
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```









### ax.plot AND ax.add_artist(Arrow3D)



#### 三维点(0, 0, 2)到点(0, 0, -2) 画线的两种方法

```python
pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.float).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]))
```

```python
# 两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.float).T
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
```



### 画虚线 



```python
# 画虚线 p1 [x, y, z] 坐标 p2 [x, y, z] 坐标 
def drawDashe(p1, p2, ax):
    pts = np.array([ p1, p2 ], np.float).T
    ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)

drawDashe([0, 0, 2], [0, 0, -2], ax)
```







```python
from book_draw_util import *
import numpy as np

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)
"""
坐标系的原点在一楼中心
"""

pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.float).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
"""
楼顶中心指向地下室中心
"""
```

<img src="Python 3  Summary.assets/image-20200804112140778.png" alt="image-20200804112140778" style="zoom: 33%;" />



```

```










### np.float，注意数据类型！别让小数变整数了！

```python
# 绘制法向量
w = [0.1, -0.2]
pts = np.array([ [0, 0, 0], [w[0], w[1], -1] ], np.float).T  # 从原点(0, 0, 0)指向(0.1, -0.2, -1)
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
"""
两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, 
    A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
"""
```





等间隔数字

Return **evenly spaced numbers** over a specified interval.

> even 等，均等
>
> space 间隔，距离，空隙



```python
# 生成等间距的n 个数的list, 包含尾端的数
np.linspace(-1.5, 1.5, endpoint=True, num=2)
```



```python
# 以行向量x1 构建新矩阵，行数是len(x2)
# 以列向量x2 构建新矩阵，列数是len(x1)
# 既len(x1) 定所有新矩阵的行数，len(x2) 定所有新矩阵的列数
# 生成形状一样的两个矩阵是为了待会把它们“叠”到一起，形成有序对(pair), (x1,y1), (x2,y1)
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
```

<img src="Python 3  Summary.assets/image-20200731184147007.png" alt="image-20200731184147007" style="zoom:50%;" />



### meshgrid 用N个坐标轴上的点在空间中画网格

>```python
># 用两个坐标轴的点画网格
>x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
>x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
>[-1.5  1.5] [-1.5  1.5]
>```

```python
# 两个点，生成两个2*2 的矩阵
# x1当成行向量，行复制len(x2) 次，生成新矩阵。这是第一个返回值
# x2当成列向量，列复制len(x1) 次，生成新矩阵。这是第一个返回值
x1, x2 = np.meshgrid(x1, x2) 

[[-1.5  1.5]
 [-1.5  1.5]] 

[[-1.5 -1.5]
 [ 1.5  1.5]]
```

```python
# 网格矩阵降维成1 维
x1, x2 = x1.flatten(), x2.flatten()
# ？？
x3 = w[0] * x1 + w[1] * x2
```

```python
# 画垂直于法向量的平面
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")
```



### 画垂直于向量的平面

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

SQUARE_FIG_SIZE = (10 ,10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
ALPHA = 0.3
LIGHT_ALPHA = 0.1


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"

ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

"""
法向量W
两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, 
    A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
"""
w = [0.1, -0.2]
pts = np.array([ [0, 0, 0], [w[0], w[1], -1] ], np.float).T  # 从原点(0, 0, 0)指向(0.1, -0.2, -1)
arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


# 从原点(0, 0, 0)指向(0.1, -0.2, 0)
pts = np.array([ [0, 0, 0], [w[0], w[1], 0] ], np.float).T
arrow = Arrow3D([0, w[0]],[0, w[1]],[0, 0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0] - 1, w[1], 0.1, r"$\left({:.1f},{:.1f},0\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)


ax.plot((w[0], w[0]), (w[1], w[1]), (-1, 0), "k--", alpha=ALPHA)    
x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = w[0] * x1 + w[1] * x2

print(x1, x2, x3)
ax.scatter(x1, x2, x3, c=x3, cmap='viridis', linewidth=0.5)

ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")
```

<img src="Python 3  Summary.assets/image-20200811102936920.png" alt="image-20200811102936920" style="zoom:50%;" />



#### 先画散点，再画平面

##### ax.scatter，plot_trisurf 

```python
# 画散点
print(x1, x2, x3)
ax.scatter(x1, x2, x3, c=x3, cmap='viridis', linewidth=0.5)
```

<img src="Python 3  Summary.assets/image-20200811101543133.png" alt="image-20200811101543133" style="zoom: 50%;" />

```
[-1.5  1.5 -1.5  1.5] [-1.5 -1.5  1.5  1.5] [ 0.15  0.45 -0.45 -0.15]
```

**z轴是 0.15到-0.15，是平面的厚度**



> numpy.meshgrid（ \*xi，\*\* kwargs ）
>
> xi 是变长参数，可传$x_1, x_2,...,x_n$ 代表n 个坐标轴的点
>
> - 每一个都是**一维数组**
>
> indexing 是可选参数，默认值'xy' 代表笛卡尔；'ij' 代表矩阵
>
> - 'xy' 返回的shape 是(M,N)，Y 定行数，X 定列数
> - ‘ij’ 返回的shape 是(N,M)，X 定行数，Y 定列数
>
> 返回值 是N 个N 维矩阵
>
> - 每一个**矩阵的shape 由indexing 参数决定**





```python
xv, yv = np.meshgrid( x, y )
```

<img src="Python 3  Summary.assets/image-20200803091424334.png" alt="image-20200803091424334" style="zoom:50%;" />



<img src="Python 3  Summary.assets/image-20200803091622368.png" alt="image-20200803091622368" style="zoom: 50%;" />



<img src="Python 3  Summary.assets/image-20200803092919491.png" alt="image-20200803092919491" style="zoom:50%;" />



https://matplotlib.org/3.1.1/api/tri_api.html

matplotlib.tri.Triangulation(x, y, triangles=None, mask=None)



得到三维数据，接着使用散点图观察大致形状，然后使用 plot_trisurf 绘图，plot_trisurf 使用三角形来构造表面并填充配色



```python
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(x) * np.cos(y) * 2

theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))

z = f(x, y)

fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(1, 2, 1, projection='3d', title='scatter')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)

ax = fig.add_subplot(1, 2, 2, projection='3d', title='trisurf')
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
```



<img src="Python 3  Summary.assets/image-20200803174755594.png" alt="image-20200803174755594" style="zoom: 67%;" />





### 楼房坐标系



```
from book_draw_util import *
import numpy as np

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)
"""
坐标系的原点在一楼中心
"""

# 两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数
#pts = np.array([ [0, 0, 0], [0, 0, -1] ], np.int32).T # 从一楼的中心指向地下室的中心
#pts = np.array([ [2, 0, 0], [-2, 0, 0] ], np.int32).T
#ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)

pts = np.array([ [0, 0, 2], [0, 0, -2] ], np.int32).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
"""
楼顶中心指向地下室中心
"""

pts = np.array([ [-2, 0, 2], [0, 0, 2]], np.int32).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
pts = np.array([ [0, 2, 2], [0, 0, 2]], np.int32).T
ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)
"""
两块楼顶地板
"""
```







所有cell 的变量是共享的，全局变量放最前面运行一次

```
all_pic_path = "D:\GitHub\doc\lang\programming\python\高品质图片"
```



doc\lang\programming\python\深入理解神经网络：从逻辑回归到CNN\neural_network-neural_network_code-master\neural_network_code\画图脚本



### alpha 控制向量颜色浅淡

```
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k", alpha=ALPHA)
```



### linestyle 设置虚线风格

```python
ax.arrow(p[0], p[1], (p_next.A1-p)[0], (p_next.A1-p)[1], head_width=0.3, length_includes_head=True, color="k", linestyle="--", alpha=DARK_ALPHA)

linestyle="dashed"
```



### arrow

两个3d 点, A,B 分别写成列向量的形式，凑成一个矩阵，矩阵的所有行作为Arrow3D 的坐标参数

```
arrow = Arrow3D([0,0],[0,0],[-2,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
arrow = Arrow3D([-2,0],[0,0],[0,0], arrowstyle="-|>", linestyle="--", lw=1,mutation_scale=10,color="k", ALPHA=0.2)
ax.add_artist(arrow)
```





### probability distribution



```python
import os, sys;
currDir = os.getcwd()
sys.path.append( os.path.dirname( os.path.dirname( currDir ) ) ) # std 包在此模块的上上上级目录

import math
import std.iFile as iFile
import std.iJson as iJson
import std.iList as iList
import std.seg.iSeg as iSeg
import std.iSql as iSql
import util.fectchData as fectchData


import pandas as pd # 导入另一个包“pandas” 命名为 pd，理解成pandas是在 numpy 基础上的升级包
import numpy as np #导入一个数据分析用的包“numpy” 命名为 np
import matplotlib.pyplot as plt # 导入 matplotlib 命名为 plt，类似 matlab，集成了许多可视化命令


fname_results = os.path.join(currDir, '知识点关联试题2020.7.10.11.03.json')
fname_similarity = os.path.join(currDir, 'similarity.csv')
rs = iJson.load_json(fname_results)

sims = []
for ls in rs:
    for l in ls:
        sims.append( l[3] )

sims = sorted(sims, key=lambda x: x, reverse=True)

frame = pd.DataFrame(sims,columns=['similarity'])
frame.to_csv(fname_similarity, index=False ,encoding="utf-8")

print(max(sims), min(sims))



#jupyter 的魔术关键字（magic keywords）
#在文档中显示 matplotlib 包生成的图形
# 设置图形的风格
%matplotlib inline 
%config InlineBackend.figure_format = 'retina'

data = pd.read_csv(fname_similarity) #载入数据文件

print( data.head(3), '\n\n')
print('row num:', len(data) )


time = data["similarity"] #把数据集中的 time 定义为 time
mean = time.mean()  #mean均值，是正态分布的中心，把 数据集中的均值 定义为 mean
print('mean value: ', mean)

#S.D.标准差，把数据集中的标准差 定义为 std
std = time.std()

#正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf


# 设定 x 轴前两个数字是 X 轴的开始和结束，第三个数字表示步长，或者区间的间隔长度
x = np.arange(0.0,6.0,0.05) 
#设定 y 轴，载入刚才的正态分布函数
y = normfun(x, mean, std)
plt.plot(x,y)
#画出直方图，最后的“density”参数，是赋范的意思，数学概念
plt.hist(time, bins=50, rwidth=0.5, density=True)
plt.title('Time distribution')
plt.xlabel('Time')
plt.ylabel('Probability')

plt.savefig(os.path.join("D:\workcode\python\AUTOMATIC_TEXT_SUMMARIZATION\matchTestAndExampoint", 'distribution.png'), format='png', dpi=600)
#输出
plt.show()
```

<img src="Python 3  Summary.assets/image-20200710154652277.png" alt="image-20200710154652277" style="zoom:50%;" />



### logistic

```python
import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6)) # width, height in inches.  1英寸=2.54厘米
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")


sigma = np.arange(-8, 8, 0.01)
ax.grid(True)
ax.plot(sigma, logistic(sigma), c="k")
plt.xlim(-8, 8)
plt.ylim(-.21, 1.2)
ax.text(x=8.5 , y=-0.02, s=r"$a$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-1.2, y=1.3, s=r"$\mathrm{Logistic}\left(a\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

plt.savefig(os.path.join("D:\workcode\python\plot\高品质图片", '1-1.png'), format='png', dpi=600)
```



<img src="Python 3  Summary.assets/image-20200710103820788.png" alt="image-20200710103820788" style="zoom:50%;" />



### two vector

```
from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")



plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,-2,4, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")

ax.text(x=4.1, y=2.1, s=r"$\left(4,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=-2.5, y=4.1, s=r"$\left(-2,4\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-3.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710110902610.png" alt="image-20200710110902610" style="zoom:50%;" />



```python
from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")

plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,2,1, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,1,3, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,3,4, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")

ax.arrow(1,3,2,1, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=0.3)
ax.arrow(2,1,1,3, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=0.3)

ax.text(x=2.2, y=1, s=r"$x=\left(2,1\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.4, y=3.4, s=r"$y=\left(1,3\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=3.1, y=4.1, s=r"$x+y=\left(3,4\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-4.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710163043611.png" alt="image-20200710163043611" style="zoom:50%;" />





```python
from book_draw_util import *


fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")



plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,1,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")


ax.arrow(1.6,0.8,-0.6,1.2, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)
ax.arrow(1.4,0.7,-0.1,0.2, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)
ax.arrow(1.3,0.9,0.2,0.1, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)

ax.text(x=4.1, y=2.1, s=r"$y=\left(4,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=1.1, y=2.1, s=r"$x=\left(1,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.2, y=0.2, s=r"$\theta$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.05, y=1.6, s=r"$\left||x\right||$", fontsize=TEXT_FONT_SIZE)
ax.annotate(s=r"$\left||x\right||\mathrm{cos}\theta=\frac{\left<x,y\right>}{\left||y\right||}$", 
        xy=(0.7,0.3), xytext=(2,0.25), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-8.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710170341783.png" alt="image-20200710170341783" style="zoom:50%;" />







```python
from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)

arrow = Arrow3D([0,3],[0,-1.5],[0,3], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(3, -1.5, 3, r"$w$", fontsize=TEXT_FONT_SIZE)


x1 = np.linspace(-0.6, 2, endpoint=True, num=2)
x2 = np.linspace(-2, 0.8, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = 2 - x1 + 0.5 * x2
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")


arrow = Arrow3D([0,0],[0,0],[0,2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(0, 0, 2, r"$x_a$", fontsize=TEXT_FONT_SIZE)
ax.text(-0.05, 0.2, 0.1, r"$\theta_a$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,2],[0,0],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(2, 0, 0, r"$x_b$", fontsize=TEXT_FONT_SIZE)
ax.text(0.2, 0, .05, r"$\theta_b$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,0],[0,2],[0,1], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(0, 2, 1, r"$x_c$", fontsize=TEXT_FONT_SIZE)
ax.text(0, 0.6, 0.12, r"$\theta_c$", fontsize=TEXT_FONT_SIZE)


ax.plot((8/7, 0), (-4/7, 0), (8/7, 2), "k--", alpha=ALPHA)
ax.plot((8/7, 2), (-4/7, 0), (8/7, 0), "k--", alpha=ALPHA)
ax.plot((8/7, 0), (-4/7, 2), (8/7, 1), "k--", alpha=ALPHA)
ax.scatter(8/7, -4/7, 8/7, s=POINT_SIZE, c="k")
ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")

ax.set_title(r"$||x_a||\mathrm{cos}\theta_a=||x_b||\mathrm{cos}\theta_b=||x_c||\mathrm{cos}\theta_c=\frac{x_a^\mathrm{T}w}{||w||}=\frac{x_b^\mathrm{T}w}{||w||}=\frac{x_c^\mathrm{T}w}{||w||}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-10.png'), format='png', dpi=600) 
```



<img src="Python 3  Summary.assets/image-20200710172303832.png" alt="image-20200710172303832" style="zoom:50%;" />





## ManimCE

- https://www.youtube.com/watch?v=_CWSYu4mrY4

  - https://github.com/univalency/Manim-animations-code-for-MetaMaths
  - awesome code

     

### Colab

- 按顺序分别运行

```
!sudo apt update
!sudo apt install libcairo2-dev ffmpeg \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev
!pip install manim
!pip install IPython --upgrade
```

```
from manim import *
config.media_width = "60%"
```

```python
%%manim -v WARNING -qm LinearTransformationSceneExample

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self, **kwargs):  # Colab 必须要多一个参数：**kwargs
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs,
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()
```



- https://try.manim.community/
- https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html

```
# https://github.com/brianamedee/Manim-Tutorials-2021
	# https://www.youtube.com/watch?v=Yf9QnATooqA
	# 极好的例子

# https://docs.manim.community/en/stable/examples.html
	# 高级例子
	
# https://github.com/Rickaym/Manim-Sideview
	# live preview

# https://docs.manim.community/en/stable/installation/jupyter.html
# https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html
	# 整合jupytern

```



### 画向量



```
from manim import *

class transform(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)

        self.add(numberplane)
        self.add(dot, arrow, origin_text)
```



### 线性变换



```
from manim import *

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()
```



###　移动的方块



```
%%manim -v WARNING -qm Tute1

from manim import *
config.media_width = "60%"

import numpy as np
import random

class Tute1(Scene):
    def construct(self):

        plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()
        box = Rectangle(stroke_color = GREEN_C, stroke_opacity=0.7, fill_color = RED_B, fill_opacity = 0.5, height=1, width=1)

        dot = always_redraw(lambda : Dot().move_to(box.get_center())) # 始终重绘，每次都移动到盒子的中心
        

        self.add(box, dot)
        self.play(box.animate.shift(RIGHT*2), run_time=4)  # 右移
        self.wait()
        self.play(box.animate.shift(UP*3), run_time=4)     # 上移
        self.wait()
        self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=4)  # 左下移
        self.wait()
        self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=4)  # 右上移
        self.wait()
```



### 取消更新



```
        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE,
        fill_color = BLUE_B, width = 4.5, height = 2).shift(UP*3+LEFT*4)

        mathtext = MathTex("\\frac{3}{4} = 0.75"
        ).set_color_by_gradient(GREEN, PINK).set_height(1.5)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))


        self.play(FadeIn(rectangle))
        self.wait()
        self.play(Write(mathtext), run_time=2)
        self.wait()

        self.play(rectangle.animate.shift(RIGHT*1.5+DOWN*5), run_time=6)
        self.wait()
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(LEFT*2 + UP*1), run_time=6)
        self.wait()
```





### 上滑动画

```
class Scroll(AnimationGroup):
    def __init__(self, mob, target_mob, shift=UP):
        super().__init__(
            FadeIn(target_mob, shift=shift),
            FadeOut(mob, shift=shift),
        )
        
class Test(Scene):
    def construct(self):
        a = Text("Hello")
        b = Text("World")
        self.add(a)
        # self.play(FadeIn(b, shift=UP), FadeOut(a, shift=UP))
        self.play(Scroll(a, b))
        self.wait()

```









## Algo



### N-Gram

```python
myre = {2:'(..)', 3:'(...)', 4:'(....)', 5:'(.....)', 6:'(......)', 7:'(.......)'}
max_sep = 4 #候选词语的最大字数
for m in range(2, max_sep+1):
    print(u'正在生成%s字词...'%m)
    t.append([])
    for i in range(m): #生成所有可能的m字词
        t[m-1] = t[m-1] + re.findall(myre[m], s[i:])

```



### 算润年

```
通常，我求一个区间内的闰年数时，常规方法是会使用一个循环进行遍历，然后依据以上的两个条件对每一个年份进行判断，从而得出给定区间内有多少个闰年，比如0~2017，但是这里就有个问题，如果所求区间较小，还没什么影响。如果所求区间较大，比如0~2017000000，那么使用常规的循环方法就会非常耗时。

-------------------------------下面是集合的方法--------------------------

我们定义三个集合A，B，C。

其中A集合中为区间内所有的4的倍数；

B集合中为区间内所有的100的倍数；

C集合中为区间内所有的400的倍数；

那么，很显然，C包含于B，B包含于A。

这里我们假设A集合中的元素个数为a，B集合中的元素个数为b，C集合中的元素个数为c，那么：

条件1、年份能被4整除但不能被400整除

即为a-b

条件2、年份能被400整除

即为c

区间内闰年的总数即为：a-b+c
```

```python
import math

A = [i*4 for i in range(1, math.floor(2021/4)+1) ]
B = [i*100 for i in range(1, math.floor(2021/100)+1) ]
C = [i*400 for i in range(1, math.floor(2021/400)+1) ]
num = len(A)-len(B)+len(C)
print(num)
```

```python
import math

A = set( [i*4 for i in range(1, math.floor(2021/4)+1) ] )
B = set( [i*100 for i in range(1, math.floor(2021/100)+1) ] )
C = set( [i*400 for i in range(1, math.floor(2021/400)+1) ] )

leapYears = ( A - B ) | C
print( len(leapYears) )
print( leapYears )
```

![image-20210225100710499](Python 3  Summary.assets/image-20210225100710499.png)



### simhash

```

https://www.jianshu.com/p/1187fb7c59c5

http://gameofdimension.com/2020/04/04/simhash/

https://wizardforcel.gitbooks.io/the-art-of-programming-by-july/content/06.03.html

https://zhuanlan.zhihu.com/p/71488127

http://www.jouypub.com/2018/9b9f561f6a0893f3d74a153b8f2e8dcb/

http://debugger.wiki/article/html/1562565630032326
	https://github.com/1e0ng/simhash  # 优秀
		sklearn-TfidfVectorizer彻底说清楚
			https://zhuanlan.zhihu.com/p/67883024
	https://www.cnblogs.com/maybe2030/p/5203186.html#_label4




https://github.com/yanyiwu/simhash
https://github.com/yanyiwu/simhash_server


原理较透彻
https://vimsky.com/article/145.html
https://tech.igengmei.com/20190531/locality-sensitive-hashing/
https://kexue.fm/archives/8159
	LSH
	从几何视角来理解模型参数的初始化策略
		https://kexue.fm/archives/7180

高维球上的取样和分布：讨论与证明
	https://re-ra.xyz/%E9%AB%98%E7%BB%B4%E7%90%83%E4%B8%8A%E7%9A%84%E5%8F%96%E6%A0%B7%E5%92%8C%E5%88%86%E5%B8%83-%E8%AE%A8%E8%AE%BA%E4%B8%8E%E8%AF%81%E6%98%8E/


随机超平面hash算法非常简单
	http://wfwei.github.io/posts/hash-rel/
	随机超平面哈希 Random projection hash
	相似哈希 simhash(Bit sampling for Hamming distance)
	最小哈希 minhash(Min-wise independent permutations)

从NLP任务中文本向量的降维问题，引出LSH（Locality Sensitive Hash 局部敏感哈希）算法及其思想的
	https://flashgene.com/archives/43580.html


维数大于3的空间中的平面一般被称为超平面


Simhash与随机超平面hash算法的联系与区别 
	https://www.cnblogs.com/LittleHann/p/11002030.html


simhash算法其实与随机超平面hash算法是相同的
	http://wfwei.github.io/posts/hash-rel/
	在simhash算法中，并没有直接产生用于分割空间的随机向量，而是间接产生的：第k个特征的hash签名的第i位拿出来，如果为0，则改为-1，如果为1则不变，作为第i个随机向量的第k维。由于hash签名是f位的，因此这样能产生f个随机向量，对应f个随机超平面。


汉明距离-海明距离


 var hammingDistance = function(x, y) {
 var num = x^y;
 var res = 0; //计数器
  while(num) {
  res += num&0X01; //num和1相与，因为1前面都是零，所以与之后可以判断出num的最后一位是不是1，若是1，则计数器就会加1.
  num>>=1;//num右移一位，注意要有等号，不然类似于i+1;只是一个公式，没有复制给变量。
  }
 return res;
 };




纯C 实现
https://github.com/optimyze/simple_simhash
	GCC有一个叫做__builtin_popcount的内建函数，它可以精确的计算1的个数



可逆hash
	Jenkins Hash算法
	http://d0evi1.com/wang-jenkins-hash/


浅谈基于simhash的文本去重原理
	https://juejin.cn/post/6844904031865798664


与simhash的位数b有关，b越大精确度越高
simhash和bloom filter算法可能出现误判现象，即不相似的文件可能会判定为相似


256bit c实现
simhash github 搜，选C语言

256位，python实现
https://github.com/sean-public/python-hashes

```

```
汉明距离-海明距离


 var hammingDistance = function(x, y) {
 var num = x^y;
 var res = 0; //计数器
  while(num) {
  res += num&0X01; //num和1相与，因为1前面都是零，所以与之后可以判断出num的最后一位是不是1，若是1，则计数器就会加1.
  num>>=1;//num右移一位，注意要有等号，不然类似于i+1;只是一个公式，没有复制给变量。
  }
 return res;
 };
```

![image-20210302160454870](Python 3  Summary.assets/image-20210302160454870.png)

![image-20210302160526564](Python 3  Summary.assets/image-20210302160526564.png)



```c++
    int hamming_distance(unsigned long x, unsigned long y) {
        int dist = 0;
        unsigned long val = x^y;

        while (val != 0) {
            dist++;
            val &= val -1;
        }
        return dist;
    }

    double similarity(const std::string s, const std::string k) {
        unsigned long hash_s = simhash(s);
        unsigned long hash_k = simhash(k);
        return 1 - hamming_distance(hash_s, hash_k) / 64.0;
    }
}
```





## 数论



[中英字幕] 科普：**费马大定理的证明** | 椭圆曲线与模形式 [u](https://www.bilibili.com/video/BV1ut4y1C7Z1?t=41)

- **sage 库**,python

**vscode+jupyternotebook+sagemath配置** [u]()



# Redis

```
https://linuxize.com/post/how-to-install-and-configure-redis-on-centos-7/
```

```
# 无需密码
CONFIG SET protected-mode no
```





# ffmpeg.wasm

[ffmpeg.wasm render video in canvas](https://www.mysourcebook.com/2023/01/decode-big-video-using-ffmpeg-wasm-to-render-use-canvas.html)

[How to enable HTTPS protocol in ffmpeg.wasm?](https://www.mysourcebook.com/2023/01/how-to-enable-https-protocol-in-ffmpeg.wasm.html)



```
    # ffmpeg -i "1.mp4" -vf "select='between(t,4,6.5)+between(t,17,26)+between(t,74,91)',setpts=N/FRAME_RATE/TB" -af "aselect='between(t,4,6.5)+between(t,17,26)+between(t,74,91)',asetpts=N/SR/TB" out.mp4
    # https://github.com/mifi/lossless-cut
    # https://zhuanlan.zhihu.com/p/62649633
    
    
    [0:v]pad=iw*2:ih[v_wide];
[v_wide][1:v]overlay=W/2:0[out_video];
[0:a]volume=6dB[ao]

-map [out_video]:v -c:v ...
-map [ao]:a -c:a aac ...

既然用了 filter_complex ，大多数情况下就没必要用-af -vf 了，所有效果写在一起更容易整理
    
```





```
(async () => {
    let { writeFile } = await import('fs/promises')
    let { createFFmpeg, fetchFile } = await import('@ffmpeg/ffmpeg')
    let ffmpeg = createFFmpeg({ log: true })
    await ffmpeg.load()

    ffmpeg.FS('writeFile', '1.mkv', await fetchFile('./1.mkv'))
    await ffmpeg.run('-i', '1.mkv', "-ss", "00:00:03", "-to", "00:00:04", '1.mp4')
    await require('fs').writeFileSync('./1.mp4', ffmpeg.FS('readFile', '1.mp4'))
    process.exit(0)
})()
```



```
 var Module = {};

   fetch('https://example.com/ffmpeg.wasm')
      .then(response => response.arrayBuffer())
      .then(bytes => WebAssembly.instantiate(bytes, Module))
      .then(results => {
         Module.instance = results.instance;
         // FFmpeg.wasm is now loaded and ready to use
      });
```





```
getting error message RuntimeError: indirect call to null when using libx265 but libx264 works with same settings
await ffmpeg.run( '-ss', '30', '-t', '3', '-i', 'input.bin', '-movflags',  '+faststart', '-vf', "scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse,format=yuv420p", '-c:v', 'libx265', '-crf', '28', '-an', 'output.mp4'  );
```





# Extract Video Subtitle



- https://github.com/YaoFANGUK/video-subtitle-extractor



see huggingface/video-subtitle-extractor/readme.txt

see 深入理解神经网络：从逻辑回归到CNN.md -> PaddleOCR



```
conda deactivate && \
conda env remove -n vse

conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n vse python=3.10 --yes && \
conda activate vse

```





```python
"""
git clone https://github.com/YaoFANGUK/video-subtitle-extractor.git

pip install -r requirements.txt  # for backend

opencv-python==4.5.4.60
python-Levenshtein-wheels==0.13.2
paddlepaddle==2.1.3
filesplit==3.0.2
pysrt==1.1.2
wordsegment==1.3.1
imgaug==0.4.0
pyclipper==1.3.0.post2
lmdb==1.2.1
"""

subtitle_area = (self.ymin, self.ymax, self.xmin, self.xmax)
from backend.main import SubtitleExtractor
self.se = SubtitleExtractor(self.video_path, subtitle_area) 
# 'D:/Downloads/火影忍者天空树双语/火影忍者001天空树双语.mp4'
#  (834, 897, 0, 1280)


    def _compare_ocr_result(self, img1, img2):
        """
        比较两张图片预测出的字幕区域文本是否相同
        """
        area_text1 = "".join(self.__get_area_text(self.ocr.predict(img1)))
        area_text2 = "".join(self.__get_area_text(self.ocr.predict(img2)))
        if ratio(area_text1, area_text2) > config.THRESHOLD_TEXT_SIMILARITY:
            return True
        else:
            return False
        
        
        
        
        
         # 删除缓存
        if os.path.exists(self.raw_subtitle_path):
            os.remove(self.raw_subtitle_path)
        # 新建文件
        f = open(self.raw_subtitle_path, mode='w+', encoding='utf-8')

        for i, frame in enumerate(frame_list):
            # 读取视频帧
            img = cv2.imread(os.path.join(self.frame_output_dir, frame))
            # 获取检测结果
            dt_box, rec_res = text_recogniser.predict(img)
            # 获取文本坐标
            coordinates = self.__get_coordinates(dt_box)
            # 将结果写入txt文本中
            text_res = [(res[0], res[1]) for res in rec_res]
            # 进度条
            self.progress = i / len(frame_list) * 100
            for content, coordinate in zip(text_res, coordinates):
                if self.sub_area is not None:
                    s_ymin = self.sub_area[0]
                    s_ymax = self.sub_area[1]
                    s_xmin = self.sub_area[2]
                    s_xmax = self.sub_area[3]
                    xmin = coordinate[0]
                    xmax = coordinate[1]
                    ymin = coordinate[2]
                    ymax = coordinate[3]
                    if s_xmin <= xmin and xmax <= s_xmax and s_ymin <= ymin and ymax <= s_ymax:
                        print(content[0])
                        if content[1] > config.DROP_SCORE:
                            f.write(f'{os.path.splitext(frame)[0]}\t'
                                    f'{coordinate}\t'
                                    f'{content[0]}\n')
                else:
                    f.write(f'{os.path.splitext(frame)[0]}\t'
                            f'{coordinate}\t'
                            f'{content[0]}\n')
        # 关闭文件
        f.close()
        
```





```

from tools.infer import utility
from tools.infer.predict_system import TextSystem

import config
from config import interface_config

import cv2


if __name__ == '__main__':

    args = utility.parse_args()

    args.use_gpu = False
    
    # 加载快速模型
    args.det_model_dir = config.DET_MODEL_FAST_PATH
    # 加载快速模型
    args.rec_model_dir = config.REC_MODEL_FAST_PATH

    # 设置字典路径
    args.rec_char_dict_path = config.DICT_PATH
    # 设置识别文本的类型
    args.rec_char_type = config.REC_CHAR_TYPE

    recogniser = TextSystem(args)

    img = cv2.imread('1.png')

    detection_box, recognise_result = recogniser(img)

    a = 1
```







### 提取关键帧图片带时间

```
"""
ffmpeg -skip_frame nokey -i 1.mp4 -r 1000 -vsync 0 -frame_pts true tmp/out%d.png
	# 只要关键帧，数字代表的时间是毫秒数（1/1000秒）
skip_frame tells the decoder to process only keyframes. -vsync 0 (in this command) preserves timestamps. -frame_pts sets the numeral portion of the output image filename to represent the timestamp. The interpretation of the number requires you to know the framerate e.g. if the framerate is 30 then an image name of out75 corresponds to a timestamp of 75/30 = 2.50 seconds. You can add -r 1000 if you want numbers to represent milliseconds.
"""

ffmpeg -ss 00:22:30 -i Mononoke.Hime.mkv -ss 00:00:30 -frames:v 1 out3.jpg
	#在这个视频文件的22分钟30秒处，再向后30秒的位置，截取一帧画面，输出为名为 "out3.jpg" 的图片文件

```



### 剪视频



```
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4

# 需重新编码，含非关键帧
ffmpeg -i movie.mp4 -ss 00:00:03 -t 00:00:08 -async 1 cut.mp4

//			.outputOptions(["-movflags", "frag_keyframe+empty_moov"]) //without these options ffmpeg errors with `muxer does not support non seekable output`

```





### 分离人声伴奏

```
# https://github.com/deezer/spleeter
```







```
# https://github.com/YaoFANGUK/video-subtitle-extractor

from backend.main import SubtitleExtractor
# 输入视频路径
# 新建字幕提取对象
se = SubtitleExtractor(video_path, subtitle_area)
# 开始提取字幕
se.run()
```



### 音频数字指纹

- https://github.com/xitu/gold-miner/blob/master/TODO/fingerprinting-and-audio-recognition-with-python.md
  - 用 Python 和 Numpy 实现音频数字指纹特征识别





# PYQT

## 提取视频人声

```
# https://github.com/YaoFANGUK/video-subtitle-extractor/issues/15
# https://github.com/m986883511/extract-video-subtittle
# https://gitee.com/m986883511/python_demo/blob/master/%E5%AD%97%E5%B9%95%E7%A1%AC%E6%8F%90%E5%8F%96/main.py
# doc\lang\programming\python\studioclassroom_FulltextSearch\insertanime\extract_human_audio.py

# marsmarcin
# 2020.3.11
# a test version for a beautiful system
# https://zmister.com/archives/477.html
import os
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtCore import QThread, QProcess, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTextEdit, QLabel, QFileDialog, QMessageBox
from pydub import AudioSegment
from pydub.silence import split_on_silence
from subtext.scripts import get_extract_voice_progress

current_dir = os.path.dirname(__file__)


class MyThread(QThread):  # 线程2
    my_signal = pyqtSignal(int)
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.estimate_time = None
        self.finished = None
        self.input_func = None
        self.input_args = None
        self.input_kwargs = None
        self.result = None
        self.name = None

    def __fake_progress(self):
        start_time = time.perf_counter()
        while not self.finished:
            use_time = time.perf_counter() - start_time
            progress = int(100.0 * use_time / self.estimate_time)
            if progress > 95:
                progress = 95
            self.my_signal.emit(progress)
            time.sleep(0.25)
        self.log_signal.emit('假进度线程结束')

    def set_function(self, name, estimate_time, func, *args, **kwargs):
        self.name = name
        self.input_func = func
        self.estimate_time = estimate_time
        self.input_args = args
        self.input_kwargs = kwargs

    def run(self):
        if not callable(self.input_func):
            return
        self.log_signal.emit('{} thread start'.format(self.name))
        self.finished = False
        fake_thread = Thread(target=self.__fake_progress)
        fake_thread.setDaemon(True)
        fake_thread.start()
        self.result = self.input_func(*self.input_args, **self.input_kwargs)
        self.finished = True
        self.my_signal.emit(100)
        print(self.result)
        self.log_signal.emit('{} thread end'.format(self.name))


class MainUi(QtWidgets.QMainWindow):
    process = QProcess()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.video_file_path = ''
        self.output_voice_path = os.path.abspath(os.path.join(current_dir, 'temp', 'extract.mp3'))
        self.temp_path = os.path.abspath(os.path.join(current_dir, 'temp'))
        self.human_voice_file = os.path.abspath(os.path.join(self.temp_path, 'extract', 'vocals.wav'))
        self.voice_path = os.path.abspath(os.path.join(self.temp_path, 'voice'))
        self.prepare_dir()
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.update_process_bar)
        self.my_thread.log_signal.connect(self.add_string_text)

    def prepare_dir(self):
        os.makedirs(os.path.join(current_dir, 'temp', 'voice'), exist_ok=True)
        os.makedirs(os.path.join(current_dir, 'temp', 'picture'), exist_ok=True)

    def init_ui(self):
        self.setFixedSize(1024, 600)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.up_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.up_widget.setObjectName('up_widget')
        self.up_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.up_widget.setLayout(self.up_layout)  # 设置左侧部件布局为网格
        self.process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.process_bar.setValue(10)
        self.process_bar.setFixedHeight(5)  # 设置进度条高度
        self.process_bar.setTextVisible(False)  # 不显示进度条文字
        self.up_layout.addWidget(self.process_bar)
        self.main_layout.addWidget(self.up_widget, 0, 0, 1, 12)  # 左侧部件在第0行第0列，占12行2列

        self.zhong_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.zhong_widget.setObjectName('zhong_widget')
        self.zhong_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.zhong_widget.setLayout(self.zhong_layout)  # 设置左侧部件布局为网格
        self.show_text = QTextEdit()
        self.picture_label = QLabel("123123")
        self.zhong_layout.addWidget(self.show_text, 0, 6, 6, 6)
        self.zhong_layout.addWidget(self.picture_label, 0, 0, 6, 6)
        self.main_layout.addWidget(self.zhong_widget, 2, 0, 2, 12)  # 左侧部件在第0行第0列，占12行2列

        self.buttom_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.buttom_widget.setObjectName('zhong_widget')
        self.buttom_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.buttom_widget.setLayout(self.buttom_layout)  # 设置左侧部件布局为网格
        self.vedio_file_button = QtWidgets.QPushButton('选择视频文件')
        self.vedio_file_button.clicked.connect(self.get_video_file)  # 关联
        self.get_voice_button = QtWidgets.QPushButton('提取人声')
        self.get_voice_button.clicked.connect(self.get_video_voice)  # 关联
        self.split_voice_button = QtWidgets.QPushButton('计算字幕位置')
        self.split_voice_button.clicked.connect(self.split_human_voice)  # 关联

        self.get_subtext_button = QtWidgets.QPushButton('识别字幕')
        self.get_subtext_button.clicked.connect(self.split_human_voice_to_list)  # 关联

        self.buttom_layout.addWidget(self.vedio_file_button, 0, 0, 2, 3)
        self.buttom_layout.addWidget(self.get_voice_button, 0, 3, 2, 3)
        self.buttom_layout.addWidget(self.split_voice_button, 0, 6, 2, 3)
        self.buttom_layout.addWidget(self.get_subtext_button, 0, 9, 2, 3)
        self.main_layout.addWidget(self.buttom_widget, 10, 0, 2, 12)  # 左侧部件在第0行第0列，占12行2列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.main_layout.setSpacing(0)

        self.process.finished.connect(self.process_finishend)
        self.process.readyReadStandardError.connect(self.update_stderr)
        self.process.readyReadStandardOutput.connect(self.update_stdout)

    # 无边框的拖动
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def split_human_voice(self):
        cmd = 'spleeter separate -d 1800 -p spleeter:2stems -o {} {}'.format(self.temp_path, self.output_voice_path)
        cmd_list = cmd.split(' ')
        self.process.start(cmd_list[0], cmd_list[1:])

    def update_process_bar(self, progress):
        self.process_bar.setValue(progress)

    def __deal_with_process_output_string(self, input_str):
        str1 = bytearray(input_str)
        str1 = str1.decode('gbk').strip()
        if str1:
            self.show_text.append(str1)
            progress = get_extract_voice_progress(str1)
            if progress:
                self.update_process_bar(progress)

    def update_stderr(self):
        str1 = self.process.readAllStandardError()
        self.__deal_with_process_output_string(str1)

    def update_stdout(self):
        str1 = self.process.readAllStandardOutput()
        self.__deal_with_process_output_string(str1)

    def add_string_text(self,str1):
        self.show_text.append(str1)


    def process_finishend(self, exitCode, exitStatus):
        if exitCode != 0:
            self.show_text.append('Abnormal End, exitCode={}, existStatus={}'.format(exitCode, exitStatus))
            QMessageBox.critical(self, 'command exception', 'process existed abnormally',
                                 QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.show_text.append('Normal End, exitCode={}, existStatus={}'.format(exitCode, exitStatus))

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def get_video_file(self):
        self.video_file_path = QFileDialog.getOpenFileName(self, '选择文件')[0]
        print(self.video_file_path)

    def get_video_voice(self):
        cmd = "ffmpeg -i {} {} -y".format(self.video_file_path, self.output_voice_path)
        cmd_list = cmd.split(' ')
        self.process.start(cmd_list[0], cmd_list[1:])

    def split_human_voice_to_list(self):
        def func():
            sound = AudioSegment.from_mp3(self.human_voice_file)
            chunks = split_on_silence(sound, min_silence_len=430,
                                      silence_thresh=-45, keep_silence=400)
            return chunks

        self.my_thread.set_function(name='根据声调分割语音', estimate_time=60, func=func)
        self.my_thread.start()

    # 关闭按钮动作函数
    def close_window(self):
        self.close()


def main():
    import cgitb

    cgitb.enable()
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```



# paddleOCR



```
anaconda3+ paddleOCR安装使用 
	# https://www.cnblogs.com/xuanmanstein/p/13840670.html
```



## PaddleOCR训练自己的数据集

- https://blog.csdn.net/u013171226/article/details/115179480



# GOT-OCR2.0

https://github.com/Ucas-HaoranWei/GOT-OCR2.0



# EasyOCR



```
# https://blog.csdn.net/woshicver/article/details/120300161
```



# Calamari-OCR



```
作者：AIDD Pro
链接：https://www.zhihu.com/question/375768882/answer/2038676357
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

背后的技术OCR 模型的性能利用了多层人工神经网络，最常见的类型是循环神经网络 (RNN) 或更准确地说是长短期记忆 (LSTM) 和卷积神经网络 (CNN)。RNN的工作原理是保存一层的输出，然后作为输入反馈回来，这种架构使得预测层的结果变得容易；CNN 是一种前馈类型的神经网络，信息流经网络，模型的输出不再用作输入。卷积循环神经网络 (CRNN) 是 CNN、RNN和CTC loss的组合，这种神经网络架构将特征提取、序列建模和转录集成到一个统一的框架中。该模型不需要字符分割，卷积神经网络从输入图像（文本检测区域）中提取特征。对CRNN模型的补充可用于改进对输入图像中文本的预测：比较流行的是添加Attention机制以创建Attention-OCR 模型。简而言之，Attention用于 CRNN和LSTM本身无法进行的长程依赖关系预测。当Attention并行运行多次时，Multi-head attention可以进一步提高准确性。Transformer是提高OCR架构准确性的另一种流行方式。Transformer基本上执行与LSTM 类似的功能，不同之处在于，与RNN不同，它不需要按顺序（即从头到尾）处理输入数据。这可以显着减少训练这种OCR算法所需的时间。一些著名的 NLP transformer模型是BERT，以及GPT-2和GPT-3。另外还有RAM和DRAM是深度学习OCR中的循环attention模型。客户的任务并不总是需要从头开始构建OCR引擎，开箱即用的框架Tesseract能够训练出神经网络的出色能力。它提供现成的基于NN的模型，并允许具有深厚专业知识的工程师训练自定义OCR算法。Tesseract最初是在1985年到1994年间在惠普实验室开发的，2005 年被惠普开源。2006年，Tesseract被认为是当时可用的最准确的开源OCR引擎之一。Tesseract的功能主要限于结构化文本数据，它在具有显著噪音的非结构化文本中表现非常差。自2006 年以来，谷歌一直在赞助它的进一步开发。基于深度学习的方法对于非结构化数据表现更好。 Tesseract4使用基于LSTM网络的OCR引擎添加了基于深度学习的功能，该引擎专注于线条识别，最新的稳定版本4.1.0于2019年7月7日发布，该版本在非结构化文本上也更加准确，但通常需要清晰的图像才能正常运行。另一个谷歌支持的项目，OCRopus是一个包含OCR的文档分析系统集合，现在使用支持GPU的文本行识别器和深度学习布局评估工具。最初是用Python编写的，目前也有独立的C++ CLSTM 版本。OCRopus一直被用作谷歌ReCaptcha算法的OCR引擎而闻名，尽管它的性能在这方面偶尔会受到批评。其分裂出来的项目还有Kraken、Calamari OCR、Keras OCR等。为了方便图像处理，来自OpenCV的工具可能会派上用场。它是一个开源库，提供不同的计算机算法。另一个由Google提供支持的解决方案是Vision API，它提供预训练模型以从不同类型和质量的图像中提取文本。
```



# PPOCRLabel 半自动化图形标注



- https://github.com/Evezerest/PPOCRLabel/blob/dygraph/README_ch.md



# ppstructure 版面分析



- https://blog.csdn.net/wss794/article/details/122494246?spm=1001.2014.3001.5502



# 目标检测

- https://shliang.blog.csdn.net/article/details/106072347
  - YOLOv3 Darknet安装编译与训练自己的数据集



# opencv

- https://github.com/OpenStitching/stitching  图片拼接

- https://yanshilin.xyz/
  - 周旋的梦游仙境 | 一个工程师的后花园

```
pip install opencv-python  # import cv2  # win10要编译很久的
```



## 读mp4第一帧图片

```
import cv2, subprocess, math
import os,sys
from PIL import Image
import numpy as np
		self.cap = cv2.VideoCapture(mp4)
        if not self.cap.isOpened():
            raise ValueError("Cannot open video file")
		self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        iterating, frame = self.cap.read()
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = Image.fromarray(display_frame)
        img.save('xxx.jpeg', format="JPEG")
```





## 图像处理宝藏

- https://pyimagesearch.com/2021/01/25/detecting-low-contrast-images-with-opencv-scikit-image-and-python/



## 中文文件名错误

```python
import numpy as np
import cv2

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':

    imgData = np.fromfile('./密密麻麻.bmp', dtype=np.uint8)
    img = cv2.imdecode(imgData, -1)
    # image = cv2.imdecode(np.fromfile('./cleaned.jpg',dtype=np.uint8), -1)

```



## base64



```python
import base64

message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
msg = base64.b64decode(base64_message).decode('ascii')

print(base64_message)
```





## crop



```python
see huggingface/rwkv5-jp-trimvd/appv2.py
            def changecrp(evt: gr.EventData):
                global m4
                if isDebug: 
                    print("### changecrp hit.", evt.target, evt._data)
                m4.crop_info = evt._data.copy()  # {x, y, width, height} is orig image's rate,  ori.width * width = corpWidth, others similar this.
                
                h = m4.ocr_frame.shape[0]  # 注意：高是行数
                w = m4.ocr_frame.shape[1]  # 宽是列数
                x_rate = m4.crop_info['x']
                y_rate = m4.crop_info['y']
                width_rate = m4.crop_info['width']
                height_rate = m4.crop_info['height']
                
                x = math.ceil(w * x_rate)
                y = math.ceil(h * y_rate)
                width = math.ceil(w * width_rate)
                height = math.ceil(h * height_rate)
                
                img_crop = m4.ocr_frame[y:y+height, x:x+width]
                
                # cv2.imshow("img_crop", img_crop)
                # cv2.waitKey(0)
                                
                return img_crop # m4.ocr_frame
            imageeditor_ocr_frame.change_crop(changecrp, None, [image_preview2])
```



 

## 读取图片为字节



```python
import numpy as np
import cv2

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':
    
    np_array = np.fromfile('./密密麻麻.bmp', dtype=np.uint8)
    img = cv2.imdecode(np_array, -1)
    # bytes = img.tobytes()  # 转字节数组  # 或者使用img.tostring()，两者是等价的
        # 注意了：得到的bytes数据并不等价于open(file,"rb")数据

    # 把img 对象编码为jpg 格式
    success, encoded_image = cv2.imencode(".jpg", img) 
    # 将数组转为bytes
    bytes = encoded_image.tobytes() # 等价于tostring() 
    
    with open("yyyyyyyyyyyyy.jpg", "wb") as fp:
        fp.write(bytes)  # 成功，我们自已写的 bytes

    cv2.imwrite('./ttttttttttttttttttt.jpg', img)  # 成功，opencv 保存 img 对象
```



```python
# 读以 base64 写入磁盘的图片
import cv2
import numpy as np
import base64

if __name__ == "__main__":
    
    with open('./a1db998d1c6c9f9e34be9689c010849e.txt', "r", encoding='ascii') as f:
        base64Image = f.read()
        
    bytesImage = base64.b64decode(base64Image)
    
    imgData = np.frombuffer(bytesImage, dtype=np.uint8)
    img = cv2.imdecode(imgData, -1)
    
    cv2.imshow('test', img)
    cv2.waitKey()
```







## 自动旋转180度

```python
import argparse
import cv2
import imutils
import numpy as np
import base64

imgData = np.fromfile('./密密麻麻.bmp', dtype=np.uint8)
image = cv2.imdecode(imgData, -1)
# image=cv2.imread('book.jpg')
# 获取图像的维度，并计算中心
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# - (cX,cY): 旋转的中心点坐标
# - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
# - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
M = cv2.getRotationMatrix2D((cX, cY), -0.0190033 * (180 / 3.1415926), 1.0)  # 1° = π/180弧度   1 弧度 =  180 / 3.1415926  # 0.0190033 是Mathematica 算出来的弧度，先转换成角度
rotated = cv2.warpAffine(image, M, (w, h))  # 仿射变换

# 顺时针旋转33度，并保证图像旋转后完整~,确保整个图都在视野范围
# 使用imutils.rotata 一行代码实现旋转
# rotated = imutils.rotate_bound(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

# bytes = img.tobytes()  # 转字节数组  # 或者使用img.tostring()，两者是等价的
  # 注意了：得到的bytes数据并不等价于open(file,"rb")数据

# 把img 对象编码为jpg 格式
success, encoded_image = cv2.imencode(".jpg", rotated)
# 将数组转为bytes
bytes = encoded_image.tobytes()  # 等价于tostring()

b64 = base64.b64encode(bytes).decode('ascii')  # base64字符串

bytes2 = base64.b64decode(b64)  # 编码解码以后是否还正确

with open("密密麻麻_base64.txt", "w") as fp:
    fp.write(b64)

with open("yyyyyyyyyyyyy.jpg", "wb") as fp:
    fp.write(bytes2)  # 成功，我们自已写的 bytes

cv2.imwrite('./ttttttttttttttttttt.jpg', rotated)  # 成功，opencv 保存 img 对象
```



## 卷积

```
import cv2
import numpy as np
  

image = cv2.imdecode(np.fromfile('./cleaned.jpg',dtype=np.uint8), -1)

# 卷积, 只保留水平线
kernel1 = np.array([ [1], [-1] ])
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
  
cv2.imshow('Original', image)
cv2.imshow('conv', img)
  
cv2.waitKey()
```





## PIL、cv2、bytes 图片格式互转换



### 1. PIL 与 cv2 相互转化

```python
import cv2
from PIL import Image
import numpy as np

# PIL 转 cv2
img= Image.open("test.jpg")
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
print(type(img))



# cv2 转 PIL
img = cv2.imread("test.jpg")
img= Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
print(type(img))
```

### 2. PIL 与 bytes 相互转化

```python
'''
    bytes 转 PIL 
'''
# 第一类：转换 本地的bytes图片 为 PIL
with open('test.jpg', 'rb') as f:
    content = f.read()  
local_img = Image.open(BytesIO(content))   
print(type(local_img))  



# 第二类：转换 网络上的bytes图片 为 PIL
url = 'https://z3.ax1x.com/2021/07/13/WAuYJU.jpg'
content = requests.get(url, stream=True).content
net_img = Image.open(BytesIO(content))   # BytesIO实现了在内存中读写Bytes
print(type(net_img))    






'''
    PIL 转 bytes
'''
img_bytes  = BytesIO()
img = Image.open('test.jpg', mode='r')
img.save(img_bytes, format='JPEG')
img_bytes = img_bytes.getvalue()
print(type(img_bytes))  
```



### 3.PIL Base64 互转

```python
import base64
from io import BytesIO

buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())
```



### 4. cv2 与bytes 相互转化

```python
import numpy as np
import cv2


# bytes 转 numpy
img_buffer_numpy = np.frombuffer(img_bytes, dtype=np.uint8)  # 将 图片字节码bytes  转换成一维的numpy数组 到缓存中
img_numpy = cv2.imdecode(img_buffer_numpy, 1)   # 从指定的内存缓存中读取一维numpy数据，并把数据转换(解码)成图像矩阵格式



# numpy 转 bytes
 _, img_encode = cv2.imencode('.jpg', img_numpy)
img_bytes = img_encode.tobytes()
```



#### gpt-4o image

```python
import openai
import json
import time
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

with open("config.json", "r", encoding='UTF-8') as f:
    api_key = json.load(f)["api_key_gpt"]

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

img = Image.open("./images/1.png")
buffered = BytesIO()
img.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

def chat_gpt4(api_key, q, img_b64=None):
    
    prompt = """
    识图片中的日语句子或使用用户提供的日语句子。现在你是一个生活在日本的日本人，你正在教一个中国人学日语。所有日语句子中的语汇和语法作出详细解释，请用简体中文以下面这种格式输出，并且最后以“句子翻译：...” 结束。例如，日语句子 "一応約束したからな。"，要严格案照以下格式输出并且不要漏掉符号">":
  一応約束したからな。
  >1. 一応（いちおう）：这是一个副词，表示"大体上，首先，暂时，总之"等。
  >2. 約束した（やくそくした）：这是一个动词的过去形，"約束する"表示"约定，承诺"。
  >3. からな：这是一个助词，表示原因或理由，"な"在这里增加了一些口语化和亲近感。
  >
  >句子翻译："毕竟我已经答应过了。
    """
    
    messages = [
        { "role": "system","content":prompt},
        { "role": "user","content":[{ "type": "text", "text": f"{q}"}]}
    ]
    
    if img_b64 != None:
        messages[1]['content'].append( { "type":"image_url", "image_url": { "url": f"data:image/jpeg;base64,{img_b64}"} } )
    
    import openai
    openai.api_key = api_key
    stream = openai.chat.completions.create(
        model= "gpt-4o", #"gpt-4",
        messages = messages,
        stream=True,
        timeout=30
    )
    for chunk in stream:
        text = chunk.choices[0].delta.content or ""
        yield text

answer = ''
it = iter(chat_gpt4(api_key, "", img_b64=img_str))
for text in it:
	print(text)
    answer += text

```





### 5. cv2 和 numpy 互转

```
  img = cv2.cvtColor(im, cv2.COLOR_RGB2BGR) # np.asarray(img)
    # numpy 图像默认是 RGB, cv2 是 BGR
    # 它们其实都是 numpy 数组
```





## simple.cs

```

using OpenCvSharp;
using SixLabors.ImageSharp;
using System;
using System.IO;

class Sample
{
    // 边缘检测
    public static void canny()
    {
        // https://blog.csdn.net/zanllp/article/details/79829813
        Mat src = new Mat("1.jpg", ImreadModes.Grayscale);
        Mat dst = new Mat();

        Cv2.Canny(src, dst, 50, 200);
        Cv2.ImWrite("2.jpg", dst);

        Cv2.ImShow("src image", src);
        Cv2.ImShow("dst image", dst);
        Cv2.WaitKey();
        //using (new Window("src image", src))
        //using (new Window("dst image", dst))
        //{
        //    Cv2.WaitKey();
        //}
    }

    // 最小外接矩形
    public static void minAreaRect()
    {
        // https://www.cnblogs.com/little-monkey/p/7429579.html
        Mat src = new Mat("minAreaRect.jpg", ImreadModes.Grayscale);
        Mat dst = src.Clone();
        Cv2.Threshold(src, src, 100, 255, ThresholdTypes.Binary);
        Cv2.ImShow("src binary", src);
        Cv2.WaitKey();
    }


    // 透视变换
    public static void perspectiveTransformation()
    {
        // https://www.cnblogs.com/wj-1314/p/11975977.html
        // https://github.com/LeBron-Jian/ComputerVisionPractice



    }

    // 删除边缘的对象
    public static void deleteBorder()
    {
        // https://answers.opencv.org/question/173768/how-to-delete-those-border-component/

    }

    // 删除边缘的对象
    public static Mat DeleteBorderComponents(Mat src)
    {
        // https://stackoverflow.com/questions/65534370/remove-the-element-attached-to-the-image-border
        using (Mat neg = new Mat())
        using (Mat pad = new Mat())
        {
            Cv2.BitwiseNot(src, neg);  // 反色
            Cv2.CopyMakeBorder(neg, pad, 1, 1, 1, 1, BorderTypes.Constant, 255);  // 上下左右各加一像素
            OpenCvSharp.Size size = pad.Size();
            Mat mask = Mat.Zeros(size.Height + 2, size.Width + 2, MatType.CV_8UC1);  // Mask 图像宽高都比pad 多两像素

            Rect rect_floodfill = new Rect();
            Cv2.FloodFill(pad, mask, new OpenCvSharp.Point(0, 0), 0, out rect_floodfill, 5, 0, FloodFillFlags.Link8);  // 填充

            Mat tmp = pad.Clone(new Rect(2, 2, size.Width - 2, size.Height - 2));  // 宽高前面各加了共两像素，这里减去
            Cv2.BitwiseNot(tmp, tmp);
            return tmp;
        }
    }

    // 二值化
    public static Mat Binarize(Mat src)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat img_binary = new Mat())
        {
            Cv2.Threshold(src, img_binary, 185, 255, ThresholdTypes.Binary); // 二值化
            return img_binary.Clone();
        }
    }

    // 二值化
    public static Mat Binarize(Mat src, double thresh, double maxval)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat img_binary = new Mat())
        {
            Cv2.Threshold(src, img_binary, thresh, maxval, ThresholdTypes.Binary); // 二值化
            return img_binary.Clone();
        }
    }

    // 去除黑边后的矩形区域
    public static Rect DeBoardRect(Mat t)
    {

        Sample sample = new Sample();

        Mat im = Binarize(t);  // 二值化
        im = DeleteBorderComponents(im);  // 删除边缘对象

        im = DeleteSmallComponents(im);  // 删除面积过小的像素点

        // 遍历每一个像素
        //for (int x = 0; x < im.Rows; x++)
        //{
        //    for (int y = 0; y < im.Cols; y++)
        //    {
        //        // Point p(x, y); 第几行第几列
        //        // At(y, x) 第几行第几列
        //        // Rect(X=y, Y=x) 第几列第几行
        //        // 注意这两个传参的顺序是不一样的
        //        int pixel = im.At<Byte>(y, x);

        //        if (pixel == 255)  // 未反色前255 是白色
        //        {
        //            //im.At<Byte>(y, x) = 135;  // 纯白全部变成一个特定的灰色

        //        }
        //    }
        //}

        int X = 0;
        // 从左向右移动，条件是这一整列的像素几乎都是0
        for (int x = 0; x < im.Cols; x++)  // x 代表的是第几列
        {
            double count = 0;

            for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一列有多少个非纯白像素点
                }
            }

            if (count > 0)
            {
                X = x;
                break;
            }

        }


        int X2 = im.Cols;
        // 从右向左移动，条件是这一整列的像素几乎都是0
        for (int x = im.Cols - 1; x >= 0; x--)  // x 代表的是第几列
        {
            double count = 0;

            for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一列有多少个非0 像素点
                }
            }

            if (count > 0.01)
            {
                X2 = x;
                break;
            }

        }


        int Y = 0;
        // 从上向下移动，条件是这一整行的像素几乎都是0
        for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
        {
            double count = 0;

            for (int x = 0; x < im.Cols; x++) // x 代表的是第几列
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一列有多少个非纯白像素点
                }
            }

            if (count > 0)
            {
                Y = y;
                break;
            }
        }


        int Y2 = im.Rows;
        // 从下向上移动，条件是这一整行的像素几乎都是0
        for (int y = im.Rows - 1; y >= 0; y--)  // y 代表的是第几行
        {
            double count = 0;

            for (int x = 0; x < im.Cols; x++) // x 代表的是第几列
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一行有多少个非0 像素点
                }
            }

            if (count > 0)
            {
                Y2 = y;
                break;
            }
        }


        // 宽度 = 有多少列 im.Cols
        // 高度 = 有多少行 im.Rows
        // x in im.Cols 是 第几列
        // y in im.Rows 是 第几行


        if (X >= 60)
        {
            X = X - 60;
        }

        if (X2 + 60 <= im.Cols)
        {
            X2 = X2 + 60;
        }


        if (Y >= 60)
        {
            Y = Y - 60;
        }

        if (Y2 + 60 <= im.Rows)
        {
            Y2 = Y2 + 60;
        }

        var rect = new Rect
        {
            X = X,
            Y = Y,
            Width = im.Cols - (X + (im.Cols - X2)),
            Height = im.Rows - (Y + (im.Rows - Y2))
        };

        return rect;
    }


    // 去除黑边（图片大小可能会改变）
    public static Mat DeBoardAndResize(Mat src, bool autoCut, bool binarize = false, bool autoSize = false, string scale = null)
    {
        Mat img_gray = new Mat();
        Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化

        if (binarize)
        {
            img_gray = Sample.Binarize(img_gray, 200, 255);
        }

        // 找出除掉边框后的区域
        Rect retct = Sample.DeBoardRect(img_gray);

        Mat img_des = null;

        if (scale != null)
        {
            double rate = 2127 / (float)img_gray.Width;  // 2127*3042 扫描仪原图

            if (scale == "缩小25%")
            {
                rate = 0.25;
            }
            else if (scale == "缩小50%")
            {
                rate = 0.5;
            }
            else if (scale == "缩小85%")
            {
                rate = 0.85;
            }
            img_des = img_gray.Resize(new OpenCvSharp.Size(0, 0), rate, rate, InterpolationFlags.Linear);
        }
        else if (autoCut)
        {
            // 自动剪掉白边
            img_des = img_gray.Clone(retct);
        }
        else if (autoSize)
        {
            /*
             自动调整分辨率  
             阿里ocr 支持图片最短边至少15px，最长边最大4096px
             */
            //img_des = img_gray.Clone();
            //if (img_gray.Width >= 3900 )
            //{
            //    img_des = img_gray.Resize(new OpenCvSharp.Size(0, 0), 0.85, 0.85, InterpolationFlags.Linear); // 调整为原尺寸的 0.85 倍
            //}
            //else if (img_gray.Width <= 800)
            //{
            //    img_des = img_gray.Resize(new OpenCvSharp.Size(0, 0), 2, 2, InterpolationFlags.Linear);  // 调整为原尺寸的两倍
            //}

            float rate = 2127 / (float)img_gray.Width;  // 2127*3042 扫描仪原图
            img_des = img_gray.Resize(new OpenCvSharp.Size(0, 0), rate, rate, InterpolationFlags.Linear);

            Rect retct2 = Sample.DeBoardRect(img_des);
            Mat img_des2 = img_des.Clone(retct2);
            img_des.Dispose();
            img_des = img_des2;
        }
        else
        {
            // rect 矩形区域以外全部变白
            img_des = Whited(img_gray, retct);
        }

        img_gray.Dispose();

        return img_des;
    }

    // rect 矩形区域以外全部变白
    public static Mat Whited(Mat t, Rect rect)
    {
        for (int x = 0; x < t.Cols; x++)  // x 第几列
        {
            for (int y = 0; y < t.Rows; y++)  // y 第几行
            {
                bool whiteQ = true;

                if (x >= rect.X && x <= rect.X + rect.Width)
                {
                    if (y >= rect.Y && y <= rect.Y + rect.Height)
                    {
                        whiteQ = false;  // 矩形区域以内的像素保留
                    }
                }

                if (whiteQ)
                {
                    t.At<Byte>(y, x) = 255;   // 矩形区域以外的像素变白
                }

            }
        }

        return t.Clone();
    }

    // 删除过小的对象
    public static Mat DeleteSmallComponents(Mat im)
    {

        // https://qiita.com/kaiyu_tech/items/a37fc929ac0f3328fea1

        Cv2.BitwiseNot(im, im);  // 反色

        var labels = new Mat();
        var stats = new Mat();
        var centroids = new Mat();
        var count = Cv2.ConnectedComponentsWithStats(im, labels, stats, centroids, PixelConnectivity.Connectivity8, MatType.CV_32SC1);

        var indexes = stats.Col((int)ConnectedComponentsTypes.Area).SortIdx(SortFlags.EveryColumn);


        var indexer = stats.GetGenericIndexer<int>();

        var output = im.CvtColor(ColorConversionCodes.GRAY2BGR);


        // 遍历每一个像素
        for (int x = 0; x < im.Rows; x++)
        {
            for (int y = 0; y < im.Cols; y++)
            {

                int label = labels.At<int>(x, y);

                if (label == 0)
                {
                    // 是背景对象，跳过
                    continue;
                }

                var area = indexer[label, (int)ConnectedComponentsTypes.Area];

                var rect = new Rect
                {
                    X = indexer[label, (int)ConnectedComponentsTypes.Left],
                    Y = indexer[label, (int)ConnectedComponentsTypes.Top],
                    Width = indexer[label, (int)ConnectedComponentsTypes.Width],
                    Height = indexer[label, (int)ConnectedComponentsTypes.Height]
                };

                // 所处的连通块面积过小则删除（变成背景色）
                if (area < 20)
                {
                    im.At<Byte>(x, y) = 0;
                }
            }
        }

        // 遍历每一个连通块
        for (int i = 0; i < indexes.Rows - 1; i++)
        {
            var index = indexes.Get<int>(i);

            var area = indexer[index, (int)ConnectedComponentsTypes.Area];

            var rect = new Rect
            {
                X = indexer[index, (int)ConnectedComponentsTypes.Left],
                Y = indexer[index, (int)ConnectedComponentsTypes.Top],
                Width = indexer[index, (int)ConnectedComponentsTypes.Width],
                Height = indexer[index, (int)ConnectedComponentsTypes.Height]
            };

            // 绘制矩形
            if (area < 20)
            {
                output.Rectangle(rect, Scalar.Blue);
            }
            //else
            //{
            //    output.Rectangle(rect, Scalar.Red);
            //}
        }

        Cv2.BitwiseNot(im, im);

        return im;

    }


    public static void convertToGif(byte[] data, string savePath)
    {
        var img = SixLabors.ImageSharp.Image.Load(data);

        img.SaveAsGif(savePath);
    }

    public static void convertToGif(System.Drawing.Bitmap img, string savePath)
    {
        Mat src = OpenCvSharp.Extensions.BitmapConverter.ToMat(img);
        src.SaveImage(savePath);
    }

    // 二值化
    public static string binarize(string filePath)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat src = new Mat(filePath))
        {
            Mat img_binary = new Mat();
            using (Mat img_gray = new Mat())
            using (Mat img_threshold = new Mat())
            {
                Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化 BGR2HSV 
                                                                            //Cv2.CvtColor(src, img_gray, ColorConversionCodes.LRGB2Luv); // 灰度化 BGR2HSV 
                                                                            //Cv2.Threshold(img_gray, img_binary, 250, 255, ThresholdTypes.Binary); // 二值化

                //img_binary = DeleteBorderComponents(img_binary);
                img_binary = DeleteBorderComponents(img_gray);
                //img_binary = DeleteSmallComponents(img_binary);

                using (MemoryStream memoryStream = img_binary.ToMemoryStream())
                {
                    byte[] imageBytes = memoryStream.ToArray();
                    string imgData = Convert.ToBase64String(imageBytes);
                    memoryStream.Dispose();
                    img_binary.Dispose();
                    return imgData;
                }
            }
        }

    }


    // 预处理
    public static string prepare(string filePath)
    {

        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat src = Cv2.ImRead(filePath, ImreadModes.Color))
        {

            Mat img_gray = new Mat();
            Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化

            // 找出除掉边框后的区域
            Rect retct = DeBoardRect(img_gray);

            // rect 矩形区域以外全部变白
            //Mat src2 = Whited(img_gray, retct);

            Mat src2 = img_gray.Clone(retct);

            //Cv2.ImWrite(@"D:\workcode\csharp\noboard__src.jpg", src2);
            Cv2.ImWrite(filePath, src2);


            using (MemoryStream memoryStream = src2.ToMemoryStream())
            {
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                memoryStream.Dispose();
                img_gray.Dispose();
                return imgData;
            }
        }

    }


    /// <summary>
    /// 截图
    /// </summary>
    /// <param name="path"></param>
    /// <param name="x"></param>
    /// <param name="y"></param>
    /// <param name="w"></param>
    /// <param name="h"></param>
    /// <param name="rx"></param>
    /// <param name="ry"></param>
    /// <param name="rw"></param>
    /// <param name="rh"></param>
    /// <returns></returns>
    public static string cutImage(string path, int x, int y, int w, int h, int rx, int ry, int rw, int rh)
    {
        using (Mat img = new Mat(path))
        {

            if (x < 0)
            {
                x = 0;
            }
            if (x + w >= img.Width)
            {
                w = img.Width - x - 1;
            }
            if (y < 0)
            {
                y = 0;
            }
            if (y + h >= img.Height)
            {
                h = img.Height - y - 1;
            }
            var rect = new Rect(x, y, w, h);
            var minImg = img[rect];

            //Mat dist = new Mat();
            //Cv2.BitwiseNot(minImg, dist);

            //Cv2.Threshold(minImg, dist, 50, 255, ThresholdTypes.Binary);

            //Cv2.Rectangle(minImg, new Rect(rx, ry, rw, rh), Scalar.Red, 2);
            using (var memoryStream = minImg.ToMemoryStream(".png"))
            {
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                memoryStream.Dispose();
                img.Dispose();
                minImg.Dispose();
                //dist.Dispose();
                return imgData;
            }
        }
    }


    /// <summary>
    /// 旋转图像
    /// </summary>
    /// <param name="src"></param>
    /// <param name="angle"></param>
    /// <returns></returns>
    public static Mat matRotate(Mat src, float angle)
    {
        Mat dst = new Mat();
        Point2f center = new Point2f(src.Cols / 2, src.Rows / 2);
        Mat rot = Cv2.GetRotationMatrix2D(center, angle, 1);
        Size2f s2f = new Size2f(src.Size().Width, src.Size().Height);
        Rect box = new RotatedRect(new Point2f(0, 0), s2f, angle).BoundingRect();
        double xx = rot.At<double>(0, 2) + box.Width / 2 - src.Cols / 2;
        double zz = rot.At<double>(1, 2) + box.Height / 2 - src.Rows / 2;
        rot.Set(0, 2, xx);
        rot.Set(1, 2, zz);
        Cv2.WarpAffine(src, dst, rot, box.Size);
        rot.Dispose();
        return dst;
    }

    /// <summary>
    /// 旋转图像(优化旋转后模糊的问题)
    /// </summary>
    /// <param name="src"></param>
    /// <param name="angle"></param>
    public static Mat matRotate2(Mat src, float angle)
    {
        //using (Mat src = Cv2.ImRead("D:\\rotate_src.jpg"))
        Mat dst = new Mat();

        var centreX = Math.Floor( (Double)(src.Cols / 2) );
        var centreY = Math.Floor( (Double)(src.Rows / 2) );

        Point2f center = new Point2f((float)centreX, (float)centreY);
        Mat rotationMatrix = Cv2.GetRotationMatrix2D(center, angle, 1);  // 计算旋转矩阵
        var cosofRotationMatrix = Math.Abs(rotationMatrix.At<double>(0, 0) );
        var sinofRotationMatrix = Math.Abs(rotationMatrix.At<double>(0, 1) );

        // 计算旋转后新图片的宽度
        var newImageHeight = Math.Floor((src.Height * sinofRotationMatrix) +
              (src.Width * cosofRotationMatrix));

        var newImageWidth = Math.Floor((src.Height * cosofRotationMatrix) +
              (src.Width * sinofRotationMatrix));

        // 更新旋转矩阵
        rotationMatrix.At<double>(0, 2) += (newImageWidth / 2) - centreX;
        rotationMatrix.At<double>(1, 2) += (newImageHeight / 2) - centreY;

        // 执行实际旋转
        Cv2.WarpAffine(src, dst, rotationMatrix, new OpenCvSharp.Size(newImageWidth, newImageHeight));


        // 重设新图片宽度，让它和源图片的宽度保持一至
        Mat dst2 = new Mat();
        Cv2.Resize(dst, dst2, new OpenCvSharp.Size(src.Width, src.Height), 0, 0, InterpolationFlags.Nearest);

        //Cv2.ImWrite("D:\\rotate_dst.jpg", dst2);

        rotationMatrix.Dispose();
        dst.Dispose();

        return dst2;
    }


    /// <summary>
    /// 图片转格式
    /// </summary>
    /// <param name="src"></param>
    /// <param name="dist"></param>
    public static void convertImageFormat(string src, string dist)
    {
        using (Mat img = new Mat(src))
        {
            img.SaveImage(dist);
            img.Dispose();
        }
    }

    public static string ocrInit(string filePath)
    {
        using (Mat src = new Mat(filePath, ImreadModes.Grayscale))
        {
            //1.Sobel算子，x方向求梯度
            Mat sobel = new Mat();
            Cv2.Sobel(src, sobel, MatType.CV_8U, 1, 0, 3);

            //2.二值化
            Mat binary = new Mat();
            Cv2.Threshold(sobel, binary, 0, 255, ThresholdTypes.Otsu | ThresholdTypes.Binary);

            //3. 膨胀和腐蚀操作的核函数
            Mat element1 = new Mat();
            Mat element2 = new Mat();
            OpenCvSharp.Size size1 = new OpenCvSharp.Size(30, 9);
            OpenCvSharp.Size size2 = new OpenCvSharp.Size(24, 6);

            element1 = Cv2.GetStructuringElement(MorphShapes.Rect, size1);
            element2 = Cv2.GetStructuringElement(MorphShapes.Rect, size2);

            //4. 膨胀一次，让轮廓突出
            Mat dilation = new Mat();
            Cv2.Dilate(binary, dilation, element2);

            //5. 腐蚀一次，去掉细节，如表格线等。注意这里去掉的是竖直的线
            Mat erosion = new Mat();
            Cv2.Erode(dilation, erosion, element1);

            Mat dilation2 = new Mat();
            Cv2.Dilate(binary, dilation2, element2);
            //6. 再次膨胀，让轮廓明显一些
            Cv2.Dilate(erosion, dilation2, element2, null, 3);

            using (MemoryStream memoryStream = binary.ToMemoryStream())
            {
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                return imgData;
            }

        }
    }

    public static System.Drawing.Image test(string src)
    {
        using (Mat img = new Mat(src))
        {

            //Mat dist = new Mat();
            //Cv2.BitwiseNot(minImg, dist);

            Mat dist = new Mat();
            Mat hd = new Mat();
            Cv2.CvtColor(img, hd, ColorConversionCodes.BGR2GRAY); // 灰度化 BGR2HSV 

            Cv2.Threshold(hd, dist, 130, 255, ThresholdTypes.Binary);

            var result = System.Drawing.Image.FromStream(dist.ToMemoryStream());

            dist.Dispose();

            return result;
        }
    }

}

```



### util.cs

```
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.RegularExpressions;

namespace ocrClient
{
    class util
    {
        /// <summary>
        /// 无损压缩图片
        /// </summary>
        /// <param name="sFile">原图片地址</param>
        /// <param name="dFile">压缩后保存图片地址</param>
        /// <param name="flag">压缩质量（数字越小压缩率越高）1-100</param>
        /// <param name="size">压缩后图片的最大大小</param>
        /// <param name="sfsc">是否是第一次调用</param>
        public static bool CompressImage(string sFile, string dFile, int flag = 90, int size = 300, bool sfsc = true)
        {
            //如果是第一次调用，原始图像的大小小于要压缩的大小，则直接复制文件，并且返回true
            FileInfo firstFileInfo = new FileInfo(sFile);
            if (sfsc == true && firstFileInfo.Length < size * 1024)
            {
                firstFileInfo.CopyTo(dFile);
                return true;
            }
            Image iSource = Image.FromFile(sFile);
            ImageFormat tFormat = iSource.RawFormat;

            Bitmap ob = new Bitmap(iSource.Width, iSource.Height);

            Graphics g = Graphics.FromImage(ob);
            g.Clear(Color.White);
            g.CompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
            g.DrawImage(iSource, new Rectangle(0, 0, iSource.Width, iSource.Height), 0, 0, iSource.Width, iSource.Height, GraphicsUnit.Pixel);
            g.Dispose();

            //设置压缩质量
            EncoderParameters ep = new EncoderParameters();
            ep.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, new long[1] { flag });

            try
            {
                //找到系统中可用的图片编码器信息
                ImageCodecInfo[] arrayICI = ImageCodecInfo.GetImageEncoders();
                ImageCodecInfo jpegICIinfo = null;
                for (int x = 0; x < arrayICI.Length; x++)
                {
                    if (arrayICI[x].FormatID == ImageFormat.Jpeg.Guid)
                    {
                        jpegICIinfo = arrayICI[x];
                        break;
                    }
                }
                //如果编码器存在的，可以压缩
                if (jpegICIinfo != null)
                {
                    ob.Save(dFile, jpegICIinfo, ep);
                    FileInfo fi = new FileInfo(dFile);
                    if (fi.Length > 1024 * size)
                    {
                        flag -= 10;
                        CompressImage(sFile, dFile, flag, size, false);
                    }
                }
                else
                {
                    ob.Save(dFile, tFormat);
                }
                return true;
            }
            catch
            {
                return false;
            }
            finally
            {
                iSource.Dispose();
                ob.Dispose();
            }
        }


        public static bool CompressImage(string path, string outPath)
        {
            try
            {
                Bitmap img = new Bitmap(path);

                Bitmap newImg = new Bitmap(img.Width, img.Height);
                Graphics g = Graphics.FromImage(newImg);

                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                g.PixelOffsetMode = System.Drawing.Drawing2D.PixelOffsetMode.HighQuality;
                g.DrawImage(img, 0, 0, img.Width, img.Height);

                newImg.Save(outPath, ImageFormat.Jpeg);
                g.Dispose();
                newImg.Dispose();
                img.Dispose();
            }
            catch (Exception)
            {
                File.Copy(path, outPath);
            }
            return true;

        }

        /// <summary>
        /// MD5
        /// </summary>
        /// <param name="txt"></param>
        /// <returns></returns>
        public static string md5(string txt)
        {
            using (MD5 mi = MD5.Create())
            {
                byte[] buffer = Encoding.Default.GetBytes(txt);
                //开始加密
                byte[] newBuffer = mi.ComputeHash(buffer);
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < newBuffer.Length; i++)
                {
                    sb.Append(newBuffer[i].ToString("x2"));
                }
                return sb.ToString();
            }
        }

        /// <summary>
        /// base64转图片
        /// </summary>
        /// <param name="base64String"></param>
        /// <returns></returns>
        public static Image convertBase64ToImage(string base64String)
        {
            byte[] imageBytes = Convert.FromBase64String(base64String);
            using (MemoryStream ms = new MemoryStream(imageBytes, 0, imageBytes.Length))
            {
                ms.Write(imageBytes, 0, imageBytes.Length);
                return Image.FromStream(ms, true);
            }
        }

        /// <summary>
        /// base64转图片
        /// </summary>
        /// <param name="base64String"></param>
        /// <returns></returns>
        public static byte[] convertBase64ToImageBytes(string base64String)
        {
            byte[] imageBytes = Convert.FromBase64String(base64String);
            return imageBytes;
        }


        /// <summary>
        ///  计算指定文件的MD5值
        /// </summary>
        /// <param name="fileName">指定文件的完全限定名称</param>
        /// <returns>返回值的字符串形式</returns>
        public static string getFileMd5(string fileName)
        {
            string hashMD5 = string.Empty;
            //检查文件是否存在，如果文件存在则进行计算，否则返回空值
            if (System.IO.File.Exists(fileName))
            {
                using (System.IO.FileStream fs = new System.IO.FileStream(fileName, System.IO.FileMode.Open, System.IO.FileAccess.Read))
                {
                    //计算文件的MD5值
                    System.Security.Cryptography.MD5 calculator = System.Security.Cryptography.MD5.Create();
                    Byte[] buffer = calculator.ComputeHash(fs);
                    calculator.Clear();
                    //将字节数组转换成十六进制的字符串形式
                    StringBuilder stringBuilder = new StringBuilder();
                    for (int i = 0; i < buffer.Length; i++)
                    {
                        stringBuilder.Append(buffer[i].ToString("x2"));
                    }
                    hashMD5 = stringBuilder.ToString();
                    fs.Dispose();
                }//关闭文件流
            }//结束计算
            return hashMD5;
        }

        /// <summary>
        /// 图片转base64
        /// </summary>
        /// <param name="img"></param>
        /// <returns></returns>
        public static string imgToBase64(Image img)
        {


            using (MemoryStream memoryStream = new MemoryStream())
            {
                img.Save(memoryStream, img.RawFormat);
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                return imgData;
            }
        }

        /// <summary>
        /// 图片转base64
        /// </summary>
        /// <param name="img"></param>
        /// <returns></returns>
        public static string imgToBase64(Bitmap img, ImageFormat format)
        {
            using (MemoryStream memoryStream = new MemoryStream())
            {
                img.Save(memoryStream, format);

                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                return imgData;
            }
        }

        /// <summary>
        /// 缩放图片
        /// </summary>
        /// <param name="objPic"></param>
        /// <param name="strNewPic"></param>
        /// <param name="intWidth"></param>
        /// <returns></returns>
        public static Image smallPic(Image objPic, int intWidth)
        {

            Bitmap objNewPic;
            try
            {
                int intHeight = (intWidth / objPic.Width) * objPic.Height;
                objNewPic = new System.Drawing.Bitmap(objPic, intWidth, intHeight);
            }
            catch (Exception exp) { throw exp; }
            finally
            {
                objPic = null;
                objNewPic = null;
            }
            return objPic;
        }


        /// <summary>
        /// 全角转半角
        /// </summary>
        /// <param name="input"></param>
        /// <returns></returns>
        public static string toDBC(string input)
        {
            Regex qj = new Regex("[，.？＠＃％＾！：；．”“［］ ]");
            char[] c = input.ToCharArray();
            for (int i = 0; i < c.Length; i++)
            {
                if (qj.IsMatch(c[i].ToString()))
                {
                    continue;
                }
                if (c[i] == 12288)
                {
                    c[i] = (char)32;
                    continue;
                }
                if (c[i] > 65280 && c[i] < 65375)
                    c[i] = (char)(c[i] - 65248);
            }
            return new String(c);
        }


        /// <summary>
        /// 以逆时针为方向对图像进行旋转
        /// </summary>
        /// <param name="b">位图流</param>
        /// <param name="angle">旋转角度[0,360](前台给的)</param>
        /// <returns></returns>
        public static Bitmap Rotate(Bitmap b, int angle)
        {
            angle = angle % 360;
            //弧度转换
            double radian = angle * Math.PI / 180.0;
            double cos = Math.Cos(radian);
            double sin = Math.Sin(radian);
            //原图的宽和高
            int w = b.Width;
            int h = b.Height;
            int W = (int)(Math.Max(Math.Abs(w * cos - h * sin), Math.Abs(w * cos + h * sin)));
            int H = (int)(Math.Max(Math.Abs(w * sin - h * cos), Math.Abs(w * sin + h * cos)));
            //目标位图
            Bitmap dsImage = new Bitmap(W, H);
            System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(dsImage);
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.Bilinear;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            //计算偏移量
            Point Offset = new Point((W - w) / 2, (H - h) / 2);
            //构造图像显示区域：让图像的中心与窗口的中心点一致
            Rectangle rect = new Rectangle(Offset.X, Offset.Y, w, h);
            Point center = new Point(rect.X + rect.Width / 2, rect.Y + rect.Height / 2);
            g.TranslateTransform(center.X, center.Y);
            g.RotateTransform(360 - angle);
            //恢复图像在水平和垂直方向的平移
            g.TranslateTransform(-center.X, -center.Y);
            g.DrawImage(b, rect);
            //重至绘图的所有变换
            g.ResetTransform();
            g.Save();
            g.Dispose();
            //dsImage.Save("cd.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
            return dsImage;
        }

    }
}

```







## OpenCV 直线检测

- https://gist.github.com/darkedges/a4f30eb1233ad17007a18dd7372b5b5c



### 面对直线，你说霍夫线变换是万能的吗



```

"""
https://mp.weixin.qq.com/s?__biz=MzA4ODgyMDg0MQ==&mid=100001057&idx=1&sn=ebfd3cf30ffb3a48909bd309fa59f82d&chksm=1025182727529131c5c63d02663bfc517b89c23f4884c4d49334fee27d12947b792e9b36643f#rd
面对直线，你说霍夫线变换是万能的吗

https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/?ref=gcse

doc\lang\programming\opencv summary.md

"""

import numpy as np
import cv2

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':

    imgData = np.fromfile('./填空题.png', dtype=np.uint8)
    img_origin = cv2.imdecode(imgData, -1)
    img_rgb = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGRA2RGB)

    # 转灰度图
    img_gray = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGR2GRAY)   #cv2.COLOR_RGB2BGR
    print(type(img_gray))

    w = img_gray.shape[0]  # w,h 反了这里，可能是将错就错后面才看起来对
    h = img_gray.shape[1]

    # slice 子矩阵，既剪裁图像
    img_crop = img_gray[0:w-30, 0:h-70]

    # 二值化
    ret, img_binary = cv2.threshold(img_crop, 92, 255, cv2.THRESH_BINARY_INV)
    # imshow("1:二值操作", binaryImage)

    # 开操作(将文字这些密集的“孔洞”给腐蚀掉，仅留下直线)
    rect_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (20, 2))  # 定义了20*2 大小的矩形核
    img_opening = cv2.morphologyEx(img_binary, cv2.MORPH_OPEN, rect_kernel)

    # 膨胀加粗
    rect_kernel2 = cv2.getStructuringElement(
        cv2.MORPH_RECT, (3, 3))  # 定义了20*2 大小的矩形核
    img_dilate = cv2.dilate(img_opening, rect_kernel2)

    #edges = cv2.Canny(img_dilate,50,150,apertureSize=3)


    # Apply HoughLinesP method to
    # to directly obtain line end points
    lines = cv2.HoughLinesP(
        img_dilate,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi/180,  # Angle resolution in radians
        threshold=30,  # Min number of votes for valid line
        minLineLength=20,  # Min allowed length of line
        maxLineGap=0  # Max allowed gap between line for joining them
        )

    #img_color = cv2.cvtColor(img_origin, cv2.COLOR_BGR2RGB)


    for points in lines:
      # Extracted points nested in the list
      x1,y1,x2,y2=points[0]
      # Draw the lines joing the points
      # On the original image
      #cv2.line(img_origin, (x1,y1),(x2,y2),(0,0,255, 255), 2)  # 原图是四通道的BGRA(蓝绿红 + alpha 透明度)
      cv2.line(img_rgb, (x1,y1),(x2,y2),(0,0,255), 2)  # 看来无论原图怎么样，cv2 的三个通道顺序永远都是: BGR
      

    cv2.imshow("origin", img_origin)
    cv2.imshow("croped", img_crop)
    cv2.imshow("binary", img_binary)
    cv2.imshow("opening", img_opening)
    cv2.imshow("dilate", img_dilate)  
    cv2.imshow("result", img_rgb)

    cv2.waitKey(0)



    """

cpp origin


# include <iostream>
# include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
  Mat srcImage, dstImage, binaryImage;
  srcImage = imread("原图.png",0);  
  imshow("原图", srcImage);
  
  waitKey(0);
  return 0;
}

 //剪裁图片
  Mat roiImage = srcImage(Rect(0, 0, srcImage.cols - 70, srcImage.rows - 30));
  imshow("0:抠图操作", roiImage);

    //对图像进行二值化
  threshold(roiImage, binaryImage, 92, 255, THRESH_BINARY_INV );
  imshow("1:二值操作", binaryImage);


  Mat morhpImage;
  Mat kernel = getStructuringElement(MORPH_RECT, Size(20, 2), Point(-1, -1));//自定义一个核
  morphologyEx(binaryImage, morhpImage, MORPH_OPEN, kernel, Point(-1, -1));//开操作
  imshow("2:开操作", morhpImage);


  Mat dilateImage;
  kernel = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));
  dilate(morhpImage, dilateImage, kernel);
  imshow("3:膨胀操作", dilateImage);

  
  vector<Vec4i> lines;
  HoughLinesP(dilateImage, lines, 1, CV_PI / 180.0, 30, 20.0, 0);
  dstImage = srcImage.clone();
  cvtColor(dstImage, dstImage, COLOR_GRAY2BGR);
  for (size_t t = 0; t < lines.size(); t++) {
    Vec4i ln = lines[t];
    line(dstImage, Point(ln[0], ln[1]), Point(ln[2], ln[3]), Scalar(0, 0, 255), 2, 8, 0);
  }
  imshow("4:绘制直线", dstImage);

    """


```



### pokemon detector

- https://gist.github.com/darkedges/a4f30eb1233ad17007a18dd7372b5b5c
- https://wolframlanguagereviews.org/

<img src="Python 3  Summary.assets/image-20220325085646084.png" alt="image-20220325085646084" style="zoom:25%;" />

```
# pokemondetector.py

#!/usr/bin/env python

# http://wolframlanguagereviews.org/2018/10/21/pokemon-card-detector/

import numpy as np
import cv2
from collections import defaultdict
import sys
from matplotlib import pyplot as plt


def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect


def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped


def segment_by_angle_kmeans(lines, k=2, **kwargs):
    """
    Group lines by their angle using k-means clustering.

    Code from here:
    https://stackoverflow.com/a/46572063/1755401
    """

    # Define criteria = (type, max_iter, epsilon)
    default_criteria_type = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
    criteria = kwargs.get('criteria', (default_criteria_type, 10, 1.0))

    flags = kwargs.get('flags', cv2.KMEANS_RANDOM_CENTERS)
    attempts = kwargs.get('attempts', 10)

    # Get angles in [0, pi] radians
    angles = np.array([line[0][1] for line in lines])

    # Multiply the angles by two and find coordinates of that angle on the Unit Circle
    pts = np.array([[np.cos(2*angle), np.sin(2*angle)]
                   for angle in angles], dtype=np.float32)

    # Run k-means
    if sys.version_info[0] == 2:
        # python 2.x
        ret, labels, centers = cv2.kmeans(pts, k, criteria, attempts, flags)
    else:
        # python 3.x, syntax has changed.
        labels, centers = cv2.kmeans(
            pts, k, None, criteria, attempts, flags)[1:]

    labels = labels.reshape(-1)  # Transpose to row vector

    # Segment lines based on their label of 0 or 1
    segmented = defaultdict(list)
    for i, line in zip(range(len(lines)), lines):
        segmented[labels[i]].append(line)

    segmented = list(segmented.values())

    return segmented


def intersection(line1, line2):
    """
    Find the intersection of two lines 
    specified in Hesse normal form.

    Returns closest integer pixel locations.

    See here:
    https://stackoverflow.com/a/383527/5087436
    """

    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    A = np.array([[np.cos(theta1), np.sin(theta1)],
                  [np.cos(theta2), np.sin(theta2)]])
    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))

    return [[x0, y0]]


def segmented_intersections(lines):
    """
    Find the intersection between groups of lines.
    """

    intersections = []
    for i, group in enumerate(lines[:-1]):
        for next_group in lines[i+1:]:
            for line1 in group:
                for line2 in next_group:
                    intersections.append(intersection(line1, line2))

    return intersections


def drawLines(img, lines, color=(255, 0, 0)):
    """
    Draw lines on an image
    """
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(img, (x1, y1), (x2, y2), color, 1)


def detect_edge(img):
    img_blurred = cv2.GaussianBlur(img, (5, 5), 0)
    canny = cv2.Canny(img_blurred, 100, 200, None, 3)
    return canny


img = cv2.imread('pokemon.png')[:, :, ::-1]
# cv2.imshow("original image", img)
# cv2.waitKey()

edged = detect_edge(img.copy())
# cv2.imshow("edge detection", edged)
# cv2.waitKey()

contours, hierarchy = cv2.findContours(
    edged, cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

img_w, img_h = np.shape(img)[:2]
CARD_MIN_AREA = (img_w * img_h) * .35
img2 = np.zeros((img_w, img_h, 3), dtype=np.uint8)
img4 = np.zeros((img_w, img_h, 3), dtype=np.uint8)

largest_item = sorted_contours[0]
hull = cv2.convexHull(largest_item)
size = cv2.contourArea(hull)
epsilon = 0.1*cv2.arcLength(hull, True)
peri = cv2.arcLength(hull, True)
approx = cv2.approxPolyDP(hull, epsilon, True)
if ((size > CARD_MIN_AREA) and (4 <= len(approx) <= 5)):
    cv2.drawContours(img2, [hull], -1, (255, 255, 255), 1)

grayimg = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
# cv2.imshow("filtered edges", grayimg)
# cv2.waitKey()

lines = cv2.HoughLines(grayimg, 1, np.pi/83, 73)

# Draw all Hough lines in red
img_with_all_lines = np.copy(img)
drawLines(img_with_all_lines, lines)
# cv2.imshow("Hough lines", img_with_all_lines)
# cv2.waitKey()

# Cluster line angles into 2 groups (vertical and horizontal)
segmented = segment_by_angle_kmeans(lines, 2)

# Find the intersections of each vertical line with each horizontal line
intersections = segmented_intersections(segmented)

img_with_segmented_lines = np.copy(img)

# https://pastiebin.com/5f36425b7ae3d
# Draw intersection points in magenta
for point in intersections:
    pt = (point[0][0], point[0][1])
    img_with_segmented_lines = cv2.circle(
        img_with_segmented_lines, pt, 3, (255, 0, 0), -1)
# cv2.imshow("Segmented lines", img_with_segmented_lines)
# cv2.waitKey()

src_pts = np.array([intersections[0], intersections[1],
                   intersections[2], intersections[3]], dtype=np.int32)
warped = four_point_transform(img, src_pts.reshape(4, 2))
# cv2.imshow("Perpesctive transform", warped)
# cv2.waitKey()

titles = ['Original Image', 'Edge Detection', 'Filtered Edges',
          'Hough Lines', 'Segmented Lines', 'Perspective Transform']
images = [img, edged, grayimg, img_with_all_lines,
          img_with_segmented_lines, warped]
for i in range(len(titles)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
```







## OpenCV 透视变换

- https://mp.weixin.qq.com/s?__biz=MzA4ODgyMDg0MQ==&mid=100001057&idx=1&sn=ebfd3cf30ffb3a48909bd309fa59f82d&chksm=1025182727529131c5c63d02663bfc517b89c23f4884c4d49334fee27d12947b792e9b36643f#rd
  - 面对直线，你说霍夫线变换是万能的吗？周旋机器视觉

- https://blog.csdn.net/qq_41821678/article/details/106851010

- https://zhuanlan.zhihu.com/p/387408410
  - awesome

- https://blog.csdn.net/wsp_1138886114/article/details/83374333
  - 基于傅里叶变换图像矫正



## ppcor_aliocr_convert.py

```python
# aliocr_results_2w\all_data\ppcor_aliocr_convert.py

"""

PPOCRLabel --lang ch  # 启动标注工具

cp autodl-tmp/train_data.zip . && \
unzip train_data.zip -d PaddleOCR

# https://github.com/PaddlePaddle/PaddleOCR/blob/static/doc/doc_ch/FAQ.md

# 7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on data.7z data/

新建文件夹 train_data, 要标注的图片全部放在里面

新建 train_data/Label.txt 内容如下
行中用 \t 分隔 , points 的标记顺序是 左上 右上  右下 左下
train_data/0093.bmp	[{"transcription":"参考答案及解析","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]
train_data/0094.bmp	[{"transcription":"其他内容","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]


给 PaddleOCR 用，前面是坐标和图片都变换；这里图像不变，坐标不变


将阿里OCR 的识别结果（图片和标注）转换成 icdar2015 格式 (注意：它的文本是含 utf8 bom 的)

给 mmocr 训练用。格式是 icdar2015 的格式，文件夹的组织方式是按照 mmocr 的要求创建的

"""


"""

! unzip ./GD500.zip -d DB/datasets

icdar2015 文本检测数据集
标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text

其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。

# 表示text难以辨认。
"""

import random
from pathlib import Path
import os
import shutil
import glob
import base64
from importlib.resources import path
import math
import numpy as np
import cv2
import json
import decimal
import datetime
from pickletools import uint8
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)


def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()


def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json


def parse(s):
    return json.loads(s, strict=False)

# convert dict to string


def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


def transform(points, M):
    # points 算出四个点变换后移动到哪里了
    # points = np.array([[word_x,  word_y],              # 左上
    #                    [word_x + word_width, word_y],                 # 右上
    #                    [word_x + word_width, word_y + word_height],  # 右下
    #                    [word_x, word_y + word_height],  # 左下
    #                    ])
    # add ones
    ones = np.ones(shape=(len(points), 1))

    points_ones = np.hstack([points, ones])

    # transform points
    transformed_points = M.dot(points_ones.T).T

    transformed_points_int = np.round(
        transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

    return transformed_points_int


def cutPoly(img, pts):
    # img = cv2.imdecode(np.fromfile('./t.png', dtype=np.uint8), -1)
    # pts = np.array([[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]])

    # (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y+h, x:x+w].copy()

    # (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    # (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    # (4) add the white background
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst

    # cv2.imwrite("croped.png", croped)
    # cv2.imwrite("mask.png", mask)
    # cv2.imwrite("dst.png", dst)
    # cv2.imwrite("dst2.png", dst2)

    return dst2


if __name__ == "__main__":

    root = 'train_data'
    tmp = 'tmp'
    label_path = os.path.join(root, 'Label.txt')
    
    key_path = os.path.join(root, 'keys.txt')

    fileState_path = os.path.join(root, 'fileState.txt')

    if os.path.exists(root):
        shutil.rmtree(root)
        # os.rmdir(root)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)

    if not os.path.exists(root):
        os.makedirs(root)

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    label = ''
    keys = ''
    states = ''


    dic_words = {}  # 所有词

    # 开始转换

    # https://help.aliyun.com/document_detail/294540.html 阿里云ocr结果字段定义
    # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换

    dir_json = './data/json'  # '/yingedu/www/ocr_server/data/json'
    dir_img = './data/img'  # '/yingedu/www/ocr_server/data/img'

    g_count = 1
    g_count2 = 1


    json_paths = glob.glob('{}/*.json'.format(dir_json), recursive=False)

    for json_path in json_paths:

        arr = []

        base = Path(json_path).stem

        # if base == '0bf0383ece9a533683e615bf57525812':
        #     continue

        img_path = os.path.join(dir_img, '{}.txt'.format(base))

        if not os.path.exists(img_path):  # 没有相应的图片，可能被删除了
            print(f'Warnnig: no image {img_path}')
            continue

        jsn = load_json(json_path)

        if not ('prism_wordsInfo' in jsn):
            print(f'Warning: no charater in {img_path}')
            continue

        with open(img_path, "r", encoding="utf-8") as fp:
            imgdata = fp.read()
            imgdata = base64.b64decode(imgdata)
            imgdata = np.frombuffer(imgdata, np.uint8)
            img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)

            # cv2.imshow('img', img)
            # cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # DBNet 原版只能处理彩图，这里转一下

        else:
            img_color = img.copy()

        img_color_origin = img_color.copy()
        img_color_origin2 = img_color.copy()

        name = f'{g_count}.jpg'
        dst_img_path = f'{root}/{name}'
        states += f'G:\\train_data\\{name}\t1\n'
        g_count += 1

        cv2.imwrite(dst_img_path, img)

        wordsInfo = jsn['prism_wordsInfo']
        for j in range(len(wordsInfo)):
            jo = wordsInfo[j]
            word = jo["word"]

            for w in list(word):
                if not (w in dic_words):
                    dic_words[w] = True

            # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换
            angle = jo['angle']

            img_color = img_color_origin.copy()

            word_x = jo['x']
            word_y = jo['y']
            word_width = jo['width']
            word_height = jo['height']

            if abs(angle) == 90 or abs(angle) == 270:
                word_width = jo['height']
                word_height = jo['width']
            elif angle != 0:

                # 变换前画出绿框，方便追踪点的前后变化
                # img_color = cv2.rectangle(img_color, (word_x, word_y), (
                #     word_x + word_width, word_y + word_height), (0, 255, 0), 2)  # 矩形的左上角, 矩形的右下角

                # cv2.imshow("green", img_color)
                # cv2.waitKey(0)

                # 变换前的多边形蓝框
                points = np.array([
                    [word_x,  word_y],                             # 左上
                    [word_x + word_width, word_y],                 # 右上
                    [word_x + word_width, word_y + word_height],  # 右下
                    [word_x, word_y + word_height],                # 左下
                ])

                # # cv2.fillPoly(img_color, pts=[points], color=(255, 0, 0)) # 填充
                # cv2.polylines(img_color, [points], isClosed=True, color=(
                #     255, 0, 0), thickness=1)  # 只画线，不填充

                # cv2.imshow("polys", img_color)
                # cv2.waitKey(0)

                # 获取图像的维度，并计算中心
                (h, w) = img_color.shape[:2]
                (cX, cY) = (w // 2, h // 2)

                # - (cX,cY): 旋转的中心点坐标
                # - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
                # - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
                # 1° = π/180弧度   1 弧度 =  180 / 3.1415926   // 0.0190033 是Mathematica 算出来的弧度，先转换成角度  // -0.0190033 * (180 / 3.1415926)
                M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
                img_color = cv2.warpAffine(img_color, M, (w, h))
                img_color_transform = img_color.copy()

                # cv2.imshow("after trans", img_color)
                # cv2.waitKey(0)

                # https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html  # 原理
                # https://stackoverflow.com/questions/30327659/how-can-i-remap-a-point-after-an-image-rotation # How can I remap a point after an image rotation?
                # 如何得到移动后的坐标点

                # points 算出四个点变换后移动到哪里了
                points = np.array([[word_x,  word_y],              # 左上
                                   # 右上
                                   [word_x + word_width, word_y],
                                   [word_x + word_width, word_y + \
                                       word_height],  # 右下
                                   [word_x, word_y + word_height],  # 左下
                                   ])
                # add ones
                ones = np.ones(shape=(len(points), 1))

                points_ones = np.hstack([points, ones])

                # transform points
                transformed_points = M.dot(points_ones.T).T

                transformed_points_int = np.round(
                    transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

                # cv2.polylines(img_color, [transformed_points_int], isClosed=True, color=(
                #     0, 0, 255), thickness=2)  # 画转换后的点

                # cv2.polylines(img_color_origin, [points], isClosed=True, color=(
                #     random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

                # cv2.imshow("orgin", img_color_origin)
                # cv2.waitKey(0)

            # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确（错，经验证不需要）
            pos = jo["pos"]
            x = int(pos[0]["x"])  # 左上
            y = int(pos[0]["y"])

            x2 = int(pos[2]["x"])  # 右下
            y2 = int(pos[2]["y"])

            lu = [pos[0]['x'], pos[0]['y']]  # left up  四个角顺时针方向数
            ru = [pos[1]['x'], pos[1]['y']]
            rd = [pos[2]['x'], pos[2]['y']]
            ld = [pos[3]['x'], pos[3]['y']]

            # 生成 icdar2015 格式的人工标记训练数据（用于训练 mmocr）
            # gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(lu[0], lu[1], ru[0], ru[1], rd[0], rd[1], ld[0], ld[1], word) )

            # 绘制矩形
            start_point = (x, y)  # 矩形的左上角

            end_point = (x2, y2)  # 矩形的右下角

            color = (0, 0, 255)  # BGR

            thickness = 2

            # 逐行画框
            # img_color_origin2 = cv2.rectangle(img_color_origin2, start_point, end_point, color, thickness)
            # cv2.imshow("box", img_color_origin2)

            # cv2.waitKey(0)

            points = [lu, ru, rd, ld]

            points0 = np.array([[word_x,  word_y],              # 左上
                                  # 右上
                                  [word_x + word_width, word_y],
                                    [word_x + word_width, word_y + \
                                     word_height],  # 右下
                                    [word_x, word_y + word_height],  # 左下
                                  ])
            points1 = np.array([lu, ru, rd, ld])

            if not (abs(angle) == 90 or abs(angle) == 270) and angle != 0:
                points = transform(points, M)
            else:
                points = np.array(points)

            ps3 = np.array(
                [
                    [min(points[0][0], points1[0][0]), min(
                        points[0][1], points1[0][1])],  # 左上(取最两者中最小的)

                    [max(points[1][0], points1[1][0]), min(
                        points[1][1], points1[1][1])],  # 右上

                    [max(points[2][0], points1[2][0]), max(
                        points[2][1], points1[2][1])],  # 右下

                    [min(points[3][0], points1[3][0]), max(
                        points[3][1], points1[3][1])]  # 左下
                ]
            )

            # img_cuted = cutPoly(img, points1)
            # cv2.imwrite(f'./tmp/{g_count2}.jpg', img_cuted)
            # with open(f'./tmp/{g_count2}.txt', 'w', encoding='utf-8') as f:
            #     f.write(word)
            # g_count2 += 1

            # cv2.polylines(img_color_origin, [points], isClosed=True, color=(   # 多边形，框得比较全
            #     100, 0, 255), thickness=2)  # 只画线，不填充

            
            arr.append( {"transcription":f"{word}","points":[lu, ru, rd, ld],"difficult":False} )


            cv2.polylines(img_color_origin, [points1], isClosed=True, color=(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

            # cv2.polylines(img_color_origin, [ps3], isClosed=True, color=(255, 0, 0), thickness=2)

            # cv2.imshow("orgin", img_color_origin)
            # cv2.waitKey(0)

            # break


        arr_str = string(arr)
        line = f'{dst_img_path}\t{arr_str}\n'
        label += line

        print( f'{g_count - 1} / {len(json_paths)} task done.' )

    ks = list( dic_words.keys() )

    keys = '\n'.join(ks)

    with open(label_path, "w", encoding='utf-8') as fp:
        fp.write(label)

    with open(key_path, "w", encoding='utf-8') as fp:
        fp.write(keys)

    with open(fileState_path, "w", encoding='utf-8') as fp:
        fp.write(states)

    print('all task done.')



```





## dbnet_aliocr_convert.py

```

# aliocr_results_2w\all_data\dbnet_aliocr_convert.py


"""

ali ocr 结果 转成 icdar2015 数据集供 mmocr 官方代码训练


icdar2015/imgs/training/img_1.jpg
icdar2015/imgs/test/img_3.jpg

icdar2015/annotations/training/gt_img_1.txt
icdar2015/annotations/test/gt_img_3.txt

注意：标注文件是 utf8-bom 格式
    必须以 icdar2015 命名文件夹，因为 DBNet 代码是以名字来判断文件格式的

    格式是 icdar2015 的格式，文件夹的组织方式是按照 DBnet 的要求创建的

PPOCRLabel --lang ch  # 启动标注工具

cp autodl-tmp/train_data.zip . && \
unzip train_data.zip -d PaddleOCR

# https://github.com/PaddlePaddle/PaddleOCR/blob/static/doc/doc_ch/FAQ.md

# 7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on data.7z data/

新建文件夹 train_data, 要标注的图片全部放在里面

新建 train_data/Label.txt 内容如下
行中用 \t 分隔 , points 的标记顺序是 左上 右上  右下 左下
train_data/0093.bmp	[{"transcription":"参考答案及解析","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]
train_data/0094.bmp	[{"transcription":"其他内容","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]


给 PaddleOCR 用，前面是坐标和图片都变换；这里图像不变，坐标不变


将阿里OCR 的识别结果（图片和标注）转换成 icdar2015 格式 (注意：它的文本是含 utf8 bom 的)

给 mmocr 训练用。格式是 icdar2015 的格式，文件夹的组织方式是按照 mmocr 的要求创建的

"""


"""

! unzip ./GD500.zip -d DB/datasets

icdar2015 文本检测数据集
标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text

其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。

# 表示text难以辨认。
"""

# 不重复的抽
from random import sample
import random
from pathlib import Path
import os
from secrets import choice
import shutil
import glob
import base64
from importlib.resources import path
import math
import numpy as np
import cv2
import json
import decimal
import datetime
from pickletools import uint8
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)


def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()


def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json


def parse(s):
    return json.loads(s, strict=False)

# convert dict to string


def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


def transform(points, M):
    # points 算出四个点变换后移动到哪里了
    # points = np.array([[word_x,  word_y],              # 左上
    #                    [word_x + word_width, word_y],                 # 右上
    #                    [word_x + word_width, word_y + word_height],  # 右下
    #                    [word_x, word_y + word_height],  # 左下
    #                    ])
    # add ones
    ones = np.ones(shape=(len(points), 1))

    points_ones = np.hstack([points, ones])

    # transform points
    transformed_points = M.dot(points_ones.T).T

    transformed_points_int = np.round(
        transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

    return transformed_points_int


def cutPoly(img, pts):
    # img = cv2.imdecode(np.fromfile('./t.png', dtype=np.uint8), -1)
    # pts = np.array([[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]])

    # (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y+h, x:x+w].copy()

    # (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    # (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    # (4) add the white background
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst

    # cv2.imwrite("croped.png", croped)
    # cv2.imwrite("mask.png", mask)
    # cv2.imwrite("dst.png", dst)
    # cv2.imwrite("dst2.png", dst2)

    return dst2


if __name__ == "__main__":

    root = 'icdar2015_dbnet'
    tmp = 'tmp'
    label_path = os.path.join(root, 'Label.txt')
    
    key_path = os.path.join(root, 'keys.txt')

    fileState_path = os.path.join(root, 'fileState.txt')

    if os.path.exists(root):
        shutil.rmtree(root)
        # os.rmdir(root)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)

    if not os.path.exists(root):
        os.makedirs(f'{root}/train_images')
        os.makedirs(f'{root}/test_images')

        os.makedirs(f'{root}/train_gts')
        os.makedirs(f'{root}/test_gts')

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    with open(f'{root}/readme.txt', "w", encoding='utf-8') as fp:
        fp.write('给 DBNet 官方代码 训练用。格式是 icdar2015 的格式，文件夹的组织方式是按照 DBnet 的要求创建的')

    label = ''
    keys = ''
    states = ''


    dic_words = {}  # 所有词

    # 开始转换

    # https://help.aliyun.com/document_detail/294540.html 阿里云ocr结果字段定义
    # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换

    dir_json = './data/json'  # '/yingedu/www/ocr_server/data/json'
    dir_img = './data/img'  # '/yingedu/www/ocr_server/data/img'

    g_count = 1
    g_count2 = 1


    json_paths = glob.glob('{}/*.json'.format(dir_json), recursive=False)

    json_paths = json_paths[:2000]

    for json_path in json_paths:

        arr = []

        base = Path(json_path).stem

        # if base == '0bf0383ece9a533683e615bf57525812':
        #     continue

        img_path = os.path.join(dir_img, '{}.txt'.format(base))

        if not os.path.exists(img_path):  # 没有相应的图片，可能被删除了
            print(f'Warnnig: no image {img_path}')
            continue

        jsn = load_json(json_path)

        if not ('prism_wordsInfo' in jsn):
            print(f'Warning: no charater in {img_path}')
            continue

        with open(img_path, "r", encoding="utf-8") as fp:
            imgdata = fp.read()
            imgdata = base64.b64decode(imgdata)
            imgdata = np.frombuffer(imgdata, np.uint8)
            
            try:
                img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)
            except Exception as e:
                print(f'Warning: image cannot decode: {img_path}')
                continue

            # cv2.imshow('img', img)
            # cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # DBNet 原版只能处理彩图，这里转一下

        else:
            img_color = img.copy()

        img_color_origin = img_color.copy()
        img_color_origin2 = img_color.copy()

        name = f'img_{g_count}.jpg'
        dst_img_path = f'{root}/train_images/{name}'
        dst_gt_path = f'{root}/train_gts/gt_img_{g_count}.txt'

        g_count += 1

        cv2.imwrite(dst_img_path, img)

        wordsInfo = jsn['prism_wordsInfo']
        for j in range(len(wordsInfo)):
            jo = wordsInfo[j]
            word = jo["word"]

            for w in list(word):
                if not (w in dic_words):
                    dic_words[w] = True

            # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换
            angle = jo['angle']

            img_color = img_color_origin.copy()

            word_x = jo['x']
            word_y = jo['y']
            word_width = jo['width']
            word_height = jo['height']

            if abs(angle) == 90 or abs(angle) == 270:
                word_width = jo['height']
                word_height = jo['width']
            elif angle != 0:

                # 变换前画出绿框，方便追踪点的前后变化
                # img_color = cv2.rectangle(img_color, (word_x, word_y), (
                #     word_x + word_width, word_y + word_height), (0, 255, 0), 2)  # 矩形的左上角, 矩形的右下角

                # cv2.imshow("green", img_color)
                # cv2.waitKey(0)

                # 变换前的多边形蓝框
                points = np.array([
                    [word_x,  word_y],                             # 左上
                    [word_x + word_width, word_y],                 # 右上
                    [word_x + word_width, word_y + word_height],  # 右下
                    [word_x, word_y + word_height],                # 左下
                ])

                # # cv2.fillPoly(img_color, pts=[points], color=(255, 0, 0)) # 填充
                # cv2.polylines(img_color, [points], isClosed=True, color=(
                #     255, 0, 0), thickness=1)  # 只画线，不填充

                # cv2.imshow("polys", img_color)
                # cv2.waitKey(0)

                # 获取图像的维度，并计算中心
                (h, w) = img_color.shape[:2]
                (cX, cY) = (w // 2, h // 2)

                # - (cX,cY): 旋转的中心点坐标
                # - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
                # - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
                # 1° = π/180弧度   1 弧度 =  180 / 3.1415926   // 0.0190033 是Mathematica 算出来的弧度，先转换成角度  // -0.0190033 * (180 / 3.1415926)
                M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
                img_color = cv2.warpAffine(img_color, M, (w, h))
                img_color_transform = img_color.copy()

                # cv2.imshow("after trans", img_color)
                # cv2.waitKey(0)

                # https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html  # 原理
                # https://stackoverflow.com/questions/30327659/how-can-i-remap-a-point-after-an-image-rotation # How can I remap a point after an image rotation?
                # 如何得到移动后的坐标点

                # points 算出四个点变换后移动到哪里了
                points = np.array([[word_x,  word_y],              # 左上
                                   # 右上
                                   [word_x + word_width, word_y],
                                   [word_x + word_width, word_y + \
                                       word_height],  # 右下
                                   [word_x, word_y + word_height],  # 左下
                                   ])
                # add ones
                ones = np.ones(shape=(len(points), 1))

                points_ones = np.hstack([points, ones])

                # transform points
                transformed_points = M.dot(points_ones.T).T

                transformed_points_int = np.round(
                    transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

                # cv2.polylines(img_color, [transformed_points_int], isClosed=True, color=(
                #     0, 0, 255), thickness=2)  # 画转换后的点

                # cv2.polylines(img_color_origin, [points], isClosed=True, color=(
                #     random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

                # cv2.imshow("orgin", img_color_origin)
                # cv2.waitKey(0)

            # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确（错，经验证不需要）
            pos = jo["pos"]
            x = int(pos[0]["x"])  # 左上
            y = int(pos[0]["y"])

            x2 = int(pos[2]["x"])  # 右下
            y2 = int(pos[2]["y"])

            lu = [pos[0]['x'], pos[0]['y']]  # left up  四个角顺时针方向数
            ru = [pos[1]['x'], pos[1]['y']]
            rd = [pos[2]['x'], pos[2]['y']]
            ld = [pos[3]['x'], pos[3]['y']]

            # 生成 icdar2015 格式的人工标记训练数据（用于训练 mmocr）
            # gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(lu[0], lu[1], ru[0], ru[1], rd[0], rd[1], ld[0], ld[1], word) )

            # 绘制矩形
            start_point = (x, y)  # 矩形的左上角

            end_point = (x2, y2)  # 矩形的右下角

            color = (0, 0, 255)  # BGR

            thickness = 2

            # 逐行画框
            # img_color_origin2 = cv2.rectangle(img_color_origin2, start_point, end_point, color, thickness)
            # cv2.imshow("box", img_color_origin2)

            # cv2.waitKey(0)

            points = [lu, ru, rd, ld]

            points0 = np.array([[word_x,  word_y],              # 左上
                                  # 右上
                                  [word_x + word_width, word_y],
                                    [word_x + word_width, word_y + \
                                     word_height],  # 右下
                                    [word_x, word_y + word_height],  # 左下
                                  ])
            points1 = np.array([lu, ru, rd, ld])

            if not (abs(angle) == 90 or abs(angle) == 270) and angle != 0:
                points = transform(points, M)
            else:
                points = np.array(points)

            ps3 = np.array(
                [
                    [min(points[0][0], points1[0][0]), min(
                        points[0][1], points1[0][1])],  # 左上(取最两者中最小的)

                    [max(points[1][0], points1[1][0]), min(
                        points[1][1], points1[1][1])],  # 右上

                    [max(points[2][0], points1[2][0]), max(
                        points[2][1], points1[2][1])],  # 右下

                    [min(points[3][0], points1[3][0]), max(
                        points[3][1], points1[3][1])]  # 左下
                ]
            )

            # img_cuted = cutPoly(img, points1)
            # cv2.imwrite(f'./tmp/{g_count2}.jpg', img_cuted)
            # with open(f'./tmp/{g_count2}.txt', 'w', encoding='utf-8') as f:
            #     f.write(word)
            g_count2 += 1

            # cv2.polylines(img_color_origin, [points], isClosed=True, color=(   # 多边形，框得比较全
            #     100, 0, 255), thickness=2)  # 只画线，不填充

            
            # arr.append( {"transcription":f"{word}","points":[lu, ru, rd, ld],"difficult":False} )

            arr.append( f'{lu[0]},{lu[1]},{ru[0]},{ru[1]},{rd[0]},{rd[1]},{ld[0]},{ld[1]},{word}' )


            # 377,117,463,117,465,130,378,130,Genaxis Theatre


            cv2.polylines(img_color_origin, [points1], isClosed=True, color=(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

            # cv2.polylines(img_color_origin, [ps3], isClosed=True, color=(255, 0, 0), thickness=2)

            # cv2.imshow("orgin", img_color_origin)
            # cv2.waitKey(0)

            # break

        gt = '\n'.join(arr) + '\n'
        
        with open(dst_gt_path, "w", encoding='utf-8') as fp:
            fp.write(gt)

        print( f'{g_count - 1} / {len(json_paths)} task done.' )

    ks = list( dic_words.keys() )
    ks = sorted(ks, key=lambda w: w, reverse=False)

    keys = '\n'.join(ks)

    with open(key_path, "w", encoding='utf-8') as fp:
        fp.write(keys)


    """
    划分训练集和测试集  8:2
    """
    testCount = int( g_count * 0.2 )
    if testCount == 0:
        testCount = 1

    img_paths = glob.glob(f'{root}/train_images/*.jpg', recursive=False)

    random.seed(1999)

    choices = sample(img_paths, testCount) # 随机抽取 testCount 个元素

    for img_path in choices:
       basename = Path(img_path).stem
       gt_path = f'{root}/train_gts/gt_{basename}.txt'

       dst_img_path = img_path.replace('train_images', 'test_images')
       dst_gt_path = gt_path.replace('train_gts', 'test_gts')

       shutil.move(img_path, dst_img_path)
       shutil.move(gt_path, dst_gt_path)


    train_list_path = f'{root}/train_list.txt'
    test_list_path = f'{root}/test_list.txt' 

    train_image_paths = glob.glob(f'{root}/train_images/*.jpg', recursive=False)
    test_image_paths = glob.glob(f'{root}/test_images/*.jpg', recursive=False)

    train_images = []
    test_images = []

    for train_image_path in train_image_paths:
        basename = os.path.basename(train_image_path)
        train_images.append( basename )

    for test_image_path in test_image_paths:
        basename = os.path.basename(test_image_path)
        test_images.append( basename )

    with open(train_list_path, "w", encoding='utf-8') as fp:
        txt = '\n'.join(train_images)
        fp.write(txt)

    with open(test_list_path, "w", encoding='utf-8') as fp:
        txt = '\n'.join(test_images)
        fp.write(txt)

    print('all task done.')



```







# Mathematica 交互

```python
# callbymma.py
import numpy as np
import cv2
import base64

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':

    np_array = np.fromfile('./密密麻麻.bmp', dtype=np.uint8)
    img = cv2.imdecode(np_array, -1)
    # bytes = img.tobytes()  # 转字节数组  # 或者使用img.tostring()，两者是等价的
        # 注意了：得到的bytes数据并不等价于open(file,"rb")数据

    # 把img 对象编码为jpg 格式
    success, encoded_image = cv2.imencode(".jpg", img) 
    # 将数组转为bytes
    bytes = encoded_image.tobytes() # 等价于tostring() 

    b64 = base64.b64encode(bytes).decode('ascii')  # base64字符串

    bytes2 = base64.b64decode(b64)  # 编码解码以后是否还正确

    with open("密密麻麻_base64.txt", "w") as fp:
        fp.write(b64)
    
    with open("yyyyyyyyyyyyy.jpg", "wb") as fp:
        fp.write(bytes2)  # 成功，我们自已写的 bytes

    cv2.imwrite('./ttttttttttttttttttt.jpg', img)  # 成功，opencv 保存 img 对象
```

```mathematica
(*callpython.nb*)
SetDirectory@NotebookDirectory[];
RunProcess[{"D:\\usr\\python.exe","D:\\workcode\\python\\opencv\\透视变换\\callbymma.py"}]
b64=Import@"密密麻麻_base64.txt";
bytes = BaseDecode@b64
BinaryWrite["bin.jpg", bytes]
Import["bin.jpg"]
```



# Pyqt5

```
https://www.zhihu.com/column/xdbcb8
```

Pyqtdeploy 



## Jamscreenshot 屏幕截图

https://github.com/fandesfyf/Jamscreenshot

https://github.com/fandesfyf/JamVideoPlayer  视频播放器



## pyside2 视频播放器

- https://gitee.com/se7enXF/pyside2

- https://github.com/se7enXF/pyside2

  

## pyside2 可视化文档纠错

- https://github.com/fiyen/PaddlePaddle-DocCRT



# python+C++

1.完整报错信息

```
Could not find platform independent libraries <prefix>
Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
Fatal Python error: initfsencoding: Unable to get the locale encoding
ModuleNotFoundError: No module named 'encodings'
 
Current thread 0x00007f5ab301f6c0 (most recent call first):
```

2.报错原因
场景是C++调用python时，找不到python解释器。

3.解决办法
在init之前添加解释器位置说明。

```
Py_SetPythonHome(L"/home/zxq/anaconda3/envs/onnx");
 
# 再去初始化
Py_Initialize();
 
printf("Python init \n");
 
 
Py_Finalize();
```



1.总结
C++传递参数给Python，需要转换成PyObject *类型。比如，C++的 int 是一个整数，该值占用4个字节的存储空间，而一个 python 的 int 实际是一个 PyObject* 指向 12字节。
前 4个字节是整数，代表引用次数；中间4个字节是指向 int 类型定义的指针，最后 4个字节是才是这个 int 的值。
所以 C++ 和 Python 之间参数互相传递都需要 Python提供的 api。

```
PyObject* arg1 = Py_BuildValue("i",220);  //整数参数
PyObject* arg2 = Py_BuildValue("f", 3.14);  //浮点数参数
PyObject* arg3 = Py_BuildValue("s", "hello"); //字符串参数
```



## C++部署onnx模型（C++和Python3混合编程）

1. 纯python部署（onnx模型）

```
import os
import time
 
import numpy as np
import onnxruntime
import json
import cv2
 
 
def imnormalize(img, mean, std, to_rgb=True):
    """Normalize an image with mean and std.
    Args:
        img (ndarray): Image to be normalized.
        mean (ndarray): The mean to be used for normalize.
        std (ndarray): The std to be used for normalize.
        to_rgb (bool): Whether to convert to rgb.
    Returns:
        ndarray: The normalized image.
    """
    img = img.copy().astype(np.float32)
 
    # cv2 inplace normalization does not accept uint8
    mean = np.float64(mean.reshape(1, -1))
    stdinv = 1 / np.float64(std.reshape(1, -1))
    if to_rgb:
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)  # inplace
    cv2.subtract(img, mean, img)  # inplace
    cv2.multiply(img, stdinv, img)  # inplace
    return img
 
 
def letterbox_image(img, input_dim, fill_value):
    """
    resize image with unchanged aspect ratio using padding
    让原图的高宽乘以同一个数，这样就不会改变比例，而这个数就是min( 高缩放的比例，宽缩放的比例)，然后padding周围区域使得缩放到指定大小。
    缩小： (2000, 4000) -> (200,200), min(200/4000, 200/2000) = 1/20, 2000 * 1/20 = 100， 4000 * 1/20 = 200
    新的尺度(100, 200)，再padding
    放大： (50, 100) -> (200, 200), min(4, 2) = 2, 50 * 2 = 100, 100 * 2 = 200
    新的尺度(100, 200)，再padding
    :param fill_value: int. Padding value
    :param img: original image.
    :param input_dim: (w, h). 缩放后的尺度
    :return:
    """
    orig_w, orig_h = img.shape[1], img.shape[0]
    input_w, input_h = input_dim  # 缩放(orig_w, orig_h) -> (input_w, input_h)
 
    # 1，根据缩放前后的尺度，获取有效的新的尺度(new_w, new_h)
    min_ratio = min(input_w / orig_w, input_h / orig_h)
    new_w = int(orig_w * min_ratio)  # （new_w, new_h）是高宽比不变的新的尺度
    new_h = int(orig_h * min_ratio)
    resized_image = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
 
    # 定义画布canvas，然后把有效区域resized_image填充进去
    canvas = np.full((input_dim[1], input_dim[0], 3), fill_value=fill_value, dtype=np.uint8)  # 定义画布，大小是（200,200）
 
    # 画布_h - 高宽不变_new_h
    start_h = (input_h - new_h) // 2  # 开始插入的高度位置, 也是上下需要padding的大小
    start_w = (input_w - new_w) // 2  # 开始插入的宽度位置
    canvas[start_h:start_h + new_h, start_w:start_w + new_w, :] = resized_image
 
    return canvas
 
 
def load_labels(path):
    with open(path) as f:
        data = json.load(f)
    return np.asarray(data)
 
 
def preprocess(input_data, mean_list, std_list):
    input_data = imnormalize(input_data, np.array(mean_list), np.array(std_list))
 
    input_data = input_data.transpose(2, 0, 1)  # [hwc] -> [chw]
 
    # add batch channel
    norm_img_data = np.expand_dims(input_data, 0).astype('float32')  # [1chw]
    return norm_img_data
 
 
def softmax(x):
    x = x.reshape(-1)
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
 
 
def postprocess(result):
    return softmax(np.array(result)).tolist()
 
 
class Model(object):
    def __init__(self
                 ):
        img_shape = [256, 256]
        mean_list = [123.675, 116.28, 103.53]
        std_list = [58.395, 57.12, 57.375]
        model_path = "/home/zxq/CLionProjects/test_my_inference_onnx/models/resnet18_mint.onnx"
        class_names = ['contamination', 'crack', 'good']
        self.img_shape = img_shape
        self.mean_list = mean_list
        self.std_list = std_list
        self.model_path = model_path
 
        self.class_names = np.array(class_names)
        self.ort_session = None  # 在构造函数里面实例化session会报错，估计是session数据结构复杂。
        self.input_name = None
        self.init_session()
 
    def init_session(self):
        self.ort_session = onnxruntime.InferenceSession(self.model_path)
        self.input_name = self.ort_session.get_inputs()[0].name
 
    def model_infer(self, img_path):
        image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        image = letterbox_image(image, self.img_shape, fill_value=0)
        input_data = preprocess(image, self.mean_list, self.std_list)  # [1chw] numpy.ndarray
 
        start_time = time.time()
        raw_output = self.ort_session.run([], {self.input_name: input_data})[0]
        pred_idx = np.argmax(raw_output)
        print(time.time() - start_time)
        pred_name = self.class_names[pred_idx]
        print('Final prediction is: {}, score: {}'.format(self.class_names[pred_idx], raw_output[0, pred_idx]))
        return pred_idx, pred_name, raw_output
 
 
if __name__ == '__main__':
    model = Model()
    # get the name of the first input of the model
 
    test_data_path = '/home/zxq/PycharmProjects/data/pill/mint/test'
    for root_, dir_, file_name_list in os.walk(test_data_path):
        for file_name in file_name_list:
            full_path = os.path.join(root_, file_name)
            print(full_path)
            model.model_infer(full_path)
```



```
// detecor.h 
// Created by zxq on 2021/5/9.
//
 
#ifndef TEST_MY_INFERENCE_ONNX_DETECTOR_H
#define TEST_MY_INFERENCE_ONNX_DETECTOR_H
 
#include <iostream>
#include <string>
#include "Python.h"
using namespace std;
class Detector {
public:
    Detector(const wchar_t *envs_path);
    ~Detector();
    size_t run(PyObject * img_path);
 
private:
    const wchar_t *envs_path;
    PyObject * pModule;
    PyObject* pDict;
    PyObject* pClassCalc;
    PyObject* pConstruct;
    PyObject* pInstance;
public:
    size_t flag;
    size_t c_result;
};
 
#endif //TEST_MY_INFERENCE_ONNX_DETECTOR_H
 
 
```



```
// detector.cpp
// Created by zxq on 2021/5/9.
//
 
#include "detector.h"
#include <Python.h>
#include <iostream>
using namespace std;
 
Detector::Detector(const wchar_t * envs_path_) {
    // set python interpret path
    envs_path = envs_path_;
    Py_SetPythonHome(envs_path);
 
    // init python
    Py_Initialize();
    assert(Py_IsInitialized());
 
    // find python script
    PyRun_SimpleString("import os, sys");
    PyRun_SimpleString("sys.path.append('../')");
 
    // import module
    pModule = PyImport_ImportModule("TestOnnxResnet_mint");
    assert(pModule);
 
    // import dict of module
    pDict = PyModule_GetDict(pModule);
    assert(pDict);
 
    // import class
    pClassCalc = PyDict_GetItemString(pDict, "Model");
    assert(pClassCalc);
 
    //get constructor
    pConstruct = PyInstanceMethod_New(pClassCalc);
    assert(pConstruct);
 
    // using constructor to construct instance.
    pInstance = PyObject_CallObject(pConstruct,nullptr);
    assert(pInstance);
}
 
Detector::~Detector() {
    Py_DECREF(pModule);
    Py_DECREF(pDict);
    Py_DECREF(pClassCalc);
    Py_DECREF(pConstruct);
    Py_DECREF(pInstance);
    Py_Finalize();
}
 
size_t Detector::run(PyObject * img_path){
    /*
     * PyObject *img_path=Py_BuildValue("(s)", "/home/zxq/CLionProjects/test_my_inference_onnx/
     * test_data/cls/mint/pill_mint_contamination_181.png");
     */
    //判断初始化是否成功
    size_t CResult;
    PyObject *PyResult = PyObject_Call(PyObject_GetAttrString(pInstance, "model_infer"), img_path, nullptr);
}
```



```
// main.cpp
#include "detector.h"
#include <Python.h>
 
using namespace std;
 
 
int main(int argc, char *argv[]) {
    const wchar_t * envs_path = L"/home/zxq/anaconda3/envs/onnx";
    Detector det(envs_path);
 
    while (true){
        PyObject *img_path=Py_BuildValue("(s)", "/home/zxq/CLionProjects/test_my_inference_onnx/test_data/cls/mint/pill_mint_contamination_181.png");
        det.run(img_path);
    }
 
    return 0;
}
```



```
// cmakelists.txt

cmake_minimum_required(VERSION 3.16)
project(test_my_inference_onnx)
 
set(CMAKE_CXX_STANDARD 14)
 
# 包含detect.h路径
SET(INC_DIR  include)
include_directories(${INC_DIR})
 
include_directories(
        /home/zxq/anaconda3/envs/onnx/include/python3.7m
)
add_executable(test_my_inference_onnx
        tmp.cpp include/detector.cpp include/detector.h)
target_link_libraries(test_my_inference_onnx
        /home/zxq/anaconda3/envs/onnx/lib/libpython3.7m.so
        )
```





# python+C#

- https://github.com/pythonnet/pythonnet



# 控制鼠标

- http://www.dszhp.com/pyautogui.html

- https://pyautogui.readthedocs.io/en/latest/mouse.html



```
netflix_auto_pin.py

# 鼠标移动最左上角退出本程序

from time import sleep
import pyautogui, sys
import keyboard
import time

'''默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止'''
#pyautogui.FAILSAFE =False
'''意味着所有pyautogui的指令都要暂停一秒；其他指令不会停顿；这样做，可以防止键盘鼠标操作太快；'''
pyautogui.PAUSE = 1

# 得到当前鼠标位置
print(pyautogui.position()) #Point(x=502, y=365)

print(pyautogui.isValidKey('del'))

# pyautogui.click(745,421,button='left')  # netflix pin码输入框最左边单击左键
# pyautogui.press('del')  # 按下 Del
# time.sleep(0.1)
# pyautogui.press('del')
# time.sleep(0.1)
# pyautogui.press('del')


#time.sleep(3)

while True:
    # 鼠标移动最左上角退出
    pyautogui.click(613,421,button='left')  # netflix pin码输入框最左边单击左键
    pyautogui.press('6')  # 按下 6
    time.sleep(0.01)
    pyautogui.press('1')
    time.sleep(0.01)
    pyautogui.press('7')
    time.sleep(0.01)
    pyautogui.press('4')
    time.sleep(10)

# try:
#     curr = 0
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)

#         pyautogui.moveTo(184, 941, 3)
#         pyautogui.moveTo(1685, 121, 3)
#         if keyboard.is_pressed('b'):
#             break
        
#         time.sleep(10)


#         curr += 1
#         if curr >= 3:
#             break
# except KeyboardInterrupt:
#     print('KeyboardInterrupt')



```





```
python3 -m pip install pyautogui
pip install keyboard

#! python3
from time import sleep
import pyautogui, sys
#import keyboard

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        pyautogui.moveTo(184, 941, 3)
        pyautogui.moveTo(1685, 121, 3)
        #if keyboard.is_pressed('b'):
            #break


except KeyboardInterrupt:
    print('\n')


"""
python3 -m pip install pyautogui
pip install keyboard
"""

```



```
win32api.ShellExecute(0, 'open', r'D:\Program Files\xx.exe', '', '', 1)
    hwnd = win32gui.FindWindow(None, 'xx')
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    res = win32gui.SetForegroundWindow(hwnd)

    pyautogui.hotkey('ctrl','l')

    pyperclip.copy('hello')
    pyautogui.hotkey('Ctrl', 'v')
    pyautogui.hotkey('enter')
```





```
import pyautogui
import pydirectinput
import time
import random
import sys
import keyboard
from PIL import ImageGrab
import ctypes

SendInput = ctypes.windll.user32.SendInput
# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002,
                        0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

CONTROL = 0x1D
ALT = 0x38
C = 0x1F #0x2E
A = 0x1E


time.sleep(2)
pydirectinput.moveTo(x=917, y=880, duration=0.4)
pydirectinput.click()
PressKey(CONTROL)
time.sleep(0.02)
PressKey(ALT)
time.sleep(0.02)
PressKey(A)

time.sleep(0.02)
ReleaseKey(A)
time.sleep(0.02)
ReleaseKey(ALT)
time.sleep(0.02)
ReleaseKey(CONTROL)

pydirectinput.mouseDown()
time.sleep(0.02)
pydirectinput.moveTo(x=1488, y=1025, duration=2.7)
time.sleep(0.02)
pydirectinput.mouseUp()
time.sleep(0.02)
PressKey(CONTROL)
time.sleep(0.02)
PressKey(C)
time.sleep(0.02)
ReleaseKey(C)
time.sleep(0.02)
ReleaseKey(CONTROL)
time.sleep(0.2)
image = ImageGrab.grabclipboard()
image.save(r'./test.png')
```





# 算数编码

- https://github.com/ahmedfgad/ArithmeticEncodingPython

  



# Excel



找不开xlsx，用engine=‘openpyxl’  替代

```bash
原因是最近xlrd更新到了2.0.1版本，只支持.xls文件。所以pandas.read_excel(‘xxx.xlsx’)会报错。

可以安装旧版xlrd，在cmd中运行：

pip uninstall xlrd
pip install xlrd==1.2.0

也可以用openpyxl代替xlrd打开.xlsx文件：

df=pandas.read_excel('data.xlsx',engine='openpyxl')
```





```python
import pandas as pd
seg = pd.DataFrame(wordlist,columns=['word','length','fre','pmi','entropy'])
seg.to_csv(fname_results, index=False ,encoding="utf-8")
```



## xlsx



```
pip install openpyxl
pip install xlrd
```



扩展名 xlsx 才是真excel，csv 不是

```python
    csv = pd.DataFrame(data,columns=['知识点ID', '考频', '考频分类', '考试大纲', '关联真题数', '关联非真题数', '知识点内容'])
    csv.to_excel(fname_csv, index=False ,encoding="utf-8")
```



```
pd.read_excel('tmp.xlsx', index_col=None, header=None) 
```








## read csv



```python
import os,glob
import pandas as pd

currDir = os.path.dirname(os.path.abspath(__file__))

csv_dir = os.path.join(currDir, 'data/mecab-ipadic')
jp_dic_paths = []
paths = glob.glob(f"{csv_dir}/*.csv", recursive=True)
df = pd.read_csv(paths[0])
```



### encoding

```python
ds = pd.read_csv(fname_csv, usecols= ['列名'], encoding='gbk') # utf-8
```







```python
    csvs = ['药学专业知识一-考频.csv', '药学专业知识二-考频.csv', '药事管理与法规-考频.csv', '药学综合知识与技能-考频.csv']
    currDir = os.path.dirname(os.path.abspath(__file__))
    
    dic_pl = {}  # Point Level

    for fname in csvs:
        fname_csv = os.path.join(currDir, DIRNAME, fname)
        print(fname_csv)
        ds = pd.read_csv(fname_csv, usecols= ['知识点ID', '考频分类']) # header=None
        print(ds.shape, ds.size)
        for l in ds.values:
            examPoinID = str(l[0])
            level = l[1]
            if examPoinID not in dic_pl:                
                dic_pl[examPoinID] = level
                #print(examPoinID, level)
            else:
                raise RuntimeError('something wrong.')  # 不同科目不应该有相同的知识点ID
```





If you only want to read the first 999,999 (non-header) rows:

```py
read_csv(..., nrows=999999)
```

If you only want to read rows 1,000,000 ... 1,999,999

```py
read_csv(..., skiprows=1000000, nrows=999999)
```

***nrows\*** : int, default None Number of rows of file to read. Useful for reading pieces of large files*

***skiprows\*** : list-like or integer Row numbers to skip (0-indexed) or number of rows to skip (int) at the start of the file

and for large files, you'll probably also want to use chunksize:

***chunksize\*** : int, default None Return TextFileReader object for iteration



## write xlsx



```
import json
import decimal
import datetime

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json 
def parse(s):
    return json.loads(s, strict=False )

# convert dict to string
def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)



import pandas as pd


if __name__ == "__main__":

    dic_domains = {}

    sheet_names = [ 'xx', 'xx', 'xx' ]

    for sheet in sheet_names:

        ds = pd.read_excel("xxx.xlsx", sheet_name = sheet, usecols= ['xxx','xxx'])

        print(ds.shape, ds.size)
        for l in ds.values:
            AppCName = str(l[0])
            AppEName = str(l[1])

            if (AppEName in dic_domains):
                raise Exception(xx + " already exist.")
            
        
            dic_domains[xx] = { "xx":AppEName, "xx":xx, "Domain":sheet }

        a = 1

    save_json('./domains.json', dic_domains)
```









## multiple dataframes



```python
import pandas as pd

# Create some Pandas dataframes from some data.
df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
```



```python
writer = pd.ExcelWriter(filepath)
companydf.to_excel(excel_writer=writer,sheet_name='公司维度表')
goodsdf.to_excel(excel_writer=writer, sheet_name='货物维度表')
writer.save()
writer.close()
```





[geeks4geeks](https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/)

[read csv](https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58)

[使用 Python 读写 CSV 文件（三）](https://zhuanlan.zhihu.com/p/40946024)



# Word



[Python读取word文本](https://blog.csdn.net/woshisangsang/article/details/75221723)

[用python-docx模块读写word文档](https://www.jianshu.com/p/94ac13f6633e)



```python
# coding:utf-8
# 写word文档文件
import sys

from docx import Document
from docx.shared import Inches

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    # 创建文档对象
    document = Document()
    
    # 设置文档标题，中文要用unicode字符串
    document.add_heading(u'我的一个新文档',0)
    
    # 往文档中添加段落
    p = document.add_paragraph('This is a paragraph having some ')
    p.add_run('bold ').bold = True
    p.add_run('and some ')
    p.add_run('italic.').italic = True
    
    # 添加一级标题
    document.add_heading(u'一级标题, level = 1',level = 1)
    document.add_paragraph('Intense quote',style = 'IntenseQuote')
    
    # 添加无序列表
    document.add_paragraph('first item in unordered list',style = 'ListBullet')
    
    # 添加有序列表
    document.add_paragraph('first item in ordered list',style = 'ListNumber')
    document.add_paragraph('second item in ordered list',style = 'ListNumber')
    document.add_paragraph('third item in ordered list',style = 'ListNumber')
    
    # 添加图片，并指定宽度
    document.add_picture('e:/docs/pic.png',width = Inches(1.25))
    
    # 添加表格: 1行3列
    table = document.add_table(rows = 1,cols = 3)
    # 获取第一行的单元格列表对象
    hdr_cells = table.rows[0].cells
    # 为每一个单元格赋值
    # 注：值都要为字符串类型
    hdr_cells[0].text = 'Name'
    hdr_cells[1].text = 'Age'
    hdr_cells[2].text = 'Tel'
    # 为表格添加一行
    new_cells = table.add_row().cells
    new_cells[0].text = 'Tom'
    new_cells[1].text = '19'
    new_cells[2].text = '12345678'
    
    # 添加分页符
    document.add_page_break()
    
    # 往新的一页中添加段落
    p = document.add_paragraph('This is a paragraph in new page.')
    
    # 保存文档
    document.save('e:/docs/demo1.docx')
    
if __name__ == '__main__':
    main()

```



# Panda



## 修改

```
# cli 的入口点在这 pandora\src\pandora_cloud\pandora\bots\legacy.py  run, 自已建一个 run_ak148 用来生成解析
# pip install openpyxl pandas

import pandas as pd
path_ak148 = 'ak148.xlsx'
df = pd.read_excel(path_ak148,engine='openpyxl')
print(df.shape, df.size)

for idx_row in range(len(df)):
    gpt = df.loc[idx_row, "gpt"]
    if pd.isnull(gpt):
        gpt = 'get expalin from pandora'
        df.loc[idx_row, "gpt"] = gpt
    df.to_excel(path_ak148, index=False ,encoding="utf-8")
    print(df.loc[idx_row, "name"], df.loc[idx_row, "dlg"], df.loc[idx_row, "gpt"])
```



## 行名列名

```python
df = pd.DataFrame([[1,2],[3,4]], index=["one", "two"], columns=["A", "B"])
df.to_excel("file.xlsx")
```

<img src="Python 3  Summary.assets/image-20230718083252045.png" alt="image-20230718083252045" style="zoom:50%;" />



## 插入图片

```

import io
from openpyxl_image_loader import SheetImageLoader
import openpyxl
import pandas as pd
import time
 
def __insert_photo_mmc(excel_file_name):
    
    #读取图片来源表
    photoExcel = openpyxl.load_workbook(filename)
 
    # 读取所有图片
    dic_style_image = dict()
 
    for sheet_name in photoExcel.sheetnames:
        sheet = photoExcel[sheet_name]  # 打开sheet
        image_loader = SheetImageLoader(sheet)
        for i in range(2, sheet.max_row+1):  # 从第2行开始，总行数要+1
            try:
                style = sheet['I'+str(i)].value  # style 在 A列
                style = style.upper()
 
                image = image_loader.get('A'+str(i))  # 图片在 C列
                dic_style_image[style] = image
 
            except ValueError:  # 没有图片，或图片超出单元格的情况
                logger.info("idx={} 没有图片".format(i))
 
    # print(len(dic_style_image))
    # dic_style_image['ARJL100798-BK3'].show()
 
    #######输出excel#################
    output_file = time.strftime("%d%H%M%S", time.localtime()) + '.xlsx' #输出的表
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    workbook = writer.book
 
    data_excel = pd.ExcelFile(excel_file_name) #读取要被插入图片的excel表
 
    for sheet_name in data_excel.sheet_names:
        df = data_excel.parse(sheet_name=sheet_name)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        sheet = writer.sheets[sheet_name]
        # 设置图片大小
        image_size = (81, 54)
 
        for idx, row in df.iterrows():
            style = row['款号']
            style = style.upper()
            img = dic_style_image.get(style, None)
 
            anchor = 'H'+str(idx+2)  # 图片输出在H列
 
            if img is None:
                sheet.write_string(anchor, 'no photho')
            else:
                img_file_name = img.filename
 
                # 设置行高
                height = math.ceil(image_size[1]*0.85)
                sheet.set_row(idx+1, height)
 
                #resize图片
                img = img.resize(image_size)
 
                #转成byteio格式
                buf = io.BytesIO()
                img.save(buf, format='JPEG')
                sheet.insert_image(anchor, img_file_name, 
                                {'image_data': buf, 'x_offset': 1, 'y_offset': 3})
 
    workbook.close()
    data_excel.close()
 
    return output_file

```



```
writer = pd.ExcelWriter('filename.xlsx', engine='xlsxwriter')
df.to_excel(writer) # 将DataFrame数据导入writer
workbook  = writer.book # 提取workbook对象
worksheet = workbook.add_worksheet()  # 添加工作表Sheet
worksheet.insert_image('D4',filename.jpg')  # 插入图片 到D4位置
writer.save() # 保存表格文件

```





## 分组、聚合

```python
# https://zhuanlan.zhihu.com/p/101284491
# 不同公司薪水按中位数显示，年龄按平均数显示
data.groupby('company').agg({'salary':'median','age':'mean'})
```







## DataFrame

> "dict-like" Series **container** for **Series objects**
>
> - **是序列对象的容器，能够以字典方式存取数据**



```python
    for N in range(2, MAX_N+1): # MAX_N+1
        print(f'正在进行{N}-Gram词的最大熵筛选({len(rt[N-2])})...')
        pp = []
        for i in range(0,len(s)):
            if i+N+2 <= len(s):  # +2 是因为一个左邻字，一个右邻字
                pp.append( [ s[i:i+1], s[i+1:N+i+1], s[N+i+1:N+i+2] ] )
        pp2 = pd.DataFrame(pp).set_index(1).sort_index() # 排序，可以加快检索速度
        """
        现在输入N-Gram 词，可以得到它的左邻右邻字
        """

        index = np.sort(np.intersect1d(rt[N-2], pp2.index)) # 作交集
        
        left = pp2[0][word]                            # word 的所有左邻字
        right = pp2[2][word]                           # word 的所有右邻字
```



### copy

```python
dataframe1 = dataframe.copy(deep=True)
```





### 前几列前几行

```python
full['Cabin'].head() # 前5列
full.head(10) # 前10行
```



### 行数和列数

```python
len(dataframe.index)
len(dataframe.columns)
dataframe.shape
```



#### 所有列名

```python
train.columns.values.tolist()
```



### 读取没有列名的csv

```python
import os,glob
import pandas as pd

currDir = os.path.dirname(os.path.abspath(__file__))

csv_dir = os.path.join(currDir, 'data/mecab-ipadic')
jp_dic_paths = glob.glob(f"{csv_dir}/*.csv", recursive=True)

dic = {}
for pth in jp_dic_paths:
    # csv本身没有列名(有的话通常是第一行), 手动定义列名
    df = pd.read_csv(pth, header=None, names=['word','feq','3','4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
    for idx_row in range(len(df)):
        word = df.loc[idx_row, 'word']
        feq = df.loc[idx_row, 'feq']
        if pd.isnull(word):
            a = 1
```





### 筛选数据

```python
# https://medium.com/jovianml/https-jovian-ml-undefined-none-titanic-logistic-regression-v-105-cellid-55-bb7b2b1b5de1
len(dataframe[(dataframe["Survived"]==1) & (dataframe["Sex"]=="female") & (dataframe["Pclass"]==1)].index)
```

```python
# 头等舱女性的存活率
len(dataframe[(dataframe["Survived"]==1) & (dataframe["Sex"]=="female") & (dataframe["Pclass"]==1)].index) / \
    len(dataframe[(dataframe["Sex"]=="female") & (dataframe["Pclass"]==1)].index)
--> 0.968
```



### loc

```python
#原始数据集有891行
sourceRow=891
'''
sourceRow是我们在最开始合并数据前知道的，原始数据集有总共有891条数据
从特征集合full_X中提取原始数据集提取前891行数据时，我们要减去1，因为行号是从0开始的。
'''
#原始数据集：特征
source_X = full_X.loc[0:sourceRow-1,:]
#原始数据集：标签
source_y = full.loc[0:sourceRow-1,'Survived']   

#预测数据集：特征
pred_X = full_X.loc[sourceRow:,:]
```





### 最大最小值均值

```python
print("Average age of all passengers -->  {0:.1f}".format(dataframe.Age.mean()))
print("Age of oldest passenger -->  {:.1f}".format(dataframe.Age.max()))
print("Age of youngest passenger -->  {:.1f}".format(dataframe.Age.min()))
```





### 合并数据帧

```python
full = pd.DataFrame()
full = pd.concat([train,test],ignore_index=True)  # 列数不一至的数据帧合并，缺失列的一方会添加空列(所有数据为空白)
print(full.columns)
```



### 填充缺失值

```python
from pandas import DataFrame
full['Age']  = full['Age'].fillna(full['Age'].mean())
#年龄因为不可从其他途径得知，采用平均年龄填充，此步骤对最终预测结果有影响。
full.info()
```

```python
# 缺失值计数
df['Age'].isnull().sum()
```



#### apply

```python
def fill_in_age(x):
    if x['Pclass_1']==1:
        return 37
    elif x['Pclass_2']==1:
        return 29
    else:
        return 25
df['Age']=df.apply(fill_in_age, axis=1)
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
```



### 数据标准化

z-score标准化

- 经过处理后的数据符合标准正态分布，即均值为0，标准差为1

```python
to_normalize=['Age','Fare']
for each in to_normalize:
    mean, std= df[each].mean(), df[each].std()
    df.loc[:, each]=(df[each]-mean)/std
```

标准化后的变量值围绕0上下波动，**大于0说明高于平均水平，小于0说明低于平均水平**。





### One hot encode

[u](https://blog.csdn.net/maymay_/article/details/80198468)

get_dummies 是利用pandas实现one hot encode的方式

<img src="Python 3  Summary.assets/image-20210203095930108.png" alt="image-20210203095930108" style="zoom:50%;" />



```python
# 直观上是把一列变成了很多列，值不是0就是1
embarkedDf = pd.get_dummies(full['Embarked'],prefix='Embarked')#predix参数用于指定类别标签
full = pd.concat([full,embarkedDf],axis=1)
full.drop('Embarked',axis=1,inplace=True)#删除‘Embarked’列
full.head()
```

![image-20210203101608443](Python 3  Summary.assets/image-20210203101608443.png)



### Map

```python
def get_title(name):#定义称谓提取函数
    str1=name.split(',')[1]#提取，后边的字符串
    str2=str1.split('.')[0]#提取.前面的字符串
    str3=str2.strip()#用于去除空格
    return str3
titleDf = pd.DataFrame()
titleDf['Title'] = full['Name'].map(get_title)
titleDf['Title'].value_counts()
```



### 柱状图



#### 三种舱生存情况

```python
sns.countplot(x="Survived", hue="Pclass", data=dataframe)
plt.title("No. of people survived from different classes")
```

<img src="Python 3  Summary.assets/image-20210203150631837.png" alt="image-20210203150631837" style="zoom:50%;" />

### 分布图

```python
# 票价分布
sns.distplot(dataframe.Fare)
```

<img src="Python 3  Summary.assets/image-20210203151255163.png" alt="image-20210203151255163" style="zoom:50%;" />



### 热力图

```python
# 缺失值高亮
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
```

<img src="Python 3  Summary.assets/image-20210203165600556.png" alt="image-20210203165600556" style="zoom:50%;" />



### 箱形图

```python
plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=titanic,palette='winter')
```







## Series [u](https://towardsdatascience.com/gaining-a-solid-understanding-of-pandas-series-893fb8f785aa)

>  Series 可以是**数据集**的行，也可以是数据集的列 



bigdataEntropy.py

```python
tt = tt.drop(labels=will_drops)  # 第二次筛选：凝合程度
rt.append( tt.index )
```





### 转有转字典

```python
from collections import OrderedDict, defaultdict
cs = pd.Series(list(s)).value_counts().to_dict(OrderedDict)
```



```python
dic_tosave = {
        'total_alphabets':0,
        't':[],
        'tt':[]
    }

    cs = pd.Series(list(s)).value_counts()              # 所有字的出现次数 
    dic_tosave['total_alphabets'] = int( cs.sum() )     # 总共有多少个字
    dic_tosave['t'].append( cs.to_dict(OrderedDict) )   # Series 转成有序字典才能保存JSON
```





### 统计每个字出现次数

```python
counts = pd.Series(list(s)).value_counts() # 每个字出现多少次
totol = counts.sum()  # 总共有多少个字
```

```python
    ls = list(s)
    for N in range(2, MAX_N+1):
        print(f'正在生成{N}-Gram词...')
        t.append([])
        for i in range(0,len(ls)):
            if i+N <= len(ls):
                t[N-1].append( "".join(ls[i:N+i]) )  # array[start:stop:step]
            
        t[N-1] = pd.Series(t[N-1]).value_counts()  # 所有N-Gram 词出现次数
        t[N-1] = t[N-1][t[N-1] > min_count]        # 最小次数筛选
        tt = t[N-1][:]
```





```python
revenue = pd.Series([1000, 1200, 1500, 800, 900], index=['2014', '2015', '2016', '2017', '2018'])
```

```python
revenue.sort_values(ascending=False).index[0]
```



# duckdb

https://huggingface.co/docs/datasets-server/duckdb

https://duckdb.org/docs/extensions/httpfs/overview.html

https://duckdb.org/docs/extensions/httpfs/s3api

https://www.cloudflare.com/en-gb/developer-platform/r2/   CF 支持



https://zhuanlan.zhihu.com/p/646788236

Duckdb 提供了SQLite 的兼容层，允许之前使用 SQLite 的重新连接到 DuckDB，可见DuckDB也可以直接应用于场景的SQLite场景。

```
import duckdb
from contextlib import suppress

def ols4(x: list, y: list) -> list[float]:
    X = sm.add_constant(np.array([[r["x1"], r["x2"]] for r in x]))
    res = sm.OLS(y, X).fit()
    return res.params

with suppress(Exception):
    duckdb.remove_function("ols4")

duckdb.create_function("ols4", ols4)


sql = """
with tmp as (
    select key, ols4(list((x1, x2)), list(y)) as coef
    from df
    group by all
)
select key, coef[1] as const, coef[2] as x1, coef[3] as x2
from tmp
order by all
"""
%timeit duckdb.sql(sql).df()

```



# steampipe 嵌入式 postgreSQL

https://github.com/turbot/steampipe

- https://github.com/yugabyte/yugabyte-db  分布式





# 爬虫



```python
有人爬清华的太过分了 服务器更新中=-=

---------------------
清华的比较简单 浏览器里会留缓存图片 python3 需要 pip install selenium img2pdf
from selenium import webdriver
import os,imghdr,shutil
import time,random
import img2pdf
from PIL import Image
def getpics(pdfidurl):
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=%s\wqbook"%os.getcwd())  # Path to your chrome profile
    driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    pdf_url = 'https://lib-nuanxin.wqxuetang.com/read/pdf/{}'.format(pdfid)
    driver.get(pdf_url)
    body=driver.find_element_by_css_selector('body')
    time.sleep(5)
    scrpositon=0
    height=driver.execute_script("return document.body.scrollHeight;")
    print(height)
    while scrpositon<height:
        scrpositon+=1500
        driver.execute_script("window.scrollTo(0,%s);"%scrpositon)
        time.sleep(4+random.randint(0,1))
    driver.quit()
def movefiles(pdfid):
    os.mkdir(pdfid)
    path = 'wqbook\Default\Cache\\'
    fileList = os.listdir(path)
    for i in fileList:
        print(imghdr.what(path + i))
        ext = imghdr.what(path + i)
        if ext == 'png':
            shutil.copyfile(path + i, '%s\\'%pdfid + i + '.' + ext)
        os.remove(path + i)
def changename(pdfid):
    fileList = os.listdir(pdfid)
    for i in fileList:
        name=i.split('.')[0]
        name=name.split('_')[1]
        os.rename(r'%s\%s'%(pdfid,i),r'%s\%s.png'%(pdfid,int(name, 16)))

if __name__ == '__main__':
    for pdfid in [
        '',#书的id
    ]:
        getpics(pdfid)
        movefiles(pdfid)
        changename(pdfid)
        for file in os.listdir(pdfid):
            filepath = '%s\\'%pdfid + file
            img = Image.open(filepath)
            img.convert('RGB').save(filepath)
        a = ['%s\\'%pdfid + i for i in os.listdir(pdfid) if i.endswith(".png")]
        a.sort(key=lambda x: int(x.split('\\')[1].split('.')[0]))
        with open("%s.pdf"%pdfid, "wb") as f:
            f.write(img2pdf.convert(a))
        print('%s已完成'%pdfid)


电子工业的似乎会banIP了

--------------------------

电子工业的一页一页截就行 一样用法
from selenium import webdriver
import time,os
from selenium.webdriver.common.action_chains import ActionChains
import img2pdf
from PIL import Image, ImageDraw, ImageFilter

def getbook(bookid):
    driver = webdriver.Chrome()
    driver.set_window_size(1456,2536)
    driver.get('https://yd.51zhy.cn/ebook/reader/index.html#/pdfReader?id=%s'%bookid)
    time.sleep(5)
    ActionChains(driver).move_by_offset(200, 100).click().perform()

    pdfboxes = driver.find_elements_by_class_name('pdf_box')
    pagenum = 0
    if os.path.exists(bookid):
        pagenum=len(os.listdir(bookid))
    else:
        os.mkdir(bookid)
    for box in pdfboxes[pagenum:]:
        driver.execute_script("arguments[0].scrollIntoView(true)", box)
        while box.get_attribute('style') != 'background: white;': time.sleep(1)
        with open(r'%s/%s.png' % (bookid,pagenum), 'wb') as f:
            f.write(box.find_element_by_class_name('page').screenshot_as_png)
        pagenum += 1
    driver.quit()

if __name__ == '__main__':
    for bookid in [
        '',
    ]:
        getbook(bookid)
        for file in os.listdir(bookid):
            filepath = '%s\\'%bookid + file
            img = Image.open(filepath)
            img.convert('RGB').save(filepath)
        a = ['%s\\'%bookid + i for i in os.listdir(bookid) if i.endswith(".png")]
        a.sort(key=lambda x: int(x.split('\\')[1].split('.')[0]))
        with open("%s.pdf"%bookid, "wb") as f:
            f.write(img2pdf.convert(a))
        print('%s已完成'%bookid)


还要下个chromedrive 看电脑上的chrome版本 是最新的话就下载这个
https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/


检查下 selenium调用chrome后 是不是没设置浏览器窗口大小
因为调用的是chrome的 capture node screenshot 可能node没显示全


跑的时候chrome里 开发者工具 alt+ctrl+p 然后 capture node screenshot 看看正不正常？

机械工业的，有人抓了电脑书的
```



## sign



```python

# https://jishuin.proginn.com/p/763bfbd5a01a
# https://www.cnblogs.com/wqzn/p/14568794.html
# https://zhuanlan.zhihu.com/p/113369113

# pip install selenium

"""
centos7 + selenium
pip3.8 install selenium

yum autoremove -y google-chrome  # 卸载旧版本

wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install -y google-chrome-stable_current_x86_64.rpm

google-chrome --version
    # 97.0.4692.71
    # http://chromedriver.storage.googleapis.com/index.html  到这里下载这个版本的驱动

wget http://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip

mv chromedriver /opt/google/chrome/
chmod 755 /opt/google/chrome/chromedriver


curl https://intoli.com/install-google-chrome.sh | bash
/opt/google/chrome/chrome  # Running as root without --no-sandbox is not supported.

google-chrome-stable --no-sandbox --headless --disable-gpu --screenshot https://www.baidu.com/  # 成功后后生成一个文件 screenshot.png

google-chrome --version
    # 97.0.4692.71
   


whereis python3.8
cp chromedriver /usr/local/bin

crontab -e # edit
crontab -l # list all task

00    07    *    *    *    python3.8 -u /root/sign.py > /root/log_sign.txt

"""

from selenium import webdriver

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

import time


show = True  # UI OR not
#show = False

if __name__  ==  "__main__": 

    # python目录下必须有chromedriver.exe （http://chromedriver.storage.googleapis.com/index.html 这里下载和当前使用版本一致的）
    
    
    opt = webdriver.ChromeOptions()
    opt.headless = show

    if show:
        wd=webdriver.Chrome()
    else:
        #opt.binary_location = '/usr/local/bin/chromedriver'
        opt.add_argument('no-sandbox')   # root account need this
        opt.add_argument('disable-dev-shm-usage')
        opt.add_argument('--disable-gpu')
        opt.add_argument('blink-settings=imagesEnabled=false')
        # opt.add_argument("--remote-debugging-port=9223")
        # opt.add_experimental_option('useAutomationExtension', False)
        # opt.add_experimental_option('excludeSwitches', ['enable-automation'])
        wd=webdriver.Chrome(options=opt, executable_path='/opt/google/chrome/chromedriver') # NO UI setting
        
    wd.implicitly_wait(5)
    #wd.set_page_load_timeout(10)

    # open
    url = 'https://www.pdawiki.com/forum/'
    wd.get(url)
    wd.page_source.encode('utf-8')

    input_usernanme = wd.find_element_by_xpath('//*[@id="ls_username"]')
    input_usernanme.send_keys('howdyhappy')

    input_passwd = wd.find_element_by_xpath('//*[@id="ls_password"]')
    input_passwd.send_keys('v34')

    input_login = wd.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button')
    input_login.click()

    time.sleep(3)

    try:
        input_sing = wd.find_element_by_xpath('//*[@id="mn_N462e"]/a')   # click sign label
        input_sing.send_keys(Keys.ENTER)
        time.sleep(1)
    except:
        print('##### err.....')
    finally:
        print('continue.....')

    input_dont = wd.find_element_by_xpath('//*[@id="qiandao"]/table[2]/tbody/tr[1]/td/label[3]/input')  # I don't gonna write text
    input_dont.click()

    time.sleep(1)

    input_raku_img = wd.find_element_by_xpath('//*[@id="kx"]/center/img')
    input_raku_img.click()

    time.sleep(1)
    
    input_sign_img = wd.find_element_by_xpath('//*[@id="qiandao"]/table[1]/tbody/tr/td/div/a/img')
    input_sign_img.click()
    
    time.sleep(1)

    print('success sign!')

    wd.quit()


```



```
# 新版api 改动：
input_usernanme = wd.find_element('xpath', '//*[@id="ls_username"]')

```



## chatgpt 网页模拟api

[土法绕过ChatGPT](https://www.bilibili.com/read/cv20610733)

```
# coding=utf-8

import os
import pytest
import time
import json
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 以下为启动Chrome，并打开调试端口、新建配置文件的命令行。按需修改和调用
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\Public\ChromeData"

# 打印日志
def log(str=""):
  print("[%s] %s" % (datetime.datetime.now(), str))

class ChatGPT(object):
  # 初始化，连接开了本地端口调试的Chrome浏览器
  def init(self, port):
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:%d" % port)
    log("尝试在端口 %d 上连接浏览器" % port)
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    # 该对象在生命周期内已收回复数
    self.reply_cnt = 0
    # self.reply_cnt的备份。重新生成时会用到，便于回溯。
    self.reply_cnt_old = 0

  # 关闭
  def close(self):
    self.driver.quit()

  # 打开ChatGPT网页。
  # 参数：
  # 1.delay:等待网页加载的秒数
  # 2.refresh:设为True，则强制Chrome重新载入网页。但会频繁触发CloudFlare。
  #    设为False，则什么都不做。但需要事先将浏览器开好。我是将ChatGPT设成了首页
  def open(self, delay=3, refresh=False):
    self.reply_cnt = 0
    self.reply_cnt_old = 0
    log("打开ChatGPT网页中...")
    if refresh:
      self.driver.get("https://chat.openai.com")
    time.sleep(delay)
    log("完成")

  # 向ChatGPT发送文本。delay为每个步骤间延迟的秒数。
  def send(self, str="你好", delay=0.25):
    self.reply_cnt_old = self.reply_cnt
    # 点击文本框
    txtbox = self.driver.find_element(By.CSS_SELECTOR, ".m-0")
    txtbox.click()
    time.sleep(delay)
    # 输入文本，需处理换行
    log("发送内容:"+repr(str))
    txtlines = str.split('\n')
    for txt in txtlines:
      txtbox.send_keys(txt)
      time.sleep(delay)
      txtbox.send_keys(Keys.SHIFT, Keys.ENTER)
      time.sleep(delay)
    # 发送
    txtbox.send_keys(Keys.ENTER)
    time.sleep(delay)

  # 重新生成
  def regenerate(self):
    self.reply_cnt = self.reply_cnt_old
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

  # 获取最近一条回复。
  # timeout为超时秒数
  def getLastReply(self, timeout = 90):
    log("等待回复中...")
    time_cnt = 0
    reply_str = ""
    # 判断ChatGPT是否正忙
    while self.driver.find_elements(By.CSS_SELECTOR, ".result-streaming") != []:

      if time_cnt >= timeout:
        reply_str += "【超过时间阈值%d秒" % timeout
        elemList = self.getReplyList()
        if len(elemList) <= self.reply_cnt:
          reply_str += "，未收到任何有效回复】"
          return reply_str, False
        else:
          reply_str += "，以下是收到的部分回复】\n"
          break

      time.sleep(1)
      time_cnt = time_cnt + 1

    elemList = self.getReplyList()
    if len(elemList) <= self.reply_cnt:
      return "【发生不可描述错误，未收到任何有效回复】", False

    for i in range (self.reply_cnt, len(elemList)):
      reply_str += elemList[i].text
      reply_str += "\n"

    log(reply_str)
    self.reply_cnt = len(elemList)
    return reply_str, True

  # 获取ChatGPT回复列表
  def getReplyList(self):
    return self.driver.find_elements(By.CSS_SELECTOR, ".markdown > p")

if __name__=="__main__":
  chatgpt = ChatGPT()
  chatgpt.init(9222)
  chatgpt.open()
  while True:
    str = input("=====================\n请输入内容，Ctrl+Q重开，Ctrl+R重新生成，Ctrl+C退出\n>>> ")
    if str.find(chr(17)) > -1:
      chatgpt.open(refresh=True)
    elif str.find(chr(18)) > -1:
      chatgpt.regenerate()
    else:
      chatgpt.send(str=str)
    chatgpt.getLastReply() 
    
```



## 滚动截屏

```
see huggingface/video-subtitle-extractor
```





# pyqt

https://github.com/fandesfyf/JamVideoPlayer  qt 视频播放器



see  huggingface\video-subtitle-extractor\readme.txt



# uvicorn

see https://huggingface.co/spaces/ronvolutional/ai-pokemon-card 宝可梦卡片生成

see https://github.com/pagefaultgames/pokerogue  宝可梦游戏



```
# 内存泄露
gunicorn 加参数 --max-requests 1000 试试
(每个 worker 接收到 1000 次请求后就重启一个新的)

你自己测试一下 max-requests 用 500 、1000 、5000 、10000 哪个更优化。
```





```
uvicorn.subprocess.spawn 要加上 freeze_support
```



```
# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


uvicorn app:app --reload
# app:app 指的是 文件名:FastAPI实例变量名，--reload 参数使得服务器在代码改变时自动重载。

```



## databases

https://github.com/encode/databases 异步查 db



# Gradio

see https://huggingface.co/spaces/dlxjj/rwkv5-jp-explain

see https://github.com/gradio-app/gradio/issues/1349 auto play

see https://github.com/gradio-app/gradio/issues/2945 **subtitle** [1](https://github.com/tomchang25/gradio/tree/main/demo/video_subtitle)

see https://github.com/gradio-app/gradio/issues/7383 高亮文本

see https://github.com/gradio-app/gradio/issues/6971 文字转图片

see https://github.com/gradio-app/gradio/issues/6763  使用 ImageDraw 画图

see https://github.com/gradio-app/gradio/pull/7192 网络图片

see https://github.com/gradio-app/gradio/issues/6851 Gallery

see https://www.gradio.app/main/docs/js/video  **js引用视频组件的方法**

- see Lib\site-packages\gradio\processing_utils.py **音视频处理**

see https://huggingface.co/spaces/Accel/media-converter **视频转换** [1](https://github.com/gradio-app/gradio/pull/2003)

see https://github.com/lazarusking/gradio-ffmpeg 视频转换

see https://github.com/kkroening/ffmpeg-python/tree/master/examples  **视频混剪** 

see https://juejin.cn/post/7201506099342082105  **关键帧信息** **必看**

see https://github.com/remotion-dev/remotion  **videos programmatically with React**

see https://github.com/mifi/lossless-cut js 剪视频

see https://github.com/mean00/avidemux2 视频编辑

see https://github.com/gradio-app/gradio/issues/2894 嵌入 youbu 视频

- https://www.gradio.app/changelog   **最新 api**

see [custom Gradio components](https://github.com/gradio-app/gradio/issues/6802) **自定义组件** 必看 [1](https://github.com/gradio-app/gradio/wiki/%F0%9F%8E%A8-How-to-Make-a-Gradio-Custom-Component) [svelte](https://learn.svelte.dev/tutorial/your-first-component) [svelte2](https://www.v2ex.com/t/760112) [svelte3](https://juejin.cn/post/7121759118070644772) [组件库分享](https://www.gradio.app/custom-components/gallery)

see https://www.gradio.app/guides/custom-CSS-and-JS  修改 css 和 javascript

see https://github.com/gradio-app/gradio/issues/6101  hotkey

see https://github.com/gradio-app/gradio/issues/5053  开新线程

see https://github.com/gradio-app/gradio/blob/main/CONTRIBUTING.md  开发者环境安装

- ```
  apt install pollen
  
  ssh -CNg -L 6006:127.0.0.1:6006 root@connect.bjb1.seetacloud.com -p 53862
  http://localhost:6006
  	# 成功访问 gradio
  
  requirements.txt
  
  pre-requirements.txt
  	https://github.com/snehankekre/streamlit-video-subtitles-poc/raw/main/streamlit-1.28.0-py2.py3-none-any.whl
  	
  packages.txt
  	ffmpeg
  
  -i https://pypi.tuna.tsinghua.edu.cn/simple
  
  vi ~/.pip/pip.conf
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  
  ```

.queue().launch()
  ```

  curl -fsSL https://get.pnpm.io/install.sh | sh -
  	# linux
  	ln -s /root/.local/share/pnpm/pnpm  /usr/bin/pnpm
  
  version=v20.11.1 && 
wget https://nodejs.org/download/release/$version/node-$version-linux-x64.tar.gz && 
tar xvf node-$version-linux-x64.tar.gz && 
cd node-$version-linux-x64/bin && 
chmod +x node npm npx && 
cd ../.. && 
mv node-$version-linux-x64 /usr/local && 
ln -s /usr/local/node-$version-linux-x64/bin/node /usr/local/bin/node && 
ln -s /usr/local/node-$version-linux-x64/bin/npm /usr/local/bin/npm && 
ln -s /usr/local/node-$version-linux-x64/bin/npx /usr/local/bin/npx
	# see docker summary.md -> ubuntu 20.04
	
VERSION=3.10.13 && 
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && 
tar -xf Python-${VERSION}.tgz && 
cd Python-${VERSION} && 
./configure --with-openssl="/usr" && 
make clean && 
make -j 8 && 
make altinstall &&
ln -s /usr/local/bin/pip3.10 /usr/bin/pip &&
ln -s /usr/local/bin/python3.10 /usr/bin/python  
  
pnpm --version && 
node --version && 
python --version && 
pip --version
  
  
pip uninstall -y markupsafe && 
pip install markupsafe==2.0.1 &&

pip uninstall -y jinja2 && 
pip install jinja2==3.1.2


  
- ```
  
  # vscode 设置 -> 搜:
  allowBreakpointsEverywhere
  
  vscdoe 插件
  	JavaScript Debugger
  	Svelte for VS Code
  
  .vscode/launch.json  
  {
      "version": "0.2.0",
      "configurations": [
          {
              "type": "chrome",
              "request": "launch",
              "name": "Launch Chrome against localhost",
              "url": "http://localhost:5174",
              "webRoot": "${workspaceFolder}"
          }
      ]
  }
  	# 正常进断点需要这个
  

vi ~/.bashrc
alias setproxy="export ALL_PROXY=http://172.16.6.253:8118"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"
	# http 代理, 用 privoxy 转 shocks5, see nodejs summary.md -> 抱抱脸
	# curl 正常  
  	
  	
  git lfs clone https://huggingface.co/datasets/dlxjj/gradio
  
  git-lfs 3.4.0         
  	# 这个片本正常

  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && \
  apt-get install git-lfs
  	
  wget https://github.com/git-lfs/git-lfs/releases/download/v3.4.0/git-lfs-linux-amd64-v3.4.0.tar.gz
  	# 这样装才行
  	# ok 这样设置 .gitconfig 后就正常了
  	
  see python 3 summary.md -> Gradio
  
  apt install pollen 
  
  bash scripts/install_gradio.sh && \
  bash scripts/build_frontend.sh && \
  bash scripts/install_test_requirements.sh
  	# 可以在 bash 后加 proxychain4 , 成功安装
  	# .bashrc 里的代理，开了也不得行
  
  ln -s /root/miniconda3/bin/gradio /usr/bin/gradio
  gradio cc install
  
  
  gr.HTML() 只用于显示，不能够交互
  
  conda create -n space pip python=3.10 -y && \
  conda activate space
  
  conda env remove -n space2
  
  pip install gradio==4.19.2
  	# pip install gradio==4.16.0
  	# 当前稳定使用的是 4.14.0
  
  
  iwr https://get.pnpm.io/install.ps1 -useb | iex
  	# powershell 执行
  
  curl -fsSL https://get.pnpm.io/install.sh | sh -
  	# linux
  	ln -s /root/.local/share/pnpm/pnpm  /usr/bin/pnpm

  
  https://github.com/gradio-app/gradio/wiki/%F0%9F%8E%A8-How-to-Make-a-Gradio-Custom-Component
  
  see Python3 Summary.md -> Gradio -> svelte -> vite
  
  pip install gradio==4.19.2
  
  gradio cc create template_video --template Video --install
      # power shell 运行不了出错
  
  cd template_video
  
  gradio cc install
  
  gradio cc dev
  
  gradio cc build
  	# 安装 python3.10
  	# pip3 install gradio==4.19.2
  	# pip3 install twine==5.0.0
                  # apt update && apt install python3.10-venv
  		# yum install python3-virtualenv
  	# /usr/bin/python -m build /root/template_video
  	    # 成功编译前端后有一个子命令，这是编译后端
  	    # ERROR Failed to create venv. Maybe try installing virtualenv.  报错
  	
  	# 成功编译！ ubuntu20.04 almalinux 9 都 ok
  
  	almalinux 9 本机能成功运行 gradio cc dev  template_video
  	    # 好像是 windows 的浏览器不行？
  
  	解决方案：
  		vscode 连过去 almalinux 9，运行 demo/app.py
  		almalinux 9 打开前端，它能正常运行，调试是在本机调试
  
  pnpm i
  
  
  pnpm create vite vite-svelte -- --template svelte
  cd vite-svelte
  pnpm install
  pnpm run dev
      # vite 有几个选项，选 svelte ，选 javascript
  	# vsocde 里 F5 能正常在 Counter.svelte 单步断下
  
  
  gradio cc create ivideo --template Video
  	# 自定义gradio 的 video 组件
  	#　把 frontend 下　node_modules shared　这两个文件夹复到 vite_gradio_video 目录下，能正常引用，并运行
          # 把 dependencies 下的包复制过来， pnpm i 就可以了 
  
  
  App.svelte
  <script>
    import Counter from './lib/Counter.svelte'
    import Player from '../shared/Player.svelte';
  	# 这样引用组件
  	
  
  
  gradio cc create RichTextbox --template SimpleTextbox --install
  	# 新组件必须是在基础组件上改的
  	
  @gradio/video
  
  cd richtextbox
  
  gradio cc dev
  	# 4.16.0 + linux 成功运行
  	
  vscode + wsl2
  	# http://127.0.0.1:7860 成功运行 demo, 127.0.0.1 自动转到 wsl 的 ip
      
  /root/gradio/gradio/components/video.py
  	# 在这里下断点, 运行 /demo/video_component/run.py 成功断下
  
  gradio cc build
  
  
  demo.queue().launch(server_name='0.0.0.0', server_port=7890, share=True, inbrowser=True) 
  	# vscode ssh 隧道连接了本机和远程的地址, 本地 127.0.0.1:7890 可以访问远程
  
  
  
  
  docker run -tid --name gradio_server_6116 -p 222:22 -p 3389:3389  -p 6116:6116 --privileged=true ubuntu:20.04 /bin/bash
  
  docker start gradio_server_6116
  docker exec -it gradio_server_6116 bash
  
  docker cp proxychains-ng-master.zip gradio_server_6116:/root
  
  sudo passwd
  	# 改密码
  
  # 移除容器
  docker ps -a
  docker stop 17b3d18c1428
  docker rm 17b3d18c1428
  
  
  ufw disable && \
  apt install openssh-server -y && \
  mkdir -p /var/run/sshd && \
  /usr/sbin/sshd -D &
  	# docker 的 ssh 这样启动
  	# lsof -i:22
  
  
  vi ~/.bashrc
  alias setproxy="export ALL_PROXY=socks5h://172.16.6.185:1080"
  alias unsetproxy="unset ALL_PROXY"
  alias ip="curl http://ip-api.com/json/?lang=zh-CN"
  	# curl 正常, git 连 huggingface 不能行
  	# 不要整这个了
  unsetproxy && \
  pip install pysocks && \
  setproxy && \
  ip
  
  
  git config --global user.name "dlxjj" && \
  git config --global user.email "12345@qq.com"
  git config --global http.proxy  socks5h://172.16.6.185:1080 && \
  git config --global https.proxy socks5h://172.16.6.185:1080
  
  .gitconfig
  [credential]
          helper = store
  [user]
          name = dlxjj
          email = 12345@qq.com
  
  [http]
          proxy = socks5h://127.0.0.1:1080
  [https]
          proxy = socks5h://127.0.0.1:1080
  
  # 不知道为什么，必须换 socks5h 才能正常　clone github
  # 但是！git lfs pull 不能行
  	# 把 socks5h 改成 socks5 就正常了 ?
  
  
  pip install huggingface_hub && \
  git config --global credential.helper store && \
  huggingface-cli login
  
  huggingface-cli whoami
  	# ssl 错误是由那个系统代理引起的，unsetproxy 就不错了
  
  
  ```

see https://huggingface.co/spaces/freddyaboulton/gradio_pdf 显示 pdf 的组件

see https://huggingface.co/spaces/fffiloni/MAGNet 音乐生成

see https://github.com/R3gm/SoniTranslate 视频语音翻译





## 成品

```

tar xvf  /mnt/f/Downloads/miniconda3.tar

tar zxvf /mnt/f/Downloads/gradio.tar.gz

bash scripts/install_gradio.sh
pnpm install

cd demo/image_editor
python run.py
pnpm dev
	# 打开前端地址就可以了

```



## compile

https://github.com/gradio-app/gradio/pull/7660  必看 编译 js 运行方法

https://www.gradio.app/guides/developing-faster-with-reload-mode 必看 热调试方法

https://github.com/gradio-app/gradio/blob/main/js/README.md 前端调试看这里

- ```
  
  proxychains4 pip install build && 
  proxychains4 bash ./build_pypi.sh
  	# 生成 gradio-4.16.0-py3-none-any.whl 用于安装
  	# 需要网络的命令全给它加上代理，比全局代理好使
  
  cd /root/huggingface/gradio440 && pnpm i --frozen-lockfile --ignore-scripts && 
  cd js/video && pnpm i --frozen-lockfile --ignore-scripts
  	# 修改原生组件需要这样安装依赖
  	# 出错的话就直接 pnpm i
  
  cd /root/huggingface/gradio/js/imageeditor
  gradio run.py # 默认它会找demo 作入口点
  gradio run.py my_demo # 自定义入口点
  gradio run.py --name Gretel  # 这样传参
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("--name", type=str, default="User")
  args, unknown = parser.parse_known_args()
  	# 接收参数
  
  pnpm dev
  	# 会启动前端，好像还能热重载 js 文件的修改？确实可以！
  	# 前提是先 gradio run.py 启动后端，再 pnpm dev 启动前端！
  
  pnpm build
  	# 生成 js/app/public 和 gradio/templates/frontend
  
  pnpm format:check
  	# 缩进检查
  	
  pnpm format:write
  	# 修正错误的缩进
  
  pnpm ts:check
  	# 类型检查
  
  
  ```
  pip install -r demo/outbreak_forecast/requirements.txt
  pnpm exec playwright install chromium
  pnpm exec playwright install-deps chromium
  pnpm test:browser:full
  
  ```
  
  
  ```
  
- ```
  pnpm --filter @gradio/app build:lite
  python -m http.server --directory js/lite
  
  bash scripts/run_all_tests.sh
  bash scripts/format_backend.sh
  bash scripts/format_frontend.sh
  ```

  

```


apt install pollen 

pip install -r requirements.txt
pnpm install
pnpm build

pip install build && 
bash build_pypi.sh
	# 编译整 gradio 本身

apt install python3.10-dev && 
apt install libcairo2-dev
	# gradio_4290 安装依赖时需要装这两个, 不然缺 python.h

bash scripts/install_gradio.sh && \
bash scripts/build_frontend.sh && \
bash scripts/install_test_requirements.sh
	# 这个会装 cuda ，不要运行这个

# gradio/package.json
"scripts": {
	"test": "pnpm --filter @gradio/client build && vitest dev --config .config/vitest.config.ts",
	
	
npm run test
	# 正常是这样运行

pnpm --filter @gradio/client build
pnpm vitest dev --config .config/vitest.config.ts
	# pnpm 单独运行


pnpm vitest dev --config .config/vitest.config.ts  js/video/Video.test.ts
	# 单独测试一个文件


```



### vscode+gradio

```
  {
      "version": "0.2.0",
    "configurations": [
          {
              "name": "Python Debugger: Current File",
              "type": "debugpy",
              "request": "launch",
              "program": "${file}",
              "console": "integratedTerminal"
          }
      ]
  }
  
  cd /root/huggingface/gradio && pnpm i --frozen-lockfile --ignore-scripts && 
cd js/video && pnpm i --frozen-lockfile --ignore-scripts
	# 修改原生组件需要这样安装依赖
  
  # python 直接运行 run.py 就可以直接断下了
  # 前端用 cd demo/xx && pnpm dev
  # {interactive} 直接在页面上显示变量的值
  
  
  
{
    "configurations": [
        {
            "type": "chrome",
            "request": "launch",
            "name": "Launch Chrome against localhost",
            "url": "http://localhost:9876",
            "webRoot": "${workspaceFolder}"
        }
    ]
}
// cd demo/image_editor && conda activate gradio && python run.py 
// cd demo/image_editor && conda activate gradio && pnpm dev
    // 只有这样运行，它的前端端口才是 9876
// vscode F5 


# gradio/js/imageeditor/shared/tools/Tools.svelte
	line 76 下断点
	register_tool: (type: tool, meta: ToolMeta) => {
# 前端代码可以成功断下
# cd gradio/demo/image_editor
# python run.py # 启动后端
# pnpm dev # 运行前端
# vscode 按 F5，启动浏览器


wslconfig  /setdefault Ubuntu-20.04
	# 默认启动 20.04
	# 20.04 用于修改编译 gradio, 生成 gradio-xxx-py3-none-any.whl

wslconfig  /setdefault Ubuntu-22.04
	# 默认启动 22.04
	# 22.04 用于 使用安装 gradio-xxx-py3-none-any.whl 并测试，以及实际开发
	
wsl --install -d Ubuntu-22.04
	# 再装一个 22.04

ubuntu2204 config --default-user root
	# 默认以 root 登录

  
  // {
  //     "version": "0.2.0",
  //     "configurations": [
  //         {
  //             "name": "Python Debugger: Current File",
  //             "type": "debugpy",
  //             "request": "launch",
  //             "program": "/root/miniconda3/bin/gradio",
  //             "console": "integratedTerminal",
  //             "args": [
  //                 "${file}"
  //             ]
  
  //         }
  //     ]
  // }
```



### 热重载

https://www.gradio.app/guides/developing-faster-with-reload-mode



## compoment



### mypdf

```

proxychains4 gradio cc create mypdf
cd mypdf && 
conda activate gradio440 
proxychains4 gradio cc install
gradio cc dev
proxychains4  gradio cc build
	# 成功生成 whl 
	

下一步把它移值到 gradio440，因为只有源码编译才能单频调试！


改成复制 gradio440 的 image 组件，名字改为 myimage
	# 注意要复制几个地方
	
	demo/myimage_component
		# 复制这个文件
	
	/root/huggingface/gradio440/gradio/components/__init__.py
		from gradio.components.image import Image
		from gradio.components.myimage import MyImage 
			# 加这一行
	
	gradio/components/myimage.py
		# 复制这个文件
		
		
	gradio/__init__.py
	from gradio.components import (
    	Image,
    	MyImage,
    		# 加这一行
    		
    js/myimage
    	# 复制
    	
    package.json
    	"@gradio/image": "workspace:^",
		"@gradio/myimage": "workspace:^",
    		# 加这一行
    
proxychains4 pnpm i
	# 重要
proxychains4 bash ./build_pypi.sh
	# 成功

cd demo/myimage_component && 
python run.py
	# 成功打开前端


```





### vsocde 附加调试 gradio

````

cd /root/huggingface/gradio && pnpm i --frozen-lockfile --ignore-scripts && 
cd js/video && pnpm i --frozen-lockfile --ignore-scripts
	# 修改原生组件需要这样安装依赖

# see huggingface/myvideo/readme.txt
vsocde 成功附加调试 demo/app.py
    1. vscode 打开目录 myvideo
    2. app.py line 72 行下断点： [ begintime, endtime, videoBase64UrlEndcode ] = evt._data
    3. myvideo 目录下运行 gradio cc dev
    4. .vscode/launch.json 让它空着，什么都别配置, F5 -> 选附加到进程选 xxx/python -u xx/app.py 的进程
    5. chrome 打开 http://127.0.0.1:7861, 点视频上的剪功按钮, 剪一下段然后点 A-B 按钮
    6. app.py 成功断下


conda create -n space pip python=3.10 && 
conda activate space && 
curl -fsSL https://get.pnpm.io/install.sh | sh - &&
ln -s /root/.local/share/pnpm/pnpm  /usr/bin/pnpm
	# 用康达稳一点？同名的两个定定义组件好像也会互相影响
	# pnpm root -g
	# rm -rf /root/.local/share/pnpm
	# 删除后重装，相当于升级
		# https://github.com/pnpm/pnpm/releases/download/v9.1.1/pnpm-linux-x64
			# 真实下载地址
			# vi install.sh 加一句  printf '%s' "${archive_url}"
			# ./pnpm-linux-x64 setup --force # 安装 
			# mv /root/.local/share/pnpm/pnpm-linux-x64 /root/.local/share/pnpm/pnpm

conda create -n rwkv pip python=3.10 && 
conda activate rwkv
	# 组件制作好了以后给 rwkv 用 
	

curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && \
apt-get install git-lfs

source ~/miniforge3/etc/profile.d/conda.sh
vi ~/bashrc
	# 加进去

conda deactivate && 
rm -rf /root/miniforge3/envs/space
	# conda env remove -n sapce
	# 这个删不掉

wsl --shutdown


pip install gradio==4.22.0
	# 这版 video 组件正常运行
	# pip freeze > freeze.txt

unsetproxy &&
pip install pysocks
	# 开代理需要先装这个

pip install --upgrade requests
	# 运行出警告的话装这个
	
gradio cc create mysimpletextbox --template SimpleTextbox && \
cd mysimpletextbox && \
gradio cc install && \
gradio cc dev
gradio cc build # 生成 .whl 可以安装使用
	# 成功运行，点　Frontend Server (Go here): http://localhost:7861/ 
	# 打开浏览器
	# 注意：只有自已编译的完整 gradio 目录下，才可以用vscode 直接运行demo下的app.py，此时它是没有前端地址的，浏览器直接打开那个地址就可以了

mysimpletextbox/frontend/Index.svelte
e.key === "Enter" && e.shiftKey
	# 改成这样，它要在 textbox 获得焦点的时侯按 sift + enter ，才能成功触发




gradio cc create myvideo --template Video && \
cd myvideo && \
gradio cc install && \
gradio cc dev

"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4"


gradio cc create myimageeditor --template ImageEditor
AnnotatedImage
ImageEditor

/root/miniforge3/envs/rwkv/lib/python3.10/site-packages/gradio/components
image_editor.py
	# 报错原因：根据它的拼写规则，本来应该是这个文件名imageeditor.py，实际上是这个 image_editor.py
	# 解决办法：复制一个 imageeditor.py 出来也可以
	# 运行不报错，前端出不来

gradio cc create myimageeditor --template SimpleTextbox && \
cd myimageeditor && \
gradio cc install && \
gradio cc dev
	# 拿它来改一下，搬运 gradio 的代码过来改
	
	
https://github.com/gradio-app/gradio/pull/6747
	# 这问题已经有 PR 了，他就是不合并
	
gradio/gradio/cli/commands/components/_create_utils.py
83 行开始，改成这样：
    "HTML": ComponentFiles(template="HTML", demo_code=static_only_demo_code),
    "ImageEditor": ComponentFiles(
        template="ImageEditor", python_file_name="image_editor.py"
    ),
    "Label": ComponentFiles(template="Label", demo_code=static_only_demo_code),

	gradio cc create myimageeditor --template ImageEditor
		# 改完可以成功安装

/root/miniforge3/envs/rwkv/lib/python3.10/site-packages/gradio/cli/commands/components/_create_utils.py
def _create_backend(
    if component.python_file_name == 'imageeditor.py':
        component.python_file_name = "image_editor.py"
        	# 解决方法，hack 一下下
    shutil.copy(
        str(p / module / component.python_file_name),
        str(python_file),
    )
	# 成功！


/usr/local/lib/python3.10/dist-packages/gradio/cli/commands/components/_create_utils.py
	# if not correct_cased_template:
	# 模板找不到的报错代码在这里 
	

	# /root/miniforge3/envs/rwkv/lib/python3.10/site-packages/gradio/cli/commands/components/_create_utils.py:321
	# 出错，看这里

gradio/components/image_editor.py
	class ImageEditor(Component):
		# 他要 Python 里的类名

/usr/local/lib/python3.10/dist-packages/gradio/cli/commands/components/create.py
	# Component to use as a template. Should use exact name of python class.


/root/miniforge3/envs/rwkv/bin/gradio
	# 入口点看这里

    sys.argv.append( 'cc' )
    sys.argv.append( 'create' )
    sys.argv.append( 'myvideo' )
    sys.argv.append( '--template' )
    sys.argv.append( 'Video' )
    	# 加这个单步运行看看


/usr/local/lib/python3.10/dist-packages/gradio/cli/cli.py
	# 直接爆力修改，运行这个
	if __name__ == '__main__':
    
    sys.argv[0] = '/root/miniforge3/envs/rwkv/bin/gradio'
    sys.argv.append( 'cc' )
    sys.argv.append( 'create' )
    sys.argv.append( 'myvideo' )
    sys.argv.append( '--template' )
    sys.argv.append( 'Video' )
    
    #sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    
    cli()


# kill 端口号

```


```
nohup node xx.js >outlog &

#!/bin/bash
kill -9 $(lsof outlog | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:7860 | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:7861 | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')
```

```

Python311\Lib\site-packages\gradio\networking.py
	LOCALHOST_NAME = os.getenv("GRADIO_SERVER_NAME", "127.0.0.1")
		# 默认它会取环境变量
		

ssh -CNg -L 7861:127.0.0.1:7861 root@172.16.6.253 -p 22

````



### \--python-path \--gradio-path

```
gradio cc dev --python-path /home/carlosz/miniconda3/envs/AIenv/bin/python --gradio-path /home/carlosz/miniconda3/envs/AIenv/bin/gradio
```





### kill

```
# kill.sh
kill -9 $(lsof -i:7860 | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:7861 | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:7862 | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:7863 | tail -n +2   |  awk '{print $2}' | tr '\n' ' ')

```



## multiple pages

https://github.com/gradio-app/gradio/issues/3806

- https://github.com/gradio-app/gradio/issues/2654

```
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import gradio as gr

app = FastAPI()

HELLO_ROUTE = "/hello"
GOODBYE_ROUTE = "/goodbye"
iframe_dimensions = "height=300px width=1000px"

index_html = f'''
<h1>Put header here</h1>

<h3>
You can mount multiple gradio apps on a single FastAPI object for a multi-page app.
However if you mount a gradio app downstream of another gradio app, the downstream
apps will be stuck loading. 
</h3>

<h3>
So in particular if you mount a gradio app at the index route "/", then all your 
other mounted gradio apps will be stuck loading. But don't worry, you can still embed
your downstream gradio apps into the index route using iframes like I do here. In fact,
you probably want to do this anyway since its your index page, which you want to detail 
more fully with a jinja template. 
For a full example, you can see my <a href=https://yfu.one/>generative avatar webapp</a>
</h3>

<div>
<iframe src={HELLO_ROUTE} {iframe_dimensions}></iframe>
</div>

<div>
<iframe src={GOODBYE_ROUTE} {iframe_dimensions}></iframe>
</div>

'''

@app.get("/", response_class=HTMLResponse)
def index():
    return index_html


hello_app = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
goodbye_app = gr.Interface(lambda x: "Goodbye, " + x + "!", "textbox", "textbox")


app = gr.mount_gradio_app(app, hello_app, path=HELLO_ROUTE)
app = gr.mount_gradio_app(app, goodbye_app, path=GOODBYE_ROUTE)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
```





## docker部署

https://huggingface.co/spaces/freddyaboulton/gradio_pdf  范例 **必看**

https://huggingface.co/docs/hub/spaces-sdks-docker



```
# Dockerfile
FROM ubuntu:22.04

RUN set -x; apt-get update; apt install python3.10-dev libcairo2-dev curl ffmpeg -y

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.10 get-pip.py

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python3.10", "main.py"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]


# main.py
import gradio as gr
from gradio import processing_utils

shortcut_js = """
<script>
function shortcuts(e) {
    var event = document.all ? window.event : e;
    switch (e.target.tagName.toLowerCase()) {
        case "input":
        case "textarea":
        case "select":
        case "button":
        break;
        default:
        if (e.code == "KeyS" && e.shiftKey) {
            document.getElementById("btn_search_jisho").click();
        }
}
}
document.addEventListener('keyup', shortcuts, false);
</script>
"""

title = "rwkv5-jp-explain"
with gr.Blocks(title=title, head=shortcut_js) as demo:
    gr.HTML(f"<div style=\"text-align: center;\">\n<h1>RWKV-5 training 50 epoch for anime and game text - {title}</h1>\n</div>")
    
demo.queue(max_size=10)
demo.launch(server_name='0.0.0.0', share=False, inbrowser=True)
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World!"}


# requirements.txt
--extra-index-url https://download.pytorch.org/whl/cpu
torch==1.13.1+cpu
numpy==1.26.4
https://huggingface.co/datasets/dlxjj/release/resolve/main/gradio-4.29.0-py3-none-any.whl
https://huggingface.co/datasets/dlxjj/release/resolve/main/gradio_myvideo-0.0.2-py3-none-any.whl
opencv-python==4.9.0.80
openai==1.12.0
google-ai-generativelanguage==0.4.0
google-api-core==2.18.0
google-auth==2.29.0
google-generativeai==0.4.1
googleapis-common-protos==1.63.0
gTTS==2.5.1
fastapi
requests
sentencepiece
transformers
uvicorn[standard]


# README.md
---
title: Rwkv5 Jp Explain Docker
emoji: 🦀
colorFrom: red
colorTo: red
sdk: docker
app_port: 7860
pinned: false
---


```









## change

```python
import gradio as gr
from gradio_rich_textbox import RichTextbox


examples = [ 
    ['[b]Hello!![/b]']
] 

with gr.Blocks(title="richBox") as demo:
    with gr.Row():
        with gr.Column():
            box1 = RichTextbox(label="in", interactive=True)
        with gr.Column():
            box2 = RichTextbox(label="out", interactive=False)

    data = gr.Dataset(components=[box1], samples=examples, label="Example bbcode", headers=["bbcode"])
    data.click(lambda x: x[0], [data], [box1])

    box1.change(lambda x:x, box1, box2) # 同步更新

# demo = gr.Interface(
#     lambda x:x,
#     RichTextbox(),  # interactive version of your component
#     RichTextbox(),  # static version of your component
#     examples=[[example]],  # uncomment this line to view the "example version" of your component
# )

if __name__ == "__main__":
    demo.launch()
```



### js



```python
see huggingface/gradio440/js/imageeditor/Index.svelte

	function wait_for_next_frame(): Promise<void> {
		return new Promise((resolve) => {
			requestAnimationFrame(() => requestAnimationFrame(() => resolve()));
		});
	}

	async function handle_change(): Promise<void> {
		await wait_for_next_frame();
		
		
	function handle_history_change(): void {
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
			tick().then((_) => (value_is_output = false));
		}
	}
```



## envets

[Custom events](https://www.gradio.app/guides/documenting-custom-components) 

- ```python
  from gradio.events import Events, EventListener
  
  class ParamViewer(Component):
    ...
  
    EVENTS = [
      Events.change,
      EventListener(
          "bingbong",
          doc="This listener is triggered when the user does a bingbong."
        )
    ]
  ```

  



```python
# https://github.com/gradio-app/gradio/issues/7380

import gradio as gr

def test(evt: gr.EventData):
    return str(evt.target)
    

with gr.Blocks() as demo:
    b = gr.Button()
    t = gr.Textbox()
    
    b.click(test, None, t)
    
demo.launch()
```



```python
# https://github.com/gradio-app/gradio/pull/7425

import gradio as gr
import time

def f(x, k: gr.KeyUpData):
    time.sleep(1)
    return gr.update(choices=[f"{k.input_value} {i}" for i in range(int(5))])    


with gr.Blocks() as demo:
    t = gr.Dropdown(interactive=True, allow_custom_value=True)
    t.key_up(f, t, t, show_progress="hidden", trigger_mode="always_last")
    
demo.launch()

```





[event-listeners](https://www.gradio.app/guides/blocks-and-event-listeners#gathering-event-data)

```python
    @gr.on(inputs=[num1, num2, num3], outputs=output)
    def sum(a, b, c):
        return a + b + c
   
    # 三个输入控件任意一个触发 change 就会调用工厂 sum 加工产品，并输出到 output 控件
    
```



### onMount

```python
import { onMount } from "svelte";

	onMount(() => {
		return () => {
			$pixi?.destroy();
			resizer.disconnect();
			for (const k of $contexts) {
				if (k in $reset_context) {
					$reset_context[k]?.();
				}
			}
		};
		# onMount 好像可以返回一个析构函数？ 

```



### load

```python
import gradio as gr
import datetime

on_load="""
async()=>{
    console.log("HELLO");
}
"""
with gr.Blocks() as demo:
    def get_time():
        return datetime.datetime.now().time()
    dt = gr.Textbox(label="Current time")
    demo.load(get_time, inputs=None, outputs=dt, _js=on_load)
demo.launch()
```





### ResizeObserver

```
	let pixi_target: HTMLDivElement;
	let canvas_wrap: HTMLDivElement;
	
	const resizer = new ResizeObserver((entries) => {
			for (const entry of entries) {
				get_dimensions(canvas_wrap, pixi_target);
			}
		});

		resizer.observe(canvas_wrap);
		resizer.observe(pixi_target);
		创建一个新的ResizeObserver对象。ResizeObserver是一个Web API，它主要用于监听并响应HTML元素的大小改变事件。

创建的这个ResizeObserver对象，每当监听的元素的大小发生变化时，它都会执行定义好的回调函数。回调函数的参数entries是一个数组，里面包含了所有被观察元素的相关信息。

对于每个被观察的元素，都会执行get_dimensions函数。这个函数似乎是用来获取一个元素(canvas_wrap)和另一个元素(pixi_target)的尺寸信息
		
```





### change

```python

Inner:
    export let value;

outter:
    <Inner bind:value={value} />


<Inner value={value} />  
<!--如果不加bind，那么子组件修改的只是内部的value变量，父组件的value变量是不会被修改的-->

<Inner bind:value={value} />
<!--加了bind，那么子组件修改了value变量，父组件的value变量也会跟着被修改-->


```

```javascript

<script>
	let user = {
		ageRange: 0
	}
	
	let onChangeAgeRange = 0
	
	const onChange = () => {
		onChangeAgeRange = user.ageRange
	}
</script>

<!-- Swap the bind:value and on:change attributes to break. -->
<select bind:value={user.ageRange} on:change={onChange}>
	<option value={0}>13-16</option>
	<option value={1}>17-19</option>
	<option value={2}>20-22</option>
	<option value={3}>22+</option>
</select>

<p>
	Reactive value {user.ageRange}
</p>

<p>
	On change age range {onChangeAgeRange}
</p>

```



```python
# https://github.com/gradio-app/gradio/issues/7432
import gradio as gr


def on_file_change(file_path):
    print(f"File path changed to {file_path}")


# Set up the Gradio interface
with gr.Blocks(
    title="File explorer value change test"
) as demo:
    file_explorer = gr.FileExplorer(root=".", file_count="single")
    file_explorer.change(fn=on_file_change, inputs=[file_explorer], outputs=[])


demo.launch()



	export let gradio: Gradio<{
		change: never;
	}>;
        
    $: if (JSON.stringify(value) !== JSON.stringify(old_value)) {
		old_value = value;
		gradio.dispatch("change");
	}

        
    on:change={() => gradio.dispatch("change")}

        
    
    export let server: {
		ls: (path: string[]) => Promise<FileNode[]>;
	};
    	{#key rerender_key}
		<DirectoryExplorer
			bind:value
			{file_count}
			{interactive}
			ls_fn={server.ls}
		/>
	{/key}
        
        
       


```



####  动态更新组件数据

```python
    with gr.Tab("SRT"):
      begintime = gr.Textbox(lines=1, label="", value="")
      endtime = gr.Textbox(lines=1, label="", value="")
      subtitle = gr.Textbox(lines=1, label="", value="")
      
      from lib.srt import parse
      with open("videos/netflix/anime/japanese/Touch/Episode 1/Touch_S01E01_Episode 1.Japanese (CC).srt", "r", encoding='UTF-8') as f:
        str = f.read()
      subs = parse(str)
      
      dir_srt = os.path.join(os.path.dirname(__file__), 'videos/netflix/anime/japanese/Touch/Episode 1/')
      file_explorer_srt = gr.FileExplorer(glob="*.srt", root_dir=dir_srt, file_count="single")
      
      dataset_srt = gr.Dataset(components=[begintime, endtime, subtitle], samples=subs, label="SRT", headers=["begintime", "endtime", "subtitle"])
      dataset_srt.click(lambda x: x, [dataset_srt], [begintime, endtime, subtitle])
      
      def ss(evt: gr.SelectData):
        return evt.value
      subtitle.select(ss, None, selected)
      
      def on_change_srt(file_path):
        if not file_path:
          return dataset_srt
        with open(file_path, "r", encoding='UTF-8') as f:
          str = f.read()
        subs = parse(str)
        return gr.update(samples=subs)  
      file_explorer_srt.change(fn=on_change_srt, inputs=[file_explorer_srt], outputs=[dataset_srt])
```



#### 动态显示隐藏组件

```python
see https://github.com/gradio-app/gradio/issues/6466
see https://github.com/gradio-app/gradio/issues/4689
import gradio as gr

def _update_group_components(checkbox_values) :
    update_info = [gr.update(visible=False)] * 4
    for checked in checkbox_values :
        update_info[checked] = gr.update(visible=True)
    return update_info

with gr.Blocks() as demo :
    with gr.Group() as group_components :
        text1 = gr.Textbox(label='Default textbox 1')
        text2 = gr.Textbox(label='Default textbox 2')
        text3 = gr.Textbox(label='Default textbox 3')
        text4 = gr.Textbox(label='Default textbox 4')

    options_checkbox = gr.CheckboxGroup(choices=['a', 'b', 'c', 'd'], type='index', value=['a','b','c','d'])
    options_checkbox.input(fn=_update_group_components,
                           inputs=options_checkbox,
                           outputs=[text1, text2, text3, text4])

demo.launch(debug=True)
```





#### 动态绑定

```python
with gr.Blocks() as demo:
  num1 = gr.Number()
  num2 = gr.Number()
  product = gr.Number(lambda a, b: a * b, inputs=[num1, num2])
	# product 会实时更新成两数的和
```





### AB 复读

```
	// huggingface/myvideo/frontend/shared/VideoControls.svelte
	const handle_change_AB_time__ = (): void => {
		// 获取AB复读起止时间
		processingVideo = true;
		trimVideo(ffmpeg, dragStart, dragEnd, videoElement)
			.then( async (videoBlob) => {

				// to base64 
				// var reader = new FileReader();
				// reader.readAsDataURL(videoBlob);
				// reader.onload = function() {
				// 	processingVideo = false;
				// 	toggleTrimmingMode()
				// 	handle_change_AB_time([dragStart, dragEnd, reader.result])
				// };
				var blob = new Uint8Array(await videoBlob.arrayBuffer())
				handle_change_AB_time([dragStart, dragEnd, blob])
			});
	};


	# huggingface/myvideo/demo/app.py
	def change_ABT(evt: gr.EventData):
        global mp4
        [ begintime, endtime, videoBase64UrlEndcode ] = evt._data
        # if isDebug: print("### change_ABT hit.", evt.target, [ begintime, endtime, videoBase64UrlEndcode ])
        # data:video/mp4;base64, 需要去掉最前面这一段 mime 它才是纯 base64
        # videoBase64 = re.compile(r'^data:.+?;base64,').sub('', videoBase64UrlEndcode)
        # videoBytes = base64.b64decode(videoBase64)
        videoBytes = bytes(list(videoBase64UrlEndcode.values())) # 改成不传 base64 了; 它返回的是字典
        trim_dir = os.path.join( os.path.dirname(mp4), f'{Path(mp4).stem}[trim]' )
        trim_name = f'{Path(mp4).stem}[{begintime}][{endtime}].mp4' # whitout ext
        if not os.path.exists(trim_dir):
            os.makedirs(trim_dir)
            print("Directory '%s' created" % trim_dir)
        print('write bytes:')
        with open(os.path.join(trim_dir, trim_name), "wb") as f:
            f.write(videoBytes)
        
        return evt._data
    out.change_AB_time(change_ABT, None, [])
```





### streaming

https://github.com/gradio-app/gradio/issues/8302



### success

```python
# https://github.com/gradio-app/gradio/pull/3430
import time
import gradio as gr

def fast_event(x):
    if not x:
        raise gr.Error("A Protein must be selected")
    return x

def slow_event(x):
    time.sleep(2)
    return (x + " ")*100

with gr.Blocks() as demo:
    dropdown = gr.Dropdown(["Protein A", "Protein B", "Protein C"])
    textbox = gr.Textbox()
    sequence = gr.Textbox()
    dropdown.change(fast_event, dropdown, textbox).success(slow_event, textbox, sequence)
    textbox.submit(slow_event, textbox, sequence)

demo.launch()
```



### then

```python
import time
import gradio as gr


def slow_event(x):
    time.sleep(2)
    return x

with gr.Blocks() as demo:
    textbox1 = gr.Textbox()
    textbox2 = gr.Textbox()
    textbox3 = gr.Textbox()
    textbox4 = gr.Textbox()
    btn = gr.Button("Cancel", variant="stop")
    
    ev1 = textbox1.submit(slow_event, textbox1, textbox2)
    ev2 = ev1.then(slow_event, textbox2, textbox3)
    ev3 = ev2.then(slow_event, textbox3, textbox4)
    btn.click(None, None, None, cancels=ev2)
    

demo.queue().launch()
```





## 动态UI

https://github.com/gradio-app/gradio/issues/2566

```
with gr.Blocks() as demo:
    gr.Markdown("# Music Mixer")
    gr.Markdown("Add tracks and set their volumes. Then click 'Combine' to mix them!")
    with gr.Row() as control_panel:
        add_track_btn = gr.Button("Add Track")
    with gr.Row() as control_panel:
         track_audio = gr.Audio()

    def add_track():
        children = control_panel.children
        return gr.Row.update(children=children.append(gr.Audio()))
    
     add_track_btn.click(add_track, None, control_panel)
   ...
```





## path

```python
# gradio/demo/file_explorer_component_events/run.py

import gradio as gr
from pathlib import Path

base_root = Path(__file__).parent.resolve()

with gr.Blocks() as demo:
    with gr.Row():
        dd = gr.Dropdown(label="Select File Explorer Root",
                        value=str(base_root / "dir1"),
                        choices=[str(base_root / "dir1"), str(base_root / "dir2"),
                                 str(base_root / "dir3")])
        
# https://github.com/gradio-app/gradio/tree/main/js/fileexplorer
	# 前端看这
   

```



### directory

[选择文件夹](https://github.com/bmaltais/kohya_ss/blob/master/dreambooth_gui.py) 必看

```python
# 选择文件
import gradio as gr

def on_file_change(file_path):
    print(f"File path changed to {file_path}")

with gr.Blocks(
    title="File explorer value change test"
) as demo:
    file_explorer = gr.FileExplorer(root=".", file_count="multiple")
    file_explorer.change(fn=on_file_change, inputs=[file_explorer], outputs=[])

demo.launch()
```



### Upload

```
# see huggingface/gradio/issues/3729/run.py

import gradio as gr

def upload_file(files):
    print("here")
    file_paths = [file.name for file in files]
    return file_paths

with gr.Blocks() as demo:
    file_output = gr.File()
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["image", "video"], file_count="multiple")
    upload_button.upload(upload_file, upload_button, file_output)

demo.launch(debug=True)
```



### allowed_paths



```python
with gr.Blocks(title=title) as demo:
	file_explorer = gr.FileExplorer(root="/root", file_count="multiple")
		# 前端成功显示 root 目录内容 
		
if __name__ == "__main__":
    demo.launch(allowed_paths=["/root"])
```





```python

import gradio as gr

with gr.Blocks() as demo:
    gr.DataFrame([["<audio src='/file=cantina.wav' controls></audio>"]], datatype="markdown")
    
demo.launch(allowed_paths=["cantina.wav"])


Files that you explicitly allow via the allowed_paths parameter in launch(). This parameter allows you to pass in a list of additional directories or exact filepaths you'd like to allow users to have access to. (By default, this parameter is an empty list).

Static files that you explicitly set via the gr.set_static_paths function. This parameter allows you to pass in a list of directories or filenames that will be considered static. This means that they will not be copied to the cache and will be served directly from your computer. This can help save disk space and reduce the time your app takes to launch but be mindful of possible security implications.
```






## yield

```python
# https://github.com/gradio-app/gradio/issues/7615

import gradio as gr
import time

def loop_method(input_number, atb, atb2):
    for i in range(1, 111):
        yield {additional_text_box: i}
        time.sleep(0.5)
        #lets assume some more code here
        yield {additional_text_box2: i*10}
        time.sleep(0.5)

block = gr.Blocks().queue()
with block:
    input_box = gr.Textbox(label="Enter a number (1 to 100):")
    output_box = gr.Textbox(label="Output:", interactive=False)
    loop_button = gr.Button("Run Loop")
    additional_text_box = gr.Textbox(label="Additional Text Box:", interactive=False)
    additional_text_box2 = gr.Textbox(label="Additional Text 2 Box:", interactive=False)

    loop_button.click(fn=loop_method, inputs=[input_box, additional_text_box, additional_text_box2], outputs=[additional_text_box, additional_text_box2])

block.launch()
```





## timer

```python
def get_current_temp():
    .... .....

with gr.Blocks() as demo:
    temperature = gr.Number()
    demo.run_forever(get_current_temp,
                     inputs=None,
                     outputs=temperature,
                     every=1 # units in seconds)
demo.queue().launch()
```



## hotkey

```python
import gradio as gr

def main() -> None:
    shortcut_js = """
<script>
function shortcuts(e) {
    var event = document.all ? window.event : e;
    switch (e.target.tagName.toLowerCase()) {
        case "input":
        case "textarea":
        case "select":
        case "button":
        break;
        default:
        if (e.code == "KeyS" && e.shiftKey) {
            document.getElementById("my_btn").click();
        }
}
}
document.addEventListener('keyup', shortcuts, false);
</script>
"""

    with gr.Blocks(head=shortcut_js) as demo:
        input = gr.Textbox(lines=2, label="in", value="hi")
        output = gr.Textbox(lines=2, label="Prompt", value="<User:>ここまでやるとはな<User$>\n\n")
        sync_btn = gr.Button(value="Sync", elem_id="my_btn")
        sync_btn.click(lambda x:x, input, output)

    demo.queue(max_size=10)
    demo.launch(share=False)

if __name__ == "__main__":
    main()
```



## theme

```python
# gradio/issues/7694/run.py
import gradio as gr


from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
import time


class Seafoam(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.emerald,
        secondary_hue: colors.Color | str = colors.blue,
        neutral_hue: colors.Color | str = colors.blue,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            body_background_fill="repeating-linear-gradient(45deg, *primary_200, *primary_200 10px, *primary_50 10px, *primary_50 20px)",
            body_background_fill_dark="repeating-linear-gradient(45deg, *primary_800, *primary_800 10px, *primary_900 10px, *primary_900 20px)",
            button_primary_background_fill="linear-gradient(90deg, *primary_300, *secondary_400)",
            button_primary_background_fill_hover="linear-gradient(90deg, *primary_200, *secondary_300)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="linear-gradient(90deg, *primary_600, *secondary_800)",
            slider_color="*secondary_300",
            slider_color_dark="*secondary_600",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )


seafoam = Seafoam()


def greet(name):
    return "Hello " + name + "!"

with gr.Blocks(theme=seafoam) as demo:
    textbox = gr.Textbox(label="Name")
    slider = gr.Slider(label="Count", minimum=0, maximum=100, step=1)
    with gr.Row():
        button = gr.Button("Submit", variant="primary")
        clear = gr.Button("Clear")
    output = gr.Textbox(label="Output")

    def repeat(name, count):
        time.sleep(3)
        return name * count

    button.click(repeat, [textbox, slider], output)

if __name__ == "__main__":
    demo.launch()


```





## Accordion

```python
import gradio as gr
with gr.Blocks() as demo:
  with gr.Accordion('Answers:', open=True):
    answerhtml = gr.HTML(value='''<a href='https://hf.co//'>huggingface</a>''', label="Answer HTML")
    answer = gr.Markdown(value='[gradio](https://gradio.app/)', label="Answer Markdown")

  gr.Examples([
        ['[StackOverflow](https://stackoverflow.com/)', '''<a href='https://stackoverflow.com/'>stackoverflow</a>'''],
        ['[google](https://google.com/)', '''<a href='https://google.com/'>google</a>''']
    ], [answer, answerhtml])
demo.launch(share=True)
```



## dataframe

https://github.com/gradio-app/gradio/issues/7601



```python
# https://github.com/gradio-app/gradio/issues/8270
import gradio as gr

with gr.Blocks() as demo:
    gr.DataFrame([["<audio src='/file=cantina.wav' controls></audio>"]], datatype="markdown")
    
demo.launch(allowed_paths=["cantina.wav"])
```





## save data

[save data](https://huggingface.co/spaces/Wauplin/space_to_dataset_saver)



https://huggingface.co/docs/datasets-server/search  它还可以查





## backup db

[running-background-tasks](https://www.gradio.app/guides/running-background-tasks)

```python
TOKEN = os.environ.get('HUB_TOKEN')
repo = huggingface_hub.Repository(
    local_dir="data",
    repo_type="dataset",
    clone_from="<name-of-your-dataset>",
    use_auth_token=TOKEN
)
repo.git_pull()

shutil.copyfile("./data/reviews.db", DB_FILE)


from apscheduler.schedulers.background import BackgroundScheduler

def backup_db():
    shutil.copyfile(DB_FILE, "./data/reviews.db")
    db = sqlite3.connect(DB_FILE)
    reviews = db.execute("SELECT * FROM reviews").fetchall()
    pd.DataFrame(reviews).to_csv("./data/reviews.csv", index=False)
    print("updating db")
    repo.push_to_hub(blocking=False, commit_message=f"Updating data at {datetime.datetime.now()}")


scheduler = BackgroundScheduler()
scheduler.add_job(func=backup_db, trigger="interval", seconds=60)
scheduler.start()

```





## textbox

https://github.com/gradio-app/gradio/issues/7950



## dropdown

```
import gradio as gr

options_1 = ['Paris', 'Berlin' ]
options_2 = {
    'Paris': ['Saint Denis', 'Eiffel Tower', 'Le Louvre'],
    'Berlin': ['Reichstag', 'Alexanderplatz', 'Kreuzberg'],
    }

with gr.Blocks() as demo:
    d1 = gr.Dropdown(choices=options_1, label="City dropdown")
    d2 = gr.Dropdown([])
    
    def update_second(first_val):
        d2 = gr.Dropdown(options_2[first_val])
        return d2 
    
    d1.input(update_second, d1, d2)

    outputs = gr.Textbox()

    def print_results(option_1, option_2):
        return f"You selected '{option_1}' in the first dropdown and '{option_2}' in the second dropdown."
        
    d2.input(print_results, [d1, d2], outputs) 

demo.launch()
```





## warning error

```python
    gr.Info("Starting process")
    if name is None:
        gr.Warning("Name is empty")
    ...
    if success == False:
        raise gr.Error("Process failed")
```





## image

https://github.com/gradio-app/gradio/issues/8711  图片 slider 效果

```python
import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import os
import tempfile

temp = tempfile.gettempdir()

width, height = 200, 200
pics = []

def make_images(num):
    global pics
    font_size = min(width, height) // 2
    for i in range(0, num - 1):
        img = Image.new('RGB', (width, height), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        text = str(i)
        bbox = d.textbbox((0,0), text)
        textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = ((width-textwidth)/2,(height-textheight)/2)
        d.text(position, text, fill=(0,0,0))
        image_path = os.path.join(temp, f'gallerytest_{i:02}.jpg')
        img.save(image_path)
        pics.append(image_path)

make_images(40)

def sel(evt: gr.SelectData):
    index = evt.index
    print(index)
    return index
    
with gr.Blocks() as demo:
    with gr.Row():
        gallery_sel = gr.Textbox(label="Selected Index", interactive=False)
    with gr.Row():
        gallery = gr.Gallery(pics, show_label=False, columns=8, selected_index=0)
        gallery.select(fn=sel, inputs=[], outputs=[gallery_sel], trigger_mode="multiple")

demo.launch()

```



### vite

```
pnpm create vite vite_gradio_imageeditor -- --template svelte


```





### coordinates

[Get Image click coordinates from .select](https://github.com/gradio-app/gradio/pull/3786) 

[ImageEditor](https://github.com/gradio-app/gradio/issues/7502)

[AnnotatedImage](https://github.com/gradio-app/gradio/issues/6992)

[gradio_image_annotator](https://github.com/SkalskiP/gradio_image_annotator) 没什么用



https://github.com/gradio-app/gradio/issues/7502  ImageEditor

https://github.com/gradio-app/gradio/issues/7685  ImageEditor

https://github.com/gradio-app/gradio/issues/6992  opencv + AnnotatedImage



### pixi.js 



```
target.appendChild(app.view as HTMLCanvasElement);
	# 你传一个 div ，它自已有一个 Canvas , 会占满这个 div
```



``` 
phaser 是 pixijs 的封装

用 pixi 的 spine plugin 给 spine 骨骼动画 load 上来，给 spine 的各个皮肤设置 skin name，完事儿…
不过你需要先搞清楚，scenegraph，game update 是怎么回事儿

https://github.com/pixijs/spine
https://github.com/pixijs/animate
	# 可以和 animate cc 配合？

```

```
see gradio/js/imageeditor/shared/utils/pixi.ts
imageeditor 用到 pixi.ts 来实现绘画效果

huggingface/gradio/js/imageeditor/shared/tools/brush.ts
function drawCircle(
	graphics: Graphics,
	# 画一个圆
	# 实际干活是在这里
	
gradio/js/imageeditor/shared/tools/Tools.svelte
	# 画刷工具的定义应该在这里

gradio/js/imageeditor/shared/InteractiveImageEditor.svelte
	import { Tools, Crop, Brush, Sources } from "./tools";
	<ImageEditor ... >
		<Tools {i18n}>
		# 工具是这样引入的

gradio/js/imageeditor/shared/tools/Tools.svelte
	line 140
	on:click={() => tool_context.activate_subtool(meta.id, meta.cb)}
	line 157
	on:click={() => ($active_tool = tool)}
	# 点画刷工具，画布上的提示文字就会消失，可以是这里作用

gradio/js/imageeditor/shared/InteractiveImageEditor.svelte
	line 168
	{#if !bg && !history}
		<div class="empty wrap">
			{#if brush}
				<div>select the draw tool to start</div>
	# 文字在这


gradio/js/imageeditor/shared/tools/Brush.svelte
	# 实际绘画是在这里的
	function pointer_down_handler(event: FederatedPointerEvent): void {
		draw = draw_path(
			$pixi.renderer!,  // 画布在这，存全局变量里
			$pixi.layer_container,
			$current_layer,
			mode
		);

		draw.start({
			x: event.screen.x,
			y: event.screen.y,
			color: selected_color || undefined,
			size: selected_size,
			opacity: 1
		});


gradio/js/imageeditor/shared/tools/Brush.svelte
	line 193
		$pixi?.layer_container[on_off](
			"pointerenter",
			(event: FederatedPointerEvent) => {
				if ($active_tool === mode) {
					brush_cursor = true;
					document.body.style.cursor = "none";
				}
			}
		);
		$pixi?.layer_container[on_off](
			"pointerleave",
			() => ((brush_cursor = false), (document.body.style.cursor = "auto"))
		);
		# 鼠标进入或刚离开的时侯
		
	line 151 
	function pointer_move_handler(event: FederatedPointerEvent): void {
		brush_cursor = true;
		document.body.style.cursor = "none";
		# 鼠标移动的时侯
	# 点画刷工具，鼠标移动到画布，就会显示一个圆。应该是这里
	
<span
	style:transform="translate({pos.x}px, {pos.y}px)"
	style:top="{$editor_box.child_top -
		$editor_box.parent_top -
		brush_size / 2}px"
	style:left="{$editor_box.child_left -
		$editor_box.parent_left -
		brush_size / 2}px"
	style:width="{brush_size}px"
	style:height="{brush_size}px"
	style:opacity={brush_cursor ? 1 : 0}
/>
	# 小圆点的本体应该是这里
	# border-radius: 50%; 边框圆角半径为50%，这将使正方形看起来像一个圆。

<style>
	span {
		display: none;
	# css 隐藏它，小圆点确实不见了


import {
	Application,
	Container,
	Graphics,
	Sprite,
	Rectangle,
	RenderTexture,
	type IRenderer,
	type DisplayObject,
	type ICanvas
} from "pixi.js";

const background_container = new Container() as Container & DisplayObject;

在Pixi.js中，Container和DisplayObject是两个重要的类。 

"Container"是Pixi.js中的一个基本构造块，可以被视为包含其他对象（如另一个容器或精灵）的一个框架或者组。你可以把它想象为一个可以容纳其他JavaScript对象的框。

"DisplayObject"是Pixi.js场景中所有可见对象的基类，包括像Sprite, Graphics以及Container等。所有DisplayObject都可以通过设定x,y,rotation等属性来改变其在容器中的位置或转向。所有的显示对象都可以添加到Pixi.js的舞台上。

当你看到 “Container & DisplayObject”，这意味着创建的`background_container`对象同时具有Container和DisplayObject的所有属性和方法。这种技术被称为“交叉类型”（Intersection Type），用于将多个类型合并为一个类型，因此，新对象将具有所需的所有功能。

在这个代码中，background_container被赋予了Container和DisplayObject的类型，这表示它可以在Container中容纳其他元素，并且作为一个DisplayObject，同时可以被置于stage上，拥有在舞台上显示和移动的能力。

请注意，有些功能由于同时是Container和DisplayObject会有冲突，但是TypeScript会处理这种情况，使用类型断言(as)来解决这个问题。

```



#### gradio_4290

```python
# gradio_4290/js/imageeditor/shared/ImageEditor.svelte
	line 223
	$: if (crop_constraint && bg && !history) {
		//set_crop();
		# 这样就不会把刚上传的图片自动切成小图了
	}
	
	# gradio_4290/js/imageeditor/shared/tools/Crop.svelte
	line 70
	c = crop_canvas($pixi!.renderer, $pixi!.mask_container, crop, 0.2);
	c.start(...$dimensions, current_crop, false);
		# 实际执行 crop 的代码在这里 
		
	# js/imageeditor/shared/InteractiveImageEditor.svelte
	line 225
    <Sources
    	# 上传图片按钮在这
	

	# gradio_4290/demo/image_editor/run.py
		#Union[np.ndarray, PIL.Image.Image, str]
		#value: EditorValue
        im = gr.ImageEditor(
            value=imgData,
            type="numpy",
            crop_size=None, # 重点：1:1 拖出来只能是方形
            # crop_size="1:1", 
        )
			# python 可以在这里直接传背景图


# gradio_4290/demo/image_editor/run.py
	# see Python 3 summay.md -> OpenCV -> PIL、cv2、bytes 图片格式互转换
import numpy as np
from pathlib import Path
import cv2
from PIL import Image
base_root = Path(__file__).parent.resolve()
imgPath = str(base_root / 'cheetah.jpg')
# imgData = np.fromfile(imgPath, dtype=np.uint8)
# img = cv2.imdecode(imgData, -1)
imgData = Image.open(imgPath)
#img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
	# 加代码，图片读取
		
# gradio_4290/gradio/processing_utils.py        
	line 215
    bytes_data = encode_pil_to_bytes(img, format)
    temp_dir = Path(cache_dir) / hash_bytes(bytes_data)
    temp_dir.mkdir(exist_ok=True, parents=True)
    filename = str((temp_dir / f"{name}.{format}").resolve())
    (temp_dir / f"{name}.{format}").resolve().write_bytes(bytes_data)
    	# 转成 webp ，存临时文件
   

# gradio_4290/js/imageeditor/shared/tools/Crop.svelte
	line 176
    {#if $active_tool === "crop" && measured}
	<Cropper
		crop_constraint={_crop_constraint}
    # crop 工具激活的时侯，显示拖拽框


# gradio_4290/js/imageeditor/shared/tools/Cropper.svelte        
  line 277
  <div class="wrap">
	<div
		class="box"
		style:width="{_width}px"
		style:height="{_height}px"
		style:top="{_top}px"
		style:left="{_left}px"
	>
    # 工具激活时拖拽框的位置和大小是由这几个参数控制的
    

# gradio_4290/js/imageeditor/shared/tools/Crop.svelte
	$: {
		//if (!manually_cropped && _crop_constraint && $pixi && $active_tool) {
		if (!manually_cropped && $pixi && $active_tool) {
			requestAnimationFrame(() => {
				initial_crop();
			});
		}
	}
	async function initial_crop(): Promise<void> {
		if (c || $current_history.previous) return;
		const { new_height, new_width, x_offset, y_offset } = resize_and_reposition(
			$editor_box.child_width,
			$editor_box.child_height,
			"c",
			1,//_crop_constraint!,

			$editor_box.child_width,
			$editor_box.child_height
		);
    
    export function resize_and_reposition(
	if (anchor.includes("t") || anchor.includes("b") || anchor == "c") {
		// new_width = original_height * aspect_ratio;
	}
	if (anchor.includes("l") || anchor.includes("r") || anchor == "c") {
		// new_height = original_width / aspect_ratio;
	}
	// new_height = new_height || new_width / aspect_ratio;
	// new_width = new_width || new_height * aspect_ratio;

	if (new_width > max_width) {
		new_width = max_width;
		// new_height = new_width / aspect_ratio;
	}
	if (new_height > max_height) {
		new_height = max_height;
		// new_width = new_height * aspect_ratio;
	}
        # 让它有初始 crop, 但是又不限制宽高比
        
# gradio_4290/js/imageeditor/shared/ImageEditor.svelte
    line 265
	$: $position_spring && get_dimensions(canvas_wrap, pixi_target);
        canvas_wrap.getBoundingClientRect();
		editor_box.set({       
    # 设置 parent, child 的大小，重要！！
            

# gradio_4290/js/imageeditor/shared/tools/Crop.svelte            
	async function initial_crop(): Promise<void> {            
    	w_p = 0.5 // new_width / $editor_box.child_width;
		h_p = 0.5 // new_height / $editor_box.child_height;
		l_p = x_offset / $editor_box.child_width;
		t_p = y_offset / $editor_box.child_height;        
        	# 破案了！这四个值决定了初始 corp 的宽高和位置
        	# w_p 宽度是原来的 1/2, 高度是原来的 1/2, 位置是 (0,0)
        	# 初次 F5 或刷新能看到效果
        	# 然后激活 corp 工具 它也是框住这个小框，完美
        		# 其实还是不太行，看看上传图片按钮，它能记得住上一次 corp 的位置，符合需求了
        	
# gradio_4290/demo/image_editor/run.py  
    button_change_bg = gr.Button("Change bg", variant="primary")
    button_change_bg.click(lambda _: gr.update(value=imgData), None, im)
        # 动态更新背景图是可以的，先前 corp 位置正常保留
        
        
# gradio_4290/js/imageeditor/shared/tools/Handle.svelte                
	# 拖拽过程中的实时动态效果                

                
const img = await createImageBitmap(background);
	# 从 File 类型创建图片
    # imageeditor/shared/tools/sources.ts
 
# gradio_4290/js/imageeditor/shared/tools/Crop.svelte
    # line 112
 	cropper = crop_canvas(
    	# 这里下断好调试

# run.py        
def predict(im):
    return im["composite"]        
im.change(predict, outputs=im_preview, inputs=im, show_progress="hidden")
	# 它是把实时合成好的图放右边输出预览
        
# gradio_4290/js/imageeditor/Index.svelte
  line 105
  gradio.dispatch("change");
  	# 触发 change 事件在这      
     
        
# gradio_4290/js/imageeditor/shared/tools/Cropper.svelte
  line 69
  dispatch("crop_end", {
  	x: l_p,
	y: t_p,
	width: w_p,
	height: h_p
  });
  # 结束 crop ，得到最终 选框 的位置
  # 务必在这里下断点好调试
  
# gradio_4290/js/imageeditor/shared/tools/crop.ts
  line 121	
  execute() {
    crop.set([
		final_crop[0] / width,
		final_crop[1] / height,
		final_crop[2] / width,
		final_crop[3] / height
	]);
    # 关键，这里也下断点
    
      
# gradio_4290/js/imageeditor/shared/InteractiveImageEditor.svelte
	line 38
    export let value: EditorData | null = {
		background: null,
		layers: [],
		composite: null
	};
    # python 监听 change 事件，取出 im["composite"] 既合成图，赋值给 output
        # 合成方法可以是先往 composite 绘制背景图，再绘制 layer1, ... 
    
# gradio_4290/js/imageeditor/shared/utils/pixi.ts
	line 295
    export interface ImageBlobs {
		background: Blob | null;
		layers: (Blob | null)[];
		composite: Blob | null;
	}
    # composite 的定义
	
    
    line 224
    function get_canvas_blob(   
    ): Promise<Blob | null> {
		return new Promise((resolve) => {   
        	let dest_canvas = document.createElement("canvas");
            dest_canvas.toBlob?.((blob) => {
				if (!blob) {
					resolve(null);
				}
				resolve(blob);
			});
    	# 如何从 canvas 里面取出 raw 数据
        
            
# gradio_4290/js/imageeditor/shared/utils/pixi.ts
    line 76
	export function create_pixi_app({        
    	# 仔细看这个函数，很多秘密都藏在这里 
        
            
imageeditor/shared/tools/Sources.svelte
	# 图片工具在这

	async function set_background(): Promise<void> {
		if (!$pixi) return;
		if (background) {
			const add_image = add_bg_image(
				$pixi.background_container,
				$pixi.renderer,
				background,
				$pixi.resize
			);
		# 设置背景图

```





#### 颜色

```python
import type { HslaColor, HslColor, HsvaColor, HsvColor, RgbaColor, RgbColor } from '@pixi/colord';
/**
 * Value types for the constructor of {@link PIXI.Color}.
 * These types are extended from [colord](https://www.npmjs.com/package/colord) with some PixiJS-specific extensions.
 *
 * Possible value types are:
 * - [Color names](https://www.w3.org/TR/css-color-4/#named-colors):
 *   `'red'`, `'green'`, `'blue'`, `'white'`, etc.
 * - RGB hex integers (`0xRRGGBB`):
 *   `0xff0000`, `0x00ff00`, `0x0000ff`, etc.
 * - [RGB(A) hex strings](https://www.w3.org/TR/css-color-4/#hex-notation):
 *   - 6 digits (`RRGGBB`): `'ff0000'`, `'#00ff00'`, `'0x0000ff'`, etc.
 *   - 3 digits (`RGB`): `'f00'`, `'#0f0'`, `'0x00f'`, etc.
 *   - 8 digits (`RRGGBBAA`): `'ff000080'`, `'#00ff0080'`, `'0x0000ff80'`, etc.
 *   - 4 digits (`RGBA`): `'f008'`, `'#0f08'`, `'0x00f8'`, etc.
 * - RGB(A) objects:
 *   `{ r: 255, g: 0, b: 0 }`, `{ r: 255, g: 0, b: 0, a: 0.5 }`, etc.
 * - [RGB(A) strings](https://www.w3.org/TR/css-color-4/#rgb-functions):
 *   `'rgb(255, 0, 0)'`, `'rgb(100% 0% 0%)'`, `'rgba(255, 0, 0, 0.5)'`, `'rgba(100% 0% 0% / 50%)'`, etc.
 * - RGB(A) arrays:
 *   `[1, 0, 0]`, `[1, 0, 0, 0.5]`, etc.
 * - RGB(A) Float32Array:
 *   `new Float32Array([1, 0, 0])`, `new Float32Array([1, 0, 0, 0.5])`, etc.
 * - RGB(A) Uint8Array:
 *   `new Uint8Array([255, 0, 0])`, `new Uint8Array([255, 0, 0, 128])`, etc.
 * - RGB(A) Uint8ClampedArray:
 *   `new Uint8ClampedArray([255, 0, 0])`, `new Uint8ClampedArray([255, 0, 0, 128])`, etc.
 * - HSL(A) objects:
 *   `{ h: 0, s: 100, l: 50 }`, `{ h: 0, s: 100, l: 50, a: 0.5 }`, etc.
 * - [HSL(A) strings](https://www.w3.org/TR/css-color-4/#the-hsl-notation):
 *   `'hsl(0, 100%, 50%)'`, `'hsl(0deg 100% 50%)'`, `'hsla(0, 100%, 50%, 0.5)'`, `'hsla(0deg 100% 50% / 50%)'`, etc.
 * - HSV(A) objects:
 *   `{ h: 0, s: 100, v: 100 }`, `{ h: 0, s: 100, v: 100, a: 0.5 }`, etc.
 * - {@link PIXI.Color} objects.
 * @memberof PIXI
 * @since 7.2.0
 */
export type ColorSource = string | number | number[] | Float32Array | Uint8Array | Uint8ClampedArray | HslColor | HslaColor | HsvColor | HsvaColor | RgbColor | RgbaColor | Color | Number;
```



#### 画好的图转base64

```python
const app = new PIXI.Application(config);
const stage = app.stage;
const renderer = app.renderer;
return renderer.plugins.extract.canvas(stage).toDataURL();

```



```
const img = renderer.plugins.extract.image(target);
	# 从画布取图

```



```

# gradio_4290/js/imageeditor/shared/utils/pixi.ts
	line 244
function get_canvas_blob(
	renderer: IRenderer,
	obj: DisplayObject,
	bounds: Rectangle,
	width: number,
	height: number
): Promise<Blob | null> {
	return new Promise((resolve) => {
		// for some reason pixi won't extract a cropped canvas without distorting it
		// so we have to extract the whole canvas and crop it manually
		const src_canvas = renderer.extract.canvas(
			obj,
			new Rectangle(0, 0, width, height)
		);

		// Create a new canvas for the cropped area with the appropriate size
		let dest_canvas = document.createElement("canvas");
		dest_canvas.width = bounds.width;
		dest_canvas.height = bounds.height;
		let dest_ctx = dest_canvas.getContext("2d");

		if (!dest_ctx) {
			resolve(null);
			throw new Error("Could not create canvas context");
		}

		// Draw the cropped area onto the destination canvas
		dest_ctx.drawImage(
			src_canvas as HTMLCanvasElement,
			// this is the area of the source that we want to copy (the crop box)
			bounds.x,
			bounds.y,
			bounds.width,
			bounds.height,
			// this is where we want to draw the crop box on the destination canvas
			0,
			0,
			bounds.width,
			bounds.height
		);

		// we grab a blob here so we can upload it
		dest_canvas.toBlob?.((blob) => {
			if (!blob) {
				resolve(null);
			}
			resolve(blob);
		});
	});
}
```



```
	async function get_blobs(
		_layers: LayerScene[],
		bounds: Rectangle,
		[w, h]: [number, number]
	): Promise<ImageBlobs> {
		const background = await get_canvas_blob(
			app.renderer,
			background_container,
			bounds,
			w,
			h
		);

		const layers = await Promise.all(
			_layers.map((layer) =>
				get_canvas_blob(
					app.renderer,
					layer.composite as DisplayObject,
					bounds,
					w,
					h
				)
			)
		);

		const composite = await get_canvas_blob(
			app.renderer,
			mask_container,
			bounds,
			w,
			h
		);

		return {
			background,
			layers,
			composite
		};
	}
```



#### blob base64 互转

```
const base64Data = "aGV5IHRoZXJl";
const base64 = await fetch(base64Data);

const base64Response = await fetch(`data:image/jpeg;base64,${base64Data}`);
	# 图片的 base64 的转换比较特殊

const blob = await base64Response.blob();


convertBlobToBase64 = (blob) => new Promise((resolve, reject) => {
    const reader = new FileReader;
    reader.onerror = reject;
    reader.onload = () => {
        resolve(reader.result);
    };
    reader.readAsDataURL(blob);
});

const base64String = await convertBlobToBase64(blob);

```





### getContext

```python

gradio/js/imageeditor/shared/tools/Brush.svelte
export const EDITOR_KEY = Symbol("editor");
import { getContext, onMount, tick } from "svelte";

	const {
		pixi,
		dimensions,
		current_layer,
		command_manager,
		register_context,
		editor_box,
		crop
	} = getContext<EditorContext>(EDITOR_KEY);

	const { active_tool, register_tool, current_color } =
		getContext<ToolContext>(TOOL_KEY);
	# 这里应该是子组件 EditorContext 是指定了返回值的类型 T 


gradio/js/imageeditor/shared/ImageEditor.svelte
export interface EditorContext {
		pixi: Writable<PixiApp | null>;
const editor_context = setContext<EditorContext>(EDITOR_KEY, {
		pixi,
		current_layer: writable(null),
	# 这里应该是父组件　


`getContext` 在 Svelte 中是一个函数，用来获取由上层组件通过 `setContext` 设置的上下文值。这种机制允许你在组件树中共享数据，而不必将属性一级一级地传递下去。

通常，`getContext` 会与 `setContext` 一起使用。先由某个祖先组件调用 `setContext` 方法来设置一个值，之后在组件树中的任何子孙组件里都可以通过调用 `getContext` 来检索这个值。

这里有一个简单的示例，展示了如何使用 `getContext` 和 `setContext`：

​```svelte
<!-- Parent.svelte -->
<script>
  import { setContext } from 'svelte';
  import Child from './Child.svelte';

  // 创建一个唯一的键，以避免上下文名称冲突
  const key = Symbol();

  // 你想要共享的数据
  const sharedValue = 'Hello from parent!';

  // 设置上下文
  setContext(key, sharedValue);
</script>

<Child />

<!-- Child.svelte -->
<script>
  import { getContext } from 'svelte';

  // 使用与父组件相同的key来获取值
  const key = Symbol();
  const sharedValue = getContext(key);
</script>

<p>{sharedValue}</p>
​```

在此示例中，`Parent.svelte` 组件设置了一个上下文值，然后在 `Child.svelte` 组件中我们可以通过 `getContext` 获取到这个值并显示它。注意这里 `key` 必须是匹配的，通常是在父组件和子组件间共享（往往导出为公共模块）。

上下文非常适合于像主题配置、国际化信息、用户权限等全局性或需跨多层组件传递的数据。


```



### 复杂的函数声明

```python
gradio/js/imageeditor/shared/ImageEditor.svelte
export type context_type = "bg" | "layers" | "crop" | "draw" | "erase";
		register_context: (
			type: context_type,
			{
				reset_fn,
				init_fn
			}: {
				reset_fn?: () => void;
				init_fn?: (dimensions?: [number, number]) => void;
			}
		) => void;
```



### 画布

```
gradio/js/imageeditor/shared/ImageEditor.svelte
	let pixi_target: HTMLDivElement;
	let canvas_wrap: HTMLDivElement;
	
	
```



### 粘贴图片

https://github.com/gradio-app/gradio/issues/735

```python


import pyclip
import numpy as np
import cv2

def rgb_to_bgr(image):
    """gradio is turning cv2's BGR colorspace into RGB, so
    I need to convert it again"""
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


def get_image(gallery):
    print("Getting image from clipboard")
    try:
        # load from clipboard
        pasted = pyclip.paste()
        decoded = cv2.imdecode(np.frombuffer(pasted, np.uint8), flags=1)
        decoded = rgb_to_bgr(decoded)

        if decoded is None:
            print("Image from clipboard was Nonetype")
            return gallery

        if gallery is None:
            return [decoded]

        if isinstance(gallery, list):
            out = []
            for im in gallery:
                out.append(
                        rgb_to_bgr(
                            cv2.imread(
                                im["name"],
                                flags=1)
                            )
                        )
            out += [decoded]

            print("Loaded image from clipboard.")
            return out

        else:
            print(f'gallery is not list or None but {type(gallery)}')
            return None

    except Exception as err:
        print(f"Error: {err}")
        return None

```



#### 可以上传图片的Textbox 

```python

# https://github.com/gradio-app/gradio/issues/7768

import gradio as gr

def dummy(mm):
  text = mm['text']
  img = mm['files'][0]['path']
  return text, img

with gr.Blocks(theme=gr.themes.Default()) as demo:
  gr.HTML('<h1><center>Multimodal Textbox</center></h1>')
  mm_input = gr.MultimodalTextbox(interactive=True, file_types=["image"], placeholder="Enter message or upload file...", show_label=False)
  with gr.Row():
    ta = gr.TextArea(label='Multimodal text')
    img = gr.Image()
  mm_input.submit(dummy, mm_input, [ta, img])

demo.launch(debug=False)
```





## audio

```python
import gradio as gr
from gtts import gTTS
from io import BytesIO
import base64


def text_to_speech(text):
    tts = gTTS(text)
    tts.save('hello_world.mp3')

    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    audio = base64.b64encode(audio_bytes.read()).decode("utf-8")
    audio_player = f'<audio src="data:audio/mpeg;base64,{audio}" controls autoplay></audio>'

    return audio_player


with gr.Blocks() as demo:
    html = gr.HTML()
    # html.visible = False

    text = gr.Text()
    btn = gr.Button("OK")
    btn.click(text_to_speech, inputs=[text], outputs=[html])

demo.launch()
```



### stream



```python
import gradio as gr
import numpy as np
import wave

def response():
    def streaming():
        f = wave.open("sound.wav", 'rb')
        buffer = f.readframes(f.getnframes())
        data = np.frombuffer(buffer, dtype=f'int{f.getsampwidth()*8}')
        chunks = []
        for idx in range(0,data.shape[0],20000):
            chunks.append( data[idx:idx+20000] )
        return chunks
    chunks = streaming()
    for i, chunk in enumerate(chunks):
        if i == 0:
            assert chunk.shape[-1] > 5000
        # print("stream chunk:",i, chunk.shape)

        wav = chunk.astype(np.float)
        wav_norm = wav * float(32767 / max(0.01, np.max(np.abs(wav))))
        wav_norm = wav_norm.astype(np.int16)
        yield (44000, wav_norm)

with gr.Blocks() as demo:
    audio_out = gr.Audio(autoplay=True,
                         show_download_button=False,
                         show_share_button=False,
                         editable=False,
                         interactive=False,
                         streaming=True,
                         label="Stream audio out")
    button = gr.Button("Test streaming audio out")
    button.click(response, [], audio_out) \

demo.launch(share=True)
```





## video

https://github.com/HumanSignal/label-studio  音视频图片标注

- https://github.com/opendatalab/labelU  各种工具很丰富

- ```
  # see huggingface/rwkv5-jp-explain-docker/app.py -> OcrVideo
  # see nodejs summary.md -> vscode + gradio
  ```

- https://blog.csdn.net/sinat_39620217/article/details/129304751

- ```
  conda create --name label-studio && 
  conda activate label-studio && 
  conda install psycopg2 && 
  pip install label-studio
  	# 实测正常运行
  	
  pm2 --name label_studio_8080 start "/root/miniforge3/envs/label-studio/bin/python /root/miniforge3/envs/label-studio/bin/label-studio"
  	
  http://xxx.77:8080/projects/
  	# 它只支持 http
  	
  
  pip install label-studio && 
  label-studio
  
  docker pull heartexlabs/label-studio:latest
  docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
  ```

https://github.com/anucvml/vidat  视频标注

https://github.com/open-mmlab/playground/blob/main/README_zh-CN.md#-mmocr-sam 组合工具箱

https://github.com/gaomingqi/Track-Anything  对象追踪

```python
gradio cc create ivideo --template Video
	# 成功自定义组件
```



```python
import gradio as gr
import cv2
import numpy as np

# 读取视频并将其转为字节流
cap = cv2.VideoCapture('my_video.mp4')
success, image = cap.read()
if not success:
    print("无法读取视频文件！")
    exit()
ret, frame = cv2.imencode('.jpg', image)
bytestr = frame.tobytes()

# 创建视频组件，并将其显示在浏览器中
video = gr.inputs.Video(content_type='mp4', label="My Video", source="webcam")
iface = gr.Interface(fn=lambda video: None, inputs=video)
iface.launch()

# 在10秒后更新视频组件
import time
time.sleep(10)
success, image = cap.read()
if success:
    # 将新图像转换为字节流
    ret, frame = cv2.imencode('.jpg', image)
    bytestr = frame.tobytes()
    # 更新视频组件
    iface.inputs[0].update(value=bytestr)
```



```python
# https://github.com/gradio-app/gradio/issues/1637
# 实时视频处理

import gradio as gr
import cv2

def process_video(input_video):
    cap = cv2.VideoCapture(input_video)

    output_path = "output.mp4"

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    iterating, frame = cap.read()
    while iterating:

        # flip frame vertically
        frame = cv2.flip(frame, 0)
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        video.write(frame)
        yield display_frame, None

        iterating, frame = cap.read()

    video.release()
    yield display_frame, output_path

with gr.Blocks() as demo:
    with gr.Row():
        input_video = gr.Video(label="input")
        processed_frames = gr.Image(label="last frame")
        output_video = gr.Video(label="output")

    with gr.Row():
        examples = gr.Examples(["parrot.mp4"], inputs=input_video)
        process_video_btn = gr.Button("process video")

    process_video_btn.click(process_video, input_video, [processed_frames, output_video])

demo.queue()
demo.launch()
```



```python
# 提取关键帧
# see huggingface gradio/issues/1637/run.py
# opencv-python
# https://juejin.cn/post/7201506099342082105 必看
# https://forums.developer.nvidia.com/t/python-what-is-the-four-characters-fourcc-code-for-mp4-encoding-on-tx2/57701
import gradio as gr
import cv2, subprocess, math

def process_video(input_video):
    cap = cv2.VideoCapture(input_video)

    output_path = "/root/gradio/issues/1637/output.mp4"
    
    cmd = f"ffprobe -i {input_video} -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1"
    out_bytes = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    total_time = float( out_bytes.decode('utf-8').strip() )
    
    cmd2 = f"ffprobe -i {input_video} -loglevel error -print_format csv -select_streams v:0 -show_entries frame=pict_type"
    out_bytes = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT)
    frame_info = out_bytes.decode('utf-8').strip().split('\n')
    
    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    total_frame2 = math.floor(total_time * fps)
    
    assert total_frame == total_frame2

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    """
    获取当前帧
    视频的首帧索引通常是0，所以最后一帧的索引会是总帧数减1
    ffprobe -i parrot.mp4 -v  quiet -select_streams v -show_entries frame=pkt_pts_time,pict_type
    得到的输出前后2个pkt_pts_time的差值即关键帧的间隔时间(单位为秒)，不过需要注意pict_type=I时，才表示是关键帧，类型还有P（前向预测帧）和B（双向预测帧）
    
    
    ffprobe -i parrot.mp4 -loglevel error -print_format csv -select_streams v:0 -show_entries frame=pict_type
        # 只显示帧类型
    
    ffprobe -loglevel error -print_format csv -select_streams v:0  -show_frames parrot.mp4
    frame,video,0,1,5940,0.066000,5940,0.066000,5940,0.066000,3000,0.033333,48,4020,854,480,yuv420p,1280:1281,I,0,0,0,0,0,unknown,unknown,unknown,unknown,left
    frame,video,0,0,8940,0.099333,8940,0.099333,8940,0.099333,3000,0.033333,4845,180,854,480,yuv420p,1280:1281,B,2,0,0,0,0,unknown,unknown,unknown,unknown,left
    frame,video,0,0,11940,0.132667,11940,0.132667,11940,0.132667,3000,0.033333,5037,215,854,480,yuv420p,1280:1281,B,3,0,0,0,0,unknown,unknown,unknown,unknown,left
    frame,video,0,0,14940,0.166000,14940,0.166000,14940,0.166000,3000,0.033333,4097,742,854,480,yuv420p,1280:1281,P,1,0,0,0,0,unknown,unknown,unknown,unknown,left
    frame,video,0,0,17940,0.199333,17940,0.199333,17940,0.199333,3000,0.033333,6413,270,854,480,yuv420p,1280:1281,B,5,0,0,0,0,unknown,unknown,unknown,unknown,left
    frame,video,0,0,20940,0.232667,20940,0.232667,20940,0.232667,3000,0.033333,5258,1143,854,480,yuv420p,1280:1281,P,4,0,0,0,0,unknown,unknown,unknown,unknown,left
       # https://juejin.cn/post/7201506099342082105

    从左到右依次为
frame 代表一个frame
media_type 媒体类型 video audio
stream_index stream 索引
key_frame 是否为关键帧
pkt_pts 展示时间戳，按time_base计算，time_base为时间基，代表1s有多少份，这里是90000
pkt_pts_time 展示时间戳，按秒为单位
pkt_dts  编码时间戳，按time_base计算
pkt_dts_time 编码时间戳，按秒为单位
best_effort_timestamp
best_effort_timestamp_time
pkt_duration  packet持续时长，按time_base计算
pkt_duration_time  packet持续时长，，按秒为单位
pkt_pos  packet文件位置
pkt_size  packet大小
width 帧的宽
height 帧的高
pix_fmt 图片的像素格式
sample_aspect_ratio  像素的宽高比例
pict_type 帧的类型 I/B/P
coded_picture_number 压缩的帧序号
display_picture_number 展示图片的序号
interlaced_frame 图像的扫描方式：隔行 逐行   


用中文解释命令：ffprobe -i parrot.mp4 -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1

这是一个使用ffprobe的命令，主要用来检查multimedia streams（例如视频、音频等）的关键信息。其中各部分的中文解释如下：

- `ffprobe`: FFmpeg项目的一部分，一个专门用于检查multimedia流的工具。

- `-i parrot.mp4`: `-i`是指定输入文件的参数，这里指定的输入文件是"parrot.mp4"。

- `-v error`： `-v`用于设置ffprobe的日志等级，这里设定只输出错误信息。

- `-show_entries format=duration`: `show_entries`指定了需要输出的信息，这里要求输出文件的时间长度。

- `-of default=noprint_wrappers=1:nokey=1`: `-of`指的是输出格式的参数，`default=noprint_wrappers=1:nokey=1`的设定是为了让输出信息更加简洁，不会显示每条信息的=key的标签，只输出对应的值。

总的来说，这个命令是用ffprobe去检测"parrot.mp4"这个文件，并只输出视频的长度（duration）信息。
 
 
 out_file = tempfile.NamedTemporaryFile(suffix="out.mp4", delete=False)
subprocess.run(f"ffmpeg -y -loglevel quiet -stats -i {output_fname} -c:v libx264 {out_file.name}".split())
return out_file.name
 
    """
    curr_frame1 = cap.get(cv2.CAP_PROP_POS_FRAMES)

    # 设置从第10帧开始读取
    # cap.set(cv2.CAP_PROP_POS_FRAMES, 10)

    # curr_frame2 = cap.get(cv2.CAP_PROP_POS_FRAMES)

    curr_idx = 0
    iterating, frame = cap.read()
    while iterating:

        # flip frame vertically
        frame = cv2.flip(frame, 0)
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        video.write(frame)
        
        iterating, frame = cap.read()
        
        info = frame_info[curr_idx]
        curr_idx += 1
        if "I" in info: # 关键帧
            yield display_frame, None
        
    cap.release()
    cv2.destroyAllWindows()
    video.release()
    yield display_frame, output_path

with gr.Blocks() as demo:
    with gr.Row():
        input_video = gr.Video(label="input")
        processed_frames = gr.Image(label="last frame")
        output_video = gr.Video(label="output")

    with gr.Row():
        examples = gr.Examples(["/root/gradio/issues/1637/parrot.mp4"], inputs=input_video)
        process_video_btn = gr.Button("process video")

    process_video_btn.click(process_video, input_video, [processed_frames, output_video])

demo.queue()
demo.launch(debug=True, show_api=False, server_name="0.0.0.0", server_port=6006, inbrowser=True)
```



```bash
# ffmpeg 从mp4 的第10帧开始提取 30 帧图片
# https://juejin.cn/post/7201506099342082105 必看

​```bash
ffmpeg -i input.mp4 -vf "select=eq(n\,10)+eq(n\,11)+eq(n\,12)+eq(n\,13)+eq(n\,14)+eq(n\,15)+eq(n\,16)+eq(n\,17)+eq(n\,18)+eq(n\,19)+eq(n\,20)+eq(n\,21)+eq(n\,22)+eq(n\,23)+eq(n\,24)+eq(n\,25)+eq(n\,26)+eq(n\,27)+eq(n\,28)+eq(n\,29)+eq(n\,30)+eq(n\,31)+eq(n\,32)+eq(n\,33)+eq(n\,34)+eq(n\,35)+eq(n\,36)+eq(n\,37)+eq(n\,38)+eq(n\,39)" -vsync 0 output_%02d.png
​```

这将提取第10帧到39帧的图片（总共30帧），生成的图片文件将以output_01.png，output_02.png等格式命名。

注意：ffmpeg的帧索引是从0开始的，所以第10帧实际上是索引为9的帧。上述命令已考虑到这一点。

在这里，`-vf "select=..."`是一个过滤器，它告诉ffmpeg只选择特定的帧。`-vsync 0`告诉ffmpeg在输出时不进行视频同步，这样就可以只输出我们选择的帧了。

`%02d`在`output_%02d.png`中是用于生成文件名的格式化字符，它表示数字将被格式化为至少2位的十进制数，不足的部分会在前面补0。

```





```javascript
<iframe width="560" height="315" src="https://www.youtube.com/embed/IVJkOHTBPn0?si=bs-sBv43X-RVA8ly" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```



### HTMLVideoElement

[requestVideoFrameCallback](https://juejin.cn/post/7125059238195363871)

[Play Videos in Html Canvas and Add Custom Controls](https://hrishikeshpathak.com/blog/play-video-html-canvas-custom-controls/)

[Canvas不会在视频上重叠](https://www.volcengine.com/theme/8321091-R-7-1)



```
<!-- svelte-ignore a11y-media-has-caption -->
	# 去除警告
	videoElement.textTracks
		# 动态加 caption
```





```
// Convert Frame to Image
Object.defineProperty(HTMLVideoElement.prototype, 'convertFrameToImage', {
    value: function convertFrameToImage() {
        // Create the Image.
        let image = new Image();

        // Create a Canvas to draw the chosen frame.
        let canvas= document.createElement('canvas'),
            canvasContext = metadata.getContext('2d');

        // Draw the frame.
        canvasContext.drawImage(this, 0, 0, this.offset.height, this.offset.width);

        // Modify the Source of the Image to the Canvas's Data URL.
        image.src = canvas.toDataURL();

        // Return the Image.
        return image
    }
})
```



```

// Using setTimeout for this is a bad idea and should use requestAnimationFrame instead.

var canvas, context, video, xStart, yStart, xEnd, yEnd;

canvas = document.getElementById("canvas");
context = canvas.getContext("2d");
canvas.addEventListener("mousedown", mouseDown);
canvas.addEventListener("mouseup", mouseUp);

function mouseDown(e) {
    if (video) {
        video.pause();
        video = null;
        context.clearRect(0, 0, canvas.width, canvas.height);
    }
    xStart = e.offsetX;
    yStart = e.offsetY;
}

function mouseUp(e) {
    xEnd = e.offsetX;
    yEnd = e.offsetY;
    if (xStart != xEnd && yStart != yEnd) {
        video = document.createElement("video");
        video.src = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4";
        video.addEventListener('loadeddata', function() {
            console.log("loadeddata");
            video.play();
            setTimeout(videoLoop, 1000 / 30);
        });
    }
}

function videoLoop() {
    if (video && !video.paused && !video.ended) {
        context.drawImage(video, xStart, yStart, xEnd - xStart, yEnd - yStart);
        setTimeout(videoLoop, 1000 / 30);
    }
}
```



```
// pixi draw to canvas
let offScreenCanvasA = document.createElement("canvas");
let offScreenCanvasB = document.createElement("canvas");
let onScreenCanvas = document.createElement("canvas");
let width = 400;
let height = 300;


offScreenCanvasA.width = width;
offScreenCanvasB.width = width;
onScreenCanvas.width = width;

offScreenCanvasA.height = height;
offScreenCanvasB.height = height;
onScreenCanvas.height = height;

document.body.appendChild(onScreenCanvas);

const app = new PIXI.Application({
  view: offScreenCanvasB,
  transparent: true,
  width: 400,
  height: 300
});


const container = new PIXI.Container();
const renderer = PIXI.autoDetectRenderer();

app.stage.addChild(container);

const texture = PIXI.Texture.from('https://picsum.photos/id/237/26/37');

for (let i = 0; i < 25; i++) {
  const bunny = new PIXI.Sprite(texture);
  bunny.anchor.set(0.5);
  bunny.x = (i % 5) * 40;
  bunny.y = Math.floor(i / 5) * 40;
  container.addChild(bunny);
}

container.x = app.screen.width / 2;
container.y = app.screen.height / 2;
container.pivot.x = container.width / 2;
container.pivot.y = container.height / 2;

let ticker = PIXI.Ticker.shared
ticker.add(function(delta) {
  container.rotation -= 0.01;
  renderer.render(container);
  onScreenCanvas.getContext("2d").clearRect(0, 0, width, height);
  onScreenCanvas.getContext("2d").drawImage(offScreenCanvasA, 0, 0, width, height);
  onScreenCanvas.getContext("2d").drawImage(offScreenCanvasB, 0, 0, width, height);
});

let image = new Image();
image.onload = function(e) {
  offScreenCanvasA.getContext("2d").drawImage(e.target, 0, 0, width, height);
}
image.src = "https://picsum.photos/id/237/400/300";
```



```
        let video = document.createElement('video');
        video.preload = 'auto';
        video.loop = true;
        video.autoplay = false;
        video.src = '../assets/placeholder/VIDEO FILE.mp4';
    
        let texture = PIXI.Texture.from(video);

        let videoSprite = new PIXI.Sprite(texture);

        app.stage.addChild(videoSprite);
        

		const videoResource = new PIXI.resources.VideoResource(video); 

        videoResource.updateFPS = 30 // set video to render at 30FPS to avoid performance issues

        let texture = PIXI.Texture.from(videoResource);

        let videoSprite = new PIXI.Sprite(texture);

        this.backgroundVideo = videoSprite

        this.backgroundVideo.height = h
        this.backgroundVideo.width = w

        app.stage.addChild(this.backgroundVideo);
```





### m3u8

[m3u8 下载 GO实现](https://github.com/orestonce/m3u8d) **实测可用**

[m3u8 nodejs 实现](https://github.com/reason211/m3u8-downloader)

[ffpmeg 下载m3u8](https://gist.github.com/tzmartin/fb1f4a8e95ef5fb79596bd4719671b5d)

[xgplayer 纯 js 播放 iptv](https://github.com/bytedance/xgplayer)

[IPTV to HTTP live streaming](https://gist.github.com/drzax/99c468b0c695491784109a4cf21c1c1b)

[ZyPlayer 支持 iptv](https://github.com/Hiram-Wong/ZyPlayer)

[m3u8 python解析](https://github.com/globocom/m3u8)

[有原理](https://github.com/Momo707577045/m3u8-downloader)



```
# https://www.1tv.ru
# https://github.com/yt-dlp/yt-dlp/issues/9521

$  yt-dlp -g "http://cdns.jp-primehome.com:8000/zhongying/live/playlist.m3u8?cid=cs19"  # the -g flag tells youtube-dl to just return the media url[s]
...
https://media.clip.host/..../media.mp4
$ aria2c "https://media.clip.host/..../media.mp4"
```



```bash
iptv-to-hls.sh
#!/bin/bash

while true; do
	currTime=`date +%Y%m%d%H%M`
	if [ "$currTime" -ge 201507081658 -a "$currTime" -le 201507082300 ]; then
		echo "$currTime: Stream should be on. Start ffmpeg if the process does not exist"
		if [ "$(pidof ffmpeg)" ]; then
			echo "$currTime: ffmpeg already running."
			sleep 10
		else
			echo "$currTime: ffmpeg not running. Start it"
			ffmpeg -i 'udp://239.193.4.70:5000' -vcodec libx264 -profile:v high -level:v 4.1 -crf 23 -preset veryfast -vf "yadif" -s 640x320 -maxrate 800k -bufsize 1600k -hls_wrap 16 -acodec libmp3lame -ac 2 -b:a 128k -strict experimental "ftp://iptv1:8gm2taXx@69.163.202.29/tv.elvery.net/hls.m3u8" &
		fi
	else
		echo "$currTime: Stream should be off. Kill ffmpeg if the process exists"
		killall ffmpeg
		sleep 10
	fi
done
```



```
ffmpeg -protocol_whitelist "concat,file,subfile,http,https,tls,rtp,tcp,udp,crypto" -i "http://cdns.jp-primehome.com:8000/zhongying/live/playlist.m3u8?cid=cs19" -vcodec copy -acodec copy -absf aac_adtstoasc out.mp4
	# 成功读到流，但是因为是直播，它没有写入文件？
	# 仔细看它的地址，是可以下载到 .ts 文件的

ffmpeg -i "http://cdns.jp-primehome.com:8000/zhongying/live/playlist.m3u8?cid=cs19" -f s16le -map 0:p:0 -c copy /dev/null 2>&1 | grep 'Opening' | awk -F "'" '{print $2}'



(ffmpeg -i "http://cdns.jp-primehome.com:8000/zhongying/live/playlist.m3u8?cid=cs19" -f s16le -map 0:p:0 -c copy NUL 2>&1) -match "Opening '(.+)'" | ForEach-Object { $Matches[1] }
	# powershell 实现

```



```
./m3u8-windows-amd64.exe -u="http://cdns.jp-primehome.com:8000/zhongying/live/playlist.m3u8?cid=cs19" -ht=apiv2

下载失败，m3u8 地址可能存在嵌套

```



```
curl --location 'http://cdns.jp-primehome.com:8000/zhongying/live/playlist.m3u8?cid=cs19' \
--header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
--header 'Accept-Encoding: gzip, deflate' \
--header 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7' \
--header 'Connection: keep-alive' \
--header 'Host: cdns.jp-primehome.com:8000' \
--header 'Upgrade-Insecure-Requests: 1' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'


#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1101759
http://142.171.31.242:5002/cs19.m3u8?token=guoziyun&gid=cs19&channel=zhongying
	# 返回另一个嵌套地址，嵌套最多只能一层




```







### infer

```python
import gradio as gr

video_path_or_url = Textbox()
video_subtitle_path_or_url = Textbox()
video_with_subtitle = gr.Video()

def set_video(file_path, subtitle_path):
     return {
        video_with_subtitle: gr.update(value=file_path, subtitle=subtitle_path)
    }

demo = gr.Interface(
    fn=set_video,
    inputs=[video_path_or_url, video_subtitle_path_or_url],
    outputs=video_with_subtitle
)

demo.launch() 
```





## pdfjs

see huggingface/vite-pdf  成功显示 pdf ，完成度很高

https://www.gradio.app/guides/pdf-component-example

- https://huggingface.co/spaces/freddyaboulton/gradio_pdf

  - ```
    proxychains4 conda create -n pdf python==3.10 pip && \
    conda activate pdf
    proxychains4 pip install -r demo/requirements.txt && 
    proxychains4 pip install gradio && 
    proxychains4 gradio cc install
    vi gradio-pdf/frontend/package.json
    	"pdfjs-dist":"4.4.168"
    		# 改成这个版本
    gradio cc dev
    	# http://localhost:7861/  成功运行
    	
    
    https://jsfiddle.net/pdfjs/wagvs9Lf/
    pnpm create vite vite-pdfjs -- --template svelte
    cd vite-pdfjs &&
    pnpm install &&
    pnpm run dev
    
    ```

  - 

- https://github.com/freddyaboulton/gradio-pdf

https://gist.github.com/ichord/9808444  pdf 取图片

```
canvas.toDataURL('image/jpeg')
	# canvas 转图片 
	
```





## fastapi+gradio



```python
import fastapi
import gradio as gr
app = gr.Blocks.launch() # this is basically fastapi instance
app.include_router(fastapi.APIRouter())
app.add_api_route("/api/v1/progress", api_progress, methods=["GET"], response_model=ProgressResponse)

class ProgressResponse(BaseModel): # inherits from base Pydantic response:
    progress: float = Field(title="Progress", description="The progress with a range of 0 to 1")

def api_progress():
    return {"progress": 0}
```





```python
import gradio as gr
from fastapi import FastAPI

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

# monkeypatch in url for api docs
def my_setup(self):
    self.docs_url = "/docs"
    self.redoc_url = "/redoc"
    self.orig_setup()

FastAPI.orig_setup = FastAPI.setup
setattr(FastAPI, "setup", my_setup)

# swagger docs should be at http://127.0.0.1:7860/docs
demo.launch()

# reverse monkey patch
FastAPI.setup = FastAPI.orig_setup
```



## svelte

[Debug vscode](https://subscription.packtpub.com/book/web-development/9781839213625/2/ch02lvl1sec11/debugging-svelte-applications)

see https://sveltejs-cn.github.io/svelte-cn/chapter1/script.html

see https://github.com/fikryfahrezy/svelte-player  正常播放的 **纯 svelte 播放器**

see https://github.com/dandiws/svelte-audio-player  **音频播放器**

see https://github.com/PacktPublishing/Svelte-3-Up-and-Running/tree/master/ch2

see https://juejin.cn/post/7204635326559322170 todo list

```
# vscode 设置 -> 搜:
allowBreakpointsEverywhere

vscdoe 插件
	JavaScript Debugger
	Svelte for VS Code

<!-- svelte-ignore a11y-no-static-element-interactions -->
	# 去除警告

```



```
# https://juejin.cn/post/6984045221352849416
# https://juejin.cn/column/6984045100888227876
svelte中的组件名由以下特点:
		1. 组件名的首字母要大写 --- 区分于一般的HTML标签
		2. 组件如果使用单标签的话 --- 必须以/闭合
<Child />

{@debug xxx}
	# chrome 运行到这里会中断？
	
	
响应式声明
  // 当依赖的状态count发生改变的时候，svlete会自动计算并更新doubled的值
  /*
	注意：
            1. 响应式声明只能定义在顶层, 在其余部分定义是会报错的
            2. 定义响应式声明的变量的时候，不需要加var|let|const (此时svelte会自动为该变量进行定义和赋值)
	*/
  $: doubled = count * 2;
  

// 和vue不同的时候，svlete的响应式声明即可以是变量，也可以是语句

// 语句
$: console.log(`the count is ${count}`);

// 代码块
$: {
    console.log(`the count is ${count}`);
    alert(`I SAID THE COUNT IS ${count}`);
}

// 逻辑语句
$: if (count >= 10) {
    alert(`count is dangerously high!`);
    count = 9;
}

svelete的响应式是由赋值触发的

所以诸如 push、splice 等数组方法， 虽然更新了状态，但是因为没有赋值操作，所以不会引起UI(界面)的自动更新。

!!crop_constraint 强转 bool
 	如果`crop_constraint`是一个空字符串、数字0、null或undefined，`!!crop_constraint`将返回false。对于非空字符串、非零数字、非空数组等，`!!crop_constraint`将返回true。


```



```
在 Svelte 中，`context="module"` 是一种特殊的 `script` 标签，它不同于普通的 `script` 标签。`context="module"` 中的代码在组件的生命周期中只执行一次，即使组件被实例化多次。

这其中包括设置属性默认值，导入依赖模块，定义组件之间公用的函数等。`context="module"` 中定义的内容，只对当前组件文件有效，不影响其他组件。
```



### vite

```
see huggingface\vite_gradio_video\readme.txt


see https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/requestVideoFrameCallback
    # 视频播放回调

see python summary -> Gradio -> svelte -> vite

# vscode 设置 -> 搜:
allowBreakpointsEverywhere

vscdoe 插件
	JavaScript Debugger
	Svelte for VS Code

.vscode/launch.json  
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "chrome",
            "request": "launch",
            "name": "Launch Chrome against localhost",
            "url": "http://localhost:5174",
            "webRoot": "${workspaceFolder}"
        }
    ]
}
	# 正常进断点需要这个

pnpm create vite vite-svelte -- --template svelte
cd vite-svelte
pnpm install
pnpm run dev
    # vite 有几个选项，选 svelte ，选 javascript
	# vsocde 里 F5 能正常在 Counter.svelte 单步断下


gradio cc create ivideo --template Video
	# 自定义gradio 的 video 组件
	#　把 frontend 下　node_modules shared　这两个文件夹复到 vite_gradio_video 目录下，能正常引用，并运行
        # 把 dependencies 下的包复制过来， pnpm i 就可以了 


App.svelte
<script>
  import Counter from './lib/Counter.svelte'
  import Player from '../shared/Player.svelte';
	# 这样引用组件

```





### $

- ```
  // see huggingface/gradio440/js/video/shared/VideoControls.svelte
  $g_isTrimMode[gid] = true
    // 这样写就不对劲了
  g_isTrimMode[gid] = true
    // 这样就 OK
  ```

  

- 响应式变量

  ```
  # 依赖更新时它也自动更新
  <script>
    let count = 0;
    $: doubled = count * 2;
  </script>
  ```

  

- 响应式语句

  ```python
  # 依赖更新时整个语句自动重算
  $: console.log(`Count is now ${count}`)
  
  $: $crop && reposition_canvas();
  	# 当全局变量 crop 改变时执行后面的方法 reposition_canvas()
  	# see huggingface/gradio/js/imageeditor/shared/ImageEditor.svelte
  	
  function set_crop(): void {
  		requestAnimationFrame(() => {
  			tick().then((v) => ($active_tool = "crop"));
  		});
  }
  这个函数的作用是在下一个动画帧，将$active_tool的值设置为"crop"。其主要的用途可能是在用户界面中切换到裁剪工具。
  - requestAnimationFrame： requestAnimationFrame是一个浏览器的API，用于执行动画更新。此函数接受一个回调，要在下一个动画帧之前调用。
  - tick： 这是Svelte框架的一个函数，它返回一个Promise，当组件的状态下一次更新时，这个Promise就会解析。
  - $active_tool： 这个变量$active_tool可能保存当前应用中选中的或者正在使用的工具。在这个函数中，$active_tool被更新为"crop"，表明正在使用的工具变为了裁剪工具。
  
  因此，set_crop这个函数的看法主要就是切换应用的工具为裁剪工具，这个操作在下一个动画帧和组件状态下一次更新时发生。
  
  
  	$: editor &&
  		editor.set_tool &&
  		(sources && sources.length
  			? editor.set_tool("bg")
  			: editor.set_tool("draw"));
  			
  	
  
  ```




```
$: t, console.log(t)
  \# 状态改变时 执行后面的语句

```



### \#key

```
# 响应式创建和销毁
# huggingface/gradio440/js/video/shared/InteractiveVideo.svelte
{#if playable()}
			{#key value?.url}
				<Player
				/>
			{/key}
{:else if value.size}
			<div class="file-size">
				{prettyBytes(value.size)}
			</div>
{/if}
	#  value?.url 每当它一变，Player 就会被销毁和重建
	
```





### 传参

```javascript
# see huggingface/gradio440/js/imageeditor/shared/tools/Crop.svelte

	arr:Array<any>
        # 泛用

	const dispatch = createEventDispatcher<{
		crop_start: {
			x: number;
			y: number;
			width: number;
			height: number;
		};
		crop_continue: {
			x: number;
			y: number;
			width: number;
			height: number;
		};
		crop_end: {
			x: number;
			y: number;
			width: number;
			height: number;
		};
	}>();
	
		function set_finished_with_timeout_and_delay(): void {
		if (timer) {
			clearTimeout(timer);
		}
		timer = setTimeout(() => {
			if (triggered) {
				dispatch("crop_end", {
					x: l_p,
					y: t_p,
					width: w_p,
					height: h_p
				});
				triggered = false;
			}

			finished = true;
			position_drag = false;
		}, 1000);
	}

	function handle_crop(
		type: "start" | "stop" | "continue",

		{
			x,
			y,
			width,
			height
		}: {
			x: number;
			y: number;
			width: number;
			height: number;
		}
	): void {
		# 看这里！！！
	
	on:crop_end={({ detail }) => handle_crop("stop", detail)}
	
	
	
```





### 类型检查


```python
type: Literal["numpy", "pil", "filepath"] = "numpy",
        valid_types = ["numpy", "pil", "filepath"]
        if type not in valid_types:
            raise ValueError(
                f"Invalid value for parameter `type`: {type}. Please choose from one of: {valid_types}"
            )
            
export let crop_size: [number, number] | `${string}:${string}` | null = null;
    # crop_size="1:1"
    # gradio_4290/demo/image_editor/run.py
         
let background: Blob | File | null;
    # 背景图类型
    # gradio_4290/js/imageeditor/shared/tools/Sources.svelte
           
const img = await createImageBitmap(background);
	# 从 File 类型创建图片
    # imageeditor/shared/tools/sources.ts
    
export function create_pixi_app({
	target,
	dimensions: [width, height],
	antialias
}: {
	target: HTMLElement;
	dimensions: [number, number];
	antialias: boolean;
}): PixiApp {
    
    
    
export function resize_and_reposition(
	original_width: number,
	original_height: number,
	anchor: "t" | "r" | "l" | "b" | "tl" | "tr" | "bl" | "br" | "c",
	aspect_ratio: number,
	max_width: number,
	max_height: number
): {
	new_width: number;
	new_height: number;
	x_offset: number;
	y_offset: number;
    	# 这第二个括号既可以声明上面的类型，也可以声明下面的类型？
} {
	let new_width = original_width;
	let new_height = original_height;    
    
 
	export let sources: ("upload" | "webcam" | "clipboard")[] = [
		"upload",
		"webcam",
		"clipboard"
	];
    const sources_meta = {
		upload: {
			icon: ImageIcon,
			label: "Upload",
			order: 0,
			id: "bg_upload",
			cb() {
				upload_component.open_file_upload();

				$active_tool = "bg";
			}
		}
    $: sources_list = sources
		.map((src) => sources_meta[src])
		.sort((a, b) => a.order - b.order);
    
```



#### 任意类型数量的参数

```
cb: (...args: any[]) => void;
	# 形参为任意类型，任意数量的参数？
```






### props

#### 属性展开
```
const info = { name: 'Klaus', age: 23, ... }
<Info name={info.name} age={info.age} gender={info.gender} location={info.location}/>
<!-- 等价于 展开props和ES6中的展开运算符 -->
<Info {...info} />

### 在子组中表示父组件传过来的所有属性
$$props

```



### event

https://juejin.cn/post/6985541622641459231



```python
import { tick } from "svelte";
	async function handle_keypress(e: KeyboardEvent): Promise<void> {
		await tick();
		if (e.key === "Enter") {
			e.preventDefault();
			gradio.dispatch("submit");
		}
	}
```





#### 事件分发器（dispatcher）





#### 中间组件必须转发事件

- > 与DOM事件不同，组件事件不会 冒泡
  >
  > 如果要在某个深层嵌套的组件上监听事件，则中间组件必须 转发 该事件



#### 安全刷新

```
# gradio/js/imageeditor/shared/ImageEditor.svelte
	function set_crop(): void {
		requestAnimationFrame(() => {
			tick().then((v) => ($active_tool = "crop"));
		});
	}
	
	import { createEventDispatcher, getContext, onMount, tick } from "svelte";

	onMount(async () => {
		await tick();

一般用于等待一段时间让Svelte去处理它的异步更新，然后再进行下一步的操作或判断。

	function set_crop(): void {
		requestAnimationFrame(() => {
			tick().then((v) => ($active_tool = "crop"));
		});
	}
		# 安全刷新全局变量
	
	
	function wait_for_next_frame(): Promise<void> {
		return new Promise((resolve) => {
			requestAnimationFrame(() => requestAnimationFrame(() => resolve()));
		});
	}	
	async function handle_change(): Promise<void> {
		await wait_for_next_frame();
	
	
	
```



#### ResizeObserver

```
# gradio/js/imageeditor/shared/ImageEditor.svelte
	let pixi_target: HTMLDivElement;
	let canvas_wrap: HTMLDivElement;
	const resizer = new ResizeObserver((entries) => {
			for (const entry of entries) {
				get_dimensions(canvas_wrap, pixi_target);
			}
		});

		resizer.observe(canvas_wrap);
		resizer.observe(pixi_target);
```





### \#each

```
{#each sub_menu.options as meta (meta.id)}
{/each}

gradio_4290/js/imageeditor/shared/tools/Cropper.svelte
	line 295
	{#each { length: 25 } as _}
		<div></div>
	{/each}

```

\- `sub_menu.options` 应该是一个数组。

\- `as meta` 意味着在每次迭代中，当前的数组元素将被命名为 `meta` ，使得您可以在`each`块内部访问它。

\- `(meta.id)` 是一个可选的键表达式，它用来优化列表的更新。当数据发生变化时，Svelte将使用这个键来最小化DOM的更新，因为它能够识别哪些项是新加入的，哪些项已经移除，从而只对有实际变动的项目进行DOM操作。



### filter

```
	
		const fetch_promises = await Promise.all(
			_layer_files.map((f) => {
				if (!f || !f.url) return null;

				return fetch(f.url);
			})
		);

		const blobs = await Promise.all(
			fetch_promises.map((p) => {
				if (!p) return null;
				return p.blob();
			})
		);
		
	function is_not_null<T>(x: T | null): x is T {
		return x !== null;
	}
	
	for (const blob of blobs.filter(is_not_null)) {
	
```







### store 

[1](https://juejin.cn/post/6986642702964097037)

组件的顶层申明Store，并且不可以包含在if代码块中

```
Store 是 Svelte 中的一种特殊的可写状态对象，它允许我们在组件之间共享状态

# see gradio/js/imageeditor/shared/ImageEditor.svelte
const contexts: Writable<context_type[]> = writable([]);
contexts.update((c) => [...c, type]);
	# contexts 是数组， c 是旧值， [...c, type] 是新值
	# ...c 是把所有元素倒出来，装新数组里面， type 加最后面，既构造了一个新数组
	# 有点像 concat
	

type PartialRecord<K extends keyof any, T> = Partial<Record<K, T>>;
	const init_context: Writable<
		PartialRecord<context_type, (dimensions?: typeof $dimensions) => void>
	> = writable({});
init_context.update((c) => ({ ...c, [type]: init_fn })); 
	# type 就是普通字符串，你看它作key要加方括号： [type]
当使用 PartialRecord 类型时，可以创建一个对象，它有以下特点：
- 对象拥有类型 K 中定义的键中的一部分或全部。
- 每个键都对应类型 T 的值。
- 不是所有的 K 键都需要出现在对象中，因为 Partial 使它们可选。

		register_context: (
			type: context_type,
			{
				reset_fn,
				init_fn
			}: {
				reset_fn?: () => void;
				init_fn?: (dimensions?: [number, number]) => void;
			}
		) => {
			contexts.update((c) => [...c, type]);
			init_context.update((c) => ({ ...c, [type]: init_fn }));
			reset_context.update((c) => ({ ...c, [type]: reset_fn }));
		}
			# 注意看字典里函数的签名
		

Partial<T> 生成的类型会将 T 中的每个属性标记为可选
interface MyOriginalInterface {
  property1: string;
  property2: number;
  property3: boolean;
}

// 使用 Partial 将所有属性变为可选
type MyPartialInterface = Partial<MyOriginalInterface>;
// 现在 MyPartialInterface 类型的对象可以缺少任意属性
const examplePartial: MyPartialInterface = {
  property1: "I'm a string",
  // 注意 property2 和 property3 并没有被定义，但是没有类型错误
};



	let editor_box: EditorContext["editor_box"] = writable({
		parent_width: 0,
		parent_height: 0,
		parent_top: 0,
		parent_left: 0,
		parent_right: 0,
		parent_bottom: 0,
		child_width: 0,
		child_height: 0,
		child_top: 0,
		child_left: 0,
		child_right: 0,
		child_bottom: 0
	});
	function get_dimensions(parent: HTMLDivElement, child: HTMLDivElement): void {
		if (!parent || !child) return;
		const {
			width: parent_width,
			height: parent_height,
			top: parent_top,
			left: parent_left,
			right: parent_right,
			bottom: parent_bottom
		} = canvas_wrap.getBoundingClientRect();
		const {
			width: child_width,
			height: child_height,
			top: child_top,
			left: child_left,
			right: child_right,
			bottom: child_bottom
		} = child.getBoundingClientRect();
		editor_box.set({
			child_width,
			child_height,
			child_left,
			child_right,
			child_top,
			child_bottom,

			parent_width,
			parent_height,
			parent_left,
			parent_right,
			parent_top,
			parent_bottom
		});
	}


// store.js
import { writable } from 'svelte/store'
export const time = writable(0)

<!-- Component.svelte -->
	import { onMount, onDestroy } from 'svelte'
	import { time } from "./store.js";
	let t = 0
	let timerID:number
	onMount(() => {
		timerID = setInterval(() => {
			t += 1;
			$time = t;
		}, 1000)
	})
	onDestroy(() => {
		clearInterval(timerID)
	})
	
	<input type="text" readonly={true} bind:value={$time} />

```



```
Svelte 假定所有以 `$` 开头的任何标识符都表示引用某个 store 值，而 `$` 实际上是一个保留字符，
Svelte 会禁止你使用 `$` 作为你声明的变量的前缀。

<script>
  import { count } from './stores.js';
</script>

<h1>count 当前的值是：{$count}</h1>
```



#### 统一定义全局变量

```
import type { Writable, Readable } from "svelte/store";
import { writable } from "svelte/store";

interface EditorContext {
		pixi: Writable<PixiApp | null>;
		current_layer: Writable<LayerScene | null>;
		dimensions: Writable<[number, number]>;
		editor_box: Writable<{
			parent_width: number;
			parent_height: number;
			parent_left: number;
			parent_top: number;
			parent_right: number;
			parent_bottom: number;
			child_width: number;
			child_height: number;
			child_left: number;
			child_top: number;
			child_right: number;
			child_bottom: number;
		}>;
}

	let editor_box: EditorContext["editor_box"] = writable({
		parent_width: 0,
		parent_height: 0,
		parent_top: 0,
		parent_left: 0,
		parent_right: 0,
		parent_bottom: 0,
		child_width: 0,
		child_height: 0,
		child_top: 0,
		child_left: 0,
		child_right: 0,
		child_bottom: 0
	});

```





#### 字典里的函数签名

```
Store 是 Svelte 中的一种特殊的可写状态对象，它允许我们在组件之间共享状态

# see gradio/js/imageeditor/shared/ImageEditor.svelte
const contexts: Writable<context_type[]> = writable([]);
contexts.update((c) => [...c, type]);
	# contexts 是数组， c 是旧值， [...c, type] 是新值
	# ...c 是把所有元素倒出来，装新数组里面， type 加最后面，既构造了一个新数组
	# 有点像 concat
	

type PartialRecord<K extends keyof any, T> = Partial<Record<K, T>>;
	const init_context: Writable<
		PartialRecord<context_type, (dimensions?: typeof $dimensions) => void>
	> = writable({});
init_context.update((c) => ({ ...c, [type]: init_fn })); 
	# type 就是普通字符串，你看它作key要加方括号： [type]
当使用 PartialRecord 类型时，可以创建一个对象，它有以下特点：
- 对象拥有类型 K 中定义的键中的一部分或全部。
- 每个键都对应类型 T 的值。
- 不是所有的 K 键都需要出现在对象中，因为 Partial 使它们可选。

		register_context: (
			type: context_type,
			{
				reset_fn,
				init_fn
			}: {
				reset_fn?: () => void;
				init_fn?: (dimensions?: [number, number]) => void;
			}
		) => {
			contexts.update((c) => [...c, type]);
			init_context.update((c) => ({ ...c, [type]: init_fn }));
			reset_context.update((c) => ({ ...c, [type]: reset_fn }));
		}
			# 注意看字典里函数的签名
		

Partial<T> 生成的类型会将 T 中的每个属性标记为可选
interface MyOriginalInterface {
  property1: string;
  property2: number;
  property3: boolean;
}

// 使用 Partial 将所有属性变为可选
type MyPartialInterface = Partial<MyOriginalInterface>;
// 现在 MyPartialInterface 类型的对象可以缺少任意属性
const examplePartial: MyPartialInterface = {
  property1: "I'm a string",
  // 注意 property2 和 property3 并没有被定义，但是没有类型错误
};
```



```
  const reset_context: Writable<PartialRecord<context_type, () => void>> =
		writable({});
	const init_context: Writable<
		PartialRecord<context_type, (dimensions?: typeof $dimensions) => void>
	> = writable({});
	const contexts: Writable<context_type[]> = writable([]);
```





#### 奇葩的函数签名

```
	function is_not_null(o: Blob | null): o is Blob {
		return !!o;
	}
	
		const fetch_promises = await Promise.all(
			_layer_files.map((f) => {
				if (!f || !f.url) return null;

				return fetch(f.url);
			})
		);

		const blobs = await Promise.all(
			fetch_promises.map((p) => {
				if (!p) return null;
				return p.blob();
			})
		);
		
	function is_not_null<T>(x: T | null): x is T {
		return x !== null;
	}
	
	for (const blob of blobs.filter(is_not_null)) {
```



#### append

```
type context_type = "bg" | "layers" | "crop" | "draw" | "erase";

const contexts: Writable<context_type[]> = writable([]);

contexts.update((c) => [...c, type]);

```



### spring

string 是一种特殊的 store, 它的数值不是一步到位，而是渐近式从初值变到终值。

用subscribe 订阅值的更新　　 

```python
# gradio_4290/js/imageeditor/shared/tools/crop.ts
	import { spring } from "svelte/motion";
	let alpha_spring = spring(current_opacity, {
		stiffness: 0.1,
		damping: 0.5
	});
	alpha_spring.subscribe((value) => {
		if (!final_crop) return;
		spring_value = value;
		crop_mask(width, height, final_crop, true);
	});

```





### timer

```
<script>
  let text = '';

  setInterval(() => {
    text = new Date().toLocaleTimeString();
  }, 2000);
</script>

<input type="text" bind:value={text} />

```





### await



```
import { createEventDispatcher, getContext, onMount, tick } from "svelte";

	onMount(async () => {
		await tick();

一般用于等待一段时间让Svelte去处理它的异步更新，然后再进行下一步的操作或判断。

	function set_crop(): void {
		requestAnimationFrame(() => {
			tick().then((v) => ($active_tool = "crop"));
		});
	}
		# 安全刷新全局变量

```





```
<script>
  // getRandomNumber是一个异步请求，返回的是一个promise
  let getNumberPromise = getRandomNumber();
</script>

<!-- number是一个异步操作返回的promise -->
{#await getNumberPromise}
    <!-- 状态为pending时候进行的操作  -->
    <p>loading ...</p>
{:then number}
    <!-- 状态为resolve时候进行的操作，后面的number是成功后返回的结果 -->
    <p>{number}</p>
{:catch error}
    <!-- 状态为reject时候进行的操作, error是返回的错误对象 -->
    <p>{error.message}</p>
{/await}


<!--
    很多情况下，我们可能并不需要处理状态为pending或reject的情况
    所以此时可以对await块进行简写操作
-->

<!-- 省略状态为pending时候的操作 -->
{#await getNumberPromise then number}
    <p>{number}</p>
{:catch error}
    <p>{error.message}</p>
{/await}

<!-- 同时省略状态为pending和reject的时候对promise结果的处理 -->
{#await getNumberPromise then number}
    <p>{number}</p>
{/await}



```



### animate

```
<script>
    let num = 0;
    let opacity = 1

    function addNumber() {
    opacity = 0
    	
        // 淡出后。修改num的值，并执行淡入效果
    setTimeout(() => {
            num = num + 2
            opacity = 1
    }, 500)
    }
</script>

<!-- 使用transition 实现在切换num值的时候的 淡出和淡入效果 -->
<p style="transition: opacity 0.5s ease; opacity: {opacity};">{ num }</p>
<button on:click="{addNumber}">+2</button>



<!--
    如果按照上述例子的写法，显然是比较繁琐的
    为此，svlete将一些简单的动画进行了封装
-->
<script>
    import { fade } from 'svelte/transition';
    let num = 0;
</script>

<!-- 
    fade只有在创建元素的时候才会生效，所以此时需要为p元素包裹key块，不包裹的时候是不会产生渐入渐出效果
    key块的作用和each块中key的作用是一致，当num发生改变的时候，svelte会自动销毁并重新创建p标签
-->
{#key num}
    <p in:fade>{ num }</p>
{/key}
<button on:click="{() => num += 2}">+2</button>


```



### compile

[compile](https://sveltejs-cn.github.io/svelte-cn/api-compile-time/svelte.compile.html)



### vite

[Vite + Svelte + Tailwindcss](https://juejin.cn/post/7096482075590524936)

```

pnpm create vite vite-svelte -- --template svelte
cd vite-svelte
pnpm install
pnpm run dev
	# 能正常在　.svelte 单步断下


gradio cc create ivideo --template Video
	# 自定义gradio 的 video 组件
	#　把　node_modules shared　这两个库复到到 vite-svelte 里去，能正常引用，并运行
	

App.svelte
<script>
  import Counter from './lib/Counter.svelte'
  import Player from '../shared/Player.svelte';
	# 这样引用组件

npm create vite@latest vite-svelte -- --template svelte
cd vite-svelte
yarn 
yarn dev

```







svelte 选择JSDoc 的原因，只是为了调试方便。

```
<script>
  let count = 0;
</script>

<button on:click={() => count += 1}>
  Clicked {count} {count === 1 ? 'time' : 'times'}
</button>

```



```
class Gradio<T extends Record<string, any> = Record<string, any>> {
```

- **class Gradio {...}**: 定义了一个名为 `Gradio` 的类。
- ** = Record>**: 这是泛型声明。它表示 `Gradio` 类可以接受一个类型参数 `T`，并带有一些约束条件。
  - **T**: 是一个类型变量，使用时可以被替换成任何类型。
  - **extends Record**: 表示 `T` 必须是一个索引签名的对象类型。具体来说：
    - **Record**: 是TypeScript的一个工具类型，表示一个对象，具备字符串类型的键（key）和任意类型的值（value）。等价于 `{ [key: string]: any }`。
  - **= Record>**: 这部分指定了默认类型。如果在实例化或扩展 `Gradio` 类时没有提供具体类型，那么 `T` 默认会是 `Record`。即，默认情况下，`Gradio` 类可以接受含有任意字符串键的对象，并且这些键对应任意类型的值。



```
dispatch<E extends keyof T>(event_name: E, data?: T[E]): void {  
```

- **dispatch**: 这是方法的名称。
- : 方法使用了一个泛型 `E`，它必须是类型 `T` 所有键（key）的类型集合中的一个成员。换句话说，`E` 必须是 `T` 的某个属性的键名。这里的 `T` 对应外部类 `Gradio` 定义中的泛型。
- **(event_name: E, data?: T[E])**: 方法接受两个参数：
  - **event_name**: 第一个参数是 `event_name`，其类型是泛型 `E`，表示该参数的值必须是类型 `T` 中属性的键。
  - **data?**: 第二个参数是 `data`，并且是可选的（这由后面的问号 `?` 表示）。如果提供此参数，它的类型必须是与 `event_name` 相对应的属性的值的类型，即类型 `T` 中键为 `E` 的属性的值类型。这是通过索引类型 `T[E]` 实现的。
- **: void**: 方法的返回类型是 `void`，表示这个 `dispatch` 方法不返回任何值。







### 成功引用 Gradio 前端组件 

[视频播放回调](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/requestVideoFrameCallback) 看它前端实现

- see echodict\svelte\requestVideoFrameCallback

- see gradio_video\frontend\shared\VideoTimeline.svelte

  - ```
    videoDuration = videoElement.duration;
    videoElement.currentTime = newTimeLeft;
    
    ```

```
# see huggingface vite_gradio_video\src\App.svelte
# # vite工程 App.svelte，语法正确，运行正常。成功播放视频
<script lang="ts">
  	import svelteLogo from './assets/svelte.svg'
 	import viteLogo from '/vite.svg'
  	import Counter from './lib/Counter.svelte'


  	import Video from "../shared/Video.svelte"
  	import { playable } from "../shared/utils"

  	let url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4"

	let type: "gallery" | "table";
	let selected = false;
	let value: string;
	let samples_dir: string;
	let video: HTMLVideoElement;
	
	async function init(): Promise<void> {
		video.muted = true;
		video.playsInline = true;
		video.controls = true;
		video.setAttribute("muted", "");
	
		var playPromise = video.play();
		if (playPromise !== undefined) {
			playPromise.then(_ => {
	  			// Automatic playback started!
	  			// Show playing UI.
	  			// We can now safely pause video...
	  			video.pause();
			})
			.catch(error => {
	  			// Auto-play was prevented
	  			// Show paused UI.
			});
		}
	}
</script>

{#if playable()}
	<div
		class="container"
		class:table={type === "table"}
		class:gallery={type === "gallery"}
		class:selected
	>
		<Video
			muted
			playsinline
			bind:node={video}
			on:loadeddata={init}
			on:mouseover={video.play.bind(video)}
			on:mouseout={video.pause.bind(video)}
			src={url}
		/>
	</div>
{:else}
	<div>{value}</div>
{/if}

<style>
	.container {
		flex: none;
		max-width: none;
	}
	.container :global(video) {
		width: var(--size-full);
		height: var(--size-full);
		object-fit: cover;
	}

	.container:hover,
	.container.selected {
		border-color: var(--border-color-accent);
	}
	.container.table {
		margin: 0 auto;
		border: 2px solid var(--border-color-primary);
		border-radius: var(--radius-lg);
		overflow: hidden;
		width: var(--size-20);
		height: var(--size-20);
		object-fit: cover;
	}
	
	.container.gallery {
		height: var(--size-20);
		max-height: var(--size-20);
		object-fit: cover;
	}
</style>
```





```
# vite工程 App.svelte，语法正确，运行出错
<script lang="ts">

	import type { Gradio, ShareData } from "@gradio/utils";
	import type { FileData } from "@gradio/client";
	import Video from "../shared/InteractiveVideo.svelte";
	
	export let label: string;
	export let sources:
		| ["webcam"]
		| ["upload"]
		| ["webcam", "upload"]
		| ["upload", "webcam"];
	export let root: string;
	export let show_label: boolean;
	export let autoplay = false;
	export let gradio: Gradio<{
		change: never;
		clear: never;
		play: never;
		pause: never;
		upload: never;
		stop: never;
		end: never;
		start_recording: never;
		stop_recording: never;
		share: ShareData;
		error: string;
		warning: string;
	}>;
	export let mirror_webcam: boolean;
	export let include_audio: boolean;
	
	let _video: FileData | null = null;
	let _subtitle: FileData | null = null;
	let active_source: "webcam" | "upload";
</script>

<Video
	value={_video}
	subtitle={_subtitle}
	{label}
	{show_label}
	{sources}
	{active_source}
	{mirror_webcam}
	{include_audio}
	{autoplay}
	{root}
	i18n={gradio.i18n}
></Video>
```





### video.play 事件

```
# see huggingface vite_gradio_video\src\App.svelte

let video: HTMLVideoElement;

			on:mouseover={video.play.bind(video)}
	
			on:mouseover={ () => {
				video.play().then(()=>{}).catch((e)=>{})
			}}

```



### bbcode

```
gradio cc create bbcode --template SimpleTextbox --install


demo.launch(debug=True, show_api=False, server_name="0.0.0.0", server_port=6006, inbrowser=True)

```



### slot

[slot](https://juejin.cn/post/6987632912900292622)  在他blog搜 svelte



### token32

```
import secrets
secrets.token_urlsafe(32)
```





### excel

[excel](https://github.com/ticruz38/svelte-sheets)

#### gspread 

https://github.com/burnash/gspread google excel







# Stramlit

```

成功显示 voide 字幕, 本地 vscode 成功断点调试

# pre-requirements.txt
https://github.com/snehankekre/streamlit-video-subtitles-poc/raw/main/streamlit-1.28.0-py2.py3-none-any.whl
	# 这是未合并的分支，装正式版的不行

# README.md
---
title: Streamlit Video Subtitles Poc
emoji: 📈
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.28.0
app_file: main.py
pinned: false
license: mit
---

# launch.json
{
    // streamlit run main.py
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "/root/miniforge3/envs/sapce/bin/streamlit",
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": [
                "run",
                "/root/streamlit-video-subtitles-poc/main.py"
            ]
        }
    ]
}

{
    // streamlit run main.py
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "C:/ProgramData/miniconda3/envs/space/Scripts/streamlit.exe",
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": [
                "run",
                "E:/t/streamlit-bg-video-demo/streamlit_app.py"
            ]
        }
    ]
}



# main.py
import io

import streamlit as st

st.title("📽️ st.video with subtitle/CC support")

st.markdown("For more information, see the [Subtitle/CC support in st.video](https://www.notion.so/snowflake-corp/Subtitle-CC-support-in-st-video-39bd511be61c49dab094672dcd38c09a) Notion page. Get the wheel file [here](https://github.com/snehankekre/streamlit-video-subtitles-poc/raw/main/streamlit-1.28.0-py2.py3-none-any.whl).")
st.write("This feature adds an argument to `st.video` to accept subtitle files")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
    [
        "Single VTT",
        "Single VTT (with label)",
        "Single SRT",
        "Single SRT (with label)",
        "Multiple",
        "Single raw string",
        "Single BytesIO",
        "All supported formats",
        "YouTube",
        "File Uploader",
    ]
)

with tab1:
    st.header("One subtitle in VTT format")
    with st.echo():
        st.video("sample.mp4", subtitles="sample_french.vtt")

with tab2:
    st.header("One labeled subtitle in VTT format")
    with st.echo():
        st.video("sample.mp4", subtitles={"French": "sample_french.vtt"})

with tab3:
    st.header("One subtitle in SRT format")
    with st.echo():
        st.video("sample.mp4", subtitles="sample_english.srt")

with tab4:
    st.header("One labeled subtitle in SRT format")
    with st.echo():
        st.video("sample.mp4", subtitles={"English": "sample_english.srt"})

with tab5:
    st.header("Multiple subtitles in either VTT or SRT format")
    with st.echo():
        st.video(
            "sample.mp4",
            subtitles={
                "English": "sample_english.srt",
                "French": "sample_french.vtt",
                "German": "sample_german.vtt",
            },
        )

with tab6:
    st.header("Raw string")
    with st.echo():
        vtt = """
        WEBVTT FILE

        1
        00:00:03.500 --> 00:00:05.000 D:vertical A:start
        Jeder möchte das Meiste aus dem Leben herausholen
    
        2
        00:00:06.000 --> 00:00:09.000 A:start
        Wie Internet-Erlebnisse, die reichhaltig <b>und</b> unterhaltsam sind
    
        3
        00:00:11.000 --> 00:00:14.000 A:end
        Telefongespräche, bei denen Menschen wirklich <c.highlight>verbinden</c>
        """
        st.video("sample.mp4", subtitles=vtt)

with tab7:
    st.header("One subtitle in SRT format (and BytesIO)")
    with st.echo():
        srt = io.BytesIO(
            """
1
00:00:03,500 --> 00:00:05,000
Everyone wants the most from life

2
00:00:06,000 --> 00:00:09,000
Like internet experiences that are rich and entertaining

3
00:00:11,000 --> 00:00:14,000
Phone conversations where people truly connect

4
00:00:14,500 --> 00:00:18,000
Your favourite TV programmes ready to watch at the touch of a button
""".strip().encode(
                "utf-8"
            )
        )

        st.video("sample.mp4", subtitles=srt)
    
        st.write("Subtitle with label")
    
        st.video("sample.mp4", subtitles={"LLM 1": srt})

with tab8:
    st.header("Multiple subtitles in either VTT or SRT format (and BytesIO)")
    with st.echo():
        srt = io.BytesIO(
            """
1
00:00:03,500 --> 00:00:05,000
Everyone wants the most from life

2
00:00:06,000 --> 00:00:09,000
Like internet experiences that are rich and entertaining

3
00:00:11,000 --> 00:00:14,000
Phone conversations where people truly connect

4
00:00:14,500 --> 00:00:18,000
Your favourite TV programmes ready to watch at the touch of a button
""".strip().encode(
                "utf-8"
            )
        )

        st.video(
            "sample.mp4",
            subtitles={
                "io.BytesIO SRT": srt,
                "German": "sample_german.vtt",
                "English VTT": "sample_english.vtt",
                "English SRT": "sample_english.srt",
            },
        )

with tab9:
    st.header("YouTube")
    st.write(
        "Checking the checkbox below will raise a `StreamlitAPIException` since YouTube videos do not support subtitles."
    )
    if st.checkbox("Show YouTube video"):
        with st.echo():
            st.video(
                "https://www.youtube.com/watch?v=xQwDfW7UHMo",
                subtitles="sample_english.vtt",
            )

with tab10:
    st.header("File Uploader")
    uploaded_file = st.file_uploader("Upload a subtitle file", type=["vtt", "srt"])
    st.video("sample.mp4", subtitles=uploaded_file)




```



## streamlit-rwkv5-jp-explain

```
# st.session_state 必须得 streamit run xx.py 它才不错

import streamlit as st


def evaluate(prompt, token_count, temperature, top_p):
    return f"Generated text based on: {prompt}, {token_count}, {temperature}, {top_p}"

def clear_output():
    st.session_state.output = ""

st.set_page_config(page_title="RWKV-5 training 50 epoch for anime and game text")

st.markdown(f"<div style=\"text-align: center;\">\n<h1>RWKV-5 training 50 epoch for anime and game text - {'rwkv5-jp-explain'}</h1>\n</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Raw Generation", "Tab 2"])

with tab1:
    
    col1, col2 = st.columns(2)
    
    with col1:
        prompt = st.text_area("Prompt", "<User:>ここまでやるとはな<User$>\n\n", height=150)
        token_count = st.slider("Max Tokens", 10, 1024, 1024, 10)
        temperature = st.slider("Temperature", 0.2, 2.0, 1.0, 0.1)
        top_p = st.slider("Top P", 0.0, 1.0, 0.7, 0.05)
    
    with col2:
        submit_button = st.button("Submit")
        clear_button = st.button("Clear")
    
        if 'output' not in st.session_state:
            st.session_state.output = ""
    
        Output = st.text_area(label="Output", value=st.session_state["output"], height=200)
    
        if submit_button:
            st.session_state.output = evaluate(prompt, token_count, temperature, top_p)
    
        if clear_button:
            clear_output()


```



## counter

```
import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment_counter():
	st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)
```



```
import streamlit as st

st.title('Counter Example using Callbacks with kwargs')
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment_counter(increment_value=0):
	st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
	st.session_state.count -= decrement_value

st.button('Increment', on_click=increment_counter,
	kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
	kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.count)
```







Streamlit 定义了 image、audio 和 video 用于展示图片、音频和视频。

可以展示本地多媒体，也通过 url 展示网络多媒体。



see https://github.com/tmgthb/Stream-responses gpt 流式输出

see https://github.com/thistleknot/chatgpt-4/blob/master/streamlit_app.py  gpt chat

see https://image-coordinates.streamlit.app 取图片坐标

see https://image-coordinates.streamlit.app/dynamic_update 图片上画点

see https://github.com/Franky1/Streamlit-ffmpeg-Test/blob/main/streamlit_app.py  ffmpeg 转格式

see https://github.com/streamlit/streamlit/issues/1662  subtitle [1](https://github.com/snehankekre/streamlit-video-subtitles-poc/blob/main/del.py) [2新特性还没有实现 必须用分支](https://github.com/streamlit/streamlit/issues/1662)

see https://github.com/tonykipkemboi/streamlit-bg-video-demo  embed a video as a background

see https://github.com/okld/streamlit-elements  加强库 支持视频控制

see https://github.com/drogbadvc/extract-sub-video-streamlit  硬字幕提取

see https://github.com/streamlit/example-app-interactive-table  table 选中一行

see https://github.com/streamlit/streamlit/issues/2446  自动播放 mp3

see https://github.com/jwsy/streamlit-two-way-binding/blob/main/three_half_miles.py  双向绑定

see https://discuss.streamlit.io/t/copy-dataframe-to-clipboard/2633/22  dataframe  [1](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616/21) 

see https://github.com/whitphx/streamlit-webrtc

- https://github.com/codespaces/  在线开发

see https://github.com/misraturp/Content-Analyzer/blob/master/Main_Page.py

see https://docs.streamlit.io/library/api-reference/media/st.video

see https://gist.github.com/sz1262011/a204b61647604d7ac9606561dd4ac56a





```
import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
    layout='wide',
    page_icon='🎈'
)


st.title('🧫 Title')


st.header('Subtitle 1')
choice = st.radio(label='labels', options=['choice1', 'choice2'], label_visibility='collapsed')

if choice == 'choice1':

    st.write("""
    Choice 1: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """)
    
    st.dataframe(
        pd.DataFrame({
            'A': np.arange(1, 12),
            'B': np.arange(1, 12),
            'C': np.arange(1, 12),
        }),
    )

else:
    st.write("""
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Choice 2: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """)
```



