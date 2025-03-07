

F12 跳转到定义，Ctrl + "-"  返回



# 使用 "调用堆栈" 窗口

若要在 Visual Studio 中打开 " **调用堆栈** " 窗口，请从 " **调试** " 菜单中选择 " **Windows > 调用堆栈**"。 若要将本地上下文设置为堆栈跟踪显示中的特定行，请选择并按住 (或双击) 行的第一列。



# C++



## 中文出错

```
如果是在windows平台的 C 代码里面，执行这一句 
#pragma execution_character_set("utf-8")  // "string 以utf-8 编码"
int main() {
	system("chcp 65001");
		# 它在windows 的sdk 里定义 


项目属性 -> C/C++ -> 命令行 ->其它 
/utf-8 
	# 加这一句
	
chcp 65001
	# 临时改控件台的当前代码页

Win + R -> regedit

计算机\HKEY_CURRENT_USER\Software\Microsoft\Command Processor

AutoRun 改成 chcp 65001
	# 改完 vs2019 就能成功打印中文了
    # 改完以后任意程序只要用到控制台，都会先执行一下 chcp 65001

	
#pragma warning(disable:4996)
strcpy(line, "歧义和同义词:研究生命起源，混合词: 做B超检查身体");

errno_t err;
if ( ( err = fopen_s( &__stream, __ifile, "rb" ) ) == 0 ) {

```



```
doc\lang\programming\cpp\c64\similar\similar.c

// visual studio 源文件utf-8 编码必须要有BOM 才行
// http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=%E4%B8%A5
// https://www.sqlite.org/c3ref/create_function.html
// https://github.com/schuyler/levenshtein

# define min(x, y) ((x) < (y) ? (x) : (y))
# define max(x, y) ((x) > (y) ? (x) : (y))

// 某个utf8 字符占几个字节
// c: 必须指向utf8 字符串
static int utf8len(char *c) {
	unsigned char c1 = c[0];
	int len = -1;
	if ((c1 & 0x80) == 0) {  // 0b10000000
		len = 1;
	}
	else if ((c1 & 0xF0) == 0xF0) {  // 0b11110000
		len = 4;
	}
	else if ((c1 & 0xE0) == 0xE0) {  // 0b11100000
		len = 3;
	}
	else if ((c1 & 0xC0) == 0xC0) {  // 0b11000000 
		len = 2;
	}
	else {
		return -1;
	}
	return len;
}

/*
** Assuming z points to the first byte of a UTF-8 character,
** advance z to point to the first byte of the next UTF-8 character.
*/
// 计算字符个数
// 实现参考sqlite3 的lengthFunc 函数
static int utf8strlen(char *str) {
	int len;
	const unsigned char *z = str;
	if (z == 0) {
		return -1;
	}
	len = 0;
	while (*z){
		len++;
		//SQLITE_SKIP_UTF8(z);
		if ((*(z++)) >= 0xc0) {
			while ((*z & 0xc0) == 0x80){ z++; }
		}
	}
	return len;
}

// utf8 编码规则
/*
1字节 0xxxxxxx
2字节 110xxxxx 10xxxxxx 0xC0 0x80
3字节 1110xxxx 10xxxxxx 10xxxxxx
4字节 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
5字节 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
6字节 1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
*/
// 假定z 指向第一个utf8 字符，函数执行完以后z 指向下一个字符
static char *nextc(char *z) {
	if (z == 0) { return 0; }
	if (*z == 0) {
		return 0;
	}
	++z;
	while ((*z & 0xC0) == 0x80) { ++z; }  // 只要最高位是10 开头就继续移动指针
	return z;
}

static char *at(char *z, int pos) {
	char *t = z;
	int i;
	for (i = 0; i < pos; i++) {
		t = nextc(t);
	}
	return t;
}

static int utf8eq(char *c1, char *c2) {
	int i;
	if (c1 == 0 || c2 == 0 || *c1 == 0 || *c2 == 0) {
		return -1;
	}
	int len1 = utf8len(c1);
	int len2 = utf8len(c2);
	if (len1 != len2) {
		return 0;
	} else {
		for (i = 0; i < len1; i++) {
			if (c1[i] != c2[i]) {
				return 0;
			}
		}
	}
	return 1;
}

static unsigned int levenshtein(const char *word1_in, const char *word2_in) {
	const char *word1 = word1_in;
	const char *word2 = word2_in;
	int len1 = utf8strlen(word1),
		len2 = utf8strlen(word2);
	unsigned int *v = calloc(len2 + 1, sizeof(unsigned int));
	unsigned int i, j, current, next, cost;

	/* strip common prefixes */
	while (len1 > 0 && len2 > 0 && utf8eq(word1, word2)) {
		word1 = nextc(word1);
		word2 = nextc(word2);
		len1--;
		len2--;
	}

	/* handle degenerate cases */
	if (!len1) return len2;
	if (!len2) return len1;

	/* initialize the column vector */
	for (j = 0; j < len2 + 1; j++)
		v[j] = j;

	for (i = 0; i < len1; i++) {
		/* set the value of the first row */
		current = i + 1;
		/* for each row in the column, compute the cost */
		for (j = 0; j < len2; j++) {
			/*
			* cost of replacement is 0 if the two chars are the same, or have
			* been transposed with the chars immediately before. otherwise 1.
			*/
			cost = !(utf8eq(at(word1,i), at(word2,j)) || (i && j &&
				utf8eq(at(word1, i - 1), at(word2, j)) && utf8eq(at(word1,i), at(word2, j - 1))));
			/* find the least cost of insertion, deletion, or replacement */
			next = min(min(v[j + 1] + 1,
				current + 1),
				v[j] + cost);
			/* stash the previous row's cost in the column vector */
			v[j] = current;
			/* make the cost of the next transition current */
			current = next;
		}
		/* keep the final cost at the bottom of the column */
		v[len2] = next;
	}
	free(v);
	return next;
}

__declspec(dllexport) double __stdcall sim(char *word1, char *word2)  {
	int len1 = utf8strlen(word1);
	int len2 = utf8strlen(word2);
	int len = max(len1, len2);
	if (len == 0) {
		return -1;
	}
	int distance = levenshtein(word1, word2);
	//return distance;
	return 1 - distance / (double)len;
}

__declspec(dllexport) int __stdcall add(int a, int b) {
	return a + b;
}

#pragma execution_character_set("utf-8")  // "string 以utf-8 编码"
int main() {
	system("chcp 65001");
	//printf ("%s", at("严严ab", 0));
	char z1[] = "严严b";
	char z2[] = "严严a";
	printf("%s", at(z1, 0));
	printf("相似度：    %f\n", sim(z1, z2));
	getchar();
}


```



