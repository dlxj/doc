
let path = require('path')

module.exports = {
    name: 'gensrt',
    remark: '',
    params: {
        type: {
            type: 'enum',
            range:["anime","drama"],
            remark: '',
            default:'anime'
        }
    },
    async handler({ type }) {

        let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', 'amazon')

        let mlpath = ttml2s[0]
        let { base,dir,ext,name,root} = path.parse(mlpath)
        let strPath = path.join( dir, `${name}.srt` )

        let srt = this.libs.ttml2.extractSrt({mlpath})
        require('fs').writeFileSync( path.join(__dirname, 'tmp.srt'), srt, {encoding:'utf8'})

        return this.msg(200, srt)
    }
}

/*



*/
