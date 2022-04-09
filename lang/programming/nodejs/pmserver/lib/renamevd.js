
let fs = require('fs')
let path = require('path')

module.exports = {

    renamevd:function(rootvd, rootttml2) {

        let aa = this

        //let m4s = this.libs.files.allfiles(rootvd, 'mp4')

        //let kvs = this.libs.files.allfiles(rootvd, 'mkv', ['amazon', 'pokemon'])

        let platform = process.platform
        let root_vd = global.config.root_vd[platform]

        let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon', 'amazon', 'S01'])  // E:\videos\anime\pokemon\amazon\S01



        let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])
        // remove space
        for (let ttml of ttml2s) {
            let { base,dir,ext,name,root} = path.parse(ttml)
            let withoutSpace = base.replace(/\s/g, '')
            if (withoutSpace != base) {
                let newname = path.join(dir, withoutSpace)
                fs.renameSync( ttml, newname )
            }
        }
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])


        for (let ttml of ttml2s) {

            let match= ttml.match(/(\d+)\./)
            if (match == null) {
                //throw `name not correct. ${ttml}`
                continue
            }
            let nth = match[1]

            let mlseason = this.libs.files.season(ttml)
            if (mlseason == null) {
                throw 'no season on ttml2'
            }

            for (let kv of kvs) {

                let match2 = kv.match(/E(\d+) - Amazon/)
                if (match2 == null) {
                    //throw `name not correct. ${m4}`
                    continue
                }
                let nth2 = match2[1]

                let kvseason = this.libs.files.season(kv)
                if (kvseason == null) {
                    throw 'no season on kv'
                }

                if (mlseason != kvseason) {
                    continue
                }

                if (Number(nth) == Number(nth2)) {

                    //ttml
                    let { base,dir,ext,name,root} = path.parse(ttml)
                    let { base:base2,dir:dir2,ext:ext2,name:name2,root:root2} = path.parse(kv)

                    let newname = `${name}.mkv`
                    let newpath = path.join(dir2, newname)

                    fs.renameSync( kv, newpath )

                    continue
                }

            }

        }

        return 'ok.'
    }

}




























/*

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon'])


*/