### VS2022 utf8

[VS2022设置编码方式为utf-8的三种方式](https://blog.csdn.net/hfy1237/article/details/129858976)

```
vs2022 -> 扩展 -> 管理扩展 -> 搜 utf8 -> 装 utf8 no bom 插件 -> 重启 vs
	# 这样以后源文件都以 utf8 保存
```





## 调试Makefile工程

[Building in Visual Studio Code with a Makefile](https://earthly.dev/blog/vscode-make/)

[VS Code搭建ARM Linux Makefile工程IDE（C/C++）](https://jackeyt.cn/[%E5%8F%B2%E4%B8%8A%E6%9C%80%E8%AF%A6%E7%BB%86]VSCode%E6%90%AD%E5%BB%BAARMLinuxMakefile%E5%B7%A5%E7%A8%8BIDE%EF%BC%88C-C++%EF%BC%89/)

[linux下使用vscode+makefile调试大型程序](https://blog.csdn.net/baidu_22429139/article/details/105125095)

[redis 目标是调试这个工程](https://github.com/redis/redis)

- [现成的](https://github.com/wenfh2020/youtobe/blob/master/redis-debug.md)



```
git clone --recursive  https://github.com/redis/redis.git && \
cd redis/src && \
vi Makefile
	# OPTIMIZATION?=-O3
	# OPTIMIZATION?=-O0  
		# 改成这个

make distclean && \
make USE_SYSTEMD=yes V=1


vi /root/redis/redis.conf
bind 0.0.0.0
daemonize yes
enable-module-command yes
	# 改成这样 

./redis-server /root/redis/redis.conf
	# 正常运行，记下它的 PID
	# 它有可能会直接后台运行，如果 lsof 6379 有输出说明正常
	

vscode 先安装 C++ 插件
	# "processId": "771184" 
		# 改成前面记下来的 PID

launch.json	
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "C/C++ Runner: Debug Session",
      "type": "cppdbg",
      "request": "attach",
      "processId": "771184",
      "program": "/root/redis/src/redis-server",
      "MIMode": "gdb",
      "miDebuggerPath": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        },
        {
          "text": "-gdb-set follow-fork-mode child",
          "ignoreFailures": true
        }
      ]
    }
  ]
}	

# 正常附加调试

vscode 在这里下一个断点，redis-cli 一连上就会成功断下
	/root/redis/src/networking.c
	client *createClient(connection *conn) {
		    if (conn) {


vscode 上开另外一个 bash

cd /src
./redis-cli --raw
keys *
MODULE LOAD /root/RedisJSON/bin/linux-x64-release/rejson.so
MODULE LOAD /root/RediSearch/bin/linux-x64-release/search/redisearch.so
	# 成功加载两个模块
MODULE LIST
	# 列出已加载模块
	# 奇怪的是，vscode 附加调试后，再加载模块就会出错，所以只能写入配置后再运行
	loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so
	loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so
		# 配置文件试入这两行，再 MODULE LIST 就可以看到正常加载了
		# 然事，这时再用 vscode 附加调试就 OK 了
		
JSON.SET product:1 $ '{"id":1,"productSn":"7437788","name":"小米8","subTitle":"全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待","brandName":"小米","price":2699,"count":1}'

JSON.SET product:2 $ '{"id":2,"productSn":"7437789","name":"红米5A","subTitle":"全网通版 3GB+32GB 香槟金 移动联通电信4G手机 双卡双待","brandName":"小米","price":649,"count":5}'

JSON.SET product:3 $ '{"id":3,"productSn":"7437799","name":"Apple iPhone 8 Plus","subTitle":"64GB 红色特别版 移动联通电信4G手机","brandName":"苹果","price":5499,"count":10}'

JSON.SET product:4 $ '{"id":4,"productSn":"7437801","name":"小米8","subTitle":"他の全文検索シリーズでも同じデータを使うので、他の記事も試す場合は wiki.json.bz2 を捨てずに残しておくことをおすすめします。","brandName":"小米","price":2699,"count":1}'

JSON.GET product:1

JSON.GET product:1 name subTitle

FT.CREATE productIdx ON JSON PREFIX 1 "product:" LANGUAGE chinese SCHEMA $.id AS id NUMERIC $.name AS name TEXT $.subTitle AS subTitle TEXT $.price AS price NUMERIC SORTABLE $.brandName AS brandName TAG

ft.search productIdx "全网通" language "chinese"

ft.search productIdx "捨てずに" language "chinese"

ft.search productIdx "てずに" language "english"


exit










# 不知道为什么，运行到一半 redis-server 自已就退出了
# 只能附加调试现在
tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "shell",
            "type": "shell",
            "command": "/usr/bin/make"
        }
    ]
}

launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "C/C++ Runner: Debug Session",
      "type": "cppdbg",
      "request": "launch",
      "args": [
        "redis.conf"
      ],
      "stopAtEntry": false,
      "externalConsole": false,
      "cwd": "${workspaceFolder}",
      "program": "${workspaceFolder}/src/redis-server",
      "MIMode": "gdb",
      "miDebuggerPath": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ],
      "environment": [],
      "preLaunchTask": "shell"
    }
  ]
}

"preLaunchTask": "shell"
	# 这一句是在调试时先执行 tasks.json 里面的命令
	
```



```
	# git submodule update --init --recursive
```

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



## .NET并发编程实战

```
第Ⅰ部分 函数式编程在并发程序中所体现的优势
第1章 函数式并发基础 3
1.1 你将从本书中学到什么 4
1.2 让我们从术语开始 5
1.2.1 顺序编程——一次执行一个任务 6
1.2.2 并发编程——同时运行多个任务 7
1.2.3 并行编程——同时执行多个任务 8
1.2.4 多任务处理——同时在一段时间内执行多个任务 9
1.2.5 多线程性能调优 10
1.3 为什么需要并发 11
1.4 并发编程的陷阱 14
1.4.1 并发的危害 14
1.4.2 共享状态的演变 17
1.4.3 一个简单的真实示例：并行快速排序 17
1.4.4 F#中的基准测试 21
1.5 为什么选择函数式编程实现并发 21
1.6 拥抱函数式范式 24
1.7 为什么选择F#和C#进行函数式并发编程 25
1.8 本章小结 27
第2章 并发函数式编程技术 29
2.1 使用函数组合解决复杂的问题 30
2.1.1 C#的函数组合 30
2.1.2 F#的函数组合 32
2.2 闭包简化函数式思考 33
2.2.1 使用lambda表达式捕获闭包中的变量 34
2.2.2 多线程环境中的闭包 36
2.3 用于程序加速的记忆化缓存技术 38
2.4 记忆快速网络爬虫的操作 42
2.5 延迟记忆化以获得更好的性能 46
2.6 有效率的并行推测以摊销昂贵计算成本 47
2.6.1 具有天然函数支持的预计算 50
2.6.2 使最佳计算获胜 51
2.7 延迟是件好事情 52
2.7.1 对严格求值语言并发行为的理解 52
2.7.2 延迟缓存技术和线程安全的单例模式 54
2.7.3 F#中的延迟支持 55
2.7.4 延迟和任务，一个强大的组合 55
2.8 本章小结 57
第3章 函数式数据结构和不可变性 59
3.1 真实世界的例子：捕猎线程不安全的对象 60
3.1.1 .NET不可变集合：一种安全的解决方案 63
3.1.2 .NET并发集合：更快的解决方案 67
3.1.3 代理消息传递模式：更快、更好的解决方案 69
3.2 在线程之间安全地共享函数式数据结构 72
3.3 修改的不可变性 73
3.3.1 数据并行的函数式数据结构 75
3.3.2 使用不可变性的性能影响 75
3.3.3 C#的不可变性 76
3.3.4 F#的不可变性 79
3.3.5 函数式列表：连接一条链中的单元格 80
3.3.6 构建可持久化数据结构：不可变二叉树 86
3.4 递归函数：一种自然的迭代方式 89
3.4.1 正确递归函数尾部：尾部调用优化 90
3.4.2 延续传递风格以优化递归函数 91
3.5 本章小结 95


第Ⅱ部分 如何处理并发程序的不同部分
第4章 处理大数据的基础：数据并行，第1部分 99
4.1 什么是数据并行 100
4.1.1 数据和任务并行 101
4.1.2 “尴尬并行”概念 102
4.1.3 .NET中的数据并行支持 102
4.2 Fork / Join模式：并行Mandelbrot 103
4.2.1 当GC是瓶颈时：结构与类对象 109
4.2.2 并行循环的缺点 111
4.3 测量性能速度 111
4.3.1 Amdahl定律定义了性能改进的极限 112
4.3.2 Gustafson定律：进一步衡量性能改进 113
4.3.3 并行循环的局限性：素数之和 113
4.3.4 简单循环可能会出现什么问题 115
4.3.5 声明式并行编程模型 117
4.4 本章小结 118
第5章 PLINQ和MapReduce：数据并行，第2部分 121
5.1 PLINQ简介 122
5.1.1 PLINQ如何更具函数式 123
5.1.2 PLINQ和纯函数：并行字计数器 123
5.1.3 使用纯函数避免副作用 125
5.1.4 隔离和控制副作用：重构并行字计数器 127
5.2 并行聚合和归约数据 128
5.2.1 择伐(Deforesting)：折叠的诸多优点之一 130
5.2.2 PLINQ中的fold：Aggregate函数 131
5.2.3 为PLINQ实现并行Reduce函数 137
5.2.4 F#的并行列表解析：PSeq 139
5.2.5 F#的并行数组 140
5.3 并行MapReduce模式 142
5.3.1 Map和Reduce函数 143
5.3.2 在NuGet 包库中使用 MapReduce 144
5.4 本章小结 149
第6章 实时事件流：函数式反应式编程 151
6.1 反应式编程: 大事件处理 152
6.2 用于反应式编程的.NET工具 155
6.2.1 事件组合器——更好的解决方案 156
6.2.2 .NET与F#组合器的互操作性 157
6.3 .NET中的反应式编程：反应式扩展(Rx) 160
6.3.1 从LINQ/PLINQ到Rx 162
6.3.2 IObservable：对偶IEnumerable 163
6.3.3 Action中的反应式扩展 164
6.3.4 Rx实时流 165
6.3.5 从事件到F# Observable 166
6.4 驯服事件流：使用Rx编程进行Twitter情绪分析 167
6.5 Rx发布者-订阅者 176
6.5.1 为强大的发布者-订阅者集线器使用Subject类型 176
6.5.2 与并发相关的Rx 177
6.5.3 实现可重用的Rx发布者-订阅者 178
6.5.4 使用Rx Pub-Sub类分析推文情绪 180
6.5.5 action中的观察者 183
6.5.6 方便的F#对象表达式 184
6.6 本章小结 184
第7章 基于任务的函数式并行 187
7.1 任务并行的简短介绍 188
7.1.1 为什么要进行任务并行和函数式编程 189
7.1.2 .NET中的任务并行化支持 189
7.2 .NET任务并行库 191
7.3 C# void的问题 196
7.4 延续传递风格(CPS)：函数式控制流程 198
7.4.1 为什么要利用CPS 199
7.4.2 等待任务完成：延续模型 200
7.5 组合任务操作的策略 205
7.5.1 使用数学模式以获得更好的组合 207
7.5.2 任务使用准则 212
7.6 并行函数式管道模式 212
7.7 本章小结 218
第8章 最终胜出的任务异步模型 219
8.1 异步编程模型(APM) 220
8.1.1 异步编程的价值 220
8.1.2 可扩展性和异步编程 223
8.1.3 CPU密集型和I/O密集型操作 223
8.2 异步编程不受限制的并行度 224
8.3 .NET的异步支持 225
8.3.1 异步编程会破坏代码结构 228
8.3.2 基于事件的异步编程 228
8.4 C#基于任务的异步编程 229
8.4.1 匿名异步lambda 232
8.4.2 Task是一个monadic容器 232
8.5 基于任务的异步编程：案例研究 235
8.5.1 异步取消 240
8.5.2 带有monadic Bind运算符的基于任务的异步组合 244
8.5.3 延迟异步计算以实现组合 245
8.5.4 如果出现问题，请重试 246
8.5.5 异步操作的错误处理 247
8.5.6 股票市场历史的异步并行处理 249
8.5.7 任务完成后的异步股票市场并行处理 251
8.6 本章小结 252
第9章 F#的异步函数编程 253
9.1 异步函数式方面 254
9.2 什么是F#异步工作流 254
9.2.1 计算表达式中的延续传递风格 254
9.2.2 异步工作流操作：Azure Blob存储并行操作 257
9.3 异步计算表达式 261
9.3.1 计算表达式和单子之间的区别 263
9.3.2 异步重试：生成自己的计算表达式 264
9.3.3 扩展异步工作流 266
9.3.4 映射异步操作：Async.map函子 267
9.3.5 并行化异步工作流：Async.Parallel 269
9.3.6 异步工作流取消支持 274
9.3.7 驯服并行异步操作 276
9.4 本章小结 280
第10章 用于流畅式并发编程的函数式组合器 281
10.1 执行流并不总是处于正常情况：错误处理 282
10.2 错误组合器：C#中的Retry、Otherwise和Task.Catch 285
10.2.1 FP中的错误处理：流控制的异常 289
10.2.2 在C#中使用Task>处理错误 291
10.2.3 F# AsyncOption类型：组合Async和Option 291
10.2.4 F#惯用的函数式异步错误处理 292
10.2.5 使用Result类型保留异常语义 294
10.3 在异步操作中控制异常 298
10.3.1 F#使用Async和Result 建模错误处理 302
10.3.2 使用monadic运算符bind扩展F# AsyncResult类型 304
10.4 使用函数式组合器抽象化操作 308
10.5 函数式组合器概要 309
10.5.1 TPL内置异步组合器 310
10.5.2 利用Task.WhenAny组合器实现冗余和交叉 311
10.5.3 使用Task.WhenAll组合器进行异步for-each 312
10.5.4 回顾迄今看到的数学模式 314
10.6 最终的并行组合应用函子 317
10.6.1 使用应用函子运算符扩展F#异步工作流 324
10.6.2 带有中缀运算符的F#应用函子语义 326
10.6.3 利用应用函子实现异构并行计算 326
10.6.4 组合和执行异构并行计算 328
10.6.5 使用条件异步组合器控制流 330
10.6.6 运用异步组合器 334
10.7 本章小结 336
第11章 使用代理应用反应式编程 339
11.1 什么是反应式编程 340
11.2 异步消息传递编程模型 342
11.2.1 消息传递和不可变性的关系 344
11.2.2 天然隔离 344
11.3 代理是什么 345
11.3.1 代理的组件 346
11.3.2 代理可以做什么 347
11.3.3 无锁并发编程的无共享方法 347
11.3.4 基于代理的编程如何体现函数式思想 348
11.3.5 代理是面向对象的 349
11.4 F#代理：MailboxProcessor 349
11.5 使用F# MailboxProcessor避免数据库瓶颈 352
11.5.1 MailboxProcessor消息类型：可区分联合 355
11.5.2 MailboxProcessor双向通信 356
11.5.3 在C#中使用AgentSQL 357
11.5.4 成组协调代理来并行工作流 358
11.5.5 如何使用F# MailboxProcessor处理错误 360
11.5.6 停止MailboxProcessor代理——CancellationToken 361
11.5.7 使用MailboxProcessor分发工作 362
11.5.8 使用代理缓存操作 364
11.5.9 由MailboxProcessor报告结果 368
11.5.10 使用线程池报告来自MailboxProcessor的事件 371
11.6 F# MailboxProcessor：10 000个代理的生命游戏 371
11.7 本章小结 376
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



# WPF



## 指定最新语言版本

- https://blog.csdn.net/liangyely/article/details/106163660

在工程文件   xxx.csproj 里修改，

LangVersion 修改为：preview

  <PropertyGroup>
	<LangVersion>preview</LangVersion>
  </PropertyGroup>
或者改为：8.0

  <PropertyGroup>
	<LangVersion>8.0</LangVersion>
  </PropertyGroup>



## 添加源码目录

- https://blog.csdn.net/yangdashi888/article/details/73323419

1.把源码目录拷贝到工程目录下

2.这时在vs的目录列表里是看不到这个目录的，在如下图工具栏中点击图标【显示所有文件】，就可以看到新增的目录了




3.这时实际上还没有真正地加入到工程中来，可见.h文件的图标是红色的，

要在工程目录上右键选择【包括在项目中】即可：



4.添加完毕，.h文件前面的图标正常了。









# 管理员权限



```
1. 打开VS的安装目录，找到devenv.exe，右键，选择“兼容性疑难解答”。

 

2. 选择“疑难解答程序”

 

3. 选择“该程序需要附加权限”

 

4. 确认用户帐户控制后，点击测试程序，不然这个对话框不让你点下一步。很蛋疼，为什么不把下一步按钮禁用了呢？

 

5. 点击“测试程序”后，VS会以管理员权限启动。这就对了。

 

6.回到兼容性疑难解答对话框，点击下一步，然后选择“是，为此程序保存这些设置”，大功告成。

 

现在，不论是直接启动VS，还是双击sln启动VS，都会以管理员身份运行了

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



