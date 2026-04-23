# 汉字坚排包

https://typst.app/universe/package/hanzi-calligraphy/

- https://github.com/yuegeao/hanzi-calligraphy

https://github.com/QwenLM/Qwen3-VL/blob/main/cookbooks/ocr.ipynb  千问3 VL 能输出单个字符坐标

https://github.com/readest/readest  **全平台阅读器** 比 koreader 好  





```

winget install --id Typst.Typst

typst init @preview/hanzi-calligraphy:0.2.0

vscode trae 安装 Typst LSP、Tinymist Typst 插件
            
```



```

编译 Typst 代码非常简单，主要使用 `typst` 命令行工具。针对你的文件 [template.typ](file:///e:/t/t/hanzi-calligraphy/template/template.typ)，你可以使用以下两种常用方式进行编译：

**1. 单次编译（生成 PDF）**
如果你只想编译一次并生成 PDF 文件，请在终端（命令行）中运行：
​```bash
typst compile e:\t\t\hanzi-calligraphy\template\template.typ
​```
这会在同一个目录下生成一个 `template.pdf` 文件。

**2. 监听模式（保存时自动编译）**
如果你正在编写代码并希望每次保存时自动更新 PDF（非常适合配合 PDF 预览插件使用），可以使用 `watch` 命令：
​```bash
typst watch e:\t\t\hanzi-calligraphy\template\template.typ
​```

**⚠️ 注意事项：**
我刚才尝试为你运行编译命令，但发现当前环境中没有找到 `typst` 命令。你需要确保已经安装了 Typst CLI 并将其添加到了系统的环境变量中。
* 如果你还没有安装，可以前往 [Typst GitHub Releases](https://github.com/typst/typst/releases) 下载对应系统的可执行文件。
* 如果你使用的是 VS Code 或 Trae 这样的编辑器，强烈建议安装 **Typst LSP** 和 **Tinymist Typst** 插件，这样你甚至不需要手动敲击命令，直接在编辑器内就能一边写代码一边实时预览生成的 PDF 效果。

```





# ∩ sect not cap

```

Typst 语法中，表示“交集（ [ o bj ec tO bj ec t ] ∩ ）”的数学符号应为 sect 而不是 Latex 中常用的 cap

```



# ≠ != not neq

```

≠ 的符号并不是像 LaTeX 那样使用 neq ，而是直接使用 != 。

```







# LuaMetaTeX

LuaMetaTeX(LMTX， LuaTeX的后继者，ConTeXt当前的实际引擎)

https://github.com/Fusyong/vertical-typesetting

https://blog.xiiigame.com/2022-06-19-ConTeXt%E5%8F%8C%E8%A1%8C%E5%A4%B9%E6%B3%A8%E7%9A%84%E7%AE%80%E5%8D%95%E5%AE%9E%E7%8E%B0/ 双行夹注



```
ConTeXt LMTX是与LuaMetaTeX(LuaTeX的后继者)配合使用的、最新的ConTeXt版本。调整后当可用于LuaTeX。可以使用context --version && luametatex --version命令查看你的环境版本。
如下编译排版脚本：
> context 大学章句.lmtx
如果控制台显示中文时有乱码，可用命令临时改变代码页：
> chcp 65001


```



