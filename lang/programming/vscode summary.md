[TOC]

 

VSCode   Alt + <-     Alt +   ->   前跳  回跳

F12 进入函数

F11 切换全屏

# bookmark

- https://github.com/alefragnani/vscode-bookmarks

CTRL + K + S 设置快捷键

CTRL + K + K 设成加书签

CTRL + K + P 设成跳到上一个

CTRL + K + N 设成跳到下一个



# 代码放大缩小



```
ctrl + + 
ctrl + -
```





# 彻底删除vscode配置

- https://www.cnblogs.com/muou2125/p/10388440.html

  > 彻底删除vscode及安装的插件和个人配置信息



```
删除 C:\Users\i\.vscode	
删除 C:\Users\i\AppData\Roaming\Code  
```



# 合并分支



先切到主分支 -> 分支 -> 合并分支 -> 先择一个分支



# 回退到指定版本



先切换到要回退的分支  -> git log （或着用 Github Destop 查看更清晰） -> copy md5 -> git reset --hard  md5



# vue 在vscode 下断点

- https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html

  > vscode 安装插件 JavaScript Debugger
  >
  > ```
  > 新建 launch.json， 弹出的选项选择 chrome
  > 重点是：先在终端 npm run dev，看它的端口是什么，下面的url 端口就填什么，然后在vscode F5，会打开浏览器, 就可以在vscode 下断了
  > {
  >  "version": "0.2.0",
  >  "configurations": [
  >      {
  >          "type": "chrome",
  >          "request": "launch",
  >          "name": "vuejs: chrome",
  >          "url": "http://localhost:8082",
  >          "webRoot": "${workspaceFolder}/src",
  >          "sourceMapPathOverrides": {
  >              "webpack:///src/*": "${webRoot}/*"
  >          }
  >      }
  >  ]
  > }
  > ```
  >
  > ```
  > vue.config.js
  > 
  > var titme = Date.now();
  > var d = {
  >   //可在浏览器中调试 说明： https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html
  >   configureWebpack: {
  >     devtool: 'source-map',
  >     output: { // 输出重构  打包编译后的 文件名称  【模块名称.版本号.时间戳】
  >       filename: `js/[name].${titme}.js`,
  >       chunkFilename: `js/[name].${titme}.js`
  >     },
  >   },
  >   // 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度
  >   productionSourceMap: false,
  >   // // 设置生成的 HTML 中 <link rel="stylesheet"> 和 <script> 标签的 crossorigin 属性（注：仅影响构建时注入的标签）
  >   publicPath: './', // 设置打包文件相对路径
  >   // 输出文件目录
  >   outputDir: "webv2",
  > }
  > console.log(`${process.env.NODE_ENV}`)
  > if( process.env.NODE_ENV.match(/build/g) ){ 
  >   delete d.configureWebpack.devtool
  >   d.productionSourceMap = false;
  > }
  > module.exports = d
  > ```



# 远程调试

- Remote Development 安装插件

https://matpool.com/supports/doc-vscode-connect-matpool/

​    VS Code 远程连接矩池云机器教程






# CPP



## Windows



## G++ debug args

```bash
-O0 -Wall -g2 -ggdb
```



launch.json

```javascript
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/textrank",
            "args": ["/home/ubuntu/workcode/cpp/textrank-master/data/news.seg", "1", "2", "./out.txt"],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```





### Clang

1. Install [LLVM 10.0 for win64](https://releases.llvm.org/download.html)

2. clang  -v

3. clang hello.cpp

   ```cpp
   #include <iostream>
   using namespace std;
   int main() {
       cout << "hello world" << endl;
   }
   ```

4. Install [MinGW-w64](http://mingw-w64.org/doku.php/download)
   - add path:  D:\usr\MingGW\mingw64\bin
   - gcc -v



[VScode单步调试](https://blog.csdn.net/fb_941219/article/details/93511926)



> 整体思路就是首先按照常规方法进行mkdir build && cd build && cmake.. && make （这一步可以在vscode的终端完成，也可以在系统终端完成，无所谓。但是为了少开点界面就在vscode里面完成比较好）生成可执行文件，然后使用vscode进行单步





# Python





## Terminal Run



View -> Terminal 

> python --version
> python iTextRankTest.py





## Plugin Run

> Ctrl + Shift + X  -> search python  -> install
> Ctrl + Shift + P ->  python select interpreter





## Formatting

> 
>
> pip install yapf
>
> linting





I had the same issue and to fix that I added following line to the settings.json file:

{
    // to fix 'Timeout waiting for debugger connections'
    "python.terminal.activateEnvironment": false
}

```py
"python.terminal.activateEnvironment": false
```





## Jupyter Notebook



```
python -m pip install --upgrade pip
pip install wheel
```



pip install jupyter

- pip install --user jupyter  出错就用这个



python -m jupyter notebook --version



python -m pip install -U matplotlib



**Ctrl+Shift+P** -> **Python: Create New Blank Jupyter Notebook**

> 注意大小写都要正确





Python: Select interpreter to start Jupyter server



```
python -m pip install -U matplotlib
```



# Python Interactive Network Visualization Using NetworkX, Plotly, and Dash

https://towardsdatascience.com/python-interactive-network-visualization-using-networkx-plotly-and-dash-e44749161ed7





需要手动加入

C:\Users\echod\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Scripts



Could not build wheels for notebook, since package 'wheel' is not installed.



```
@echo off
cd /d E:
cd %cd%
jupyter notebook
cmd.exe
```



# Win10提升管理权限删除顽固文件

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





# networkx plot graph



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
>  (0, 2): Text(-0.4999999999999998, 0.1325001701718984,
>
> "{'weight': 0.2}"),
>
> 
>
>  (1, 2): Text(0.13279379500757726, 0.3346403042157172, "{'weight': 0.1}")}



[

[0.  0.4 0.2],

[0.4 0. 0.1],

 [0.2 0.1 0. ]

]



https://reference.wolfram.com/language/GraphUtilities/ref/PageRanks.html

https://www.mathworks.com/help/textanalytics/ref/textrankscores.html

https://github.com/YevaGabrielyan/tldl



# Windows



# Win10 WSL | Ubuntu 18.04 with Xfce & Xrdp



## MUST make sure that the XRDP doesn’t use port 3389 

- which is used by Microsoft RDP (in case if your Windows 10 is already configured for RDP)



```
sudo apt install xfce4
sudo apt install xrdp && \
sudo echo xfce4-session >~/.xsession && \
sudo service xrdp restart
```



### Change the port from 3389 to 3390



```
vi /etc/xrdp/xrdp.ini

service xrdp restart
```



## Use Win10 remote destop to connect



Press Win key -> 附件 -> 远程桌面

> input: 
>
> localhost:3390








```

sudo apt-get install xfce4

如果网速较慢，这会持续一段时间。

然后安装xrdp组件和vnc服务器：

sudo apt-get install xrdp vnc4server

安装好后要自行新建配置文件，使得在远程登录时默认使用xfce作为界面登录，然后重启xrdp服务：

echo "xfce4-session" >~/.xsession

sudo service xrdp restart

这个相当于在当前用户的home目录下新建一个名为.xsession的隐藏文件，并向文件中写入一行xfce4-session。也可以用touch新建文件，并用vi编辑：

touch ~/.xsession

vi ~/.xsession
```







