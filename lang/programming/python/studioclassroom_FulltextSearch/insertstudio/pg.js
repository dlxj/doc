/*
// drop database studio
pg_ctlcluster 9.5 main stop --force
pg_ctlcluster 9.5 main start
dropdb -U postgres  studio -h 127.0.0.1 -p 5432
*/

var dbpostgres = require('pg-db')("postgres://postgres:psql@192.157.212.220/postgres");
var db = require('pg-db')("postgres://postgres:psql@192.157.212.220/studio");
var sqlite3 = require('sqlite3').verbose();
var dbsq = new sqlite3.Database('./db/studioclassroom.db', sqlite3.OPEN_READONLY);
var util = require('util');

// CREATE TABLE 'studioclassroom_content'(docid INTEGER PRIMARY KEY, 'c0en', 'c1zh', 'c2name', 'c3time');
// SELECT * FROM "studioclassroom_content;

function queryStudio(callback) {
	dbsq.all("SELECT * FROM studioclassroom_content;", function(err, rows) {
		callback(rows);
	}); /**/
}

function createDatabase(cb) {
	dbpostgres.execute("CREATE DATABASE studio \
WITH OWNER = postgres \
   ENCODING = 'UTF8' \
   TABLESPACE = pg_default \
   LC_COLLATE = 'zh_CN.UTF-8' \
   CONNECTION LIMIT = -1 \
   TEMPLATE template0;", function(err, result) {
		cb(err, 'createDatabase ok.');
	});
}

function dropTable(cb) {
	db.execute("DROP TABLE IF EXISTS studio;", function(err, result) {
		cb(err, 'dropTable ok.');
	});
}

function createTable(cb) {
	db.execute("create table studio( \
   id serial primary key, \
   en text, \
   zh text, \
   type text, \
   time text, \
   v_en  tsvector, \
   v_zh  tsvector \
);", function(err, result) {
		cb(err, 'createTable ok.');
	});
}

function insertStudio(cb) {
	db.execute("insert into studio(en, zh, type, time, v_en, v_zh ) values('When something does not go as you expected and you feel anxious or upset, it helps to understand that these feelings are part of the package.', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。','AD050851', '01:20.3', 'no', to_tsvector('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。'));", function(err, result) {
		cb(err, 'insertStudio ok.');
	});
}

queryStudio(function(rows) {
	createDatabase(function(err, msg) {
		if (err) throw err;
		console.log(msg);
		db.tx.series([
			dropTable,
			createTable,
			function(cb) {
				db.execute('create extension pg_jieba;', function(err) {
					cb(err, 'create extension pg_jieba ok.');
				});
			},
			function(cb) {

				var curr = 0;
				var last = 10000 - 1; // rows.length - 1;

				for (var i = 0; i < rows.length; i++) {
					var sql = "insert into studio(en, zh, type, time, v_en, v_zh ) values('%s', '%s', '%s', '%s', 'no', to_tsvector('jiebacfg', '%s'));";
					sql = util.format(sql, rows[curr].c0en.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c2name.replace(/\n/g, ''), rows[curr].c3time.replace(/\n/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''));
					//console.log(sql);
					db.execute(sql, function(err, result) {
						if (err) {
							console.log(sql);
							throw err;
						}
						curr = curr + 1;
						console.log('insrt one task done. curr/last is: ', curr, '/', last); //console.log(rows.length, rows[curr].c0en, rows[curr].c1zh, rows[curr].c2name, rows[curr].c3time);
						if (curr > last) {
							console.log('insrt all task done. curr is: ' + curr);
							cb(null, 'insertStudio ok.');
						}
					});
				}

				function insrt(curr, last) {
					if (curr > last) {
						console.log('insrt all task done. curr is: ' + curr);
						cb(null, 'insertStudio ok.');
						return;
					}
					var sql = "insert into studio(en, zh, type, time, v_en, v_zh ) values('%s', '%s', '%s', '%s', 'no', to_tsvector('jiebacfg', '%s'));";
					sql = util.format(sql, rows[curr].c0en.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''), rows[curr].c2name.replace(/\n/g, ''), rows[curr].c3time.replace(/\n/g, ''), rows[curr].c1zh.replace(/\n/g, '').replace(/[",']/g, ''));
					//console.log(sql);
					//db.execute("insert into studio(en, zh, type, time, v_en, v_zh ) values('When something does not go as you expected and you feel anxious or upset, it helps to understand that these feelings are part of the package.', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。','AD050851', '01:20.3', 'no', to_tsvector('jiebacfg', '當事情進行不如預期，讓你感到焦慮心煩時，若能瞭解這些情緒是不可避免的，將會大有幫助。'));", function(err, result) {
					db.execute(sql, function(err, result) {
						if (err) {
							console.log(sql);
							throw err;
						}
						console.log('insrt one task done. curr/last is: ', curr, '/', last);
						insrt(curr + 1, last);
						//console.log(rows.length, rows[curr].c0en, rows[curr].c1zh, rows[curr].c2name, rows[curr].c3time);
						//cb(err, 'insertStudio ok.');
					});
				}
				//insrt(curr, last);
				//cb(null,'inset ok.');
			}
		], function(err, rs) {
			if (err) throw err;
			console.log(rs);
			console.log('all task done.');
		});
	});
});

/*
createDatabase(function(err, msg) {
	if (err) throw err;
	console.log(msg);
	db.tx.series([
		dropTable,
		createTable,
		function(cb) {
			db.execute('create extension pg_jieba;', function(err) {
				cb(err, 'create extension pg_jieba ok.');
			});
		},
		insertStudioFromSqlite
	], function(err, rs) {
		if (err) throw err;
		console.log(rs);
		console.log('all task done.');
	});
});*/

/*
db.tx.series([
	//dropTable,
	//createTable,
	
	function(cb) {
		db.execute('create extension pg_jieba;', function(err) {
			cb(err);
		});
	},
	//insertStudion
], function(err, rs) {
	if (err) throw err;
	console.log('all task done.');
});*/