
// 实际干活

const {
    parentPort
} = require('worker_threads')

parentPort.onmessage = function (event) {

    parentPort.postMessage([ false, { 'msg':'not done yet' } ])

    //parentPort.postMessage([ true, { 'msg':'done.' } ])
}

