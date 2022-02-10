
let { Pool, Client } = require('pg')

let config = require('../../config.js')

function getconfig(dbname) {
  return config[dbname]
}

function getDB(dbname) {

  let config = getconfig(dbname)
  let pool = new Pool(config)
  let lib = {

    async query(sql, par, conn = null) {

      sql = buildSQL(sql, par)  // 替换形参

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

  }

  return lib
}

let defaultDB = getDB('defaultDB')

// 参数替换，形参 $(parmName) 替换成实参
function buildSQL(sql, par) {
  const arr = []
  const parNames = sql.match(/\$\([0-9a-zA-Z\_]{1,9999}?\)/g)
  if (parNames != null) {
    for (let pName of parNames) {
      //替换参数名
      sql = sql.replace(pName, '?')
      //转换参数名
      pName = pName.replace(/\$\(([[0-9a-zA-Z\_]{1,9999}?)\)/g, '$1')
      arr.push(par[pName])
    }
  }
  return { sql: sql, params: arr }
}

module.exports = {
  getDB,
  defaultDB
}