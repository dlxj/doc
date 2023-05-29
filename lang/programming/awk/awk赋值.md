```
shell里面的赋值方法有两种，格式为
    1) arg=`(命令)`
    2) arg=$(命令)
因此，如果想要把某一文件的总行数赋值给变量nlines，可以表达为：
    1) nlines=`(awk 'END{print NR}' filename)`
或者
    2) nlines=$(awk 'END{print NR}' filename)  
```


