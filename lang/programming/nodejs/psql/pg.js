
const config = {
  user: 'postgres',
  password: 'echodict.com',
  host: '209.141.34.77',
  port: '5432',
  database: 'postgres',
  ssl: false
}

let { Pool, Client } = require('pg')
var pool = new Pool(config)

module.exports = {
  query
}

function query(sql, params) {

  var client = await pool.connect()

  try {

    //var result = await client.query('select $1::text as name', ['brianc'])
    var result = await client.query(sql, params)
    return result

  } catch (err) {
    throw new Error(err.message)
  } finally {
    client.release()
  }

}





// (async () => {

//   String.prototype.replaceAll = function (search, replacement) {
//     var target = this
//     return target.replace(new RegExp(search, 'g'), replacement)
//   }


//   let rc = require('fs').readFileSync(require('path').join(require('path').dirname(__filename), '1.lrc'),{encoding:'utf8', flag:'r'})
//   rc = rc.replaceAll('\r\n', '\n')







//   // let kuromoji = require('kuromoji')

//   // let [ tokenizer, ms ] = await new Promise(function (resolve) {

//   //   kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {

//   //     if (err) resolve([ null, err.toString() ] )

//   //     resolve([ tokenizer, ''])

//   //  })

//   // })

//   // let arr = require('fs').readFileSync('./data.json', {encoding:'utf8', flag:'r'})



//   // let a = tokenizer.tokenize(arr[0])



//   var rcs = []


//   //[00:00.00]  分、秒、百分之一秒

//   let matchs = rc.matchAll( new RegExp(String.raw`\[\d\d:\d\d\.\d\d\]`, 'g') )
//   let arr = Array.from( matchs )
//   for (let i = 0; i < arr.length; i++) {

//     let match = arr[i]
//     let begin = match.index

//     let text = ''
//     let endtime = ''
//     if (i == arr.length -1) {

//       text = rc.substring(begin)

//     } else {

//       let end = arr[i+1].index
//       let endreal = end + arr[i+1][0].length
//       endtime = rc.substring(end, endreal)

//       text = rc.substring(begin, end)

//     }

//     let match2 = text.match( new RegExp(String.raw`\[(\d\d):(\d\d)\.(\d\d)\](.+)`, 's') )
//     if (match2 != null) {

//       let m = match2[1]   // minute
//       let s = match2[2]   // second
//       let ss = match2[3]  // 1% second
//       let begin_time = `00:${m}:${s}.${ss}0`

//       let text2 = match2[4]
//       if (text2.replaceAll(/\s+/, '') == '') {

//         a = 1

//       } else {

//         let j = ''
//         let z = ''
//         let arr_j = text2.split(/[（(]/)
//         if (arr_j.length > 0) {
//           j = arr_j[0].trim()
//         } else {
//           throw 'Error: LRC Format not correct. '
//         }

//         if (endtime != '') {

//           let match_endtime = endtime.match( new RegExp(String.raw`\[(\d\d):(\d\d)\.(\d\d)\]`) )
//           if (match_endtime != null) {

//             let med = match_endtime[1]   // minute
//             let sed = match_endtime[2]   // second
//             let ssed = match_endtime[3]  // 1% second
//             let end_time = `00:${med}:${sed}.${ssed}0`

//             // '00:01:12.960'  // 时 分 秒 毫秒

//             let arr_z = text2.split(/[)）\s]/)
//             if (arr_z.length > 0) {

//               if (arr_z[1] == undefined) {
//                 a = 1
//               }

//               z = arr_z[1].trim()
//             } else {
//               throw 'Error: LRC Format not correct. '
//             }


//             rcs.push( {j, z, begin_time, end_time} )

//           }


//         }

//         a = 1
//       }


//       a = 1

//     }

//     a = 1

//   }


//   a = 1









//   //a = 1

//   let [sr1, ms1] = await new Promise(function (resolve) {

//     var ffmpeg = require('fluent-ffmpeg')

//     var vd = require('fs').createReadStream('F:/1.mp3')
//     //var au = require('fs').createWriteStream('tmp.srt')

//     const stream = require('stream')
//     let bufferStream = new stream.PassThrough()
//     // Read the passthrough stream
//     const buffers = []
//     bufferStream.on('data', function (buf) {
//       buffers.push(buf)
//     })
//     bufferStream.on('end', function () {
//       const outputBuffer = Buffer.concat(buffers)
//       //let sr = outputBuffer.toString('utf8')
//       let dir =  require('path').dirname(__filename)
//       let fname = require('path').join(dir, 'tmp.mp3')
//       require('fs').writeFileSync(fname, outputBuffer, 'binary')
//       // use outputBuffer
//       resolve([outputBuffer, ''])
//     })

//     ffmpeg(vd)//.output(au)
//       .noVideo()
//       .format('mp3')
//       .outputOptions('-ss','00:01:12.960')
//       .outputOptions('-to','00:01:14.640')
//       .writeToStream(bufferStream)
//       // .on('start', () => {

//       //   a = 1

//       // })
//       // .on('end', () => {

//       //   a = 1

//       //   resolve(['ok', 'ok.'])
//       // })
//       // .run()
//   })


//   /*

//       out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
//       "-ar", "44100", "-ac", "2", "-b:a", "192k", \
//         "tmp.mp3"])

//   */


//   a = 1



//   let [sr, ms] = await new Promise(function (resolve) {

//     var ffmpeg = require('fluent-ffmpeg')

//     var vd = require('fs').createReadStream('F:/1.mkv')
//     //var au = require('fs').createWriteStream('tmp.srt')

//     const stream = require('stream')
//     let bufferStream = new stream.PassThrough()
//     // Read the passthrough stream
//     const buffers = []
//     bufferStream.on('data', function (buf) {
//       buffers.push(buf)
//     })
//     bufferStream.on('end', function () {
//       const outputBuffer = Buffer.concat(buffers)
//       let sr = outputBuffer.toString('utf8')
//       // use outputBuffer
//       resolve([sr, ''])
//     })

//     ffmpeg(vd)//.output(au)
//       .noVideo()
//       .format('srt')
//       .outputOptions('-map', '0:s:0')
//       //.outputOptions('-ss','00:01:12.960')
//       //.outputOptions('-to','00:01:14.640')
//       .writeToStream(bufferStream)
//       // .on('start', () => {

//       //   a = 1

//       // })
//       // .on('end', () => {

//       //   a = 1

//       //   resolve(['ok', 'ok.'])
//       // })
//       // .run()
//   })
















//   const { Pool, Client } = require('pg')

//   const config = {
//     user: 'postgres',
//     password: 'echodict.com',
//     host: '209.141.34.77',
//     port: '5432',
//     database: 'anime',
//     ssl: false
//   }











//   var pool = new Pool(config)
//   var client = await pool.connect()
//   try {
//     //var result = await client.query('select $1::text as name', ['brianc'])
//     //var result = await client.query(`select id, en, zh, type from anime where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;`, ['黑白'])
//     var result = await client.query(`SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ $1 ORDER BY RANDOM() limit 3;`, ['大']) // ここ
//     //var result = await client.query(`SELECT id, jp, zh, time FROM anime limit $1;`, ['1'])
//     console.log('hello from', result.rows)
//   } finally {
//     client.release()
//     a = 1
//   }
// })().catch(e => console.error(e.message, e.stack))


