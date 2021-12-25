
(async () => {

    String.prototype.replaceAll = function (search, replacement) {
        var target = this
        return target.replace(new RegExp(search, 'g'), replacement)
      }
    
    
      let rc = require('fs').readFileSync(require('path').join(require('path').dirname(__filename), '1.lrc'),{encoding:'utf8', flag:'r'})
      rc = rc.replaceAll('\r\n', '\n')

    const { Pool, Client } = require('pg')

    const config = {
      user: 'postgres',
      password: 'echodict.com',
      host: '209.141.34.77',
      port: '5432',
      database: 'postgres',
      ssl: false
    }

    const config2 = {
        user: 'postgres',
        password: 'echodict.com',
        host: '209.141.34.77',
        port: '5432',
        database: 'zhry',
        ssl: false
      }


    var pool = new Pool(config)
    var pool2 = new Pool(config2)
    var client = await pool.connect()
    var client2 = null
    try {

        var result = await client.query('DROP DATABASE IF EXISTS zhry;', [])
        result = await client.query(`CREATE DATABASE zhry 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;`, [])
        result = await client.query(`DROP TABLE IF EXISTS zhry.zhry;`, [])
        client2 = await pool2.connect()
        result = await client2.query(`create table zhry( 
            id integer primary key generated always as identity, 
            name text, 
            jp text, 
            zh text DEFAULT '', 
            en text DEFAULT '', 
            type text, 
            time text, 
            jp_mecab text, 
            v_jp  tsvector, 
            v_zh  tsvector, 
            v_en  tsvector, 
            videoname text, 
            seasion text DEFAULT '', 
            audio bytea, 
            video bytea 
        );`, [])

        result = await client2.query(`CREATE extension pgroonga;
            CREATE INDEX pgroonga_jp_index ON zhry USING pgroonga (jp);
            CREATE INDEX pgroonga_jpmecab_index ON zhry USING pgroonga (jp_mecab);
            CREATE extension pg_jieba;
            CREATE INDEX animename_index ON zhry (name);
            CREATE INDEX videoname_index ON zhry (videoname);
        `)
        

        a = 1

        var rcs = []


        //[00:00.00]  分、秒、百分之一秒
      
        let matchs = rc.matchAll( new RegExp(String.raw`\[\d\d:\d\d\.\d\d\]`, 'g') )
        let arr = Array.from( matchs )
        for (let i = 0; i < arr.length; i++) {
      
          let match = arr[i]
          let begin = match.index
      
          let text = ''
          let endtime = ''
          if (i == arr.length -1) {
      
            text = rc.substring(begin)
      
          } else {
      
            let end = arr[i+1].index
            let endreal = end + arr[i+1][0].length
            endtime = rc.substring(end, endreal)
      
            text = rc.substring(begin, end)
      
          }
      
          let match2 = text.match( new RegExp(String.raw`\[(\d\d):(\d\d)\.(\d\d)\](.+)`, 's') )
          if (match2 != null) {
      
            let m = match2[1]   // minute
            let s = match2[2]   // second
            let ss = match2[3]  // 1% second
            let begin_time = `00:${m}:${s}.${ss}0`
      
            let text2 = match2[4]
            if (text2.replaceAll(/\s+/, '') == '') {
      
              a = 1
      
            } else {
      
              let j = ''
              let z = ''
              let arr_j = text2.split(/[（(]/)
              if (arr_j.length > 0) {
                j = arr_j[0].trim()
              } else {
                throw 'Error: LRC Format not correct. '
              }
      
              if (endtime != '') {
      
                let match_endtime = endtime.match( new RegExp(String.raw`\[(\d\d):(\d\d)\.(\d\d)\]`) )
                if (match_endtime != null) {
      
                  let med = match_endtime[1]   // minute
                  let sed = match_endtime[2]   // second
                  let ssed = match_endtime[3]  // 1% second
                  let end_time = `00:${med}:${sed}.${ssed}0`
      
                  // '00:01:12.960'  // 时 分 秒 毫秒
      
                  let arr_z = text2.split(/[)）\s]/)
                  if (arr_z.length > 0) {
      
                    if (arr_z[1] == undefined) {
                      a = 1
                    }
      
                    z = arr_z[1].trim()
                  } else {
                    throw 'Error: LRC Format not correct. '
                  }
      
      
                  rcs.push( {j, z, begin_time, end_time} )
      
                }
      
      
              }
      
            }
      
          }
      
        }

        a  = 1

        var vd = require('fs').createReadStream('F:/1.mp3')
        for (let i = 0; i < rcs.length; i++) {

          let item = rcs[i]
          let j = item.j
          let z = item.z
          let begin_time = item.begin_time
          let end_time = item.end_time
      
          let [au, ms1] = await new Promise(function (resolve) {
      
            var ffmpeg = require('fluent-ffmpeg')
        
            
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
              //let sr = outputBuffer.toString('utf8')
              let dir =  require('path').dirname(__filename)
              let fname = require('path').join(dir, 'tmp.mp3')
              require('fs').writeFileSync(fname, outputBuffer, 'binary')
              // use outputBuffer
              resolve([outputBuffer, ''])
            })
        
            ffmpeg(vd)//.output(au)
              .noVideo()
              .format('mp3')
              .outputOptions('-ss',begin_time) // '00:01:12.960'
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

          a = 1
      
        }


    } finally {
      client.release()
      if (client2 != null) {
        client2.release()
      }
      a = 1
    }

    a = 1

})().catch(e => console.error(e.message, e.stack))



/*



*/
