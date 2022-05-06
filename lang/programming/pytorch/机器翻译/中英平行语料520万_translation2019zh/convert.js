
// 原始语料在 doc\lang\programming\pytorch\机器翻译\中英平行语料520万_translation2019zh  格式是：每行一个JSON 文本， 有两个字段 english 和 chinese 
// 转换为 OpenNMT-py 格式，英文一个文件，中文一个文件

(async () => {

    // let fs = require('fs')
    // fs.readFileSync(fpath, { encoding: 'utf8', flag: 'r' })

    function clean(str) {
        return str.replace(/\r\n/g, '\n').replace(/\n{2,999}/g, '\n')
    }

    async function convert(fpath1, fpath2) {

        var data = await new Promise(function (resolve, reject) {

            var fs = require('fs')

            fs.rmSync('en_chs', { recursive: true, force: true })
            fs.mkdirSync('en_chs', { recursive: true })

            var src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            var tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_trains = []
            let tgt_trains = []
            

            async function read_big_file(fpath) {

                var data = await new Promise(function (resolve2, reject2) {

                    

                })

                var buffer = '';
                var rs = fs.createReadStream(fpath)
                rs.on('data', function (chunk) {
                    var lines = (buffer + chunk).split(/\r?\n/g)
                    buffer = lines.pop()
                    for (var i = 0; i < lines.length; ++i) {
    
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
    
                            src_trains.push(english + '\n')
                            tgt_trains.push(chinese + '\n')
    
                        }
    
                    }
                })
                rs.on('end', function () {
                    src_train.end()
                    tgt_train.end()
                    console.log(`done one task ${fpath}`)
                    // return resolve({ msg: 'ok.' })
    
                    
    
                })
            }



        })

        let ens = 'file too large to return string'
        let chts = '文件太大，无法返回字符串'

        return { ens, chts }

    }

    let { ens, chts } = await convert('./translation2019zh_train.json', './translation2019zh_valid.json')

    // let { ens:ens2, chts:chts2 } = convert('./validation.txt')

    // let { ens:ens3, chts:chts3 } = convert('./testing.txt')


    // require('fs').writeFileSync('src-train.txt', ens1, {encoding:'utf-8'} )
    // require('fs').writeFileSync('tgt-train.txt', chts1, {encoding:'utf-8'} )

    // require('fs').writeFileSync('src-val.txt', ens2, {encoding:'utf-8'} )
    // require('fs').writeFileSync('tgt-val.txt', chts2, {encoding:'utf-8'} )

    // require('fs').writeFileSync('src-test.txt', ens3, {encoding:'utf-8'} )
    // require('fs').writeFileSync('tgt-test.txt', chts3, {encoding:'utf-8'} )

    let a = 1

})()



