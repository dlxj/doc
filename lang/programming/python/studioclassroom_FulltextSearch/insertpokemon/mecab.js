
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

module.exports = {
    haras: async function haras(str) {

        let [hiras, msg] = await new Promise(async function (resolve) {

            kuroshiro.init(new KuromojiAnalyzer())  // for windows
                //kuroshiro.init(mecabAnalyzer)     // for linux
                .then(async function () {
                    let ruby = await kuroshiro.convert(str, { mode: "furigana", to: "hiragana" })  // jia ming biao zhu
                    let hiragana = await kuroshiro.convert(str, { to: "hiragana" })
                    resolve([{ ruby, hiragana, origin: str }, ''])
                })
                .catch((err) => {
                    resolve([null, err])
                })
        })

        return [hiras, msg]

    }
}

/*

    let [hiras, msg] = await libmecab.haras('感じ取れ')

    console.log( hiras, msg )

*/





