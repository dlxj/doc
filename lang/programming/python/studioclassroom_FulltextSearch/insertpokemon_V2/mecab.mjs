
// https://mebee.info/2021/02/18/post-29277/

// https://www.npmjs.com/package/kuroshiro
// https://github.com/Zerxz/kuroshiro-analyzer-mecab
// https://github.com/hexenq/kuroshiro-analyzer-kuromoji
// npm install kuroshiro@1.1.2
// # 其他版本有Bug

import Kuroshiro from "kuroshiro"
import KuromojiAnalyzer from "kuroshiro-analyzer-kuromoji"
import MecabAnalyzer from "kuroshiro-analyzer-mecab"  // only linux
let mecabAnalyzer = new MecabAnalyzer({
    dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd",
    execOptions: {
        maxBuffer: 200 * 1024,
        timeout: 0
    }
})
let kuroshiro = new Kuroshiro()

export default {

    init: async function () {
        if (process.platform == 'win32') {
            await kuroshiro.init(new KuromojiAnalyzer())  // for windows
        } else if (process.platform == 'linux') {
            await kuroshiro.init(mecabAnalyzer)           // for linux
        } else if (process.platform == 'darwin') {
            await kuroshiro.init(mecabAnalyzer)
        } else {
            throw 'unknow os type.'
        }
    },

    haras: async function haras(str) {

        let [hiras, msg] = await new Promise(async function (resolve) {

            let ruby = await kuroshiro.convert(str, { mode: "furigana", to: "hiragana" })  // jia ming biao zhu
            let hiragana = await kuroshiro.convert(str, { to: "hiragana" })
            resolve([{ ruby, hiragana, origin: str }, ''])

        })

        return [hiras, msg]
    }
}

/*

    let [hiras, msg] = await libmecab.haras('感じ取れ')

    console.log( hiras, msg )

*/





// let kuroshiro = new Kuroshiro()
// await kuroshiro.init(new KuromojiAnalyzer())  // for windows







