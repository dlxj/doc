

[TOC]



# Create



```mysql
CREATE TABLE `frequencystatistics` (
	`AppID` INT(11) NOT NULL,
	`TestCptID` INT(11) NOT NULL,
	`FrequencyJson` LONGTEXT NOT NULL COLLATE 'utf8_unicode_ci',
	PRIMARY KEY (`AppID`, `TestCptID`),
	INDEX `index_AppIDCptID` (`AppID`, `TestCptID`)
)
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB;
```





# Insert



## INSERT INTO ON DUPLICATE



```python
INSERT INTO searchkeywods (AppEName, KeyWord, Count) VALUES ('a', 'b', 1) ON DUPLICATE KEY UPDATE Count=Count+1;

```





# Query



##  Mysql Version



```mysql
SHOW VARIABLES LIKE "%version%";
```





