
/*

  "dependencies": {
    "fluent-ffmpeg": "^2.1.2",
    "kuroshiro": "~1.2.0",
    "pg": "^8.7.1",
    "pg-pool": "^3.4.1"
  }

*/

(async () => {

    var arguments = process.argv

    console.log( arguments[2] )

    String.prototype.replaceAll = function (search, replacement) {
        var target = this
        return target.replace(new RegExp(search, 'g'), replacement)
    }

    // let arr = require('fs').readFileSync('./data.json', { encoding: 'utf8', flag: 'r' })

    // arr = JSON.parse(arr)

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

    let str = arguments[2] // arr[0]

    let [hiras, msg] = await new Promise(function (resolve) {

        //kuroshiro.init(new KuromojiAnalyzer())
        kuroshiro.init(mecabAnalyzer)
            .then(function () {
                return kuroshiro.convert(str, { to: "hiragana" })
            })
            .then(function (result) {
                resolve([result.toString(), ''])
            }).catch((err) => {
                resolve([null, err])
            })

    })

    //originals = originals.replaceAll(String.raw`\s`, '')
    hiras = hiras.replaceAll(String.raw`\s`, '')
    let hiras_ngrams = NG(hiras)

    // console.log( hiras_ngrams )

    // console.log(originals)
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

