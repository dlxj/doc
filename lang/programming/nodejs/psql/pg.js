

/*


const { Pool, Client } = require('pg')
const connectionString = 'postgresql://postgres:echodict.com@111.229.53.195:5432/anime'
const pool = new Pool({
  connectionString,
})

*/



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

    var pool = new Pool(config)
    var client = await pool.connect()
    try {
      var result = await client.query('select $1::text as name', ['brianc'])
      console.log('hello from', result.rows[0])
    } finally {
      client.release()
    }
})().catch(e => console.error(e.message, e.stack))