
let http = require('http')
let url = require('url')
let path = require('path')
let fs = require('fs')

let startPath = path.resolve(__dirname, '.') // startup dir

process.on('uncaughtException', function (err) {
  console.error(err)
})

let httpServer = http.createServer( async (req, res) => {

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

  let apiPath = path.join(startPath, `/http/api/${apiBasename}.js`)  //`${startPath}/http/api/${apiBasename}.js`

  //判断文件是否存在
  if (!fs.existsSync(apiPath)) {
    res.writeHead(404, 'not found')
    res.send(404)
    return
  }

  let api = require(apiPath)

  //接收到的参数
  let data = {}
  let result = ''

  //进入API
  result = api.handler(data)
  if (result instanceof Promise) {
    result = await result
  }

  return res.end(result)

})

let port = undefined || 80
httpServer.listen(port)
console.log(`server listening on ${port} port...`)





