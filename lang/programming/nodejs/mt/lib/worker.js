
const { Worker,workerData } = require('worker_threads');
const path = require('path');

module.exports = {
  
    async create(_path, params) {
        return new Promise(function (resolve, reject) {
          // const port = param.port
          let Pool = []
          var { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params
          //let conn = param.conn
      
          const wk1 = new Worker(path.resolve(__dirname, _path));
          Pool.push(wk1)
          wk1.ref()
          //wk1.postMessage(params);
          wk1.postMessage(JSON.stringify({ AppID, UserID, refresh, testCptIDs }));
          const onWorkerMsg = async (res) => {

            if (typeof(res) == 'string') {
              res = JSON.parse(res)
            }
      
            let data = res
            if (data[0] == true) {
              wk1.terminate()
              Pool = []
              resolve(data[1])
            } else {
      
              // 任务未完成，给前端报告进度
              params.__ws__.send({ msg:'not done yet' })
            }
      
          }
      
          wk1.on('message', onWorkerMsg)
        });
      
      
      }
}