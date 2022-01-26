
let http = require('http')
let url = require('url')
let path = require('path')
let fs = require('fs')
let formurlencoded = require('form-urlencoded')
let formidable = require('formidable')

process.on('uncaughtException', function (err) {
  console.error(err)
})

let startPath = path.resolve(__dirname, '.')  // startup dir
Object.defineProperty(global, 'startPath', {  // global 是保留关键字，系统全局对象
  get() {
    return startPath
  }
})


let httpServer = http.createServer(async (req, res) => {

  if (req.method !== 'POST' && req.method !== 'GET') {
    return res.writeHead(200, {
      "Server": `servername`,
      "Access-Control-Allow-Origin": `*`,
      "Content-Type": `text/json`,
      'Access-Control-Allow-Headers': `content-type`,
      'Access-Control-Request-Method': `GET,POST`
    })
  }

  res.send = function (data) {
    if (typeof (data) === 'object') {
      data = JSON.stringify(data);
    }
    if (data === undefined || data === null) {
      data = JSON.stringify({
        status: 200, data: ''
      })
    }
    res.end(data.toString())
  }

  let form = new formidable.IncomingForm()

  let json = {
    keywd: '',
    name: '',
    seasion: '',
    episode: '',
    nthpage: '',
    nperpage: ''
  }

  let formurlencoded_json = formurlencoded(json)

  let apiBasename = ''
  if (req.url == '/') {
    req.url = '/search'
  }

  let apiPath = path.join(startPath, `/http/api${req.url}.js`)

  //判断文件是否存在
  if (!fs.existsSync(apiPath)) {
    res.writeHead(404)
    res.send('not found')
    return
  }

  let api = require(apiPath)
  //注入msg函数
  Object.defineProperty(api, "msg", {
    get() {
      return (status, data) => {
        return { status, data }
      }
    }
  })

  //接收到的参数
  let data = {}
  let result = ''

  //进入API
  result = api.handler(data)
  if (result instanceof Promise) {
    result = await result
  }

  return res.send(result)

})

let port = undefined || 80
httpServer.listen(port)
console.log(`server listening on ${port} port...`)





