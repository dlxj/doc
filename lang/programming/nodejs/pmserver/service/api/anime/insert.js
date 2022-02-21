module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({ }) {

        //let name = 'danganronpa'
        // let seasion = 'S01'
        // let seasionName = ''

        let obj = this

        let re = await this.dbs.defaultDB.dropdatabase.query({'dbname': 'anime'})
        re = await this.dbs.defaultDB.createdatabase.query({'dbname':'anime'})
        // re = await this.dbs.anime.createtable.query({'tablename':name})

        //let mkvs = this.libs.files.allmkv(global.animes.root, name)
        let mkvs = this.libs.files.allmkv(global.animes.root)


        let animenames = {}
        for (let vdpath of mkvs) {
            let { animename, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)
            if ( !( animename in animenames ) ) {
                animenames[animename] = animename
                re = await this.dbs.anime.createtable.query({'tablename':animename})
            }
        }

        for (let j = 0; j < mkvs.length; j++) {

            let vdpath = mkvs[j]
            let { animename, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)
            let name = animename

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
                let jp = item.jp.trim()
                let zh = item.zh.trim()

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

                let re = await this.dbs.anime.insert.query({name, seasion, jp, zh, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionname, endtime, audio, video})
            
                console.log(`${i + 1}/${subtitles2.length} subs ｜ ${j + 1} / ${mkvs.length} mkvs ${name}`)   
                
                

            }

        }

        console.log('all taske done.')

        return 'all taske done.'

    }
}

/*


//let { hiras, msg }= await this.libs.mecab.haras('騙して勝つ')
// let { hiras, msg }= await this.libs.mecab.haras("お願いします! ピカピカ! ")  // crash

SELECT Max(ID) FROM danganronpa;
SELECT p."id", p.jp_ruby, p.zh, p.v_jp, p.v_zh, p.seasion, p."name" FROM danganronpa p WHERE ID IN (1, 3);

*/
