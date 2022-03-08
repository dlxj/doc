
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

        let srt = this.libs.ttml2.extractSrt(ttml2s[0])

        // let { srt, msg } = await this.libs.ffmpeg.extractSubtitle(vdpath, 'srt', nth)

        //let re = await this.services.search( { keywd, type } )

        return this.msg(200, ttml2s)
    }
}

/*



*/
