

F12 跳转到定义，Ctrl + "-"  返回



# 使用 "调用堆栈" 窗口

若要在 Visual Studio 中打开 " **调用堆栈** " 窗口，请从 " **调试** " 菜单中选择 " **Windows > 调用堆栈**"。 若要将本地上下文设置为堆栈跟踪显示中的特定行，请选择并按住 (或双击) 行的第一列。



# C#



```
        // 余弦相似度
        public double SimCos(List<wordToken> diffWords1, List<wordToken> diffWords2)
        {
            var allWords = (from w in diffWords1.Concat(diffWords2) group w by w.word into g select g.First()).ToList();

            // 不同的词计数（相同的词分在一个组，取list 的第一个元素和list 的长度）
            var wordCount1 = (from w in diffWords1 group w by w.word into g select (new Tuple<string, int>(g.First().word, g.ToList().Count())) ).ToList();
            var wordCount2 = (from w in diffWords2 group w by w.word into g select (new Tuple<string, int>(g.First().word, g.ToList().Count()))).ToList();

            var wordDict1 = new Dictionary<string, int>();
            var wordDict2 = new Dictionary<string, int>();

            foreach( var t in wordCount1 )
            {
                wordDict1.Add(t.Item1, t.Item2);
            }

            foreach (var t in wordCount2)
            {
                wordDict2.Add(t.Item1, t.Item2);
            }

            double v1 = 0.000000d;

            double v2 = 0.000000d;
            double v3 = 0.000000d;

            double c1, c2;
            foreach (var w in allWords)
            {
                c1 = wordDict1.ContainsKey(w.word) ? wordDict1[w.word] : 0;
                c2 = wordDict2.ContainsKey(w.word) ? wordDict2[w.word] : 0;

                v1 += c1 * c2;
                v2 += c1 * c1;
                v3 += c2 * c2;
            }
            double result = v1 / (Math.Sqrt(v2) * Math.Sqrt(v3));

            return 0;
        }
```





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



## 委托（函数指针）、匿名委托

```
https://www.cnblogs.com/sntetwt/p/5402734.html

            var dicfuncs = new Dictionary<string, Func<string, string>>();
            dicfuncs.Add("A型题、多选题|非真题|非真题|题干60以上|答案不同|干扰60以下|有解析", new Func<string, string>(delegate (string x)
            {
                return "";
            }));

            dicfuncs["A型题、多选题|非真题|非真题|题干60以上|答案不同|干扰60以下|有解析"]("");
```







# Windows

## 应用商启



```
Microsoft.WindowsStore_11810.1001.12.0_x64__8wekyb3d8bbwe

add-appxpackage -register "C:\Program Files\WindowsApps\Microsoft.WindowsStore_11810.1001.12.0_x64__8wekyb3d8bbwe*\appxmanifest.xml" -disabledevelopmentmode

```





```
【卸载Microsoft Store命令】
get-appxpackage *store* | remove-Appxpackage
卸载以后，在开始菜单中确认Microsoft Store已经移除了


【查看Microsoft Store安装包位置】
get-appxpackage -allusers | Select Name, PackageFullName
执行上面命令会列出所有Windows自带的软件，只需要找到【Microsoft.WindowsStore】以及其后面对应的安装包位置，复制后面的安装包位置：Microsoft.WindowsStore_12001.1001.5.0_x64__8wekyb3d8bbwe进行安装即可
Microsoft.WindowsStore                      Microsoft.WindowsStore_12001.1001.5.0_x64__8wekyb3d8bbwe

【安装Microsoft Store 】
add-appxpackage -register "C:\Program Files\WindowsApps\Microsoft.WindowsStore_12001.1001.5.0_x64__8wekyb3d8bbwe*\appxmanifest.xml" -disabledevelopmentmode 
安装后，开始菜单中确认Microsoft Store已经又添加回来了

#https://blog.csdn.net/sunny05296/article/details/104623355
```



