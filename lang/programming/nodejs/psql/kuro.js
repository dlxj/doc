
// let kuromoji = require('kuromoji')

// kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {
   
//    let a = tokenizer.tokenize('abc')

//    console.log(a)

//    b = 1

// })


(async () => {

   let kuromoji = require('kuromoji')

   let [ tokenizer, ms ] = await new Promise(function (resolve) {

     kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {

       if (err) resolve([ null, err.toString() ] )
  
       resolve([ tokenizer, ''])
    
    })

   })

   let arr = require('fs').readFileSync('./data.json', {encoding:'utf8', flag:'r'})

   arr = JSON.parse(arr)

   

   let a = tokenizer.tokenize(arr[0])

   let hanas = ''

   for (let i = 0; i < a.length; i++) {

      let item = a[i]

      let basic_form = item.basic_form

      hanas += basic_form

   }

   

   console.log(a)

   b  = 1

})()

