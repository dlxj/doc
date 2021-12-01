
var kuromoji = require("kuromoji");

kuromoji.builder({ dicPath: "node_modules/kuromoji/dict" }).build(function (err, tokenizer) {
  // tokenizer is ready
  var path = tokenizer.tokenize("すもももももももものうち");
  console.log(path);
  a = 1
});

