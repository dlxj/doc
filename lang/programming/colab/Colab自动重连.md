

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

