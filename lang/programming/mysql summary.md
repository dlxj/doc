

[TOC]

# install mysql

```
𬌗   去掉这个字就不出错
由中國的四川大学华西口腔医院教授鄒海帆於1920/1930年代造出。
	# 插入这个字会让mysql 出错，试不同的utf8 编码看
		INSERT INTO t(TEXT) VALUE ('𬌗');
			utf8mb4_general_ci 实测不会出错
```



```
sudo apt purge mysql-*

rm -rf /etc/mysql
rm -rf /var/lib/mysql

```



```
# centos7
shell> yum search libaio  # search for info
shell> yum install libaio openssl # install library
# ubuntu
shell> apt-cache search libaio # search for info
shell> apt-get install libaio1 # install library

```



```
# 安装mysql 5.6

# 先把发现的mysql 文件或包全删干净
rpm -qa | grep mysql
rpm -qa | grep maria
yum remove and run yum install mysql-devel
yum clean all

find / -name mysql   # 全删干净
find / -name my.cnf  # 全删干净

rm -rf (all folders listed in find)


yum install perl
yum install perl-Data-Dumper.x86_64



free -m
     # -m -g # m or g size show

dpkg -l '*mysql*'
dpkg --force-depends --purge mysql
     # uninstall mysql

http://dev.mysql.com/doc/refman/5.6/en/binary-installation.html
shell> groupadd mysql
shell> useradd -r -g mysql mysql
shell> cd /usr/local
shell> tar zxvf /path/to/mysql-VERSION-OS.tar.gz
shell> ln -s full-path-to-mysql-VERSION-OS mysql
shell> cd mysql
shell> chown -R mysql .
shell> chgrp -R mysql .
shell> scripts/mysql_install_db --user=mysql
    apt-get install libaio1 libaio-dev
    scripts/mysql_install_db --user=mysql --defaults-file=/usr/local/mysql/my.cnf
    scripts/mysql_install_db --user=mysql --no-defaults
shell> chown -R root .
shell> chown -R mysql data
shell> bin/mysqld_safe --user=mysql &
# Next command is optional
shell> cp support-files/mysql.server /etc/init.d/mysql.server

```

```
cd bin
mysql -uroot # 直接进，并不需要密码
	# GRANT ALL PRIVILEGES ON *.* TO rootsuper@'%' IDENTIFIED BY 'rootsuper4321' WITH GRANT OPTION;
	# % 换成 IP 地址，就是只允许这个IP 登录，% 表示任意IP

UPDATE mysql.user SET Password=PASSWORD('Axxev@2020') WHERE User='root';

GRANT ALL PRIVILEGES ON *.* TO 'unamehere'@'%' IDENTIFIED BY 'passwdhere' WITH GRANT OPTION;

service mysql.server status

```





```
my.cnf
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
[mysqld]
collation-server = utf8_general_ci
init-connect='SET NAMES utf8'
character-set-server = utf8
# binding IPv4 and 3306 port
bind-address = 0.0.0.0
port = 3306
basedir  = /usr/local/mysql
datadir  = /home/mysqldata
lc-messages-dir = /usr/local/mysql/share
innodb_use_native_aio = 0
```





/etc/my.cnf, /etc/mysql/my.cnf, /usr/local/etc/my.cnf, ~/.my.cnf 这些就是mysql默认会搜寻my.cnf的目录，顺序排前的优先



```
查看运行的配置信息
    cat /proc/$(pidof mysqld)/cmdline
    tr '\0' '\n' < /proc/$(pidof mysqld)/environ | grep -i cnf
    /usr/sbin/mysqld --help --verbose --skip-networking --pid-file=$(tempfile) 2> /dev/null | grep -A1 'Default options are read'
```

```
rpm -qa | grep mysql
rpm -qa | grep maria
yum remove and run yum install mysql-devel

find / -name mysql

rm -rf (all folders listed in find)

```



## 特殊字符报错

```
查数据库各种字符符设置
SHOW VARIABLES WHERE Variable_name LIKE 'character_set_%' OR Variable_name LIKE 'collation%';

ALTER DATABASE db_name(你的数据库) CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci;


```





## install 5.7



```
bin/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
	# 失败就删除 /etc/my.cnf ，不知道为什么新装系统就有

cat /root/.mysql_secret
	# 初始密码

yum install libaio numactl

yum install -y cmake bison bison-devel libaio libaio-devel gcc gcc-c++ ncurses ncurses-devel

yum -y install initscripts && yum clean all
	# service: command not found

vi /etc/my.cnf
[client]
default-character-set=utf8mb4
[mysql]
default-character-set=utf8mb4
[mysqld]
collation-server = utf8mb4_general_ci
init-connect='SET NAMES utf8mb4'
character-set-server = utf8mb4
# binding IPv4 and 3306 port
bind-address = 0.0.0.0
port = 3306
basedir  = /usr/local/mysql
datadir  = /usr/local/mysql/data
lc-messages-dir = /usr/local/mysql/share
innodb_use_native_aio = 0
skip-grant-tables


service mysql.server restart

./mysql -uroot # 直接进，并不需要密码

update mysql.user set authentication_string=PASSWORD('root') where User='root';

GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
	# % 换成 IP 地址，就是只允许这个IP 登录，% 表示任意IP

alter user 'root'@'%' identified by 'root';

\q 退出


接下来把  skip-grant-tables  注释掉！然后  service mysql.server restart

./mysql -uroot -p
	# 重新用密码登录


service mysql.server status

```



### crontab

```
crontab -e # 定时任务
00   00    26      01   *   echo 'hi from crontab.' > /root/sayhi.txt
分	时	  日	     月	 年

@reboot  service mysql.server restart # 重启自动执行
crontab -l

```





## windows

- https://www.cnblogs.com/kendoziyu/p/MySQL.html

```
新增系统变量 MYSQL_HOME=D:\usr\mysql-5.7.40-winx64
在系统变量Path后面追加;%MYSQL_HOME%\bin

mysqld -install

```





# Gram



## DataTime



```
let AddTime = moment(nowDate).format('YYYY-MM-DD HH:mm:ss')


date_format(StartTime, "%Y-%c-%d %H:%i:%s") as StartTime

```





### 时间差



```
# 单位秒数
select unix_timestamp("2020-01-01 00:01:00") - unix_timestamp("2020-01-01 00:00:00")
```





# Create



```mysql
CREATE TABLE `frequencystatistics` (
	`AppID` INT(11) NOT NULL,
	`TestCptID` INT(11) NOT NULL,
	`FrequencyJson` LONGTEXT NOT NULL COLLATE 'utf8_unicode_ci',
	`UpdateTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`AppID`, `TestCptID`) USING BTREE,
	INDEX `index_AppIDCptID` (`AppID`, `TestCptID`) USING BTREE
)
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB
;
```



```
create table bt_ask_to_cate_backup_temp select * from bt_ask_to_cate_backup;delete from bt_ask_to_cate_backup 
where (ask_id, cate) 
    in (SELECT ask_id, cate 
        FROM bt_ask_to_cate_backup_temp 
        group by ask_id,cate 
        having count(*) > 1
    ) 
and id 
    not in (SELECT min(id) 
            FROM bt_ask_to_cate_backup_temp 
            group by ask_id,cate 
            having count(*) > 1
        )
```



## 唯一索引和主键



```mysql
CREATE TABLE `duplicatetest` (
	`ID` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
	`appID` INT(11) NOT NULL,
	`testID` INT(11) NOT NULL COMMENT '',
	`childTestID` INT(11) NOT NULL,
	`isMaster` ENUM('1','0') NOT NULL DEFAULT '0' COMMENT '' COLLATE 'utf8_general_ci',
	`masterAppID` INT(11) NULL DEFAULT NULL COMMENT '',
	`masterTestID` INT(11) NULL DEFAULT NULL COMMENT '',
	`masterChildTestID` INT(11) NULL DEFAULT NULL COMMENT '',
	`addTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updateTime` DATETIME NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`appID`, `testID`, `childTestID`) USING BTREE,
	UNIQUE INDEX `ID` (`ID`) USING BTREE,
	INDEX `findByMaster` (`appID`, `masterTestID`, `masterChildTestID`) USING BTREE,
	INDEX `masterAppID` (`masterAppID`) USING BTREE
)
COMMENT=''
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
```





## upateTime



```
`createTime` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,  # 仅创建时写入
`updateTime` DATETIME NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,  # 仅更新时写入
```



## function

### nextval

```

