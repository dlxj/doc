
let path = require('path')
let fs = require('fs')
let subtitleSteams = global.config.subtitleSteams

module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({}) {

        // drop and create db, then create table
        let type = 'anime'
        let re = await this.dbs.defaultDB.dropdatabase.query({'dbname': type})
        re = await this.dbs.defaultDB.createdatabase.query({'dbname':type})
        re = await this.dbs.anime.createtable.query({'tablename': type})

        let mkvs = this.libs.files.allmkv(global.animes.root, type)

        let names = {}
        for (let vdpath of mkvs) {
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)
            if ( !( name in names ) ) {
                names[name] = name
                //re = await this.dbs.anime.createtable.query({'tablename':name}) // create table, this is separate table, cancel now
            }
        }

        for (let j = 0; j < mkvs.length; j++) {

            let vdpath = mkvs[j]
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)

            if ( !(name in subtitleSteams) ) {
                throw `error: name '${name}' not in config.subtitleSteams!`
            }

            let audio_dir = path.join(global.animes.root_audio, name, seasion)
            if ( ! fs.existsSync( audio_dir ) ) {
                fs.mkdirSync(audio_dir, { recursive: true })
            }

            let subsjp = []
            let subszh = []

            let nths = subtitleSteams[name]
            for (let nth of nths) {
                let { srt, msg } = await this.libs.ffmpeg.extractSubtitle(vdpath, 'srt', nth)
                if (srt == null) {
                    console.log(`Warning: srt_jp is null\nmsg: ${msg}`)
                    continue
                }
                srt = this.libs.srt.clean(srt)
    
                let subtitles = this.libs.srt.parse(srt)  // jp ch all in one srt, and have the same time
    
    
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
            }


            let subtitles2 = this.libs.srt.merge(subsjp, subszh)

            console.log(`# begin insert...`)
            for (let i = 0; i < subtitles2.length; i++) {  // 

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

                let re = await this.dbs.anime.insert.query({tablename:type, name, seasion, jp, zh, type, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionname, endtime, audio, video})
                
                let { tableID } = re.fields[0]

                let audio_path = path.join(audio_dir, `${tableID}.mp3`)

                fs.writeFileSync(audio_path, audio )

                console.log(`${i + 1}/${subtitles2.length} subs | ${j + 1} / ${mkvs.length} mkvs ${name}`)   
                
                

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


/*

ffmpeg -i "E:\videos\anime\pokemon\S14\Best_Wishes\1.mkv" -y -map 0:s:0 -f srt pipe:1
ffmpeg -i "/mnt/videos/anime/pokemon/S14/Best_Wishes/1.mkv" -y -map 0:s:0 -f srt pipe:1

*/