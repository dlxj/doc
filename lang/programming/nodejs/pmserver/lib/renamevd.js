
let fs = require('fs')
let path = require('path')

module.exports = {

    renamevd:function(rootvd, rootttml2) {

        let aa = this

        //let m4s = this.libs.files.allfiles(rootvd, 'mp4')

        let kvs = this.libs.files.allfiles(rootvd, 'mkv', ['amazon', 'pokemon'])


        let ttml2s = this.libs.files.allfiles(rootttml2, 'ttml2')

        for (let ttml of ttml2s) {

            let match= ttml.match(/(\d+)\./)
            if (match == null) {
                //throw `name not correct. ${ttml}`
                continue
            }
            let nth = match[1]

            for (let m4 of kvs) {

                let match2 = m4.match(/E(\d+) - Amazon/)
                if (match2 == null) {
                    //throw `name not correct. ${m4}`
                    continue
                }
                let nth2 = match2[1]

                if (Number(nth) == Number(nth2)) {

                    //ttml
                    let { base,dir,ext,name,root} = path.parse(ttml)
                    let { base:base2,dir:dir2,ext:ext2,name:name2,root:root2} = path.parse(m4)

                    let newname = `${name}.mkv`
                    let newpath = path.join(dir2, newname)

                    fs.renameSync( m4, newpath )
                }

            }

        }

        return 'ok.'
    }

}




























/*

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon'])


*/