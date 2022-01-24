
import { eachFileFilterSync } from 'rd'
import path from 'path'

export default {

    allmkv : function(dir, filter) {

        var paths = []

        // 目录下的所有文件名
        eachFileFilterSync(dir, /\.mkv$/, function (fullpath, stats) {

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