DELIMITER //
CREATE DEFINER=`root`@`%` FUNCTION `nextval`(
	`i_BookID` int,
	`i_tableName` varchar(32)
)
RETURNS int(11)
LANGUAGE SQL
NOT DETERMINISTIC
CONTAINS SQL
SQL SECURITY DEFINER
COMMENT ''
begin
  update TableMaxID set MaxID = MaxID + 1 where BookID = i_BookID and TableName = i_tableName;
  if ROW_COUNT() = 0 then
     insert into TableMaxID(BookID, TableName, MaxID)
     values(i_BookID, i_tableName, 1);
     return 1;
  else
     return currval(i_BookID, i_tableName);
  end if;

END//
DELIMITER ;


CREATE TABLE `tablemaxid` (
	`BookID` INT(11) NOT NULL,
	`TableName` VARCHAR(32) NOT NULL COLLATE 'utf8_unicode_ci',
	`MaxID` INT(11) NULL DEFAULT NULL,
	PRIMARY KEY (`BookID`, `TableName`) USING BTREE,
	UNIQUE INDEX `book` (`BookID`, `TableName`) USING BTREE
)

```



# Insert



## INSERT INTO 多条



```
INSERT INTO 
items(name,city,price,number,picture) 
VALUES
('耐克运动鞋','广州',500,1000,'003.jpg'),
('耐克运动鞋2','广州2',500,1000,'002.jpg');
```

```javascript
  var { result: r1, msg: m1 } = await new Promise((resolve, reject) => {
    mysql_temp.queryParam(`INSERT INTO smartmakeexam_selected(AppID,SrcID,Sort) VALUES ? ON DUPLICATE KEY UPDATE Sort=VALUES(Sort);`, [ [ [1, 1, 1], [2, 2, 2] ]  ], (error, result) => {
      if (error) {
        return reject({ result: null, msg: error })
      }
      return resolve({ result, msg: '' })
    })
  })
  
  # 注意括号套三层！！
  
```





## INSERT INTO ON DUPLICATE



```python
INSERT INTO searchkeywods (AppEName, KeyWord, Count) VALUES ('a', 'b', 1) ON DUPLICATE KEY UPDATE Count=Count+1;  # 用表中原来的值


INSERT INTO searchkeywods (AppEName, KeyWord, Count) VALUES ('a', 'b', 1) ON DUPLICATE KEY UPDATE Count=values(Count); # 用语句提供的值

```



```
insert into discussion3

select * from discussion2

where DiscussionID not in

(select dd.DiscussionID from discussion2 dd

  inner join discussion d on d.AppID = dd.AppID and d.UserID = dd.UserID and d.AllTestID = dd.AllTestID and d.ChildTableID = dd.ChildTableID)


/////////////////////////

insert into discussion3(AppID, UserID,AllTestID,ChildTableID,Type, CreateTime, ReplyToID, CommendCount, Content, IsEnabled)

select AppID, UserID,AllTestID,ChildTableID,Type, CreateTime, ReplyToID, CommendCount, Content, IsEnabled from discussion2

where DiscussionID not in

(select dd.DiscussionID from discussion2 dd

  inner join discussion d on d.AppID = dd.AppID and d.UserID = dd.UserID and d.AllTestID = dd.AllTestID and d.ChildTableID = dd.ChildTableID)

```





## Replace Into



```mysql
REPLACE INTO users (id,name,age) VALUES(123, '赵本山', 50);
REPLACE INTO users SET id = 123, name = '赵本山', age = 50;
```





## Before insert



```
begin



if new.NickName is null

then

set new.NickName=(

select `name` from nickname_list as t1

join (SELECT FLOOR( MAX(id) * RAND()) as id FROM `nickname_list` ) as t2

where t1.id>t2.id limit 1

);

end if;

end


```



## 取自增字段的值

```
 SELECT @@IDENTITY 插入完了以后可以通过它执行获取上一条插入语句中生成的自增长字段的值。
```





## 自增ID 不连续

```
和 MySQL 的 innodb 数据库引擎相关，据说是 MyISAM 引擎 不会有这种问题

innodb 自增列 锁机制简述

解决方案
换掉 innodb 数据库引擎
用上提到的方案二SQL
配置 innodb_autoinc_lock_mode 参数
```





# Update



```mysql
UPDATE knowledgecard_test kt

INNER JOIN knowledgecard_info kn

ON kn.AllTestID1 = kt.AllTestId AND kn.ChildTableID1 = kt.ChildtableId

SET kt.KnowledgeCardId = kn.KnowledgeCardId
```





```

update app set AppEndTime = '2017-04-30 23:59' where appid in (select appid from (select appid from app where appename like '%__YN' or appename like '%__NM') as a);

```



```
update book set bookname=replace(bookname,'-','《') where bookid in(

select bookid from(
select book.bookid from bookandapp as bind
left join 
book
on book.bookid =bind.bookid
where bind.appid in(1332,1325,1326,1327)
) as t
)
```









# Query



## Info



```
mysql -h ip -uUserName -pPassWd
	SHOW DATABASES;
	use DBName;
	show tables;
	DESCRIBE DBName.TableName;
	SHOW TABLE STATUS WHERE Name='TableName';  # 显示表的备注
```





## IFNULL

```
SELECT c.TestCptID, IFNULL(s.SourceName, '-') AS SourceName FROM testchapter c  LEFT JOIN source s ON s.AppID = c.AppID AND s.SrcID = c.SrcID WHERE c.AppID = 8911
```





```mysql
mysql> SELECT * FROM table LIMIT 5,10;  // 检索记录行 6-15
 //为了检索从某一个偏移量到记录集的结束所有的记录行，可以指定第二个参数为 -1：
mysql> SELECT * FROM table LIMIT 95,-1; // 检索记录行 96-last.


SELECT * FROM t_question WHERE question_text LIKE '%安全法%' ;
 
select Srcid, Source from Source order by Sortid asc, Srcid desc  -- 来源
 
 
select * from Source order by Sortid asc, Srcid desc
select * from Subject order by Sortid asc, Sbjid desc
 
select Srcid from Source order by Sortid asc, Srcid desc limit 0,1  -- 来源1
select Srcid from Source order by Sortid asc, Srcid desc limit 1,1  -- 来源2
 
select distinct sbjID from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1)  -- 科目  -- distinct 去重复
     select * from Subject where Sbjid in ( select distinct sbjID from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1) ) order by Sortid asc    
 
 
 
select * from Chapter where SrcID = 2 order by SbjID asc
     select * from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1) order by SbjID, Sortid asc
     select distinct sbjID from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1)
          select distinct sbjID from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1) limit 0, 1
 
 
指定来源，指定科目，选出章节
select * from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1) and SbjID = (select distinct sbjID from Chapter where SrcID = (select Srcid from Source order by Sortid asc, Srcid desc limit 0,1) limit 0, 1)  order by Sortid asc
 
 select * from t_question where media_content is not null and media_width = 0


```





##  Mysql Version



```mysql
SHOW VARIABLES LIKE "%version%";
```



### Inner join



```mysql
SELECT tr.* FROM trialexampoint tr INNER JOIN (SELECT ts.ID AS menuID FROM trialexampointmenus ts INNER JOIN ( SELECT ID AS subjectID FROM tiku_new.trialsubject tt WHERE tt.appID = 8911 AND tt.name = '药学专业知识二' ) tt 
ON ts.subjectID = tt.subjectID WHERE ts.appID = 8911 AND ts.enable = 1) ts ON tr.menuID = ts.menuID  WHERE tr.enable = 1

sql = f"SELECT tr.ID as exampointID, CONCAT(tr.attribute,'\n', tr.context) as text FROM trialexampoint tr INNER JOIN (SELECT ts.ID AS menuID FROM trialexampointmenus ts INNER JOIN ( SELECT ID AS subjectID FROM tiku_new.trialsubject tt WHERE tt.appID = {appid} AND tt.name = '{subject}' ) tt ON ts.subjectID = tt.subjectID WHERE ts.appID = {appid} AND ts.enable = 1) ts ON tr.menuID = ts.menuID  WHERE tr.enable = 1 ORDER BY tr.ID asc;"

