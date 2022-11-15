const {GPU} = require('gpu.js');
const gpu = new GPU();

const multiplyMatrix = gpu.createKernel(function(a, b) {
    let sum = 0;
    for (let i = 0; i < 512; i++) {
        sum += a[this.thread.y][i] * b[i][this.thread.x];
    }
    return sum;
}).setOutput([512, 512]);

var a = [];
var b = [];
for (var i = 0; i < 512; i++) {
    a.push([]);
    b.push([]);
    for (var j = 0; j < 512; j++) {
        a[i].push(1);
        b[i].push(-1);
    }
}

console.time("gpu");
const c = multiplyMatrix(a, b);
console.timeEnd("gpu"); //2148ms

console.time("cpu"); 
var d = [];
for (var i = 0; i < 512; i++) {
    d.push([]);
    for (var j = 0; j < 512; j++) {
        let sum = 0;
        for (let k = 0; k < 512; k++) {
            sum += a[i][k] * b[k][j];
        }
        
        d[i].push(sum);
    }
}
console.timeEnd("cpu"); //710ms