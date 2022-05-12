
let path = require('path')
let fs = require('fs')

module.exports = {
    name: 'genmkv',
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

        let platform = process.platform
        let root_vd = global.config.root_vd[platform]

        let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon_amazon', 'S01'])  // E:\videos\anime\pokemon\amazon\S01

        let m4s = this.libs.files.allfiles(root_vd, 'mp4', ['pokemon_tw', 'S01']) 

        let srts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S01', 'jp'])

        for (let kvpath of kvs) {

            let { base:kvbase, dir:kvdir, ext:kvext, name:kvname, root:kvroot } = path.parse(kvpath)

            let kvseason = this.libs.files.season(kvpath)
            if (kvseason == null) {
                throw 'no season on vd'
            }

            for (let rtpath of srts) {

                let { base:rtbase, dir:rtdir, ext:rtext, name:rtname, root:rtroot } = path.parse(rtpath)
    
                let rtseason = this.libs.files.season(rtpath)
                if (rtseason == null) {
                    throw 'no season on rt'
                }

                if (kvseason != rtseason) {
                    continue
                }
                
                if ( kvname == rtname ) {

                    for (let m4path of m4s) {

                        let { base:m4base, dir:m4dir, ext:m4ext, name:m4name, root:m4root } = path.parse(m4path)

                        let m4season = this.libs.files.season(m4path)
                        if (m4season == null) {
                            throw 'no season on m4'
                        }

                        if (m4season != rtseason) {
                            continue
                        }

                        if ( m4name == rtname ) {

                            let outdir = path.join(m4dir, 'output')
                            if (!fs.existsSync(outdir)) {
                                fs.mkdirSync(outdir, { recursive: false })
                            }

                            let outpath = path.join(outdir, `${rtname}.mkv`)
                            let { msg } = await this.libs.ffmpeg.merge_pokemonAmazon_pokemonTW(m4path, kvpath, rtpath, outpath)


                            break

                        }

                    }


                    break
                }
    
            }
        }

        await genkv_season3(type)


        return this.msg(200, 'ok.')
    }
}

async function genkv_season3(type) {
    // S01 包含了S02
    let platform = process.platform
    let root_vd = global.config.root_vd[platform]

    let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon_amazon', 'S03'])  // E:\videos\anime\pokemon\amazon\S01

    let m4s = this.libs.files.allfiles(root_vd, 'mp4', ['pokemon_tw', 'S03']) 

    let srts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S03', 'jp'])

    for (let kvpath of kvs) {

        let { base:kvbase, dir:kvdir, ext:kvext, name:kvname, root:kvroot } = path.parse(kvpath)

        let kvseason = this.libs.files.season(kvpath)
        if (kvseason == null) {
            throw 'no season on vd'
        }

        for (let rtpath of srts) {

            let { base:rtbase, dir:rtdir, ext:rtext, name:rtname, root:rtroot } = path.parse(rtpath)

            let rtseason = this.libs.files.season(rtpath)
            if (rtseason == null) {
                throw 'no season on rt'
            }

            if (kvseason != rtseason) {
                continue
            }
            
            if ( kvname == rtname ) {

                for (let m4path of m4s) {

                    let { base:m4base, dir:m4dir, ext:m4ext, name:m4name, root:m4root } = path.parse(m4path)

                    let m4season = this.libs.files.season(m4path)
                    if (m4season == null) {
                        throw 'no season on m4'
                    }

                    if (m4season != rtseason) {
                        continue
                    }

                    if ( m4name == rtname ) {

                        let outdir = path.join(m4dir, 'output')
                        if (!fs.existsSync(outdir)) {
                            fs.mkdirSync(outdir, { recursive: false })
                        }

                        let outpath = path.join(outdir, `${rtname}.mkv`)
                        let { msg } = await this.libs.ffmpeg.merge_pokemonAmazon_pokemonTW(m4path, kvpath, rtpath, outpath)


                        break

                    }

                }


                break
            }

        }
    }


}
