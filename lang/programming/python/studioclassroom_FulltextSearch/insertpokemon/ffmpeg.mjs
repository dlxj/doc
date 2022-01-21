
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
            let cmd = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} -f srt pipe:1`   // write stdout

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            childProcess.stdout.pipe(process.stdout)
            let { stdout } = await childProcess

            return { srt:stdout, msg:'' }

        } catch(err) {
           return { srt:null, msg : err }
        }
    }

}

