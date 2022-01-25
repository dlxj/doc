
let http = require('http')

let startPath = path.resolve(__dirname, '.') // startup dir

process.on('uncaughtException', function (err) {
  console.error(err)
})

let httpServer = http.createServer((req, res) => {

  if (req.method !== 'POST' && req.method !== 'GET') {
    return res.writeHead(200, {
      "Server": `servername`,
      "Access-Control-Allow-Origin": `*`,
      "Content-Type": `text/json`,
      'Access-Control-Allow-Headers': `content-type`,
      'Access-Control-Request-Method': `GET,POST`
    })
  }

  if (req.protocol == undefined) {
    req.protocol = 'http'
  }

  let baseURL =  req.protocol + '://' + req.headers.host + '/'
  let reqUrl = new URL(req.url,baseURL)

  return res.end( 'ok' )

})

let port = undefined || 80
httpServer.listen(port)
console.log(`server listening on ${port} port...`)





