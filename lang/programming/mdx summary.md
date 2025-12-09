

## js-mdict

[js-mdict 很新](https://github.com/terasum/js-mdict/issues/67)

```
const Mdict = require('js-mdict');
const dict = new Mdict.default('./testDict/data.mdx');  <= you should use Mdict.default;
console.log('lookup red', dict.lookup('red'));
```



```





MDD 基本格式和 MDX 结构类似，只是 key:value 变成 filename:file content

同时给 GoldenDict 提了 feature request，希望他们能加上 mdx/mdd 支持。
https://github.com/goldendict/goldendict/issues/203



mdx就是html的子集，mdx特有的语法：@@@LINK=条目 重定向条目内容，entry="条目#id" 条目跳转，sound:// 音频引用链接。就这三个



老版的 MdxBuilder 3.0 RC1 是已知的 MdxBuilder 3.x 的**最后一个版本**，制作出的 mdx 词库**兼容** GoldenDict 等开源词典新版的 MdxBuilder 4.x 制作出的 mdx 词库升级了格式、优化了索引，适用于新版的 MDict 词典，但与 GoldenDict 等开源词典存在**兼容性问题**也就是说，如果想要制作出的 mdx 词库完美**兼容** GoldenDict 等开源词典，推荐使用**老版**的 MdxBuilder 3.x


这次排版是我自己写的，有必要说明下词典内容和排版。

圆角方框内是词性选择框，当这个词头有多个释义时，这玩意将出现，单个释义时，不会有这个。可以点击跳转到对应词性。￼

方角方框内就是词性标题。￼

灰色背景内容是词条的解释。

小圆点是例句。

小圆点下面的小灰字是例句的中文翻译。

发音后面的 ① ② 等是日语的声调。

查看词条你会发现有251874个，这是我加了汉语查询、平假查询的跳转，所以你可以放心用平假和汉语查询这本词典。不过就像开头所说，实际词头是92998。







```

