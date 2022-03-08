
let fs = require('fs')

module.exports = {

    extractSrt: function({str, mlpath=null}) {
       let ml = str
       if (mlpath != null) {
        ml = fs.readFileSync(mlpath, { encoding:"utf-8"})
       } 
       ml = ml.replace(/\r\n/g, '\n')
       let matchs = ml.matchAll(String.raw`<p begin="(\d\d:\d\d:\d\d.\d\d\d)"\s+end="(\d\d:\d\d:\d\d.\d\d\d)".+?>(.+?)</p>`)
       let arr = Array.from(matchs)
       for (let match of arr) {

        let origin = match[0]
        let begin = match[1]
        let end = match[2]
        let text = match[3]
        text = text.replace(/<span.+?>/g, '').replace(/<\/span>/g, '').replace(/<br\s*\/>/g, '\n')

        let a = 1

       } 
       //a.replace(/<span.+?>/g, '').replace(/<\/span>/g, '').replace(/<br\s*\/>/g, '\n')

       let a = 1

        return ml

    } 
}






























module.exports.extractSrt({str:`<p begin="00:02:14.802" end="00:02:17.304" style="s1"><span style="s2">（アナウンサー）<span style="s3">さあ イワーク</span><br /><span style="s3">巨体を生かして—</span></span></p>`})
