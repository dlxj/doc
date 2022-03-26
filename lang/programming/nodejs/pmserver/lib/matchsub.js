
let fs = require('fs')
let path = require('path')

module.exports = {

    matchsub:function(rootssa, rootttml2) {

        let aa = this

        let ssas = this.libs.files.allfiles(rootssa, 'ssa')

        let ttml2s = this.libs.files.allfiles(rootttml2, 'ttml2')
        // remove space
        for (let ttml of ttml2s) {
            let { base,dir,ext,name,root} = path.parse(ttml)
            let withoutSpace = base.replace(/\s/g, '')
            if (withoutSpace != base) {
                let newname = path.join(dir, withoutSpace)
                fs.renameSync( ttml, newname )
            }
        }

        ttml2s = this.libs.files.allfiles(rootttml2, 'ttml2')
        for (let ttml of ttml2s) {

            let match= ttml.match(/(\d+)\./)
            if (match == null) {
                throw `name not correct. ${ttml}`
            }
            let nth = match[1]

            for (let ssa of ssas) {

                let match2 = ssa.match(/\](\d+)\.chs/)
                if (match == null) {
                    throw `name not correct. ${ssa}`
                }
                let nth2 = match2[1]

                if (Number(nth) == Number(nth2)) {

                    let { base,dir,ext,name,root} = path.parse(ttml)
                    let { base:base2,dir:dir2,ext:ext2,name:name2,root:root2} = path.parse(ssa)

                    let newname = `${name}.ssa`
                    let newpath = path.join(dir2, newname)

                    fs.renameSync( ssa, newpath )
                }

            }

        }

        return 'ok.'
    }

}




























/*

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon'])


*/