
// mkv srt jp chs sepera separated

let path = require('path')
let fs = require('fs')
let subtitleSteams = global.config.subtitleSteams

module.exports = {
    name: 'insertV2',
    remark: '',
    params: {
    },
    async handler({}) {

        // drop and create db, then create table
        let type = 'anime'
        let re = await this.dbs.defaultDB.dropdatabase.query({'dbname': type})
        re = await this.dbs.defaultDB.createdatabase.query({'dbname':type})
        re = await this.dbs.anime.createtable.query({'tablename': type})

        //let mkvs = this.libs.files.allmkv(global.animes.root, type)


        let platform = process.platform
        let root_vd = global.config.root_vd[platform]

        let mkvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon', 'amazon', 'S01'])

        for (let j = 0; j < mkvs.length; j++) {

            let vdpath = mkvs[j]
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)

            if ( !(name in subtitleSteams) ) {
                // throw `error: name '${name}' not in config.subtitleSteams!`
                console.log(`waning: name '${name}' not in config.subtitleSteams!`)
            }

            //let audio_dir = path.join(global.animes.root_audio, name, seasion)
            let audio_dir = path.join(global.animes.root_audio, type, name, seasion)

            if ( ! fs.existsSync( audio_dir ) ) {
                fs.mkdirSync(audio_dir, { recursive: true })
            }

            let subsjp = []
            let subszh = []

            if (subtitleSteams[name] != undefined) {

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
            } else {

            
                let { base:vdbase, dir:vddir, ext:vdext, name:vdname, root:vdroot } = path.parse(vdpath)

                let srtjps = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S01', 'jp'])  // amazon\pokemon

                let srtjp = ''
                for (let rtpath of srtjps) {

                    let { base:rtbase, dir:rtdir, ext:rtext, name:rtname, root:rtroot } = path.parse(rtpath)
        
                    let rtseason = this.libs.files.season(rtpath)
                    if (rtseason == null) {
                        throw 'no season on rt'
                    }

                    if (seasion != rtseason) {
                        continue
                    }
                    
                    if ( vdname == rtname ) {

                        srtjp = fs.readFileSync(rtpath, {encoding:'utf8'})

                        break
                    }

                }

                if (srtjp == '') {
                    throw `vd no srt jp subtile ${vdpath}`
                }

                srtjp = this.libs.srt.clean(srtjp)
        
                let subtitlesjp = this.libs.srt.parse(srtjp)  // jp ch all in one srt, and have the same time
    
                for (let i = 0; i < subtitlesjp.length; i++) {
                    let item = subtitlesjp[i]
                    let subtitlejp = item.subtitle
                    if (subtitlejp.trim() == '') {
                        continue
                    }
                    
                    subsjp.push(item)

                }


                // chs
                let srtchss = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S01', 'chs'])  // amazon\pokemon

                let srtchs = ''
                for (let rtpath of srtchss) {

                    let { base:rtbase, dir:rtdir, ext:rtext, name:rtname, root:rtroot } = path.parse(rtpath)
        
                    let rtseason = this.libs.files.season(rtpath)
                    if (rtseason == null) {
                        throw 'no season on rt'
                    }

                    if (seasion != rtseason) {
                        continue
                    }
                    
                    if ( vdname == rtname ) {

                        srtchs = fs.readFileSync(rtpath, {encoding:'utf8'})

                        break
                    }

                }

                if (srtchs == '') {
                    console.log( `Warning: vd no srt chs subtile ${vdpath}` )
                    continue
                }

                srtchs = this.libs.srt.clean(srtchs)
        
                let subtitleschs = this.libs.srt.parse(srtchs)  // jp ch all in one srt, and have the same time
    
                for (let i = 0; i < subtitleschs.length; i++) {
                    let item = subtitleschs[i]
                    let subtitlechs = item.subtitle
                    if (subtitlechs.trim() == '') {
                        continue
                    }
                    
                    subszh.push(item)

                }


                let a = 1

            }



            


            let subtitles2 = this.libs.srt.mergev2(subsjp, subszh)

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

                //fs.writeFileSync(path.join(audio_dir, `${jp}.mp3`), audio )
            
                //fs.writeFileSync('./tmp.mp3', audio )
        
                let video = Buffer.from('')  // empty now

                let re = await this.dbs.anime.insert.query({tablename:type, name, seasion, jp, zh, type, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionname, endtime, audio, video})
                
                let { id } = re.rows[0]

                //let audio_path = path.join(audio_dir, `${id}.mp3`)
                let audio_path = path.join(audio_dir, `${id}.mp3`)
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


re = await tempDB.query("create extension pgroonga;")
re = await tempDB.query("create extension pg_jieba;")
re = await tempDB.query("CREATE INDEX pgroonga_jp_index ON pokemon USING pgroonga (jp);")
re = await tempDB.query("CREATE INDEX pgroonga_jpmecab_index ON pokemon USING pgroonga (jp_mecab);")
re = await tempDB.query("CREATE INDEX animename_index ON pokemon (name);")
re = await tempDB.query("CREATE INDEX episode_index ON pokemon (episode);")  // nth ji

*/