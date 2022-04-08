
let path = require('path')
let fs = require('fs')

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
    async handler({type}) {

        let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])

        let ssas = this.libs.files.allfiles(global.root_subtitles, 'ssa', ['amazon', 'pokemon', 'ssa', 'S01'])

        //D:\GitHub\doc\lang\Japanese\anime\sutitles\anime\amazon\pokemon\ssa\S01

        let srts = []

        for (let mlpath of ttml2s) {

            let { base, dir, ext, name, root } = path.parse(mlpath)

            let season = ''
            let match = mlpath.match(/[\\\/](S\d\d)[\\\/]/)
            if (match == null) {
                throw 'no season on subtitle path'
            }
            season = match[1]
    
            let dir_up = require('path').resolve(dir, '..', '..')
            let dir_srt = path.join(dir_up, 'srt', season, 'jp')
            if ( !fs.existsSync( dir_srt ) ) {
                fs.mkdirSync(dir_srt, { recursive: true })
            }
            let srtpath = path.join(dir_srt, `${name}.srt`)
    
            let srt = this.libs.ttml2.extractSrt({mlpath})
            require('fs').writeFileSync( srtpath, srt, {encoding:'utf8'})

            srts.push(srt)

        }

        return this.msg(200, srts)
    }
}
