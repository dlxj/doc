
let fs = require('fs')

module.exports = {

    renamevd:function(rootvd, rootttml2) {

        let aa = this

        let m4s = this.libs.files.allfiles(rootvd, 'mp4')
        let ttml2s = this.libs.files.allfiles(rootttml2, 'ttml2')

        return 'ok.'
    }

}




























/*

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon'])


*/