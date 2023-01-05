
// 实际干活

const {
    parentPort
} = require('worker_threads')

parentPort.onmessage = function (event) {

    // 这里只适合做单纯的 CPU 计算，复杂对象参数传不进来，只能是 string 而已

    parentPort.postMessage(JSON.stringify([ false, { 'msg':'not done yet' } ]))

    setTimeout(async ()=>{
        parentPort.postMessage(JSON.stringify([ true, { 'msg':'task done.' } ]))
    },1000)

    //parentPort.postMessage([ true, { 'msg':'done.' } ])
}

