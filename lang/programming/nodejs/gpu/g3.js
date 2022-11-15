const { GPU } = require('gpu.js');
const gpu = new GPU({ mode: 'gpu' });
const nobs=10000;

const kernel = gpu.createKernel(function() {
const y=Math.random();
return y;
}, { output: [nobs] });

console.time("gpu")
const data = kernel()
console.timeEnd("gpu")

console.time("cpu")
let data2 = []
for (let i = 0; i < 10000; i++) {
    data2.push( Math.random() )
}
console.timeEnd("cpu")


let a  = 1