

let { default: libdir } = await import('./dir.mjs')

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

let { default: libmecab } = await import('./mecab.mjs')
await libmecab.init()
//let [hirass, msgg] = await libmecab.haras('騙して勝つ')
let [hirass, msgg] = await libmecab.haras("お願いします! ピカピカ! ")  // crash

let { default: libff } = await import('./ffmpeg.mjs')
// let { srt: srt_jpp, msg: msg_jpp } = await libff.extractSubtitle("E:\\videos\\anime\\Pokemon\\S14\\Best_Wishes\\06.mkv", 'srt', 2)

let { default: libsrt } = await import('./srt.mjs')
import fs from 'fs'

let { default: libpg } = await import('./pgsql.mjs')
// let re = await libpg.defaultDB.query('select $1::text as name', ['brianc'])

let name = 'Pokemon_Best_Wishes'
let seasion = 'S14'


let re = await libpg.defaultDB.query('DROP DATABASE IF EXISTS temp;', [])
re = await libpg.defaultDB.query(`
    CREATE DATABASE temp 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `, [])

let tempDB = libpg.getDB('temp')
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

for (let j = 0; j < mkvs.length; j++) {

    let vdpath = mkvs[j]

    let { srt: srt_jp, msg: msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream
    srt_jp = libsrt.clean(srt_jp)
    //fs.writeFileSync(`tmp.srt`, srt_jp, { encoding: 'utf8' })
    let jps = libsrt.parse(srt_jp)

    let { srt: srt_zhs, msg: msg_zhs } = await libff.extractSubtitle(vdpath, 'srt', 0)
    srt_zhs = libsrt.clean(srt_zhs)
    let zhss = libsrt.parse(srt_zhs)
    let subtitles = libsrt.merge(jps, zhss)
    

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

        let { au: audio } = await libff.extractAudio(vdpath, 'mp3', begintime, endtime)


        let video = Buffer.from('')  // empty now

        re = await tempDB.query(`
    INSERT INTO pokemon (name, seasion, jp, zh, time, jp_ruby, v_jp, v_zh, audio, video)
    VALUES
     ( $1, $2, $3, $4, $5, $6, to_tsvector($7), to_tsvector($8), $9, $10 );
     `, [name, seasion, jp, zh, item.begintime, ruby, jp_ng, zh_ng, audio, video])


        // re = await tempDB.query(`SELECT audio FROM pokemon limit 1;`)
        // let au = re.rows[0].audio  //  Uint8Array
        // au = Buffer.from(au)

        console.log(`${i + 1}/${subtitles.length} subs ｜ ${j + 1} / ${mkvs.length} mkvs `)

    }

}


re = await tempDB.query(`SELECT jp_ruby, jp, zh, audio FROM pokemon WHERE v_jp @@ to_tsquery($1);`, ['地方'])

let jp_ruby = re.rows[0].jp_ruby
let jp = re.rows[0].jp
let zh = re.rows[0].zh
let au = re.rows[0].audio  //  Uint8Array
au = Buffer.from(au)

let sta1 = libpg.defaultDB.status()
let sta2 = tempDB.status()

re = await tempDB.release()
re = await libpg.defaultDB.release()

console.log(`jp_ruby: ${jp_ruby}`)

console.log('hi,,,')


import { execa } from 'execa'
if (process.platform != 'win32') {  // 停止pm2 的执行，否则会无限重启不会结束的
  
    let cmd = `pm2 stop insertpokemon`
    console.log(`execte command: ${cmd}`)
    let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
    //childProcess.stdout.pipe(process.stdout)  // don't print to screen
    let { stdout } = await childProcess
    
    console.log(stdout)
}





/*

cp /mnt/Downloads/宠物小精灵BW双语/*第0[0-9]*.mkv /mnt/videos/anime/Pokemon/S14/Best_Wishes

*/