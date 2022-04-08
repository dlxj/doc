

let path = require('path')
let fs = require('fs')

module.exports = {
    name: 'matchsub',
    remark: '',
    params: {
        rootssa: {
            type: 'string',
            remark: ''
        },
        rootttml2: {
            type: 'string',
            remark: ''
        },
    },
    async handler({rootssa, rootttml2}) {

        let rts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S01'])

        let re = this.libs.matchsub.matchsub(rootssa, rootttml2)

        return this.msg(200, re)
    }
}

/*

D:\GitHub\doc\lang\Japanese\anime\sutitles\anime\amazon\pokemon\S01\ttml2

*/

