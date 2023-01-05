
// 实际干活

const {
    parentPort
} = require('worker_threads')

parentPort.onmessage = function (event) {

    // parentPort.postMessage([ false, { 'msg':'not done yet' } ])

    parentPort.postMessage(JSON.stringify([ false, { 'msg':'not done yet' } ]))

    setTimeout(async ()=>{
        parentPort.postMessage(JSON.stringify([ true, { 'msg':'task done.' } ]))
    },1000)

    //parentPort.postMessage([ true, { 'msg':'done.' } ])
}

