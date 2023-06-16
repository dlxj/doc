# Install go

[VsCode Go插件配置最佳实践指南](https://zhuanlan.zhihu.com/p/320343679)

[为 Go 开发配置Visual Studio Code](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)



```
ctrl + X, 装 go 插件

ctrl + shift + p ->go install tools ->Go: Install/Update Tools
	->勾选全部 ->ok

ctrl + , ->go.lang ->勾选 Use Language Server 


```



```

go mod init t
	# 必须先执行
	
// t/main.go
package main

import "fmt"

func main() {
    name := "Go Developers"
    fmt.Println("Azure for", name)
}

vscode F5 成功断下

```





```
VsCode Go插件的那些常用快捷
	
	ctrl+p　文件搜索快捷键
	
	ctrl+shift+p　命令快捷键
	
	ctrl+shift+k　删除一行

	alt+左方向键　回到上一次编辑的地方

	ctrl+鼠标左键，跳到方法定义的地方

```

