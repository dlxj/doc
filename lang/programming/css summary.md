



# 标准盒子

```
/**
  快速弹性布局
*/
* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: none;
}



```

**content-box** 所指定的宽度**仅表示内容的宽高**，实际显示的宽高还要加上：边框（border），内边距（padding），外边距（margin）

**border-box**  所指定的宽度 = 内容 + 内边距 + 边框 的宽高，但不包括外边距



[border](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 和 outline 很类似，但有如下区别：

- **outline 不占据空间，绘制于元素内容周围。**
- 根据规范，outline 通常是矩形，但也可以是非矩形的。



# display: flex

```

<div class="headerBox d-flex flex-between w-100 p-x-2">

    <div class="d-flex flex-center-y">
        <b>书籍名称：</b><p class="m-r-2">石油石化职业技能鉴定试题集:轻烃装置操作工</p> <a href="javascript:void(0);" >更换</a>
    </div>

</div>

<style>

body {
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size: 14px;
    line-height: 1.5;
    color: #515a6e;
    background-color: #fff;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.headerBox{    
  position: fixed;
  top: 45px;
  left: 0px;
  height: 30px;
  display: flex;
  align-items: center;
  align-self: center;
}

.flex-between{
  -webkit-box-pack: justify;
  -ms-flex-pack   : justify;
  justify-content : space-between;
}

.w-100{width: 100%;}
.h-100{height: 100%;}

.p-x-2{padding-left:0.5rem;padding-right:0.5rem;}


.m-r-2{margin-right:0.5rem;}

/*水平布局*/
.d-flex {
display: -webkit-box;
display: -ms-flexbox;
display: flex;
}

.flex-center-y{
align-items: center;
align-self: center;
}

a {
    color: #409EFF;
    text-decoration:none;
}

a:hover {
    color: #409EFF;
    text-decoration:underline;
}

</style>

```



**margin-right** 右外边距



# color

```
.probErr {
  color: rgb(51, 31, 233) !important;
  font-weight: bold;
}
.wrongChar {
  color: red !important;
  font-weight: bold;
}
```





# ttf font

```
<html>

<body>
	<div id="expandMenu">
		<i id="expandMenuIcon" style="
		font-family: 'iviewFont';
		display: inline-block;
    	font-style: normal;
    	font-weight: normal;
    	font-variant: normal;
    	text-transform: none;
    	text-rendering: auto;
    	line-height: 1;
    	-webkit-font-smoothing: antialiased;
    	-moz-osx-font-smoothing: grayscale;
    	vertical-align: middle;
		
		">
			&#xf11f;
		</i>

		<!-- import ViewUI from 'view-design';
			 import 'view-design/dist/styles/iview.css';
			 Vue.use(ViewUI); -->
		<!-- ios-arrow-forward &#xf11f; -->
		<!-- ios-folder-open-outline &#xf1d0  font-size: 100px; -->
	</div>
</body>
<style>
	@font-face {
		font-family: iviewFont;
		src: url('ionicons.ttf');
	}

	#expandMenu {
		float: left;
		cursor: pointer;
		text-align: center;
		margin-left: -8px;
	}

	#expandMenu:hover {
		color: #09f;
	}

	#expandMenuIcon {
		font-size: 20px;
		margin-top: calc(50vh - 10px);
	}
</style>

</html>
```





