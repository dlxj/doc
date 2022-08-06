
let path = require('path')
let fs = require('fs')
let _ = require('lodash')

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

        await genkv_season6(type)

        await genkv_season10(type)

        return this.msg(200, 'ok.')
    }
}

async function genkv_season3(type) {
    // S01 包含了S02
    let platform = process.platform
    let root_vd = global.config.root_vd[platform]

    function sort(ttml) {
        let match= ttml.match(/(\d+)\./)
        if (match == null) {
            throw `name not correct. ${ttml}`
        }
        let nth = match[1]
        return Number(nth)
    }

    let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon_amazon', 'S03'])  // E:\videos\anime\pokemon\amazon\S01

    let m4s = this.libs.files.allfiles(root_vd, 'mp4', ['pokemon_tw', 'S03']) 

    let lvs = this.libs.files.allfiles(root_vd, 'flv', ['pokemon_tw', 'S03']) 

    let srts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S03', 'jp'])

    kvs = _.orderBy(kvs, [
        function (item) { return sort(item); }
    ], ["asc"])

    m4s = _.orderBy(m4s, [
        function (item) { return sort(item); }
    ], ["asc"])

    lvs = _.orderBy(lvs, [
        function (item) { return sort(item); }
    ], ["asc"])

    srts = _.orderBy(srts, [
        function (item) { return sort(item); }
    ], ["asc"])

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

                for (let m4path of m4s) {  // S03 mp4 只到76 集，后面开始是是flv

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
                        let { msg } = await this.libs.ffmpeg.merge_pokemonAmazon_pokemonTWS03(m4path, kvpath, rtpath, outpath)

                        break

                    }

                }

                for (let lvpath of lvs) {  // S03 mp4 只到76 集，后面开始是是flv

                    let { base:lvbase, dir:lvdir, ext:lvext, name:lvname, root:lvroot } = path.parse(lvpath)

                    let lvseason = this.libs.files.season(lvpath)
                    if (lvseason == null) {
                        throw 'no season on lv'
                    }

                    if (lvseason != rtseason) {
                        continue
                    }

                    if ( lvname == rtname ) {

                        let outdir = path.join(lvdir, 'output')
                        if (!fs.existsSync(outdir)) {
                            fs.mkdirSync(outdir, { recursive: false })
                        }

                        let outpath = path.join(outdir, `${rtname}.mkv`)
                        let { msg } = await this.libs.ffmpeg.merge_pokemonAmazon_pokemonTWS03(lvpath, kvpath, rtpath, outpath)

                        break

                    }

                }
                break
            }

        }
    }


}

async function genkv_season6(type) {

    let platform = process.platform
    let root_vd = global.config.root_vd[platform]

    function sort(ttml) {
        let match= ttml.match(/(\d+)\./)
        if (match == null) {
            throw `name not correct. ${ttml}`
        }
        let nth = match[1]
        return Number(nth)
    }

    let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon_amazon', 'S06'])  // E:\videos\anime\pokemon\amazon\S01

    let lvs = this.libs.files.allfiles(root_vd, 'flv', ['pokemon_tw', 'S06']) 

    let srts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S06', 'jp'])

    kvs = _.orderBy(kvs, [
        function (item) { return sort(item); }
    ], ["asc"])

    lvs = _.orderBy(lvs, [
        function (item) { return sort(item); }
    ], ["asc"])

    srts = _.orderBy(srts, [
        function (item) { return sort(item); }
    ], ["asc"])

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

                for (let lvpath of lvs) {

                    let { base:lvbase, dir:lvdir, ext:lvext, name:lvname, root:lvroot } = path.parse(lvpath)

                    let lvseason = this.libs.files.season(lvpath)
                    if (lvseason == null) {
                        throw 'no season on lv'
                    }

                    if (lvseason != rtseason) {
                        continue
                    }

                    if ( lvname == rtname ) {

                        let outdir = path.join(lvdir, 'output')
                        if (!fs.existsSync(outdir)) {
                            fs.mkdirSync(outdir, { recursive: false })
                        }

                        let outpath = path.join(outdir, `${rtname}.mkv`)
                        let { msg } = await this.libs.ffmpeg.merge_pokemonAmazon_pokemonTWS06(lvpath, kvpath, rtpath, outpath)

                        break

                    }

                }
                break
            }

        }
    }


}

async function genkv_season10(type) {

    let platform = process.platform
    let root_vd = global.config.root_vd[platform]

    function sort(ttml) {
        let match= ttml.match(/(\d+)\./)
        if (match == null) {
            throw `name not correct. ${ttml}`
        }
        let nth = match[1]
        return Number(nth)
    }

    let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon_amazon', 'S10'])  // E:\videos\anime\pokemon\amazon\S01

    let m4s = this.libs.files.allfiles(root_vd, 'mp4', ['pokemon_tw', 'S10']) 

    let srts = this.libs.files.allfiles(global.root_subtitles, 'srt', ['amazon', 'pokemon', 'srt', 'S10', 'jp'])

    kvs = _.orderBy(kvs, [
        function (item) { return sort(item); }
    ], ["asc"])

    m4s = _.orderBy(m4s, [
        function (item) { return sort(item); }
    ], ["asc"])

    srts = _.orderBy(srts, [
        function (item) { return sort(item); }
    ], ["asc"])

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

                    let { base:lvbase, dir:m4dir, ext:lvext, name:m4name, root:lvroot } = path.parse(m4path)

                    let m4season = this.libs.files.season(m4path)
                    if (m4season == null) {
                        throw 'no season on lv'
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
                        let { msg } = await this.libs.ffmpeg.merge_pokemonAmazon_pokemonTWS10(m4path, kvpath, rtpath, outpath)

                        break

                    }

                }
                break
            }

        }
    }


}