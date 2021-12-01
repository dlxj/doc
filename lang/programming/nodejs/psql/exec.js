
// let spawn = require('child_process').spawn

// child = spawn('d:\\usr\\python.exe')

// //child = spawn('mecab')
// child.stdin.setEncoding('utf-8');
// child.stdout.pipe(process.stdout);

// child.stdin.write("ここ\n");

// child.stdin.end();


// const mecabSpawn = require('mecab-spawn')
// const mecab = mecabSpawn.spawn()

// const mecab = mecabSpawn.spawn('mecab', ['-d', `C:\Program Files (x86)\MeCab\dic\ipadic`])





// var exec = require('child_process').exec;

// const cmd = `D:\\usr\\python.exe a.py`;
// console.log(`hi,,,`);
// exec(cmd, (error, stdout, stderr) => {
//    if (error) {
//     throw error
//    }

//    a = 1
      
// })



var MeCab = new require('mecab-async')
  , mecab = new MeCab()

mecab.parse('いつもニコニコあなたの隣に這い寄る混沌ニャルラトホテプです！', function(err, result) {
    if (err) throw err;
    console.log(result);
});

a = 1


