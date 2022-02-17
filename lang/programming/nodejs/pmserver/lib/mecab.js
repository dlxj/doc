
// https://github.com/atilika/kuromoji dict

// https://mebee.info/2021/02/18/post-29277/

// https://www.npmjs.com/package/kuroshiro
// https://github.com/Zerxz/kuroshiro-analyzer-mecab
// https://github.com/hexenq/kuroshiro-analyzer-kuromoji
// npm install kuroshiro@1.1.2
// # 其他版本有Bug


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

            try {

                ruby = await kuroshiro.convert(str, { mode: "furigana", to: "hiragana" })  // jia ming biao zhu
                hiragana = await kuroshiro.convert(str, { to: "hiragana" })
            } catch(e) {
                console.log(`## error in haras funtion in mecab.mjs change kuroshiro2 to segment...`)
                ruby = await kuroshiro2.convert(str, { mode: "furigana", to: "hiragana" })  // jia ming biao zhu
                hiragana = await kuroshiro2.convert(str, { to: "hiragana" })  
            }

            resolve([{ ruby, hiragana, origin: str }, ''])

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





// let kuroshiro = new Kuroshiro()
// await kuroshiro.init(new KuromojiAnalyzer())  // for windows







