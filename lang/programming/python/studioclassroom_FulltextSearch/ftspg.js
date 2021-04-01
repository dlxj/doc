// apachectl -k stop // free 80 port
// pm2 start ftspg.js -n ftspg80
// cat ~/.pm2/logs/ftspg777-out-0.log
// 哈佛商业评论
// http://www.hbrchina.org/2016-06-16/4208.html
// https://hbr.org/2015/07/your-team-cant-read-your-mind
// iTools安卓模拟器 adb
// adb connect 127.0.0.1:54001
/*
百度云分享链接：http://pan.baidu.com/s/1qXo3Ok8  密码：566x

【温馨提示】分享链接如果失效请加微信号book8848咨询获取新的下载地址，加微信号book8848还可获取更多英文原版杂志和报纸，微信号book8848的朋友圈每天都会发布最新杂志的更新说明。

【目前已经包括的英文杂志，持续快速更新】

日报类：
1、纽约时报（The New York Times）
2、华尔街日报（The Wall Street Journal）
3、金融时报（Financial Times）
4、华盛顿邮报（The Washington Post）
5、卫报（The Guardian）
6、今日美国（USA Today）
7、独立报（The Independent）
8、法国世界报（Le Monde）

周刊类：
1、经济学人（The Economist）
2、时代周刊（Time）
3、新闻周刊（Newsweek）
4、纽约客（The New Yorker）
5、彭博商业周刊（Bloomberg Businessweek）
6、巴伦周刊（Barron's）
7、科学（Science）
8、自然（Nature）
9、新科学家（New Scientist）
10、德国明镜周刊（Der Spiegel）

半月刊&月刊&双月刊类：
1、美国国家地理（National Geographic）
2、国家地理旅行者（National Geographic Traveler）
3、科学美国人（Scientific American）
4、哈佛商业评论（Harvard Business Review）
5、读者文摘（Reader's Digest）
6、发现（Discover）
7、大西洋月刊（The Atlantic）
8、财富（Fortune）
9、福布斯（Forbes）
10、彭博市场杂志（Bloomberg Markets）
11、麻省理工技术评论（MIT Technology Review）
12、外交政策（Foreign Policy）
13、外交事务（Foreign Affairs）
14、时尚Vogue（Vogue）
15、BBC历史（BBC History）
16、BBC聚焦（BBC Focus）
17、快公司（Fast Company）
18、纽约书评（The New York Review of Books）
19、纽约时报书评（The New York Times Review of Books）
20、伦敦书评（London Review of Books）
21、连线（Wired）
22、瑞丽时尚家居设计（Elle Decor）
23、时尚（Cosmopolitan）
24、跑步者世界（Runners' World）
25、嘉人（Marie Claire）
26、时尚芭莎（Harper's Bazaar）
27、时尚先生（Esquire）
28、建筑师（Architect）
29、大众科学（Popular Science）
30、孤独星球（Lonely Planet）
*/

'use strict';
var express = require('express'),
  app = express(),
  cookieParser = require('cookie-parser'),
  expressSession = require('express-session'),
  bodyParser = require('body-parser');

const { Pool, Client } = require('pg')
const connectionString = 'postgresql://postgres:postgres@111.229.53.195:5432/studio'
const pool = new Pool({
  connectionString,
})

const connectionString2 = 'postgresql://postgres:postgres@111.229.53.195:54322/anime'
const pool2 = new Pool({
  connectionString2,
})

function isJP(s) 
{ 
	var re = /[^\u0800-\u4e00]/; 
	if(re.test(s)) return false; 
	return true; 
}

var newStr = str2.replace( /([a-z])+/g,'qqq' );

// var db = require('pg-db')("postgres://postgres:psql@192.157.212.220/studio");

app.use(cookieParser());
app.use(expressSession({
  secret: 'somesecrettokenhere'
}));
app.use(bodyParser());

app.get('/', function(req, res) {

  var html = '<form action="/" method="post">' +
    'keyword: <input type="text" name="keyword"><br>' +
    '<button type="submit">Search</button>' +
    '</form>';
  if (req.session.keyword) {
    var keywd = req.session.keyword;
    if (typeof keywd != 'undefined' &&
      typeof keywd != null && keywd.trim().length > 0) {
      keywd = keywd.trim();
      var zhQ = false;
      for (var i in keywd) {
        if (keywd.charCodeAt(i) > 127) {
          zhQ = true;
          break;
        }
      }

      /*

      select id, en, zh, type, time from studio where v_en @@  to_tsquery('en', 'achieving') limit 3;

SELECT id, ts_headline(en, q), rank
FROM (SELECT id, en, q, ts_rank_cd(en, q) AS rank
FROM studio, to_tsquery('en', 'achieving') q
WHERE en @@ q
ORDER BY rank DESC
LIMIT 3) AS foo;
      */

      var sql = "";
      if (zhQ) {
        sql = "select id, en, zh, type from studio where v_zh @@  to_tsquery('jiebacfg', $1) ORDER BY RANDOM() limit 3;"
      } else {
        sql = "SELECT id, ts_headline(en, q) as en, zh, type \
                FROM studio, plainto_tsquery('en', $1) q \
                WHERE v_en @@ q \
                ORDER BY RANDOM() LIMIT 3 ;";
      }

      pool.query(sql, [keywd], (err, rt) => {
        if (err) throw err;
        // JSON.stringify
        for (var i in rt['rows']) {
          html += ('<br>' + rt['rows'][i].en + '<br>' + rt['rows'][i].zh + '<br>' + rt['rows'][i].type);
          html += ('<br>' + '<br>');
        }

        res.cookie('keywd', req.session.keyword);
        html += '<br>Your keyword is: ' + req.session.keyword;
        console.log('session is: ' + req.session.keyword);
        html += '<form action="/next" method="post">' +
          '<button type="submit">Next</button>' +
          '</form>';

        res.send(html);
      });

    } else {
      html += 'ooops: keyword plz.'
      res.send(html);
    }
  } else {
    res.send(html);
  }
});

app.post('/', function(req, res) {
  //if (req.cookies.bar) {
  //req.session.keyword = req.body.keyword;
  req.session.keyword = req.body.keyword;
  res.redirect('/');
    //}
    //res.send(req.cookies.bar);
    //res.redirect('/');
});

app.post('/next', function(req, res) {
  console.log('cookies is: ', req.cookies.keywd);
  req.session.keyword = req.cookies.keywd;
  res.redirect('/');
});


app.listen(8084, function() {
  console.log("ready captain.");
});