





```bash
find . -type f | xargs cat | 
 grep "<p>.*仁.*<span class='note-inline'>(\[CloseCurlyDoubleQuote]
  仁者(而親反周禮云德一曰仁鄭玄曰愛人及物曰仁上下相親曰仁釋名仁者忍也好生惡煞善惡含忍也)。
```



# 特定串后的 5 行

```
 see postgresql summary.md -> supabase -> Supabase 配置
 
 grep -A 5 "Captcha Config" /opt/supabase/.env
 
```





# sed 修改文件

```
$sed 's/unix/linux/' geekfile.txt  # 所有 unix 改为 linux
$sed 's/unix/linux/2' geekfile.txt # 第二次出现的unix 改为linux
$sed 's/unix/linux/g' geekfile.txt # 所有 unix 改为 linux
$sed 's/unix/linux/3g' geekfile.txt # 第三次出现开始(包含) 和之后所有出现的unix 改为linux

```



```
# b 表示 begin，所有以A-Z开头的字母，替换成( + A-Z + )
$echo "Welcome To The Geek Stuff" | sed 's/\(\b[A-Z]\)/\(\1\)/g'  
> (W)elcome (T)o (T)he (G)eek (S)tuff
```



```
$sed 's/batch_size\:\ 16/batch_size\:\ 12/1' td500_resnet18_deform_thre.yaml #打印不修改
$sed 's/num_workers\:\ 16/num_workers\:\ 12/1' td500_resnet18_deform_thre.yaml

$sed -i 's/batch_size\:\ 16/batch_size\:\ 12/1' td500_resnet18_deform_thre.yaml #修改不打印
$sed -i 's/num_workers\:\ 16/num_workers\:\ 12/1' td500_resnet18_deform_thre.yaml


```





```
sed -e 's/foo/bar/' myfile

将 myfile 文件中每行第一次出现的foo用字符串bar替换，然后将该文件内容输出到标准输出

sed -e 's/foo/bar/g' myfile

g 使得 sed 对文件中所有符合的字符串都被替换, 修改后内容会到标准输出，不会修改原文件

sed -i 's/foo/bar/g' myfile
选项 i 使得 sed 修改文件

sed -i 's/foo/bar/g' ./m*
批量操作当前目录下以 m 开头的文件

sed -i 's/foo/bar/g' `grep foo -rl --include="m*" ./`

```







