
// const {
//     Worker,
//     workerData
//   } = require('worker_threads');
//   const path = require('path');

// async function creat(_path, params) {
//     return new Promise(function (resolve, reject) {
//       // const port = param.port
//       let Pool = []
//       let { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params
  
//       const wk1 = new Worker(path.resolve(__dirname, _path));
//       Pool.push(wk1)
//       wk1.ref()
//     //   wk1.postMessage(params);
  
//       const onWorkerMsg = async (res) => {
  
//         let data = res
//         if (data[0] == true) {
//           wk1.terminate()
//           Pool = []
//           resolve(data[1])
//         } else {
  
//           // 任务未完成，给前端报告进度
//           let msg = {
            
//           }
//           __ws__.send(msg)
//         }
  
//       }
  
//       wk1.on('message', onWorkerMsg)
//     });

// }

module.exports = {
    name: '智能计算试题标签',
    params: {
        AppID: {
            type: 'number',
            remark: '题库ID'
        },
        UserID: {
            type: 'number',
            remark: '操作用户ID'
        },
        testCptIDs: {
            type: 'array',
            default: [],
            remark: '章节ID'
        },
        refresh: {
            type: 'bool',
            remark: 'true 重新计算，false 不进行重新计算'
        }
    },
    remark: '',
    author: 'gd',
    handler: async function (params) {  // conn, params, 

        let { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params

        let worker = require('../../../lib/worker.js')
        let simir_data1 = await worker.create('../m.js', params) // 相对路径是相对 worker.js 所在目录说的

        let a = 1

        // __ws__.send({msg:'ok'})

    }
}