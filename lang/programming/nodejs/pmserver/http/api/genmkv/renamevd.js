

let path = require('path')
let fs = require('fs')

module.exports = {
    name: 'renamevd',
    remark: '',
    params: {
        rootvd: {
            type: 'string',
            remark: ''
        },
        rootsrt: {
            type: 'string',
            remark: ''
        },
    },
    async handler({rootvd, rootsrt}) {

        let re = this.libs.renamevd.renamevd(rootvd, rootsrt)

        return this.msg(200, re)
    }
}

/*

D:\GitHub\doc\lang\Japanese\anime\sutitles\anime\amazon\pokemon\S01\ttml2

*/

