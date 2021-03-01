$ arch

x86_64





uname -a

lsb_release -a



centos only

cat /etc/redhat-release

```csharp
# cpu info
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
```



```bash
# 修改当前用户的PATH
# 永久有效，仅对当前用户
vi ~/.bashrc
export PATH=/home/data/users/weiqibang/project/flask_server/Anaconda3/bin:$PATH

source ~/.bashrc

```



