
(async () => {

  // let kuromoji = require('kuromoji')

  // let [ tokenizer, ms ] = await new Promise(function (resolve) {

  //   kuromoji.builder({ dicPath: "./dicts/neologd/" }).build((err, tokenizer) => {

  //     if (err) resolve([ null, err.toString() ] )

  //     resolve([ tokenizer, ''])

  //  })

  // })

  // let arr = require('fs').readFileSync('./data.json', {encoding:'utf8', flag:'r'})



  // let a = tokenizer.tokenize(arr[0])




  let [sr, ms] = await new Promise(function (resolve) {

    var ffmpeg = require('fluent-ffmpeg')

    var vd = require('fs').createReadStream('F:/1.mkv')
    //var au = require('fs').createWriteStream('tmp.srt')

    const stream = require('stream')
    let bufferStream = new stream.PassThrough()
    // Read the passthrough stream
    const buffers = []
    bufferStream.on('data', function (buf) {
      buffers.push(buf)
    })
    bufferStream.on('end', function () {
      const outputBuffer = Buffer.concat(buffers)
      let sr = outputBuffer.toString('utf8')
      // use outputBuffer
      resolve([sr, ''])
    })

    ffmpeg(vd)//.output(au)
      .noVideo()
      .format('srt')
      .outputOptions('-map', '0:s:0')
      //.outputOptions('-ss','00:01:12.960')
      //.outputOptions('-to','00:01:14.640')
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
















  const { Pool, Client } = require('pg')

  const config = {
    user: 'postgres',
    password: 'echodict.com',
    host: '209.141.34.77',
    port: '5432',
    database: 'anime',
    ssl: false
  }











  var pool = new Pool(config)
  var client = await pool.connect()
  try {
    //var result = await client.query('select $1::text as name', ['brianc'])
    //var result = await client.query(`select id, en, zh, type from anime where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;`, ['黑白'])
    var result = await client.query(`SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ $1 ORDER BY RANDOM() limit 3;`, ['大']) // ここ
    //var result = await client.query(`SELECT id, jp, zh, time FROM anime limit $1;`, ['1'])
    console.log('hello from', result.rows)
  } finally {
    client.release()
    a = 1
  }
})().catch(e => console.error(e.message, e.stack))

