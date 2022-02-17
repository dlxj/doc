module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({ }) {

        let name = 'danganronpa'
        let seasion = 'S01'
        let seasionName = ''

        let obj = this

        let re = await this.dbs.defaultDB.dropdatabase.query({'dbname': name})
        re = await this.dbs.defaultDB.createdatabase.query({'dbname':name})
        re = await this.dbs.danganronpa.createtable.query({})

        let mkvs = this.libs.files.allmkv(global.animes.root, name)
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
                if (subtitle.trim() == '') {
                    continue
                }
                if (this.libs.mecab.isJP(subtitle)) {
                    subsjp.push(item)
                } else {
                    subszh.push(item)
                }
            }

            let subtitles2 = this.libs.srt.merge(subsjp, subszh)


            console.log(`# begin insert...`)
            for (let i = 0; i < subtitles2.length; i++) {  // subtitles.length;

                let item = subtitles2[i]

                let begintime = item.begintime.replace(',', '.')  // for ffmpeg
                let endtime = item.endtime.replace(',', '.')
                let jp = item.jp
                let zh = item.zh

                let { hiras, msg } = await this.libs.mecab.hiras(jp)
                if (hiras == null) {
                    throw `Error: segment fail. ${msg}`
                }


                let jp_ruby = hiras.ruby
                let hiragana = hiras.hiragana

                let hiragana_ng = this.libs.srt.NG(hiragana)
                let jp_ng = this.libs.srt.NG(jp)
                let zh_ng = this.libs.srt.NG(zh)

                jp_ng = (jp_ng.concat(hiragana_ng)).join(' ')  // for fulltext search All in one
                zh_ng = zh_ng.join(' ')
                hiragana_ng = hiragana_ng.join(' ')

                let { au: audio } = await this.libs.ffmpeg.extractAudio(vdpath, 'mp3', begintime, endtime)
                if (audio == null) {
                    throw `au is null. ${vdpath} ${begintime}`
                }
            
                //fs.writeFileSync('./tmp.mp3', audio )
        
                let video = Buffer.from('')  // empty now

                let re = await this.dbs.danganronpa.insert.query({name, seasion, jp, zh, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionName, endtime, audio, video})










                // re = await tempDB.query(`
                // INSERT INTO pokemon (name, seasion, jp, zh, begintime, jp_ruby, v_jp, v_zh, videoname, episode, seasionName, endtime, audio, video)
                // VALUES
                //  ( $1, $2, $3, $4, $5, $6, to_tsvector($7), to_tsvector($8), $9, $10, $11, $12, $13, $14 );
                //  `, [name, seasion, jp, zh, begintime, ruby, jp_ng, zh_ng, videoname, episode, seasionName, endtime, audio, video])
            
            
                    // re = await tempDB.query(`SELECT audio FROM pokemon limit 1;`)
                    // let au = re.rows[0].audio  //  Uint8Array
                    // au = Buffer.from(au)
            
                console.log(`${i + 1}/${subtitles.length} subs ｜ ${j + 1} / ${mkvs.length} mkvs `)
            

                let a = 1
            }

            let a = 1


        }

        //dbpaths.forEach((dbPath) => {

        re = await this.dbs.defaultDB.drop.query({ 'dbname': 'danganronpa' })  // drop db
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