```



## 查知识点目录树

```python
SELECT * FROM tiku_new.trialexampointmenus ts WHERE ts.appid = 8911 AND ts.enable = 1 AND ts.subjectID = ( SELECT ID AS subid FROM tiku_new.trialsubject sb WHERE sb.appid = 8911 AND sb.enable = 1 AND sb.name = '药学综合知识与技能' ) 

-- SELECT * FROM tiku_new.trialexampointmenus ts WHERE ts.appid = 8911 AND PID = 61040  -- AND ts.enable = 1 AND ts.subjectID = ( SELECT ID AS subid FROM tiku_new.trialsubject sb WHERE sb.appid = 8911 AND sb.enable = 1 AND sb.name = '药学综合知识与技能' )  order BY ts.sort 

-- SELECT * FROM tiku_new.trialexampointmenus ts WHERE ts.appid = 8911 AND PID = 61080 

-- 61223

SELECT * FROM tiku_new.trialexampoint WHERE menuid IN (61223,61719,61720,61721,61722,62671,62672,62673,62679,62680,62685,63235,63236);
```



```python
// 查题
http://192.168.2.88:5002/test/getTestByOldCpt1
appID: 8911
cptID: 1722,1830,1832,1909,2006,2115,2116
testFilterType: 选择范围所有题
guid: 719b099e-48f2-406f-88cc-689495310d2b
userID: 840
```



## 查来源科目试题

```mysql
来源和章节名都查出来了
SELECT t.AppID, t.TestID, t.TestCptID, t.PageNo, t.TestJson,  IFNULL(sc.SourceName, '-') as SourceName,  IFNULL(sc.SubjectName, '-') as SubjectName 

from tiku.test t 
LEFT JOIN ( SELECT c.TestCptID, sb.SubjectName, IFNULL(s.SourceName, '-') AS SourceName FROM tiku.testchapter c
LEFT JOIN tiku.subject sb ON sb.AppID = c.AppID AND sb.SbjID = c.SbjID  
LEFT JOIN tiku.source s ON s.AppID = c.AppID AND s.SrcID = c.SrcID WHERE c.AppID = 8911  ) AS sc ON sc.TestCptID = t.TestCptID 
where appid=8911 and `Enable`='1' ORDER BY TestCptID asc;
```



## 查表结构

```python
select * from information_schema.columns
where table_schema = 'tiku'
and table_name = 'test';
```



## 连接



```
sql 左，右，内连接都可以 一对多。多对一。多对多的

左连接：保留左边全部行。按左边行顺序和右边比较是否相等。相等就连接成一行。可以多对多

右连接：保留右边全部行。按右边行顺序和左边比较是否相等。相等就连接成一行。可以多对多

内连接：不保留不相等的行。左右有相等的就连接，不相等的多去掉不要。可以多对多

```





## group by distinct 



```
DISTINCT实际上和GROUP BY的操作非常相似，只不过是在GROUP BY之后的每组中只取出一条记录而已。所以，DISTINCT的实现和GROUP BY的实现也基本差不多，没有太大的区别。同样可以通过松散索引扫描或者是紧凑索引扫描来实现，当然，在无法仅仅使用索引即能完成DISTINCT的时候，MySQL只能通过临时表来完成。但是，和GROUP BY有一点差别的是，DISTINCT并不需要进行排序。也就是说，在仅仅只是DISTINCT操作的Query如果无法仅仅利用索引完成操作的时候，MySQL会利用临时表来做一次数据的“缓存”，但是不会对临时表中的数据进行filesort操作。当然，如果我们在进行DISTINCT的时候还使用了GROUP BY并进行了分组，并使用了类似于MAX之类的聚合函数操作，就无法避免filesort了。

下面我们就通过几个简单的Query示例来展示一下DISTINCT的实现。

 

1.首先看看通过松散索引扫描完成DISTINCT的操作：


sky@localhost:  example 11:03:41>EXPLAIN SELECT  DISTINCT group_id

->  FROM group_message\G

***************************1.  row  ***************************

id:  1SELECT_type:SIMPLE

table:group_message

type:range

possible_keys:NULL

key:  idx_gid_uid_gc

key_len:4ref:  NULL

rows:10Extra: Using index for  group-by

1  row  in  set  (0.00sec)


 

我们可以很清晰的看到，执行计划中的Extra信息为“Usingindex for group-by”，这代表什么意思？为什么我没有进行GROUP BY操作的时候，执行计划中会告诉我这里通过索引进行了GROUP BY呢？其实这就是于DISTINCT的实现原理相关的，在实现DISTINCT的过程中，同样也是需要分组的，然后再从每组数据中取出一条返回给客户端。而这里的Extra信息就告诉我们，MySQL利用松散索引扫描就完成了整个操作。当然，如果MySQLQuery Optimizer要是能够做的再人性化一点将这里的信息换成“Using index for distinct”那就更好更容易让人理解了，呵呵。

 

2.  我们再来看看通过紧凑索引扫描的示例：


sky@localhost: example 11:03:53> EXPLAIN SELECT DISTINCT user_id

->FROM group_message

->WHERE group_id = 2\G

***************************1. row ***************************

id:1SELECT_type: SIMPLE

table:group_message

type:ref

possible_keys:idx_gid_uid_gc

key:idx_gid_uid_gc

key_len:4ref: const

rows:4Extra: Using WHERE; Using index

1row in set (0.00 sec)


这里的显示和通过紧凑索引扫描实现GROUP BY也完全一样。实际上，这个Query的实现过程中，MySQL会让存储引擎扫描group_id=2的所有索引键，得出所有的user_id，然后利用索引的已排序特性，每更换一个user_id的索引键值的时候保留一条信息，即可在扫描完所有gruop_id=2的索引键的时候完成整个DISTINCT操作。

3.下面我们在看看无法单独使用索引即可完成DISTINCT的时候会是怎样：


sky@localhost: example 11:04:40> EXPLAIN SELECT DISTINCT user_id

->FROM group_message

->WHERE group_id > 1 AND group_id < 10\G

***************************1. row ***************************

id:1SELECT_type: SIMPLE

table:group_message

type:range

possible_keys:idx_gid_uid_gc

key:idx_gid_uid_gc

key_len:4ref: NULL

rows:32Extra: Using WHERE; Using index; Using temporary

1row in set (0.00 sec)


当MySQL无法仅仅依赖索引即可完成DISTINCT操作的时候，就不得不使用临时表来进行相应的操作了。但是我们可以看到，在MySQL利用临时表来完成DISTINCT的时候，和处理GROUP BY有一点区别，就是少了filesort。实际上，在MySQL的分组算法中，并不一定非要排序才能完成分组操作的，这一点在上面的GROUP BY优化小技巧中我已经提到过了。实际上这里MySQL正是在没有排序的情况下实现分组最后完成DISTINCT操作的，所以少了filesort这个排序操作。

4.最后再和GROUP BY结合试试看：


sky@localhost: example 11:05:06> EXPLAIN SELECT DISTINCT max(user_id)

->FROM group_message

->WHERE group_id > 1 AND group_id < 10

->GROUP BY group_id\G

***************************1. row ***************************

id:1SELECT_type: SIMPLE

table:group_message

type:range

possible_keys:idx_gid_uid_gc

key:idx_gid_uid_gc

key_len:4ref: NULL

rows:32Extra: Using WHERE; Using index; Using temporary; Usingfilesort

1row in set (0.00 sec)


最后我们再看一下这个和GROUP BY一起使用带有聚合函数的示例，和上面第三个示例相比，可以看到已经多了filesort排序操作了，因为我们使用了MAX函数的缘故。

对于DISTINCT的优化，和GROUP BY基本上一致的思路，关键在于利用好索引，在无法利用索引的时候，确保尽量不要在大结果集上面进行DISTINCT操作，磁盘上面的IO操作和内存中的IO操作性能完全不是一个数量级的差距。
```









## 重置自增ID 



```
alter table xxx AUTO_INCREMENT=0;
```



## GROUP_CONCAT

```
# 所有行用逗号连接起来
SELECT GROUP_CONCAT('\'',`md5`, '\'') FROM img_extinfo WHERE  bookID = 57500 GROUP BY bookID;
```





# PROCEDURE



```mysql

