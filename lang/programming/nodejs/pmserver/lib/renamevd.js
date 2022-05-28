
let fs = require('fs')
let path = require('path')
let _ = require('lodash')

module.exports = {

    renamevd: function () {

        let aa = this

        //let m4s = this.libs.files.allfiles(rootvd, 'mp4')

        //let kvs = this.libs.files.allfiles(rootvd, 'mkv', ['amazon', 'pokemon'])

        let platform = process.platform
        let root_vd = global.config.root_vd[platform]

        let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon', 'amazon', 'S01'])  // E:\videos\anime\pokemon\amazon\S01

        let m4s = this.libs.files.allfiles(root_vd, 'mp4', ['pokemon_tw', 'S01'])


        let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])
        // remove space
        for (let ttml of ttml2s) {
            let { base, dir, ext, name, root } = path.parse(ttml)
            let withoutSpace = base.replace(/\s/g, '')
            if (withoutSpace != base) {
                let newname = path.join(dir, withoutSpace)
                fs.renameSync(ttml, newname)
            }
        }
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])


        for (let ttml of ttml2s) {

            let match = ttml.match(/(\d+)\./)
            if (match == null) {
                //throw `name not correct. ${ttml}`
                continue
            }
            let nth = match[1]

            let mlseason = this.libs.files.season(ttml)
            if (mlseason == null) {
                throw 'no season on ttml2'
            }

            for (let kv of kvs) {

                let match2 = kv.match(/E(\d+) - Amazon/)
                if (match2 == null) {
                    //throw `name not correct. ${m4}`
                    continue
                }
                let nth2 = match2[1]

                let kvseason = this.libs.files.season(kv)
                if (kvseason == null) {
                    throw 'no season on kv'
                }

                if (mlseason != kvseason) {
                    continue
                }

                if (Number(nth) == Number(nth2)) {

                    //ttml
                    let { base, dir, ext, name, root } = path.parse(ttml)
                    let { base: base2, dir: dir2, ext: ext2, name: name2, root: root2 } = path.parse(kv)

                    let newname = `${name}.mkv`
                    let newpath = path.join(dir2, newname)

                    fs.renameSync(kv, newpath)

                    continue
                }

            }

            for (let m4 of m4s) {

                let match3 = m4.match(/(\d+)\_/)
                if (match3 == null) {
                    //throw `name not correct. ${m4}`
                    continue
                }
                let nth3 = match3[1]

                let m4season = this.libs.files.season(m4)
                if (m4season == null) {
                    throw 'no season on kv'
                }

                if (mlseason != m4season) {
                    continue
                }

                if (m4season == 'S01' && Number(nth3) >= 38) {
                    nth3 = Number(nth3) + 1
                }

                if (Number(nth) == Number(nth3)) {

                    //ttml
                    let { base, dir, ext, name, root } = path.parse(ttml)
                    let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(m4)

                    let newname = `${name}.mp4`
                    let newpath = path.join(dir3, newname)

                    fs.renameSync(m4, newpath)
                }

            }

        }

        rename_season3()

        rename_season6()

        return 'ok.'
    }

}


function rename_season3() {
    // S01包含了S02
    let platform = process.platform
    let root_vd = global.config.root_vd[platform]

    let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon', 'amazon', 'S03'])  // E:\videos\anime\pokemon\amazon\S01

    let m4s = this.libs.files.allfiles(root_vd, 'mp4', ['pokemon_tw', 'S03'])

    let lvs = this.libs.files.allfiles(root_vd, 'flv', ['pokemon_tw', 'S03'])

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S03'])
    // remove space
    for (let ttml of ttml2s) {
        let { base, dir, ext, name, root } = path.parse(ttml)
        let withoutSpace = base.replace(/\s/g, '')
        if (withoutSpace != base) {
            let newname = path.join(dir, withoutSpace)
            fs.renameSync(ttml, newname)
        }
    }
    ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S03'])

    function sort(ttml) {
        let match = ttml.match(/(\d+)\./)
        if (match == null) {
            throw `name not correct. ${ttml}`
        }
        let nth = match[1]
        return Number(nth)
    }

    ttml2s = _.orderBy(ttml2s, [
        function (item) { return sort(item); }
    ], ["asc"])

    for (let ttml of ttml2s) {

        let match = ttml.match(/(\d+)\./)
        if (match == null) {
            //throw `name not correct. ${ttml}`
            continue
        }
        let nth = match[1]

        let mlseason = this.libs.files.season(ttml)
        if (mlseason == null) {
            throw 'no season on ttml2'
        }

        for (let kv of kvs) {

            let match2 = kv.match(/E(\d+) - Amazon/)
            if (match2 == null) {
                //throw `name not correct. ${m4}`
                continue
            }
            let nth2 = match2[1]

            let kvseason = this.libs.files.season(kv)
            if (kvseason == null) {
                throw 'no season on kv'
            }

            if (mlseason != kvseason) {
                continue
            }

            if (Number(nth) == Number(nth2)) {

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base2, dir: dir2, ext: ext2, name: name2, root: root2 } = path.parse(kv)

                let newname = `${name}.mkv`
                let newpath = path.join(dir2, newname)

                fs.renameSync(kv, newpath)

                continue
            }

        }

        // 190 之前是mp4
        for (let m4 of m4s) {

            let match3 = m4.match(/(\d+)\_/)
            if (match3 == null) {
                //throw `name not correct. ${m4}`
                continue
            }
            let nth3 = match3[1]

            let m4season = this.libs.files.season(m4)
            if (m4season == null) {
                throw 'no season on kv'
            }

            if (mlseason != m4season) {
                continue
            }

            // if (m4season == 'S01' && Number(nth3) >= 38) {
            //     nth3 = Number(nth3) + 1
            // }

            if (Number(nth) <= 62 && Number(nth) == Number(nth3) - 117) {

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(m4)

                let newname = `${name}.mp4`
                let newpath = path.join(dir3, newname)

                fs.renameSync(m4, newpath)
            } else if (Number(nth) >= 66 && Number(nth) == Number(nth3) - 114) {  // 63.ミュウツー！我ハココニ在リ(1) 到 65  台版无

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(m4)

                let newname = `${name}.mp4`
                let newpath = path.join(dir3, newname)

                fs.renameSync(m4, newpath)
            }

        }

        // 191 之后是flv
        for (let lv of lvs) {

            let match3 = lv.match(/(\d+)\_/)
            if (match3 == null) {
                //throw `name not correct. ${m4}`
                continue
            }
            let nth3 = match3[1]

            let lvseason = this.libs.files.season(lv)
            if (lvseason == null) {
                throw 'no season on kv'
            }

            if (mlseason != lvseason) {
                continue
            }

            // if (m4season == 'S01' && Number(nth3) >= 38) {
            //     nth3 = Number(nth3) + 1
            // }

            // if (Number(nth) <= 63 && Number(nth) <= 65) {
            //     let a = 1
            // }

            if (Number(nth) <= 62 && Number(nth) == Number(nth3) - 117) {  // 63.ミュウツー！我ハココニ在リ(1) 到 65  台版无

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(lv)

                let newname = `${name}.flv`
                let newpath = path.join(dir3, newname)

                fs.renameSync(lv, newpath)
            } else if (Number(nth) >= 66 && Number(nth) == Number(nth3) - 114) {  // 63.ミュウツー！我ハココニ在リ(1) 到 65  台版无
                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(lv)

                let newname = `${name}.flv`
                let newpath = path.join(dir3, newname)

                fs.renameSync(lv, newpath)
            }

        }

    }

    return 'ok.'
}


