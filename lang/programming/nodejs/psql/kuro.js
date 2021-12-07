

/*



See: nodejs summary.md -> centos7+mecab+neologd

https://kuroshiro.org/

const result = Kuroshiro.Util.isHiragana("あ"))

isKanji(char)

isJapanese(char)

*/


// let kuromoji = require('kuromoji')

// kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {

//    let a = tokenizer.tokenize('abc')

//    console.log(a)

//    b = 1

// })


(async () => {

  let arr = require('fs').readFileSync('./data.json', { encoding: 'utf8', flag: 'r' })

  arr = JSON.parse(arr)

  let gss = NG('abcd')

  a = 1


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







  var ffmpeg = require('fluent-ffmpeg');
  const path = require('path');
  
  // var filename = './not-commit-test-file/1.mp4';
  // var full_path = path.resolve(filename);
  
  // var command = ffmpeg(full_path)

  // command.outputOptions([
  //   '-vn',
  //   '-acodec copy',
  // ]).save('output-audio.aac')

  var vd = require('fs').createReadStream('F:/1.mkv')
  var au = require('fs').createWriteStream('tmp.mp3')

  ffmpeg(vd).output(au)
  .noVideo()
  .format('mp3')
  .outputOptions('-ab','192k')
  .outputOptions('-ss','00:01:12.960')
  .outputOptions('-to','00:01:14.640')
  .run().on('start',()=>{

    a = 1
    
  })
  .on('end', ()=>{ 

    a = 1
  })


  a = 1


  /*
  
00:01:12.960 -to 00:01:14.640

  "-ss", begintime, "-to", endtime

  */







  var MeCab = new require('mecab-async')
  var mecab = new MeCab()
  //MeCab.command = "mecab"
  MeCab.command = "mecab -d /usr/lib64/mecab/dic/mecab-ipadic-neologd"
  //var text = arr[0]
  
  

  let str = arr[1]

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
    originals += d.original + " "

  })
  

  //let kanji_ngrams = NG(kanjis)
  //let original_ngrams = NG(originals)


  console.log( result )

  //console.log( kanji_ngrams )

  //console.log( original_ngrams )
  
  const Kuroshiro = require("kuroshiro")
  const KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji")
  const MecabAnalyzer = require("kuroshiro-analyzer-mecab")
  const kuroshiro = new Kuroshiro()

  const mecabAnalyzer = new MecabAnalyzer({
    dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd",
    execOptions: {
      maxBuffer: 200 * 1024,
      timeout: 0
    }
  })

  let [ hiras, msg] = await new Promise(function (resolve) {

    //kuroshiro.init(new KuromojiAnalyzer())
    kuroshiro.init(mecabAnalyzer)
    .then(function(){
      return kuroshiro.convert(str, { to: "hiragana" } )
    })
    .then(function(result) {  
      resolve( [ result, '' ] )
    }).catch((err) => {
      resolve( [ null, err ] )
    })

  })
  
  //originals = originals.replaceAll(String.raw`\s`, '')
  hiras = hiras.replaceAll(String.raw`\s`, '')
  let hiras_ngrams = NG(hiras)

  console.log( hiras_ngrams )

  console.log(originals)
  console.log(hiras)




  a = 1

})()



function NG(strs) {

  function ng(s, n) {

    var grs = []

    for (let i = 0; i < s.length; i++) {

      if ( i + n > s.length ) {
        break
      }

      var gr = s.substring(i, i+n)

      grs.push(gr)
      

    }

    return grs

  }

  var gss = []
  for (let i = 2; i <= 10; i++) {
    
    let gs = ng(strs, i)

    if (gs.length > 0) {

      gss = gss.concat( gs )

    } else {

      break

    }

  }

  return gss

}


String.prototype.replaceAll = function(search, replacement) {
  var target = this
  return target.replace(new RegExp(search, 'g'), replacement)
}



/*


var video = fs.createReadStream('F:/1.mkv')
var audio = fs.createWriteStream('1.mp3')
ffmpeg(video).output(audio)
.noVideo()
.format('mp3')
.outputOptions('-ab','192k')
.run();


*/