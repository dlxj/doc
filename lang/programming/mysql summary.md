

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





# Insert



## INSERT INTO ON DUPLICATE



```python
INSERT INTO searchkeywods (AppEName, KeyWord, Count) VALUES ('a', 'b', 1) ON DUPLICATE KEY UPDATE Count=Count+1;

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



# Update





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



