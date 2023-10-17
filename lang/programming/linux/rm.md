```
# 删不掉 .git 是因为有进程占用
lsof +D .git
kill -9 
rm -rf .git
	# 成功删除
```



```
rm -- -r
	# 删除名为 -r 的顽固文件
```

