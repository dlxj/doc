
(async () => {

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
        a = 1


    //   //var result = await client.query('select $1::text as name', ['brianc'])
    //   //var result = await client.query(`select id, en, zh, type from anime where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;`, ['黑白'])
    //   var result = await client.query(`SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ $1 ORDER BY RANDOM() limit 3;`, ['大']) // ここ
    //   //var result = await client.query(`SELECT id, jp, zh, time FROM anime limit $1;`, ['1'])
    //   console.log('hello from', result.rows)
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


            cur.execute("DROP TABLE IF EXISTS anime;")
            #  id serial primary key, \
            cur.execute("create table anime( \
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
            );")
            #cur.execute("CREATE TABLE audio(id SERIAL PRIMARY KEY, data BYTEA);")

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            cur.execute("CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);")

            cur.execute("create extension pg_jieba;")

            cur.execute("CREATE INDEX animename_index ON anime (name);")
            cur.execute("CREATE INDEX videoname_index ON anime (videoname);")

*/
