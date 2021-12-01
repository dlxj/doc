
let kuromoji = require('kuromoji')

kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {
   
   let a = tokenizer.tokenize('abc')

   console.log(a)

   b = 1

})

