
// https://juejin.cn/post/6972006652631318564
// https://depth-first.com/articles/2019/01/17/debugging-es-modules-with-mocha-in-vs-code/
// https://github.com/sindresorhus/execa
// https://jestjs.io/docs/ecmascript-modules
// https://gist.github.com/Drubo/1574291
// https://github.com/sindresorhus/execa
// https://github.com/Kagami/ffmpeg.js/
// https://www.postgresql.org/docs/12/functions-textsearch.html
// https://gist.github.com/srujandeshpande/3b79a2e7809548beea32e9af7597ddb3
// https://github.com/ColinEberhardt/ffmpeg-wasm-streaming-video-player/blob/main/app.js

(async () => {

  let libdir = require('./dir')

  let root = ''
  if (process.platform == 'win32') {
    root = String.raw`E:\videos\anime`
  } else if (process.platform == 'linux') {
    root = String.raw`/mnt/videos/anime`
  } else if (process.platform == 'darwin') {
    root = String.raw`/Users/olnymyself/Downloads/videos/anime`
  } else {
    throw 'unknow os type.'
  }

  let mkvs = libdir.allmkv(root, 'Pokemon')
  let fs = require('fs')
  let ff = require('./ffmpeg')
  let libsrt = require('./srt')
  let libmecab = require('./mecab')
  await libmecab.init()
  let pg = require('./pgsql')

  let name = 'Pokemon_Best_Wishes'
  let seasion = 'S14'

  for (let j = 0; j < mkvs.length; j++) {

    let vdpath = mkvs[j]
    //   vdpath = String.raw`/mnt/videos/anime/Pokemon/S14/Best_Wishes/06.mkv`


    let { default: libff } = await import('./ffmpeg.mjs')
    let { srt: srt_jp, msg: msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream
    srt_jp = libsrt.clean(srt_jp)
    //fs.writeFileSync(`tmp.srt`, srt_jp, { encoding: 'utf8' })
    let jps = libsrt.parse(srt_jp)

    // let [srt_zhs, ms2] = await ff.extractSubtitle(vdpath, 'srt', 0) // the nth subtitle stream
    // srt_zhs = srt_zhs.toString('utf8')
    let { srt: srt_zhs, msg: msg_zhs } = await libff.extractSubtitle(vdpath, 'srt', 0)
    srt_zhs = libsrt.clean(srt_zhs)
    let zhss = libsrt.parse(srt_zhs)
    let subtitles = libsrt.merge(jps, zhss)
    //let { au: axx} = await libff.extractAudio(vdpath, 'mp3', '00:00:01.960', '00:00:05.660')

    a = 1
    
    let re = await pg.defaultDB.query('select $1::text as name', ['brianc'])
    re = await pg.defaultDB.query('DROP DATABASE IF EXISTS temp;', [])
    re = await pg.defaultDB.query(`
    CREATE DATABASE temp 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `, [])

    let tempDB = pg.getDB('temp')
    re = await tempDB.query(`
    CREATE TABLE pokemon (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        zh text DEFAULT '', 
        en text DEFAULT '', 
        type text, 
        time text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector, 
        v_zh  tsvector, 
        v_en  tsvector, 
        videoname text, 
        seasion text DEFAULT '', 
        audio bytea, 
        video bytea 
      )
    `)

    re = await tempDB.query("create extension pgroonga;")
    re = await tempDB.query("create extension pg_jieba;")
    re = await tempDB.query("CREATE INDEX pgroonga_jp_index ON pokemon USING pgroonga (jp);")
    re = await tempDB.query("CREATE INDEX pgroonga_jpmecab_index ON pokemon USING pgroonga (jp_mecab);")
    re = await tempDB.query("CREATE INDEX animename_index ON pokemon (name);")
    re = await tempDB.query("CREATE INDEX videoname_index ON pokemon (videoname);")

    console.log(`# begin insert...`)
    for (let i = 0; i < subtitles.length; i++) {  // subtitles.length;

      let item = subtitles[i]

      let begintime = item.begintime.replace(',', '.')  // for ffmpeg
      let endtime = item.endtime.replace(',', '.')
      let jp = item.jp
      let zh = item.zh

      let [hiras, msg] = await libmecab.haras(jp)
      if (hiras == null) {
        throw `Error: segment fail. ${msg}`
      }

      let ruby = hiras.ruby
      let hiragana = hiras.hiragana

      let hiragana_ng = libsrt.NG(hiragana)
      let jp_ng = libsrt.NG(jp)
      let zh_ng = libsrt.NG(zh)

      jp_ng = (jp_ng.concat(hiragana_ng)).join(' ')  // for fulltext search All in one
      zh_ng = zh_ng.join(' ')
      hiragana_ng = hiragana_ng.join(' ')

      //let [audio, ms1] = await ff.extractAudio(vdpath, 'mp3', begintime, endtime)

      let { au: audio } = await libff.extractAudio(vdpath, 'mp3', begintime, endtime)
      if (audio == null) {
        throw `au is null. ${vdpath} ${begintime}`
      }

      require('fs').writeFileSync('tmp.mp3', audio )

      let video = Buffer.from('')  // empty now

      re = await tempDB.query(`
    INSERT INTO pokemon (name, seasion, jp, zh, time, jp_ruby, v_jp, v_zh, audio, video)
    VALUES
     ( $1, $2, $3, $4, $5, $6, to_tsvector($7), to_tsvector($8), $9, $10 );
     `, [name, seasion, jp, zh, item.begintime, ruby, jp_ng, zh_ng, audio, video])


      // re = await tempDB.query(`SELECT audio FROM pokemon limit 1;`)
      // let au = re.rows[0].audio  //  Uint8Array
      // au = Buffer.from(au)

      console.log(`${i + 1}/${subtitles.length}`)

    }

  }

  re = await tempDB.query(`SELECT jp_ruby, jp, zh, audio FROM pokemon WHERE v_jp @@ to_tsquery($1);`, ['地方'])

  let jp_ruby = re.rows[0].jp_ruby
  let jp = re.rows[0].jp
  let zh = re.rows[0].zh
  let au = re.rows[0].audio  //  Uint8Array
  au = Buffer.from(au)

  let sta1 = pg.defaultDB.status()
  let sta2 = tempDB.status()

  re = await tempDB.release()
  re = await pg.defaultDB.release()


  //fs.writeFileSync(`subtitles.txt`, JSON.stringify(subtitles), {encoding:'utf8'})

  console.log('hi,,')

})()


/*

const execa = require('execa')

const subprocess = execa('echo', ['foo'])
subprocess.stdout.pipe(process.stdout)
;(async () => {
  const { stdout } = await subprocess
  console.log('child output:', stdout)
})()

*/
