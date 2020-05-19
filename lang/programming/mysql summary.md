

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



