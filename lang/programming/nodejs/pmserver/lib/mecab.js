
// https://github.com/atilika/kuromoji dict

// https://mebee.info/2021/02/18/post-29277/

// https://www.npmjs.com/package/kuroshiro
// https://github.com/Zerxz/kuroshiro-analyzer-mecab
// https://github.com/hexenq/kuroshiro-analyzer-kuromoji
// npm install kuroshiro@1.1.2 kuroshiro-analyzer-kuromoji@1.1.0 kuroshiro-analyzer-mecab@1.0.1
// # 其他版本有Bug
/*
    "kuroshiro": "~1.1.2",
    "kuroshiro-analyzer-kuromoji": "~1.1.0",
    "kuroshiro-analyzer-mecab": "~1.0.1",
*/


let Kuroshiro = require("kuroshiro")
let KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji")
let MecabAnalyzer = require("kuroshiro-analyzer-mecab")  // only linux
let mecabAnalyzer = new MecabAnalyzer({
    dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd",
    execOptions: {
        maxBuffer: 200 * 1024,
        timeout: 0
    }
})
let kuroshiro = new Kuroshiro()
let kuroshiro2 = new Kuroshiro()

let MeCab  = require("@zerxz/mecab-async")
let mecab = new MeCab()
// mecab.wakachi('いつもニコニコあなたの隣に這い寄る混沌ニャルラトホテプです！', function(err, result) {
//     if (err) throw err;
//     console.log(result);
// });

module.exports = {

    init: async function () {
        
        //await kuroshiro2.init(new KuromojiAnalyzer())

        if (process.platform == 'win32') {
            await kuroshiro.init(new KuromojiAnalyzer())  // for windows
        } else if (process.platform == 'linux') {
            await kuroshiro.init(new KuromojiAnalyzer(mecabAnalyzer))  // for linux  // has Crash BUG: let [hirass, msgg] = await libmecab.haras("お願いします! ピカピカ! ")  
            await kuroshiro2.init(new KuromojiAnalyzer())
            //await kuroshiro.init(new KuromojiAnalyzer({dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd"}))  // dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd"     /usr/lib64/mecab/dic/ipadic
        } else if (process.platform == 'darwin') {
            await kuroshiro.init(new KuromojiAnalyzer())    
        } else {
            throw 'unknow os type.'
        }
    },
    hiras: async function (str) {

        let [hrs, msg] = await new Promise(async function (resolve) {

            let ruby = null
            let hiragana = null
            let spaced = null

            try {

                ruby = await kuroshiro.convert(str, { mode: "furigana", to: "hiragana" })  // jia ming biao zhu
                hiragana = await kuroshiro.convert(str, { to: "hiragana" })
                //spaced = await kuroshiro.convert(str, {mode:"okurigana", to:"hiragana"})

                spaced = await new Promise(async function (resolve, reject) {
                    mecab.wakachi(str, function(err, result) {
                        if (err) reject(err)
                        resolve(result.join(' ').replace(/\s+/g, ' '))
                    })
                })

            } catch(e) {
                console.log(`## error in haras funtion in mecab.mjs change kuroshiro2 to segment...`)
                ruby = await kuroshiro2.convert(str, { mode: "furigana", to: "hiragana" })  // jia ming biao zhu
                hiragana = await kuroshiro2.convert(str, { to: "hiragana" })  
                spaced = await kuroshiro2.convert(str, {mode:"okurigana", to:"hiragana"})
            }

            resolve([{ ruby, spaced, hiragana, origin: str }, ''])

        })

        return { hiras:hrs, msg }
    },
    isJP: function(str) {
        // https://github.com/hexenq/kuroshiro
        if ( Kuroshiro.Util.hasKana(str)) {  // hiragana AND katakana
            return true
        }
        // else if (hasKanji(str)) {
        //     return true
        // }
        return false

    }
}

/*

    let [hiras, msg] = await libmecab.haras('感じ取れ')

    console.log( hiras, msg )

*/


// (async () => {

// //let kuroshiro = new Kuroshiro()
// // await kuroshiro.init(new KuromojiAnalyzer())  // for windows
// // let a = await kuroshiro.convert("感じ取れたら手を繋ごう、重なるのは人生のライン and レミリア最高！", {mode:"okurigana", to:"hiragana"})


// let b = 1

// })()











