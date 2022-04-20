
let fs = require('fs')
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
    }
}