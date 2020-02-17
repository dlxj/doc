



MDD 基本格式和 MDX 结构类似，只是 key:value 变成 filename:file content

同时给 GoldenDict 提了 feature request，希望他们能加上 mdx/mdd 支持。
https://github.com/goldendict/goldendict/issues/203



mdx就是html的子集，mdx特有的语法：@@@LINK=条目 重定向条目内容，entry="条目#id" 条目跳转，sound:// 音频引用链接。就这三个



老版的 MdxBuilder 3.0 RC1 是已知的 MdxBuilder 3.x 的**最后一个版本**，制作出的 mdx 词库**兼容** GoldenDict 等开源词典新版的 MdxBuilder 4.x 制作出的 mdx 词库升级了格式、优化了索引，适用于新版的 MDict 词典，但与 GoldenDict 等开源词典存在**兼容性问题**也就是说，如果想要制作出的 mdx 词库完美**兼容** GoldenDict 等开源词典，推荐使用**老版**的 MdxBuilder 3.x