CREATE  PROCEDURE `insertAllAppToVip`(IN `userID` INT, IN `beginTime` DATETIME, IN `endTime` DATETIME)
BEGIN
DECLARE done BOOLEAN DEFAULT 0;
declare currAppId int;
DECLARE cur CURSOR FOR
   select appId from app ;
DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done=1;
START TRANSACTION; 
 prepare stmtOfInsert from 
  'insert into vip(UserID,AppID,BeginTime,EndTime,IsLock,ClientType) values(?,?,?,?,1,8)';
 prepare stmtOfDelete from 
  'delete from vip where UserID= ? and AppID = ? ';
 set @uId = userID;
 set @bTime = beginTime;
 set @eTime = endTime;
 open cur;
repeat
 FETCH cur INTO currAppId;
 set @apId = currAppId;
 execute stmtOfDelete using @uId,@apId;
 execute stmtOfInsert using @uId,@apId,@bTime,@eTime;
until done end repeat;
COMMIT;  
DEALLOCATE PREPARE stmtOfInsert;
DEALLOCATE PREPARE stmtOfDelete;
close cur;
END

```



```

# 知识点摘要，以及对应书中的原文

DELIMITER $$
DROP PROCEDURE IF EXISTS SummaryText;
CREATE PROCEDURE `SummaryText`(IN `in_appid` INT)
BEGIN

	declare currAppId INT;
	declare currTestid INT;
	declare currChildTestID INT;
	
	
	DECLARE done BOOLEAN DEFAULT 0;
	DECLARE cur CURSOR FOR
   	select appid, testid, childTestID from trxxxxxxxxxxxxxxxt WHERE appid = in_appid;
	DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done=1;
	
	CREATE TEMPORARY TABLE if not exists IAMTMPTABLET1(pcontext LONGTEXT, ccontext LONGTEXT, scontext LONGTEXT);
	
	truncate TABLE IAMTMPTABLET1;
	
	prepare stmtOfInsert FROM
		'INSERT INTO IAMTMPTABLET1 SELECT ppm.context AS pcontext, tmp.ccontext, tmp.context FROM ( SELECT pm.PID, pm.`name`, pm.`context` AS ccontext , pt.context  from trialexampointrelevanttest rt INNER JOIN trialexampoint pt ON rt.examPointID = pt.ID INNER JOIN trialexampointmenus pm ON pm.ID = pt.menuID  WHERE rt.appid = ? AND rt.testid = ? AND rt.childTestID = ? AND rt.`enable` = 1  ) AS tmp INNER JOIN trialexampointmenus ppm on tmp.PID = ppm.ID WHERE NOT ( ppm.context IS NULL AND tmp.ccontext IS NULL )'; 
	
	
	open cur;
	repeat
 		FETCH cur INTO currAppId, currTestid, currChildTestID;
 		set @apId = currAppId;
		set @tsId = currTestid;
		set @chId = currChildTestID;
		
		execute stmtOfInsert using @apId, @tsId, @chId;

	until done end repeat;
	close cur;
	
	DEALLOCATE PREPARE stmtOfInsert;

	SELECT * FROM IAMTMPTABLET1;
		
END $$


CALL SummaryText(17397);
```





## Backup





/usr/local/mysql/bin/mysqldump -uksbao -pksbao_4321 -h rm-bp1lino8asl32m84c.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF --routines --opt -R  newmaindb_11 | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/ZC_HLXHSnewmaindb_11.sql

 /usr/local/mysql/bin/mysql  -uksbao -pksbaotest -h 10.29.184.219 -P3306 zc_fc_ytmjnew_21 < /mntt/ksbao/ZC_FC_YTMJnewmaindb_21.sql

/usr/local/mysql/bin/mysqldump -uksbao -pksbao_4321 -h rm-bp16n8v3p3vm3xp4h0o.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF --routines --opt -R  newmaindb_21 | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/ZC_FC_YTMJnewmaindb_21.sql

/usr/local/mysql/bin/mysql  -uksbao -pksbaotest -h 10.29.184.219 -P3306  zc_hlxhs_ytmjnewmaindb_8 < /mntt/ksbao/ZC_HLXHS_YTMJnewmaindb_8.sql

/usr/local/mysql/bin/mysqldump -uksbao -pksbao_4321 -h rm-bp1384s8oqe25n865bo.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF --routines  --opt -R  newmaindb_8 | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/ZC_HLXHS_YTMJnewmaindb_8.sql

routines 

wjwd

--set-gtid-purged=OFF --routines --no-data  --opt -R

/usr/local/mysql/bin/mysql  -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 jiakaodb < /mntt/ksbao/dzdb/wjwdb_20171031.sql

/usr/local/mysql/bin/mysqldump -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF --routines --no-data --opt -R  wjwdb | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/dzdb/wjwdb_20171031.sql



/usr/local/mysql/bin/mysql  -uksbao -pksbaotest -h  101.37.24.216 -P3306  stdt  < /mntt/ksbao/dzdb/standardized_training_db_20171028.sql

/usr/local/mysql/bin/mysql  -uksbao -pksbaotest -h 101.37.24.216 -P3306 pbc < /mntt/ksbao/dzdb/ytpublicdb_20171028.sql

/usr/local/mysql/bin/mysql  -uksbao -pksbaotest -h 101.37.24.216 -P3306  ytpublicdb2  < /mntt/ksbao/dzdb/ytpublicdb_20171028.sql

/usr/local/mysql/bin/mysqldump -uksbao -pksbaotest -h 101.37.24.216 -P3306 --set-gtid-purged=OFF --routines --opt -R --no-data ytpublicdb | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/dzdb/ytpublicdb_20171028.sql

/usr/local/mysql/bin/mysql  -uksbao -pksbaotest -h 101.37.24.216 -P3306  standardizedtrainingdb  < /mntt/ksbao/dzdb/standardized_training_db_20171028.sql

/usr/local/mysql/bin/mysqldump -uksbao -pksbaotest -h  101.37.24.216 -P3306 --set-gtid-purged=OFF --routines --opt -R --no-data standardized_training_db | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/dzdb/standardized_training_db_20171028.sql

/usr/local/mysql/bin/mysql  -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 jiakaodb < /mntt/ksbao/dzdb/wjwdb_20171027.sql

/usr/local/mysql/bin/mysqldump -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF wjwdb | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/dzdb/wjwdb_20171027.sql

GRANT ALL PRIVILEGES ON *.* TO root@61.234.53.146 IDENTIFIED BY 'adminroot' WITH GRANT OPTION;

 /usr/local/mysql/bin/mysqldump  -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF wjwdzdb2 | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/dzdb/wjwdzdb2_20170606.sql

 /usr/local/mysql/bin/mysqldump  -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 --set-gtid-purged=OFF newmaindb | perl -pe 's/DEFINER=`.+?\ /\ /' > /mntt/ksbao/dzdb/newmaindb_20170512.sql

 /usr/local/mysql/bin/mysql  -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 freemaindb < /mntt/ksbao/dzdb/newmaindb_20170512.sql

/usr/local/mysql/bin/mysql  -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 \

wjwdb < /mntt/ksbao/dzdb/wjwdzdb2_20170428.sql

./mysqldump -uroot -proot -h 127.0.0.1 -P3306 \

--set-gtid-purged=OFF --routines  --opt -R  --no-data wjwdzdb2 \

\> /mntt/ksbao/wjwdzdb2_20170412.sql

newtest

./mysql -uksbao -pksbaotest  -h 101.37.24.216 -P3306 \

 wjwdzdb2 < /mntt/ksbao/wjwdzdb2_20170412.sql

定制版

./mysql -uksbaosuper -pksbaosuper_4321 -h rm-bp1kdu4q0lq56lsqo.mysql.rds.aliyuncs.com -P3306 \

 wjwdzdb2 < /mntt/ksbao/wjwdzdb2_20170412.sql

./mysql -uroot -proot -h 127.0.0.1 -P3306 \

