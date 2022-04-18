
/*

对于小规模样本集（几万量级），常用的分配比例是60% 训练集、20% 验证集、20% 测试集。 对于大规模样本集（百万级以上），只要验证集和测试集的数量足够即可，例如有100w 条数据，那么留1w 验证集，1w 测试集即可。 1000w 的数据，同样留1w 验证集和1w 测试集。

*/

let path = require('path')
let fs = require('fs')
let _ = require("lodash")
let subtitleSteams = global.config.subtitleSteams
let root_corpus = global.config.root_corpus[process.platform]

module.exports = {
    name: 'opennmt',
    remark: '',
    params: {
    },
    async handler({}) {

        let mkvs = this.libs.files.allfiles(global.animes.root, 'mkv', ['pokemon_c2club', 'S14', 'Best_Wishes'])

        let names = {}
        for (let vdpath of mkvs) {
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)
            if ( !( name in names ) ) {
                names[name] = name
            }
        }

        let jps = []
        let chss = []

        for (let j = 0; j < 1; j++) {  // mkvs.length

            let vdpath = mkvs[j]
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)

            if ( !(name in subtitleSteams) ) {
                throw `error: name '${name}' not in config.subtitleSteams!`
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

            console.log(`# begin gen jp_cht data for opennmt...`)
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

                let { spaced:spacedjp } = hiras
                spacedjp = spacedjp.replace(/\（.+?\）/g, '').replace(/(\(.+?\))/g, ' ')

                let { spaced:spacedzh } = await this.libs.jieba.spaced(zh)

                jps.push(spacedjp)
                chss.push(spacedzh)

                console.log(`${i + 1}/${subtitles2.length} subs | ${j + 1} / ${mkvs.length} mkvs ${name}`)   
                
            }

        }

        // pick 60% for train, 20% for valiate, 20% for test
        let arr = []
        for (let i = 0; i < jps.length; i++) {
            arr.push( { jp:jps[i], chs:chss[i] } )
        }

        arr = _.shuffle(arr)

        // require('fs').writeFileSync(path.join(root_corpus, 'src-train.txt'), jps.join('\n'), {encoding:'utf-8'} )
        // require('fs').writeFileSync(path.join(root_corpus, 'tgt-train.txt'), chss.join('\n'), {encoding:'utf-8'} )
        
        // require('fs').writeFileSync('src-val.txt', ens2, {encoding:'utf-8'} )
        // require('fs').writeFileSync('tgt-val.txt', chts2, {encoding:'utf-8'} )
    
        // require('fs').writeFileSync('src-test.txt', ens3, {encoding:'utf-8'} )
        // require('fs').writeFileSync('tgt-test.txt', chts3, {encoding:'utf-8'} )

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