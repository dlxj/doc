
(async () => {

    var MeCab = new require('mecab-async')
    let mecab = new MeCab()

    mecab.parse('いつもニコニコあなたの隣に這い寄る混沌ニャルラトホテプです！', function(err, result) {
      if (err) throw err
      console.log(result)
    })

    const { Pool, Client } = require('pg')

    const config = {
        user: 'postgres',
        password: 'echodict.com',
        host: '209.141.34.77',
        port: '5432',
        database: 'anime',
        ssl: false
    }

    var pool = new Pool(config)
    var client = await pool.connect()
    try {
      //var result = await client.query('select $1::text as name', ['brianc'])
      //var result = await client.query(`select id, en, zh, type from anime where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;`, ['黑白'])
      var result = await client.query(`SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ $1 ORDER BY RANDOM() limit 3;`, ['ここ'])
      console.log('hello from', result.rows)
    } finally {
      client.release()
      a = 1
    }
})().catch(e => console.error(e.message, e.stack))

