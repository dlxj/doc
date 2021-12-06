
// let kuromoji = require('kuromoji')

// kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {

//    let a = tokenizer.tokenize('abc')

//    console.log(a)

//    b = 1

// })


(async () => {

  let arr = require('fs').readFileSync('./data.json', { encoding: 'utf8', flag: 'r' })

  arr = JSON.parse(arr)

  NG('abcd')


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
  var mecab = new MeCab()
  MeCab.command = "mecab"
  //MeCab.command = "mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
  //var text = arr[0]
  
  

  let str = arr[0]

  let [ result, ms ] = await new Promise(function (resolve) {

    MeCab.parseFormat(str, function (err, morphs) {
      
      if (err) resolve([ null, err.toString() ] )

      resolve([ morphs, ''])

    })

  })

  let kanjis = ''
  let originals = ''
  result.forEach(d => {

    kanjis += d.kanji
    originals += d.original

  })
  


  console.log( result )

 

  a = 1

})()



function NG(strs) {

  function ng(s, n) {

    var grs = []

    for (let i = 0; i < s.length; i++) {

      let j = i
      
      do {

        if ( j + n > s.length ) {
          break
        }

        var gr = s.substring(j, j+n)

        grs.push(gr)


        j += 1

      }
      while(j < s.length)
      

    }

    return grs

  }

  let gs = ng(strs, 2)

  return gs

}


/*

abcd

0:'ab'
1:'bc'
2:'cd'
3:'bc'
4:'cd'
5:'cd'

*/