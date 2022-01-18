



module.exports = {

    // extractSRT: async function (vdpath, nth) {

    //     let fs = require('fs')
    //     let ffmpeg = require('fluent-ffmpeg')

    //     ffmpeg.setFfmpegPath(String.raw`E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe`)

    //     let [au, ms1] = await new Promise(function (resolve) {

    //         const stream = require('stream')

    //         var vd = fs.createReadStream(vdpath)

    //         let bufferStream = new stream.PassThrough()
    //         // Read the passthrough stream
    //         const buffers = []
    //         bufferStream.on('data', function (buf) {
    //             buffers.push(buf)
    //         })
    //         bufferStream.on('end', function () {
    //             const outputBuffer = Buffer.concat(buffers)
    //             //let sr = outputBuffer.toString('utf8')
    //             // let dir = require('path').dirname(__filename)
    //             // let fname = require('path').join(dir, 'tmp.mp3')
    //             fs.writeFileSync(`tmp.srt`, outputBuffer, 'binary')
    //             vd.close()
    //             resolve([outputBuffer, ''])
    //         })

    //         ffmpeg(vd)//.output(au)
    //             .noVideo()
    //             .format('srt')
    //             .outputOptions('-map', `0:s:${nth}`)
    //             .writeToStream(bufferStream)
    //         // .on('start', () => {

    //         //   a = 1

    //         // })
    //         // .on('end', () => {

    //         //   a = 1

    //         //   resolve(['ok', 'ok.'])
    //         // })
    //         // .run()
    //     })

    //     return [au, ms1]


    // },
    extractAudio: async function (vdpath, type, begin_time, end_time) {

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

            })

            ffmpeg(vd)//.output(au)
                .noVideo()
                .format(type)
                // .audioBitrate('128')
                // .outputOptions('-ss', begin_time) // 00:00:00.000
                // .outputOptions('-to', end_time)   // 00:00:07.520
                .outputOption(
                    [
                        "-vn", 
                        "-ss", 
                        begin_time, 
                        "-to", 
                        end_time, 
                        "-acodec", "mp3",
                        "-ar", "44100", 
                        "-ac", "2", 
                        "-b:a", "192k"
                    ]
                )
                .writeToStream(bufferStream)
                .on("end", (stdout, stderr) =>{
                    const outputBuffer = Buffer.concat(buffers)
                    //let sr = outputBuffer.toString('utf8')
                    // let dir = require('path').dirname(__filename)
                    // let fname = require('path').join(dir, 'tmp.mp3')
                    fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                    vd.close()
                    resolve([outputBuffer, ''])
                })

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


    },
    extractSubtitle: async function (vdpath, type, nth) {

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

            })

            ffmpeg(vd)
                .noVideo()
                .format(type)
                .outputOption(
                    [
                        '-map', `0:s:${nth}`
                    ]
                )
                .writeToStream(bufferStream)
                .on("end", (stdout, stderr) =>{
                    const outputBuffer = Buffer.concat(buffers)
                    //let sr = outputBuffer.toString('utf8')
                    // let dir = require('path').dirname(__filename)
                    // let fname = require('path').join(dir, 'tmp.mp3')
                    fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                    vd.close()
                    resolve([outputBuffer, ''])
                })

        })

        return [au, ms1]


    },

}


/*
    ffmpeg -i F:\videos\anime\Pokemon\S14\Best_Wishes\06.mkv
          Stream #0:2: Subtitle: ass (default)
          Stream #0:3: Subtitle: ass
          Stream #0:4: Subtitle: ass

    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])

    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
      "-ar", "44100", "-ac", "2", "-b:a", "192k", \
        "tmp.mp3"])
    
    https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/issues/470

    ffmpeg
  //.withVideoCodec('h264_nvenc')
  .withVideoBitrate(8000)
  .withAudioCodec('libmp3lame')
  .withVideoCodec('h264_nvenc')
  .outputOption([
    '-map 0',
    '-map -v',
    '-map -a',
    '-map 0:V',
    '-map 0:m:language:eng?', // TODO: This should be an input parameter to be able to change language
    '-deadline realtime',
    '-lag-in-frames 0',
    '-static-thresh 0',
    '-frame-parallel 1',
    '-crf 4',
    '-movflags frag_keyframe+faststart',
    '-pix_fmt yuv420p',
    '-sn',
    '-max_muxing_queue_size 9999'
  ])
  .outputFormat('mp4')
};


*/


