

let path = require('path')
let fs = require('fs')

module.exports = {
    name: 'renamevd',
    remark: '',
    params: {
        rootvd: {
            type: 'string',
            remark: '',
            default:''
        },
        rootttml2: {
            type: 'string',
            remark: '',
            default:''
        },
    },
    async handler({rootvd, rootttml2}) {

        let re = this.libs.renamevd.renamevd(rootvd, rootttml2)

        return this.msg(200, re)
    }
}

/*

D:\GitHub\doc\lang\Japanese\anime\sutitles\anime\amazon\pokemon\S01\ttml2

*/

