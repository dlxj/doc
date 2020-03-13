var http = require("http"),
    url = require("url"),
    path = require("path"),
    fs = require("fs"),
    mime = require("mime")
    port = process.argv[2] || 8888;
 
http.createServer(function(req, res) {
 
  var uri = url.parse(req.url).pathname
    , filename = path.join(process.cwd(), uri);
  
  fs.exists(filename, function(exists) {
    if(!exists) {
      res.writeHead(404, {"Content-Type": "text/plain"});
      res.write("404 Not Found\n");
      res.end();
      return;
    }
 
    var stat = fs.statSync(filename);
    res.writeHeader(200, {"Content-Length": stat.size});
    console.log('filename is: ' + filename, 'size is: ' + stat.size);
    var fReadStream = fs.createReadStream(filename);
    fReadStream.on('data', function (chunk) {
        if(!res.write(chunk)){//判断写缓冲区是否写满(node的官方文档有对write方法返回值的说明)
            fReadStream.pause();//如果写缓冲区不可用，暂停读取数据
        }
    });
    fReadStream.on('end', function () {
        res.end();
    });
    res.on("drain", function () {//写缓冲区可用，会触发"drain"事件
        fReadStream.resume();//重新启动读取数据
    });

  });
}).listen(parseInt(port, 10));
 
console.log("Static file server running at\n  => http://23.88.246.242:" + port + "/\n");
