



module.exports = {

    extract: async function (vdpath, type, begin_time, end_time) {

        let fs = require('fs')
        let ffmpeg = require('fluent-ffmpeg')

        ffmpeg.setFfmpegPath(String.raw`E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe`)

        let [au, ms1] = await new Promise(function (resolve) {

            const stream = require('stream')

            var vd = fs.createReadStream(vdpath)

            let bufferStream = new stream.PassThrough()
            // Read the passthrough stream
            const buffers = []
            bufferStream.on('data', function (buf) {
                buffers.push(buf)
            })
            bufferStream.on('end', function () {
                const outputBuffer = Buffer.concat(buffers)
                //let sr = outputBuffer.toString('utf8')
                // let dir = require('path').dirname(__filename)
                // let fname = require('path').join(dir, 'tmp.mp3')
                fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                // use outputBuffer
                resolve([outputBuffer, ''])
            })

            ffmpeg(vd)//.output(au)
                .noVideo()
                .format(type)
                .outputOptions('-ss', begin_time) // '00:01:12.960'
                .outputOptions('-to', end_time) // '00:01:14.640'
                .writeToStream(bufferStream)
            // .on('start', () => {

            //   a = 1

            // })
            // .on('end', () => {

            //   a = 1

            //   resolve(['ok', 'ok.'])
            // })
            // .run()
        })

        return [au, ms1]


    }

}





