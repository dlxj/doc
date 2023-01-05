
// const {
//   Worker,
//   workerData
// } = require('worker_threads');
const path = require('path');

// async function creat(_path, params) {
//   return new Promise(function (resolve, reject) {
//     // const port = param.port
//     let Pool = []
//     let { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params
//     //let conn = param.conn

//     const wk1 = new Worker(path.resolve(__dirname, _path));
//     Pool.push(wk1)
//     wk1.ref()
//     wk1.postMessage(params);

//     const onWorkerMsg = async (res) => {

//       let data = res
//       if (data[0] == true) {
//         wk1.terminate()
//         Pool = []
//         resolve(data[1])
//       } else {

//         // 任务未完成，给前端报告进度
//         let msg = {

//         }
//         // __ws__.send(msg)
//       }

//     }

//     wk1.on('message', onWorkerMsg)
//   });


// }

function getExtName(name) {
  return path.extname(name).toLowerCase();
}


(async () => {

  let apiCache = {}
  function getAPI(pth) {
    if (apiCache[pth] !== undefined) {
      return apiCache[path];
    }
    let api = require(pth);
    if (typeof (api) === 'function') {
      api = new api();
    }
    apiCache[require.resolve(pth)] = api;
    return api;
  }

  const http = require('http');
  const path = require('path');
  const webSocket = require('ws');
  const uuid = require('uuid');
  const fs = require('fs');


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

  wsServer.on('connection', async (ws, req) => {
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

      if (data instanceof Buffer) {
        data = data.toString()
      }

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

      const apiStat = fs.statSync(apiPath);
      const apiExists = apiStat.isFile() && getExtName(apiPath) === '.js';
      //判断请求API是否存在
      if (!apiExists) {
        ws.send("404");
        return;
      }

      let api = getAPI(apiPath)

      //参数验证
      paramsData = require('./lib/paramVerify')(api.params, paramsData);
      paramsData['__ip__'] = ws.ip;
      paramsData['__ws__'] = ws;

      //进入API
      let result = api.handler(paramsData);
      if (result instanceof Promise) {
          result = await result;
      }


      // const {
      //   Worker,
      //   workerData
      // } = require('worker_threads');
      // const path = require('path');
      
      // async function creat(_path, params) {
      //   return new Promise(function (resolve, reject) {
      //     // const port = param.port
      //     let Pool = []
      //     var { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params
      //     //let conn = param.conn
      
      //     const wk1 = new Worker(path.resolve(__dirname, _path));
      //     Pool.push(wk1)
      //     wk1.ref()
      //     //wk1.postMessage(params);
      //     wk1.postMessage('');
      //     const onWorkerMsg = async (res) => {

      //       if (typeof(res) == 'string') {
      //         res = JSON.parse(res)
      //       }
      
      //       let data = res
      //       if (data[0] == true) {
      //         wk1.terminate()
      //         Pool = []
      //         resolve(data[1])
      //       } else {
      
      //         // 任务未完成，给前端报告进度
      //         params.__ws__.send({ msg:'not done yet' })
      //       }
      
      //     }
      
      //     wk1.on('message', onWorkerMsg)
      //   });
      
      
      // }

      // let simir_data1 = await creat('./m.js', paramsData)

      // let worker = require('./lib/worker.js')
      // let simir_data1 = await worker.create('../m.js', paramsData) // 相对路径是相对 worker.js 所在目录说的



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

  // let conn = null

  // let simir_data1 = await creat('./m.js', { conn })

  // let a = 1

})()

