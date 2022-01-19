
let { Pool, Client } = require('pg')

// global.getconfig = 

// global.getDB = 

// global.defaultDB = global.getDB('postgres')

function getconfig(dbname) {
  return {
    user: 'postgres',
    password: 'et.com',
    host: 'xxx.77',
    port: '5432',
    database: dbname,
    ssl: false
  }
}

function getDB(dbname) {
  let config = getconfig(dbname)
  let pool = new Pool(config)
  let lib = {

    async query(sql, par, conn = null) {
      if (conn == null) {
        conn = await pool.connect()
      }

      //await client.query('select $1::text as name', ['brianc'])
      let result = await conn.query(sql, par)
      conn.release(true)

      return result

    },
    async release() {
      return await new Promise((resolve, reject) => {
        pool.end().then(() => {
          resolve(`pool has been release, db is ${config.database}`)
        })
      })

    },
    status() {
      let totalCount = pool.totalCount
      let idleCount = pool.idleCount
      let waitingCount = pool.waitingCount
      return { totalCount, idleCount, waitingCount }
    }

    /*
    pool.totalCount: int
      The total number of clients existing within the pool.

    pool.idleCount: int
      The number of clients which are not checked out but are currently idle in the pool.

    pool.waitingCount: int
      The number of queued requests waiting on a client when all clients are checked out. It can be helpful to monitor this number to see if you need to adjust the size of the pool.
    */

  }

  return lib
}

let defaultDB = getDB('postgres')

module.exports = {
  getconfig,
  getDB,
  defaultDB,
  arry_to_buffer: function (array) {  // Uint8Array -> buffer
    // let buffer = new ArrayBuffer(array.length)
    // array.map(function(value, i) {buffer[i] = value})
    let buffer = array.buffer.slice(array.byteOffset, array.byteLength + array.byteOffset)
    return  buffer
  }
}

/*

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
