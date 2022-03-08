
let fs = require('fs')

module.exports = {

    extractSrt: function(mlpath) {
       let ml = fs.readFileSync(mlpath, { encoding:"utf-8"})
       ml = ml.replace(/\r\n/g, '\n')
       let matchs = ml.matchAll(String.raw`<p begin="(\d\d:\d\d:\d\d.\d\d\d)"\s+end="(\d\d:\d\d:\d\d.\d\d\d)".+?>(.+?)</p>`)
       let arr = Array.from(matchs)
       for (let match of arr) {

        let origin = match[0]
        let begin = match[1]
        let end = match[2]

       } 
       //a.replace(/<span.+?>/g, '').replace(/<\/span>/g, '').replace(/<br\s*\/>/g, '\n')

       let a = 1

        return ml

    } 

}