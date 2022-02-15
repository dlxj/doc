
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

        let a = 1
        
    }

}