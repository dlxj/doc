### 使用第三方API教程

1. 到 https://mathf.xyz/ 购买app_id 和 app_key，**如果你是第一次购买请认真阅读公告**

3. 按照[安装教程](https://github.com/itewqq/MathpixCsharp/blob/master/README.md)装好客户端。安装完之后如果没找到在哪儿启动请打开```开始```进行查找。
4. 第一次打开会弹出在名为```login```的窗口，在里面填入之前的app_id和app_key，**下方的复选框选择```第三方Key```**，**注意不要选错**，选错了会导致无法使用。然后点击确认。只需要填一次之后再打开就不用填了。如果填错了或者要更换Key可以在主界面点击```菜单->重置Key```。
   
![image.png](https://i.loli.net/2021/02/19/rbQ4LYlG37OqywS.png)

> 强调一下，无论使用官方API还是第三方API，使用本客户端必须要填入两个字段，app_id和app_key。注意是**两个字段**，app_id和app_key，我觉得在教程里以及第三方的公告里已经写得很清楚了，不知道为什么很多人还是只填一个app_key，或者根本不填，或者没有把卡密的格式处理好直接带四个#来填进去，然后来找我发邮件问为什么不能用= =

5. 客户端主界面如下图，使用第三方Api的时候右上角会显示当前Key的剩余使用次数：

![image.png](https://i.loli.net/2021/02/19/ucQt4NAfgOnGP2X.png)

6. 使用时需要先截屏选择要识别的公式。点击**截屏按钮**或者使用**快捷键Ctrl+Alt+Q** (0.0.6及之前的版本是Ctrl+Alt+M)开始截屏。进入截屏模式时，**鼠标会变成十字形**，如果进入截屏模式后不想截屏了，可以**按右键取消截屏**。截屏过程类似QQ的截屏功能，鼠标按下开始截屏，拖动选择区域，松开完成截屏。
7. 截屏完成后客户端会自动完成识别，并将识别结果置于文本框内，点击文本框对应的按钮可以复制到剪贴板。为了方便使用，**默认情况下程序会自动把inline的公式复制到剪贴板，无需点击按钮**，如果点击了按钮，则之后的默认复制会记住本次的选择，在之后的自动复制中会选取该选择进行自动复制。完整的演示流程参考下图：
![使用演示](/images/demo1.gif)

8. 当点击关闭窗口的时候，MathpixCsharp会自动最小化到系统托盘，**如果要退出客户端，请右键系统托盘上的客户端图标再选择退出。**
9. **关于Office Word中的公式**：Word用户请点击**复制MathML**按钮，然后在word文档里**右键->粘贴->仅粘贴文本**。有时候Ctrl+V会有问题，但是现在这个问题貌似很少出现了。另外，由于Word自身处理公式的问题，有时候一些带括号的公式可能会出现这种情况：
![image.png](https://i.loli.net/2021/02/19/yKu7RCmknDGNz8V.png)这时候只需要把**光标放在公式最后面，敲一下回车**就好了。如果还有问题，就把**光标放在异常的括号后面，点一下空格**就好了。

注： 使用**多个显示器**时，MathpixCsharp将选择**其窗体当前所在的屏幕**进行截屏。