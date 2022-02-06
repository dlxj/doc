
import fs from 'fs'
import { execa } from 'execa'
import path from 'path'
import { dirname } from 'path'
//global.__dirname = process.cwd()
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

export default {

    extractSubtitle: async function (vdpath, type, nth) {

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

        try {

            // 管道读出来的音频流播放不了，改成写临时文件
            //let cmd = `ffmpeg -i "${vdpath}" -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} pipe:1`   // write stdout

            let cmd = `ffmpeg -i "${vdpath}" -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} tmp.mp3`   // write stdout


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
    }
}

/*

  let { default: libff } = await import('./ffmpeg.mjs')
  // let { srt: str_jp, msg:msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream
  //let { srt: srt_chs, msg:msg_chs } = await libff.extractSubtitle(vdpath, 'srt', 0) 
  //let { au: axx} = await libff.extractAudio(vdpath, 'mp3', '00:00:01.960', '00:00:05.660')

*/

