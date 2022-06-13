
// 推流服务器 前端通过ws 请求触发，ws 请求触发后，向 pmserver 发起 http 请，pmserver 调用 ffmpeg 发起http://localhost:9999/push/id 的请求，把数据传回这里, 
// 这里再把数据广播到前端 
// ffmpeg -re -i 1.mkv -q 0 -f mpegts -codec:v mpeg1video -s 1000x600 -r 30 http://localhost:9999/push/test   // 持续推流





const http = require('http')
const ws = require('ws')

let bent = require('bent')
let formurlencoded = require('form-urlencoded')

const prefix = `[JSMpeg-Server] `

class Server {
  attachListener(source) {
    const id = source.id
    if (id in this.sessions) {
      this.sessions[id].add(source)
    } else {
      const set = (this.sessions[id] = new Set())
      set.add(source)
    }

    console.log(`${prefix}attach new Session: ${id}`)
  }

  detachListener(source) {
    const id = source.id
    if (id in this.sessions && this.sessions[id].has(source)) {
      this.sessions[id].delete(source);
      console.log(`${prefix}detach new Session: ${id}`)
    }
  }

  broadcast(id, chunk) {
    if (id in this.sessions) {
      const sess = this.sessions[id].values()
      for (const s of sess) {
        s.onMessage(chunk)
      }
    }
  }

  constructor(port) {
    this.sessions = {}

    this.server = http
      .createServer((req, res) => {
        const url = req.url || '/'

        if (!url.startsWith('/push/')) {
          res.statusCode = 404
          res.write('Not found')
          res.end()
          return
        }

        const id = url.slice(6)

        console.log(`${prefix}Stream connected: ${id}`)

        res.connection.setTimeout(0)

        req.on('data', (c) => {
          this.broadcast(id, c)
        })

        req.on('end', () => {
          console.log(`${prefix}Stream closed: ${id}`)
        })
      })
      .listen(port, () => {
        console.log(
          `${prefix}Listening for incomming MPEG-TS Stream on http://127.0.0.1:${port}`,
        )
      })

    /**
     * 使用 webSocket 拉取流
     */
    this.wss = new ws.Server({
      server: this.server,
      verifyClient: (info, cb) => {
        if (info.req.url && info.req.url.startsWith('/pull')) {
          cb(true)
        } else {
          cb(false, undefined, 'use /pull/{id}')
        }
      },
    })

    // 新连接
    this.wss.on('connection', async (client, req) => {
      const url = req.url
      const id = url.slice(6)

      console.log(`${prefix}new player attached: ${id}`)

      let buzy = false
      const listener = {
        id,
        onMessage: (data) => {
          // 推送
          if (buzy) {
            return
          }

          buzy = true;
          client.send(data, { binary: true }, function ack() {
            buzy = false
          })
        },
      }

      this.attachListener(listener)

      client.on('close', () => {
        console.log(`${prefix} player dettached: ${id}`)
        this.detachListener(listener)
      })


      let host = `127.0.0.1:8880`
      let url2 = `http://${host}`

      let json = {
          id: id
      }

      let formurlencoded_json = formurlencoded(json)

      let post = bent(url2, 'POST', 'json', 200)
      // let response = await post('/pushsteam', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded'})
      post('/pushsteam', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded'})

      // if (response.status == 200) {
      //     return [ response.data, '']
      // } else {
      //     return [null, response.msg]
      // }

      // 

      // let { execa } = await import('execa')

      // let cmd = `ffmpeg -re -i "E:\\1.mkv" -ss 00:00:00.000 -to 00:00:03.000 -q 0 -f mpegts -codec:v mpeg1video -s 1000x600 -r 30 http://localhost:9999/push/test`
      // // let cmd = `ffmpeg -re -i "E:\\1.mkv" -ss 00:00:00.000 -to 00:00:03.000 -q 0 -f mpegts -codec:v mpeg1video -s 1000x600 -r 30 http://localhost:9999/push/test`  // write stdout

      // let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
      // //childProcess.stdout.pipe(process.stdout)  // don't print to screen
      // let { stdout } = childProcess

      // let a = 1

    })
  }
}

new Server(9999);


