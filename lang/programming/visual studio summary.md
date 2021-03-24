

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

```c#
                    var xsd = new XSD { 
                        simTitle = repeat.test.compareResult.simTitle 
                    };

                    var xsdstr =  JsonConvert.SerializeObject(xsd);
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



```
            var dicfuncs = new Dictionary<string, Func<string, Result>>();
            dicfuncs.Add("A型题、多选题|非真题|非真题|题干相同|答案相同|干扰相同|有解析", new Func<string, Result>(delegate (string x)
            {
                // "4468/81016337/-1"  "4468/80000113/-1"
                var newer = newandold.Item1;
                var older = newandold.Item2;

                // 删除新试题
                newer.isMachineDelete = true;  // 多线程这里应该加锁

                if (newer.hasExplain && !older.hasExplain)
                {
                    thisguy.transExplain = another.testCode;
                }
                var r = new Result
                {
                    isSame = true,
                    simTitle = simTitle,
                    simRight = simRight,
                    simWrong = simWrong
                };
                return r;
            }));
```



```c#
        private static void ApplyJam(Toast toast) =>
            Console.WriteLine("Putting jam on the toast");
```







## 格式化

```C#
Console.WriteLine($"cracking {howMany} eggs");
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



# 多线程

```
https://docs.microsoft.com/zh-cn/dotnet/csharp/programming-guide/concepts/async/
	        Task sleepTask = Task.Delay(TimeSpan.FromSeconds(2));
            await sleepTask;

    public class Utils
    {
        public static async Task<string> GetStringAsync()
        {
            await Task.Delay(TimeSpan.FromSeconds(2));
            return "hi,,,,";
        }
    }


https://www.cnblogs.com/hez2010/p/async-in-dotnet.html
	Task是一个异步任务，运行在预先分配好的线程池中
```



```c#
using System;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var hi = Utils.GetStringAsync();
            var sayhi = await hi;
            Console.WriteLine(sayhi);

            Console.WriteLine("Hello World!");
        }

    }

    public class Utils
    {
        public static async Task<string> GetStringAsync()
        {

            Task sleepTask = Task.Delay(TimeSpan.FromSeconds(2));
            await sleepTask;
            return "hi,,,,";
        }
    }

}

```



```C#
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace AsyncBreakfast
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Coffee cup = PourCoffee();
            Console.WriteLine("coffee is ready");

            var eggsTask = FryEggsAsync(2);
            var baconTask = FryBaconAsync(3);
            var toastTask = MakeToastWithButterAndJamAsync(2);

            var breakfastTasks = new List<Task> { eggsTask, baconTask, toastTask };
            while (breakfastTasks.Count > 0)
            {
                Task finishedTask = await Task.WhenAny(breakfastTasks);
                if (finishedTask == eggsTask)
                {
                    Console.WriteLine("eggs are ready");
                }
                else if (finishedTask == baconTask)
                {
                    Console.WriteLine("bacon is ready");
                }
                else if (finishedTask == toastTask)
                {
                    Console.WriteLine("toast is ready");
                }
                breakfastTasks.Remove(finishedTask);
            }

            Juice oj = PourOJ();
            Console.WriteLine("oj is ready");
            Console.WriteLine("Breakfast is ready!");
        }

        static async Task<Toast> MakeToastWithButterAndJamAsync(int number)
        {
            var toast = await ToastBreadAsync(number);
            ApplyButter(toast);
            ApplyJam(toast);

            return toast;
        }

        private static Juice PourOJ()
        {
            Console.WriteLine("Pouring orange juice");
            return new Juice();
        }

        private static void ApplyJam(Toast toast) =>
            Console.WriteLine("Putting jam on the toast");

        private static void ApplyButter(Toast toast) =>
            Console.WriteLine("Putting butter on the toast");

        private static async Task<Toast> ToastBreadAsync(int slices)
        {
            for (int slice = 0; slice < slices; slice++)
            {
                Console.WriteLine("Putting a slice of bread in the toaster");
            }
            Console.WriteLine("Start toasting...");
            await Task.Delay(3000);
            Console.WriteLine("Remove toast from toaster");

            return new Toast();
        }

        private static async Task<Bacon> FryBaconAsync(int slices)
        {
            Console.WriteLine($"putting {slices} slices of bacon in the pan");
            Console.WriteLine("cooking first side of bacon...");
            await Task.Delay(3000);
            for (int slice = 0; slice < slices; slice++)
            {
                Console.WriteLine("flipping a slice of bacon");
            }
            Console.WriteLine("cooking the second side of bacon...");
            await Task.Delay(3000);
            Console.WriteLine("Put bacon on plate");

            return new Bacon();
        }

        private static async Task<Egg> FryEggsAsync(int howMany)
        {
            Console.WriteLine("Warming the egg pan...");
            await Task.Delay(3000);
            Console.WriteLine($"cracking {howMany} eggs");
            Console.WriteLine("cooking the eggs ...");
            await Task.Delay(3000);
            Console.WriteLine("Put eggs on plate");

            return new Egg();
        }

        private static Coffee PourCoffee()
        {
            Console.WriteLine("Pouring coffee");
            return new Coffee();
        }
    }

    internal class Egg
    {
        public Egg()
        {
        }
    }

    internal class Bacon
    {
    }

    internal class Toast
    {
    }

    internal class Juice
    {
    }

    internal class Coffee
    {
    }
}
```



```
using System.Collections.Concurrent;
static ConcurrentDictionary<>
```





# C# 

await一个 async 方法是由多个同步执行的程序块组成的，每个同步程序块之间由 await 语句分隔。**第一个同步程序块在调用这个方法的线程中运行，但其他同步程序块在哪里运行呢？情况比较复杂**。



```C#
SelectedItems.Select(e => e.ItemName).ToList();
```

```C#
(from e in axtest.SelectedItems where e.ItemName == anser select e).ToList();
```





```C#
(from l in tools.splitAll(content.ToString()) where l.pos != "stopWord" select l).ToList();
```

```C#
(from w in test.words orderby w.tfidf descending select w).Take(10);
```

```C#
(from t in diffList group t by t.testCode into g select g.First()).ToList();
```







# 知识空间理论



```
https://blog.csdn.net/qq_36317312/article/details/110871925

对于准确的评估出学生的在每个知识点的掌握水平，解决方案是认知诊断（Cognitive Diagnosis）。
对于快速综合测试来评估学生的认知水平，根据诊断结果出题，主要的解决方案是自适应测评（Adaptive Testing）


ALEKS
	知识空间理论
		https://zhuanlan.zhihu.com/p/139141469

	知识域 -> 有限问题(知识点)的集合Q ={q1，q2，q3，q4}


	知识状态：问题之间的关系
		不清
```



