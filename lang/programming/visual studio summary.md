

F12 跳转到定义，Ctrl + "-"  返回



# 使用 "调用堆栈" 窗口

若要在 Visual Studio 中打开 " **调用堆栈** " 窗口，请从 " **调试** " 菜单中选择 " **Windows > 调用堆栈**"。 若要将本地上下文设置为堆栈跟踪显示中的特定行，请选择并按住 (或双击) 行的第一列。



# C#



```c#


list = new List<resultToken>();

List<resultToken>
	class resultToken
		List<Test> repeatList

list.select( token => token.repeatList.count ).ToList();



                            List<string> features1 = test.diffWords.Select(e => e.word).ToList();
                            List<string> features2 = diffTest.diffWords.Select(e => e.word).ToList();


# 试题表没有试题添加时间
desc tiku.test;

desc tiku.testchapter;
真题
	来源有“真题”两个字的是真题
	真题的年份：章节 有年份


# 正确，可以直接跑
SELECT t.appID, t.testID, t.testJson, IFNULL(sc.SourceName, '-') as SourceName,  IFNULL(sc.SubjectName, '-') as SubjectName from tiku.test t LEFT JOIN ( SELECT c.AppID, c.TestCptID, sb.SubjectName, IFNULL(s.SourceName, '-') AS SourceName FROM tiku.testchapter c LEFT JOIN tiku.subject sb ON sb.AppID = c.AppID AND sb.SbjID = c.SbjID  LEFT JOIN tiku.source s ON s.AppID = c.AppID AND s.SrcID = c.SrcID WHERE c.AppID IN (4468, 4469)  ) AS sc ON sc.AppID = t.appID and sc.TestCptID = t.TestCptID WHERE t.appID IN (4468, 4469) and `Enable`='1' ORDER BY t.TestCptID asc LIMIT 1000;

WHERE t.appID IN (4468, 4469) and `Enable`='1' AND sc.SourceName LIKE '%真题%'  ORDER BY

# 真题，正确
SELECT t.appID, t.testID, t.testJson, IFNULL(sc.SourceName, '-') as SourceName,  IFNULL(sc.SubjectName, '-') as SubjectName from tiku.test t LEFT JOIN ( SELECT c.AppID, c.TestCptID, sb.SubjectName, IFNULL(s.SourceName, '-') AS SourceName FROM tiku.testchapter c LEFT JOIN tiku.subject sb ON sb.AppID = c.AppID AND sb.SbjID = c.SbjID  LEFT JOIN tiku.source s ON s.AppID = c.AppID AND s.SrcID = c.SrcID WHERE c.AppID IN (4468, 4469)  ) AS sc ON sc.AppID = t.appID and sc.TestCptID = t.TestCptID WHERE t.appID IN (4468, 4469) and `Enable`='1' AND sc.SourceName LIKE '%真题%' ORDER BY t.TestCptID asc LIMIT 1000;


# list 去重
List<int> list = new List<int> { 1, 1, 2, 2, 3, 4, 5, 5 };
list.Distinct().ToList().ForEach(s => Console.WriteLine(s));
            DataRow[] rows = testTable.Select();

            var sourceNames = rows.Select(r => r["SourceName"].ToString()).ToList();
            var srcReals = (from s in sourceNames where s.Contains("真题") select s).ToList();
            var srcRealsSet = srcReals.Intersect(srcReals);

source
	"历年真题"
	"2020真题（网友回忆版）"

subject
	2010年5月真题


            var result = Controllers.testRepeatCheck.Compare.RealYear("2010年5月真题");
            bool isReal = result.Item1;
            int year = result.Item2;

            DataRow[] rows = testTable.Select();

            var sourceNames = rows.Select(r => r["SourceName"].ToString()).ToList();
            var srcReals = (from s in sourceNames where s.Contains("真题") select s).ToList().Distinct().ToList();
            //var srcRealsSet = srcReals.Intersect(srcReals);

            var subjectNames = rows.Select(r => r["SubjectName"].ToString()).ToList();
            var subReals = (from s in subjectNames where s.Contains("真题") select s).ToList().Distinct().ToList();


            var year = -1;
            var isReal = false;
            var groups = Regex.Match("2010年5月真题", @"(^\d+).*?(真题).*?", RegexOptions.IgnoreCase).Groups;
            if (groups.Count > 0)
            {
                isReal = true;
                if (groups.Count == 3)
                {
                    year = int.Parse(groups[1].Value);
                }
                
            }


select ts.appID,ts.testID from tiku.test ts where ts.appID in  (4468,4469) and ts.enable='1' limit 1000;


 SELECT c.AppID, c.SrcID, c.TestCptID AS CptID, sb.SubjectName, IFNULL(s.SourceName, '-') AS SourceName FROM tiku.testchapter c LEFT JOIN tiku.subject sb ON sb.AppID = c.AppID AND sb.SbjID = c.SbjID  LEFT JOIN tiku.source s ON s.AppID = c.AppID AND s.SrcID = c.SrcID WHERE c.AppID IN (4468,4469)

```



## JSON



```
https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/
```



