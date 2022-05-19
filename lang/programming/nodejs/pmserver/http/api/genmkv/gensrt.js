
let path = require('path')
let fs = require('fs')

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
    async handler({type}) {

        let ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])  // 第一季实际上是 01~02 共两季
        // remove space
        for (let ttml of ttml2s) {
            let { base,dir,ext,name,root} = path.parse(ttml)
            let withoutSpace = base.replace(/\s/g, '')
            if (withoutSpace != base) {
                let newname = path.join(dir, withoutSpace)
                fs.renameSync( ttml, newname )
            }
        }
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S01'])

        let ssas = this.libs.files.allfiles(global.root_subtitles, 'ssa', ['amazon', 'pokemon', 'ssa', 'S01'])

        let asss = this.libs.files.allfiles(global.root_subtitles, 'ass', ['amazon', 'pokemon', 'ass', 'S01'])

        ssas = ssas.concat(asss)

        let jps = []

        for (let mlpath of ttml2s) {

            let { base, dir, ext, name, root } = path.parse(mlpath)

            let season = ''
            let match = mlpath.match(/[\\\/](S\d\d)[\\\/]/)
            if (match == null) {
                throw 'no season on subtitle path'
            }
            season = match[1]
    
            let dir_up = require('path').resolve(dir, '..', '..')
            let dir_srt = path.join(dir_up, 'srt', season, 'jp')
            if ( !fs.existsSync( dir_srt ) ) {
                fs.mkdirSync(dir_srt, { recursive: true })
            }
            let srtpath = path.join(dir_srt, `${name}.srt`)
    
            let srt = this.libs.ttml2.extractSrt({mlpath})
            require('fs').writeFileSync( srtpath, srt, {encoding:'utf8'})

            jps.push(srt)

        }

        let chs = []
        for (let ttml of ttml2s) {

            let match= ttml.match(/(\d+)\./)
            if (match == null) {
                throw `name not correct. ${ttml}`
            }
            let nth = match[1]

            let match_season = ttml.match(/[\\\/](S\d+)[\\\/]/)
            if (match_season == null) {
                throw `match_season not correct. ${ttml}`
            }

            let season = match_season[1]

            for (let sapath of ssas) {

                let match2 = sapath.match(/\](\d+)\.chs/)
                if (match2 == null) {
                    continue  //throw `name not correct. ${ssa}`
                }
                let nth2 = match2[1]
    
                let match_season2 = sapath.match(/[\\\/](S\d+)[\\\/]/)
                if (match_season2 == null) {
                    throw `match_season2 not correct. ${sapath}`
                }
                let season2 = match_season2[1]
    
                if (season == season2) {
    
                    if (Number(nth) == Number(nth2)) {
    
                        let { base,dir,ext,name,root} = path.parse(ttml)
                        let { base:base2,dir:dir2,ext:ext2,name:name2,root:root2} = path.parse(sapath)

                        let dir_up = require('path').resolve(dir, '..', '..')
                        let dir_srt = path.join(dir_up, 'srt', season, 'chs')
                        if ( !fs.existsSync( dir_srt ) ) {
                            fs.mkdirSync(dir_srt, { recursive: true })
                        }
                        let srtpath = path.join(dir_srt, `${name}.srt`)

                        let srt = this.libs.ssa.extractSrt({sapath})
                        require('fs').writeFileSync(srtpath, srt, {encoding:'utf8'})

                        if (srt == '') {
                            let a = 1
                        }

                        chs.push(srt)

                        break
    
                    }
    
                }
    
            }
        
        }


        //
        // 处理第三季字幕
        //
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S03'])
        // remove space
        for (let ttml of ttml2s) {
            let { base,dir,ext,name,root} = path.parse(ttml)
            let withoutSpace = base.replace(/\s/g, '')
            if (withoutSpace != base) {
                let newname = path.join(dir, withoutSpace)
                fs.renameSync( ttml, newname )
            }
        }
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S03'])
        jps = save_ttml2(ttml2s)

        // 
        // 处理第六季字幕
        //
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S06'])
        // remove space
        for (let ttml of ttml2s) {
            let { base,dir,ext,name,root} = path.parse(ttml)
            let withoutSpace = base.replace(/\s/g, '')
            if (withoutSpace != base) {
                let newname = path.join(dir, withoutSpace)
                fs.renameSync( ttml, newname )
            }
        }
        ttml2s = this.libs.files.allfiles(global.root_subtitles, 'ttml2', ['amazon', 'pokemon', 'S06'])
        jps = save_ttml2(ttml2s)

        return this.msg(200, {jps, chs})
    }
}



function save_ttml2(ttml2s) {

    let jps = []

    for (let mlpath of ttml2s) {

        let { base, dir, ext, name, root } = path.parse(mlpath)

        let season = ''
        let match = mlpath.match(/[\\\/](S\d\d)[\\\/]/)
        if (match == null) {
            throw 'no season on subtitle path'
        }
        season = match[1]

        let dir_up = require('path').resolve(dir, '..', '..')
        let dir_srt = path.join(dir_up, 'srt', season, 'jp')
        if ( !fs.existsSync( dir_srt ) ) {
            fs.mkdirSync(dir_srt, { recursive: true })
        }
        let srtpath = path.join(dir_srt, `${name}.srt`)

        let srt = this.libs.ttml2.extractSrt({mlpath})
        require('fs').writeFileSync( srtpath, srt, {encoding:'utf8'})

        jps.push(srt)

    }

    return jps
}