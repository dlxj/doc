
let { Pool, Client } = require('pg')

// global.getconfig = 

// global.getDB = 

// global.defaultDB = global.getDB('postgres')

function getconfig (dbname) {
  return {
    user: 'postgres',
    password: 'echodict.com',
    host: '209.141.34.77',
    port: '5432',
    database: dbname,
    ssl: false
  }
}

function getDB (dbname) {
  let config = getconfig(dbname)
  let pool = new Pool(config)
  let lib = {

    async query(sql, par, conn = null) {
      if (conn == null) {
        conn = await pool.connect()
      }

      //await client.query('select $1::text as name', ['brianc'])
      let result = await conn.query(sql, par)
      return result

    }
  }

  return lib
}

let defaultDB = getDB('postgres')

module.exports = {
  getconfig,
  getDB,
  defaultDB
}