wjwdzdb2 < /mntt/ksbao/wjwdzdb2_20170412.sql

./mysqldump -uroot -proot -h 127.0.0.1 -P3306 \

--set-gtid-purged=OFF --routines --no-data  --opt -R wjwdzdb2 \

\> /mntt/ksbao/wjwdzdb2_20170408.sql

./mysql -uroot -proot -h 127.0.0.1 -P3306 \

 wjwdb < /mntt/ksbao/wjwdzdb2_20170408.sql

./mysql -uksbao -pksbaotest  -h 101.37.24.216 -P3306 \

wjwdb < /mntt/ksbao/wjwdzdb2_20170408.sql

./mysql -uksbao -pksbaotest -h 101.37.24.216 -P3306  -uroot -pksbaotest  \

newmaindb  < /mntt/ksbao/newmaindb20170511.sql

./mysqldump -h rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com -P3306 -urootsuper -prootsuper4321 \

--set-gtid-purged=OFF --routines --no-data  --opt -R newmaindb appidenames | perl -pe 's/DEFINER=`.+?\ /\ /' \

\> /mntt/ksbao/newmaindb20170511.sql

./mysql -h 101.37.24.216 -P3306 -uksbao -pksbaotest \

wjwdb < /mntt/ksbao/newmaindb20170408.sql

./mysql -h 101.37.24.216 -P3306 -uksbao -pksbaotest \

 newmaindb  < /mntt/ksbao/newmaindb_app20170310.sql

./mysql -uroot -proot -h 127.0.0.1 -P3306 newtmaindb </mntt/ksbao/newmaindb_app20170310.sql

6.只导出表结构不导出数据，--no-data

mysqldump -uroot -proot --no-data --databases db1 >/tmp/db1.sql

./mysqldump -h rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com -P3306 -urootsuper -prootsuper4321 \

--set-gtid-purged=OFF --no-data  --opt -R  newmaindb \

\> /mntt/ksbao/newmaindb161107.sql 

./mysql -uroot -proot -h 127.0.0.1 -P3306 wjwdzdb2 </mntt/ksbao/newmaindb161107.sql

./mysqldump -h rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com -P3306 -urootsuper -prootsuper4321 \

--set-gtid-purged=OFF newmaindb book bookandapp materialchapter knowledgepoint knowledgeandtest \

\> /mntt/ksbao/knowledgepoint20160829.sql 

./mysqldump -uroot -proot -h 127.0.0.1 -P3306 \

--set-gtid-purged=OFF newtmaindb book bookandapp materialchapter knowledgepoint knowledgeandtest \

\> /mntt/ksbao/knowledgepoint_newt_20160829.sql

./mysql -uroot -proot -h 127.0.0.1 -P3306 newtmaindb < /mntt/ksbao/knowledgepoint20160829.sql

./mysqldump -uroot -proot -h 127.0.0.1 -P3306  --routines --set-gtid-purged=OFF \

niukedb >/mntt/ksbao/niukedb20160804.sql 

./mysql -uroot -proot -h 127.0.0.1 -P3306  \

nursenotedb </mntt/ksbao/niukedb20160804.sql

nursenotedb

insert into discussion(AppID,UserID,AllTestID,ChildTableID,Type,CreateTime,ReplyToID,CommendCount,Content )

select AppID,UserID,AllTestID,ChildTableID,Type,CreateTime,ReplyToID,CommendCount,Content from discussion_nt;

//

/* Affected rows: 2,411,299 已找到记录: 0 警告: 0 持续时间 1 query: 32.433 sec. */

insert into discussion_backup(AppID,UserID,AllTestID,ChildTableID,Type,CreateTime,ReplyToID,CommendCount,Content )

select AppID,UserID,AllTestID,ChildTableID,Type,CreateTime,ReplyToID,CommendCount,Content from discussion_nt;

./mysql -h rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com -P3306 -urootsuper -prootsuper4321

./mysqldump -h 115.29.210.3 -P3307 -urootsuper -prootsuper4321  --set-gtid-purged=OFF \

community discussion_note > /mntt/ksbao/discussion_note160526.sql

./mysql -h rds4j9p1t26e20v63859.mysql.rds.aliyuncs.com -P3306 -urootsuper2 -prootsuper24321 \

community < /mntt/ksbao/discussion_note160526.sql

 

GRANT ALL PRIVILEGES ON *.* TO root@100.98.254.80 IDENTIFIED BY 'adminroot' WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON *.* TO rootsuper2@10.161.211.35 IDENTIFIED BY 'rootsuper24321' WITH GRANT OPTION;

./mysql -h rds4j9p1t26e20v63859.mysql.rds.aliyuncs.com  -P3306 -urootsuper2 -prootsuper24321

./mysql -h sub1459349088195-rds4j9p1t26e20v63859.mysql.rds.aliyuncs.com -P3306 -urootsuper2 -prootsuper24321

delete g.* from userexamgather g inner join (select appid, userid from vip where appid=22 and EndTime < '2016-01-01') v on g.AppID=22 and g.AppID = v.AppID and g.UserID = v.UserID;

select count(*) from userexamgather g inner join (select appid, userid from vip where appid=343 and EndTime < '2016-01-01') v on g.AppID=343 and g.AppID = v.AppID and g.UserID = v.UserID;

book

bookandapp

knowledgepoint

knowledge

materialchapter

app

./mysqldump -h 115.29.210.3 -P3307 -uadminroot -p --set-gtid-purged=OFF \

newmaindb app vip users > /mntt/ksbao/newapp160322.sql

mysql  -usuper -psuper -h 192.168.0.23 userexamgatheranalysis < newapp160322.sql

./mysql -h 115.29.210.3 -P3306 -urootsuper -prootsuper4321 newtmaindb < /mntt/ksbao/newapp160314.sql

./mysq  -h 115.29.210.3 -P3307 -urootsuper -prootsuper4321 newmaindb  < /mntt/ksbao/knowledgepoint160414.sql

sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/ ' /mntt/ksbao/knowledgepoint160414.sql > /mntt/ksbao/knowledgepoint1604144.sql

awk '{ if (index($0,"GTID_PURGED")) { getline; while (length($0) > 0) { getline; } } else { print $0 } }'  /mntt/ksbao/knowledgepoint1604144.sql | grep -iv 'set @@' >/mntt/ksbao/knowledgepoint16041444.sql

./mysqldump -h 115.29.210.3 -P3306 -urootsuper -prootsuper4321 --set-gtid-purged=OFF  newtmaindb knowledgepoint  materialchapter  > /mntt/ksbao/knowledgepoint160414.sql

./mysqldump -h 115.29.210.3 -P3306 -urootsuper -prootsuper4321 --set-gtid-purged=OFF  --opt -R newtmaindb book bookandapp knowledgepoint knowledge materialchapter app > /mntt/ksbao/knowledgepoint20160225.sql

./mysql -h 115.29.210.3 -P3306 -urootsuper -prootsuper4321 knowledgepoint < /mntt/ksbao/knowledgepoint20160225.sql



./mysql -uroot -p  newdb2 < newmaindb.sql



./mysqldump -uroot -p  newmaindb userexamgather > /root/newmaindb_userexamgather150819.sql

insert into newmaindb2. userexamgather (select * from newmaindb.userexamgather)





```
insert into newytmaindb.users (select * from newymaindb.users)
```





115.29.210.3

115.29.210.3

115.29.210.3

115.29.210.3

curl  -o hins534293_xtra_20150708012023.tar.gz --limit-rate 1M Http://rdsbak-hzf.oss-cn-hangzhou-f-internal.aliyuncs.com/custins340149/hins534293_xtra_20150708012023.tar.gz?OSSAccessKeyId=c9gzsqpauj3duw5whwdv40hb&Expires=1436606855&Signature=9b1GCeOECZzhGnoSI%2Fl6LPd50q8%3D



mysqldump -uroot  --routines # 存储过程一起dump



login

   ./mysql -uroot -p -h 127.0.0.1

  ./mysql -urootsuper -p -h 10.140.47.156

PING rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com (10.140.47.156) 56(84) bytes of data.

   

