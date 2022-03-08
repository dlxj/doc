
let fs = require('fs')

module.exports = {

    extractSrt: function(mlpath) {
       let ml = fs.readFileSync(mlpath, { encoding:"utf-8"})
       ml = ml.replace(/\r\n/g, '\n')

       // <p begin="00:02:14.802" end="00:02:17.304" style="s1">

       let a = 1

        return ml

    } 

}