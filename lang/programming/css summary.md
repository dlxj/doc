

# div > :global



```
div > :global(.md.prose) {
    color: var(--block-info-text-color);
    font-weight: var(--block-info-text-weight);
    font-size: var(--block-info-text-size);
    line-height: var(--line-sm);
}

div {
    margin-bottom: var(--spacing-md);
}
```

这里的 CSS 分为两部分，分别设置了 `div > :global(.md.prose)` 和 `div` 元素的样式。

------

## 背后的设计原因

1. **为什么使用 `:global`？**

   - `:global` 是特定 CSS 工具或框架（如 CSS Modules 或 Svelte 的 Scoped CSS）中的写法，用来解除样式的局部作用域限制。当你在某些框架（比如 Svelte）中使用 scoped CSS 时，默认的样式规则仅对当前组件生效，但可能需要定义全局的样式，使样式可以影响其他组件中触及的元素。
   - 在这里，`:global(.md.prose)` 表示 `.md.prose` 是一个 **全局类名**，不会受组件作用域限制，而 `div >` 是为了限定作用范围，仅应用于当前组件的某些结构（即 `div` 中的直接后代元素 `.md.prose`）。

   **作用：确保 `.md.prose` 的样式能跨组件生效，同时限制在特定结构下调用该样式。**

------

1. **避免使用 `!important`**

   - `!important` 是一种非常强制性的方式，用来提高 CSS 样式优先级，但过多使用 `!important` 会带来难以维护的样式冲突，因此一般是在没办法的情况下才使用。
   - 在这段代码中，并未使用 `!important` 强制覆盖其他样式，而是通过清晰的选择器优先策略（如使用更具体的 `div > :global(.md.prose)`）实现了对元素样式的精准控制，从而避免了使用 `!important`。

   **作用：通过精确的选择器提升优先级，避免了使用强制的 `!important`，提高了代码的可维护性。**

------

1. **为什么设置 `margin-bottom` 在 `div` 上，而不是子元素 `span`？**

   - `div` 的样式中设置了 `margin-bottom: var(--spacing-md);`，这是为了给某些元素在块级布局中添加间距，比如段与段之间的下边距。
   - CSS 的 `margin` 属性只对块级（block-level）元素生效，如果子元素是 `span`（默认是 `display: inline`），它不会响应 `margin-bottom`。换句话说，将 `margin-bottom` 设置在 `span` 上是无效的。

   在实际情况中，可能遇到了 `:global(.md.prose)` 使用了 `span` 或其他内联元素，因此改为将 `margin-bottom` 设置在 `div`，这是块级元素，能正确应用下边距。

    

   **作用：保证间距适用于块级布局，而不会因为子元素为内联元素（`display: inline`）导致样式无效。**





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

	<div id="leftPanel" style="width: 200px;
			  box-shadow: 0 0 5px #ccc;
			  overflow: hidden;
			  position: fixed;
			  left: 5px;
			  top: 80px;
			  bottom: 5px;
			">
		<div style="position:absolute;left:0px;top:0px;right:0px;bottom:0px;margin:auto;
		  margin:0rem;
		  display: -webkit-box;
		  display: -ms-flexbox;
		  display: flex;
		  -ms-flex-direction: column;
		  flex-direction: column;
		">
			<header>
				<div id="ocrMenuPanel" style="padding: 6px 0px;
			  border-bottom: 1px solid rgb(235, 233, 233);
			  overflow: hidden;">

					<div>
						<i style="
				font-family: 'iviewFont';
				display: inline-block;
				font-style: normal;
				font-weight: normal;
				font-variant: normal;
				font-size: calc(5vh - 15px);
				text-transform: none;
				text-rendering: auto;
				line-height: 1;
				-webkit-font-smoothing: antialiased;
				-moz-osx-font-smoothing: grayscale;
				vertical-align: middle;
				
				"
				title="选择图片"
				>
							&#xf1d0;
						</i>

					</div>
			</header>
			<main style="-webkit-box-flex: 1;
			-ms-flex: 1;
			flex: 1;
			overflow-y: auto;
			">

			</main>

		</div>
	</div>


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

<script>
	let expandMenuIcon = document.querySelector('#expandMenuIcon')
	expandMenuIcon.addEventListener('click', () => {
		console.log(`clicked.`)
		expandMenuIcon.style.display = 'none'  // 隐藏
		// expandMenuIcon.style.display = "inline-block"  // 显示  
	}, true)
</script>

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





