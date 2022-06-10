
( async () => {

  let http = require('http')
  let url = require('url')
  let path = require('path')
  let fs = require('fs')
  let formurlencoded = require('form-urlencoded')
  let formidable = require('formidable')
  let rd = require('rd')
  let ws = require('ws')


  //let re = await pg.defaultDB.query('select $1::text as name', ['brianc'])

  process.on('uncaughtException', function (err) {
    console.error(err)
  })

  await require('./init.js')()

  let isDebug = global.config.debug
  let headers = global.config.http.headers

  let httpServer = http.createServer(async (req, res) => {

    if (req.method !== 'POST' && req.method !== 'GET') {
      return res.writeHead(200, headers)
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

    //接收到的参数
    let data = {}
    //填充URL参数到data
    if (req.method == 'GET') {
      let query = url.parse(req.url, true).query
      Object.assign(data, query)
      if (req.url.indexOf('?') != -1) {
        let url = req.url.split('?')
        req.url = url[0]
      }
    }
    //填充post数据到data里
    if (req.method == 'POST') {
      let form = new formidable.IncomingForm()
      await new Promise((resolve, reject) => {
        form.parse(req, async (err, body, files) => {
          if (err) throw err
          Object.assign(data, body)
          resolve()
        })
      })
    }

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

    //判断api 是否存在
    let apiPath = path.join(global.startDir, `/http/api${req.url}.js`)
    if (!(apiPath in global.apiCache)) {
      res.writeHead(404, headers)
      res.send('not found')
      return
    }

    let api = global.apiCache[apiPath]

    //参数验证
    data = require('./lib/paramVerify.js')(api.params, data)
    data['__ip__'] = req.ip
    data['__request__'] = req
    data['__response__'] = res

    //进入API
    let result = api.handler(data)
    if (result instanceof Promise) {   // async 函数是 Promise的实例
      result = await result
    }

    if (result.data.name == 'cb') {  // 对方要求回调
      return result.data(res)
    }

    //
    // 奇怪的问题：这样进入 service, 在service 的handler 里面的 this 对象是有 services 的，
    // 但是如果是从 api 里面用 await this.services.search( { keywd } ) 进入service 的handler ，里面的this 对象就没有 services  了 ！
    // 作为替代方案，当service 需要调用其它接口的时侯只能用 await global.services.user.getuser( { userid:'' } ) 这样子
    //
    //进入Service
    // let servicePath = path.join(global.startDir, `/service/api${req.url}.js`)
    // let service = global.serviceCache[servicePath]
    // let result2 = await service.handler(data)

    
    res.writeHead(200, headers)
    return res.send(result)

  })

  let port = isDebug ? global.config.http.port_debug : global.config.http.port || 80
  httpServer.listen(port)
  console.log(`server listening on ${port} port...`)

})()