backup

   ./mysqldump -uroot -proot  -h 127.0.0.1 test >~/test.sql

   ./mysqldump -uroot -p115135root  -h 127.0.0.1  newmaindb>~/newmaindb140724.sql

   ./mysqldump -uroot -p  maindb> /mnt/ksbao/maindb140821.sql 

   ./mysqldump -uroot -p  newmaindb> /mntt/ksbao/newmaindb141009.sql

​    ./mysqldump -uroot -p newytmaindb> /mntt/ksbao/newytmaindb1411110800.sql

​     ./mysqldump -uroot -p newtmaindb> /mntt/ksbao/newtmaindb1411111532.sql

​     ./mysqldump -uroot -p useractionanalysis> /mntt/ksbao/useractionanalysis1411121824.sql

​     ./mysqldump -uroot -p  newytmaindb> /mntt/ksbao/newytmaindb1411211702.sql

  ./mysqldump -uroot -p  zhongxindb> /mntt/ksbao/zhongxindb1412010821.sql

  ./mysqldump -uroot -p  tbsmaindb> /mntt/ksbao/tbsmaindb1412030837.sql

  ./mysqldump -uroot -p newtmaindb> /mntt/ksbao/newtmaindb1412040904.sql

 ./mysqldump -uroot -p  newmaindb> /mntt/ksbao/newmaindb1412111506.sql

  ./mysqldump -uroot -p  newmaindb> /mntt/ksbao/newmaindb1412180907.sql

 ./mysqldump -uroot -p newtmaindb> /mntt/ksbao/newtmaindb141226.sql

  ./mysqldump -uroot -p  newmaindb> /mntt/ksbao/newmaindb1501041854.sql

  ./mysqldump -uroot -p  newmaindb> /mntt/ksbao/newmaindb1502041435.sql

  ./mysqldump -uroot -p tbsmaindb> /mntt/ksbao/tbsmaindb150318.sql

 ./mysqldump -uroot -p db789> /mntt/ksbao/db789150330.sql

./mysql -urootsuper -p -h 10.140.47.156 newtmaindb > /mntt/ksbao/newtmaindb150408.sql 

./mysql -urootsuper -p -h 10.140.47.156 newmaindb > /mntt/ksbao/newmaindb150408.sql 



rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com

3306

 

./mysql -h rdsazm0i3pizuq6t9dgad.mysql.rds.aliyuncs.com -u rootsuper -p newtmaindb < /mntt/ksbao/db789150330.sql

 

 ./mysqldump -uroot -p  --routines newdb> /mntt/ksbao/newdb150423.sql

 ./mysql -uroot -p  schooldb < /mntt/ksbao/newdb150423.sql

 ./mysql -uroot -p  newtmaindb < /mntt/ksbao/newdb150423.sql

./mysqldump -uroot -p  newtmaindb users vip viplog userorder > /mntt/ksbao/newtmaindb-users-vip-viplog-userorder150603.sql

./mysql -uroot -p newtmaindb < /mntt/ksbao/newtmaindb-users-vip-viplog-userorder150603.sql

./mysqldump -h 115.29.210.3 -P3307 -uadminroot -p  --set-gtid-purged=OFF newtmaindb users vip viplog userorder vipassistant > /mntt/ksbao/newtmaindb-users-vip-viplog-userorder-vipassistant150603.sql

mysqldump -usuper -p -h 169.254.197.92 newexamsystem >C:\rds\newexamsystem151019.sql

mysqldump -usuper -p -h 169.254.197.92 newexamsystem >C:\rds\newexamsourcedb151019.sql

 ./mysqldump -uroot -padminroot -h 127.0.0.1 --opt -R sipinmaindb > /mntt/ksbao/sipinmaindb151214.sql 

 ./mysql -uroot -padminroot -h 127.0.0.1 sipinmaindbt < /mntt/ksbao/sipinmaindb151214.sql 

 mysqldump -uroot -proot -h YT-WinSer08-23 --opt -R newexamsourcedb4 > /mntt/ksbao/newexamsourcedb4151216.sql 

mysql -usuper -psuper654321 -h iZ23o4w751sZ  newexamsourcedb < E:\upload\newexamsourcedb4151216.sql

cd /usr/bin && \

./mysqldump -h 115.29.210.3 -P3307 -uadminroot -p --set-gtid-purged=OFF \

newmaindb users vip viplog userorder vipassistant examgather > \

/home/ubt/rds/newmaindb-users-vip-viplog-userorder-vipassistant-examgather$(date +\%Y-\%m-\%d-\%H-\%M-\%S).sql && \

echo '##### backup task done.'

 

backupdb

20 * * * * /home/ubt/sh/backup.sh >/dev/null 2>&1

 

crontab backupdb

 

crontab -l

crontab -e

crontab -r

/etc/init.d/cron restart

windows

@echo off

cd C:/mysql-5.6.25-winx64/bin

set "curdate=%date:~0,4%%date:~5,2%%date:~8,2%"

for /f "tokens=1-3 delims=.: " %%1 in ("%time%") do set curtime=%%1%%2%%3

set "datetime=%curdate%-%curtime%"

set "fname=newtmaindb-users-vip-viplog-userorder-vipassistant-examgather%datetime%.sql"

set "path=c:/rds/%fname%"

mysqldump -h 115.29.210.3 -P3307 -uadminroot -p --set-gtid-purged=OFF ^

newtmaindb users vip viplog userorder > %path% && ^

echo ##### backup task done. && ^

echo ##### importing backup to local mysql ... && ^

mysql -uroot -proot newtmaindb < %path% && ^

echo ##### import backup succeess

pause

**mysql_config_editor set --login-path=loginpath133 --user=root --host=127.0.0.1 --password**

**mysql_config_editor set --login-path=loginpath3 --user=adminroot --host=115.29.210.3 -P3307 --password**

**mysql_config_editor set --login-path=loginpath3-3306 --user=root --host=115.29.210.3 -P3306 --password**

**mysql --login-path=loginpath3-3306**

**121.40.239.133**

@echo off

cd C:/mysql-5.6.25-winx64/bin

set "curdate=%date:~0,4%%date:~5,2%%date:~8,2%"

for /f "tokens=1-3 delims=.: " %%1 in ("%time%") do set curtime=%%1%%2%%3

set "datetime=%curdate%-%curtime%"

set "fname=newtmaindb-users-vip-viplog-userorder-vipassistant-examgather%datetime%.sql"

set "path=c:/rds/%fname%"

mysqldump --login-path=loginpath3 --set-gtid-purged=OFF ^

newtmaindb users vip viplog userorder > %path% && ^

echo ##### backup task done. && ^

echo ##### importing backup to local mysql ... && ^

mysql --login-path=loginpath133 newtmaindb < %path% && ^

echo ##### import backup succeess

pause



revert

   ./mysql -uroot -proot  -h 127.0.0.1 test2 <~/test.sql

./mysql -uroot -padminroot  maindbcolone< ~/maindbcolone.sql

   ./mysql -uroot -p zhongxindb <~/mntt/ksbao/

 ./mysql -uroot -p maindb8011< /mntt/ksbao/maindb140925.sql

./mysql -uroot -p  tbsmaindb< /mntt/ksbao/newtmaindb1411111532.sql

 ./mysql -uroot -p newytmaindb< /mntt/ksbao/newytmaindb1411110800.sql

./mysql -uroot -p useractionanalysis< /mntt/ksbao/useractionanalysis1411121824.sql

./mysql -uroot -p  zhongxindb< /mntt/ksbao/zhongxindb1411101652.sql

 ./mysql -uroot -p newmaindb< /mntt/ksbao/newytmaindb1411211702.sql

./mysql -uroot -p  zhongxindb141202< /mntt/ksbao/zhongxindb1412010821.sql

  ./mysql -uroot -p  tbsmaindb< /mntt/ksbao/tbsmaindb1412030837.sql

  ./mysql -uroot -p newtmaindb< /mntt/ksbao/newtmaindb1412040904.sql

  ./mysql -uroot -p newtmaindb </root/dbbackup141111/newytmaindb1411110800.sql
 ./mysql -uroot -p xinkedb< /mntt/ksbao/newtmaindb141226.sql

 ./mysql -uroot -p newdb< /mntt/ksbao/newmaindb1502041435.sql



