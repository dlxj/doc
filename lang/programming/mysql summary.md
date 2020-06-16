

[TOC]



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





# Insert



## INSERT INTO ON DUPLICATE



```python
INSERT INTO searchkeywods (AppEName, KeyWord, Count) VALUES ('a', 'b', 1) ON DUPLICATE KEY UPDATE Count=Count+1;

```



## Replace Into



```mysql
REPLACE INTO users (id,name,age) VALUES(123, '赵本山', 50);
REPLACE INTO users SET id = 123, name = '赵本山', age = 50;
```



# Query



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



