
(async () => {

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
    re = await tempDB.query(    `
    CREATE TABLE bookdata (
        id  serial NOT NULL PRIMARY KEY,
        info json NOT NULL
      )
    `)
    re = await tempDB.query(`CREATE INDEX bookdata_fts ON bookdata USING gin((to_tsvector('english',info->'title')));`)
    
    re = await tempDB.query(`
    INSERT INTO bookdata (info)
    VALUES
     ( '{ "title": "The Tattooed Duke", "items": {"product": "Diaper","qty": 24}}'),
     ( '{ "title": "She Tempts the Duke", "items": {"product": "Toy Car","qty": 1}}'),
     ( '{ "title": "The Duke Is Mine", "items": {"product": "Toy Train","qty": 2}}'),
     ( '{ "title": "What I Did For a Duke", "items": {"product": "Toy Train","qty": 2}}'),
     ('{ "title": "King Kong", "items": {"product": "Toy Train","qty": 2}}');
     `)
    
     re = await tempDB.query(`
     SELECT info -> 'title' as title FROM bookdata
     WHERE to_tsvector('english',info->'title') @@ to_tsquery('Duke');
     `)

    let sta1 = pg.defaultDB.status()
    let sta2 = tempDB.status()

    re = await tempDB.release()
    re = await pg.defaultDB.release()

    a = 1
})()


/*

sql = $"SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ '{keywd}' ORDER BY RANDOM() limit 3;";  // 不用系统的分司插件，手动分词（用NGram）


sql = f"""insert into anime(name, seasion, jp, time, jp_mecab, zh, v_zh, videoname, audio, video) values('{animename}', '{seasion}','{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'), '{videoname}', %s, %s);"""
sql = $"SELECT id, jp, zh, time FROM anime WHERE v_zh @@  to_tsquery('jiebacfg', '{keywd}') ORDER BY RANDOM() limit 3;";  // 系统分词


to_tsvector('fat cats ate rats') @@ to_tsquery('cat & rat')

*/