```
$ mysqldump yourFirstDatabase -u user -ppassword > yourDatabase.sql$ mysql yourSecondDatabase -u user -ppassword < yourDatabase.sql
```



backup database

   ./mysqldump -uroot -proot --all-databases >~/sql.sql





windows

   backup

​     mysqldump -uroot -proot -h YT-WinSer08-23  tt >sql.sql

   reverse

​     mysql -uroot -proot -h YT-WinSer08-23  tt2 <sql.sql

​     mysql -uroot -proot -h YT-WinSer08-23  newmaindb140724 < newmaindb140724.sql

​     mysql -uroot -proot -h YT-WinSer08-23  newmaindb140806 < newmaindb140806.sql



ubuntu

./mysqldump -uroot -proot --all-databases >~/sql.sql

./mysqldump -uroot -proot  test >~/test.sql

./mysqldump -uroot -proot  -h 127.0.0.1 test >~/test.sql



还原

mysql -uroot -proot -h YT-WinSer08-23 maindb < sql.sql





\-----------

```
mysqldump -h [server] -u [user] -p[password] db1 | mysql -h [server] -u [user] -p[password] db2
```

Note: There is NO space between `-p` and `[password]`

\-----------





备份

mysqldump -uroot -proot -h YT-WinSer08-23 maindb >maindb23.sql





还原

mysql -uroot -proot -h YT-WinSer08-23  maindbcolone <maindb23.sql

mysql -uroot -proot -h YT-WinSer08-23  newdb140717 <newdb140717.sql



**备份MySQL数据库的命令**

mysqldump -hhostname -uusername -ppassword databasename > backupfile.sql

**备份MySQL数据库为带删除表的格式**

备份MySQL数据库为带删除表的格式，能够让该备份覆盖已有数据库而不需要手动删除原有数据库。

mysqldump -–add-drop-table -uusername -ppassword databasename > backupfile.sql

**直接将MySQL数据库压缩备份**

mysqldump -hhostname -uusername -ppassword databasename | gzip > backupfile.sql.gz

**备份MySQL数据库某个(些)表**

mysqldump -hhostname -uusername -ppassword databasename specific_table1 specific_table2 > backupfile.sql

**同时备份多个MySQL数据库**

mysqldump -hhostname -uusername -ppassword –databases databasename1 databasename2 databasename3 > multibackupfile.sql

**仅仅备份数据库结构**

mysqldump –no-data –databases databasename1 databasename2 databasename3 > structurebackupfile.sql

**备份服务器上所有数据库**

mysqldump –all-databases > allbackupfile.sql

**还原MySQL数据库的命令**

mysql -hhostname -uusername -ppassword databasename < backupfile.sql

**还原压缩的MySQL数据库**

gunzip < backupfile.sql.gz | mysql -uusername -ppassword databasename

**将数据库转移到新服务器**

mysqldump -uusername -ppassword databasename | mysql –host=*.*.*.* -C databasename



# Functioin



```
CREATE DEFINER=`book`@`%` FUNCTION `ntval`(
	`i_BookID` int,
	`i_tableName` varchar(32)
)
RETURNS int(11)
LANGUAGE SQL
NOT DETERMINISTIC
CONTAINS SQL
SQL SECURITY DEFINER
COMMENT ''
begin
  update TableMaxID set MaxID = MaxID + 1 where BookID = i_BookID and TableName = i_tableName;
  if ROW_COUNT() = 0 then
     insert into TableMaxID(BookID, TableName, MaxID)
     values(i_BookID, i_tableName, 1);
     return 1;
  else
     return currval(i_BookID, i_tableName);
  end if;
end
```

```
CREATE DEFINER=`book`@`%` FUNCTION `crrval`(
	`i_BookID` int,
	`i_tableName` varchar(32)
)
RETURNS int(11)
LANGUAGE SQL
NOT DETERMINISTIC
CONTAINS SQL
SQL SECURITY DEFINER
COMMENT ''
begin
    declare v_maxID integer;
    set v_maxID = 0;
    select MaxID into v_maxID from TableMaxID  where BookID  = i_BookID  and TableName = i_tableName;
    return v_maxID;
end
```









# [mysql备份与还原](http://www.cnblogs.com/Cherie/p/3309456.html)

## 一、备份常用操作基本命令

1、备份命令mysqldump格式

  格式：mysqldump -h主机名 -P端口 -u用户名 -p密码 –database 数据库名 > 文件名.sql 

2、备份MySQL数据库为带删除表的格式

备份MySQL数据库为带删除表的格式，能够让该备份覆盖已有数据库而不需要手动删除原有数据库。

mysqldump --add-drop-table -uusername -ppassword -database databasename > backupfile.sql

3、直接将MySQL数据库压缩备份

mysqldump -hhostname -uusername -ppassword -database databasename | gzip > backupfile.sql.gz

4、备份MySQL数据库某个(些)表

mysqldump -hhostname -uusername -ppassword databasename specific_table1 specific_table2 > backupfile.sql

5、同时备份多个MySQL数据库

mysqldump -hhostname -uusername -ppassword –databases databasename1 databasename2 databasename3 > multibackupfile.sql仅仅备6、仅备份份数据库结构

mysqldump –no-data –databases databasename1 databasename2 databasename3 > structurebackupfile.sql

7、备份服务器上所有数据库

mysqldump –all-databases > allbackupfile.sql

8、还原MySQL数据库的命令

mysql -hhostname -uusername -ppassword databasename < backupfile.sql

9、还原压缩的MySQL数据库

gunzip < backupfile.sql.gz | mysql -uusername -ppassword databasename

10、将数据库转移到新服务器

mysqldump -uusername -ppassword databasename | mysql –host=*.*.*.* -C databasename

11、--master-data 和--single-transaction

  在mysqldump中使用--master-data=2，会记录binlog文件和position的信息 。--single-transaction会将隔离级别设置成repeatable-commited

12、导入数据库

常用source命令，用use进入到某个数据库，mysql>source d:\test.sql，后面的参数为脚本文件。

13、查看binlog日志

查看binlog日志可用用命令 mysqlbinlog binlog日志名称|more

 

14、general_log

General_log记录数据库的任何操作，查看general_log 的状态和位置可以用命令show variables like "general_log%" ,开启general_log可以用命令set global general_log=on

## 二、增量备份

