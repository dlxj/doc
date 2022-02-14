
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

      let [sql2, params] = buildSQL(sql, par)  // 替换形参

      if (conn == null) {
        conn = await pool.connect()
      }

      //await client.query('select $1::text as name', ['brianc'])
      let result = await conn.query(sql2, params)
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

// 参数替换，形参替换成实参
function buildSQL(sql, par) {

  // 先处理掉 '$$(dbname)' 这样的形参，它是表示字面替换
  for (let [key, value] of Object.entries(par)) {

    sql = sql.replace(new RegExp(new RegExp(String.raw`\$\$\(${key}\)`,'g')), value)

  }

  const params = []
  const parNames = sql.match(/\$\([0-9a-zA-Z\_]{1,9999}?\)/g)  // 在sql 语句中匹配所有这样的形参： '$(dbname)' ，返回值是形参的数组
  if (parNames != null) {
      for (let i = 0; i < parNames.length; i++) {
          let pName = parNames[i]

          //sql.indexOf('$$')

          //替换参数名
          sql = sql.replace(pName, `$${i+1}`)
          //转换参数名
          pName = pName.replace(/\$\(([[0-9a-zA-Z\_]{1,9999}?)\)/g, '$1')
          params.push(par[pName])
      }
  }
  return [sql, params]  // { sql: sql, params: arr }
}

module.exports = {
  getDB
}


// defaultDB
// let sql = `
// DROP DATABASE IF EXISTS $$(dbname);
// `
// let par = {'dbname':'temp'}

// buildSQL(sql, par)





