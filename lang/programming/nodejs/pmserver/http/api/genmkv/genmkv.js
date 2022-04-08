
let path = require('path')
let fs = require('fs')

module.exports = {
    name: 'genmkv',
    remark: '',
    params: {
        type: {
            type: 'enum',
            range:["anime","drama"],
            remark: '',
            default:'anime'
        }
    },
    async handler({type}) {

        let platform = process.platform
        let root_vd = global.config.root_vd[platform]

        let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon', 'amazon', 'S01'])  // E:\videos\anime\pokemon\amazon\S01

        let srts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S01'])  // amazon\pokemon

        for (let kvpath of kvs) {

            let { base:kvbase, dir:kvdir, ext:kvext, name:kvname, root:kvroot } = path.parse(kvpath)

            let kvseason = this.libs.files.season(kvpath)
            if (kvseason == null) {
                throw 'no season on vd'
            }

            for (let rtpath of srts) {

                let { base:rtbase, dir:rtdir, ext:rtext, name:rtname, root:rtroot } = path.parse(rtpath)
    
                let rtseason = this.libs.files.season(rtpath)
                if (rtseason == null) {
                    throw 'no season on vd'
                }
                
                if ( kvname == rtname ) {

                    
                    break

                }
    
            }
        }

        return this.msg(200, srts)
    }
}