小量的数据库可以每天进行完整备份，因为这也用不了多少时间，但当数据库很大时，就不太可能每天进行一次完整备份了，这时候就可以使用增量备份。增量备份的原理就是使用了[mysql](http://www.centos.bz/category/mysql/)的binlog志。

 

1、首先做一次完整备份：

mysqldump -h10.6.208.183 -utest2 -p123 -P3310 --single-transaction --master-data=2 test>test.sql这时候就会得到一个全备文件test.sql

在sql文件中我们会看到：
-- CHANGE MASTER TO MASTER_LOG_FILE='bin-log.000002', MASTER_LOG_POS=107;是指备份后所有的更改将会保存到bin-log.000002二进制文件中。
2、在test库的t_student表中增加两条记录，然后执行flush logs命令。这时将会产生一个新的二进制日志文件bin-log.000003，bin-log.000002则保存了全备过后的所有更改，既增加记录的操作也保存在了bin-log.00002中。

3、再在test库中的a表中增加两条记录，然后误删除t_student表和a表。a中增加记录的操作和删除表a和t_student的操作都记录在bin-log.000003中。

 

## 三、恢复

1、首先导入全备数据

mysql -h10.6.208.183 -utest2 -p123 -P3310 < test.sql，也可以直接在mysql命令行下面用source导入

2、恢复bin-log.000002

  mysqlbinlog bin-log.000002 |mysql -h10.6.208.183 -utest2 -p123 -P3310 

3、恢复部分 bin-log.000003

  在general_log中找到误删除的时间点，然后更加对应的时间点到bin-log.000003中找到相应的position点，需要恢复到误删除的前面一个position点。

可以用如下参数来控制binlog的区间

--start-position 开始点 --stop-position 结束点

--start-date 开始时间 --stop-date 结束时间

找到恢复点后，既可以开始恢复。

 mysqlbinlog mysql-bin.000003 --stop-position=208 |mysql -h10.6.208.183 -utest2 -p123 -P3310 







\3. 先停止业务，使用MySQLdump的数据导出工具，将原有数据库数据导出为数据文件。例如：

mysqldump -h cloudcc.mysql.aliyun.com -u user_name -p --opt

--default-character-set=utf8 --extended-insert=false --triggers

--hex-blob db_name > /tmp/db_name.sql

其中user_name以您真实的数据库用户代替 db_name以您真实的数据库名代替。 /tmp/db_name.sql是文件名，由您自己随意填写。

\4. 将数据文件使用ftp工具上传到已经购买的云服务器中。

\5. 远程登录到云服务器，将刚才上传的数据文件导入到example.mysql.aliyun.com：3306中。例如：

mysql -h cloudcc.mysql.aliyun.com -u user_name -p db_name <

/tmp/db_name.sql

数据迁移完毕，可以对RDS正常使用。用户可使用数据库客户端工具（如MySQL-Front）或第三方数据库管理工具(如phpmyadmin)以及程序的方式，通过域名和端口号连接数据库，在输入正确的用户名和密码后即可登陆DB进行操作和开发。



来源： <http://blog.csdn.net/jk0803_wantao/article/details/9179217>

 

# 用mysqldump备份和恢复指定表的方法

代码如下:
mysqldump -u user -p db tab1 tab2 > db.sql 


恢复 
复制代码代码如下:
mysql -u user -p db < db.sql 

备份整个数据库   -->   mysqldump db1 >/backup/db1.20060725  
压缩备份       -->   mysqldump db1 | gzip >/backup/db1.20060725 
分表备份       -->   mysqldump db1 tab1 tab2 >/backup/db1_tab1_tab2.sql 
直接远程备份    -->  mysqladmin -h boa.snake.net create db1 
              -->   mysqldump db1 | mysql -h boa.snake.net db1 



# 排除表不备份



```
--ignore-table=
```



```
mysqldump -h主机名 -P端口 -u用户名 -p密码 –database 数据库名 > 文件名.sql
```





# 用户权限



```mysql
show grants for username; # 现在权限

GRANT ALL PRIVILEGES ON `dbname`.* TO 'username'@'%' WITH GRANT OPTION;  
	# 给他某库的所有权限


GRANT SELECT ON ocr.*, origintest_master.*, test_cooperate_master.* TO 'backup'@'%' IDENTIFIED BY "2022_backup"


GRANT ALL PRIVILEGES ON `temp`.* TO 'temp'@'%' IDENTIFIED BY "Pwd@2022"

      port: 3306,
      multipleStatements: true,
      connectTimeout: 60 * 1000,
      connectionLimit: 100,
      acquireTimeout: 15000, // 连接超时时间
      queueLimit: 0, // 排队最大数量(0 代表不做限制)
      waitForConnections: true, // 超过最大连接时排队

```





```mysql
show grants for 'xx';

mysql>select * from mysql.user where user='user1'\G

mysql>show grants for user1@'localhost';

例如，如果想让用户能读取和修改已有表的内容，但又不允许创建新表或删除表，可按如下授权：
GRANT SELECT,INSERT,DELETE,UPDATE ON samp_db.* TO 'user'@'%' IDENTIFIED BY "pass"

grant select,insert,update,delete on mydb.* to test2@localhost identified by "abc"; 

grant select on useractionanalysis.* to guest@222.217.18.123 identified by "guest";
```



# 定时备份





```
00   01    11      12   *   echo 'say hi from auto.'>/root/hi.txt
```





```
30   5    8      6   *   ls     指定每年的6月8日5：30执行ls命令
分   时    日     月
```



```
5   *    *      *   *   ls     指定每小时的第5分钟执行一次ls命令
30   5    *      *   *   ls     指定每天的 5:30 执行ls命令
30   7    8      *   *   ls     指定每月8号的7：30分执行ls命令
30   5    8      6   *   ls     指定每年的6月8日5：30执行ls命令
30   5    8      6   *   ls     指定每年的6月8日5：30执行ls命令
30   6    *      *   0   ls     指定每星期日的6:30执行ls命令
30   3   10,20     *   *   ls     每月10号及20号的3：30执行ls命令
25   8-11  *      *   *   ls     每天8-11点的第25分钟执行ls命令
*/15  *    *      *   *   ls     每15分钟执行一次ls命令
30   6   */10     *   *   ls     每个月中，每隔10天6:30执行一次ls命令
22   4    *      *   *   root   run-parts   /etc/cron.daily
#每天4：22以root身份执行/etc/cron.daily目录中的所有可执行文件，run-parts参数表示，执行后面目录中的所有可执行文件。
```



```
注意 

* *1 * * * 命令表示是每小时之内的每一分钟都执行。

必须指定在每个小时的第几分钟执行，也就是说第一个*号必须改成一个数值。

因为*号表示的就是每一分钟。

另外小时位的/1和没有区别，都是每小时一次。

如果是设置*/2，实际上是能被2整除的小时数而不是从定时设置开始2小时后执行，比如9点设的到10点就会执行。

最后可能会遇到下面这个问题

root用户下 输入 crontab -l 显示

no crontab for root 例如：

[root@CentOS ~]# crontab -l

no crontab for root

这个问题非常简单，同样在 root 用户下输入 crontab -e

按 Esc 按： wq 回车

在输入 crontab -l 就没有问题了

主要原因是由于这个liunx服务器 第一次使用 crontab ，还没有生成对应的文件导致的，执行了 编辑（crontab -e）后 就生成了这个文件
```



```
1.安装crontab

[root@CentOS ~]# yum install cronie
[root@CentOS ~]# yum install crontabs
cronie软件包是cron的主程序；

crontabs软件包是用来安装、卸装、或列举用来驱动 cron 守护进程的表格的程序。

2.开启crontab服务

service crond start //启动服务
用以下的方法启动、关闭这个cron服务：

service crond start //启动服务

service crond stop //关闭服务

service crond restart //重启服务

service crond reload //重新载入配置

查看crontab服务状态：service crond status

手动启动crontab服务：service crond start

查看crontab服务是否已设置为开机启动，执行命令：ntsysv
```



```
设置开机自动启动crond服务: 

[root@CentOS ~]# chkconfig crond on

查看各个开机级别的crond服务运行情况

[root@CentOS ~]# chkconfig –list crond

crond 0:关闭 1:关闭 2:启用 3:启用 4:启用 5:启用 6:关闭

可以看到2、3、4、5级别开机会自动启动crond服务

取消开机自动启动crond服务: 

[root@CentOS ~]# chkconfig crond off

3.设置需要执行的脚本 

新增调度任务可用两种方法：

1)、在命令行输入: crontab -e 然后添加相应的任务，wq存盘退出。
	crontab -e
	20   18    10      12   *   echo 'hi from crontab.' >sayhi.txt
	
2)、直接编辑/etc/crontab 文件，即vi /etc/crontab，添加相应的任务。

crontab -e配置是针对某个用户的，而编辑/etc/crontab是针对系统的任务

查看调度任务

crontab -l //列出当前的所有调度任务

crontab -l -u jp //列出用户jp的所有调度任务

删除任务调度工作

crontab -r //删除所有任务调度工作

直接编辑 vim /etc/crontab ,默认的文件形式如下：
```



# 远程数据库映射





```

# 远程表映射

xx测xx评远程表  映射到 3x 的xx_material 数据库 

DROP SERVER IF EXISTS AIEval_xxx_aiexam_Server;

CREATE SERVER `AIEval_xxxx_aiexam_Server`
FOREIGN DATA WRAPPER mysql
OPTIONS (
  HOST 'xx',
  PORT 3306,
  USER 'xx',
  PASSWORD 'xxx',
  DATABASE 'xxx'
);

CREATE TABLE `knowledgepoint_remote` (
     `department` VARCHAR(255) NOT NULL,
) ENGINE=FEDERATED   
CONNECTION='AIEval_xxx_aiexam_Server/knowledgepoint';


CREATE TABLE `knowledgepoint_remote` (
	`ID` INT(11) NOT NULL 
)
COMMENT='xx表（远程：xx宝xx测x的映射）'
COLLATE='utf8_unicode_ci'
ENGINE=FEDERATED
CONNECTION='AIEval_ksb_aiexam_Server/knowledgepoint';
;
```



