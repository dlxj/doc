
let path = require('path')
let fs = require('fs')
let util = require('util')

module.exports = {
    name: 'pushsteam',
    remark: '',
    params: {
        id: {
            type: 'string',
            remark: ''
        }
    },
    async handler({id}) {

        let { execa } = await import('execa')

        let cmd = `ffmpeg -re -i "E:\\1.mkv" -ss 00:00:00.000 -to 00:00:03.000 -q 0 -f mpegts -codec:v mpeg1video -s 1000x600 -r 30 http://localhost:9999/push/${id}`
        
        let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
        //childProcess.stdout.pipe(process.stdout)  // don't print to screen
        let { stdout } = await childProcess
        
        return this.msg(200, 'ok.')
    }
}



/*

let audio_dir = path.join(global.animes.root_audio, name, seasion)
                let audio_path = path.join(audio_dir, `${id}.mp3`)


                  res.writeHead(500, {
    'Content-Type': 'text/plain;charset=utf-8'
  });

        res.writeHead(404, headers)   nodejs writeHead audio/mpeg
      res.send('not found')

      https://gist.github.com/dtrce/1204243/47b9adf3c398dbcf092378c1f036c579aed76426

 var filePath = '/Users/djavia/_Eminem  Cleaning Out My Closet.mp3';
    var stat = fileSystem.statSync(filePath);

    response.writeHead(200, {
        'Content-Type': 'audio/mpeg',
        'Content-Length': stat.size
    });

    var readStream = fileSystem.createReadStream(filePath);
    // We replaced all the event handlers with a simple call to util.pump()
    util.pump(readStream, response);
    
    readStream.pipe(writeStream)

*/

/*

var http = require('http'),
    url = require('url'),
    fs   = require('fs'),
    filePath = '/home/risto/Downloads/oleg.mp3',
    stat = fs.statSync(filePath);

http.createServer(function(request, response) {
    var queryData = url.parse(request.url, true).query;
    const skip = typeof(queryData.skip) == 'undefined' ? 0 : queryData.skip;
    const startByte = stat.size * skip;

    response.writeHead(200, {
        'Content-Type': 'audio/mpeg',
        'Content-Length': stat.size - startByte
    });

    // We replaced all the event handlers with a simple call to util.pump()
    fs.createReadStream(filePath, {start:startByte}).pipe(response);
})
.listen(2000);

*/
