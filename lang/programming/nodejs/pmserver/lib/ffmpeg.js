
let fs = require('fs')
const { platform } = require('os')
let path = require('path')
let dirname = path.dirname
// global.__dirname = process.cwd()
let url = require('url')
let fileURLToPath = url.fileURLToPath
//  __filename = fileURLToPath(import.meta.url)
// const __dirname = path.dirname(__filename)


module.exports = {

    extractSubtitle: async function (vdpath, type, nth) {

        let { execa } = await import('execa')

        try {

            // let args = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} ${path.join( __dirname, 'tmp.srt' )}` // write file
            let cmd = `ffmpeg -i "${vdpath}" -y -map 0:s:${nth} -f ${type} pipe:1`  // write stdout

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            //childProcess.stdout.pipe(process.stdout)  // don't print to screen
            let { stdout } = await childProcess

            return { srt:stdout, msg:'' }

        } catch(err) {
           return { srt:null, msg : err }
        }        
    },
    extractAudio: async function (vdpath, type, begin_time, end_time) {
        
        let { execa } = await import('execa')

        try {

            // 管道读出来的音频流播放不了，改成写临时文件
            //let cmd = `ffmpeg -i "${vdpath}" -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} pipe:1`   // write stdout

            let cmd = ``
            if (end_time != '') {
                cmd = `ffmpeg -i "${vdpath}" -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} tmp.mp3`   // write stdout
            } else {
                cmd = `ffmpeg -i "${vdpath}" -y -vn -ss ${begin_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} tmp.mp3`   // write stdout
            }

            //let cmd = `ffmpeg -i "${vdpath}" -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} tmp.mp3`   // write stdout

            let childProcess = execa(cmd, {shell:true})
            //childProcess.stdout.pipe(process.stdout) // don't print to screen
            let { stdout } = await childProcess

            let audio = fs.readFileSync('./tmp.mp3')
            //fs.writeFileSync('./tmpppp.mp3', audio)
            fs.unlinkSync('./tmp.mp3')

            return { au: audio }

        } catch(err) {
           return { au:null}
        }
    },
    cutVideo: async function (vdpath, times) {

        /*
        ffmpeg -ss 00:00:01.500 -to 00:11:36.000 -accurate_seek -i 5.mp4 -vcodec copy -acodec copy -avoid_negative_ts 1 -y tmp.mp4
ffmpeg -ss 00:11:49.500 -to 00:15:49.500 -accurate_seek -i 5.mp4 -vcodec copy -acodec copy -avoid_negative_ts 1 -y tmp2.mp4

ffmpeg -safe 0 -f concat -i tmp.mp4 tmp2.mp4 -vcodec copy -acodec copy -strict -2 -y concat.mp4

list.txt
file 'tmp.mp4'
file 'tmp2.mp4'
         */

        let { base, dir, ext, name, root } = path.parse(vdpath)
        
        let { execa } = await import('execa')

        try {

            let list_txt = ``
            let tmpNames = []
            for (let [ k, v ] of Object.entries(times) ) { // 00:00:01.500

                let { ss, to } = v
                let cmd = ``
                let tmpName = `tmp${k}${ext}`
                if (to != '') {
                    cmd = `ffmpeg -ss ${ss} -to ${to} -accurate_seek -i "${vdpath}" -vcodec copy -acodec copy -y ${tmpName}`
                } else {
                    cmd = `ffmpeg -ss ${ss} -accurate_seek -i "${vdpath}" -vcodec copy -acodec copy -y ${tmpName}`
                }

                list_txt += `file '${tmpName}'\n`
                tmpNames.push(tmpName)
                
                let childProcess = execa(cmd, {shell:true})
                //childProcess.stdout.pipe(process.stdout) // don't print to screen
                let { stdout } = await childProcess

                let a = 1

            }
            
            require('fs').writeFileSync('list.txt', list_txt, {encoding:'utf8'})

            let des = `concat${ext}`

            let cmd = `ffmpeg -safe 0 -f concat -i list.txt -vcodec copy -acodec copy -strict -2 -y ${des}`

            let childProcess = execa(cmd, {shell:true})
            let { stdout } = await childProcess

            let a = 1

            for (let tmpName of tmpNames) {

                fs.unlinkSync(tmpName)

            }

            fs.unlinkSync(vdpath)

            fs.unlinkSync('list.txt')

            require('fs-extra').moveSync( des, vdpath )

            return { result:'', msg: 'ok' }

        } catch(err) {
           return { result:null, msg:err }
        }
    },
    injectSubtitle:async function(vdpath, subpath, outpath) {

        // ffmpeg -i F:\video.mkv -vn -an -codec:s:0 srt F:\subtitle.srt

        let { execa } = await import('execa')

        try {

            let cmd = `ffmpeg -i "${vdpath}" -i "${subpath}" -c copy ${outpath}`  // ffmpeg -i video.mkv -i subtitle.ass -c copy output.mkv

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            let { stdout } = await childProcess

            return { msg:stdout }

        } catch(err) {
           return { msg : err }
        } 
    },
    injectSubtitleAudio:async function(vdpath, subpath, aupath, outpath) {

        // ffmpeg -i F:\video.mkv -vn -an -codec:s:0 srt F:\subtitle.srt

        let { execa } = await import('execa')

        try {

            let cmd = `ffmpeg -i "${vdpath}" -i "${subpath}" -i "${aupath}" -c copy ${outpath}`  // ffmpeg -i video.mkv -i subtitle.ass -c copy output.mkv

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            let { stdout } = await childProcess

            return { msg:stdout }

        } catch(err) {
           return { msg : err }
        } 
    },
    merge_pokemonAmazon_pokemonTW:async function(vdTWPath, vdAMPath, subpath, outpath) {
        /*
           # 提前2.2 秒，嵌入日文作为硬字幕  # 试转一小段看对不对，经实验 -2.2 比较好
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 -ss 00:01:49.000 -to 00:05:00.000 -vf subtitles=1.srt advance2second.mp4

           # 先提前2.2 秒，再嵌入日文软字幕
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
           ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv

           # 1 是pokemon台版中文硬字幕mp4，2 是日文软字幕mkv，中硬比日软要慢2.2 秒左右
        */

        // hard subtitle
        // ffmpeg -y -itsoffset -2.2 -i 1.mp4 -vf subtitles=1.srt advance2second_hardjp.mp4

        /*
         * soft subtitle
         * ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
         * ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
         */

        let { execa } = await import('execa')

        try {

            let { base,dir,ext,name,root} = path.parse(outpath)

            /*
            
            // 绝对路径的写法比较特别
            ffmpeg -y -itsoffset -2.2 -i "E:\t\1.mp4" -vf  "subtitles='E\:\\t\\1.srt'"  advance2second_hardjp.mp4

            
            */

            
            let hardjpdir = path.join(dir, 'hardjp')
            if (!fs.existsSync(hardjpdir)) {
                fs.mkdirSync(hardjpdir, { recursive: false })
            }

            let hardjppath = path.join(hardjpdir, `${name}.mp4`)

            let softjpdir = path.join(dir, 'softjp')
            if (!fs.existsSync(softjpdir)) {
                fs.mkdirSync(softjpdir, { recursive: false })
            }

            let softjppath = path.join(softjpdir, `${name}.mkv`)

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -ss 00:01:49.000 -to 00:05:00.000 -vf "subtitles='E\\:\\\\t\\\\1.srt'" "${hardjppath}"`  // 生成硬字幕
            
            let ffmpegsubtitle = `E\\:\\\\t\\\\1.srt`

            let platform = process.platform
            if (platform == 'win32') {
                ffmpegsubtitle = subpath.replace(/\\/g, '\\\\')
                ffmpegsubtitle = ffmpegsubtitle.replace(/\:/, '\\:')
            } else if (platform == 'linux') {
                ffmpegsubtitle = subpath
            } else if (platform == 'darwin') {
                ffmpegsubtitle = subpath
            } else {
                throw `unkonw os type.`
            }

            let match3 = vdTWPath.match(/[\\\/](\d+)\./)  // 必须是改过名的, 和amazon pm jp 名字一样
            if (match3 == null) {
                throw `name not correct. ${m4}`
            }
            let nth3 = match3[1]

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -ss 00:01:49.000 -to 00:01:59.000 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕

            if ( Number(nth3) >= 83 ) {
                // tw 对 am 的延迟时间变了
                cmd = `ffmpeg -y -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }



            let childProcess = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out1 } = await childProcess

            cmd = `ffmpeg -y -i "${hardjppath}" -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0 -map 0:a:1 -c copy -map 2 -c:s srt "${softjppath}"`

            let childProcess2 = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out2 } = await childProcess2

            return { msg:out2 }


            /*
            
            ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
            ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
            
            */

            // let tmpm4 = `advance2second.mp4`
            // let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" ${tmpm4}`

            // let childProcess2 = execa(cmd, { shell:true, 'encoding': 'utf8' })
            // let { stdout:out2 } = await childProcess2

            // cmd = `ffmpeg -y -i ${tmpm4} -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt ${softjppath}`

            // let childProcess3 = execa(cmd, { shell:true, 'encoding': 'utf8' })
            // let { stdout:out3 } = await childProcess3

            // fs.unlinkSync(tmpm4)

        } catch(err) {
           return { msg : err }
        } 
    },
    merge_pokemonAmazon_pokemonTWS03:async function(vdTWPath, vdAMPath, subpath, outpath) {
        /*
           # 提前2.2 秒，嵌入日文作为硬字幕  # 试转一小段看对不对，经实验 -2.2 比较好
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 -ss 00:01:49.000 -to 00:05:00.000 -vf subtitles=1.srt advance2second.mp4

           # 先提前2.2 秒，再嵌入日文软字幕
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
           ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv

           # 1 是pokemon台版中文硬字幕mp4，2 是日文软字幕mkv，中硬比日软要慢2.2 秒左右
        */

        // hard subtitle
        // ffmpeg -y -itsoffset -2.2 -i 1.mp4 -vf subtitles=1.srt advance2second_hardjp.mp4

        /*
         * soft subtitle
         * ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
         * ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
         */

        let { execa } = await import('execa')

        try {

            let { base,dir,ext,name,root} = path.parse(outpath)

            /*
            
            // 绝对路径的写法比较特别
            ffmpeg -y -itsoffset -2.2 -i "E:\t\1.mp4" -vf  "subtitles='E\:\\t\\1.srt'"  advance2second_hardjp.mp4

            
            */

            
            let hardjpdir = path.join(dir, 'hardjp')
            if (!fs.existsSync(hardjpdir)) {
                fs.mkdirSync(hardjpdir, { recursive: false })
            }

            let hardjppath = path.join(hardjpdir, `${name}.mp4`)

            let softjpdir = path.join(dir, 'softjp')
            if (!fs.existsSync(softjpdir)) {
                fs.mkdirSync(softjpdir, { recursive: false })
            }

            let softjppath = path.join(softjpdir, `${name}.mkv`)

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -ss 00:01:49.000 -to 00:05:00.000 -vf "subtitles='E\\:\\\\t\\\\1.srt'" "${hardjppath}"`  // 生成硬字幕
            
            let ffmpegsubtitle = `E\\:\\\\t\\\\1.srt`

            let platform = process.platform
            if (platform == 'win32') {
                ffmpegsubtitle = subpath.replace(/\\/g, '\\\\')
                ffmpegsubtitle = ffmpegsubtitle.replace(/\:/, '\\:')
            } else if (platform == 'linux') {
                ffmpegsubtitle = subpath
            } else if (platform == 'darwin') {
                ffmpegsubtitle = subpath
            } else {
                throw `unkonw os type.`
            }

            let match3 = vdTWPath.match(/[\\\/](\d+)\./)  // 必须是改过名的, 和amazon pm jp 名字一样
            if (match3 == null) {
                throw `name not correct. ${m4}`
            }
            let nth3 = match3[1]

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -ss 00:01:49.000 -to 00:01:59.000 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            let cmd = `ffmpeg -y -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕

            if ( Number(nth3) >= 95 ) {  // 95 开始tw 慢了1 秒
                // tw 对 am 的延迟时间变了
                cmd = `ffmpeg -y -itsoffset -1.0 -i  "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }



            let childProcess = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out1 } = await childProcess

            cmd = `ffmpeg -y -i "${hardjppath}" -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0 -map 0:a:1 -c copy -map 2 -c:s srt "${softjppath}"`

            let childProcess2 = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out2 } = await childProcess2

            return { msg:out2 }


        } catch(err) {
           return { msg : err }
        } 
    },
    merge_pokemonAmazon_pokemonTWS06:async function(vdTWPath, vdAMPath, subpath, outpath) {
        /*
           # 提前2.2 秒，嵌入日文作为硬字幕  # 试转一小段看对不对，经实验 -2.2 比较好
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 -ss 00:01:49.000 -to 00:05:00.000 -vf subtitles=1.srt advance2second.mp4

           # 先提前2.2 秒，再嵌入日文软字幕
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
           ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv

           # 1 是pokemon台版中文硬字幕mp4，2 是日文软字幕mkv，中硬比日软要慢2.2 秒左右
        */

        // hard subtitle
        // ffmpeg -y -itsoffset -2.2 -i 1.mp4 -vf subtitles=1.srt advance2second_hardjp.mp4

        /*
         * soft subtitle
         * ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
         * ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
         */

        let { execa } = await import('execa')

        try {

            let { base,dir,ext,name,root} = path.parse(outpath)

            /*
            
            // 绝对路径的写法比较特别
            ffmpeg -y -itsoffset -2.2 -i "E:\t\1.mp4" -vf  "subtitles='E\:\\t\\1.srt'"  advance2second_hardjp.mp4

            
            */

            
            let hardjpdir = path.join(dir, 'hardjp')
            if (!fs.existsSync(hardjpdir)) {
                fs.mkdirSync(hardjpdir, { recursive: false })
            }

            let hardjppath = path.join(hardjpdir, `${name}.mp4`)

            let softjpdir = path.join(dir, 'softjp')
            if (!fs.existsSync(softjpdir)) {
                fs.mkdirSync(softjpdir, { recursive: false })
            }

            let softjppath = path.join(softjpdir, `${name}.mkv`)

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -ss 00:01:49.000 -to 00:05:00.000 -vf "subtitles='E\\:\\\\t\\\\1.srt'" "${hardjppath}"`  // 生成硬字幕
            
            let ffmpegsubtitle = `E\\:\\\\t\\\\1.srt`

            let platform = process.platform
            if (platform == 'win32') {
                ffmpegsubtitle = subpath.replace(/\\/g, '\\\\')
                ffmpegsubtitle = ffmpegsubtitle.replace(/\:/, '\\:')
            } else if (platform == 'linux') {
                ffmpegsubtitle = subpath
            } else if (platform == 'darwin') {
                ffmpegsubtitle = subpath
            } else {
                throw `unkonw os type.`
            }

            let match3 = vdTWPath.match(/[\\\/](\d+)\./)  // 必须是改过名的, 和amazon pm jp 名字一样
            if (match3 == null) {
                throw `name not correct. ${m4}`
            }
            let nth3 = match3[1]

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -ss 00:01:49.000 -to 00:01:59.000 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            let cmd = `ffmpeg -y -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕

            if (Number(nth3) >= 90 && Number(nth3) <= 91) {
                cmd = `ffmpeg -y -itsoffset -11 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }

            if (Number(nth3) >= 92) {
                cmd = `ffmpeg -y -itsoffset -14 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }

            if (Number(nth3) >= 93) {
                cmd = `ffmpeg -y -itsoffset -13 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }

            
            if (Number(nth3) >= 106) {
                cmd = `ffmpeg -y -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }

            if (Number(nth3) >= 152) {
                cmd = `ffmpeg -y -itsoffset -6 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            }

            let childProcess = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out1 } = await childProcess

            cmd = `ffmpeg -y -i "${hardjppath}" -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0 -map 0:a:1 -c copy -map 2 -c:s srt "${softjppath}"`

            // if (Number(nth3) >= 90) {
            //     cmd = `ffmpeg -y  -itsoffset -11 -i "${hardjppath}" -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0 -map 0:a:1 -c copy -map 2 -c:s srt "${softjppath}"`
            // }

            let childProcess2 = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out2 } = await childProcess2

            return { msg:out2 }


        } catch(err) {
           return { msg : err }
        } 
    },
    merge_pokemonAmazon_pokemonTWS10:async function(vdTWPath, vdAMPath, subpath, outpath) {
        /*
           # 提前2.2 秒，嵌入日文作为硬字幕  # 试转一小段看对不对，经实验 -2.2 比较好
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 -ss 00:01:49.000 -to 00:05:00.000 -vf subtitles=1.srt advance2second.mp4

           # 先提前2.2 秒，再嵌入日文软字幕
           ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
           ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv

           # 1 是pokemon台版中文硬字幕mp4，2 是日文软字幕mkv，中硬比日软要慢2.2 秒左右
        */

        // hard subtitle
        // ffmpeg -y -itsoffset -2.2 -i 1.mp4 -vf subtitles=1.srt advance2second_hardjp.mp4

        /*
         * soft subtitle
         * ffmpeg -y -itsoffset -2.2 -i 1.mp4 advance2second.mp4
         * ffmpeg -y -i advance2second.mp4 -i 2.mkv -i 1.srt -map 0:v -map 1:a:0  -map 0:a:0  -c copy  -map 2 -c:s srt out.mkv
         */

        let { execa } = await import('execa')

        try {

            let { base,dir,ext,name,root} = path.parse(outpath)

            /*
            
            // 绝对路径的写法比较特别
            ffmpeg -y -itsoffset -2.2 -i "E:\t\1.mp4" -vf  "subtitles='E\:\\t\\1.srt'"  advance2second_hardjp.mp4

            
            */

            
            let hardjpdir = path.join(dir, 'hardjp')
            if (!fs.existsSync(hardjpdir)) {
                fs.mkdirSync(hardjpdir, { recursive: false })
            }

            let hardjppath = path.join(hardjpdir, `${name}.mp4`)

            let softjpdir = path.join(dir, 'softjp')
            if (!fs.existsSync(softjpdir)) {
                fs.mkdirSync(softjpdir, { recursive: false })
            }

            let softjppath = path.join(softjpdir, `${name}.mkv`)

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -ss 00:01:49.000 -to 00:05:00.000 -vf "subtitles='E\\:\\\\t\\\\1.srt'" "${hardjppath}"`  // 生成硬字幕
            
            let ffmpegsubtitle = `E\\:\\\\t\\\\1.srt`

            let platform = process.platform
            if (platform == 'win32') {
                ffmpegsubtitle = subpath.replace(/\\/g, '\\\\')
                ffmpegsubtitle = ffmpegsubtitle.replace(/\:/, '\\:')
            } else if (platform == 'linux') {
                ffmpegsubtitle = subpath
            } else if (platform == 'darwin') {
                ffmpegsubtitle = subpath
            } else {
                throw `unkonw os type.`
            }

            let match3 = vdTWPath.match(/[\\\/](\d+)\./)  // 必须是改过名的, 和amazon pm jp 名字一样
            if (match3 == null) {
                throw `name not correct. ${m4}`
            }
            let nth3 = match3[1]

            //let cmd = `ffmpeg -y -itsoffset -2.2 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -ss 00:01:49.000 -to 00:01:59.000 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            let cmd = `ffmpeg -y -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕

            if (Number(nth3) >= 5 && Number(nth3) <= 47) {  // 台版从第五集开始有多余的东西需要剪掉 48 是总集编台版没有 

                let times = [
                    {ss:`00:00:01.500`, to:`00:11:36.000`},
                    {ss:`00:11:49.500`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            
            if (Number(nth3) >= 49 && Number(nth3) <= 49) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:12:14.500`},
                    {ss:`00:12:28.000`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 50 && Number(nth3) <= 50) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:08:59.500`},
                    {ss:`00:09:13.000`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            
            if (Number(nth3) >= 51 && Number(nth3) <= 51) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:12:53.000`},
                    {ss:`00:13:04.000`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 52 && Number(nth3) <= 52) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:12:28.000`},
                    {ss:`00:12:39.000`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 53 && Number(nth3) <= 53) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:13:58.000`},
                    {ss:`00:14:09.000`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 54 && Number(nth3) <= 54) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:11:54.449`},
                    {ss:`00:12:05.529`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 55 && Number(nth3) <= 55) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:11:50.676`},
                    {ss:`00:12:01.520`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 56 && Number(nth3) <= 56) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:10:45.578`},
                    {ss:`00:10:56.255`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            
            if (Number(nth3) >= 57 && Number(nth3) <= 57) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:12:06.528`},
                    {ss:`00:12:17.421`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 58 && Number(nth3) <= 58) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:11:55.516`},
                    {ss:`00:12:08.428`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 59 && Number(nth3) <= 59) {  //  

                let times = [
                    {ss:`00:00:00.000`, to:`00:11:59.519`},
                    {ss:`00:12:12.465`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 60 && Number(nth3) <= 60) {

                let times = [
                    {ss:`00:00:00.000`, to:`00:11:01.495`},
                    {ss:`00:11:12.306`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            if (Number(nth3) >= 61 && Number(nth3) <= 61) {

                let times = [
                    {ss:`00:00:00.000`, to:`00:12:23.561`},
                    {ss:`00:12:33.738`, to:``}
                ]

                await this.libs.ffmpeg.cutVideo(vdTWPath, times)

            }

            // if (Number(nth3) >= 92) {
            //     cmd = `ffmpeg -y -itsoffset -14 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            // }

            // if (Number(nth3) >= 93) {
            //     cmd = `ffmpeg -y -itsoffset -13 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            // }

            
            // if (Number(nth3) >= 106) {
            //     cmd = `ffmpeg -y -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            // }

            // if (Number(nth3) >= 152) {
            //     cmd = `ffmpeg -y -itsoffset -6 -i "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
            // }

            let childProcess = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out1 } = await childProcess

            cmd = `ffmpeg -y -i "${hardjppath}" -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0 -map 0:a:1 -c copy -map 2 -c:s srt "${softjppath}"`

            // if (Number(nth3) >= 90) {
            //     cmd = `ffmpeg -y  -itsoffset -11 -i "${hardjppath}" -i "${vdAMPath}" -i "${subpath}" -map 0:v -map 1:a:0 -map 0:a:1 -c copy -map 2 -c:s srt "${softjppath}"`
            // }

            let childProcess2 = execa(cmd, { shell:true, 'encoding': 'utf8' })
            let { stdout:out2 } = await childProcess2

            return { msg:out2 }


        } catch(err) {
           return { msg : err }
        } 
    }
}