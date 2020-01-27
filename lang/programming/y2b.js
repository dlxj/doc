y2b.js
// 经济学人音频版mp3 转mp4，用于上传youtube

var log = console.log
var fs = require('fs')
var path = require('path')
var async = require('async')

function audioTime(f, cb) {
    var re = ''
    var spawn = require('child_process').spawn
    ls = spawn('ffmpeg.exe', ['-i', f])
    ls.stdout.on('data', function(data) {
        log(null, 'stdout: ' + data) //命令执行结果
    })
    ls.stderr.on('data', function(data) {
        re = re + data
    })
    ls.on('exit', function(code) {
        var pat = /\d\d:\d\d:\d\d\.\d\d/; // g 全局搜索
        var match = pat.exec(re);
        var arr = match[0].split(':')
        var time = Number(arr[1]) * 60 + Math.ceil(arr[2]) // 音频长度是多少秒
        cb(null, time)
    })
}

function mp3tomp4(f, o, time, cb) {
    // var cmd = "-i mp3 -f image2 -loop 1 -t time -i jpg -acodec aac -vcodec h264 -r 25 -b 200k -y mp4"
    var cmd = "-i 005.mp3 -t 500 -y auto.mp4 -f image2 -loop 1 -i 0.jpg -acodec aac -vcodec h264 -r 25 -b 200k"
    var arr = []
    arr = cmd.split(' ')
    arr[1] = f
    arr[3] = '' + time
    arr[5] = path.join(o, path.basename(f.replace('mp3', 'mp4')))
    log(arr)

    var erre = ''
    var dre = ''
    var spawn = require('child_process').spawn
    ls = spawn('ffmpeg.exe', arr)
    ls.stdout.on('data', function(data) {
        dre = dre + dre //命令执行结果
            //log(data)
    })
    ls.stderr.on('data', function(data) {
        erre = erre + data
        log('' + data)
    })
    ls.on('exit', function(code) {
            //log(erre)
            //log('all take done.')
            return cb(null)
        })
        /**/
}

function convert(f, o, cb) {
    audioTime(f, function(err, time) {
        if (err) return cb(err)
        log('time: ', time)
        if (time < 60) {
            // return cb(null)
        }
        mp3tomp4(f, o, time, function(err) {
            if (err) return cb(err)
            cb(null)
        })
    })
}

function fnames(dir, cb) {
    fs.readdir(
        dir,
        function(err, files) {
            cb(err, files);
        }
    )
}

var dir = './audio/'
var out = './mp4'
fnames(dir, function(e, ns) {
    if (e) throw e
        //log(path.join(dir, ns[0]))
    var cur = 0
    async.eachOfLimit(ns, 1, function(f, k, cb) {
        process.nextTick(function() {
            log(f)
            convert(path.join(dir, f), out, function(err) {
                if (err) throw err
                cur = cur + 1
                log(f)
                log('### one task done.', cur, '/', ns.length)
                cb(null)
            })
        })
    }, function finish(e) {
        if (e) throw e
        log('### all task done.')
    })
})