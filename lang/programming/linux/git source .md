# Linux 获取最新版本Git并编译安装 [z](https://zhuanlan.zhihu.com/p/74953334)



## 1.安装依赖

### Git 的工作需要调用 curl，zlib，openssl，expat，libiconv 等库的代码，所以需要先安装这些依赖工具。在有 yum 的系统上（比如 Fedora）或者有 apt-get 的系统上（比如 Debian 体系），可以用下面的命令安装：

```bash
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel lftp -y
sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev lftp -y
```

## 2.获取最新版本

```bash
git_version=$(lftp https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/ -e "cls;bye" | grep -e "git-[0-9].*.tar.gz" | sed -r 's/git-(.*).tar.gz/\1/g' | sort -rV | xargs | awk -F ' ' '{print $1}')
```

### 命令详解

- 第1步

```bash
lftp https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/ -e "cls;bye"
```

访问 [https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/](https://link.zhihu.com/?target=https%3A//mirrors.ustc.edu.cn/kernel.org/software/scm/git/) ， 使用lftp内的cls命令，列出服务器上所有的文件名称，然后bye退出 - 第2步

```bash
grep -e "git-[0-9].*.tar.gz"
```

使用grep命令搭配正则表达式，筛选出类似git-2.3.8.tar.gz这样格式的文件名 - 第3步

```bash
sed -r 's/git-(.*).tar.gz/\1/g'
```

使用sed的正则表达式分组功能，上面筛选出的文件名中的版本号提取出来 - 第4步

```bash
sort -rV
```

使用sort命令的版本号排序功能(-V),将上面提取出的版本号从高到低排序(-r)

- 第5步

```bash
xargs | awk -F ' ' '{print $1}')
```

使用xargs命令将多行输出内容转换成一行以空格分隔的输出内容，通过管道传递给awk命令，然后使用awk命令以空格为分隔符，获取第一个最高的版本号

## 3.编译安装

```bash
wget https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/git-${git_version}.tar.gz
tar -zxvf git-${git_version}.tar.gz
cd git-${git_version}
make prefix=/usr/local all
make prefix=/usr/local install
```

## 4.验证

```bash
git --version
```

### 一键执行

- CentOS

```bash
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel lftp -y
git_version=$(lftp https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/ -e "cls;bye" | grep -e "git-[0-9].*.tar.gz" | sed -r 's/git-(.*).tar.gz/\1/g' | sort -rV | xargs | awk -F ' ' '{print $1}')
wget https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/git-${git_version}.tar.gz
tar -zxvf git-${git_version}.tar.gz
cd git-${git_version}
make prefix=/usr/local all
make prefix=/usr/local install
```

- Ubuntu

```bash
sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev lftp -y
git_version=$(lftp https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/ -e "cls;bye" | grep -e "git-[0-9].*.tar.gz" | sed -r 's/git-(.*).tar.gz/\1/g' | sort -rV | xargs | awk -F ' ' '{print $1}')
wget https://mirrors.ustc.edu.cn/kernel.org/software/scm/git/git-${git_version}.tar.gz
tar -zxvf git-${git_version}.tar.gz
cd git-${git_version}
make prefix=/usr/local all
make prefix=/usr/local install
```

### 参考：

[Git - 安装 Git](https://link.zhihu.com/?target=https%3A//git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)