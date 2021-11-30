
// let spawn = require('child_process').spawn

// child = spawn('mecab')
// child.stdin.setEncoding('utf-8');
// child.stdout.pipe(process.stdout);

// child.stdin.write("console.log('Hello from PhantomJS')\n");

// child.stdin.end();


const mecabSpawn = require('mecab-spawn')
const mecab = mecabSpawn.spawn()

const mecab = mecabSpawn.spawn('mecab', ['-d', `C:\Program Files (x86)\MeCab\dic\ipadic`])



a = 1


