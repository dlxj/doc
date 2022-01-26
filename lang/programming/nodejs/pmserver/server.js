
let http = require('http')
let url = require('url')
let path = require('path')

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

  // if (req.protocol == undefined) {
  //   req.protocol = 'http'
  // }

  let apiBasename = ''
  if (req.url == '/') {
    apiBasename = 'search'
  }

  const apiPath =  path.join(startPath, `/http/api/${apiBasename}.js`)  //`${startPath}/http/api/${apiBasename}.js`



  return res.end( 'ok' )

})

let port = undefined || 80
httpServer.listen(port)
console.log(`server listening on ${port} port...`)





