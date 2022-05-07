
// 原始语料在 doc\lang\programming\pytorch\机器翻译\中英平行语料520万_translation2019zh  格式是：每行一个JSON 文本， 有两个字段 english 和 chinese 
// 转换为 OpenNMT-py 格式，英文一个文件，中文一个文件
/*

npm install nodejieba --registry=https://registry.npm.taobao.org --nodejieba_binary_host_mirror=https://npm.taobao.org/mirrors/nodejieba --save
npm install lodash --save

*/

(async () => {

    function clean(str) {
        return str.replace(/\r\n/g, '\n').replace(/\n{2,999}/g, '\n')
    }

    async function convert(fpath1, fpath2) {

        let { msg } = await new Promise(async function (resolve, reject) {

            let fs = require('fs')
            let _ = require('lodash')

            let c1 = _.chunk([1, 2, 3, 4, 5], 3)

            let nodejieba = require("nodejieba")
            let result = nodejieba.cut("南京市长江大桥");
            console.log(result.join(' '))

            fs.rmSync('en_chs', { recursive: true, force: true })
            fs.mkdirSync('en_chs', { recursive: true })

            // var src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            // var tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_val = fs.createWriteStream('en_chs/src-val.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_val = fs.createWriteStream('en_chs/tgt-val.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_test = fs.createWriteStream('en_chs/src-test.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_test = fs.createWriteStream('en_chs/tgt-test.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)


            let src_trains = []
            let tgt_trains = []

            let src_vals = []
            let tgt_vals = []

            let src_tests = []
            let tgt_tests = []

            async function read_big_file(fpath, arr1, arr2) {

                let { msg } = await new Promise(function (resolve2, reject2) {

                    var buffer = '';
                    var rs = fs.createReadStream(fpath)
                    rs.on('data', function (chunk) {
                        var lines = (buffer + chunk).split(/\r?\n/g)
                        buffer = lines.pop()
                        for (var i = 0; i < lines.length; i++) {

                            let line = lines[i]
                            if (line.trim() != '') {
                                line = JSON.parse(line)
                                let english = line.english //clean(line.english)
                                english = english.replace(/(\,)/g, ' $1 ')  // OpenNMT 要通过空格分词，这里把标点和单词拆开
                                english = english.replace(/(\.)/g, ' $1 ')
                                english = english.replace(/(\?)/g, ' $1 ')
                                english = english.replace(/(\!)/g, ' $1 ')
                                english = english.replace(/([^\r\n\S]{2,999})/g, ' ')

                                let chinese = line.chinese // clean(line.chinese)
                                chinese = chinese.replace(/(\，)/g, ' $1 ')  // OpenNMT 要通过空格分词，这里把标点和单词拆开
                                chinese = chinese.replace(/(\、)/g, ' $1 ')
                                chinese = chinese.replace(/(\；)/g, ' $1 ')
                                chinese = chinese.replace(/(\：)/g, ' $1 ')
                                chinese = chinese.replace(/(\。)/g, ' $1 ')
                                chinese = chinese.replace(/(\？)/g, ' $1 ')
                                chinese = chinese.replace(/(\！)/g, ' $1 ')
                                chinese = chinese.replace(/(\《)/g, ' $1 ')
                                chinese = chinese.replace(/(\》)/g, ' $1 ')
                                chinese = chinese.replace(/(\“)/g, ' $1 ')
                                chinese = chinese.replace(/(\”)/g, ' $1 ')
                                chinese = chinese.replace(/(\‘)/g, ' $1 ')
                                chinese = chinese.replace(/(\’)/g, ' $1 ')
                                chinese = chinese.replace(/(\（)/g, ' $1 ')
                                chinese = chinese.replace(/(\）)/g, ' $1 ')




                                chinese = chinese.replace(/([^\r\n\S]{2,999})/g, ' ')
                                // chinese = chinese.replace(/(\p{P})/gu, ' $1 ')  // 正则匹配所有中文标点

                                // src_train.write(english + '\n') 
                                // tgt_train.write(chinese + '\n')

                                arr1.push(english + '\n')
                                arr2.push(chinese + '\n')

                            }

                        }
                    })
                    rs.on('end', function () {
                        // src_train.end()
                        // tgt_train.end()
                        //console.log(`done one task ${fpath}`)
                        return resolve2({ msg: 'ok.' })


                    })

                })

                return { msg }

            }

            let { msg: m1 } = await read_big_file(fpath1, src_trains, tgt_trains)
            let { msg: m2 } = await read_big_file(fpath2, src_vals, tgt_vals)


            async function writeSync(arr, steam) {

                for (let s of arr) {

                    steam.write(s)

                }

                await new Promise(async function (resolve_, reject_) {
                    steam.end(() => {
                        return resolve_('done.')
                    })
                })

                return {msg:'done'}

            }

            let chunks1 = _.chunk(src_vals, src_vals.length - 100)  // 分一百作测试集
            let chunks2 = _.chunk(tgt_vals, tgt_vals.length - 100)


            src_vals = chunks1[0]
            tgt_vals = chunks2[0]

            src_tests = chunks1[1]
            tgt_tests = chunks2[1]


            await writeSync(src_trains, src_train)
            await writeSync(tgt_trains, tgt_train)

            await writeSync(src_vals, src_val)
            await writeSync(tgt_vals, tgt_val)

            await writeSync(src_tests, src_test)
            await writeSync(tgt_tests, tgt_test)

            return resolve({ msg: 'ok.' })

        })


        let ens = 'file too large to return string'
        let chts = '文件太大，无法返回字符串'

        return { ens, chts }

    }

    let { ens, chts } = await convert('./translation2019zh_train.json', './translation2019zh_valid.json')

})()



