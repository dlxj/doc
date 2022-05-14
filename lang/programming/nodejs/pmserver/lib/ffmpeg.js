
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
                cmd = `ffmpeg -y -i -itsoffset -1.0 "${vdTWPath}" -i "${vdAMPath}" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='${ffmpegsubtitle}'" "${hardjppath}"`  // 生成硬字幕
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
    }
}