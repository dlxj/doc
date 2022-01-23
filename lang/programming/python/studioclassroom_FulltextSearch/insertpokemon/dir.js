
let rd = require('rd')
let path = require('path')

module.exports = {

    allmkv : function(dir, filter) {

        var paths = []

        // 目录下的所有文件名
        rd.eachFileFilterSync(dir, /\.mkv$/, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (filter != undefined && fullpath.indexOf(filter) != -1) {
                paths.push(fullpath)
            } else if (filter == undefined ) {
                paths.push(fullpath)
            }
            
        })

        return paths

    }

}