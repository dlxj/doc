
// let kuromoji = require('kuromoji')

// kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {
   
//    let a = tokenizer.tokenize('abc')

//    console.log(a)

//    b = 1

// })


(async () => {

   let arr = require('fs').readFileSync('./data.json', {encoding:'utf8', flag:'r'})

   arr = JSON.parse(arr)

   // let kuromoji = require('kuromoji')

   // let [ tokenizer, ms ] = await new Promise(function (resolve) {

   //   kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {

   //     if (err) resolve([ null, err.toString() ] )
  
   //     resolve([ tokenizer, ''])
    
   //  })

   // })



   

   // let a = tokenizer.tokenize(arr[0])

   // let basics = ''
   // let surfaces = ''
   // let readings = ''

   // for (let i = 0; i < a.length; i++) {

   //    let item = a[i]

   //    let basic_form = item.basic_form
   //    let surface_form = item.surface_form
   //    let reading =  item.reading

   //    basics += basic_form + " "
   //    surfaces += surface_form + " "
   //    readings += reading + " "

   // }

   

   // console.log(a)



   // //var MeCab = new require('mecab-async-winfix')
   // var MeCab = new require('mecab-async')
   // , mecab = new MeCab()

   // //mecab.ENCODING = 'UTF-8'
 

   // let [ result, ms2 ] = await new Promise(function (resolve) {

   //    mecab.parse('ここ', function(err, result) {

   //       if (err) resolve([ null, err.toString() ] )

   //       resolve([ result, ''])

   //    })

 
   //  })

   
   // console.log(result)


   var MeCab = new require('mecab-async')
   var mecab = new MeCab();
       //MeCab.command = "mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
       var text = 'こんにちは、サミュエルLジャクソンです。'
       //注：パースコマンドを利用する時 "MeCab.~"と大文字にしないと動かないみたいです
       MeCab.parseFormat(text, function(err, morphs) {
           if (err) throw err;
           morphs.map(function(morph) {
           if (morph.lexical === '感動詞') {
             console.log(morph.lexical + ' : ' + morph.original);
           }
           if (morph.lexical === '名詞') {
             console.log(morph.lexical + ' : ' +morph.original);
           }
       });
       });


   b  = 1

})()

