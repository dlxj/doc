
// 原始语料在 doc\lang\programming\pytorch\机器翻译\中英平行语料520万_translation2019zh  格式是：每行一个JSON 文本， 有两个字段 english 和 chinese 
// 转换为 OpenNMT-py 格式，英文一个文件，中文一个文件

( async () => {

    // let fs = require('fs')
    // fs.readFileSync(fpath, { encoding: 'utf8', flag: 'r' })

    function clean(str) {
       //return str.replace(/\r\n/g, '\n').replace(/\n{2,999}/g, '\n')
       return str
    }

    async function convert(fpath) {

        var data = await new Promise(function (resolve, reject) {

            let lineReader = require('line-reader')
            lineReader.open(fpath, function(err, reader) {
                if (err) return reject(err)
                if (reader.hasNextLine()) {
                  reader.nextLine(function(err, line) {
                    try {
                        if (err) return reject(err)
                        console.log(line)
                    } finally {
                      reader.close(function(err) {
                        if (err) return reject(err)
                    });
                    }
                  });
                } else {
                  reader.close(function(err) {
                    if (err) return reject(err)
                    return resolve(result)
                  })
                }
            })
        })




        // let fs = require('fs')

        // let trainingstr = clean( fs.readFileSync(fpath, { encoding: 'utf8', flag: 'r' }) )
        // let trainingarr = trainingstr.split('\n')
    
        let ens = ''
        let chts = ''
        // for (let s of trainingarr) {
        //     if (s == '') {
        //         continue
        //     }
        //     let trainingarr2 = s.split('\t')
        //     let en = trainingarr2[0]
        //     let cht = trainingarr2[1]
    
        //     ens += `${en}\n`
        //     chts += `${cht}\n`
        // }

        return { ens, chts }

    }

    let { ens:ens1, chts:chts1 } = await convert('./translation2019zh_train.json')

    // let { ens:ens2, chts:chts2 } = convert('./validation.txt')

    // let { ens:ens3, chts:chts3 } = convert('./testing.txt')


    // require('fs').writeFileSync('src-train.txt', ens1, {encoding:'utf-8'} )
    // require('fs').writeFileSync('tgt-train.txt', chts1, {encoding:'utf-8'} )

    // require('fs').writeFileSync('src-val.txt', ens2, {encoding:'utf-8'} )
    // require('fs').writeFileSync('tgt-val.txt', chts2, {encoding:'utf-8'} )

    // require('fs').writeFileSync('src-test.txt', ens3, {encoding:'utf-8'} )
    // require('fs').writeFileSync('tgt-test.txt', chts3, {encoding:'utf-8'} )

})()



