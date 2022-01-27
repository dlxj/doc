
let rd = require('rd')
let path = require('path')

module.exports = {

    allfiles : function(dir, ext, filter=null) {

        let paths = []

        let reg = new RegExp(String.raw`\.${ext}$`)
        // 目录下的所有文件名
        rd.eachFileFilterSync(dir, reg, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (filter != null && fullpath.indexOf(filter) != -1) {
                paths.push(fullpath)
            } else if (filter == null ) {
                paths.push(fullpath)
            }
            
        })

        return paths

    }
}