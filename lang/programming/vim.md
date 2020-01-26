
:$  or  G   跳到文件尾  
:0  or  gg 跳到文件首  
A  跳到行尾，并进入后插模式    
I  跳到行首，并进入前插模式    
u  撤销上次更改   
dd 删除当前行    
ndd 删除多行    
nyy  复制多行    

:noh  取消高亮  

~/.bash_profile 每次shell 启动都会执行的文件，在次设置环境变量  

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

PATH="${HOME}/usr/bin:${PATH}"
export PATH

PATH="${HOME}/.local/bin:${PATH}"
export PATH

PATH="${HOME}/.cabal/bin:${PATH}"
export PATH

IHaskell notebook 指定内核    
ipython3 kernelspec list    

进去选Haskell 内核  
jupyter notebook  



