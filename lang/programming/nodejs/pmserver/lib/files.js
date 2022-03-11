
let rd = require('rd')
let path = require('path')

module.exports = {

    allfiles : function(dir, ext, filters=[]) {

        let paths = []

        let reg = new RegExp(String.raw`\.${ext}$`)
        // 目录下的所有文件名
        rd.eachFileFilterSync(dir, reg, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (filters.length > 0) {

                let allfitQ = true
                for (let filter of filters) {
                    if ( fullpath.indexOf(filter) == -1 ) {
                        allfitQ = false
                        break
                    }
                    
                }

                if (allfitQ) {
                    paths.push(fullpath)
                }

            } else {
                paths.push(fullpath)
            }
            
        })

        return paths

    },
    allmkv : function(dir, filter=null) {

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