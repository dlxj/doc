module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({ }) {



        let obj = this

        let mkvs = this.libs.files.allmkv(global.animes.root, 'Danganronpa')
        for (let j = 0; j < mkvs.length; j++) {

            let vdpath = mkvs[j]
            let { videoname, episode } = this.libs.vdinfo.episode(vdpath)
            //let { srt: srt_jp, msg: msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream

            let { srt: srt_jp, msg: msg_jp } = await this.libs.ffmpeg.extractSubtitle(vdpath, 'srt', 0)
            if (srt_jp == null) {
                console.log(`Warning: srt_jp is null\nmsg: ${msg_jp}`)
                continue
            }
            srt_jp = this.libs.srt.clean(srt_jp)

            let subtitles = this.libs.srt.parse(srt_jp)  // jp ch all in one srt, and have the same time

            let subsjp = []
            let subszh = []


            for (let i = 0; i < subtitles.length; i++) {
                let item = subtitles[i]
                let subtitle = item.subtitle
                if ( subtitle.trim() == '' ) {
                    continue
                }
                if ( this.libs.mecab.isJP(subtitle) ) {
                    subsjp.push( item )
                }  else {
                    subszh.push( item )
                }
            }

            let subtitles2 = this.libs.srt.merge(subsjp, subszh)


            let a = 1


        }

        //dbpaths.forEach((dbPath) => {

        let re = await this.dbs.defaultDB.drop.query({ 'dbname': 'danganronpa' })  // drop db
        re = await this.dbs.defaultDB.danganronpa.create.query({})              // create db
        re = await this.dbs.danganronpa.createtable.query({})                   // create table 

        //let re = await this.services.user.getuser( { userid:'0' } )

        // let re = await this.dbs.temp2.search.query({keywd})

        return 'hi from insert'

        // return 'hi from service.'

    }
}

/*

//let { hiras, msg }= await this.libs.mecab.haras('騙して勝つ')
        // let { hiras, msg }= await this.libs.mecab.haras("お願いします! ピカピカ! ")  // crash

*/
