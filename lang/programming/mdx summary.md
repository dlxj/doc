

## js-mdict

[js-mdict 很新](https://github.com/terasum/js-mdict/issues/67)

```
const Mdict = require('js-mdict');
const dict = new Mdict.default('./testDict/data.mdx');  <= you should use Mdict.default;
console.log('lookup red', dict.lookup('red'));
```

