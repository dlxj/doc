
const {
    Worker,
    workerData
} = require('worker_threads');
const path = require('path');

async function creat(_path, param) {
    return new Promise(function (resolve, reject) {
        // const port = param.port
        let Pool = []
        let conn = param.conn

        const wk1 = new Worker(path.resolve(__dirname, _path));
        Pool.push(wk1)
        wk1.ref()
        wk1.postMessage(param);        

        const onWorkerMsg = async (res) => {

            let data = res
            if (data[0] == true) {
                wk1.terminate()
                Pool = []
                resolve(data[1])
            } else {
                
                // 任务未完成，给前端报告进度
                let msg = {

                }
                conn.__ws__.send(msg)
            }

        }

        wk1.on('message', onWorkerMsg)
    });


}


(async () => {



    const http = require('http');
    const path = require('path');
    const webSocket = require('ws');
    const uuid = require('uuid');


    //程序启动目录
    let startPath = path.resolve(__dirname, '.');

    const httpServer = http.createServer((req, res) => {

        if (req.method !== 'POST' && req.method !== 'GET') {
          //res.writeHead(200, global.conf.http.headers);
          res.end('');
          return;
        }
    })

    const wsServer = new webSocket.Server({
        server: httpServer
    })

    wsServer.on('connection', (ws, req) => {
        ws.ip = req.socket.remoteAddress;
        if (req.headers['x-forwarded-for'] != null) {
          ws.ip = req.headers['x-forwarded-for'].split(/\s*,\s*/)[0];
        }
        ws.isAlive = true;
        //客户端唯一ID
        ws.clientID = uuid.v4();
        ws.type = 'ws';
        ws.startTime = new Date().getTime();
  
        //构建ws对象
        function rewritews(res) {
            const send = res.send;
            res.send = (data) => {
              if (typeof (data) === 'object') {
                data = JSON.stringify(data);
              }
        
              send.apply(res, [data.toString()]);
            }
        }
        rewritews(ws);

        ws.on("message", async (data) => {
          let t1 = new Date().getTime();
          try {
            if (typeof (data) !== 'object') {
              data = JSON.parse(data);
            }
          } catch {
            return;
          }
  
  
          let apiPathName = '';
          let apiPath = '';
          let requestID = '';
          let paramsData = {};
          let dataSet = {};
          let aesKey = '';

          //普通websocket
          apiPath = `${startPath}/ws/api${data.api}.js`;
          apiPathName = data.api;
          requestID = data.requestID;
          paramsData = data.params;
  
          paramsData['__ip__'] = ws.ip;
          paramsData['__ws__'] = ws;
          const apiStat = fs.statSync(apiPath);
          const apiExists = apiStat.isFile() && getExtName(apiPath) === '.js';
          //判断请求API是否存在
          if (!apiExists) {
            ws.send("404");
            return;
          }

        });
  
        ws.on("close", (evt) => {
          ws.isAlive = false;
  
          if (ws.service === true) {

            console.log(`${ws.ip}断开service连接`);
          }
        });
  
      });
  

    let port = 321
    httpServer.listen(port)
    console.log(`lisen at ${port}`)

    let conn = null

    // let simir_data1 = await creat('./m.js', { conn })

    let a = 1

})()
