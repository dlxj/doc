
// 原始语料在 doc\lang\programming\pytorch\李宏毅2020机器翻译\HW8_Seq2Seq\cmn-eng  格式是： 英文 + TAB + 中文
// 转换为 OpenNMT-py 格式，英文一个文件，中文一个文件

(() => {

    function clean(str) {
       return str.replace(/\r\n/g, '\n').replace(/\n{2,999}/g, '\n')
    }

    function convert(fpath) {
        let fs = require('fs')

        let trainingstr = clean( fs.readFileSync(fpath, { encoding: 'utf8', flag: 'r' }) )
        let trainingarr = trainingstr.split('\n')
    
        let ens = ''
        let chts = ''
        for (let s of trainingarr) {
            if (s == '') {
                continue
            }
            let trainingarr2 = s.split('\t')
            let en = trainingarr2[0]
            let cht = trainingarr2[1]
    
            ens += `${en}\n`
            chts += `${cht}\n`
        }

        return { ens, chts }

    }

    let { ens:ens1, chts:chts1 } = convert('./training.txt')

    let { ens:ens2, chts:chts2 } = convert('./validation.txt')

    let { ens:ens3, chts:chts3 } = convert('./testing.txt')

    


    require('fs').writeFileSync('src-train.txt', ens1, {encoding:'utf-8'} )
    require('fs').writeFileSync('tgt-train.txt', chts1, {encoding:'utf-8'} )

    require('fs').writeFileSync('src-val.txt', ens2, {encoding:'utf-8'} )
    require('fs').writeFileSync('tgt-val.txt', chts2, {encoding:'utf-8'} )

    require('fs').writeFileSync('src-test.txt', ens3, {encoding:'utf-8'} )
    require('fs').writeFileSync('tgt-test.txt', chts3, {encoding:'utf-8'} )

    let a = 1
})()



