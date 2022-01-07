
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
    // let pg = require('./pgsql')

    // let re = await pg.query('select $1::text as name', ['brianc'])
    // re = await pg.exec('DROP DATABASE IF EXISTS temp;', [])
    // re = await pg.exec(`CREATE DATABASE temp 
    // WITH OWNER = postgres 
    // ENCODING = 'UTF8' 
    // TABLESPACE = pg_default 
    // CONNECTION LIMIT = -1 
    // TEMPLATE template0;
    // `, [])

    


    a = 1
})()




/*

"create table anime( \
                id integer primary key generated always as identity, \
                name text, \
                jp text, \
                zh text DEFAULT '', \
                en text DEFAULT '', \
                type text, \
                time text, \
                jp_mecab text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector, \
                videoname text, \
                seasion text DEFAULT '', \
                audio bytea, \
                video bytea \
            );"

*/