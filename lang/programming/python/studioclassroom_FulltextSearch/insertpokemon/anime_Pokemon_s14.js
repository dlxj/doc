

// https://github.com/Kagami/ffmpeg.js/

(async () => {

    let fs = require('fs')
    let ff = require('./ffmpeg')
    let libsrt = require('./srt')
    let libmecab = require('./mecab')

    await libmecab.init()


    let pg = require('./pgsql')
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
        id  serial NOT NULL PRIMARY KEY,
        info json DEFAULT NULL,
        audio bytea DEFAULT NULL
      )
    `)
    // re = await tempDB.query(`CREATE INDEX bookdata_fts ON bookdata USING gin((to_tsvector('english',info->'title')));`)

    // re = await tempDB.query(`
    // INSERT INTO bookdata (info)
    // VALUES
    //  ( '{ "title": "The Tattooed Duke", "items": {"product": "Diaper","qty": 24}}'),
    //  ( '{ "title": "She Tempts the Duke", "items": {"product": "Toy Car","qty": 1}}'),
    //  ( '{ "title": "The Duke Is Mine", "items": {"product": "Toy Train","qty": 2}}'),
    //  ( '{ "title": "What I Did For a Duke", "items": {"product": "Toy Train","qty": 2}}'),
    //  ('{ "title": "King Kong", "items": {"product": "Toy Train","qty": 2}}');
    //  `)

    //  re = await tempDB.query(`
    //  SELECT info -> 'title' as title FROM bookdata
    //  WHERE to_tsvector('english',info->'title') @@ to_tsquery('Duke');
    //  `)



    // let [hiras, msg] = await libmecab.haras('感じ取れ')

    // console.log( hiras, msg )

    let vdpath = String.raw`F:\videos\anime\Pokemon\S14\Best_Wishes\06.mkv`


    //let [audio, ms1] = await ff.extractAudio(vdpath, 'mp3', `00:00:00.000`, `00:00:07.520`)  // output type, begintime, endtime

    //let [audio2, ms2] = await ff.extractAudio(vdpath, 'mp3', `00:00:00.000`, `00:00:07.520`)  // output type, begintime, endtime

    //a = 1



    let [srt_jp, ms3] = await ff.extractSubtitle(vdpath, 'srt', 2) // the nth subtitle stream
    srt_jp = srt_jp.toString('utf8')
    srt_jp = libsrt.clean(srt_jp)
    fs.writeFileSync(`tmp.srt`, srt_jp, { encoding: 'utf8' })

    let jps = libsrt.parse(srt_jp)

    let [srt_zhs, ms2] = await ff.extractSubtitle(vdpath, 'srt', 0) // the nth subtitle stream
    srt_zhs = srt_zhs.toString('utf8')
    srt_zhs = libsrt.clean(srt_zhs)

    let zhss = libsrt.parse(srt_zhs)

    let subtitles = libsrt.merge(jps, zhss)

    for (let i = 0; i < subtitles.length; i++) {

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

        let [audio, ms1] = await ff.extractAudio(vdpath, 'mp3', begintime, endtime)

        re = await tempDB.query(`
    INSERT INTO pokemon (audio)
    VALUES
     ( $1 );
     `, [audio])

        re = await tempDB.query(`SELECT audio FROM pokemon limit 1;`)
        let au = re.rows[0].audio  //  Uint8Array
        au = Buffer.from(au)
        //let buf2 = pg.arry_to_buffer(au)

        a = 1

    }

    let sta1 = pg.defaultDB.status()
    let sta2 = tempDB.status()

    re = await tempDB.release()
    re = await pg.defaultDB.release()


    //fs.writeFileSync(`subtitles.txt`, JSON.stringify(subtitles), {encoding:'utf8'})

    a = 1

    // let pg = require('./pgsql')

    // let re = await pg.defaultDB.query('select $1::text as name', ['brianc']) 
    // re = await pg.defaultDB.query('DROP DATABASE IF EXISTS temp;', [])
    // re = await pg.defaultDB.query(`
    // CREATE DATABASE temp 
    //     WITH OWNER = postgres 
    //     ENCODING = 'UTF8' 
    //     TABLESPACE = pg_default 
    //     CONNECTION LIMIT = -1 
    //     TEMPLATE template0;
    // `, [])

    // let tempDB = pg.getDB('temp')
    // re = await tempDB.query(    `
    // CREATE TABLE bookdata (
    //     id  serial NOT NULL PRIMARY KEY,
    //     info json NOT NULL
    //   )
    // `)
    // re = await tempDB.query(`CREATE INDEX bookdata_fts ON bookdata USING gin((to_tsvector('english',info->'title')));`)

    // re = await tempDB.query(`
    // INSERT INTO bookdata (info)
    // VALUES
    //  ( '{ "title": "The Tattooed Duke", "items": {"product": "Diaper","qty": 24}}'),
    //  ( '{ "title": "She Tempts the Duke", "items": {"product": "Toy Car","qty": 1}}'),
    //  ( '{ "title": "The Duke Is Mine", "items": {"product": "Toy Train","qty": 2}}'),
    //  ( '{ "title": "What I Did For a Duke", "items": {"product": "Toy Train","qty": 2}}'),
    //  ('{ "title": "King Kong", "items": {"product": "Toy Train","qty": 2}}');
    //  `)

    //  re = await tempDB.query(`
    //  SELECT info -> 'title' as title FROM bookdata
    //  WHERE to_tsvector('english',info->'title') @@ to_tsquery('Duke');
    //  `)

    // let sta1 = pg.defaultDB.status()
    // let sta2 = tempDB.status()

    // re = await tempDB.release()
    // re = await pg.defaultDB.release()

    console.log(111)

})()


/*

<font face="方正粗圆_GBK" size="30"><b>イッシュ地方で
最初のジム戦に挑戦したサトシ。
</b></font>

*/