function rename_season6() {

    let platform = process.platform
    let root_vd = global.config.root_vd[platform]

    let kvs = this.libs.files.allfiles(root_vd, 'mkv', ['pokemon', 'amazon', 'S06'])  // E:\videos\anime\pokemon\amazon\S01

    let lvs = this.libs.files.allfiles(root_vd, 'flv', ['pokemon_tw', 'S06'])

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S06'])
    // remove space
    for (let ttml of ttml2s) {
        let { base, dir, ext, name, root } = path.parse(ttml)
        let withoutSpace = base.replace(/\s/g, '')
        if (withoutSpace != base) {
            let newname = path.join(dir, withoutSpace)
            fs.renameSync(ttml, newname)
        }
    }
    ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S06'])

    function sort(ttml) {
        let match = ttml.match(/(\d+)\./)
        if (match == null) {
            throw `name not correct. ${ttml}`
        }
        let nth = match[1]
        return Number(nth)
    }

    ttml2s = _.orderBy(ttml2s, [
        function (item) { return sort(item); }
    ], ["asc"])

    for (let ttml of ttml2s) {

        let match = ttml.match(/(\d+)\./)
        if (match == null) {
            //throw `name not correct. ${ttml}`
            continue
        }
        let nth = match[1]

        let mlseason = this.libs.files.season(ttml)
        if (mlseason == null) {
            throw 'no season on ttml2'
        }

        for (let kv of kvs) {

            let match2 = kv.match(/E(\d+) - Amazon/)
            if (match2 == null) {
                //throw `name not correct. ${m4}`
                continue
            }
            let nth2 = match2[1]

            let kvseason = this.libs.files.season(kv)
            if (kvseason == null) {
                throw 'no season on kv'
            }

            if (mlseason != kvseason) {
                continue
            }

            if (Number(nth) == Number(nth2)) {

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base2, dir: dir2, ext: ext2, name: name2, root: root2 } = path.parse(kv)

                let newname = `${name}.mkv`
                let newpath = path.join(dir2, newname)

                fs.renameSync(kv, newpath)

                continue
            }

        }

        for (let lv of lvs) {

            let match3 = lv.match(/(\d+)\./)
            if (match3 == null) {
                //throw `name not correct. ${m4}`
                continue
            }
            let nth3 = match3[1]

            let lvseason = this.libs.files.season(lv)
            if (lvseason == null) {
                throw 'no season on kv'
            }

            if (mlseason != lvseason) {
                continue
            }

            if (Number(nth) <= 119 && Number(nth) == Number(nth3)) {  // 120 原版是总集编，台版没有。 台120 对应原121

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(lv)

                let newname = `${name}.flv`
                let newpath = path.join(dir3, newname)

                fs.renameSync(lv, newpath)

                break

            }

            
            if (Number(nth) >= 121 && Number(nth) == Number(nth3) +1 ) {  // 120 原版是总集编，台版没有。 台120 对应原121

                //ttml
                let { base, dir, ext, name, root } = path.parse(ttml)
                let { base: base3, dir: dir3, ext: ext3, name: name3, root: root3 } = path.parse(lv)

                let newname = `${name}.flv`
                let newpath = path.join(dir3, newname)

                fs.renameSync(lv, newpath)

                break

            }


        }

    }

    return 'ok.'
}























/*

    let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon'])


*/