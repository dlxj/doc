



## nuget

```
https://www.nuget.org/downloads 
	# 先下载一个最新的 nuget.exe 放 D:\usr\nuget 目录，环境变量加一下

nuget install -OutputDirectory packages # 它默认会安装在当前目录，这里指定安装在packages 目录

	# edgejs 高版本会出错，安装 9.3.4 版，如果编译出现复制文件出错，那就先卸载，再安装一次
	# 缺少的dll从这里复制 C:\Users\i\.nuget\packages\paddleocrsharp\2.2.0\build\PaddleOCRLib

packages.config
	# D:\GitHub\echodict\cut

<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="cef.redist.x64" version="108.4.13" targetFramework="net461" />
  <package id="cef.redist.x86" version="108.4.13" targetFramework="net461" />
  <package id="CefSharp.Common" version="108.4.130" targetFramework="net461" />
  <package id="CefSharp.WinForms" version="108.4.130" targetFramework="net461" />
  <package id="EdgeJs" version="9.3.4" targetFramework="net461" />
  <package id="MaterialSkin.2" version="2.3.1" targetFramework="net461" />
  <package id="Newtonsoft.Json" version="13.0.2" targetFramework="net461" />
  <package id="PaddleOCRSharp" version="2.2.0" targetFramework="net461" />
  <package id="System.Reflection.Emit" version="4.7.0" targetFramework="net461" />
  <package id="Tesseract" version="5.2.0" targetFramework="net461" />
</packages>
```



## .net core



```
        // /home/data/users/xxx/soft/dotnet ainlp.dll
        // /home/data/users/xxx/project/smartsearch

        // curl -d "" "http://localhost:63164/api/smarsearch/search"
        // 要禁止强制跳转，只需要在项目的 Startup.cs 程序的 Configure 方法中注释掉 “app.UseHttpsRedirection();” 这一行代码即可。
```



```
# html标签不转义，原样输出
@((MarkupString)@row.jp)
```





## LINQPad

```
LINQPad的优点
快速POC
POC是指概念验证，比如开发过程中遇到以下这类情况：

Dictionary使用.Add()添加相同的key，是否会报错？（会）
数组形式的JToken，转字符串数组string[]应该用强转？还是用.ToArray<string>()？还是.ToObject<string[]>()？
ASP.NET Core获取远程IPv6地址，使用Connection.RemoteIpAddress是否可行？（可行）
Newtonsoft.Json与System.Text.Json相比，反序列化性能哪个好？耗时、内存分配各相差多少倍？（…）
面对这些问题，下意识地会想必须要做实验——不然到了测试时甚至生产环境时才暴露出来就太迟了。而做实验就要写代码——而这个做实验的过程，就叫POC——Proof of Concept。
```







## datatime

```c#
            int unixTimestamp = ((int)DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1)).TotalSeconds);
            DateTime ConvertedUnixTime = DateTimeOffset.FromUnixTimeSeconds(unixTimestamp).DateTime;
            string batch = ConvertedUnixTime.ToString("yyyy-MM-dd HH:mm:ss");
```



## Grammar



### Switch



```C#
            <span style="color:@(days switch { _ when days > 3 => "#ccc", _ when days > 0 => "#ffd800", _ => "#ff0000" })">
                @Item.Deadline?.ToShortDateString()
            </span>
```



```
// C# switch
					system = systemStr switch
                    {
                        "1" => RomajiSystem.Nippon,
                        "2" => RomajiSystem.Passport,
                        "3" => RomajiSystem.Hepburn,
                        _ => RomajiSystem.Hepburn
                    };
```





## Json



```
using Newtonsoft.Json;
JObject json = (JObject)JsonConvert.DeserializeObject(message);
json["outPath"].ToString(), json["list"].Value<JArray>(), json["fileType"].Value<string>(), json["startPage"].Value<int>()
```







Newtonsoft.Json



```c#
json["status"].Value<int>() != 200
```



```c#
            // 没有中文，认为是乱码
            if (Util.unAZchinese_remove(strSearch) == "")
            {
                var ret = new
                {
                    keywords = "",
                    type = -1,
                    testlist = new { }
                };

                return new JsonResult(new { status = 200, msg = "输入为乱码", data = ret });
            }
```





```
var strtk = Newtonsoft.Json.JsonConvert.SerializeObject(tk);

Regex rex = new Regex(@"\r\n|\r|\n|\t|\s", RegexOptions.IgnoreCase);
context = rex.Replace(context, "");
var contextJson = (JObject)JsonConvert.DeserializeObject(context);
```





```c#
# 不需要事先定义结构
JsonConvert.SerializeObject( new {
                                simTitle = xx,
                                simRight = xx
                            }
```





```
         
         Newtonsoft.Json 动态添加字段
         
         
         var data = new
            {
                mobile = "18888888888",
                company = "1",
                isTravel = "1",
                invoiceId = "1",
                serialId = "fd580000000f670"
            };

            var str = Newtonsoft.Json.JsonConvert.SerializeObject(data);

            //动态添加memberId
            var obj = JObject.Parse(str);
            obj.Add("memberId", "123456789");

            //动态添加clientInfo，这个clientInfo下面又有一级对象
            JObject jObject = new JObject();
            jObject.Add("VersionNumber", "1.4.1");
            obj.Add("clientInfo", jObject);

            var result = obj.ToString();
            Console.WriteLine(result);
```



```

# https://github.com/zanders3/json


var lst = new List<Dictionary<string, string>>();
            lst.Add( new Dictionary<string, string>() { { "simTitle", (0.7142857142857143).ToString() } } );
            lst.Add(new Dictionary<string, string>() { { "simRight", (1.0).ToString() } });
            lst.Add(new Dictionary<string, string>() { { "simWrong", (1.0).ToString() } });
            lst.Add(new Dictionary<string, string>() { { "maincode", "009725" } });

            var js = lst.ToJson();

            var test = "{ \"simTitle\":0.7142857142857143,\"simRight\":1.0,\"simWrong\":1.0, \"maincode\":\"009725\"}".FromJson<object>();
            var teststr = test.ToJson();
```



### 数组

```
# https://blog.csdn.net/stwuyiyu/article/details/79170019

Linq to JSON是用来操作JSON对象的.可以用于快速查询,修改和创建JSON对象.当JSON对象内容比较复杂,而我们仅仅需要其中的一小部分数据时,可以考虑使用Linq to JSON来读取和修改部分的数据而非反序列化全部.

二.创建JSON数组和对象
在进行Linq to JSON之前,首先要了解一下用于操作Linq to JSON的类.

类名	说明
JObject
 用于操作JSON对象
JArray
 用语操作JSON数组
JValue
 表示数组中的值
JProperty
 表示对象中的属性,以"key/value"形式
JToken
 用于存放Linq to JSON查询后的结果

```



```c#
            var datalist = new JArray();

            foreach (DataRow row in appTable.Rows)
            {
                string AppID = row["AppID"].ToString();
                string CName = row["CName"].ToString();
                string AppEname = row["AppEname"].ToString();

                datalist.Add( new JObject { { "AppID", AppID }, { "CName", CName }, { "AppEname", AppEname } } );

            }

            var ret = datalist.ToString();
```



```c#
# 从字符串解析出数组

			var datalist = new JArray();
            datalist.Add(new JObject { { "AppID", 1 }, { "CName", 1 }, { "AppEname", 1 } });

            var s = datalist.ToString();

            JArray jar = JArray.Parse(s);
            foreach( JObject jo in jar)
            {
                string appid =  jo["AppID"].ToString();
            }
```





## System.Text.Json



```
# https://stackoverflow.com/questions/58271901/converting-newtonsoft-code-to-system-text-json-in-net-core-3-whats-equivalent/58273914

//https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-8#using-declarations 
using var doc = JsonDocument.Parse(json);

//Print the property names.
var names = doc.RootElement.EnumerateObject().Select(p => p.Name);
Console.WriteLine("Property names: {0}", string.Join(",", names)); // Property names: status,message,Log_id,Log_status,FailureReason

//Re-serialize with indentation.
using var ms = new MemoryStream();
using (var writer = new Utf8JsonWriter(ms, new JsonWriterOptions { Indented = true }))
{
    doc.WriteTo(writer);
}
var json2 = Encoding.UTF8.GetString(ms.GetBuffer(), 0, checked((int)ms.Length));

Console.WriteLine(json2);
```



```c#

# https://dotnetfiddle.net/OSaW78

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Reflection;

using System.Text.Json;
using System.Text.Json.Serialization;

using NUnit.Framework; // Throws NUnit.Framework.AssertionException

//https://stackoverflow.com/questions/58271901/converting-newtonsoft-code-to-system-text-json-in-net-core-3-whats-equivalent

	public class ResponseJson
	{
		[JsonPropertyName("status")]
		public bool Status { get; set; }
		[JsonPropertyName("message")]
		public string Message { get; set; }
		[JsonPropertyName("Log_id")]
		public string LogId { get; set; }
		[JsonPropertyName("Log_status")]
		public string LogStatus { get; set; }

		public string FailureReason { get; set; }
	}

    class TestClass
    {
        public static void Test()
        {
			var response = new ResponseJson
			{
				Status = true, 
				Message = "my message",
				LogId = "my log id",
				LogStatus = "my log status",
				FailureReason = "my failure reason"
			};
			
			var options = new JsonSerializerOptions
			{
				WriteIndented = false,
			};
			var json = JsonSerializer.Serialize(response, options);

			Console.WriteLine("Serialized {0}", response);
			Console.WriteLine(json);
			
			Console.WriteLine("\nParsing JSON using JsonDocument.Parse:");
			
			//https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-8#using-declarations 
			using var doc = JsonDocument.Parse(json);
			
			var names = doc.RootElement.EnumerateObject().Select(p => p.Name);
			Console.WriteLine("Property names: {0}", string.Join(",", names)); // Property names: status,message,Log_id,Log_status,FailureReason
			
			using var ms = new MemoryStream();
			using (var writer = new Utf8JsonWriter(ms, new JsonWriterOptions { Indented = true }))
			{
				doc.WriteTo(writer);
			}
			var json2 = Encoding.UTF8.GetString(ms.GetBuffer(), 0, checked((int)ms.Length));
			
			Console.WriteLine(json2);
		}	
	}


	public class Program
	{
		public static void Main()
		{
			Console.WriteLine("Environment version: {0} ({1})", System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription , GetNetCoreVersion());
			Console.WriteLine();

			try
			{
				TestClass.Test();
			}
			catch (Exception ex)
			{
				Console.WriteLine("Failed with unhandled exception: ");
				Console.WriteLine(ex);
				throw;
			}
		}
		
		public static string GetNetCoreVersion()
		{
			//https://techblog.dorogin.com/how-to-detect-net-core-version-in-runtime-ecd65ad695be
			//
			var assembly = typeof(System.Runtime.GCSettings).GetTypeInfo().Assembly;
			var assemblyPath = assembly.CodeBase.Split(new[] { '/', '\\' }, StringSplitOptions.RemoveEmptyEntries);
			int netCoreAppIndex = Array.IndexOf(assemblyPath, "Microsoft.NETCore.App");
			if (netCoreAppIndex > 0 && netCoreAppIndex < assemblyPath.Length - 2)
				return assemblyPath[netCoreAppIndex + 1];
			return null;
		}
	}

```



```c#
WeatherForecast Deserialize(string json)
{
    var options = new JsonSerializerOptions
    {
        AllowTrailingCommas = true
    };
    return JsonSerializer.Parse<WeatherForecast>(json, options);
}

class WeatherForecast {
    public DateTimeOffset Date { get; set; }

    // Always in Celsius.
    [JsonPropertyName("temp")]
    public int TemperatureC { get; set; }

    public string Summary { get; set; }

    // Don't serialize this property.
    [JsonIgnore]
    public bool IsHot => TemperatureC >= 30;
}
```







## 正则



```c#
                Regex r = new Regex(@"[^0-9,]*");
                srcList = r.Replace(srcList, "");
```



```c#
        // 移除非中文、26个英文字母以外的字符
        static public string unAZchinese_remove(string s)
        {
            return Regex.Replace(s, @"[^\u4e00-\u9fa5^a-z^A-Z]", "");
        }
```



```c#
# 重复两次以上
		str = Regex.Replace(str, "\\{2,}\"", "");
        str = Regex.Replace(str, "\\{2,}n", "");
```



### 斜杠的匹配



```c#
# "\" 需要\\\\ 来表示，就是转义成 \\
string strr = "<font face=\"黑体\" size=\"45\" color=\"#4b3d2e\">{\\an7}</font>";
string content = Regex.Replace(strr, "{\\\\an7}", "");
```



### Replace

```c#
 content = Regex.Replace(content, "{\\\\an7}", "");  # 转义后是 \\ 用于替换 \
```





### 出现次数

```c#
            Regex RegexWords = new Regex("a");
            int WordCount = RegexWords.Matches("a321adfklsaabcd2a").Count;
```



### 分组

```c#
# https://www.cnblogs.com/stu-acer/archive/2010/01/23/1655011.html
Regex regex = new Regex(@"(\d+)/(\d+)");

MatchCollection matches = regex.Matches(@"最后比分是：19/24");

//show matches

Console.WriteLine("////////////////----------------------------------////////////////");

foreach(Match m in matches)

{

//Console.WriteLine("match string is: \"{0}\", length: {1}", // m.Value.ToString(), m.Value.Length);

foreach(string name in regex.GetGroupNames())

{

Console.WriteLine("\r capture group \"{0}\" value is:\"{1}\""

, name, m.Groups[name].Value);

}

}

Console.WriteLine("matched count: {0}", matches.Count);

输出：

////////////////----------------------------------////////////////

capture group "0" value is:"19/24"

capture group "1" value is:"19"

capture group "2" value is:"24"

matched count: 1
```



```c#
            //string x = "Live for nothing,die for something";

            //string y = "Live for nothing,die for somebody";

            //Regex r = new Regex(@"^Live ([a-z]{3}) no([a-z]{5}),die \1 some\2$");

            //Console.WriteLine("x match count:" + r.Matches(x).Count);//1  

            //Console.WriteLine("y match count:" + r.Matches(y).Count);//0  

            ////正则表达式引擎会记忆“()”中匹配到的内容，作为一个“组”，  
            ////并且可以通过索引的方式进行引用。表达式中的“\1”，  
            ////用于反向引用表达式中出现的第一个组，即粗体标识的第一个括号内容，“\2”则依此类推。  

            //string x = "Live for nothing,die for something";
            //Regex r = new Regex(@"^Live for no([a-z]{5}),die for some\1$");
            //if (r.IsMatch(x))
            //{
            //    Console.WriteLine("group1 value:" + r.Match(x).Groups[1].Value);//输出：thing  
            //}
            ////获取组中的内容。注意，此处是Groups[1]，  
            ////因为Groups[0]是整个匹配的字符串，即整个变量x的内容。  

            //string x = "Live for nothing,die for something";
            //Regex r = new Regex(@"^Live for no(?﹤g1﹥[a-z]{5}),die for some\1$");
            //if (r.IsMatch(x))
            //{
            //    Console.WriteLine("group1 value:" + r.Match(x).Groups["g1"].Value);
            //    //输出：thing  
            //}
            ////可根据组名进行索引。使用以下格式为标识一个组的名称(?﹤groupname﹥…)。  

            //string x = "Live for nothing nothing";
            //Regex r = new Regex(@"([a-z]+) \1");
            //if (r.IsMatch(x))
            //{
            //    x = r.Replace(x, "$1");
            //    Console.WriteLine("var x:" + x);//输出：Live for nothing  
            //}
            //删除原字符串中重复出现的“nothing”。在表达式之外，  
            //使用“$1”来引用第一个组，下面则是通过组名来引用：  
            string x = "Live for nothing nothing";
            Regex r = new Regex(@"(?﹤g1﹥[a-z]+) \1");
            if (r.IsMatch(x))
            {
                x = r.Replace(x, "${g1}");
                Console.WriteLine("var x:" + x);//输出：Live for nothing  
            }

            string x = "Live for nothing";
            Regex r = new Regex(@"^Live for no(?:[a-z]{5})$");
            if (r.IsMatch(x))
            {
                Console.WriteLine("group1 value:" + r.Match(x).Groups[1].Value);//输出：(空)  
            }
            //在组前加上“?:”表示这是个“非捕获组”，即引擎将不保存该组的内容。  
```



### 平衡组 递归匹配



```
https://www.cnblogs.com/qiantuwuliang/archive/2011/06/11/2078482.html
```

- (**?'group') 把捕获的内容命名为group,并压入堆栈(Stack)**
- (?'-group') 从堆栈上弹出最后压入堆栈的名为group的捕获内容，如果堆栈本来为空，则本分组的匹配失败
- (?(group)yes|no) 如果堆栈上存在以名为group的捕获内容的话，继续匹配yes部分的表达式，否则继续匹配no部分
- (?!) 零宽负向先行断言，由于没有后缀表达式，试图匹配总是失败

第一个就 是在黑板上写一个"group"，第二个就是从黑板上擦掉一个"group"，第三个就是看黑板上写的还有没有"group"，如果有就继续匹配yes部 分，否则就匹配no部分。

我们需要做的是每碰到了左括号，就在压入一个"Open",每碰到一个右括号，就弹出一个，到了最后就看看堆栈是否为空－－如果不为空那就证明左括号比右括号多，那匹配就应该失败。正则表达式引擎会进行回溯(放弃最前面或最后面的一些字符)，尽量使整个表达式得到匹配。





## 乱码解决



```
            string aa =  @"\u4E94\u5473";
            string bb = System.Text.RegularExpressions.Regex.Unescape(aa);
            
            --> 五味
```







##　去重



https://www.jianshu.com/p/c38baf286dd7



```

public class Comparer: IEqualityComparer<TBINPN>
{
    public bool Equals(TBINPN x, TBINPN y)
    {
        //这里定义比较的逻辑
        return x.ID == y.ID && x.PN == y.PN;
    }

    public int GetHashCode(TBINPN obj)
    {
        //返回字段的HashCode，只有HashCode相同才会去比较
        return obj.ID.GetHashCode();
    }
}

List<TBINPN> newTbinpns = tbinpns.Distinct(new Comparer()).ToList();

```



## 不回收内存

```
System.GC.SuppressFinalize(obj);
```





## Get 请求



```c#
# 返回字节 
    	// http://localhost:5000/search/getaudio?id=1
		[HttpGet("getaudio")]
        public async Task<IActionResult> getaudio()
        {
            string id = "1";

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录

            string dir_audio = Path.Combine(ecxutePath, "audio");

            if ( !Directory.Exists(dir_audio) )
            {
                Directory.CreateDirectory(dir_audio);
            }

            if (Request.Query.ContainsKey("id"))
            {
                id = Request.Query["id"].ToString();
            }

            string audioPath = Path.Combine(dir_audio, id + ".mp3");

            if (!System.IO.File.Exists(audioPath))
            {
                if (!anime.initQ)
                {
                    anime.initConn();
                }

                anime.g_conn.Open();

                string sql = $"SELECT id, audio FROM anime WHERE id={id};";

                using (var cmd = new NpgsqlCommand(sql, anime.g_conn))
                {
                    NpgsqlDataReader reader = await cmd.ExecuteReaderAsync();
                    if (reader.HasRows)
                    {
                        while (reader.Read())
                        {
                            string idd = reader["id"].ToString();
                            byte[] audio = (byte[])reader["audio"];

                            try
                            {
                                System.IO.File.WriteAllBytes(audioPath, audio);
                            } catch(Exception ex)
                            {
                                Console.WriteLine("### ERROR: 写入audio 失败. " + ex.Message);
                                throw new Exception(ex.Message);
                            }

                        }
                    }
                }

                anime.g_conn.Close();

            }

            var memory = new MemoryStream();
            using (var stream = new FileStream(audioPath, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                await stream.CopyToAsync(memory);
            }
            memory.Position = 0;
            //var types = GetMimeTypes();
            //var ext = Path.GetExtension(filePath).ToLowerInvariant();
            return File(memory, "audio/mpeg", "tmp.mp3");

        }
```





```
1.简单发送Get请求

/// <summary>
/// 指定Url地址使用Get 方式获取全部字符串
/// </summary>
/// <param name="url">请求链接地址</param>
/// <returns></returns>
public static string Get(string url)
{
    string result = "";
    HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
    HttpWebResponse resp = (HttpWebResponse)req.GetResponse();
    Stream stream = resp.GetResponseStream();
    try
    {
        //获取内容
        using (StreamReader reader = new StreamReader(stream))
        {
            result = reader.ReadToEnd();
        }
    }
    finally
    {
        stream.Close();
    }
    return result;
}
2.带请求参数的Get方法
/// <summary>
/// 发送Get请求
/// </summary>
/// <param name="url">地址</param>
/// <param name="dic">请求参数定义</param>
/// <returns></returns>
public static string Get(string url, Dictionary<string, string> dic)
{
    string result = "";
    StringBuilder builder = new StringBuilder();
    builder.Append(url);
    if (dic.Count > 0)
    {
        builder.Append("?");
        int i = 0;
        foreach (var item in dic)
        {
            if (i > 0)
                builder.Append("&");
            builder.AppendFormat("{0}={1}", item.Key, item.Value);
            i++;
        }
    }
    HttpWebRequest req = (HttpWebRequest)WebRequest.Create(builder.ToString());
    //添加参数
    HttpWebResponse resp = (HttpWebResponse)req.GetResponse();
    Stream stream = resp.GetResponseStream();
    try
    {
        //获取内容
        using (StreamReader reader = new StreamReader(stream))
        {
            result = reader.ReadToEnd();
        }
    }
    finally
    {
        stream.Close();
    }
    return result;
}

3.自定义指定Http请求头，自定义指定编码解析返回结果
HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
req.Method = "GET";
req.Headers["Accept-Language"] = "zh-CN,zh;q=0.8";
req.Referer = "https://www.baidu.com/";
HttpWebResponse resp = (HttpWebResponse)req.GetResponse();
Stream stream = resp.GetResponseStream();
string result = "";
//注意，此处使用的编码是：gb2312
//using (StreamReader reader = new StreamReader(stream, Encoding.Default))
using (StreamReader reader = new StreamReader(stream, Encoding.GetEncoding("gb2312")))
{
    result = reader.ReadToEnd();
}

```



## Post



```C#
namespace ksb_aiexam.Controllers
{

    [Route("api/[controller]")]
    [ApiController]
    public class ksbaiexamController : ControllerBase
    {
        [HttpPost("gettest")]
        public JsonResult gettest()
        {

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            string prms = Request.Form["params"];

            return new JsonResult(new { status = 200, msg = "success.", data = prms });
        }
    }
}
```





```

        public static void Main(string[] args)
        {
        
        Stopwatch stopw = new Stopwatch();

            stopw.Start();
            
            stopw.Stop();
            Console.WriteLine(string.Format("加载完成,耗时{0}", stopw.Elapsed.TotalSeconds + "s"));

            CreateHostBuilder(args).Build().Run();
        
        }
        
                public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {

                    webBuilder.UseStartup<Startup>().ConfigureAppConfiguration(builder =>
                    {
                        builder.AddJsonFile("host.json");
                    });
                });
                
                
                


namespace xxx.Controllers.SmartSearch
{
    [Route("api/[controller]")]
    [ApiController]
    public class smarsearchController : ControllerBase
    {
    
            [HttpPost("search")]
        public JsonResult search()
        {

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            string prms = Request.Form["params"];


            string typeSearch = null;
            string strSearch = null;
            string appList = null;

            Dictionary<string, string> prmsJson = null;
            if (prms == null || prms == "")
            {
                return new JsonResult(new
                {
                    status = 201,
                    msg = "参数为空",
                    data = new JArray()
                });
            }
            else
            {
                try
                {
                    prmsJson = JsonConvert.DeserializeObject<Dictionary<string, string>>(prms);
                    typeSearch = prmsJson["type"];
                    strSearch = prmsJson["search"];

                    appList = prmsJson["appList"];

                    if (!"1,2,3,4".Contains(typeSearch))
                    {
                        return new JsonResult(new
                        {
                            status = 201,
                            msg = "参数错误",
                            data = new JArray()
                        });
                    }

                    if (strSearch == "")
                    {
                        return new JsonResult(new
                        {
                            status = 201,
                            msg = "参数为空",
                            data = new JArray()
                        });
                    }

                }
                catch (Exception)
                {
                    return new JsonResult(new
                    {
                        status = 201,
                        msg = "参数json 解析错误",
                        data = new JArray()
                    });
                }
            }
    
    }
}
```





```
 public static List<wordToken> Get(string url)
        {

            string result = "";
            HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);

            req.Method = "GET";
            req.ContentType = "application/json; charset=utf-8";
            req.Timeout = 20000;

            HttpWebResponse resp = (HttpWebResponse)req.GetResponse();

            Stream stream = resp.GetResponseStream();
            try
            {
                //获取内容
                using (StreamReader reader = new StreamReader(stream, Encoding.GetEncoding("utf-8")))
                {
                    result = reader.ReadToEnd();
                }
            }
            finally
            {
                stream.Close();
            }

            result = System.Text.RegularExpressions.Regex.Unescape(result);  //  \u4E94\u5473  会被替换成 “五味”


            List<wordToken> wordsSearch = new List<wordToken>();

            JArray jar = JArray.Parse(result);
            foreach (JObject jo in jar)
            {
                wordToken to = new wordToken
                {
                    word = jo["word"].ToString(),
                    pos = jo["type"].ToString(),
                    enable = true,
                    tf = double.Parse(jo["tf"].ToString()),
                    tfidf = double.Parse(jo["tfidf"].ToString())
                };

                wordsSearch.Add(to);

            }

            return wordsSearch;
        }

        // [{id:"1",context:"\"用药错误\"A级（1级）的标准"}]


        public static List<wordToken> Post(string url, string str)
        {


            // "assist" "pro" "stopWord"


            var datalist = new JArray();
            datalist.Add(new JObject { { "id", 1 }, { "context", str } });

            var content = datalist.ToString();


            // 以键值对的形式Post
            StringBuilder buffer = new StringBuilder();
            buffer.AppendFormat("&{0}={1}", "array", content);


            string result = "";
            HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
            req.Method = "POST";
            req.ContentType = "application/x-www-form-urlencoded";


            byte[] kvdata = Encoding.UTF8.GetBytes(buffer.ToString());
            req.ContentLength = kvdata.Length;

            using (Stream strm = req.GetRequestStream())
            {
                strm.Write(kvdata, 0, kvdata.Length);
            }

            using (Stream strm = req.GetResponse().GetResponseStream())
            {
                using (StreamReader reader = new StreamReader(strm, Encoding.UTF8))
                {
                    result = reader.ReadToEnd();
                }
            }

            result = System.Text.RegularExpressions.Regex.Unescape(result);  //  \u4E94\u5473  会被替换成 “五味”


            JObject job = JObject.Parse(result);
            var status = job["status"].ToString();
            if (status != "200")
            {

            }

            List<wordToken> wordsSearch = new List<wordToken>();

            JArray jar = JArray.Parse(job["data"].ToString());
            foreach (JObject jo in jar[0]["words"])
            {
                wordToken to = new wordToken
                {
                    word = jo["word"].ToString(),
                    pos = jo["type"].ToString(),
                    enable = true,
                    tf = double.Parse(jo["tf"].ToString()),
                    tfidf = double.Parse(jo["tfidf"].ToString())
                };

                wordsSearch.Add(to);

            }

            return wordsSearch;

        }
```



## 长连接



```c#
      但除了程序本身的原因，还有可能是客服端访问造成（当然这个客户端也包含如蜘蛛软件等搜索引擎），如果服务器和客户端建立的是长链接(可以用"netstat -a"命令查看网络访问信息)，这就需要对http响应头的connection做一定的设置。

      介绍如下：

 

1. 解释一下：

 

    在http1.1中request和reponse header中都有可能出现一个connection头字段，此header的含义是当client和server通信时对于长链接如何进行处理。

    在http1.1中，client和server都是默认对方支持长链接的， 如果client使用http1.1协议，但又不希望使用长链接，则需要在header中指明connection的值为close；如果server方也不想支持长链接，则在response中也需要明确说明connection的值为close.

    不论request还是response的header中包含了值为close的connection，都表明当前正在使用的tcp链接在请求处理完毕后会被断掉。以后client再进行新的请求时就必须创建新的tcp链接了。 HTTP Connection的 close设置允许客户端或服务器中任何一方关闭底层的连接双方都会要求在处理请求后关闭它们的TCP连接。

 

2.如何在程序中设置：

 

    可以在过滤器中加入：response.setHeader("connection", "close");

 

 

 

与之相关：解决服务器产生大量close_wait问题

 

 

要解决这个问题的可以修改系统的参数(/etc/sysctl.conf文件)，系统默认超时时间的是7200秒，也就是2小时。

默认如下：

tcp_keepalive_time = 7200 seconds (2 hours)
tcp_keepalive_probes = 9
tcp_keepalive_intvl = 75 seconds

 

意思是如果某个TCP连接在idle 2个小时后,内核才发起probe.如果probe 9次(每次75秒)不成功,内核才彻底放弃,认为该连接已失效

 

修改后

 

sysctl -w net.ipv4.tcp_keepalive_time=30
sysctl -w net.ipv4.tcp_keepalive_probes=2
sysctl -w net.ipv4.tcp_keepalive_intvl=2

 

经过这个修改后，服务器会在短时间里回收没有关闭的tcp连接。
```







## String



var ext = Path.GetExtension(filePath).ToLowerInvariant();



### 不转义



```c#
 // @禁止转义符内部用两个双引"" 表示单个双引，否则出现语法错误 
                    using (var cmd = new NpgsqlCommand(@"
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab(""use_base_form"", true, ""include_reading"", true)')

        LOOP

            reading = (js-> 'metadata'->> 'reading');
                    IF reading IS NULL THEN
                            RETURN 0;
                    END IF;

                    END LOOP;
                    END LOOP;

                    RETURN 1;

                    END;
$func$ LANGUAGE plpgsql IMMUTABLE;
                    ", conn))
                    {
                        cmd.ExecuteNonQuery();
                    }


                    conn.Close();

                }
```



### 动态计算



```c#
string prms = $" {{ \"keyword\" : \"{Request.Form["keyword"]}\", \"lang_select\": \"{Request.Form["lang_select"]}\" }} ";  // $ 里面的 { 要双写进行转义
```





### 拼接



```c#
# {} 里面的是动态计算
string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
```



### Split



```c#
# 以string 作为 delimiter
string beginTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
string endTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();
```





### String join

```
string.Join(",", wmids.appids.Keys.ToList());
```



### IsNullOrWhiteSpace

```
string.IsNullOrWhiteSpace(Body)
# See below: markdig
```





### UTF8

```c#
# https://github.com/madelson/MedallionShell/blob/master/SampleCommand/Program.cs

var encoding = args.Contains("--utf8") ? new UTF8Encoding(encoderShouldEmitUTF8Identifier: false)
                        : args.Contains("--utf162") ? new UnicodeEncoding(bigEndian: false, byteOrderMark: false)
                        : default(Encoding);
                    if (encoding != null)
                    {
                        Console.InputEncoding = Console.OutputEncoding = encoding;
                    }
```







## List



```c#
static List<string[]> apps = new List<string[]>() { new string[] { "a", "b", "b", "2401", "2906" }
};
```





### List 交集



```
 List<char> a = new List<char>();
            List<char> b = new List<char>();
            foreach (wordToken w in diffWords1)
            {
                a.AddRange(w.word.ToList<char>());
            }
            foreach (wordToken w in diffWords2)
            {
                b.AddRange(w.word.ToList<char>());
            }
            //并集
            var union = a.Union(b).Count();
            //交集
            var intersection = a.Intersect(b).Count();

            var score = Convert.ToDouble(intersection) / Convert.ToDouble(union);
```





### IEnumerable



```c#
public IEnumerable<People> peopleList => new List<People> {
```





## Tuple



```c#
var (begintime, endtime) = new Tuple<int, int>(1, 1);
```





## Dictionary



```c#
    private async void HandleSubmit()
    {
        var values = new Dictionary<string,string>{
            { "keyword", "hello" },
            { "lang_select", "jp" }
        };

        var content = new FormUrlEncodedContent(values);
        var response = await client.PostAsync("http://www.example.com/recepticle.aspx", content);
        var responseString = await response.Content.ReadAsStringAsync();
    }
```









## 字典排序



```c#
# 双排序
dict.OrderByDescending(i => i.Value).ThenBy(i => i.Key)
```



```c#
# SortedDictionary 排序
dic_orders 输入key 会返回一个int ，作为顺序的定义

dic_testmenutree[AppID] = new SortedDictionary<string, SortedDictionary<string, List<string>>>(new SourceComparer(dic_orders));

public class SourceComparer : IComparer<string>
{
    Dictionary<string, int> dic_orders;

    public SourceComparer(Dictionary<string, int> dic_orders)
    {
        this.dic_orders = dic_orders;
    }
    public int Compare(string x, string y)
    {
        return dic_orders[x].CompareTo(dic_orders[y]);
    }
}
```



```
var D = new SortedDictionary<int, string>();
var qD = from kvp in D
         orderby kvp.Value
         select kvp
;
```





```C#
# https://csharpsage.com/sort-dictionary-by-key/
var fruit = new Dictionary<string, int>
{
    ["apple"] = 1,
    ["pear"] = 4,
    ["banana"] = 6,
};
foreach (var item in fruit.OrderByDescending(x => x.Key))
{
    Console.WriteLine(item);
}
```



```C#
public class KeyComparer<TItem, TKey> : Comparer<TItem>
{
    private readonly Func<TItem, TKey> extract;
    private readonly IComparer<TKey> comparer;

    public KeyComparer(Func<TItem, TKey> extract)
        : this(extract, Comparer<TKey>.Default)
    { }

    public KeyComparer(Func<TItem, TKey> extract, IComparer<TKey> comparer)
    {
        this.extract = extract;
        this.comparer = comparer;
    }

    public override int Compare(TItem x, TItem y)
    {
        // need to handle nulls
        TKey xKey = extract(x);
        TKey yKey = extract(y);
        return comparer.Compare(xKey, yKey);
    }
}


SortedDictionary<string, int> sortDict = new SortedDictionary<string, int>(
    new KeyComparer<string, string>(s => new string(s.Reverse().ToArray())));
    
    
```



## 字典 filter



```c#
dic = dic.Where(p => p.Key == 1)
         .ToDictionary(p => p.Key, p => p.Value);
```



```
# 随机选择 (值是 kvpair)
return dict.ElementAt(rand.Next(0, dict.Count)).Value;
```





## Select



```
dic = dic.Where(p => p.Key == 1)
         .ToDictionary(p => p.Key, p => p.Value);
```





```
tokens.Where(t => appList.Contains(t.appID)).ToList();  # 这种更简洁

List<testToken> tokens2 = (from t in tokens where appList.Contains(t.appID) select t).ToList();
```



## 匿名函数



```
Func<int> fun = () => { return 1; };
```



```
Dictionary<string, Func<CompareResult>>  dicfuncs

 Func<CompareResult> deletnewTrans = new Func<CompareResult>(delegate ()
           {

               return r;
           });
           
dicfuncs.Add("xxxx", deletnewTrans);
```



### Action 可以没有返回值

```
Action func = () => {  };
```

func 必须有返回值



```c#
                Action<JObject, JObject> func = null;

                func = (jobj, jobj_father) =>
                {

                    string PID = jobj_father["code"].ToString();

                    string id = jobj["id"].ToString();
                    string key = jobj["key"].ToString();
                    string cntxt = jobj["context"].ToString();

                    List<wordToken> words = new List<wordToken>();

                    if (cntxt != "")
                    {
                        string cntxt2 = Util.removeTrivial(cntxt);
                        words = Util.splitAll(cntxt2);
                    }


                    string code = string.Format("{0}/{1}/{2}", appID, bookID, id);
                    jobj.Add("code", code);

                    bookItemModel bi = new bookItemModel { AppID = appID, bookID = bookID, id = id, PID = PID, code = code, key = key, context = cntxt, words = words, wordDict = new Dictionary<string, double>(), childs = new Dictionary<string, bookItemModel>() };


                    string father_code = jobj_father["code"].ToString();

                    if (dic_allbooksItems.ContainsKey(father_code))
                    {
                        bookItemModel father = dic_allbooksItems[father_code];
                        if (!father.childs.ContainsKey(bi.code))
                        {
                            father.childs.Add(bi.code, bi);
                        }

                    }

                    foreach (var w in words)
                    {
                        // 词频计数
                        if (!bi.wordDict.ContainsKey(w.word))
                        {
                            bi.wordDict.Add(w.word, 1);
                        }
                        else
                        {
                            bi.wordDict[w.word]++;
                        }

                        // 有这个词的所有书籍段落
                        if (!dict_wordbooks.ContainsKey(w.word))
                        {
                            dict_wordbooks.Add(w.word, new List<bookItemModel>());
                        }

                        if (!dict_wordbooks[w.word].Contains(bi))
                        {
                            dict_wordbooks[w.word].Add(bi);
                        }
                    }

                    dic_allbooksItems.Add(code, bi);

                    foreach (JObject jobj_child in jobj["childs"])
                    {
                        func(jobj_child, jobj); // 递归调用
                    }

                };


                foreach (JObject jobj in contextJson["childs"])
                {
                    func(jobj, contextJson);
                }
```



## 随机数

```
Random rd = new Random()
rd.next(1,10)(生成1~10之间的随机数，不包括10)
```





## blazor



```
<p>@($"{_currentTime.ToString("mm\\:ss")} / {_duration.ToString("mm\\:ss")}")</p>
```



```
# sdk
mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-5.0.401-linux-x64.tar.gz -C $HOME/dotnet
export DOTNET_ROOT=$HOME/dotnet
export PATH=$PATH:$HOME/dotnet

ln -s /root/dotnet/dotnet /usr/bin
```





```c#
1. Server\dangan.Server.csproj 加入
  <ItemGroup>
    <PackageReference Include="Blazored.SessionStorage" Version="2.1.0" />
    <PackageReference Include="MeCab.DotNet" Version="0.0.40" />
    <PackageReference Include="MedallionShell" Version="1.6.2" />
    <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.Server" Version="5.0.7" />
    <PackageReference Include="Newtonsoft.Json" Version="13.0.1" />
    <PackageReference Include="Npgsql" Version="5.0.10" />
  </ItemGroup>
2. MainLayout.razor 把导航和关于都去掉，只留body

3. debug 和 Release 的端口不一样  launchSettings.json 里面有设置
    
4. 发布以后再重设
    dotnet publish -c Release -r linux-x64 # 在dangan 根目录运行
    cd /mnt/dangan/Server/bin/Release/net5.0/linux-x64/publish/
	./dangan.Server --urls http://0.0.0.0:5000
systemctl stop firewalld
    
5. pm2 --name dangan_80 start "./dangan.Server --urls http://0.0.0.0:80"

6. dotnet dangan.Server.dll --urls http://0.0.0.0:80
	# windows 发布的这样

## nohup

​```bash
# 加 -u 才能看到打印的输出
nohup python3.8 -u anime_Danganronpa_version1.py >outlog &
tail -f outlog
jobs -l # 查看运行中的进程
ps -aux | grep "anime_Danganronpa_version1.py"

kill -9 $(lsof outlog | tail -n +2  | awk '{print $2}' | tr '\n' ' ')
kill -9 $(lsof -i:8077 | tail -n +2  | awk '{print $2}' | tr '\n' ' ')

​```
```





```
# https://www.jeremymorgan.com/blog/linux/blazor-in-linux/
	# cool
# .NET SDK on CentOS
	# https://docs.microsoft.com/en-us/dotnet/core/install/linux-scripted-manual#scripted-install

./dotnet-install.sh -c 5.0

~/.dotnet/dotnet --version  # 装到root 文件夹里面了
ln -s ~/.dotnet/dotnet  /usr/bin  #新建软链接

cd Server/  # 这是windows 用Visual studio 2019 创建的hosted（有client和server）的项目
dotnet run
	# wget http://localhost:5000  正常返回主页面

	dotnet run --urls http://0.0.0.0:5000


dotnet publish -c Release -r linux-x64 # 在dangan 根目录运行

cd /mnt/dangan/Server/bin/Release/net5.0/linux-x64
./dangan.Server
	# 奇怪的是wget http://localhost:5000 返回404
	
./dangan.Server --urls http://0.0.0.0:5000
	# 外网正常访问

[root@localhost linux-x64]# ./dangan.Server
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: http://localhost:5000
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Production
info: Microsoft.Hosting.Lifetime[0]
      Content root path: /mnt/dangan/Server/bin/Release/net5.0/linux-x64



# 关闭防火墙
systemctl stop firewalld

Client\Properties\launchSettings.json
Server\Properties\launchSettings.json
	# 把localhost 改成 0.0.0.0 就可以在外网访问了


# 转发80 端口
yum install nginx

/etc/nginx/nginx.conf


把访问 http://127.0.0.1:9001/edu 的请求转发到 http://127.0.0.1:8080
把访问 http://127.0.0.1:9001/vod 的请求转发到 http://127.0.0.1:8081
这种要怎么配置呢，首先同样打开主配置文件，然后在 http 模块下增加一个 server 块：

server {
  listen 9001;
  server_name localhost;

  location ~ /edu/ {
    proxy_pass http://127.0.0.1:8080;
  }
  
  location ~ /vod/ {
    proxy_pass http://127.0.0.1:8081;
  }
}

location / {
    proxy_pass http://localhost:5000;
}

systemctl start nginx
nginx -s reload # 重新加载配置

iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
```





```
# https://github.com/TimChen44/Blazor-ToDo
	# 进击吧blazor
	
# https://www.yogihosting.com/blazor-first-application/
	# begining
```





要使用Blazor WebAssembly 的**ASP.NET Core hosted模式**,即模板具有Client，**Server**，Share三个项目。



### using



```c#
# .razor 代码内要用@using  而不是普通的using，否则既不报错又不生效

@page "/"

@using dangan.Client.Model;

@inject NavigationManager NavigationManager
@*<form action="/search" method="post">
        keyword: <InputText id="keyword" /> <button type="submit">Search</button> <br>
        <select name="lang_select">
            <option value="en">en</option>
            <option value="jp">jp</option>
        </select>

    </form>*@


<EditForm Model="@model" OnValidSubmit="@HandleSubmit">
    <DataAnnotationsValidator />
    <ValidationSummary />

    <InputText id="keyowrdInput" @bind-Value="model.keyword" />

    <button type="submit">Submit</button>
</EditForm>
```



### section



```c#
# https://tutorialslink.com/Articles/How-to-use-Sessions-in-Blazor-Application/2057
```



### hosted



```

dotnet run --urls http://0.0.0.0:5000


# https://www.jeremymorgan.com/blog/linux/blazor-in-linux/
	# cool

# https://github.com/TimChen44/Blazor-ToDo
	# 进击吧blazor

--hosted when using the client-hosted Blazor.

https://docs.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server?view=aspnetcore-3.1#linux-with-apache

Using the Blazor Server hosting model, Blazor is executed on the server from within an ASP.NET Core app. UI updates, event handling, and JavaScript calls are handled over a SignalR connection.

```



### Markdown



```
# https://www.syncfusion.com/blogs/post/blazor-live-preview-markdown-editors-content-using-markdig-library.aspx
# https://www.telerik.com/blogs/blazedown-experiment-with-markdown-and-blazor

# https://www.telerik.com/blogs/10-blazor-features-you-probably-didnt-know

# https://zhuanlan.zhihu.com/p/393065362
	# 基于 Blazor 打造一款实时字幕

# https://gitee.com/LongbowEnterprise/BootstrapAdmin/wikis/CentOS%20nginx%20%E5%BC%80%E5%90%AF%20br%20%E5%8E%8B%E7%BC%A9

	# CentOS nginx 开启 br 压缩


```





### 路由地址



linux 没有IIS，服务端和客户端应该要分别运行



```c#
# linux 服务端布署（先安装aspnetcore-runtime-5.0.10-linux-x64 运行时）
./dotnet anime/dangan.Server.dll
curl  http://localhost:5000/WeatherForecast
	# 成功响应默认的Get 接口
```





```c#
    // http://localhost:2575/api/ksbaiexam/gettest

    [ApiController]
    [Route("api/[controller]")]
    public class ksbaiexamController : ControllerBase
```



```c#
# ASP.NET Core hosted模式中，如果用IIS 启动，前端和服务端共用一个IP端口

http://localhost:44732/WeatherForecast/gettest
	// 这里既可以get 前端页面，又可以POST 后端接口，是自动选择的
```







```
# https://zhuanlan.zhihu.com/p/157582707
	# 使用Blazor组件 - 创建一个音乐播放器
# https://zhuanlan.zhihu.com/p/136802873
	# 拖拽 .NET Blazor Development - Drag & Drop

# https://zhuanlan.zhihu.com/p/367531004
	# 通过 EmbededFileProvider 实现 Blazor 的静态文件访问

```



```c#
<MatButton TrailingIcon="favorite" @onclick="@(async () => await AddItemtoShoppingCart(@item))" Label="add"></MatButton>
    
@code{
public async Task AddItemtoShoppingCart(FoodItem selectedItem)
    {
        var test = await JSRuntime.InvokeAsync<object>("blazorExtensions.WriteCookie", "cookieName", "cookieValue", "cookieExpiryDate");
    }
}

```



```c#
<script>
        window.blazorExtensions = {

            WriteCookie: function (name, value, days) {

                var expires;
                if (days) {
                    var date = new Date();
                    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                    expires = "; expires=" + date.toGMTString();
                }
                else {
                    expires = "";
                }
                document.cookie = name + "=" + value + expires + "; path=/";
            }
        }
    </script>
```



### switch when



```C#
            <span style="color:@(days switch { _ when days > 3 => "#ccc", _ when days > 0 => "#ffd800", _ => "#ff0000" })">
                @Item.Deadline?.ToShortDateString()
            </span>
```



```
// C# switch
					system = systemStr switch
                    {
                        "1" => RomajiSystem.Nippon,
                        "2" => RomajiSystem.Passport,
                        "3" => RomajiSystem.Hepburn,
                        _ => RomajiSystem.Hepburn
                    };
```





### Serverless

```
https://www.v2ex.com/t/653978
```





### JSON 乱码



```c#
            # Startup.cs
            public void ConfigureServices(IServiceCollection services)
            
            // json 里的中文乱码
            services.AddControllers().AddJsonOptions(options =>
            {
                options.JsonSerializerOptions.Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping; // JavaScriptEncoder.Create(UnicodeRanges.All);
                //options.JsonSerializerOptions.Encoder = JavaScriptEncoder.Create(UnicodeRanges.All);
            });
```





### 读取配置文件



```c#
# https://www.daveabrock.com/2021/01/19/config-top-level-programs/
# https://www.zhihu.com/people/dotnetkai-fa-zhe
	# .net 6 的做法

{
    "Name": "Dave Brock",
    "Hobbies": {
        "Weekday": "code",
        "Weekend": "play guitar"
    },
    "SwansonApiUri": "https://ron-swanson-quotes.herokuapp.com/v2/quotes"
}


Then, make sure your project file has the following packages installed, and that the appSettings.json file is being copied to the output directory:

  <ItemGroup>
    <PackageReference Include="Microsoft.Extensions.Configuration" Version="5.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="5.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.EnvironmentVariables" Version="5.0.0" />
  </ItemGroup>

  <ItemGroup>
    <None Update="appsettings.json">
      <CopyToOutputDirectory>Always</CopyToOutputDirectory>
    </None>
  </ItemGroup>
  
  
using Microsoft.Extensions.Configuration;

var config = new ConfigurationBuilder()
                 .SetBasePath(Directory.GetCurrentDirectory())
                 .AddJsonFile("appsettings.json")
                 .Build();

var name = config["Name"];
var weekdayHobby = config.GetSection("Hobbies:Weekdays");
var weekendHobby = config.GetSection("Hobbies:Weekends");
var quote = await new HttpClient().GetStringAsync(config["SwansonApiUri"]);

Console.WriteLine($"Hey, I'm {name}!");
  
  
```





### Form



```c#
# https://docs.microsoft.com/en-us/aspnet/core/blazor/forms-validation?view=aspnetcore-5.0

```



#### Post



```c#
private static readonly HttpClient client = new HttpClient();
//发送Get请求
var responseString = await client.GetStringAsync("http://www.example.com/recepticle.aspx");
        
        //发送Post请求
        var values = new Dictionary<string, string>
        {
            { "keyword", "a" },
            { "lang_select", "b" }
        };

        var content = new FormUrlEncodedContent(values);
        var response = await client.PostAsync("http://localhost:5000/search", content);
        var responseString = await response.Content.ReadAsStringAsync();
```



### 跨域



```
# https://blog.csdn.net/catshitone/article/details/118224052

# https://www.shuzhiduo.com/A/n2d9WW74JD/


 public class Startup
    {
        //其他代码.....
 
        readonly string MyAllowSpecificOrigins = "_myAllowSpecificOrigins";
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddCors(options =>
            {
                options.AddPolicy(MyAllowSpecificOrigins,
                builder =>
                {
　　　　　　　　　　　　//替换成你Blazor wasm（client）的域名
                    builder.WithOrigins("http://localhost:5001").AllowAnyHeader().AllowAnyMethod();
                });
            });
            //其他代码.......
 
        }
 
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
 
            app.UseRouting();
 
            //添加CORS到管道中，记得一定要放在UseRouting和UseEndpoints之间，否则没用
            app.UseCors(MyAllowSpecificOrigins);
 
 
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }  

```







### Action



```c#
# https://docs.microsoft.com/en-us/aspnet/core/mvc/models/model-binding?view=aspnetcore-5.0
[HttpGet("{id}")]
public ActionResult<Pet> GetById(int id, bool dogsOnly)

And the app receives a request with this URL:
http://contoso.com/api/pets/2?DogsOnly=true
```



### SignalR

```
# https://docs.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-5.0
	# 实时响应
```







### 嵌套页面



```
# https://blog.csdn.net/weixin_46295080/article/details/107167429
	# Blazor中的布局页面以及嵌套
```



```
<div>
    <Slider TValue="double" Reverse="@reversed" DefaultValue="33" />
    <Slider TValue="(double, double)" Reverse="@reversed" DefaultValue="(20, 50)" />
    Reversed: <Switch Size="small" Checked="@reversed" OnChange="(e)=>OnSwitchReverse(e)" />
</div>

@code {

    private bool reversed = true;

    private void OnSwitchReverse(bool args)
    {
        reversed = args;
    }
}
```





```

# Bug test
# https://github.com/ant-design-blazor/ant-design-blazor/issues/1912

@page "/test"

<div class="queryDiv">
    <Select Mode="default"
            DataSource="@jobTypeList"
            @bind-Value="@jobType"
            LabelName="@nameof(NameValueRecord<string, string>.Name)"
            ValueName="@nameof(NameValueRecord<string, string>.Value)"
            DefaultActiveFirstOption="true"
            OnSelectedItemChanged="JobTypeChanged">
    </Select>
    <Select Mode="tags"
            EnableSearch="true"
            MaxTagCount="5"
            TItem="string"
            TItemValue="string"
            @bind-Values="@queryModel.Area"
            AllowClear="true">
        <SelectOptions>
            @if (AreaList?.Any() ?? false)
            {
                @foreach (TestNameSpace.AreaDTO area in AreaList)
                {
                    <SelectOption @key="@area.ObjectID" TItemValue="string" TItem="string" Value="@area.AreaID" Label="@area.AreaID" />
                }
            }
        </SelectOptions>
    </Select>
</div>


using Model.Record;
using System.Collections.Generic;
using System.Linq;
using TestNameSpace;

namespace Client.Pages
{
    public partial class Test
    {
        #region Field
        private string jobType = "List1";
        #endregion

        #region Properity
        private List<AreaDTO> RTAreaList { get; set; } = new();

        private List<AreaDTO> NonRTAreaList { get; set; } = new();

        readonly QueryModel queryModel = new();

        private static readonly List<NameValueRecord<string, string>> jobTypeList = new()
        {
            new NameValueRecord<string, string>("List1", "List1"),
            new NameValueRecord<string, string>("List2", "List2")
        };
        #endregion

        #region DataSource
        private List<AreaDTO> AreaList { get; set; } = new();
        #endregion
        protected override void OnInitialized()
        {
            InitAreaInfo();
        }

        private void InitAreaInfo()
        {
            for (int i = 0; i < 7; i++)
            {
                RTAreaList.Add(new AreaDTO { ObjectID = i, AreaID = i.ToString() });
            }
            for (int i = 7; i < 10; i++)
            {
                NonRTAreaList.Add(new AreaDTO { ObjectID = i, AreaID = i.ToString() });
            }
            AreaList = RTAreaList;
        }

        private void JobTypeChanged(NameValueRecord<string, string> item)
        {
            switch (item.Value)
            {
                case "List1":
                    AreaList = RTAreaList;
                    break;
                case "List2":
                    AreaList = NonRTAreaList;
                    break;
                default:
                    break;
            }
            queryModel.area = string.Join(",", AreaList.Select(a => a.AreaID));
            StateHasChanged();
        }
    }
    
}

namespace TestNameSpace
{
    public class AreaDTO
    {
        /// <summary>
        /// AREA_ID
        /// </summary>
        public string AreaID { get; set; }

        /// <summary>
        /// OBJECT_ID
        /// </summary>
        public long ObjectID { get; set; }
    }

    public class QueryModel
    {
        public IEnumerable<string> Area
        {
            get => string.IsNullOrWhiteSpace(area) ? null : area?.Split(",");
            set => area = value is null ? null : string.Join(",", value.Where(v => !string.IsNullOrWhiteSpace(v)));
        }
        #region Field
        public string area;
        #endregion
    }
}

```



### 重定向



```C#
@page "/YourPageName"
@inject NavigationManager NavigationManager

<h1>xxx</h1>
.
.
.

@code {

    void MethodToTriggerUrl()
    {
        NavigationManager.NavigateTo("PageToRedirect");
    }
}
```







## 自动格式化



```
Ctrl + K ,  Ctrl + D.  自动整理代码
```



# File



## 读取字节数组



```csharp
			byte[] bts = null;

            using (FileStream stream = new FileStream("tmp.mp3", FileMode.Open, FileAccess.Read))
            using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
            {
                bts = reader.ReadBytes(Convert.ToInt32(stream.Length));
            }
```





## 建目录如不存在

```
using System.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

			string dir = Path.Join(new string[] { rootImageDir, bookNO });
            if ( ! Directory.Exists(dir) )  // 目录不存在，创建
            {
                DirectoryInfo di = Directory.CreateDirectory(dir);
                if (!Directory.Exists(dir))
                {
                    return new JsonResult(new { status = 200, msg = "success.", data = new { isSave = false, msg = $"创健目录失败：{dir}" } });
                }
            }

            string image_path = Path.Join(new string[] { dir, image_name });

            if (System.IO.File.Exists(image_path))
            {
                // 文件已存在
                return new JsonResult(new { status = 200, msg = "success.", data = new { isSave = false, msg = "文件已存在" } });

            }
```







# 图像



###  Base64 图片互转 



```
        public static Image convertBase64ToImage(string base64String)
        {
            byte[] imageBytes = Convert.FromBase64String(base64String);
            using (MemoryStream ms = new MemoryStream(imageBytes, 0, imageBytes.Length))
            {
                ms.Write(imageBytes, 0, imageBytes.Length);
                return Image.FromStream(ms, true);
            }
        }
        
        public static string imgToBase64(Bitmap img, ImageFormat format)
        {
            using (MemoryStream memoryStream = new MemoryStream())
            {
                img.Save(memoryStream, format);

                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                return imgData;
            }
        }
```



### 字符数组图片互转



```
    using OpenCvSharp;
	using SixLabors.ImageSharp;
    
    public static void convertToGif(byte[] data, string savePath)
    {
        var img = SixLabors.ImageSharp.Image.Load(data);

        img.SaveAsGif(savePath);
    }

    public static void convertToGif(System.Drawing.Bitmap img, string savePath)
    {
        Mat src = OpenCvSharp.Extensions.BitmapConverter.ToMat(img);
        src.SaveImage(savePath);
    }
```



```c#
 Regex regex = new Regex("<img src=\"data: image / ([a-zA-Z]{3,4}); base64,(.+?)\"\\s*/>");

            if (regex.IsMatch(s))
            {
                MatchCollection matches = regex.Matches(s);

                int count = matches.Count;

                foreach (Match m in matches)
                {
                    string sub = m.Value;

                    string extname = ""; // 图片扩展名
                    string base64 = "";

                    foreach (string name in regex.GetGroupNames())
                    {
                        string g = m.Groups[name].Value;

                        if (name == "0")
                        {
                            // 整个匹配
                        }

                        if (name == "1")
                        {
                            // 第一个分组
                            extname = g;
                        }


                        if (name == "2")
                        {
                            // 第二个分组
                            base64 = g;
                        }

                    }

                    byte[] imageBytes = Convert.FromBase64String(base64);

                    var img = SixLabors.ImageSharp.Image.Load(imageBytes);

                    if (extname == "png")
                    {
                        img.SaveAsPng("xx.png");
                    }
                }
            }
```



### Post的时侯UrlEncode 一下



```csharp
HttpUtility.UrlEncode(imgName)}&originImgData={HttpUtility.UrlEncode(originImgData)
    
                //读取原始图像
                byte[] imageBytes = null;
                using (FileStream stream = new FileStream(fp, FileMode.Open, FileAccess.Read))
                using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
                {
                    imageBytes = reader.ReadBytes(Convert.ToInt32(stream.Length));
                }
                string originImgData = Convert.ToBase64String(imageBytes);    
    
```



### 截图

- https://github.com/itewqq/MathpixCsharp

- https://blog.51cto.com/u_6650004/2780378



# OpenCV



```
# simple.cs

using OpenCvSharp;
using SixLabors.ImageSharp;
using System;
using System.IO;

class Sample
{
    // 边缘检测
    public static void canny()
    {
        // https://blog.csdn.net/zanllp/article/details/79829813
        Mat src = new Mat("1.jpg", ImreadModes.Grayscale);
        Mat dst = new Mat();

        Cv2.Canny(src, dst, 50, 200);
        Cv2.ImWrite("2.jpg", dst);

        Cv2.ImShow("src image", src);
        Cv2.ImShow("dst image", dst);
        Cv2.WaitKey();
        //using (new Window("src image", src))
        //using (new Window("dst image", dst))
        //{
        //    Cv2.WaitKey();
        //}
    }

    // 最小外接矩形
    public static void minAreaRect()
    {
        // https://www.cnblogs.com/little-monkey/p/7429579.html
        Mat src = new Mat("minAreaRect.jpg", ImreadModes.Grayscale);
        Mat dst = src.Clone();
        Cv2.Threshold(src, src, 100, 255, ThresholdTypes.Binary);
        Cv2.ImShow("src binary", src);
        Cv2.WaitKey();
    }


    // 透视变换
    public static void perspectiveTransformation()
    {
        // https://www.cnblogs.com/wj-1314/p/11975977.html
        // https://github.com/LeBron-Jian/ComputerVisionPractice



    }

    // 删除边缘的对象
    public static void deleteBorder()
    {
        // https://answers.opencv.org/question/173768/how-to-delete-those-border-component/

    }

    // 删除边缘的对象
    public static Mat DeleteBorderComponents(Mat src)
    {
        // https://stackoverflow.com/questions/65534370/remove-the-element-attached-to-the-image-border
        using (Mat neg = new Mat())
        using (Mat pad = new Mat())
        {
            Cv2.BitwiseNot(src, neg);  // 反色
            Cv2.CopyMakeBorder(neg, pad, 1, 1, 1, 1, BorderTypes.Constant, 255);  // 上下左右各加一像素
            OpenCvSharp.Size size = pad.Size();
            Mat mask = Mat.Zeros(size.Height + 2, size.Width + 2, MatType.CV_8UC1);  // Mask 图像宽高都比pad 多两像素

            Rect rect_floodfill = new Rect();
            Cv2.FloodFill(pad, mask, new OpenCvSharp.Point(0, 0), 0, out rect_floodfill, 5, 0, FloodFillFlags.Link8);  // 填充

            Mat tmp = pad.Clone(new Rect(2, 2, size.Width - 2, size.Height - 2));  // 宽高前面各加了共两像素，这里减去
            Cv2.BitwiseNot(tmp, tmp);
            return tmp;
        }
    }

    // 二值化
    public static Mat Binarize(Mat src)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat img_binary = new Mat())
        {
            Cv2.Threshold(src, img_binary, 185, 255, ThresholdTypes.Binary); // 二值化
            return img_binary.Clone();
        }
    }

    // 二值化
    public static Mat Binarize(Mat src, double thresh, double maxval)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat img_binary = new Mat())
        {
            Cv2.Threshold(src, img_binary, thresh, maxval, ThresholdTypes.Binary); // 二值化
            return img_binary.Clone();
        }
    }

    // 去除黑边后的矩形区域
    public static Rect DeBoardRect(Mat t)
    {

        Sample sample = new Sample();

        Mat im = Binarize(t);  // 二值化
        im = DeleteBorderComponents(im);  // 删除边缘对象

        im = DeleteSmallComponents(im);  // 删除面积过小的像素点

        // 遍历每一个像素
        //for (int x = 0; x < im.Rows; x++)
        //{
        //    for (int y = 0; y < im.Cols; y++)
        //    {
        //        // Point p(x, y); 第几行第几列
        //        // At(y, x) 第几行第几列
        //        // Rect(X=y, Y=x) 第几列第几行
        //        // 注意这两个传参的顺序是不一样的
        //        int pixel = im.At<Byte>(y, x);

        //        if (pixel == 255)  // 未反色前255 是白色
        //        {
        //            //im.At<Byte>(y, x) = 135;  // 纯白全部变成一个特定的灰色

        //        }
        //    }
        //}

        int X = 0;
        // 从左向右移动，条件是这一整列的像素几乎都是0
        for (int x = 0; x < im.Cols; x++)  // x 代表的是第几列
        {
            double count = 0;

            for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一列有多少个非纯白像素点
                }
            }

            if (count > 0)
            {
                X = x;
                break;
            }

        }


        int X2 = im.Cols;
        // 从右向左移动，条件是这一整列的像素几乎都是0
        for (int x = im.Cols - 1; x >= 0; x--)  // x 代表的是第几列
        {
            double count = 0;

            for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一列有多少个非0 像素点
                }
            }

            if (count > 0.01)
            {
                X2 = x;
                break;
            }

        }


        int Y = 0;
        // 从上向下移动，条件是这一整行的像素几乎都是0
        for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
        {
            double count = 0;

            for (int x = 0; x < im.Cols; x++) // x 代表的是第几列
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一列有多少个非纯白像素点
                }
            }

            if (count > 0)
            {
                Y = y;
                break;
            }
        }


        int Y2 = im.Rows;
        // 从下向上移动，条件是这一整行的像素几乎都是0
        for (int y = im.Rows - 1; y >= 0; y--)  // y 代表的是第几行
        {
            double count = 0;

            for (int x = 0; x < im.Cols; x++) // x 代表的是第几列
            {
                int pixel = im.At<Byte>(y, x);
                if (pixel != 255)
                {
                    count++;  // 计算这一行有多少个非0 像素点
                }
            }

            if (count > 0)
            {
                Y2 = y;
                break;
            }
        }


        // 宽度 = 有多少列 im.Cols
        // 高度 = 有多少行 im.Rows
        // x in im.Cols 是 第几列
        // y in im.Rows 是 第几行


        if (X >= 60)
        {
            X = X - 60;
        }

        if (X2 + 60 <= im.Cols)
        {
            X2 = X2 + 60;
        }


        if (Y >= 60)
        {
            Y = Y - 60;
        }

        if (Y2 + 60 <= im.Rows)
        {
            Y2 = Y2 + 60;
        }

        var rect = new Rect
        {
            X = X,
            Y = Y,
            Width = im.Cols - (X + (im.Cols - X2)),
            Height = im.Rows - (Y + (im.Rows - Y2))
        };

        return rect;
    }


    // 去除黑边（图片大小可能会改变）
    public static Mat DeBoardAndResize(Mat src, bool autoCut, bool binarize = false)
    {
        Mat img_gray = new Mat();
        Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化

        if (binarize)
        {
            img_gray = Sample.Binarize(img_gray, 200, 255);
        }

        // 找出除掉边框后的区域
        Rect retct = Sample.DeBoardRect(img_gray);

        Mat img_des = null;

        if (autoCut)
        {
            // 自动剪掉白边
            img_des = img_gray.Clone(retct);
        }
        else
        {
            // rect 矩形区域以外全部变白
            img_des = Whited(img_gray, retct);
        }

        img_gray.Dispose();

        return img_des;
    }

    // rect 矩形区域以外全部变白
    public static Mat Whited(Mat t, Rect rect)
    {
        for (int x = 0; x < t.Cols; x++)  // x 第几列
        {
            for (int y = 0; y < t.Rows; y++)  // y 第几行
            {
                bool whiteQ = true;

                if (x >= rect.X && x <= rect.X + rect.Width)
                {
                    if (y >= rect.Y && y <= rect.Y + rect.Height)
                    {
                        whiteQ = false;  // 矩形区域以内的像素保留
                    }
                }

                if (whiteQ)
                {
                    t.At<Byte>(y, x) = 255;   // 矩形区域以外的像素变白
                }

            }
        }

        return t.Clone();
    }

    // 删除过小的对象
    public static Mat DeleteSmallComponents(Mat im)
    {

        // https://qiita.com/kaiyu_tech/items/a37fc929ac0f3328fea1

        Cv2.BitwiseNot(im, im);  // 反色

        var labels = new Mat();
        var stats = new Mat();
        var centroids = new Mat();
        var count = Cv2.ConnectedComponentsWithStats(im, labels, stats, centroids, PixelConnectivity.Connectivity8, MatType.CV_32SC1);

        var indexes = stats.Col((int)ConnectedComponentsTypes.Area).SortIdx(SortFlags.EveryColumn);


        var indexer = stats.GetGenericIndexer<int>();

        var output = im.CvtColor(ColorConversionCodes.GRAY2BGR);


        // 遍历每一个像素
        for (int x = 0; x < im.Rows; x++)
        {
            for (int y = 0; y < im.Cols; y++)
            {

                int label = labels.At<int>(x, y);

                if (label == 0)
                {
                    // 是背景对象，跳过
                    continue;
                }

                var area = indexer[label, (int)ConnectedComponentsTypes.Area];

                var rect = new Rect
                {
                    X = indexer[label, (int)ConnectedComponentsTypes.Left],
                    Y = indexer[label, (int)ConnectedComponentsTypes.Top],
                    Width = indexer[label, (int)ConnectedComponentsTypes.Width],
                    Height = indexer[label, (int)ConnectedComponentsTypes.Height]
                };

                // 所处的连通块面积过小则删除（变成背景色）
                if (area < 20)
                {
                    im.At<Byte>(x, y) = 0;
                }
            }
        }

        // 遍历每一个连通块
        for (int i = 0; i < indexes.Rows - 1; i++)
        {
            var index = indexes.Get<int>(i);

            var area = indexer[index, (int)ConnectedComponentsTypes.Area];

            var rect = new Rect
            {
                X = indexer[index, (int)ConnectedComponentsTypes.Left],
                Y = indexer[index, (int)ConnectedComponentsTypes.Top],
                Width = indexer[index, (int)ConnectedComponentsTypes.Width],
                Height = indexer[index, (int)ConnectedComponentsTypes.Height]
            };

            // 绘制矩形
            if (area < 20)
            {
                output.Rectangle(rect, Scalar.Blue);
            }
            //else
            //{
            //    output.Rectangle(rect, Scalar.Red);
            //}
        }


        Cv2.BitwiseNot(im, im);

        return im;

    }


    public static void convertToGif(byte[] data, string savePath)
    {
        var img = SixLabors.ImageSharp.Image.Load(data);

        img.SaveAsGif(savePath);
    }

    public static void convertToGif(System.Drawing.Bitmap img, string savePath)
    {
        Mat src = OpenCvSharp.Extensions.BitmapConverter.ToMat(img);
        src.SaveImage(savePath);
    }

    // 二值化
    public static string binarize(string filePath)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat src = new Mat(filePath))
        {
            Mat img_binary = new Mat();
            using (Mat img_gray = new Mat())
            using (Mat img_threshold = new Mat())
            {
                Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化 BGR2HSV 
                                                                            //Cv2.CvtColor(src, img_gray, ColorConversionCodes.LRGB2Luv); // 灰度化 BGR2HSV 
                                                                            //Cv2.Threshold(img_gray, img_binary, 250, 255, ThresholdTypes.Binary); // 二值化

                //img_binary = DeleteBorderComponents(img_binary);
                img_binary = DeleteBorderComponents(img_gray);
                //img_binary = DeleteSmallComponents(img_binary);

                using (MemoryStream memoryStream = img_binary.ToMemoryStream())
                {
                    byte[] imageBytes = memoryStream.ToArray();
                    string imgData = Convert.ToBase64String(imageBytes);
                    memoryStream.Dispose();
                    img_binary.Dispose();
                    return imgData;
                }
            }
        }

    }


    // 预处理
    public static string prepare(string filePath)
    {

        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat src = Cv2.ImRead(filePath, ImreadModes.Color))
        {

            Mat img_gray = new Mat();
            Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化

            // 找出除掉边框后的区域
            Rect retct = DeBoardRect(img_gray);

            // rect 矩形区域以外全部变白
            //Mat src2 = Whited(img_gray, retct);

            Mat src2 = img_gray.Clone(retct);

            //Cv2.ImWrite(@"D:\workcode\csharp\noboard__src.jpg", src2);
            Cv2.ImWrite(filePath, src2);


            using (MemoryStream memoryStream = src2.ToMemoryStream())
            {
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                memoryStream.Dispose();
                img_gray.Dispose();
                return imgData;
            }
        }

    }


    /// <summary>
    /// 截图
    /// </summary>
    /// <param name="path"></param>
    /// <param name="x"></param>
    /// <param name="y"></param>
    /// <param name="w"></param>
    /// <param name="h"></param>
    /// <param name="rx"></param>
    /// <param name="ry"></param>
    /// <param name="rw"></param>
    /// <param name="rh"></param>
    /// <returns></returns>
    public static string cutImage(string path, int x, int y, int w, int h, int rx, int ry, int rw, int rh)
    {
        using (Mat img = new Mat(path))
        {

            if (x < 0)
            {
                x = 0;
            }
            if (x + w >= img.Width)
            {
                w = img.Width - x - 1;
            }
            if (y < 0)
            {
                y = 0;
            }
            if (y + h >= img.Height)
            {
                h = img.Height - y - 1;
            }
            var rect = new Rect(x, y, w, h);
            var minImg = img[rect];

            //Mat dist = new Mat();
            //Cv2.BitwiseNot(minImg, dist);

            //Cv2.Threshold(minImg, dist, 50, 255, ThresholdTypes.Binary);

            //Cv2.Rectangle(minImg, new Rect(rx, ry, rw, rh), Scalar.Red, 2);
            using (var memoryStream = minImg.ToMemoryStream(".png"))
            {
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                memoryStream.Dispose();
                img.Dispose();
                minImg.Dispose();
                //dist.Dispose();
                return imgData;
            }
        }
    }


    /// <summary>
    /// 旋转图像
    /// </summary>
    /// <param name="src"></param>
    /// <param name="angle"></param>
    /// <returns></returns>
    public static Mat matRotate(Mat src, float angle)
    {
        Mat dst = new Mat();
        Point2f center = new Point2f(src.Cols / 2, src.Rows / 2);
        Mat rot = Cv2.GetRotationMatrix2D(center, angle, 1);
        Size2f s2f = new Size2f(src.Size().Width, src.Size().Height);
        Rect box = new RotatedRect(new Point2f(0, 0), s2f, angle).BoundingRect();
        double xx = rot.At<double>(0, 2) + box.Width / 2 - src.Cols / 2;
        double zz = rot.At<double>(1, 2) + box.Height / 2 - src.Rows / 2;
        rot.Set(0, 2, xx);
        rot.Set(1, 2, zz);
        Cv2.WarpAffine(src, dst, rot, box.Size);
        rot.Dispose();
        return dst;
    }


    /// <summary>
    /// 图片转格式
    /// </summary>
    /// <param name="src"></param>
    /// <param name="dist"></param>
    public static void convertImageFormat(string src, string dist)
    {
        using (Mat img = new Mat(src))
        {
            img.SaveImage(dist);
            img.Dispose();
        }
    }

    public static string ocrInit(string filePath)
    {
        using (Mat src = new Mat(filePath, ImreadModes.Grayscale))
        {
            //1.Sobel算子，x方向求梯度
            Mat sobel = new Mat();
            Cv2.Sobel(src, sobel, MatType.CV_8U, 1, 0, 3);

            //2.二值化
            Mat binary = new Mat();
            Cv2.Threshold(sobel, binary, 0, 255, ThresholdTypes.Otsu | ThresholdTypes.Binary);

            //3. 膨胀和腐蚀操作的核函数
            Mat element1 = new Mat();
            Mat element2 = new Mat();
            OpenCvSharp.Size size1 = new OpenCvSharp.Size(30, 9);
            OpenCvSharp.Size size2 = new OpenCvSharp.Size(24, 6);

            element1 = Cv2.GetStructuringElement(MorphShapes.Rect, size1);
            element2 = Cv2.GetStructuringElement(MorphShapes.Rect, size2);

            //4. 膨胀一次，让轮廓突出
            Mat dilation = new Mat();
            Cv2.Dilate(binary, dilation, element2);

            //5. 腐蚀一次，去掉细节，如表格线等。注意这里去掉的是竖直的线
            Mat erosion = new Mat();
            Cv2.Erode(dilation, erosion, element1);

            Mat dilation2 = new Mat();
            Cv2.Dilate(binary, dilation2, element2);
            //6. 再次膨胀，让轮廓明显一些
            Cv2.Dilate(erosion, dilation2, element2, null, 3);

            using (MemoryStream memoryStream = binary.ToMemoryStream())
            {
                byte[] imageBytes = memoryStream.ToArray();
                string imgData = Convert.ToBase64String(imageBytes);
                return imgData;
            }

        }
    }

    public static System.Drawing.Image test(string src)
    {
        using (Mat img = new Mat(src))
        {

            //Mat dist = new Mat();
            //Cv2.BitwiseNot(minImg, dist);

            Mat dist = new Mat();
            Mat hd = new Mat();
            Cv2.CvtColor(img, hd, ColorConversionCodes.BGR2GRAY); // 灰度化 BGR2HSV 

            Cv2.Threshold(hd, dist, 130, 255, ThresholdTypes.Binary);

            var result = System.Drawing.Image.FromStream(dist.ToMemoryStream());

            dist.Dispose();

            return result;
        }
    }

}

```







# Word



```
# https://cloud.tencent.com/developer/article/1802670
	# 换页
```





```
private void A_Btn(object sender, RoutedEventArgs e)
        {
            var path = @"C:\_whosawbo\temp\myw.dotx";
            var outPath = @"C:\_whosawbo\temp\out.dotx";

            using (FileStream fs = File.OpenRead(path))
            {
                XWPFDocument doc = new XWPFDocument(fs);

                // 替换模板中的#image#等标记
                // 同理可以替换标记为图片
                foreach (var para in doc.Paragraphs)
                {
                    string oldtext = para.ParagraphText;
                    if (oldtext == "")
                        continue;
                    string tempText = para.ParagraphText;
                    if(tempText.Contains("#image#"))
                    {
                        tempText = tempText.Replace("#image#", "");
                        var pos = doc.GetPosOfParagraph(para);
                        var run = para.CreateRun();

                        var p1 = @"C:\_ace\temp\1.jpg";
                        using (FileStream picData = new FileStream(p1, FileMode.Open, FileAccess.Read))
                        {
                            run.AddPicture(picData, (int)PictureType.JPEG,"1.jpg", 480 * 9525, 270 * 9525);
                        }
                    }
                    if(tempText.Contains("#LoverName#"))
                    {
                        tempText = tempText.Replace("#LoverName#", "Eyes Open");
                    }

                    if(tempText.Contains("#JJLength#"))
                    {
                        tempText = tempText.Replace("#JJLength", "-0.2 ~ 0.7");
                    }
                    para.ReplaceText(oldtext, tempText);
                }

                FileStream file = new FileStream(outPath, FileMode.Create, FileAccess.Write);
                doc.Write(file);
                file.Close();
                file.Dispose();
            }

            
        }
```





```

# https://blog.csdn.net/yw1688/article/details/52067699

以前的项目都是导出数据到Excel中，这个对于NPOI来说，技术是比较成熟的，但是导出到Word的，就差一些。

刚好手头的项目需要导出一些数据到Word中，基于对NPOI导出到Word的认知是一片黑，于是到处找资料，结合了网上其他网友的代码，简单的封装了一下，因为赶项目进度，没有细调，插入表格的部分有bug,插入普通内容的没问题，图文混排的需要完善，本版只支持文字和图片分离的情况，代码等以后有空了再完善，先在这里留个记号。

using NPOI.OpenXmlFormats.Dml.WordProcessing;
using NPOI.OpenXmlFormats.Wordprocessing;
using NPOI.XWPF.UserModel;
using System.Drawing;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;
namespace zifar.PublicSentimentCommonMethod
{
    public class WordHelper
    {
        public void CreateWord(string filePath, List<WordModel> ContentList)
        {
            //1‘=1440twip=25.4mm=72pt(磅point)=96px(像素pixel)
            // A4:W=11906 twip=8.269''=210mm,h=16838twip=11.693''=297mm
            //A5:W=8390 twip=5.827''=148mm,h=11906 twip=8.269''=210mm
            //A6:W=5953 twip=4.134''=105mm,h=8390twip=5.827''=1148mm
            CT_SectPr srcpr = new CT_SectPr();
            //设置A4纸纵向，如果要横向，两个值调换即可
            srcpr.pgSz.w = (ulong)11906;
            srcpr.pgSz.h = (ulong)16838;
            var doc = new XWPFDocument();
            doc.Document.body.sectPr = srcpr;
            foreach (var c in ContentList)
            {
                #region 普通段落文字
                if (c.Xpara != null)
                {
                    if (c.Xpara.Pic != null)
                    {
                        if (string.IsNullOrEmpty(c.Xpara.Pic.FilePath) || !File.Exists(c.Xpara.Pic.FilePath))
                        {
                            continue;
                        }
                        #region 图片流,图片流也是要作为一个段落插入
                        CT_P m_p = doc.Document.body.AddNewP();
                        m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                        XWPFParagraph gp = new XWPFParagraph(m_p, doc);
                        XWPFRun gr = gp.CreateRun();
 
                        如果需要图文混排,在图片前面加文字，可以加下面的这些属性
                        //gr.GetCTR().AddNewRPr().AddNewRFonts().ascii = "黑体";
                        //gr.GetCTR().AddNewRPr().AddNewRFonts().eastAsia = "黑体";
                        //gr.GetCTR().AddNewRPr().AddNewRFonts().hint = ST_Hint.eastAsia;
                        //gr.GetCTR().AddNewRPr().AddNewSz().val = (ulong)44;
                        //gr.GetCTR().AddNewRPr().AddNewSzCs().val = (ulong)44;
                        //gr.GetCTR().AddNewRPr().AddNewColor().val = "red"; 
 
                        #region 插入图片
 
                        FileStream stream = new FileStream(c.Xpara.Pic.FilePath, FileMode.Open, FileAccess.Read);
                        switch (c.Xpara.Pic.Ptype)
                        {
                            case ParType.inline:
                                {
                                    gr.AddPicture(stream, (int)c.Xpara.Pic.PicFormat, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height);
                                    m_p = doc.Document.body.AddNewP();
                                    m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                    gp = new XWPFParagraph(m_p, doc);//再添加一个段落，空点距离
                                }
                                break;
                            case ParType.anchor:
                                {
                                    CT_Anchor anchor = new CT_Anchor();
                                    //图片距正文上(distT)、下(distB)、左(distL)、右(distR)的距离。114300EMUS=3.1mm
                                    anchor.distT = 0u;
                                    anchor.distB = 0u;
                                    anchor.distL = 114300u;
                                    anchor.distR = 114300u;
                                    anchor.simplePos1 = false;
                                    anchor.relativeHeight = 251658240u;
                                    anchor.behindDoc = false;
                                    anchor.locked = false;
                                    anchor.layoutInCell = true;
                                    anchor.allowOverlap = true;
 
                                    CT_Positive2D simplePos = new CT_Positive2D();
                                    simplePos.x = 0;
                                    simplePos.y = 0;
 
                                    CT_EffectExtent effectExtent = new CT_EffectExtent();
                                    effectExtent.l = 0;
                                    effectExtent.t = 0;
                                    effectExtent.r = 0;
                                    effectExtent.b = 0;
                                    switch (c.Xpara.Pic.Wrap)
                                    {
                                        case WrapType.wrapSquare:
                                            {
                                                //四周型
                                                gr.GetCTR().AddNewRPr().AddNewRFonts().ascii = "宋体";
                                                gr.GetCTR().AddNewRPr().AddNewRFonts().eastAsia = "宋体";
 
                                                gr.GetCTR().AddNewRPr().AddNewSz().val = (ulong)28;//四号
                                                gr.GetCTR().AddNewRPr().AddNewSzCs().val = (ulong)28;
 
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.both;
 
                                                gr.GetCTR().AddNewRPr().AddNewB().val = true; //加粗      
                                                gp.IndentationFirstLine = Indentation("宋体", 28, 2, FontStyle.Bold);
                                                //图左上角坐标
                                                CT_PosH posH = new CT_PosH();
                                                posH.relativeFrom = ST_RelFromH.column;
                                                posH.posOffset = 4000000;//单位：EMUS,1CM=360000EMUS
                                                CT_PosV posV = new CT_PosV();
                                                posV.relativeFrom = ST_RelFromV.paragraph;
                                                posV.posOffset = 200000;
                                                CT_WrapSquare wrapSquare = new CT_WrapSquare();
                                                switch (c.Xpara.Pic.Postp)
                                                {
                                                    case PosType.Besides:
                                                        //两侧
                                                        wrapSquare.wrapText = ST_WrapText.bothSides;
                                                        break;
                                                    case PosType.Largest:
                                                        //最大一侧
                                                        wrapSquare.wrapText = ST_WrapText.largest;
                                                        break;
                                                    case PosType.Left:
                                                        //左侧
                                                        wrapSquare.wrapText = ST_WrapText.left;
                                                        break;
                                                    case PosType.Right:
                                                        //右侧
                                                        wrapSquare.wrapText = ST_WrapText.right;
                                                        break;
                                                }
                                                gr.AddPicture(stream, (int)c.Xpara.Pic.PicFormat, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height, posH, posV, wrapSquare, anchor, simplePos, effectExtent);
                                                m_p = doc.Document.body.AddNewP();
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                                gp = new XWPFParagraph(m_p, doc);
                                                gr = gp.CreateRun();
                                            }
                                            break;
                                        case WrapType.wrapTight:
                                            {
                                                //紧密型
                                                gr.GetCTR().AddNewRPr().AddNewRFonts().ascii = "宋体";
                                                gr.GetCTR().AddNewRPr().AddNewRFonts().eastAsia = "宋体";
 
                                                gr.GetCTR().AddNewRPr().AddNewSz().val = (ulong)28;//四号
                                                gr.GetCTR().AddNewRPr().AddNewSzCs().val = (ulong)28;
 
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.both;
                                                m_p.AddNewPPr().AddNewSpacing().line = "400";//行距固定20磅
                                                m_p.AddNewPPr().AddNewSpacing().lineRule = ST_LineSpacingRule.exact;
 
                                                //gr.GetCTR().AddNewRPr().AddNewB().val = true; //加粗      
                                                gp.IndentationFirstLine = Indentation("宋体", 21, 2, FontStyle.Regular);
 
                                                CT_WrapTight wrapTight = new CT_WrapTight();
                                                switch (c.Xpara.Pic.Postp)
                                                {
                                                    case PosType.Besides:
                                                        //两侧
                                                        wrapTight.wrapText = ST_WrapText.bothSides;
                                                        break;
                                                    case PosType.Largest:
                                                        //最大一侧
                                                        wrapTight.wrapText = ST_WrapText.largest;
                                                        break;
                                                    case PosType.Left:
                                                        //左侧
                                                        wrapTight.wrapText = ST_WrapText.left;
                                                        break;
                                                    case PosType.Right:
                                                        //右侧
                                                        wrapTight.wrapText = ST_WrapText.right;
                                                        break;
                                                }
                                                wrapTight.wrapPolygon = new CT_WrapPath();
                                                wrapTight.wrapPolygon.edited = false;
                                                wrapTight.wrapPolygon.start = new CT_Positive2D();
                                                wrapTight.wrapPolygon.start.x = 0;
                                                wrapTight.wrapPolygon.start.y = 0;
                                                CT_Positive2D lineTo = new CT_Positive2D();
                                                wrapTight.wrapPolygon.lineTo = new List<CT_Positive2D>();
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 0;
                                                lineTo.y = 21394;
                                                wrapTight.wrapPolygon.lineTo.Add(lineTo);
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 21806;
                                                lineTo.y = 21394;
                                                wrapTight.wrapPolygon.lineTo.Add(lineTo);
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 21806;
                                                lineTo.y = 0;
                                                wrapTight.wrapPolygon.lineTo.Add(lineTo);
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 0;
                                                lineTo.y = 0;
                                                wrapTight.wrapPolygon.lineTo.Add(lineTo);
                                                //图位置
                                                CT_PosH posH = new CT_PosH();
                                                posH.relativeFrom = ST_RelFromH.column;
                                                posH.posOffset = 4000000;
                                                CT_PosV posV = new CT_PosV();
                                                posV.relativeFrom = ST_RelFromV.paragraph;
                                                posV.posOffset = -432000;//-1.2cm*360000
 
                                                gr.AddPicture(stream, (int)c.Xpara.Pic.PicFormat, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height, posH, posV, wrapTight, anchor, simplePos, effectExtent);
                                                m_p = doc.Document.body.AddNewP();
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                                gp = new XWPFParagraph(m_p, doc);
                                                gr = gp.CreateRun();
                                            }
                                            break;
                                        case WrapType.wrapThrough:
                                            {
                                                //穿越型-两边
                                                gr.GetCTR().AddNewRPr().AddNewRFonts().ascii = "宋体";
                                                gr.GetCTR().AddNewRPr().AddNewRFonts().eastAsia = "宋体";
 
                                                gr.GetCTR().AddNewRPr().AddNewSz().val = (ulong)28;//四号
                                                gr.GetCTR().AddNewRPr().AddNewSzCs().val = (ulong)28;
 
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.both;
                                                m_p.AddNewPPr().AddNewSpacing().line = "400";//行距固定20磅
                                                m_p.AddNewPPr().AddNewSpacing().lineRule = ST_LineSpacingRule.exact;
 
                                                CT_WrapThrough wrapThrough = new CT_WrapThrough();
                                                switch (c.Xpara.Pic.Postp)
                                                {
                                                    case PosType.Besides:
                                                        //两侧
                                                        wrapThrough.wrapText = ST_WrapText.bothSides;
                                                        break;
                                                    case PosType.Largest:
                                                        //最大一侧
                                                        wrapThrough.wrapText = ST_WrapText.largest;
                                                        break;
                                                    case PosType.Left:
                                                        //左侧
                                                        wrapThrough.wrapText = ST_WrapText.left;
                                                        break;
                                                    case PosType.Right:
                                                        //右侧
                                                        wrapThrough.wrapText = ST_WrapText.right;
                                                        break;
                                                }
                                                wrapThrough.wrapPolygon = new CT_WrapPath();
                                                wrapThrough.wrapPolygon.edited = false;
                                                wrapThrough.wrapPolygon.start = new CT_Positive2D();
                                                wrapThrough.wrapPolygon.start.x = 0;
                                                wrapThrough.wrapPolygon.start.y = 0;
                                                CT_Positive2D lineTo = new CT_Positive2D();
                                                wrapThrough.wrapPolygon.lineTo = new List<CT_Positive2D>();
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 0;
                                                lineTo.y = 21394;
                                                wrapThrough.wrapPolygon.lineTo.Add(lineTo);
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 21806;
                                                lineTo.y = 21394;
                                                wrapThrough.wrapPolygon.lineTo.Add(lineTo);
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 21806;
                                                lineTo.y = 0;
                                                wrapThrough.wrapPolygon.lineTo.Add(lineTo);
                                                lineTo = new CT_Positive2D();
                                                lineTo.x = 0;
                                                lineTo.y = 0;
                                                wrapThrough.wrapPolygon.lineTo.Add(lineTo);
                                                CT_PosH posH = new CT_PosH();
                                                posH.relativeFrom = ST_RelFromH.column;
                                                posH.posOffset = 4000000;
                                                CT_PosV posV = new CT_PosV();
                                                posV.relativeFrom = ST_RelFromV.paragraph;
                                                posV.posOffset = -432000;//-1.2cm*360000
 
                                                gr.AddPicture(stream, (int)NPOI.XWPF.UserModel.PictureType.JPEG, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height, posH, posV, wrapThrough, anchor, simplePos, effectExtent);
                                                //gp = m_Docx.CreateParagraph();
                                                //gp.GetCTPPr().AddNewJc().val = ST_Jc.center; //水平居中
                                                m_p = doc.Document.body.AddNewP();
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                                gp = new XWPFParagraph(m_p, doc);
                                                gr = gp.CreateRun();
                                            }
                                            break;
                                        case WrapType.wrapTopAndBottom:
                                            {
                                                //上下型
                                                //图左上角坐标
                                                CT_PosH posH = new CT_PosH();
                                                posH.relativeFrom = ST_RelFromH.column;
                                                posH.posOffset = 400000;//单位：EMUS,1CM=360000EMUS
                                                CT_PosV posV = new CT_PosV();
                                                posV.relativeFrom = ST_RelFromV.paragraph;
                                                posV.posOffset = 200000;
                                                CT_WrapTopBottom wrapTopandBottom = new CT_WrapTopBottom();
                                                gr.AddPicture(stream, (int)c.Xpara.Pic.PicFormat, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height, posH, posV, wrapTopandBottom, anchor, simplePos, effectExtent);
                                                m_p = doc.Document.body.AddNewP();
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                                gp = new XWPFParagraph(m_p, doc);
                                                gr = gp.CreateRun();
                                            }
                                            break;
                                        case WrapType.wrapNoneBehindDoc:
                                            {
                                                //上方型
                                                //图左上角坐标
                                                CT_PosH posH = new CT_PosH();
                                                posH.relativeFrom = ST_RelFromH.column;
                                                posH.posOffset = 4000000;//单位：EMUS,1CM=360000EMUS
                                                CT_PosV posV = new CT_PosV();
                                                posV.relativeFrom = ST_RelFromV.paragraph;
                                                posV.posOffset = 0;
                                                CT_WrapNone wrapNone = new CT_WrapNone();
                                                anchor.behindDoc = false;
                                                gr.AddPicture(stream, (int)c.Xpara.Pic.PicFormat, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height, posH, posV, wrapNone, anchor, simplePos, effectExtent);
                                                m_p = doc.Document.body.AddNewP();
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                                gp = new XWPFParagraph(m_p, doc);
                                                gr = gp.CreateRun();
                                            }
                                            break;
                                        case WrapType.wrapBehindDoc:
                                            {
                                                //下方型
                                                //图左上角坐标
                                                CT_PosH posH = new CT_PosH();
                                                posH.relativeFrom = ST_RelFromH.column;
                                                posH.posOffset = 4000000;//单位：EMUS,1CM=360000EMUS
                                                CT_PosV posV = new CT_PosV();
                                                posV.relativeFrom = ST_RelFromV.paragraph;
                                                posV.posOffset = 0;
                                                CT_WrapNone wrapNone = new CT_WrapNone();
                                                anchor.behindDoc = true;
                                                gr.AddPicture(stream, (int)c.Xpara.Pic.PicFormat, c.Xpara.Pic.PicName, c.Xpara.Pic.Width, c.Xpara.Pic.Height, posH, posV, wrapNone, anchor, simplePos, effectExtent);
                                                m_p = doc.Document.body.AddNewP();
                                                m_p.AddNewPPr().AddNewJc().val = ST_Jc.center;//段落水平居中
                                                gp = new XWPFParagraph(m_p, doc);
                                                gr = gp.CreateRun();
                                            }
                                            break;
                                    }
                                }
                                break;
                        }
                        
                        #endregion
 
                        #endregion
                    }
                    else
                    {
                        #region 普通文本
                        if (c.Xpara.ParaStyle == null) c.Xpara.ParaStyle = new Style();
                        第一种创建段落的方式
                        //XWPFParagraph p = doc.CreateParagraph();
                        //p.Alignment = (ParagraphAlignment)Enum.Parse(typeof(ParagraphAlignment), c.Xpara.ToString());
 
                        //第二种创建段落的方法
                        CT_P ctp = doc.Document.body.AddNewP();
                        ctp.AddNewPPr().AddNewJc().val = (ST_Jc)Enum.Parse(typeof(ST_Jc), c.Xpara.Align.ToString().ToLower());//ST_Jc.center
 
                        XWPFParagraph gp = new XWPFParagraph(ctp, doc);
                        if (c.Xpara.FirstIdentity > 0)
                        {
                            gp.IndentationFirstLine = c.Xpara.FirstIdentity;
                        }
                        //单倍为默认值（240twip）不需设置，1.5倍=240X1.5=360twip，2倍=240X2=480twip
                        if (!string.IsNullOrEmpty(c.Xpara.ParaStyle.LineDistance))
                        {
                            ctp.AddNewPPr().AddNewSpacing().line = c.Xpara.ParaStyle.LineDistance;
                        }
                        ctp.AddNewPPr().AddNewSpacing().lineRule = ST_LineSpacingRule.exact;
 
                        //创建run
                        XWPFRun pr = gp.CreateRun();
                        if (!string.IsNullOrEmpty(c.Xpara.ParaStyle.FontFamily))
                        {
                            pr.GetCTR().AddNewRPr().AddNewRFonts().ascii = c.Xpara.ParaStyle.FontFamily;
                            pr.GetCTR().AddNewRPr().AddNewRFonts().eastAsia = c.Xpara.ParaStyle.FontFamily;
                            pr.GetCTR().AddNewRPr().AddNewRFonts().hint = ST_Hint.eastAsia;
                        }
                        if (c.Xpara.ParaStyle.FontSize > 0)
                        {
                            pr.GetCTR().AddNewRPr().AddNewSz().val = (ulong)c.Xpara.ParaStyle.FontSize;
                            pr.GetCTR().AddNewRPr().AddNewSzCs().val = (ulong)c.Xpara.ParaStyle.FontSize;
                        }
                        pr.GetCTR().AddNewRPr().AddNewB().val = c.Xpara.ParaStyle.IsBold;
                        pr.GetCTR().AddNewRPr().AddNewI().val = c.Xpara.ParaStyle.IsItalic;
                        if (!string.IsNullOrEmpty(c.Xpara.ParaStyle.RgbColor))
                        {
                            pr.GetCTR().AddNewRPr().AddNewColor().val = c.Xpara.ParaStyle.RgbColor;
                        }
                        pr.SetText(c.Xpara.Content);
                        #endregion
                    }
                    
                }
                #endregion
 
                #region 表格
                if (c.XTable != null)
                {
                    //第一种新增表格的方法
                    CT_Tbl tbl = doc.Document.body.AddNewTbl();
                    XWPFTable tab = new XWPFTable(tbl, doc);//创建一行一列表
                    tab.SetCellMargins(c.XTable.MarginTop, c.XTable.MarginLeft, c.XTable.MarginBottom, c.XTable.MarginRight);
                    tbl.AddNewTblPr().jc = new CT_Jc();
                    tbl.AddNewTblPr().jc.val = ST_Jc.center;//表格居中对齐
 
                    //设置表格宽度
                    if (c.XTable.Width > 0)
                    {
                        tbl.AddNewTblPr().AddNewTblW().w = c.XTable.Width.ToString();
                    }
                    tbl.AddNewTblPr().AddNewTblW().type = ST_TblWidth.dxa;
 
                    tbl.tblPr.tblpPr = new CT_TblPPr();
                    //表格定位
                    //若tblpXSpec、tblpX同时存在，则tblpXSpec优先tblpX；
                    //若tblpYSpec、tblpY同时存在，则tblpYSpec优先tblpY；
                    if (c.XTable.Pxy != null)
                    {
                        tbl.tblPr = new CT_TblPr();
                        tbl.tblPr.tblpPr.tblpX = c.XTable.Pxy.X.ToString();//左上角坐标
                        tbl.tblPr.tblpPr.tblpY = c.XTable.Pxy.Y.ToString();
                    }
 
                    if (c.XTable.TabLeft > 0) tbl.tblPr.tblpPr.leftFromText = (ulong)c.XTable.TabLeft;
                    if (c.XTable.TabRight > 0) tbl.tblPr.tblpPr.rightFromText = (ulong)c.XTable.TabRight;
                    tbl.tblPr.tblpPr.vertAnchor = ST_VAnchor.text;
                    tbl.tblPr.tblpPr.horzAnchor = ST_HAnchor.page;
 
                    第二种方式新增表格
                    //var t = doc.CreateTable(c.XTable.RowNum, c.XTable.ColNum);
                    //t.SetCellMargins(c.XTable.MarginTop, c.XTable.MarginLeft, c.XTable.MarginBottom, c.XTable.MarginRight);
                    //foreach (var row in c.XTable.Rows)
 
                    //前面创建的表只有一行一列,这里将它补齐
                    //按c.XTable的RowNum和ColNum生成x行y列表格，并且设置好单元格的宽度
                    if (c.XTable.RowNum > 0 && c.XTable.ColNum > 0)
                    {
                        if (c.XTable.Rows == null) c.XTable.Rows = new List<TabRow>();
                    }
                    for (int i = 0; i < c.XTable.RowNum; i++)
                    {
                        XWPFTableRow tr = null;
                        if (i > 0)
                        {
                            tr = tab.InsertNewTableRow(i - 1);
                        }
                        else
                        {
                            tr = tab.GetRow(i);
                        }
                        var myrow = c.XTable.Rows.FirstOrDefault(m => m.RowIndex == i);
                        if (myrow == null)
                        {
                            myrow = new TabRow();
                        }
                        if (myrow.Cells == null)
                        {
                            myrow.Cells = new List<TabCell>();
                        }
                        for (int k = 0; k < c.XTable.ColNum-1; k++)
                        {
                            //因为是在已有的单元格内进行分割，因此要减一
                            XWPFTableCell cell = tr.AddNewTableCell();
                            CT_Tc ctc = cell.GetCTTc();
                            var curcell = myrow.Cells.FirstOrDefault(m => m.CellIndex == k);
                            if (curcell == null)
                            {
                                continue;
                            }
                            if (curcell.Width > 0)
                            {
                                CT_TcPr curtcpr = ctc.AddNewTcPr();
                                curtcpr.tcW = new CT_TblWidth();
                                curtcpr.tcW.w = curcell.Width.ToString();
                            }
                            
                            if (curcell.CStyle != null)
                            {
                                //给单元格的内容加格式
                                XWPFParagraph para = cell.AddParagraph();
                                XWPFRun xr= para.CreateRun();
                                //设置字体
                                if (!string.IsNullOrEmpty(curcell.CStyle.FontFamily))
                                {
                                    xr.GetCTR().AddNewRPr().AddNewRFonts().ascii = curcell.CStyle.FontFamily;
                                    xr.GetCTR().AddNewRPr().AddNewRFonts().eastAsia = curcell.CStyle.FontFamily;
                                    xr.GetCTR().AddNewRPr().AddNewRFonts().hint = ST_Hint.eastAsia;
                                    //xr.SetFontFamily(curcell.CStyle.FontFamily, FontCharRange.Ascii);
                                    //xr.SetFontFamily(curcell.CStyle.FontFamily, FontCharRange.EastAsia);
                                }
                                if (curcell.CStyle.FontSize > 0)
                                {
                                    xr.GetCTR().AddNewRPr().AddNewSz().val = (ulong)curcell.CStyle.FontSize;
                                    xr.GetCTR().AddNewRPr().AddNewSzCs().val = (ulong)curcell.CStyle.FontSize;
                                }
                                xr.GetCTR().AddNewRPr().AddNewB().val = curcell.CStyle.IsBold;
                                xr.GetCTR().AddNewRPr().AddNewI().val = curcell.CStyle.IsItalic;
                                //设置颜色
                                if(!string.IsNullOrEmpty(curcell.CStyle.RgbColor))
                                    xr.SetColor(curcell.CStyle.RgbColor);
                                xr.SetText(curcell.Content);
                                
                            }
                            else
                            {
                                if (curcell.Content != null) cell.SetText(curcell.Content);
                            }
                        }
                        
                    }
                }
                #endregion
            }
 
            using (MemoryStream stream=new MemoryStream())
            {
                doc.Write(stream);
                stream.Flush();
                stream.Close();
                stream.Dispose();
                SaveToFile(stream, filePath);
            }
        }
 
        static void SaveToFile(MemoryStream ms, string fileName)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.Create, FileAccess.Write))
            {
                byte[] data = ms.ToArray();
                fs.Write(data, 0, data.Length);
                fs.Flush();
                data = null;
            }
        }
 
        /// <summary>
        /// 计算点数
        /// </summary>
        /// <param name="fontname"></param>
        /// <param name="fontsize"></param>
        /// <param name="Indentationfonts"></param>
        /// <param name="fs"></param>
        /// <returns></returns>
        protected int Indentation(String fontname, int fontsize, int Indentationfonts, FontStyle fs)
        {
            //字显示宽度，用于段首行缩进
            /*字号与fontsize关系
             * 初号（0号）=84，小初=72，1号=52，2号=44，小2=36，3号=32，小3=30，4号=28，小4=24，5号=21，小5=18，6号=15，小6=13，7号=11，8号=10
             */
            Graphics m_tmpGr = new Control().CreateGraphics();
            //Graphics m_tmpGr = this.CreateGraphics();
            
            m_tmpGr.PageUnit = GraphicsUnit.Point;
            SizeF size = m_tmpGr.MeasureString("好", new Font(fontname, fontsize * 0.75F, fs));
            return (int)size.Width * Indentationfonts * 10;
        }
 
        /// <summary>
        /// 给定一个图片路径，得出合适的长宽插入文档中
        /// </summary>
        /// <param name="imgpath"></param>
        /// <param name="imgw"></param>
        /// <param name="imgh"></param>
        public static void CalcImgWH(string imgpath, ref int imgw, ref int imgh)
        {
            if (!File.Exists(imgpath)) return;
            Bitmap bmap = new Bitmap(imgpath);
            SizeF size = bmap.PhysicalDimension;
            imgw = (int)size.Width;
            imgh = (int)size.Height;
            decimal d = 70;//算出一厘米的大概像素,1CM=360000EMUS
            imgw = (int)(imgw * 360000 / d);
            imgh = (int)(imgh * 360000 / d);
        }
 
        /// <summary>
        /// 给定一个图片流，得出合适的长宽插入文档中
        /// </summary>
        /// <param name="imgpath"></param>
        /// <param name="imgw"></param>
        /// <param name="imgh"></param>
        public static void CalcImgWH(Stream stream, ref int imgw, ref int imgh)
        {
            Bitmap bmap = new Bitmap(stream);
            SizeF size = bmap.PhysicalDimension;
            imgw = (int)size.Width;
            imgh = (int)size.Height;
            decimal d = 70;//算出一厘米的大概像素,1CM=360000EMUS
            imgw = (int)(imgw * 360000 / d);
            imgh = (int)(imgh * 360000 / d);
        }
    }
 
    
 
    public class WordModel
    {
        /// <summary>
        /// 段落
        /// </summary>
        public ParaGragh Xpara { set; get; }
 
        /// <summary>
        /// 表格集合
        /// </summary>
        public Table XTable { set; get; }
    }
 
    /// <summary>
    /// 段落实体
    /// </summary>
    public class ParaGragh
    {
        /// <summary>
        /// 段落的文本内容
        /// </summary>
        public string Content { set; get; }
 
        /// <summary>
        /// 首行缩进点数，一般设置为100,约两个字
        /// </summary>
        public int FirstIdentity { set; get; }
 
        /// <summary>
        /// 文字的对齐方式
        /// </summary>
        public AlignMent Align { set; get; }
 
        /// <summary>
        /// 字体样式
        /// </summary>
        public Style ParaStyle { set; get; }
 
        /// <summary>
        /// 图片
        /// </summary>
        public Picture Pic { set; get; }
        
    }
 
    /// <summary>
    /// 图片
    /// </summary>
    public class Picture
    {
        public ParType Ptype { set; get; }
        public WrapType Wrap { set; get; }
 
        public PictureTp PicFormat { set; get; }
 
        public string PicName { set; get; }
        public string FilePath { set; get; }
 
        /// <summary>
        /// 宽，单位：EMUS,1CM=360000EMUS
        /// </summary>
        public int Width { set; get; }
 
        /// <summary>
        /// 高，单位：EMUS,1CM=360000EMUS
        /// </summary>
        public int Height { set; get; }
 
        /// <summary>
        /// 对齐方式
        /// </summary>
        public PosType Postp { set; get; }
 
        /*项目中的图基本上都会以上下的方式进行显示，所以图片特效和阴影之类的都不考虑*/
    }
 
    public class Table
    {
        /// <summary>
        /// 表格有多少行
        /// </summary>
        public int RowNum { set; get; }
 
        /// <summary>
        /// 表格有多少列
        /// </summary>
        public int ColNum { set; get; }
 
        /// <summary>
        /// 左边距
        /// </summary>
        public int MarginLeft { set; get; }
 
        /// <summary>
        /// 右边距
        /// </summary>
        public int MarginRight { set; get; }
 
        /// <summary>
        /// 下边距
        /// </summary>
        public int MarginBottom { set; get; }
 
        /// <summary>
        /// 上边距
        /// </summary>
        public int MarginTop { set; get; }
 
        /// <summary>
        /// 表格的行的集合
        /// </summary>
        public List<TabRow> Rows { set; get; }
 
        /// <summary>
        /// 宽度
        /// </summary>
        public int Width { set; get; }
 
        /// <summary>
        /// 左上角位置
        /// </summary>
        public Point Pxy { set; get; }
 
        /// <summary>
        /// 表格离左边的间距
        /// </summary>
        public int TabLeft { set; get; }
 
        /// <summary>
        /// 表格离右边的间距
        /// </summary>
        public int TabRight { set; get; }
    }
 
    public class TabRow
    {
        /// <summary>
        /// 行标
        /// </summary>
        public int RowIndex { set; get; }
 
        /// <summary>
        /// 本行的单元格集合
        /// </summary>
        public List<TabCell> Cells { set; get; }
    }
 
    public class TabCell
    {
        /// <summary>
        /// 列标
        /// </summary>
        public int CellIndex { set; get; }
 
        /// <summary>
        /// 是否是合并列
        /// </summary>
        public bool IsMege { set; get; }
 
        /// <summary>
        /// 合并的列数，此处只考虑在本行水平往后合并
        /// </summary>
        public int MegeNum { set; get; }
 
        /// <summary>
        /// 单元格宽
        /// </summary>
        public int Width { set; get; }
 
        /// <summary>
        /// 单元格高
        /// </summary>
        public int Height { set; get; }
 
        /// <summary>
        /// 单元格的内容
        /// </summary>
        public string Content { set; get; }
 
        /// <summary>
        /// 带格式的单元格内容
        /// </summary>
        public Style CStyle { set; get; }
    }
 
    /// <summary>
    /// 样式
    /// </summary>
    public class Style
    {
        /// <summary>
        /// 行间距，固定值是20磅
        /// </summary>
        public string LineDistance { set; get; }
 
        /// <summary>
        /// 文字大小
        /// </summary>
        public int FontSize { set; get; }
 
        /// <summary>
        /// 字体
        /// </summary>
        public string FontFamily { set; get; }
 
        /// <summary>
        /// 是否倾斜
        /// </summary>
        public bool IsItalic { set; get; }
 
        /// <summary>
        /// 是否加粗
        /// </summary>
        public bool IsBold { set; get; }
 
        /// <summary>
        /// 文字RGB色,如：red
        /// </summary>
        public string RgbColor { set; get; }
    }
 
    public class Point
    {
        /// <summary>
        /// x坐标
        /// </summary>
        public int X { set; get; }
 
        /// <summary>
        /// y坐标
        /// </summary>
        public int Y { set; get; }
    }
 
    /// <summary>
    /// 文字的水平对齐方式
    /// </summary>
    public enum AlignMent
    {
        BOTH = 1,
        CENTER = 2,
        DISTRIBUTE = 3,
        HIGH_KASHIDA = 4,
        LEFT = 5,
        LOW_KASHIDA = 6,
        MEDIUM_KASHIDA = 7,
        NUM_TAB = 8,
        RIGHT = 9,
        THAI_DISTRIBUTE = 10
    }
 
    /// <summary>
    /// 图片插入的方式
    /// </summary>
    public enum ParType
    {
        /// <summary>
        /// 内嵌式
        /// </summary>
        inline=1,
        /// <summary>
        /// 锚式，可以拖动的那种
        /// </summary>
        anchor=2
    }
 
    /// <summary>
    /// 图片与文字关系
    /// </summary>
    public enum WrapType
    {
        /// <summary>
        ///四周型
        /// </summary>
        wrapSquare= 1,
        /// <summary>
        /// 紧密型
        /// </summary>
        wrapTight=2,
        /// <summary>
        /// 穿越型
        /// </summary>
        wrapThrough=3,
        /// <summary>
        /// 上下型
        /// </summary>
        wrapTopAndBottom=4,
        /// <summary>
        /// 上方型，图在左上角
        /// </summary>
        wrapNoneBehindDoc=5,
        /// <summary>
        /// 下方型，图左下角
        /// </summary>
        wrapBehindDoc=6
    }
 
    /// <summary>
    /// 图片类型
    /// </summary>
    public enum PictureTp
    {
        EMF = 2,
        WMF = 3,
        PICT = 4,
        JPEG = 5,
        PNG = 6,
        DIB = 7,
        GIF = 8,
        TIFF = 9,
        EPS = 10,
        BMP = 11,
        WPG = 12,
    }
 
    /// <summary>
    /// 图片与文字的对齐方式
    /// </summary>
    public enum PosType
    {
        /// <summary>
        /// 两侧
        /// </summary>
        Besides=1,
        /// <summary>
        /// 左
        /// </summary>
        Left=2,
        /// <summary>
        /// 右
        /// </summary>
        Right=3,
        /// <summary>
        /// 最大一侧
        /// </summary>
        Largest=4
    }
}

以下是测试代码：
chart1.Series.Clear();//清除默认的图例
            chart1.BackColor = ColorTranslator.FromHtml("#D3DFF0");//用网页颜色
            chart1.BackGradientStyle = GradientStyle.TopBottom;//渐变背景，从上到下
            chart1.BorderlineDashStyle = ChartDashStyle.Solid;//外框线为实线
            chart1.BorderlineWidth = 2;
 
            Series zser = new Series("正面");
            Series fser = new Series("负面");
 
            //构造正面数据
            zser.Points.AddXY("昨日", 4);
            zser.Points.AddXY("今日", 5);
            zser.Points.AddXY("上周", 20);
            zser.Points.AddXY("本周", 15);
            zser.Points.AddXY("上月", 40);
            zser.Points.AddXY("本月", 50);
            zser["PointWidth"] = "0.6";
 
            //构造负面数据
            fser.Points.AddXY("昨日", 6);
            fser.Points.AddXY("今日", 23);
            fser.Points.AddXY("上周", 37);
            fser.Points.AddXY("本周", 25);
            fser.Points.AddXY("上月", 30);
            fser.Points.AddXY("本月", 40);
            fser["PointWidth"] = "0.6";
            zser.IsValueShownAsLabel = true;
            zser.ChartType = SeriesChartType.Column;
            fser.IsValueShownAsLabel = true;
            fser.ChartType = SeriesChartType.Column;
            //fser.Color = Color.Red;
            //series["DrawingStyle"] = "cylinder";
            //chart1.Legends[0].Enabled = false;//是否显示图例
 
            chart1.Series.Add(zser);
            chart1.Series.Add(fser);
            chart1.ChartAreas[0].BackColor = Color.Transparent;//数据区域的背景，默认为白色
            chart1.ChartAreas[0].BackGradientStyle = GradientStyle.TopBottom;
            chart1.ChartAreas[0].BorderDashStyle = ChartDashStyle.Solid;
            chart1.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.FromArgb(64, 64, 64, 64);//数据区域，纵向的线条颜色
            chart1.ChartAreas[0].AxisX.MajorGrid.Interval = 3;//主网格间距
            chart1.ChartAreas[0].AxisX.MinorGrid.Interval = 2;//副网格间距
            chart1.ChartAreas[0].AxisY.MajorGrid.LineColor = Color.FromArgb(64, 64, 64, 64);//数据区域，横向线条的颜色
            chart1.Titles.Add(string.Format("舆情统计"));
            chart1.Titles.Add(string.Format("{0}",DateTime.Now.ToString("yyyy-MM-dd HH:mm")));
            chart1.Titles[0].Font = new Font("微软雅黑", 18, FontStyle.Bold);
            chart1.ChartAreas[0].AxisY.Title = "数量";
            chart1.Width = 900;
            chart1.Height = 450;

测试是用winform写的，所以直接拖了个图表控件在窗体上。


```



# Excel



```
# https://blog.csdn.net/weixin_42176639/article/details/101648803
	# NOPI读写Excel，并插入图片


```





# FFMPEG



```
# ffmpeg 录制 hls 直播经常出现 HTTP error 404 Not Found
ffmpeg -headers "Referer: http://popkontv.com`r`nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31`r`n" -i "input.m3u8" -c copy "C:\live\output.mp4"

紧跟着 -i 的前面，加个 -re，再试试。

```





```
# Nuget 安装 MedallionShell
            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录
            string path = new DirectoryInfo("../").FullName;  // 上级目录

            string fname = @"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv";
            string frtname = $"{ecxutePath}/out.srt";
            var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            var ffmpegArgs = new List<string>() { "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname };

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs); // 执行命令

            using (StreamWriter sw = File.AppendText(outlog)) // 写入日志
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }
```





```c#
            /*
            out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
            out_text = out_bytes.decode('utf-8')

            https://gist.github.com/bobend/ae229860d4f69c563c3555e3ccfc190d
				# LINQPad

            c# ffmpeg stream

			https://stackoverflow.com/questions/15758114/using-ffmpeg-in-c-sharp-project
		

            https://github.com/rosenbjerg/FFMpegCore
                // FFMpegCore

            */


            //ffmpeg.StartInfo.UseShellExecute = false;
            //ffmpeg.StartInfo.RedirectStandardOutput = true;
            //ffmpeg.StartInfo.FileName = Server.MapPath("~/Video_Clips/ffmpeg.exe");

            //ffmpeg.StartInfo.Arguments = String.Format(@"-i ""{0}"" -threads 8 -f webm -aspect 16:9 -vcodec libvpx -deinterlace -g 120 -level 216 -profile 0 -qmax 42 -qmin 10 -rc_buf_aggressivity 0.95 -vb 2M -acodec libvorbis -aq 90 -ac 2 ""{1}""",
            //										   Server.MapPath("~/Video_Clips/" + sNameWithoutExtension + ".wmv"),
            //										   Server.MapPath("~/Video_Clips/" + sNameWithoutExtension + ".webm"));
            //ffmpeg.Start();

            //ffmpeg.WaitForExit();

            var startInfo = new ProcessStartInfo('path/to/ffmpeg');
            startInfo.RedirectStandardInput = true;
            startInfo.RedirectStandardOutput = true;
            startInfo.UseShellExecute = false;

            var argumentBuilder = new List<string>();
            argumentBuilder.Add("-loglevel panic"); // this makes sure only data is sent to stdout
            argumentBuilder.Add("-i pipe:.mp3"); //this sets the input to stdin

            // the target audio specs are as follows
            argumentBuilder.Add($"-f wav");
            argumentBuilder.Add("-ac 1");
            argumentBuilder.Add($"-ar 44100");
            argumentBuilder.Add("pipe:1"); // this sets the output to stdout

            startInfo.Arguments = String.Join(" ", argumentBuilder.ToArray());

            var _ffMpegProcess = new Process();
            _ffMpegProcess.StartInfo = startInfo;

            _ffMpegProcess.Start();

            _ffMpegProcess.WaitForExit();


            // _ffMpegProcess.StandardInput.BaseStream.Write(byteBuffer);
            // We have to write the data to the FFMpeg input channel using Standard Input, we can do it like so:
            // 写入它的输入流

            while (true)
            {
                var bytes = new byte[1024];


                var result = await _ffMpegProcess.StandardOutput.BaseStream.ReadAsync(bytes);

                if (result == 0)
                {
                    // no data retrieved
                }
                else
                {
                    // do something with the data
                }
            }
```



### LINQPad



```C#
            await Command.Run(
                executable: "PING.exe",
                arguments: new object[] { "127.0.0.1", "/t" },
                options: o => o.Timeout(TimeSpan.FromSeconds(1))
             )
            .RedirectTo(new FileInfo(@"C:\Temp\shellTestOuput.txt"))
            .Task;
# Timeout 异常需要处理
```



```c#
# https://github.com/madelson/MedallionShell/issues/80
	var command = Command.Run(
                  executable: "cmd.exe",
                  arguments: new[] { "/c", "ping", "127.0.0.1", "/t" },
                  options: o => { } // no timeout
        )
        .RedirectTo(new FileInfo(@"C:\Temp\shellTestOuput.txt"));
            // manually set up a timeout with graceful shutdown
            await Task.Delay(TimeSpan.FromSeconds(1))
               .ContinueWith(_ =>
               {
                   // 尝试给目标进程发送 CTRL+C 命令，让它自动退出终止自身进程
                   if (!command.TrySignalAsync(CommandSignal.ControlC).Result
                       || !command.Task.Wait(TimeSpan.FromSeconds(1)))
                   {
                       // only resort to kill if sending the signal fails (it shouldn't) or if the command doesn't
                       // promptly exit after the signal is sent
                       command.Kill();  // 超时以后还没有退出，则强行Kill 掉
                   }
               });
```



```c#
void Main()
{
	var sc = @"C:\Users\...\MedallionShell\SampleCommand\bin\Debug\net46\SampleCommand.exe";
	var process = new Process { StartInfo = { FileName = sc, RedirectStandardOutput = true, RedirectStandardInput = true, UseShellExecute = false, CreateNoWindow = true } };
	process.Start();
	try
	{
		var standardOutput = (FileStream)process.StandardOutput.BaseStream;
		var newHandle = ReOpenFile(standardOutput.SafeFileHandle.DangerousGetHandle(), FileAccess.Read, FileShare.Write, ((FileAttributes)0x40000000).Dump());
		newHandle.Dump();
		Marshal.GetLastWin32Error().Dump();
		var newSafeHandle = new SafeFileHandle(newHandle, ownsHandle: true);
		var stream = new FileStream(newSafeHandle, FileAccess.Read, 1024, isAsync: true);
	}
	finally {
		process.Kill();
	}
}

[DllImport("kernel32.dll", SetLastError = true)]
public static extern IntPtr ReOpenFile(IntPtr originalFile, FileAccess dwDesiredAccess, FileShare dwShareMode, FileAttributes dwFlagsAndAttributes);
```



```c#
# 原命令
c:\tmp\magick.exe c:\tmp\a.jpg -depth 8 ppm:- | c:\tmp\jpeg-recompress.exe --ppm - c:\tmp\b.jpg

# MedallionShell 实现
string magickExe = @"c:\tmp\magick.exe";
string jpegRecompressExe = @"c:\tmp\jpeg-recompress.exe";
string logFile = @"c:\tmp\log.txt";
var magickArgs = new List<string>() { @"c:\tmp\a.jpg", "-depth", "8", "ppm:-" };
var jpegRecompressArgs = new List<string>() { "--ppm", "-", @"c:\tmp\b.jpg" };

var command = Command.Run(magickExe, magickArgs).PipeTo(Command.Run(jpegRecompressExe, jpegRecompressArgs));
using (StreamWriter sw = File.AppendText(logFile))
{
  sw.WriteLine($"Exit code: {command.Result.ExitCode}");
  sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
  sw.WriteLine($"Stderr: {command.Result.StandardError}");
}
```





```
# vs2019 用NuGet 安装MedallionShell
Command.Run("/path/to/bash", "-c", $"/usr/local/bin/youtube-dl --no-progress {cleanURL}");

```





```
# vs2019 用NuGet 安装MedallionShell
# ffmpeg-process-pining-MedallionShell.linq

<Query Kind="Program">
  <NuGetReference>MedallionShell</NuGetReference>
  <Namespace>System.Threading.Tasks</Namespace>
  <Namespace>Medallion.Shell</Namespace>
  <Namespace>Medallion.Shell.Streams</Namespace>
</Query>

DumpContainer dc;
async Task Main()
{	var input = @"D:\Temp\fieldtest.mxf".Dump("input file");
	var output = @"D:\Temp\out43.mp4".Dump("output file");
	var cmdPath =  @"D:\Temp\ffmpeg.exe"; 
	var args = "-i pipe:0 -c:v libx264 -b:v 2600k -c:a aac -b:a 128k -f mp4 -movflags frag_keyframe+empty_moov -y pipe:1";	
	$"{cmdPath} {args}".Dump("cmd line");
	dc = new DumpContainer().Dump("ffmpeg standard error out");
	
	using (var inputStream = File.OpenRead(input))
	using (var outputStream = File.OpenWrite(output))
	using (var cmd = Command.Run(cmdPath, options: o => o.StartInfo(i => i.Arguments = args)))
	{		
		var inputTask = cmd.StandardInput.PipeFromAsync(inputStream);
		var outputTask = cmd.StandardOutput.PipeToAsync(outputStream);
		var cs = new CancellationTokenSource();	
		var logTask = ReadError(cmd.StandardError, cs.Token);			
		await inputTask;
		await outputTask;
		cs.Cancel();
		await logTask;
	}
}

async Task ReadError(ProcessStreamReader reader, CancellationToken token) {
	while (!token.IsCancellationRequested)
		dc.Content += $"{await Task<string>.Run(reader.ReadLineAsync, token)}{Environment.NewLine}";
	
}
```







```
                Image img = Image.FromFile(distPath);
                string showImgData = util.imgToBase64(img);
                img.Dispose();
```



### cs-script

- https://github.com/oleg-shilo/cs-script
  - C# 脚本语言





# 进程、异步、流



```
        //声明委托
        private delegate Mat calcHandler(string img_path, bool autoCut, bool binarize = false, bool autoSize = false, string scale = null);

        //代理方法
        public Mat calc(string img_path, bool autoCut, bool binarize = false, bool autoSize = false, string scale = null)
        
        
                //异步调用
        public async void calc_all(List<string> img_paths, bool autoCut, bool binarize = false, bool autoSize = false, string scale = null)
        {

            if (img_paths.Count <= 0)
            {
                return;
            }

            calcHandler handler = new calcHandler(calc);

            imgBoardForm.g_total = img_paths.Count;
            imgBoardForm.g_curr = 0;

            string path = img_paths[imgBoardForm.g_curr];
            IAsyncResult result = handler.BeginInvoke(path, this.radioButton1.Checked, this.checkBox1.Checked, this.radioButton3.Checked, (string)this.listBox1.SelectedItem, new AsyncCallback(CallBack), "one task done.");

        }

        //异步回调方法
        public void CallBack(IAsyncResult result)
        {
            //AsyncResult 是IAsyncResult接口的一个实现类，空间：System.Runtime.Remoting.Messaging
            //AsyncDelegate 属性可以强制转换为用户定义的委托的实际类。
            calcHandler handler = (calcHandler)((AsyncResult)result).AsyncDelegate;

            var img_paths = imgBoardForm.g_img_paths;

            string path = img_paths[imgBoardForm.g_curr];

            string basename = Path.GetFileName(path);

            string msg = $"处理进度：{imgBoardForm.g_curr+1} /{imgBoardForm.g_img_paths.Count}";

            _syncContext.Post(SetButtonText, msg);//子线程中通过UI线程上下文更新UI

            //等待函数执行完毕
            var image = handler.EndInvoke(result);

            var state = result.AsyncState;

            if (imgBoardForm.g_dic_images.ContainsKey(basename))
            {

                //var img = imgBoardForm.g_dic_images[basename];
                //img.Dispose();

            }
            //imgBoardForm.g_dic_images[basename] = image;


            string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(path)}";

            //保存到临时目录
            image.SaveImage(dist);

            image.Dispose();

            Thread.Sleep(100);
            File.Delete(path);
            Thread.Sleep(100);
            File.Move(dist, path);

            Thread.Sleep(100);
            File.Delete(dist);
            Thread.Sleep(100);

            // 一个图片处理异步任务完成
            imgBoardForm.g_curr += 1;



            if (imgBoardForm.g_curr < imgBoardForm.g_img_paths.Count)
            {
                // 开始下一个任务
                path = img_paths[imgBoardForm.g_curr];

                IAsyncResult result2 = handler.BeginInvoke(path, this.radioButton1.Checked, this.checkBox1.Checked, this.radioButton3.Checked, (string)this.listBox1.SelectedItem, new AsyncCallback(CallBack), "one task done.");

            }
            else
            {
                _syncContext.Post(SetButtonText, "一键处理全部图片");//子线程中通过UI线程上下文更新UI
                MessageBox.Show("全部图片处理完成.");
            }

        }
```





```
private void button4_Click(object sender, EventArgs e)
        {
            using (BackgroundWorker bw = new BackgroundWorker())
            {
                bw.RunWorkerCompleted += new RunWorkerCompletedEventHandler(bw_RunWorkerCompleted);
                bw.DoWork += new DoWorkEventHandler(bw_DoWork);
                bw.RunWorkerAsync("Tank");
            }         
        }

        void bw_DoWork(object sender, DoWorkEventArgs e)
        {       
            // 这里是后台线程， 是在另一个线程上完成的
            // 这里是真正做事的工作线程
            // 可以在这里做一些费时的，复杂的操作
            Thread.Sleep(5000);
            e.Result = e.Argument + "工作线程完成";
        }

        void bw_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            //这时后台线程已经完成，并返回了主线程，所以可以直接使用UI控件了 
            this.label4.Text = e.Result.ToString(); 
        }
```







```
The much easier way would be to do just use cmd as your process.

Process test = new Process();
test.StartInfo.FileName = "cmd";
test.StartInfo.Arguments = @"/C ""echo testing | grep test""";
test.Start();
You can capture the output or whatever else you want like any normal process then. This was just a quick test I built, but it works outputting testing to the console so I would expect this would work for anything else you plan on doing with the piping. If you want the command to stay open then use /K instead of /C and the window will not close once the process finishes.
```





```c#
# https://github.com/steaks/codeducky/blob/master/blogs/Processes.md
            https://gist.github.com/bobend/ae229860d4f69c563c3555e3ccfc190d
				# LINQPad
wrapping much of this complexity into a new .NET library: MedallionShell. With MedallionShell, this kind of task is a one-liner:

var output = Command.Run(pathToExecutable, arg1, ...).Result.StandardOutput;
More on that later, though. For now, let's get back to Process. As a concrete example, I recently wanted my application to launch an instance of NodeJS from .NET to run the less css compiler. I needed to write to Node's standard input while capturing the standard output text, standard error text, and exit code.

An initial attempt
Here's the code I started out with:

// not-quite-functional code
using (var process = new Process
	{
		StartInfo = 
		{
			FileName = /* Path to node */,
			// in my case, these were some file paths and options
			Arguments = string.Join(" ", new[] { arg1, arg2, ... }),
			CreateNoWindow = true,
			RedirectStandardError = true,
			RedirectStandardInput = true,
			RedirectStandardOutput = true,
			UseShellExecute = true,
		}
	}
)
{
	process.Start();
	process.StandardInput.Write(/* input data */);
	// signals to the process that there's no more input coming
	process.StandardInput.Close();
	var outText = process.StandardOutput.ReadToEnd();
	var errText = process.StandardError.ReadToEnd();
	process.WaitForExit();
	var exitCode = process.ExitCode;
}	
This code is quite verbose; unfortunately it's quite buggy as well.

Dealing with process arguments
One of the first problems we notice with this code is that the Arguments property on ProcessStartInfo is just a string. If the arguments we are passing are dynamic, we'll need to provide the appropriate escape logic before concatenating to prevent things like spaces in file paths from breaking. Escaping windows command line arguments is oddly complex; luckily, the code needed to implement it is well documented in this StackOverflow post. Thus, the first change we'll make is to add escaping logic:

...
// Escape() implementation based on the SO post
Arguments = string.Join(" ", new[] { arg1, arg2, ... }.Select(Escape)),
...
Dealing with deadlocks
A less-obvious problem is that of deadlocking. All three process streams (in, out, and error) are finite in how much content they can buffer. If the internal buffer fills up, then whoever is writing to the stream will block. In this code, for example, we don't read from the out and error streams until after the process has exited. That means that we could find ourselves in a case where Node exhausts it's error buffer. In that case, Node would block on writing to standard error, while our .NET app is blocked reading to the end of standard out. Thus, we've found ourselves in a deadlock!

The Process API provides a method that seems designed for dealing with this: BeginOutput/ErrorReadLine. With this method, you can subscribe to asynchronous "DataReceived" events instead of reading from the output streams directly. That way, you can listen to both streams at once. Unfortunately, this method provides no way to know when the last bit of data has been received. Because everything is asynchronous, it is possible (and I have observed this) for events to fire after WaitForExit() has returned.

Luckily, we can provide our own workaround using Tasks to asynchronously read from the streams while we wait for Node to exit:

...
var outTask = process.StandardOutput.ReadToEndAsync();
var errTask = process.StandardError.ReadToEndAsync();
process.WaitForExit();
var outText = outTask.Result;
var errText = errTask.Result;
...
Adding a timeout
Another issue we'd like to handle is that of a process hanging. Rather than waiting forever for the process to exit, our code would be more robust if we enforced a timeout instead:

...
if (!process.WaitForExit(TimeoutMillis))
{
	process.Kill();
	throw new TimeoutException(...);
}
...
Async all the way!
While we are now using async IO to read from the process streams, we are still blocking one .NET thread while waiting for the process to complete. We can further improve efficiency here by going fully async:

// now inside an async method
using (var process = new Process
	{
		...
		EnableRaisingEvents = true,
		...
	}
)
{
	...	
	var processExitedSource = new TaskCompletionSource();
	process.Exited += (o, e) => processExitedSource.SetResult(true);
	
	var exitOrTimeout = Task.WhenAny(processExitedSource.Task, Task.Delay(Timeout));
	if (await exitOrTimeout.ConfigureAwait(false) != processExitedSource.Task)
	{
		process.Kill();
		throw new TimeoutException(...);
	}
	...
}
Adapting to larger data volumes
Another question that might come up when trying to generalize this approach is that of data volume. If we are piping a large amount of data through the process, we'll likely want to replace the convenient ReadToEndAsync() calls with async read loops that process each piece of data as it comes in.				

```



## run exe as service

- https://www.codeproject.com/Articles/35773/Subverting-Vista-UAC-in-Both-32-and-64-bit-Archite

```
// obtain the process id of the winlogon process that 
// is running within the currently active session
Process[] processes = Process.GetProcessesByName("winlogon");
foreach (Process p in processes)
{
    if ((uint)p.SessionId == dwSessionId)
    {
        winlogonPid = (uint)p.Id;
    }
}

// obtain a handle to the winlogon process
hProcess = OpenProcess(MAXIMUM_ALLOWED, false, winlogonPid);

// obtain a handle to the access token of the winlogon process
if (!OpenProcessToken(hProcess, TOKEN_DUPLICATE, ref hPToken))
{
    CloseHandle(hProcess);
    return false;
}

// Security attibute structure used in DuplicateTokenEx and   CreateProcessAsUser
// I would prefer to not have to use a security attribute variable and to just 
// simply pass null and inherit (by default) the security attributes
// of the existing token. However, in C# structures are value types and   therefore
// cannot be assigned the null value.
SECURITY_ATTRIBUTES sa = new SECURITY_ATTRIBUTES();
sa.Length = Marshal.SizeOf(sa);

// copy the access token of the winlogon process; 
// the newly created token will be a primary token
if (!DuplicateTokenEx(hPToken, MAXIMUM_ALLOWED, ref sa, 
    (int)SECURITY_IMPERSONATION_LEVEL.SecurityIdentification, 
    (int)TOKEN_TYPE.TokenPrimary, ref hUserTokenDup))
    {
      CloseHandle(hProcess);
      CloseHandle(hPToken);
      return false;
    }

 STARTUPINFO si = new STARTUPINFO();
 si.cb = (int)Marshal.SizeOf(si);

// interactive window station parameter; basically this indicates 
// that the process created can display a GUI on the desktop
si.lpDesktop = @"winsta0\default";

// flags that specify the priority and creation method of the process
int dwCreationFlags = NORMAL_PRIORITY_CLASS | CREATE_NEW_CONSOLE;

// create a new process in the current User's logon session
 bool result = CreateProcessAsUser(hUserTokenDup,  // client's access token
                            null,             // file to execute
                            applicationName,  // command line
                            ref sa,           // pointer to process    SECURITY_ATTRIBUTES
                            ref sa,           // pointer to thread SECURITY_ATTRIBUTES
                            false,            // handles are not inheritable
                            dwCreationFlags,  // creation flags
                            IntPtr.Zero,      // pointer to new environment block 
                            null,             // name of current directory 
                            ref si,           // pointer to STARTUPINFO structure
                            out procInfo      // receives information about new process
                            );
```



```
Process proc = new Process();
proc.StartInfo.FileName = AppDomain.CurrentDomain.BaseDirectory + @"test.bat";
proc.StartInfo.CreateNoWindow = true;
proc.StartInfo.UseShellExecute = false;
proc.Start();
```



```

#include "stdafx.h"
#include <windows.h>
#include "string.h"
 
#include <iostream>
using namespace std;
 
string GetExePath();
 
int main(int argc, _TCHAR* argv[])
{
	if(argc != 2){
		return 0;
	}
	//Sleep(10*1000);
 
	string exePath = GetExePath();
	string parameter(argv[1]);
	string cmd;
	cmd.append(exePath);
	cmd.append("node.exe ");
	cmd.append(exePath);
	cmd.append("myApplication.js \"");
	cmd.append(parameter);
	cmd.append("\"");
 
	STARTUPINFO StartInfo ={sizeof(StartInfo)}; 
	PROCESS_INFORMATION ProcInfo;
	StartInfo.dwFlags = STARTF_USESHOWWINDOW;
	StartInfo.wShowWindow = false;
	CreateProcess(NULL,(LPSTR)cmd.c_str(), NULL, NULL, NULL, NULL, NULL, NULL, &StartInfo, &ProcInfo);
 
	return 0;
}
```



## 异步下载

- https://github.com/bezzad/Downloader/blob/master/src/Samples/Downloader.Sample/Program.cs

```

	private static void OnDownloadStarted(object sender, DownloadStartedEventArgs e)
        {
            var fname = $"Downloading {Path.GetFileName(e.FileName)}";
        }

        private static void OnDownloadFileCompleted(object sender, AsyncCompletedEventArgs e)
        {
            if (e.Cancelled)
            {
            }
            else if (e.Error != null)
            {

            }
            else
            {
                var a = "DONE";
            }

        }

        public static async Task Main(string[] args)
        {
            var downloadOpt = new DownloadConfiguration()
            {
                ChunkCount = 1, // file parts to download, default value is 1
                OnTheFlyDownload = true, // caching in-memory or not? default values is true
                ParallelDownload = false // download parts of file as parallel or not. Default value is false
            };
            var downloader = new DownloadService(downloadOpt);
            downloader.DownloadStarted += OnDownloadStarted;
            downloader.DownloadFileCompleted += OnDownloadFileCompleted;

            await downloader.DownloadFileTaskAsync("https://yingedu-ad3.oss-cn-hangzhou.aliyuncs.com/tk_ppt/27222/56647/第一节泌尿系统的解剖生理.pptx", @"G:\a.pptx");

```



## 调用外部程序

- https://gist.github.com/elerch/5628117

```
// NodeFromCSharp.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            var proc = new System.Diagnostics.Process();
            proc.StartInfo.CreateNoWindow = true;
            proc.StartInfo.RedirectStandardInput = true;
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.RedirectStandardError = true;
            proc.StartInfo.FileName = "node.exe";
            proc.StartInfo.Arguments = "-i";
            proc.Start();
            proc.BeginOutputReadLine();

            proc.StandardInput.WriteLine("2 + 2;");
            proc.StandardInput.WriteLine("setTimeout(function(){ process.exit();}, 10000).suppressOut;");
            proc.OutputDataReceived += proc_OutputDataReceived;
            proc.WaitForExit();
        }

        static void proc_OutputDataReceived(object sender, System.Diagnostics.DataReceivedEventArgs e)
        {
            Console.WriteLine(e.Data);
        }
    }
}
```



## interop rust 

- https://github.com/lmtr0/rust-chsarp-interop





# interop





## C++ 调用 node.dll



```
// C++ 调用 node.dll

#include <iostream>

#include "windows.h"

int main()
{
    HINSTANCE   ghDLL = NULL;
    ghDLL = LoadLibrary("D:\\GitHub\\node-14.21.1\\out\\Debug\\node.dll");

    typedef int (_cdecl* FunctionPtr) (int argc, wchar_t* wargv[]);

    FunctionPtr wmain;

    wmain = (FunctionPtr)GetProcAddress(ghDLL, "wmain");

    int argc = 2;

    wchar_t* wargv[] = {
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
      //(wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
      (wchar_t*)L"D:\\GitHub\\echodict\\pmserver\\server.js"
    };

    wmain(argc, wargv);

    std::cout << "Hello World!\n";
}
```



## C# 调用 node.dll



````
// C# 调用 node.dll

using System.Runtime.InteropServices;

        [DllImport("user32.dll", EntryPoint = "MessageBoxA")]
        public static extern int MsgBox(int hWnd, string msg, string caption, int type);

        // 定义给 C# 的传参，全部参数都定义在这个结构数组里
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        public struct wmain_params
        {
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
            public string[] wargv;  // 大小固定为 2 个元素
        }
        [DllImport("D:\\GitHub\\node-14.21.1\\out\\Debug\\node.dll", EntryPoint = "wmain", CallingConvention = CallingConvention.Cdecl, CharSet = CharSet.Unicode)]
        public static extern int wmain(int argc,  ref wmain_params wargv);


        static void Main(string[] args)
        {

            //ThreadPool.QueueUserWorkItem(s =>
            //{
                wmain_params pms = new wmain_params();
                pms.wargv = new string[] {
                    "C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
                    //"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
                    "D:\\GitHub\\echodict\\pmserver\\server.js"
                };

                wmain(2, ref pms);

            //});

            MsgBox(0, "C#调用DLL文件", "这是标题", 0x30);
        }
````





### 





## nodejs

### C# 调 nodejs

- https://github.com/agracio/edge-js
  
  - https://github.com/agracio/edge-js/issues/163  编译方法
  
    - https://github.com/agracio/edge-js#building-edgejs-nuget-package 编译 Nuget 包的方法
  
  - https://github.com/agracio/edge-js/issues/93
  
  - https://github.com/atom/node  node编译为 dll 的方法
  
    ```
    Script CLR from Node.js - this part requires to recompile new versions of Node.js and the binaries are stored under lib/native/win32. When you working with Node.js to CLR interaction you do need to have Node installed and the version you have is the one that is used by your application.
    
    Script Node.js from CLR - this is the one you are trying to use. It requires to fully recompile Node.js from source as dll rather than exe and is added to nuget package. Unlike option 1 it has no dependency on Node.js installation on machine and works as a standalone dll with no other dependencies, similar to any other dll that you install from nuget.
    ```
  
    
  
  ```
  
  # https://github.com/agracio/edge-js/issues/163
  
  https://nodejs.org/dist/v18.9.0/
  	# 先安装 node 18.9.0
  
  git clone -q --branch=master https://github.com/agracio/edge-js.git C:\projects\edge-js
  
  cd C:\projects\edge-js\
  
  git checkout -qf c1cfba1f063cf9c8fb983809eb08d114719cc6dc
  
  npm install -g node-gyp
  
  edge-js/package.json
  	# 修改成这个版本 "nan": "2.16.0"
  
  edge-js/src/common/edge.cpp
  		NAN_MODULE_WORKER_ENABLED(edge_coreclr, init)
  	#else
  		NAN_MODULE_WORKER_ENABLED(edge_nativeclr, init)
  
  	# 最后两行改成这样
  	
  edge-js/lib/edge.js
  	var versionMap = [
      	[ /^14\./, '14.19.3' ],
      	[ /^16\./, '16.15.1' ],
      	[ /^18\./, '18.9.0' ],
  	];
  
  	# versionMap 改成这样
  	
  	
  
  npm install
  	# 出错，没关系，下面先编译，完了以后再来执行一次
  
  cd tools
  ./build.bat release 18.9.0
  	./build.bat debug 18.9.0
  		# 这样方便以后断点调试
  
  	# 成功编译
  
  npm install
  	# 编译成功后再执行一次 
  
  
  打开 C:\projects\edge-js\EdgeJs.sln 工程，启动test 项目，提示缺少运行时
  
  https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-1.1.2-windows-x64-binaries
  	下载后，放在 C:\Program Files\dotnet\shared\Microsoft.NETCore.App\1.1.2
  
  再次运行，成功！
  
  
  
  # 建一个控制台新项目，添加引用项目 edgejs ，只需要加这一个
  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using System.Threading.Tasks;
  
  using EdgeJs;
  
  namespace ConsoleApp1
  {
      class Program
      {
          public static async Task Start()
          {
              var func = Edge.Func(@"
              return function (data, callback) {
                  callback(null, 'Node.js welcomes ' + data);
              }
          ");
  
              Console.WriteLine(await func(".NET"));
          }
  
  
          static void Main(string[] args)
          {
              Start().Wait();
  
              var a = 1;
          }
      }
  }
  
  
  # 上面编译出来的东西，是给 nodejs 用的，是让 nodejs 调 C#，没有 node.dll 生成，
  	所以控制台项目提示缺少 node.dll 
  	
  14.21.1 build
  
  
  
  # 下面编译 NuGet 包，给 C# 用，让 C# 调用 nodejs
  
  打开vs2019 开发者命令行窗口 Developer Command Prompt for VS 2019
  
  cd C:\projects\edge-js\tools
  build_double_new.bat 18.9.0
  	# 命令行里编译失败，但是值接打开 node.sln 什么都不改，可以编译成功
  	# C:\projects\edge-js\tools\build\node-18.9.0\out\Debug\libnode.dll
  
  
  
  ```
  
  - https://github.com/Elringus/DotNetJS  可能的替换品 但它必须用 blazor
  
- https://www.nuget.org/packages/EdgeJs

- https://zhuanlan.zhihu.com/p/554452304  编译Node.js

  - https://github.com/nodejs/node/issues/34539  解决问题

- https://zhuanlan.zhihu.com/p/359598262 Puerts 让 nodejs 兼容 C# 和 Unity 

  - https://www.cnblogs.com/1eon/p/16851750.html  使用VsCode调试UE5的PuerTs
  - https://github.com/passiony/puerts-framework  一键安装运行

  > 好像是个好东西

- https://bbs.kanxue.com/thread-68730.htm  exe当作dll 来调用

- https://github.com/nodejs/node/issues/28845  成功编译dll

  - https://github.com/nodejs/node/pull/30695/commits
  
  > ```
  > I was able to compile my Windows dll using @davidhouweling 's updated node.gyp from #30695
  > 
  > Run nuget pack to generate the .nupkg file
  > nuget pack <project-name>.nuspec
  > 
  > 一切正常，但是 edgejs 调用时 内存错误了，尝试直接调用 node.dll
  > 
  > dll.cpp
  > #include <stdint.h>
  > extern "C" __declspec(dllexport) uint64_t factorial(int max) {
  >     int i = max;
  >     uint64_t result = 1;
  >     while (i >= 2) {
  >         result *= i--;
  >     }
  >     return result;
  > }
  > 
  > 
  > call.c
  > 
  > #include "stdio.h"
  > #include "windows.h"
  > 
  > #pragma comment(lib, "C:\\Users\\i\\source\\repos\\ConsoleApplication1\\x64\\Debug\\Dll1.lib")
  > 
  > extern int factorial(int max);
  > 
  > int main()
  > {
  > 
  >     int cc = factorial(3);
  > 
  >     HMODULE    ghDLL = NULL;
  >     //ghDLL = LoadLibrary("C:\\Users\\i\\source\\repos\\ConsoleApplication1\\x64\\Debug\\Dll1.dll");
  >     ghDLL = LoadLibrary("C:\\Users\\i\\source\\repos\\ConsoleApplication1\\x64\\Debug\\node.dll");
  >     
  >     int a = 1;
  > 
  > }
  > ```
  
  ```
  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using System.Threading.Tasks;
  using EdgeJs;
  
  namespace ConsoleApp1
  {
      class Program
      {
          public static async Task Start()
          {
              var func = Edge.Func(@"
              return function (data, callback) {
                  callback(null, 'Node.js welcomes ' + data + process.version);
              }
          ");
  
              Console.WriteLine(await func(".NET"));
          }
  
          static void Main(string[] args)
          {
              Start().Wait();
          }
      }
  }
  ```
  
  



  ```
  
  https://github.com/nodejs/node/tags?after=v16.18.1
  	# 下载 v14.21.1 源码 
  
  .\vcbuild debug vs2019 dll x64
  .\vcbuild debug vs2019 dll x64 noprojgen # 不要再生成sln 工程文件
  
  无法解析的外部符号 __imp__timeGetTime@0
  	#pragma comment(lib, "winmm.lib")
  
  v8_base_without_compiler.lib(basic-block-profiler.obj) : error LNK2005
  	Oh, and manually removing v8_base_without_compiler from node References in VS solves this.
  	# 加入 winmm.lib 会引起的错误
  	
  	
  	
  
  ```

  

  - https://xiaoiver.github.io/coding/2018/05/14/%E7%BC%96%E8%AF%91-Node.js-%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6.html  nexe 支持打包node为单一exe
    
- https://github.com/MadLittleMods/node-usb-detection/  U盘插拔检测
  
- https://zhuanlan.zhihu.com/p/569304401  CEF与Node集成【0】架构简介

  > 收费咨询

- https://github.com/ElectronNET/Electron.NET/issues/211

  > electron 解决方案

- https://github.com/zyyc5/NodeSharp  low一点但兼容性好的方案

  - http://blog.qicheen.com/2022/04/14/nodesharp%E5%8E%9F%E7%90%86%E5%AE%9E%E7%8E%B0/

- https://juejin.cn/post/6982133816001462285  pkg 打包 node
  - https://segmentfault.com/a/1190000041958374
  - https://jingsam.github.io/2018/03/02/pkg.html

```

// edgejs 改造完成的成品

	private async Task<string>  Start()
        {
            // edgejs 原版的调用方法
            var func = Edge.Func(@"
            return function (data, callback) {
                //import {franc, francAll} from 'franc'
                let path = require('path')
                //let t = require(`${path.join(__dirname, 't.js')}`)
                //let d = t.path()
                //callback(null, 'Node.js welcomes ' + data + `${path.join(__dirname, 'temp.json')}`);
                //let ws = require('ws')
                //let langDetect = require('langdetect')
                let d = ( ()=>{
                    return 'paaaaa ' //+ ws.msg
                })()
                callback(null, 'Node.js welcomes ' + data + d);
            }
            ");
            //string ret = (string)await func(".NET");

            
            // 改造后的 edgejs 调用方法
            var func2 = Edge.Func(@"
                result = 'hi from double_edge.js ' + data   // data 是 C# 传进来的参数数据
                    // 约定 js 代码最后一句一定是 result = xxx , 这是代码运行最后得到的结果，它会自动赋值到沙盒里
            ");

            string ret = (string)await func2(".NET");


            /*
             
            D:\GitHub\echodict\cut\bin\x64\Debug\edge\double_edge.js

            compileFunc 函数改成这样

                var compileFunc = function (code, callback) {  // code 是 C# 传进来要执行的 js 代码

        var func = function (data, callback) {  // data 是 C# 传进来的参数数据

            var sandbox = { data }  // 把传进来的参数放在沙盒里面，因为要运行的 js 代码只能访问沙盒里面字段值
            const vm = require('vm')
            const script = new vm.Script(code)
            let ctx = vm.createContext(sandbox)
            script.runInContext(ctx)

            callback(null, sandbox.result)  // 约定 js 代码最后一句一定是 result = xxx , 这是代码运行最后得到的结果，它会自动赋值到沙盒里
        }

        if (typeof func !== 'function') {
            throw new Error('Node.js code must return an instance of a JavaScript function. '
                + 'Please use `return` statement to return a function.');
        }

        callback(null, func);
    };
             
             */

            return ret;
        }
```





```

// 成功改造运行目录下 edge 文件夹内的 compileFunc 函数
	// GitHub\echodict\cut\bin\x64\Debug\edge\double_edge.js

// 如需异步转同步，参见 GitHub\doc\lang\programming\nodejs summary.md 


double_edge.js

	var compileFunc = function (d, callback) {

        var func = function (data, callback) {

            let code = `
                result = 'hi from double_edge.js ' + data
            `

            var sandbox = {d, data}
            const vm = require('vm')
            const script = new vm.Script(code)
            let ctx = vm.createContext(sandbox)
            script.runInContext(ctx)

            callback(null, sandbox.result);
        }

        if (typeof func !== 'function') {
            throw new Error('Node.js code must return an instance of a JavaScript function. '
                + 'Please use `return` statement to return a function.');
        }

        callback(null, func);
    };
    
    
    
    

Form4.cs

using System.Threading.Tasks;
using System.Windows.Forms;
using CefSharp.WinForms;
using EdgeJs;

        private async Task<string>  Start()
        {
            var func = Edge.Func(@"
            return function (data, callback) {
                //import {franc, francAll} from 'franc'
                let path = require('path')
                //let t = require(`${path.join(__dirname, 't.js')}`)
                //let d = t.path()
                //callback(null, 'Node.js welcomes ' + data + `${path.join(__dirname, 'temp.json')}`);
                //let ws = require('ws')
                //let langDetect = require('langdetect')
                let d = ( ()=>{
                    return 'paaaaa ' //+ ws.msg
                })()
                callback(null, 'Node.js welcomes ' + data + d);
            }
        ");

            string ret = (string)await func(".NET");
            return ret;
        }


public Form4(string text)
        {
            InitializeComponent();

            MainAsync(text);
        }
        
        
        
                private async void MainAsync(string text)
        {
            string str = await Start();

            //string path = AppDomain.CurrentDomain.BaseDirectory + @"dist/index.html";
            String path = string.Format(@"{0}\dist\index.html", Application.StartupPath);

            //String path = "http://baidu.com";

            browser = new ChromiumWebBrowser(path);
            browser.JavascriptObjectRepository.Settings.LegacyBindingEnabled = true;

            this.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;

            //browser.GetBrowser().MainFrame.ExecuteJavaScriptAsync("document.dispatchEvent(new CustomEvent('event_name', { detail: { para: 'para' } }));");

            var setting = new CefSettings { RemoteDebuggingPort = 33229 };
            //CefSharp.Cef.Initialize(setting);

            await browser.WaitForInitialLoadAsync();

            //browser.GetBrowser().MainFrame.ExecuteJavaScriptAsync("document.dispatchEvent(new CustomEvent('event_name', { detail: { para: 'para' } }));");
            browser.GetBrowser().MainFrame.ExecuteJavaScriptAsync($"document.dispatchEvent(new CustomEvent('event_name', {{ detail: {{ para: '{text}' }} }}));");
            // // $ 里面的 { 要双写进行转义
            // {} 里面的会进行动态计算
        }

```





```
How to: use external Node.js modules
You can use external Node.js modules, for example modules installed from NPM.

Note: Most Node.js modules are written in JavaScript and will execute in Edge as-is. However, some Node.js external modules are native binary modules, rebuilt by NPM on module installation to suit your local execution environment. Native binary modules will not run in Edge unless they are rebuilt to link against the NodeJS dll that Edge uses.

To install modules from NPM, you must first install Node.js on your machine and use the npm package manager that comes with the Node.js installation. NPM modules must be installed in the directory where your build system places the Edge.js NuGet package (most likely the same location as the rest of your application binaries), or any ancestor directory. Alternatively, you can install NPM modules globally on the machine using npm install -g:

C:\projects\websockets> npm install ws
...
ws@0.4.31 node_modules\ws
├── tinycolor@0.0.1
├── options@0.0.5
├── nan@0.3.2
└── commander@0.6.1
You can then use the installed ws module to create a WebSocket server inside of a .NET application:

class Program
{
    public static async void Start()
    {
        var createWebSocketServer = Edge.Func(@"
            var WebSocketServer = require('ws').Server;

            return function (port, cb) {
                var wss = new WebSocketServer({ port: port });
                wss.on('connection', function (ws) {
                    ws.on('message', function (message) {
                        ws.send(message.toUpperCase());
                    });
                    ws.send('Hello!');
                });
                cb();
            };
        ");

        await createWebSocketServer(8080);
    }

    static void Main(string[] args)
    {
        Task.Run((Action)Start);
        new ManualResetEvent(false).WaitOne();
    }
}
```



```
# 命令行编译 sln
test>"C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\devenv.com" build\1.sln /Build

```



#### 去掉node 的黑窗

- https://zhuanlan.zhihu.com/p/573089992



```

node 工程 -> 调试 -> 命令行参数：
$(TargetDir)pmserver\\server.js

node 工程 -> 链接 -> 子系统  改成： 窗口 (/SUBSYSTEM:WINDOWS)

node_main.cc 加入

#include <string>
int WinMain(HINSTANCE hInstance,
            HINSTANCE hPrevInstance,
            LPSTR lpCmdLine,
            int nShowCmd) {

  int argc = 2;

  wchar_t* wargv[] = {
    L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
    (wchar_t*)lpCmdLine,
    //L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
    nullptr
  };

  //char** argv = new char*[argc + 1];

  //wchar_t *v1 =  // 这参数是没有用到的

  //wchar_t *v2 = L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js";  // 脚本路径


  //// 先算大小
  //DWORD size = WideCharToMultiByte(
  //    CP_UTF8, 0, v1, -1, nullptr, 0, nullptr, nullptr);
  //DWORD size2 = WideCharToMultiByte(
  //    CP_UTF8, 0, v2, -1, nullptr, 0, nullptr, nullptr);

  //// 再转 utf8
  //argv[0] = new char[size];
  //DWORD result = WideCharToMultiByte(
  //    CP_UTF8, 0, v1, -1, argv[0], size, nullptr, nullptr);
  //argv[1] = new char[size2];
  //DWORD result = WideCharToMultiByte(
  //    CP_UTF8, 0, v2, -1, argv[1], size2, nullptr, nullptr);


  wmain(argc, wargv);

  return 0;
}

```



##### nodejs 源码分析

> ```
> # D:\GitHub\node-14.21.1\lib\repl.js
> 	# REPLServer 内部可以直接执行代码
> 	function REPLServer
> 		  # 加在最后面执行成功
> 		  console.log(`here is self.eval(111)`)
>   			self.eval(`111`, self.context, getREPLResourceName(), function(e, ret) {
>     			console.log(e)
>     			console.log(ret)
>   			})
> 
> 	# 执行代码并回调在这里
>     const evalCmd = self[kBufferedCommandSymbol] + cmd + '\n';
> 		# evalCmd 是要执行的代码
>     console.log(`evalCmd is: ${evalCmd}`)
> 
>     debug('eval %j', evalCmd);console.log(`here is: self.eval(evalCmd, self.context, getREPLResourceName(), finish)`);
>     self.eval(evalCmd, self.context, getREPLResourceName(), finish);
> 
>     function finish(e, ret) {
>     	# ret 是代码执行返回的结果
> 
> 
> self.emit('line', self._line_buffer);
> 	# 发送消息，可以执行一行代码
> 
> 
> D:\GitHub\node-14.21.1\src\node_process_events.cc
> 	# C++ 如可给 js 发消息？
> 	MaybeLocal<Value> ProcessEmit(Environment* env,
>                               const char* event,
>                               Local<Value> message) {
> 
> 
> d:\github\node-14.21.1\lib\internal\bootstrap\node.js
> 	# 在 js 进程对象里面定义发送特定消息的方法 
> 	const { emitWarning } = require('internal/process/warning');
> 	process.emitWarning = emitWarning;
> 
> 
> Welcome to Node.js
> # 源码里面搜这个，就可以找到交互式执行代码的地方
> D:\GitHub\node-14.21.1\lib\internal\main\repl.js
> 
> readStdin
> # 源码里面搜这个，可以找到命令行输入代码回车并回调的过程
> D:\GitHub\node-14.21.1\lib\internal\process\execution.js
> 	function readStdin(callback) {
> 		process.stdin.setEncoding('utf8');
> 
> 		let code = '';
> 		process.stdin.on('data', (d) => {
>  		code += d;
> 		});
> 
> 		process.stdin.on('end', () => {
>  		callback(code);
> 		});
> 	}
> 
> 	D:\GitHub\node-14.21.1\lib\internal\main\eval_stdin.js
> 	
> 	readStdin((code) => {
> 
> 		process._eval = code;
> 
> 		const print = getOptionValue('--print');
> 		if (getOptionValue('--input-type') === 'module')
>  		evalModule(code, print);
> 		else
>  		evalScript('[stdin]',
>             code,
>             getOptionValue('--inspect-brk'),
>             print);
> 	});
> 
> 
> eval_stdin
> 	# 源码里面搜这个，可以找到命令行交互最开始的地方
> 
> 	D:\GitHub\node-14.21.1\src\node.cc
> 		StartExecution(Environment* env, StartExecutionCallback cb) {
> 			
> 			return StartExecution(env, "internal/main/eval_stdin");
> 			
> ```
>
> 

- https://github.com/nodejs/help/issues/3048  

  ```
  Can node::Environment (or NodeJS instances) run more than one script at a time
  
  #include <assert.h>
  #include <stdio.h>
  #include <execinfo.h>
  #include <signal.h>
  #include <stdlib.h>
  #include <unistd.h>
  #include <node.h>
  #include <uv.h>
  
  void segfault_handler(int sig) {
    void *array[10];
    size_t size;
    // get void*'s for all entries on the stack
    size = backtrace(array, 10);
    // print out all the frames to stderr
    fprintf(stderr, "Error: signal %d:\n", sig);
    backtrace_symbols_fd(array, size, STDERR_FILENO);
    exit(1);
  }
  
  std::unique_ptr<node::MultiIsolatePlatform> platform;
  std::unique_ptr<node::CommonEnvironmentSetup> setup;
  v8::Global<v8::Function> require;
  
  void run_javascript(node::MultiIsolatePlatform *platform, node::CommonEnvironmentSetup *setup, const char *code) {
    // obtain + lock isolate
    v8::Isolate* isolate= setup->isolate();
    node::Environment* node_env = setup->env();
    v8::Local<v8::Context> context = isolate->GetCurrentContext();
    v8::Locker locker(isolate);
    v8::Isolate::Scope isolateScope(isolate);
    v8::HandleScope handle_scope(isolate);
    v8::Context::Scope context_scope(setup->context());
    // require('vm').runInThisContext(code)
    v8::Local<v8::String> vm_string = v8::String::NewFromUtf8Literal(isolate, "vm");
    v8::Local<v8::Value> function_args[1];
    function_args[0] = vm_string;
    v8::Local<v8::Value> vm_value = require.Get(isolate)->Call(setup->context(), v8::Null(isolate), 1, function_args).ToLocalChecked();
    v8::Local<v8::Object> vm_object = vm_value.As<v8::Object>();
    v8::Local<v8::String> run_in_this_context_string = v8::String::NewFromUtf8Literal(isolate, "runInThisContext");
    v8::Local<v8::Function> run_in_this_context = vm_object->Get(setup->context(), run_in_this_context_string).ToLocalChecked().As<v8::Function>();
    v8::Local<v8::String> script_string = v8::String::NewFromUtf8(isolate, code, v8::NewStringType::kNormal).ToLocalChecked();
    function_args[0] = script_string;
    run_in_this_context->Call(setup->context(), v8::Null(isolate), 1, function_args);
  }
  
  int main(int argc, char *argv[]) {
    // segfault
    signal(SIGSEGV, segfault_handler);
    // args
    argv = uv_setup_args(argc, argv);
    std::vector<std::string> args(argv, argv + argc);
    std::vector<std::string> exec_args;
    std::vector<std::string> errors;
    // InitializeNodeWithArgs
    int ret_val = node::InitializeNodeWithArgs(&args, &exec_args, &errors);
    assert(ret_val == 0);
    // MultiIsolatePlatform::Create
    int thread_pool_size = 4;
    platform = node::MultiIsolatePlatform::Create(thread_pool_size);
    // InitializePlatform
    v8::V8::InitializePlatform(platform.get());
    v8::V8::Initialize();
    // CommonEnvironmentSetup::Create
    setup = node::CommonEnvironmentSetup::Create(platform.get(), &errors, args, exec_args);
    assert(setup);
    // set global require
    {
      // obtain + lock iolsate
      v8::Isolate* isolate= setup->isolate();
      node::Environment* node_env = setup->env();
      v8::Local<v8::Context> context = isolate->GetCurrentContext();
      v8::Locker locker(isolate);
      v8::Isolate::Scope isolateScope(isolate);
      v8::HandleScope handle_scope(isolate);
      v8::Context::Scope context_scope(setup->context());
      // node::LoadEnvironment
      v8::MaybeLocal<v8::Value> loadenv_ret = node::LoadEnvironment(
        node_env,
        [&](const node::StartExecutionCallbackInfo& info) -> v8::MaybeLocal<v8::Value> {
          require.Reset(isolate, info.native_require);
        }
      );
    }
    // run code
    {
      run_javascript(platform.get(), setup.get(), "console.log('hello world')");
      run_javascript(platform.get(), setup.get(), "console.log('hello world')");
    }
    // cleanup
    {
      node::Environment* node_env = setup->env();
      node::Stop(node_env);
    }
    // exit
    return 0;
  }
  
  ```

- https://juejin.cn/post/7065989551080570917  Node.js 源码分析 - 从 main 函数开始

- https://github.com/DavidCai1111/my-blog/issues/28

- https://github.com/yjhjstz/deep-into-node/blob/master/chapter2/chapter2-2.md

- https://developer.aliyun.com/article/592873

- https://juejin.cn/post/7068480351697371149  为Node.js创建一个自定义的REPL

- http://www.ayqy.net/blog/nodejs%E8%BF%9B%E7%A8%8B%E9%97%B4%E9%80%9A%E4%BF%A1/

  > **Nodejs进程间通信**  必看

- https://github.com/xtx1130/blog/issues/10 

  > **node_js2c的前世今生** 必看  
  >
  > - https://github.com/gatewayapps/kamino   clone github issue

- https://cloud.tencent.com/developer/article/1929213  在 Node.js 和 C++ 之间**使用 Buffer 共享数据**

- https://cnodejs.org/topic/60aff08e1de2d96635d5a9bc  Node.js的底层原理

  > ```
  > 首先Node.js会调用registerBuiltinModules函数注册C++模块，这个函数会调用一系列registerxxx的函数，我们发现在Node.js源码里找不到这些函数，因为这些函数会在各个C++模块中，通过宏定义实现的。宏展开后就是上图黄色框的内容，每个registerxxx函数的作用就是往C++模块的链表了插入一个节点，最后会形成一个链表。
  > 
  > 那么Node.js里是如何访问这些C++模块的呢？在Node.js中，是通过internalBinding访问C++模块的，internalBinding的逻辑很简单，就是根据模块名从模块队列中找到对应模块。但是这个函数只能在Node.js内部使用，不能在用户js模块使用。用户可以通过process.binding访问C++模块。
  > 
  > 注册完C++模块后就开始创建Environment对象，Environment是Node.js执行时的环境对象，类似一个全局变量的作用，他记录了Node.js在运行时的一些公共数据。创建完Environment后，Node.js会把该对象绑定到V8的Context中，为什么要这样做呢？主要是为了在V8的执行上下文里拿到env对象，因为V8中只有Isolate、Context这些对象。如果我们想在V8的执行环境中获取Environment对象的内容，就可以通过Context获取Environment对象。
  > 
  > ```

- https://blog.csdn.net/theanarkh/article/details/113870194 **nodejs的js调用c++以及c++调用libuv过程**

  > ```
  > 
  > ```
  >
  > 



#### mpv.net

- https://github.com/mpvnet-player/mpv.net



#### 日语翻译器

- https://github.com/hanmin0822/MisakaTranslator  翻译器



#### B站下载 

- DownKyi



### nodejs 调 C# dll

- https://github.com/dealenx/edge-js-example-dll

  

### eval 中使用await

- https://stackoverflow.com/questions/63030198/how-to-use-async-await-with-eval-function-in-javascript





## cpp

### C# 调用 c++



```
using System.Runtime.InteropServices;

namespace ConsoleApp2
{
    class Program
    {
        [DllImport("user32.dll", EntryPoint = "MessageBoxA")]
        public static extern int MsgBox(int hWnd, string msg, string caption, int type);

        static void Main(string[] args)
        {
            MsgBox(0, "C#调用DLL文件", "这是标题", 0x30);
        }
    }
}
```



```

 [DllImport(@"COM_DLL.dll", EntryPoint = "TOEC_ComRun", CharSet = CharSet.Ansi, ExactSpelling = false, CallingConvention = CallingConvention.Winapi)]
 public static extern int CPP_Run(CallBack cb);
 public delegate void CallBack(tagOutInfo data);
 private CallBack cb_f;
 CPP_Run(handle_sx, par, cb_f );
 public void Init(){
   cb_f=CallBack_Function;
 }
 public void CallBack_Function(tagOutInfo data)
 {   
 //.....回调函数体
 }

```



```
// header
extern "C" __declspec(dllexport) wchar_t* SysGetLibInfo(void);

// implementation
extern "C" __declspec(dllexport) wchar_t* SysGetLibInfo(void)
{
    return TEXT("Hello from unmanaged world!");
}


  [DllImport("NativeLibrary.dll", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.LPTStr)]
    static extern string SysGetLibInfo();
    
    
    
    extern "C" __declspec(dllexport) wchar_t* SysGetLibInfo(void)
{
    wchar_t* pStr = (wchar_t*)CoTaskMemAlloc(100);

    ZeroMemory(pStr, 100);

    wcscpy(pStr, TEXT("Hello from unmanaged world!"));

    return pStr;
}

then [return: MarshalAs(UnmanagedType.LPWStr)] will work too.

```



```
AddManyItems(string name, string[] items)
{
 unsafe 
 {
    // Iterate through the array items and marshal the strings to a IntPtr[]
    // Use Marshal.StringToHGlobalUni or similar here. 
    // Check https://github.com/mono/CppSharp/blob/main/src/Generator/Types/Std/Stdlib.CSharp.cs#L118
    IntPtr[] strings = items.Select((s) => Marshal.StringToHGlobalUni(s)).ToArray();
    char*[] ptrs = strings.Select((s) => (char*)s.ToPointer());
    fixed (char** arr = &ptrs)
    {
      __Internal.AddManyItems(name, arr);
    }
    // Call Marshal.FreeHGlobal on ptrs items
  }
}
```



```
static Encoding _encoding = RuntimeInformation.IsOSPlatform(OSPlatform.Linux) ? Encoding.UTF32 : Encoding.Default;

Using that, you can get the string length for marshalling back to managed code as such:

public static unsafe int WStringLength(byte* bytes, Encoding encoding)
        {
            byte[] zero = encoding.GetBytes(new char[] { '\0' });
            int sizeof_Char = zero.Length;
            int i = 0;
            while(true)
            {
                for(int j=0; j < zero.Length; j++) 
                {
                    if(bytes[i * sizeof_Char + j] != 0) 
                    {
                        break;
                    }
                    return i;
                }
                i++;
            }
        }

[...]
public unsafe string MarshalNativeToManaged(IntPtr input)
{
  return new string((sbyte*)input, 0, WStringHelper.WStringLength((byte*)input, _encoding) * sizeof_Char, _encoding);
}
```



#### 传指针

- https://gist.github.com/esskar/3779066

  ```
  // cpp
  #include <stdio.h>
  #include <Windows.h>
  
  struct Name
  {	
  	char FirstName[100];
  	char LastName[100];
  	char *Array[3];
  };
  
  extern "C" __declspec(dllexport) void __cdecl GetName(struct Name *name)
  {
  	strncpy_s(name->FirstName, "FirstName", sizeof(name->FirstName));
  	name->Array[0] = "Foo 0";
  	name->Array[1] = "Foo 1";
  	name->Array[2] = "Foo 2";
  }
  
  extern "C" __declspec(dllexport) void __cdecl Hello()
  {
  	printf("Hello\n");
  }
  
  
  // cs
  using System;
  using System.Runtime.InteropServices;
  
  namespace TestApp
  {
      class Program
      {
          [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
          public struct Name
          {
              [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 100)]
              public string FirstName;
              [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 100)]
              public string LastName;
              [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
              public string[] Array;
          };
  
          [DllImport("TestDll.dll")]
          public static extern void GetName(ref Name name);
  
          [DllImport("TestDll.dll")]
          public static extern void Hello();
  
          static void Main(string[] args)
          {
              Hello();
              var name = new Name();
              GetName(ref name);
              Console.WriteLine(name.FirstName);
              foreach (var s in name.Array)
                  Console.WriteLine(s);
          }
      }
  }
  
  ```

  

- https://blog.csdn.net/youqingyike/article/details/39253045



#### 传指针数组

- https://wurang.net/csharp_calling_c_dll_conversion_of_char/



#### 传结构体

- https://blog.51cto.com/u_15067227/4125021





# OS 兼容



```c#
# https://github.com/madelson/MedallionShell/blob/master/SampleCommand/PlatformCompatibilityTests.cs

public static readonly string DotNetPath = RuntimeInformation.IsOSPlatform(OSPlatform.Windows)
            ? @"C:\Program Files\dotnet\dotnet.exe"
            : "/usr/bin/dotnet";
            
```



# anime_Danganronpa_version1.cs



```

 systemctl stop firewalld
 pm2 resurrect  # pm2 save 后恢复
 
 dotnet publish -c Release -r linux-x64 # 在dangan 根目录运行

 cd /mnt/dangan/Server/bin/Release/net5.0/linux-x64

# 更新：现在需要vs studio 编译的版本才能外网了
 ./dangan.Server --urls http://0.0.0.0:80
	# 外网正常访问
```



```
dotnet publish -c Release -r win-x64 --self-contained true
```







```c#
using System;

using Medallion.Shell;
using Npgsql;
using NpgsqlTypes;
using MeCab;
using System.Text.RegularExpressions;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;

namespace dangan
{
    // /mnt/aspnetcore-runtime-5.0.10-linux-x64/dotnet publish/dangan.dll

    class Program
    {

        public static string unhana_remove(string s)
        {
            return Regex.Replace(s, @"[^\u3040-\u309F^\u30A0-\u30FF]", "");
        }

        public static string unchinese_remove(string s)
        {
            return Regex.Replace(s, @"[^\u4e00-\u9fa5]", "");
        }

        public static bool hasHanaQ(string s)
        {
            return unhana_remove(s).Length > 0;
        }

        public static Tuple<string, string> parseSrtTime(string time)
        {
            // time = "00:01:12,960 --> 00:01:14,640"
            string begin = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
            string end = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();

            begin = begin.Replace(',', '.');
            end = end.Replace(',', '.');

            return new Tuple<string, string>(begin, end);
        }

        public static string extractSRT(string ffmpegExe, string videopath, string frtname, string ecxutePath)
        {
            //string fname = @"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv";
            //string frtname = $"{ecxutePath}/out.srt";
            //var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            var ffmpegArgs = new List<string>() { "-y", "-loglevel", "error", "-i", videopath, "-map", "0:s:0", frtname };

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs); // 执行命令

            using (StreamWriter sw = File.AppendText(outlog)) // 写入日志
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            return strs;
        }
        public static Byte[] extractAudio(string ffmpegExe, string videopath, string begintime, string endtime)
        {
            //# Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
            //# -vn  no video
            //# out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
            //#   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
            //#   "tmp.mp3"])

            var ffmpegArgs = new List<string>() {
                "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3",
                "-ar", "44100", "-ac", "2", "-b:a", "192k",
                "tmp.mp3"
            };

            string ecxutePath = Environment.CurrentDirectory;

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs);

            using (StreamWriter sw = File.AppendText(outlog))
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            byte[] bts = null;

            using (FileStream stream = new FileStream("tmp.mp3", FileMode.Open, FileAccess.Read))
            using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
            {
                bts = reader.ReadBytes(Convert.ToInt32(stream.Length));
            }

            return bts;
        }

        public static void createAnimeDB(string host, string port)
        {
            using (var conn = new NpgsqlConnection($"Server={host};Port={port};Database=postgres;User Id=postgres;Password=echodict.com;"))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand("DROP DATABASE IF EXISTS anime;", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                using (var cmd = new NpgsqlCommand(@"CREATE DATABASE anime 
                        WITH OWNER = postgres 
                        ENCODING = 'UTF8' 
                        TABLESPACE = pg_default 
                        CONNECTION LIMIT = -1 
                        TEMPLATE template0; ", conn))
                {
                    cmd.ExecuteNonQuery();
                }



                conn.Close();

            }

            using (var conn = new NpgsqlConnection($"Server={host};Port={port};Database=anime;User Id=postgres;Password=echodict.com;"))
            {
                conn.Open();



                using (var cmd = new NpgsqlCommand("DROP TABLE IF EXISTS anime;", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                using (var cmd = new NpgsqlCommand(@"create table anime( 
                        id integer primary key generated always as identity, 
                        name text, 
                        jp text, 
                        zh text DEFAULT '', 
                        en text DEFAULT '', 
                        type text, 
                        time text, 
                        jp_mecab text, 
                        v_jp  tsvector, 
                        v_zh  tsvector, 
                        v_en  tsvector, 
                        videoname text, 
                        seasion text DEFAULT '', 
                        audio bytea, 
                        video bytea 
                    ); ", conn))
                {
                    cmd.ExecuteNonQuery();
                }


                using (var cmd = new NpgsqlCommand(@"CREATE extension pgroonga;
                        CREATE INDEX pgroonga_jp_index ON anime USING pgroonga(jp);
                        CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);
                        CREATE extension pg_jieba;
                        CREATE INDEX animename_index ON anime (name);
                        CREATE INDEX videoname_index ON anime (videoname);
                    ", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                // @禁止转义符内部用两个双引"" 表示单个双引，否则出现语法错误 
                using (var cmd = new NpgsqlCommand(@"
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab(""use_base_form"", true, ""include_reading"", true)')

        LOOP

            reading = (js-> 'metadata'->> 'reading');
                    IF reading IS NULL THEN
                            RETURN 0;
                    END IF;

                    END LOOP;
                    END LOOP;

                    RETURN 1;

                    END;
$func$ LANGUAGE plpgsql IMMUTABLE;
                    ", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                conn.Close();
            }
        }

        public static string mecab(string sentence)
        {
            string result = "";

            var parameter = new MeCabParam();
            var tagger = MeCabTagger.Create(parameter);

            foreach (var node in tagger.ParseToNodes(sentence))
            {
                if (node.CharType > 0)
                {
                    var features = node.Feature.Split(',');
                    var displayFeatures = string.Join(", ", features);

                    result += $"{node.Surface}\t{displayFeatures}\n";
                }
            }

            return result;
        }


        public static void allfiles(string targetDirectory, List<string> fnames )
        {
            // Process the list of files found in the directory.
            string[] fileEntries = Directory.GetFiles(targetDirectory);
            foreach (string fileName in fileEntries)
                fnames.Add(fileName);

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
            foreach (string subdirectory in subdirectoryEntries)
                allfiles(subdirectory, fnames);
        }



        public static void importAnime(string ffmpegExe, string animename, string seasion, string frtname, string videoname, string videopath)
        {
            List<string> chinese = new List<string>();
            List<Tuple<string, string>> japanese = new List<Tuple<string, string>>();

            Dictionary<string, string> dic_chs = new Dictionary<string, string>();

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            MatchCollection matches = Regex.Matches(strs, @"\n\d+\n");

            int count = matches.Count;

            for (int i = 0; i < count; i++)
            {
                var item = matches[i];

                int start = item.Index;
                int end = start + item.Length;
                int len = item.Length;

                string text = strs.Substring(start, len);  // 和item.Value 应该是一样的

                string content = "";

                if (i == count - 1)
                {
                    content = strs.Substring(end);
                }
                else
                {
                    int l = matches[i + 1].Index - end;
                    content = strs.Substring(end, l);
                }

                var arr = content.Trim().Split('\n');
                if (arr.Length < 2)
                {
                    continue;
                }

                var time = arr[0];
                content = arr[1];

                Regex r = new Regex("size=.+>(.+?)</font>");

                string subtitle = "";
                if (r.Match(content).Groups.Count > 0)
                {
                    subtitle = r.Match(content).Groups[1].Value;  // 0 永远是整个串，并不是捕获组。1 才是第一个组
                }
                else
                {
                    content = Regex.Replace(content, "face=\".+?\"", "");
                    content = Regex.Replace(content, "size=\"\\d+\"", "");
                    content = Regex.Replace(content, "color=\".+?\"", "");
                    content = Regex.Replace(content, "<font.+?>", "");
                    content = Regex.Replace(content, "{\\\\an7}", "");

                    subtitle = content;
                }

                subtitle = subtitle.Replace("<b>", "").Replace("</b>", "");

                if (hasHanaQ(subtitle)) // 有jia ming 的是jp
                {
                    japanese.Add(new Tuple<string, string>(subtitle, time));
                }
                else
                {
                    if (unchinese_remove(subtitle).Length > 0)
                    {
                        if (dic_chs.ContainsKey(time))
                        {
                            continue;
                        }

                        dic_chs[time] = subtitle;

                        string beginTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
                        string endTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();
                    }
                }
            }

            japanese = japanese.OrderBy(tu => tu.Item2).ToList<Tuple<string, string>>(); // sort by time asc

            var conn = new NpgsqlConnection("Server=209.141.34.77;Port=5432;Database=anime;User Id=postgres;Password=echodict.com;");
            conn.Open();

            int total = 0;

            foreach (var tu in japanese)
            {
                string j = tu.Item1;
                string zh = "";

                string t = tu.Item2;
                var (begintime, endtime) = parseSrtTime(t);

                if (dic_chs.ContainsKey(t))
                {
                    zh = dic_chs[t];
                }

                var bts = extractAudio(ffmpegExe, videopath, begintime, endtime);


                //string animename = "a";
                //string seasion = "b";
                string tags = mecab(j);
                //string videoname = Path.GetFileName(fname);

                string sql = $"insert into anime(name, seasion, jp, time, jp_mecab, zh, v_zh, videoname, audio, video) values('{animename}', '{seasion}','{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'), '{videoname}', @audio, @video);";

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    NpgsqlParameter paramAudio = cmd.CreateParameter();
                    paramAudio.ParameterName = "@audio";
                    paramAudio.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
                    paramAudio.Value = bts;
                    cmd.Parameters.Add(paramAudio);

                    NpgsqlParameter paramVideo = cmd.CreateParameter();
                    paramVideo.ParameterName = "@video";
                    paramVideo.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
                    paramVideo.Value = bts;
                    cmd.Parameters.Add(paramVideo);


                    cmd.ExecuteNonQuery();
                }

                total += 1;
                Console.WriteLine($"###### {total} / {japanese.Count}");

                break;
            }

            conn.Close();
        }


        public static void import()
        {
            /*

             python3.8

                out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
                out_text = out_bytes.decode('utf-8')

             windows cmd
                ffmpeg -y -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt

             MedallionShell

             */

            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录
            string path = new DirectoryInfo("../").FullName;  // 上级目录

            string OS = "";

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                OS = "Windows";
            } else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
            {
                OS = "OSX";
            } else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
            {
                OS = "Linux";
            } else
            {
                Console.WriteLine("##### ERROR:Unkonw OS Type!");
                return;
            }

            Console.WriteLine($"OS: {OS}");


            string host = "209.141.34.77";
            string port = "5432";

            createAnimeDB(host, port);


            var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            string realroot = @"F:\videos\anime";

            if (OS == "Linux")
            {
                realroot = @"/mnt/videos/anime";
                ffmpegExe = "/usr/bin/ffmpeg";
            }
            if (OS == "OSX")
            {
                realroot = @"/Users/olnymyself/Downloads/videos/anime";
            }

            List<string> fnames = new List<string>();


            allfiles(realroot, fnames);

            fnames = fnames.OrderBy(s => s).ToList();


            string dir = Directory.GetParent(fnames[0]).FullName;
            string dir2 = Directory.GetParent(dir).FullName;
            string dir3 = Directory.GetParent(dir2).FullName;
            string rootorigin = dir;  //# root origin
            string seasion = Path.GetFileName(dir2);
            string animename = Path.GetFileName(dir3);



            int cur = 0;

            foreach(var fname in fnames)
            {
                string videoname = Path.GetFileName(fname);
                string frtname = $"{ecxutePath}/out.srt";
                

                string srts = extractSRT(ffmpegExe, fname, frtname, ecxutePath);

                importAnime(ffmpegExe, animename, seasion, frtname, videoname, fname);

                cur = cur + 1;

                Console.WriteLine($"one task done.  {cur} / {fnames.Count}");

                break;
            }

        }

        static void Main(string[] args)
        {
            import();
        }
    }
}

```



```python

# ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p06_executing_external_command_and_get_its_output.html

import os,sys,subprocess
import re
import glob
import chardet
import MeCab
tagger = MeCab.Tagger()

import platform

def OSXQ():
    return platform.system() == 'Darwin'


"""
D:\GitHub\doc\lang\programming\postgresql summary.md
    docker exec -it centos7PG10 /bin/bash
        54322 port
    Install PG_Jieba [u](https://github.com/jaiminpan/pg_jieba)

pip install mecab-python3
pip install unidic-lite

pip install xmltodict
GFW
https://www.ishells.cn/archives/linux-ssr-server-client-install
"""


"""

SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
 --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}


CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("include_reading", true)')
  LOOP
    reading = (js -> 'metadata' ->> 'reading');

    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
  END LOOP;

  RETURN array_to_string(total, '');
END;
$func$ LANGUAGE plpgsql IMMUTABLE;


SELECT ja_reading ('有');
-- 

/*
{"{\"value\":\"海\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"ウミ\"}}"}
{"{\"value\":\"1\",\"position\":0,\"force_prefix_search\":false}"}
*/


{
  "force_prefix_search": false,
  "metadata": {
    "reading": "シ"
  },
  "position": 0,
  "value": "する"
}



SELECT string_to_array('xx~^~yy~^~zz', '~^~')
  --> {xx,yy,zz}


"""

"""

https://groonga.org/docs/reference/tokenizers/token_mecab.html

https://github.com/pgroonga/pgroonga/issues/171

My thought has become

CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);

CREATE INDEX idx_tatoeba_jpn ON dict.tatoeba
  USING pgroonga ("jpn")
  WITH (
    tokenizer='TokenMecab("use_base_form", true, "include_form", true, "include_reading", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );
CREATE INDEX idx_tatoeba_eng ON dict.tatoeba
  USING pgroonga ("eng")
  WITH (plugins='token_filters/stem', token_filters='TokenFilterStem');
Then

SELECT * FROM dict.tatoeba
WHERE jpn &@ 'うみ'
ORDER BY pgroonga_score(tableoid, ctid) DESC
LIMIT 10;
But it isn't comparable to 海.
"""

"""

&@ 单关键词的fulltext search

CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);



CREATE INDEX idx_tatoeba_jpn_base_form ON dict.tatoeba
  USING pgroonga ((jpn || ''))
  WITH (
    tokenizer='TokenMecab("use_base_form", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );

CREATE INDEX idx_tatoeba_jpn_reading ON dict.tatoeba
  USING pgroonga ((jpn || '' || ''))
  WITH (
    tokenizer='TokenMecab("use_reading", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );

SELECT * FROM dict.tatoeba
WHERE (jpn || '')       &@~ ja_expand('海') -- search by base_form
   OR (jpn || '' || '') &@~ ja_expand('海') -- search by reading
LIMIT 10;
"""

"""
CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);

CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("include_reading", true)')
  LOOP
    reading = (js -> 'metadata' ->> 'reading');

    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
  END LOOP;

  RETURN array_to_string(total, '');
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION ja_expand (TEXT) RETURNS TEXT AS
$func$
BEGIN
  IF $1 ~ '[\u4e00-\u9fa5]' THEN
    RETURN  $1||' OR '||ja_reading($1);
  END IF;

  RETURN $1;
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

SELECT * FROM dict.tatoeba
WHERE jpn &@~ ja_expand('海')
LIMIT 10;
"""


"""

CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
		LOOP
			reading = (js -> 'metadata' ->> 'reading');
			IF reading IS NULL THEN
					RETURN 0;
      END IF;
		
		END LOOP;
  END LOOP;
	
	RETURN 1;
	
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

"""


"""

自动重连

https://github.com/psycopg/psycopg2/blob/9e6c3322d8640bca7007a222973d87d8ea60057c/lib/pool.py#L103

status = conn.get_transaction_status()
                if status == _ext.TRANSACTION_STATUS_UNKNOWN:
                    # server connection lost
                    conn.close()
                elif status != _ext.TRANSACTION_STATUS_IDLE:
                    # connection in error or in transaction
                    conn.rollback()
                    self._pool.append(conn)
                else:
                    # regular idle connection
                    self._pool.append(conn)
"""


import psycopg2
import psycopg2.extensions as _ext
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#from psycopg2.extensions import ISOLATION_LEVEL_DEFAULT

import sqlite3 as sqlite # Python 自带的

from pymysql import escape_string
import glob

import json
import decimal
import datetime

import xmltodict



class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def writestring(fname, strs):
    with open(fname, "w", encoding="utf-8") as fp:
        fp.write(strs)
        fp.close()

# out_bytes = subprocess.check_output([r"ffmpeg", "-i", "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv", "-map", "0:s:0", "out.srt"])
# out_text = out_bytes.decode('utf-8')

# \u4e00-\u9fa5

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def chinese_remove(s):
    return re.sub(r"[\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def unjp_remove(s):
    return re.sub(r"[^\u0800-\u4e00]", "", s, flags=re.UNICODE)

def unhana_remove(s):
    return re.sub(r"[^\u3040-\u309F^\u30A0-\u30FF]", "", s, flags=re.UNICODE)

def hasHanaQ(s):
    return len( unhana_remove(s) ) > 0

def parseSrtTime(time):
  
  #time = "00:01:12,960 --> 00:01:14,640"
  begin = time.split('-->')[0].strip()
  end = time.split('-->')[1].strip()

  begin = begin.replace(',', '.')
  end = end.replace(',', '.')

  return begin, end

  # if match := re.compile(r'(\d\d):(\d\d):(\d\d),(\d\d\d)').search(begin):
  #   h1 = int(match.group(1))
  #   m1 = int(match.group(2))
  #   s1 = int(match.group(3))
  #   ms1 = int(match.group(4))

  #   totalMs1 = h1 * 3600 * 1000 + m1 * 60 * 1000 + s1 * 1000 + ms1

  #   if match := re.compile(r'(\d\d):(\d\d):(\d\d),(\d\d\d)').search(begin):
  #     h2 = int(match.group(1))
  #     m2 = int(match.group(2))
  #     s2 = int(match.group(3))
  #     ms2 = int(match.group(4))

  #     totalMs2 = h2 * 3600 * 1000 + m2 * 60 * 1000 + s2 * 1000 + ms2

  #     ms3 = totalMs1 - totalMs2  
  # print(h1)

def readImage(fname):

    fin = None

    try:
        fin = open(fname, "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        sys.exit(1)

    finally:

        if fin:
            fin.close()


"""
ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3
Explanation of the used arguments in this example:

-i - input file

-vn - Disable video, to make sure no video (including album cover image) is included if the source would be a video file

-ar - Set the audio sampling frequency. For output streams it is set by default to the frequency of the corresponding input stream. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options.

-ac - Set the number of audio channels. For output streams it is set by default to the number of input audio channels. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options. So used here to make sure it is stereo (2 channels)

-b:a - Converts the audio bitrate to be exact 192kbit per second

-hide_banner -loglevel error

"""
def extractAudio(videopath, begintime, endtime):
  # Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
  # -vn  no video
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.mp3"])
    
    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
      "-ar", "44100", "-ac", "2", "-b:a", "192k", \
        "tmp.mp3"])

    out_text = out_bytes.decode('utf-8')
    bts = readImage("tmp.mp3")
    os.remove("tmp.mp3")
    return bts
    
# success
# hevc 表示使用h.265 编码
# ffmpeg -y -ss 00:01:12.960 -to 00:01:14.640  -i t.mkv  -codec:v hevc -acodec mp3 -ar 44100 -ac 2 -b:a 192k t.ts
def extractVideo(videopath, begintime, endtime):
  # Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
  # -vn  no video
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.mp3"])
    
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-codec:v", "hevc",  "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.ts"])

    """
    # jsmpeg.js normal play
    ! ffmpeg -i t.mkv -y -ss 00:01:12.960 -to 00:01:14.640 -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=t.mkv t.ts
    """
    # out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-f", "mpegts", "-codec:v", "mpeg1video",  "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
    #   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
    #     "tmp.ts"])

    tmpmkv = "tmp.mkv"
    if ( os.path.exists(tmpmkv) ):
      os.unlink("tmp.mkv")
    os.symlink(videopath, "tmp.mkv")
    
    #cmd = f'ffmpeg -i \"{videopath}\" -y -ss {begintime} -to {endtime} -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=\"{videopath}\" tmp.ts' #% (videopath,videopath)#('t.mkv', 't.mkv')
    cmd = f'ffmpeg -i \"{videopath}\" -y -hide_banner -loglevel error -ss {begintime} -to {endtime} -f mpegts -codec:v mpeg1video -b:v 1500k -s 960x540 -r 30 -bf 0 -codec:a mp2 -ar 44100 -ac 2 -b:a 192k -vf subtitles=\"tmp.mkv\" tmp.ts' #% (videopath,videopath)#('t.mkv', 't.mkv')

    out_bytes = subprocess.check_output(cmd, shell=True)

    

    out_text = out_bytes.decode('utf-8')
    bts = readImage("tmp.ts")
    #os.remove("tmp.t")
    return bts


def allfname(root, ext):
    names = os.listdir(root)
    #names = list( filter(lambda s: ext in s,names) )
    
    # tmp = f'{root}/*.{ext}'
    # tmp = '/Users/olnymyself/Downloads/*.mkv'
    # tmp = "/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]/*.mkv"
    # names = glob.glob(tmp)
    names = list(map(lambda ns:os.path.basename(ns),names))
    #names.sort() # key = lambda x: int(x[:-4])

    # if os.path.exists( root ):
    #   p =  os.path.join( root, '*.mkv' )
    #   names = os.listdir(root) # glob.glob(p)
    #   a = 1    
    # path = r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"+ f'/*.mkv'
    # names = glob.glob(path)
    return names
  











# 有假名的是日语，没有pgroonga_tokenize 分出来没有读音的不是日语
# 没有读音的不是
# SELECT pgroonga_tokenize('并','tokenizer', 'TokenMecab("use_base_form", true,"include_reading", true)') # use_base_form 可能会把变形转成原形？
# SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true,"include_reading", true)')
  # --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}

def jpQ(s):
    return len( unhana_remove(s) ) > 0


def createAnimeDB(host, port):
    with psycopg2.connect(database='postgres', user='postgres', password='echodict.com',host=host, port=port) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS anime;")
            cur.execute("CREATE DATABASE anime \
                WITH OWNER = postgres \
                ENCODING = 'UTF8' \
                TABLESPACE = pg_default \
                CONNECTION LIMIT = -1 \
                TEMPLATE template0;")

    with psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port) as conn:
        with conn.cursor() as cur:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur.execute("DROP TABLE IF EXISTS anime;")
            #  id serial primary key, \
            cur.execute("create table anime( \
                id integer primary key generated always as identity, \
                name text, \
                jp text, \
                zh text DEFAULT '', \
                en text DEFAULT '', \
                type text, \
                time text, \
                jp_mecab text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector, \
                videoname text, \
                seasion text DEFAULT '', \
                audio bytea, \
                video bytea \
            );")
            #cur.execute("CREATE TABLE audio(id SERIAL PRIMARY KEY, data BYTEA);")

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            cur.execute("CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);")

            cur.execute("create extension pg_jieba;")

            cur.execute("CREATE INDEX animename_index ON anime (name);")
            cur.execute("CREATE INDEX videoname_index ON anime (videoname);")
            #cur.execute("create unique index audio_unique_hash_index on anime (md5(audio));")
            
            
            # cur.execute("create extension rum;") 
            # cur.execute("CREATE INDEX fts_rum_anime ON anime USING rum (v_jp rum_tsvector_ops);")

            # 加一个函数，只要有一个字没有读音就不是jp 
            cur.execute(
              """
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
		LOOP
			reading = (js -> 'metadata' ->> 'reading');
			IF reading IS NULL THEN
					RETURN 0;
      END IF;
		
		END LOOP;
  END LOOP;
	
	RETURN 1;
	
END;
$func$ LANGUAGE plpgsql IMMUTABLE;
              """
            )

def importAnime(animename, seasion, frtname, videoname, videopath):
    dic_chs = {}

    currDir = os.path.dirname(os.path.abspath(__file__))

    
    fsrt = os.path.join(currDir, frtname)
    strs = "\n"+readstring(fsrt)+"\n"
    iters = re.finditer(r"\n\d+\n", strs, re.DOTALL)
    poss = [ i.span() for i in iters ]


    #animename = 'Danganronpa'

    chinese = []
    jpanese = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        
        n = strs[start:end]

        content = None
        if i == ( len(poss) - 1 ):
            content = strs[ end : len(strs) ]
        else:
            content = strs[ end : poss[i+1][0] ]
        
        arr = content.strip().split('\n')
        if len(arr) < 2:
          continue
        time = content.strip().split('\n')[0]
        content = content.strip().split('\n')[1]



        

        if len( re.compile(r'size=.+>(.+?)\<\/font\>').findall(content) ) > 0:
          subtitle = re.compile(r'size=.+>(.+?)\<\/font\>').findall(content)[0]
        else:
          content = re.compile(r"""face=".+?\"""").sub('', content)
          content = re.compile(r"""size="\d+\"""").sub('', content)
          content = re.compile(r"""color=".+?\"""").sub('', content)
          content = re.compile(r"""<font.+?>""").sub('', content)
          content = re.compile(r"""{\\an7}""").sub('', content)
          
          subtitle = content

        # elif match := re.compile("""(<font face=".+?" size="\d+"><font size="\d+">).+?""").search(content):
        #   m = match.group(1)
        #   subtitle = content.replace(m, "")
        # elif match := re.compile(r"""(<font face=".+?" size="\d+"><font face=".+?">{\\an\d+}<font size="\d+">).+?""").search(content):
        #   m = match.group(1)
        #   subtitle = content.replace(m, "")
        # else:
        #   raise RuntimeError('some err')

        subtitle = subtitle.replace('<b>','').replace('</b>','')
        
        chrst = chardet.detect(subtitle.encode())

        
        if chrst['encoding'] == 'ascii' and chrst['confidence'] > 0.99:
            b = 1
        elif hasHanaQ(subtitle): # 有jia ming 的是jp
          jpanese.append( (subtitle, time) )
        else:
            tmp = unchinese_remove(subtitle)
            if tmp != "":
              
              if time in dic_chs:
                continue
                #raise RuntimeError('some err')
              
              dic_chs[time] = subtitle

              tmp = "|".join( list(tmp) )
              begin = time.split('-->')[0].strip()
              end = time.split('-->')[1].strip()
              allhasjpduyingQ = False


    jpanese = sorted(jpanese, key=lambda tu: tu[1], reverse=False)  # sort by time asc


              # with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port) as conn: 
              #   with conn.cursor() as cur:
              #     sql = f"select JPQ ('{tmp}');"
              #     cur.execute( sql )
              #     row = cur.fetchone()
              #     tt = row[0]
              #     if row[0] == 1:
              #       allhasjpduyingQ = True
              #     else:
              #       allhasjpduyingQ = False

              #chinese.append( (subtitle, time) )

    # writestring('jp.txt', "\r\n".join(jpanese[0]+jpanese[1]))
    # writestring('ch.txt', "\r\n".join(chinese[0]+chinese[1]))


    with psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port) as conn:
        #conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # 不自动开启事务？
        with conn.cursor() as cur:
          
            #cur.execute('BEGIN;')
            count = 0
            for idx, tu in enumerate(jpanese):

                status = conn.get_transaction_status()
                if status == _ext.TRANSACTION_STATUS_UNKNOWN:
                    # server connection lost
                    conn.close()
                    conn = psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port)
                    cur = conn.cursor()
                elif status != _ext.TRANSACTION_STATUS_IDLE:
                    # connection in error or in transaction
                    #conn.rollback()
                    #self._pool.append(conn)
                    pass
                else:
                    # regular idle connection
                    #self._pool.append(conn)
                    pass

                j = tu[0]
                zh = ""
                # if (idx < len(chinese)):
                #     zh = chinese[idx][0].replace("(", "`(`").replace(")", "`)`")
                tags = tagger.parse(j)
                #tags = tags.split('\n')
                t = tu[1]
                begintime, endtime = parseSrtTime(t)
                bts = extractAudio(videopath, begintime, endtime)
                #bts = b''
                bts = psycopg2.Binary(bts)
                #bts_video = extractVideo(videopath, begintime, endtime)
                bts_video = b''
                bts_video = psycopg2.Binary(bts_video)

                if (t in dic_chs):
                  zh = dic_chs[t].replace("(", "`(`").replace(")", "`)`").replace("'", "''")
                videoname = videoname.replace("(", "`(`").replace(")", "`)`").replace("'", "''")
                sql = f"""insert into anime(name, seasion, jp, time, jp_mecab, zh, v_zh, videoname, audio, video) values('{animename}', '{seasion}','{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'), '{videoname}', %s, %s);"""
                cur.execute( sql, (bts,bts_video,) )
                count += 1
                #if count % 10 == 0:
                print( f"###### {count} / {len(jpanese)}" )
                
                #if count >= 10:
                #  break
                # sql = f"""insert into anime(name, jp, time, jp_mecab, zh, v_zh, videoname) values('{animename}', '{j}', '{t}', '{tags}', '{zh}', '{videoname}', to_tsvector('jiebacfg', '{zh}'));"""
                #cur.execute( sql )

                #cur.execute("""INSERT INTO audio(data) VALUES(%s);""", (bts,))
                #break

            #cur.execute('COMMIT;')


    with psycopg2.connect(database='anime', user='postgres', password='echodict.com',host=host, port=port) as conn:
        with conn.cursor() as cur:
            #cur.execute("SELECT * FROM anime WHERE jp &@ '遅刻';")
            cur.execute("SELECT * FROM anime WHERE jp_mecab &@ 'チコク';")
            rows = cur.fetchall()
    
    # with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port=port) as conn:
    #     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #     with conn.cursor() as cur:
    #         cur.execute("DROP DATABASE IF EXISTS anime;")

    print("hi,,,")

if __name__ == "__main__":

    """
    pg_ctlcluster 13 main start       # echo pg

    docker exec -it centos7PG10 /bin/bash
    systemctl restart postgresql-13   # echo docker pg
    """

    print("start")

    OS = ''
    try:
      test = os.uname()
      if test[0] == "Linux":
        OS = "Linux"
      elif test[0] == 'Darwin':
        OS = "OSX"
    except Exception as e:
      OS = "Windows"


    print(f"OS: {OS}")

    #begin, end = parseSrtTime("00:01:12,960 --> 00:01:14,640")

    #host = '111.229.53.195'
    host = '209.141.34.77'
    port = 5432

    #createAnimeDB(host, port)






    realroot = r"F:\videos\anime"
    if OS == "Linux":
      realroot = r"/mnt/videos/anime"
    if OS == "OSX":
      root = r"/Users/olnymyself/Downloads/videos/anime"


    fnames2 = glob.glob(realroot + '/**/*.mkv', recursive=True)
    tmp = fnames2[0]
    dir = os.path.dirname(tmp)
    dir2 = os.path.dirname(dir)
    dir3 = os.path.dirname(dir2)
    rootorigin = dir  # root origin
    seasion = os.path.basename(dir2)
    animename = os.path.basename(dir3)

    
    root = rootorigin # r"F:\videos\anime\Danganronpa\S01\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]" # r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    # if OS == "Linux":
    #   root = r"/mnt/videos/anime/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    # if OS == "OSX":
    #   #root = r"/Users/olnymyself/Downloads/[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    #   root = r"/Users/olnymyself/Downloads/d"

    print( f"root path: \n{root}" )

    fnames = allfname(root, 'mkv')

    fnames = sorted(fnames, key=lambda s: s, reverse=False)  # sort by name

    cur = 0
    for fname in fnames:
      videoname = fname
      frtname = f"{fname}.srt"
      fname = os.path.join( root, fname )
      videopath = os.path.join( root, videoname )
      out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
      out_text = out_bytes.decode('utf-8')

      #animename = 'Danganronpa'
      #seasion = '01'
      importAnime(animename, seasion, frtname, videoname, videopath)

      cur = cur + 1

      print('one task done. ', cur, '/', len(fnames) )

      #break


    print("all task done.")

    """
    ここ
    とかい【都会】  トカイ
    """

```



# dangan



## anime.cs



```c#
using System;

using Medallion.Shell;
using Npgsql;
using NpgsqlTypes;
using MeCab;
using System.Text.RegularExpressions;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using OpenCCNET;
using Kawazu;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

/*
 
 dotnet publish -c Release -r linux-x64 # 在dangan 根目录运行

 cd /mnt/dangan/Server/bin/Release/net5.0/linux-x64

 ./dangan.Server --urls http://0.0.0.0:5000
	# 外网正常访问
 
 */

namespace dangan
{
    public class anime
    {

        public static bool initQ = false;

        public static NpgsqlConnection g_conn = null;


        public static void initConn()
        {
            /*
             
            1. Increase max_connection and shared_buffers

in /var/lib/pgsql/{version_number}/data/postgresql.conf

change

 max_connections = 100
shared_buffers = 24MB
to

 max_connections = 1000
shared_buffers = 240MB
The shared_buffers configuration parameter determines how much memory is dedicated to PostgreSQL to use for caching data.

If you have a system with 1GB or more of RAM, a reasonable starting value for shared_buffers is 1/4 of the memory in your system.it's unlikely you'll find using more than 40% of RAM to work better than a smaller amount (like 25%)Be aware that if your system or PostgreSQL build is 32-bit, it might not be practical to set shared_buffers above 2 ~ 2.5GB.Note that on Windows, large values for shared_buffers aren't as effective, and you may find better results keeping it relatively low and using the OS cache more instead. On Windows, the useful range is 64MB to 512MB.
2. Change kernel.shmmax

You would need to increase kernel max segment size to be slightly larger than the shared_buffers.

In file /etc/sysctl.conf set the parameter as shown below. It will take effect when PostgreSQL reboots (The following line makes the kernel max to 96Mb)

 kernel.shmmax=100663296
But I want you to know that increase it may not resolve issues for you if your traffic is large. You need to check all your code and sure that you no connect to DB in a LOOP.
             
             */

            // https://www.npgsql.org/doc/connection-string-parameters.html
            g_conn = new NpgsqlConnection("Server=209.141.34.77;Port=5432;Database=anime;User Id=postgres;Password=echodict.com;Minimum Pool Size=10;Maximum Pool Size=20;Connection Idle Lifetime=200;Tcp Keepalive = false;");
            //g_conn.Open();
            System.GC.SuppressFinalize(g_conn);
            initQ = true;
        }

        public static string unhana_remove(string s)
        {
            return Regex.Replace(s, @"[^\u3040-\u309F^\u30A0-\u30FF]", "");
        }

        public static string unchinese_remove(string s)
        {
            return Regex.Replace(s, @"[^\u4e00-\u9fa5]", "");
        }

        public static string chinese_remove(string s)
        {
            return Regex.Replace(s, @"[\u4e00-\u9fa5]", "");
        }

        public static bool hasHanaQ(string s)
        {
            return unhana_remove(s).Length > 0;
        }

        public static bool jpQ(string s)
        {
            return unhana_remove(s).Length > 0;
        }

        public static bool chQ(string s)
        {
            return !jpQ(s) && chinese_remove(s).Length == 0;
        }

        public static Tuple<string, string> parseSrtTime(string time)
        {
            // time = "00:01:12,960 --> 00:01:14,640"
            string begin = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
            string end = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();

            begin = begin.Replace(',', '.');
            end = end.Replace(',', '.');

            return new Tuple<string, string>(begin, end);
        }

        public static string extractSRT(string ffmpegExe, string videopath, string frtname, string ecxutePath)
        {
            //string fname = @"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv";
            //string frtname = $"{ecxutePath}/out.srt";
            //var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            var ffmpegArgs = new List<string>() { "-y", "-loglevel", "error", "-i", videopath, "-map", "0:s:0", frtname };

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs); // 执行命令

            using (StreamWriter sw = File.AppendText(outlog)) // 写入日志
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            return strs;
        }
        public static Byte[] extractAudio(string ffmpegExe, string videopath, string begintime, string endtime)
        {
            //# Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
            //# -vn  no video
            //# out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
            //#   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
            //#   "tmp.mp3"])

            var ffmpegArgs = new List<string>() {
                "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3",
                "-ar", "44100", "-ac", "2", "-b:a", "192k",
                "tmp.mp3"
            };

            string ecxutePath = Environment.CurrentDirectory;

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs);

            using (StreamWriter sw = File.AppendText(outlog))
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            byte[] bts = null;

            using (FileStream stream = new FileStream("tmp.mp3", FileMode.Open, FileAccess.Read))
            using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
            {
                bts = reader.ReadBytes(Convert.ToInt32(stream.Length));
            }

            return bts;
        }

        public static void createAnimeDB(string host, string port)
        {
            using (var conn = new NpgsqlConnection($"Server={host};Port={port};Database=postgres;User Id=postgres;Password=echodict.com;"))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand("DROP DATABASE IF EXISTS anime;", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                using (var cmd = new NpgsqlCommand(@"CREATE DATABASE anime 
                        WITH OWNER = postgres 
                        ENCODING = 'UTF8' 
                        TABLESPACE = pg_default 
                        CONNECTION LIMIT = -1 
                        TEMPLATE template0; ", conn))
                {
                    cmd.ExecuteNonQuery();
                }



                conn.Close();

            }

            using (var conn = new NpgsqlConnection($"Server={host};Port={port};Database=anime;User Id=postgres;Password=echodict.com;"))
            {
                conn.Open();



                using (var cmd = new NpgsqlCommand("DROP TABLE IF EXISTS anime;", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                using (var cmd = new NpgsqlCommand(@"create table anime( 
                        id integer primary key generated always as identity, 
                        name text, 
                        jp text, 
                        zh text DEFAULT '', 
                        en text DEFAULT '', 
                        type text, 
                        time text, 
                        jp_mecab text, 
                        v_jp  tsvector, 
                        v_zh  tsvector, 
                        v_en  tsvector, 
                        videoname text, 
                        seasion text DEFAULT '', 
                        audio bytea, 
                        video bytea 
                    ); ", conn))
                {
                    cmd.ExecuteNonQuery();
                }


                using (var cmd = new NpgsqlCommand(@"CREATE extension pgroonga;
                        CREATE INDEX pgroonga_jp_index ON anime USING pgroonga(jp);
                        CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);
                        CREATE extension pg_jieba;
                        CREATE INDEX animename_index ON anime (name);
                        CREATE INDEX videoname_index ON anime (videoname);
                    ", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                // @禁止转义符内部用两个双引"" 表示单个双引，否则出现语法错误 
                using (var cmd = new NpgsqlCommand(@"
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab(""use_base_form"", true, ""include_reading"", true)')

        LOOP

            reading = (js-> 'metadata'->> 'reading');
                    IF reading IS NULL THEN
                            RETURN 0;
                    END IF;

                    END LOOP;
                    END LOOP;

                    RETURN 1;

                    END;
$func$ LANGUAGE plpgsql IMMUTABLE;
                    ", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                conn.Close();
            }
        }

        public static string mecab(string sentence)
        {
            string result = "";

            var parameter = new MeCabParam();
            var tagger = MeCabTagger.Create(parameter);

            foreach (var node in tagger.ParseToNodes(sentence))
            {
                if (node.CharType > 0)
                {
                    var features = node.Feature.Split(',');
                    var displayFeatures = string.Join(", ", features);

                    result += $"{node.Surface}\t{displayFeatures}\n";
                }
            }

            return result;
        }


        public static void allfiles(string targetDirectory, List<string> fnames)
        {
            // Process the list of files found in the directory.
            string[] fileEntries = Directory.GetFiles(targetDirectory);
            foreach (string fileName in fileEntries)
                fnames.Add(fileName);

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
            foreach (string subdirectory in subdirectoryEntries)
                allfiles(subdirectory, fnames);
        }



        public static void importAnime(string ffmpegExe, string animename, string seasion, string frtname, string videoname, string videopath)
        {
            List<string> chinese = new List<string>();
            List<Tuple<string, string>> japanese = new List<Tuple<string, string>>();

            Dictionary<string, string> dic_chs = new Dictionary<string, string>();

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            MatchCollection matches = Regex.Matches(strs, @"\n\d+\n");

            int count = matches.Count;

            for (int i = 0; i < count; i++)
            {
                var item = matches[i];

                int start = item.Index;
                int end = start + item.Length;
                int len = item.Length;

                string text = strs.Substring(start, len);  // 和item.Value 应该是一样的

                string content = "";

                if (i == count - 1)
                {
                    content = strs.Substring(end);
                }
                else
                {
                    int l = matches[i + 1].Index - end;
                    content = strs.Substring(end, l);
                }

                var arr = content.Trim().Split('\n');
                if (arr.Length < 2)
                {
                    continue;
                }

                var time = arr[0];
                content = arr[1];

                Regex r = new Regex("size=.+>(.+?)</font>");

                string subtitle = "";
                if (r.Match(content).Groups.Count > 0)
                {
                    subtitle = r.Match(content).Groups[1].Value;  // 0 永远是整个串，并不是捕获组。1 才是第一个组
                }
                else
                {
                    content = Regex.Replace(content, "face=\".+?\"", "");
                    content = Regex.Replace(content, "size=\"\\d+\"", "");
                    content = Regex.Replace(content, "color=\".+?\"", "");
                    content = Regex.Replace(content, "<font.+?>", "");
                    content = Regex.Replace(content, "{\\\\an7}", "");

                    subtitle = content;
                }

                subtitle = subtitle.Replace("<b>", "").Replace("</b>", "");

                if (hasHanaQ(subtitle)) // 有jia ming 的是jp
                {
                    japanese.Add(new Tuple<string, string>(subtitle, time));
                }
                else
                {
                    if (unchinese_remove(subtitle).Length > 0)
                    {
                        if (dic_chs.ContainsKey(time))
                        {
                            continue;
                        }

                        dic_chs[time] = subtitle;

                        string beginTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
                        string endTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();
                    }
                }
            }

            japanese = japanese.OrderBy(tu => tu.Item2).ToList<Tuple<string, string>>(); // sort by time asc

            var conn = new NpgsqlConnection("Server=209.141.34.77;Port=5432;Database=anime;User Id=postgres;Password=echodict.com;");
            conn.Open();

            int total = 0;

            foreach (var tu in japanese)
            {
                string j = tu.Item1;
                string zh = "";

                string t = tu.Item2;
                var (begintime, endtime) = parseSrtTime(t);

                if (dic_chs.ContainsKey(t))
                {
                    zh = dic_chs[t];
                }

                var bts = extractAudio(ffmpegExe, videopath, begintime, endtime);


                //string animename = "a";
                //string seasion = "b";
                string tags = mecab(j);
                //string videoname = Path.GetFileName(fname);

                string sql = $"insert into anime(name, seasion, jp, time, jp_mecab, zh, v_zh, videoname, audio, video) values('{animename}', '{seasion}','{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'), '{videoname}', @audio, @video);";

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    NpgsqlParameter paramAudio = cmd.CreateParameter();
                    paramAudio.ParameterName = "@audio";
                    paramAudio.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
                    paramAudio.Value = bts;
                    cmd.Parameters.Add(paramAudio);

                    NpgsqlParameter paramVideo = cmd.CreateParameter();
                    paramVideo.ParameterName = "@video";
                    paramVideo.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
                    paramVideo.Value = bts;
                    cmd.Parameters.Add(paramVideo);


                    cmd.ExecuteNonQuery();
                }

                total += 1;
                Console.WriteLine($"###### {total} / {japanese.Count}");

                //break;
            }

            conn.Close();
        }


        public static Action import = () =>
        {
            /*

             python3.8

                out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
                out_text = out_bytes.decode('utf-8')

             windows cmd
                ffmpeg -y -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt

             MedallionShell

             */

            // CommandTimeout=0;
            //NpgsqlConnection conn_pool = 


            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录
            string path = new DirectoryInfo("../").FullName;  // 上级目录

            string OS = "";

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                OS = "Windows";
            }
            else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
            {
                OS = "OSX";
            }
            else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
            {
                OS = "Linux";
            }
            else
            {
                Console.WriteLine("##### ERROR:Unkonw OS Type!");
                return;
            }

            Console.WriteLine($"OS: {OS}");


            string host = "209.141.34.77";
            string port = "5432";

            createAnimeDB(host, port);


            var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            string realroot = @"F:\videos\anime";

            if (OS == "Linux")
            {
                realroot = @"/mnt/videos/anime";
                ffmpegExe = "/usr/bin/ffmpeg";
            }
            if (OS == "OSX")
            {
                realroot = @"/Users/olnymyself/Downloads/videos/anime";
            }

            List<string> fnames = new List<string>();


            allfiles(realroot, fnames);

            fnames = fnames.OrderBy(s => s).ToList();


            string dir = Directory.GetParent(fnames[0]).FullName;
            string dir2 = Directory.GetParent(dir).FullName;
            string dir3 = Directory.GetParent(dir2).FullName;
            string rootorigin = dir;  //# root origin
            string seasion = Path.GetFileName(dir2);
            string animename = Path.GetFileName(dir3);



            int cur = 0;

            foreach (var fname in fnames)
            {
                string videoname = Path.GetFileName(fname);
                string frtname = $"{ecxutePath}/out.srt";


                string srts = extractSRT(ffmpegExe, fname, frtname, ecxutePath);

                importAnime(ffmpegExe, animename, seasion, frtname, videoname, fname);

                cur = cur + 1;

                Console.WriteLine($"one task done.  {cur} / {fnames.Count}");

                //break;
            }

        };

        public async static Task<List<Dictionary<string, string>>> search(string keywd)
        {


            bool isEn = false;
            bool isCh = false;
            bool isJp = false;

            //keyword = ZhConverter.HansToHant(keyword);  // chs to cht  

            if (chQ(keywd))
            {
                Console.WriteLine("### ch.");
                //keywd = ZhConverter.HansToHant(keywd);  // chs to cht // https://github.com/CosineG/OpenCC.NET
                isCh = true;
            }
            else if (jpQ(keywd))
            {
                Console.WriteLine("### jp.");
                isJp = true;
            }
            else
            {
                Console.WriteLine("### en.");
                isEn = true;
            }

            //var jaconv = new KawazuConverter();

            //JArray ret = new JArray();

            List<Dictionary<string, string>> ret = new List<Dictionary<string, string>>();

            string sql = "";

            if (isJp)
            {
                if (unhana_remove(keywd).Length == keywd.Length)
                {
                    //var converter = new KawazuConverter(); // https://github.com/Cutano/Kawazu
                    //keywd = await converter.Convert(keywd, To.Katakana, Mode.Normal, RomajiSystem.Hepburn, "(", ")");
                }

                sql = $"SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ '{keywd}' ORDER BY RANDOM() limit 3;";

            }
            else if (isCh)
            {
                sql = $"SELECT id, jp, zh, time FROM anime WHERE v_zh @@  to_tsquery('jiebacfg', '{keywd}') ORDER BY RANDOM() limit 3;";
            }


            if (sql != "")
            {

                using (var conn = new NpgsqlConnection("Server=xxxxx;Port=5432;Database=anime;User Id=postgres;Password=xxxxxx;Minimum Pool Size=10;Maximum Pool Size=20;Connection Idle Lifetime=200;Tcp Keepalive = false;"))
                {
                    conn.Open();

                    using (var cmd = new NpgsqlCommand(sql, conn))
                    {
                        NpgsqlDataReader reader = await cmd.ExecuteReaderAsync();
                        if (reader.HasRows)
                        {
                            while (reader.Read())
                            {
                                string id = reader["id"].ToString();
                                string jp = reader["jp"].ToString();
                                string zh = reader["zh"].ToString();
                                string time = reader["time"].ToString();

                                var d = new Dictionary<string, string> { { "id", id }, { "jp", jp }, { "zh", zh }, { "time", time } };

                                ret.Add(d);

                                //JObject jo = new JObject { { "id", id }, { "jp", jp }, { "zh", zh }, { "time", time } };
                            }
                        }
                    }
                }

            }

            return ret;
        }

    }
}

```



## searchController.cs



```csharp
using dangan.Shared;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Npgsql;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace dangan.Server.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class searchController : ControllerBase
    {

        public static bool initQ = false; 

        //private static readonly string[] Summaries = new[]
        //{
        //    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        //};

        //private readonly ILogger<searchController> _logger;

        //public searchController(ILogger<searchController> logger)
        //{
        //    _logger = logger;
        //}


        // http://localhost:5000/search?clear=1 重新导入数据

        [HttpGet]
        public string Get()
        {
            if (!initQ)
            {
                Console.WriteLine("##### Attention！！！！！Hit Get Method, And Not init yet.");

                //int fc = Request.Form.Count;
                var querys = Request.Query.Keys.ToList();

                if ( Request.Query.ContainsKey("clear"))
                {
                    Console.WriteLine("##### importting ...");

                    Task.Run(anime.import);
                }

                //if (!)
                //{

                //}

            }

            return "";

            //var rng = new Random();
            //return Enumerable.Range(1, 5).Select(index => new WeatherForecast
            //{
            //    Date = DateTime.Now.AddDays(index),
            //    TemperatureC = rng.Next(-20, 55),
            //    Summary = Summaries[rng.Next(Summaries.Length)]
            //})
            //.ToArray();
        }

        [HttpPost]
        public async Task<JsonResult> Post()
        {

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            if (!Request.Form.ContainsKey("keyword") || !Request.Form.ContainsKey("lang_select"))
            {
                return new JsonResult(new
                {
                    status = 201,
                    msg = "Form args not correct.",
                    data = new JArray()
                });
            }

            string prms = $" {{ \"keyword\" : \"{Request.Form["keyword"]}\", \"lang_select\": \"{Request.Form["lang_select"]}\" }} ";  // $ 里面的 { 要双写进行转义

            string keyword = "";
            string lang_select = "";

            Dictionary<string, string> prmsJson = null;
            if (prms == null || prms == "")
            {
                return new JsonResult(new
                {
                    status = 201,
                    msg = "参数为空",
                    data = new JArray()
                });
            }
            else
            {
                try
                {
                    prmsJson = JsonConvert.DeserializeObject<Dictionary<string, string>>(prms);
                    keyword = prmsJson["keyword"];
                    lang_select = prmsJson["lang_select"];

                    if (keyword == "")
                    {
                        return new JsonResult(new
                        {
                            status = 201,
                            msg = "参数为空",
                            data = new JArray()
                        });
                    }
                }
                catch (Exception)
                {
                    return new JsonResult(new
                    {
                        status = 201,
                        msg = "参数json 解析错误",
                        data = new JArray()
                    });
                }
            }



            var ret = await anime.search(keyword);

            return new JsonResult(new { status = 200, msg = "success.", data = ret });
        }


        [HttpGet("getaudio")]
        public async Task<IActionResult> getaudio()
        {
            string id = "1";

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录

            string dir_audio = Path.Combine(ecxutePath, "audio");

            if ( !Directory.Exists(dir_audio) )
            {
                Directory.CreateDirectory(dir_audio);
            }

            if (Request.Query.ContainsKey("id"))
            {
                id = Request.Query["id"].ToString();
            }

            string audioPath = Path.Combine(dir_audio, id + ".mp3");

            if (!System.IO.File.Exists(audioPath))
            {

                using (var conn = new NpgsqlConnection("Server=xxx;Port=5432;Database=anime;User Id=postgres;Password=xxxx;Minimum Pool Size=10;Maximum Pool Size=20;Connection Idle Lifetime=200;Tcp Keepalive = false;"))
                {

                    conn.Open();

                    string sql = $"SELECT id, audio FROM anime WHERE id={id};";

                    //using (var cmd = new NpgsqlCommand(sql, conn))
                    using (var cmd = new NpgsqlCommand(sql, conn))
                    {
                        NpgsqlDataReader reader = await cmd.ExecuteReaderAsync();
                        if (reader.HasRows)
                        {
                            while (reader.Read())
                            {
                                string idd = reader["id"].ToString();
                                byte[] audio = (byte[])reader["audio"];

                                try
                                {
                                    System.IO.File.WriteAllBytes(audioPath, audio);
                                }
                                catch (Exception ex)
                                {
                                    Console.WriteLine("### ERROR: 写入audio 失败. " + ex.Message);
                                    throw new Exception(ex.Message);
                                }

                            }
                        }
                    }
                }

            }

            var memory = new MemoryStream();
            using (var stream = new FileStream(audioPath, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                await stream.CopyToAsync(memory);
            }
            memory.Position = 0;

            return File(memory, "audio/mpeg", $"{id}.mp3");

        }

    }
}

```



## Search.razor



```c#
@page "/search"

@using dangan.Client.Model;
@using System.Text.Json;

@namespace dangan.Client
@inherits AntDesign.AntDomComponentBase


@inject NavigationManager NavigationManager
@inject Blazored.SessionStorage.ISessionStorageService sessionStorage
@*<form action="/search" method="post">
        keyword: <input type="text" name="keyword">  <button type="submit">Search</button> <br>
        <select name="lang_select">
            <option value="en">en</option>
            <option value="jp">jp</option>
        </select>

    </form>*@

<title>Welcome!</title>

<div>


    <audio id="audio" preload="auto" src="01.mp3"></audio>

    <EditForm Model="@model" OnValidSubmit="@HandleSubmit">
        <DataAnnotationsValidator />
        <ValidationSummary />

        keyword:<InputText id="keyowrdInput" @bind-Value="model.keyword" />

        <button type="submit">Submit</button> <br>

        <select name="lang_select">
            <option value="en">en</option>
            <option value="jp">jp</option>
        </select>
    </EditForm>


    @if (rowData != null)
    {

        @foreach (var row in rowData)
        {
            string url = debugQ ? $"http://{hostDebug}:5000/search/getaudio?id={row.id}" : $"http://{hostLV}:80/search/getaudio?id={row.id}";

            //<audio id="@($"audio{row.id}")" src="01.mp3" type="audio/mpeg" preload="auto"></audio>
            <audio id="@($"audio{row.id}")" src="@($"{url}")" type="audio/mpeg" preload="auto"></audio>
            <br>
            <br>
            @row.jp <img id="@($"img{row.id}")" src="images/play.gif" alt="play" @onclick="@(() => HandlePlayAudio($"{row.id}"))" style=" cursor: pointer">
            <br>
            @row.zh


        }

        <br>
        @*<AntDesign.Button Type="primary" Shape="circle" Icon="@PlayPauseIcon" Size="large" OnClick="OnPlayPause" />*@

        <br>
        <br>
        <button @onclick="@HandleSubmit">next</button>
        <br>
    }

</div>

@*@if (debugQ)
    {
        HandleSubmit();
    }*@

@*
    https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/
        https://github.com/kevin-montrose/Jil
    https://www.0daydown.com/04/1611202.html
    https://docs.microsoft.com/en-us/aspnet/core/blazor/forms-validation?view=aspnetcore-5.0


    https://jonhilton.net/blazor-markdown-editor/

*@


@code {

    private static readonly HttpClient client = new HttpClient();

    private static List<rowModel> rowData = null;

    bool debugQ = true;

    string hostDebug = "localhost";
    string hostHK = "35.241.67.141";
    string hostLV = "209.141.34.77";

    //string host = "209.141.34.77";
    //string host = "35.241.67.141";

    KeywordModel model = new KeywordModel();


    private async void HandleSubmit()
    {
        if (debugQ)
        {
            model.keyword = "ここ"; // それぞれ  房间
                                  //model.keyword = "房间";
        }

        string keyword = model.keyword;

        //发送Post请求
        var values = new Dictionary<string, string>
        {
            { "keyword", keyword },
            { "lang_select", "b" }
        };

        var content = new FormUrlEncodedContent(values);
        string url = debugQ ? $"http://{hostDebug}:5000/search" : $"http://{hostLV}:80/search";

        Console.WriteLine($"### Post URL: {url}");

        var response = await client.PostAsync(url, content);
        var responseString = await response.Content.ReadAsStringAsync();

        var json = JsonDocument.Parse(responseString);

        JsonElement root = json.RootElement;

        var status = root.GetProperty("status").ToString();

        if (status == "200")
        {
            var data = root.GetProperty("data").ToString();

            var ls = JsonSerializer.Deserialize<List<rowModel>>(data);

            rowData = ls;

            await sessionStorage.SetItemAsync("keyword", keyword);
            await sessionStorage.SetItemAsync("lang_select", values["lang_select"]);
            var keyword_from_section = await sessionStorage.GetItemAsync<string>("keyword");

            Refresh();

        }


    }

    private async void HandlePlayAudio(string id)
    {
        Console.WriteLine("### HandlePlayAudio hitting..." + id);

        //playaudio(imgid)

        await JsInvokeAsync("playaudio", id);

        //Refresh();

    }



    void MethodToTriggerUrl()
    {
        NavigationManager.NavigateTo("/");
    }

    //public void Refresh()
    //{
    //    // Update the UI
    //    InvokeAsync(() =>
    //    {
    //        StateHasChanged();
    //    });
    //}
}

```



## Index.razor



```c#
@page "/"

@inherits AntDesign.AntDomComponentBase

@inject NavigationManager NavigationManager

@code {

    protected override Task OnFirstAfterRenderAsync()
    {
        NavigationManager.NavigateTo("/search");

        return base.OnFirstAfterRenderAsync();
    }
}

```



### markdig

```
@page "/editor"
@using Markdig;

<div class="row">
    <div class="col-6">
        <textarea class="form-control" @bind-value="Body" @bind-value:event="oninput"></textarea>
    </div>
    <div class="col-6">
        @if (!string.IsNullOrWhiteSpace(Body))
        {
            @((MarkupString)Preview)
        }
    </div>
</div>

@code {
    public string Body { get; set; }

    //public string Preview => Markdown.ToHtml(Body);
    public string Preview => Markdown.ToHtml(Body, new MarkdownPipelineBuilder().UseAdvancedExtensions().Build());
}
```









# Postgresql



HeidiSQL 、Navicat Premium



```
# https://www.connectionstrings.com/npgsql/
	# 连接串
```



```

# https://github.com/npgsql/npgsql/issues/3829

using the below SQL to find the running sql

SELECT pid, age(clock_timestamp(), query_start), usename, query,state,* FROM pg_stat_activity WHERE --state = 'idle' AND query NOT ILIKE '%pg_stat_activity%' and usename='autovhcowner' and application_name='nelson_console' ORDER BY query_start desc;

this is how we are testing, but we are struggling to recreate at the moment, but we did notice this difference.

 public static void MyThread()
        {
            //int index = 0;
            Console.WriteLine($"{DateTime.Now} - program started ");
            Console.ReadKey();
            for (int i = 0; i < 5; i++)
            {
                //index++;
                Console.WriteLine($"{DateTime.Now} - thread created  {i}");

                Thread t = new Thread(ConnectionCheck);
                t.Start(i);

            }
            Console.WriteLine($"{DateTime.Now} - program finished ");
            Console.ReadKey();
        }
        public static void ConnectionCheck(object index)
        {
            try
            {
              
                Thread.Sleep(5000);
                Console.WriteLine($"{DateTime.Now} ConnectionCheck thread {index} ");
                var query = @"select pg_sleep(1)";
                var connectionType = CoreConfigurationManager.DBConnectionType();
                
                if (connectionType == "NPGSQL")
                {
                    using (var connection =
                        new NpgsqlConnection(ConnectionConfigurationManager.MasterConnectionString))
                    {
                        using (var command = new NpgsqlCommand(query, connection))
                        {

                            if (command.Connection.State == ConnectionState.Closed)
                                command.Connection.Open();

                            var res = command.ExecuteNonQuery();
                            Console.WriteLine($"{DateTime.Now} - thread completed  {index} - result {res}");
                        }
                    }
                }
                else if (connectionType == "EDB")
                {
                    using (var connection = new EDBConnection(ConnectionConfigurationManager.MasterConnectionString))
                    using (var command = new EDBCommand(query, connection))
                    {

                        if (command.Connection.State == ConnectionState.Closed)
                            command.Connection.Open();

                        var res = command.ExecuteNonQuery();
                        Console.WriteLine($"{DateTime.Now} - thread completed  {index} - result {res}");
                    }
                }

            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
Connectionstring :

 <add name="MasterConnectionString" connectionString="Host='XXX';port=9999;username='XXX';password='XXX;Database='XXXX';Timeout=300;ConnectionLifetime=2;MinPoolSize=5;MaxPoolSize=25;CommandTimeout=300;ApplicationName=nelson_console;" />
   <add name="NPGSQLMasterConnectionString" connectionString="Host='XXX';port=9999;username='XXX';password='XXX';Database='XXXX';Timeout=300;ConnectionLifetime=2;MinPoolSize=5;MaxPoolSize=25;CommandTimeout=300;Application Name=nelson_console;" />      


```





```
using Npgsql;

namespace NpgsqlTest
{
    class NpgsqlTestClass
    {
        static void Main(string[] args)
        {
            NpgsqlConnectionStringBuilder connectionBuilder = new NpgsqlConnectionStringBuilder();
            connectionBuilder.Host = "localhost";
            connectionBuilder.Username = "postgres";
            connectionBuilder.Password = "test";
            connectionBuilder.Port = 5432;
            connectionBuilder.Database = "";

            NpgsqlConnection connection = new NpgsqlConnection(connectionBuilder);
            connection.Open();
            NpgsqlCommand command = new NpgsqlCommand("CREATE DATABASE \"newDataBase\" \n" +
                                                      "WITH OWNER \"postgres\" \n" +
                                                      "ENCODING = 'UTF8' \n" +
                                                      "TEMPLATE = template0 \n" +
                                                      "CONNECTION LIMIT = -1; \n", connection);

            command.ExecuteNonQuery();
            connection.Close();
            connectionBuilder.Database = "newDataBase";
            connection = new NpgsqlConnection(connectionBuilder);
            connection.Open();
            command = new NpgsqlCommand("CREATE EXTENSION postgis \n" +
                                        "SCHEMA public ; \n", connection);
            command.ExecuteNonQuery();
        }
    }
}
```



```

```







```c#
# https://stackoverflow.com/questions/46128132/how-to-insert-and-retrieve-image-from-postgresql-using-c-sharp
using Npgsql;
using NpgsqlTypes;

using (var conn = new NpgsqlConnection(connString))
{
    string sQL = "insert into picturetable (id, photo) VALUES(65, @Image)";
    using (var command = new NpgsqlCommand(sQL, conn))
    {
        NpgsqlParameter param = command.CreateParameter();
        param.ParameterName = "@Image";
        param.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
        param.Value = ImgByteA;
        command.Parameters.Add(param);

        conn.Open();
        command.ExecuteNonQuery();
    }
}


using (var conn = new NpgsqlConnection(connString))
{
    string sQL = "SELECT photo from picturetable WHERE id = 65";
    using (var command = new NpgsqlCommand(sQL, conn))
    {
        byte[] productImageByte = null;
        conn.Open();
        var rdr = command.ExecuteReader();
        if (rdr.Read())
        {
            productImageByte = (byte[])rdr[0];
        }
        rdr.Close();
        if (productImageByte != null)
        {
            using (MemoryStream productImageStream = new System.IO.MemoryStream(productImageByte))
            {
                ImageConverter imageConverter = new System.Drawing.ImageConverter();
                pictureBox1.Image = imageConverter.ConvertFrom(productImageByte) as System.Drawing.Image;
            }
        }
    }
}
```





# Network



## localhost 可以127.0.0.1 不可



```
C:/WINDOWS/system32/drivers/etc/hosts
127.0.0.1 localhost # 修改

ipconfig /flushdns # 刷新DNS

#https://blog.csdn.net/StrideBin/article/details/78063685
	localhost不能访问127.0.0.1可以访问
```








# WinForm



## Path



```c#
string path = $"{Directory.GetCurrentDirectory()}"; // exe 文件目录

var ext = Path.GetExtension(filePath).ToLowerInvariant();

```



## 打开新窗体



```c#
new imgBoardForm("").Show();
```



## 鼠标穿透窗体

```
# https://blog.csdn.net/u012372584/article/details/113916322
	# QT 实现
引入user32.dll

 [DllImport("user32.dll")]
 public static extern uint SetWindowLong(IntPtr h, int n, uint x);
 
使指定窗体穿透，this.Handle为将要设为穿透效果的窗体句柄

SetWindowLong(this.Handle, -20, 0x20 | 0x80000);
 
恢复
  this.FormBorderStyle =  this.FormBorderStyle;
```



## 最小化到托盘+双击托盘恢复

- https://blog.csdn.net/cxu123321/article/details/93380478



## 拖盘菜单

- https://www.cnblogs.com/huashanqingzhu/p/6899383.html



## 截图

> doc\lang\programming\csharp\cut





## 显示图片

```c#
# pictureBox    
    	public void loadImage(string _imagePath)
        {
            if (_imagePath == "")
            {
                return;
            }
            this.imagePath = _imagePath;
            if (this.img != null)
            {
                this.img.Dispose();
            }
            this.img = new Mat(this.imagePath);
            if (pictureBox1.Image != null)
            {
                pictureBox1.Image.Dispose();
            }
            string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
            File.Copy(_imagePath, dist);
            this.pictureBox1.Image = Image.FromFile(dist);
        }
```



### 显示内存流的图片



```c#
#  OpenCvSharp.Mat

        void showImage()
        {
            using (var memoryStream = img.ToMemoryStream())
            {

                var image = Image.FromStream(memoryStream);
                this.pictureBox1.Image = image;
            }
        }

```



## 保存图片



```c#
            string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
            
            //保存到临时目录
            this.img_des.SaveImage(dist);

            this.img_des.Dispose();
            this.img_des = null;

            this.pictureBox2.Image.Dispose();
            Thread.Sleep(100);
            File.Delete(this.imagePath);
            Thread.Sleep(100);
            File.Move(dist, this.imagePath);
```





## 列表



```c#
        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count == 0)
            {
                return;
            }
            loadImage(listView1.SelectedItems[0].Tag.ToString());
        }
```



### 表头

```
# https://blog.csdn.net/weixin_30333885/article/details/99901696
	# winform ListView点击行表头，排序

```









## 入口点



```c#
        static void Main()
        {
            string erroLogPath = Directory.GetCurrentDirectory() + "/error.log";

            File.AppendAllText(erroLogPath, $"{DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")}\r\nstart:启动\r\n---------------------------------\r\n\r\n");

            ThreadPool.SetMinThreads(20, 20);
            ThreadPool.SetMaxThreads(20, 20);



            Application.SetUnhandledExceptionMode(UnhandledExceptionMode.CatchException);
            //处理UI线程异常
            Application.ThreadException += new ThreadExceptionEventHandler((o, teea) =>
            {
                File.AppendAllText(erroLogPath, $"{DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")}\r\nThreadException:\r\n{teea.Exception.Message},{teea.Exception.StackTrace}\r\n---------------------------------\r\n\r\n");
            });

            AppDomain.CurrentDomain.UnhandledException += new UnhandledExceptionEventHandler((o, ueea) =>
            {
                var err = ueea.ExceptionObject as Exception;
                File.AppendAllText(erroLogPath, $"{DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")}\r\nUnhandledException:\r\n{err.Message},{err.StackTrace}\r\n---------------------------------\r\n\r\n");
            });

            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
```



```
# 窗体初始化完成回调
        private void Form1_Load(object sender, EventArgs e)
        {
            new ws(this);  // websockes 连接初始化
        }
        
        // 改这里，窗体外观也会跟着变
        private void InitializeComponent()
        {
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Window;
            this.ClientSize = new System.Drawing.Size(0, 0);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.ShowInTaskbar = false;
            this.Text = "ocr";
            this.TransparencyKey = System.Drawing.SystemColors.Window;
            this.Load += new System.EventHandler(this.Form1_Load); // 窗体完成后回调，做其他初始化
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);
        }
```



## 添加资源



```
# 先生成资源文件
Open the Form1, right click Properties, look for the Localizable property, turn it to true then to False. You should see a new Form1.resx file being generated.

右键点击项目，选择属性
点击左侧的“应用程序”，选择“图标和清单”，在资源里面添加一个图标文件（*.ico或者*.icon）





```





## 拖盘图标



```
NotifyICon 控件，会显示一个图标在Windows 桌面右下角的工具栏里，图标可以设置右键菜单

重要：右击NotifyICon 属性，有一个icon，选一个图标，否则拖盘图标不会显示出来 

先往窗体上拖一个NotifyICon（这是拖盘图标），再拖一个ContextMenuStrip（这里右键菜单），右点NotifyICon 属性，把它的ContextMenuStrip 设成刚刚拖进来的ContextMenuStrip

在ContextMenuStrip 的Items 添加item ，这就是菜单项

```





## 打开程序文件夹



```
            string path = Directory.GetCurrentDirectory();
            System.Diagnostics.Process.Start("explorer.exe", path);
```



## 目录



### 遍历所有文件

```
        public static void allfiles(string targetDirectory, List<string> fnames )
        {
            // Process the list of files found in the directory.
            string[] fileEntries = Directory.GetFiles(targetDirectory);
            foreach (string fileName in fileEntries)
                fnames.Add(fileName);

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
            foreach (string subdirectory in subdirectoryEntries)
                allfiles(subdirectory, fnames);
        }
```



### 上级目录名



```
 string dir = Directory.GetParent(fnames2[0]).Name;
```





```



当前目录

stringpath= Environment.CurrentDirectory;

上级目录

string path = new DirectoryInfo("../").FullName;

上上级目录

string path = new DirectoryInfo("../../").FullName;


```



```
# 只要文件名
string name = Path.GetFileName(path);
# 扩展名
Path.GetExtension(imagePath)

```





## 文件读写



```c#
# 字节流
    	// http://localhost:5000/search/getaudio?id=1
 		[HttpGet("getaudio")]
        public async Task<IActionResult> getaudio()
        {
            string id = "1";

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录

            string dir_audio = Path.Combine(ecxutePath, "audio");

            if ( !Directory.Exists(dir_audio) )
            {
                Directory.CreateDirectory(dir_audio);
            }

            if (Request.Query.ContainsKey("id"))
            {
                id = Request.Query["id"].ToString();
            }

            string audioPath = Path.Combine(dir_audio, id + ".mp3");

            if (!System.IO.File.Exists(audioPath))
            {
                if (!anime.initQ)
                {
                    anime.initConn();
                }

                anime.g_conn.Open();

                string sql = $"SELECT id, audio FROM anime WHERE id={id};";

                using (var cmd = new NpgsqlCommand(sql, anime.g_conn))
                {
                    NpgsqlDataReader reader = await cmd.ExecuteReaderAsync();
                    if (reader.HasRows)
                    {
                        while (reader.Read())
                        {
                            string idd = reader["id"].ToString();
                            byte[] audio = (byte[])reader["audio"];

                            try
                            {
                                System.IO.File.WriteAllBytes(audioPath, audio);
                            } catch(Exception ex)
                            {
                                Console.WriteLine("### ERROR: 写入audio 失败. " + ex.Message);
                                throw new Exception(ex.Message);
                            }

                        }
                    }
                }

                anime.g_conn.Close();

            }

            var memory = new MemoryStream();
            using (var stream = new FileStream(audioPath, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                await stream.CopyToAsync(memory);
            }
            memory.Position = 0;
            //var types = GetMimeTypes();
            //var ext = Path.GetExtension(filePath).ToLowerInvariant();
            return File(memory, "audio/mpeg", "tmp.mp3");

        }
```



```c#

            g_conn = new NpgsqlConnection("Server=xx.xx.xx.xx;Port=5432;Database=anime;User Id=postgres;Password=xx;MinPoolSize=2;Maximum Pool Size=3;Connection Idle Lifetime=200;Tcp Keepalive = true;Keepalive = 30;");
            initQ = true;

				anime.g_conn.Open();

                string sql = $"SELECT id, audio FROM anime WHERE id={id};";

                using (var cmd = new NpgsqlCommand(sql, anime.g_conn))
                {
                    NpgsqlDataReader reader = await cmd.ExecuteReaderAsync();
                    if (reader.HasRows)
                    {
                        while (reader.Read())
                        {
                            string idd = reader["id"].ToString();
                            byte[] audio = (byte[])reader["audio"];

                            try
                            {
                                System.IO.File.WriteAllBytes(audioPath, audio);
                            } catch(Exception ex)
                            {
                                Console.WriteLine("### ERROR: 写入audio 失败. " + ex.Message);
                                throw new Exception(ex.Message);
                            }

                        }
                    }
                }


                anime.g_conn.Close();
```







```
# 写文件
File.WriteAllText(@"xx\xx\", strj, new System.Text.UTF8Encoding(false));
# 读文件
File.ReadAllText(@"xx\xx", new System.Text.UTF8Encoding(false));  // utf8 无BOM
```



```
# string、json 互转
json = (JObject)JsonConvert.DeserializeObject(result);  // str to json
string strj = json.ToString();  // json to str

# 用流来读写
private void btnSave_Click(object sender, EventArgs e)
{
    string result = txtWrite.Text.Trim(); //输入文本
    StreamWriter sw = File.AppendText(@"D:\\test.txt"); //保存到指定路径
    sw.Write(result);
    sw.Flush();
    sw.Close();
}

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



## 系统热键

- https://www.meziantou.net/hotkey-global-shortcuts.htm windows 大佬

- https://github.com/meziantou/Window-Manager

  > 直接能用 WPF

- https://www.cnblogs.com/rosesmall/archive/2012/09/19/2693707.html

  ```
  HotKeyId   :=   GlobalAddAtom(‘MyHotKey’)   -   $C000;
  注：   HotKeyId的合法取之范围是0x0000到0xBFFF之间，   GlobalAddAtom函数得到的值
  在0xC000到0xFFFF之间，所以减掉0xC000来满足调用要求。
  ```

- https://blog.csdn.net/u011555996/article/details/78923743 获取窗口句柄

- https://www.cnblogs.com/daxingxing/archive/2012/05/31/2528381.html  遍历已注册的热键



```c#
# 注册 win + 小键盘7 热键 WPF窗体工程 
    # winform 好像不行
    # doc\lang\programming\csharp\Window-Manager WPF 工业级代码

using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Threading;
using System.Windows;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Interop;

namespace hotkey1
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(IntPtr hWnd, int id, ModifierKeys fsModifiers, Keys vk);

        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(IntPtr hWnd, int id);

        [DllImport("user32")]
        private static extern int ToAscii(int uVirtKey, int uScanCode, byte[] lpbKeyState, byte[] lpwTransKey, int fuState);

        [DllImport("user32")]
        internal static extern int GetKeyboardState(byte[] pbKeyState);

        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        private static extern short GetKeyState(int vKey);

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr SetWindowsHookEx(int idHook, LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr GetModuleHandle(string lpModuleName);


        private static int _lastHotKeyId = 0;
        private readonly int _id;

        public bool IsRegistered;

        private byte[] _keyboardStateNative;

        public delegate void HotKeyPressedEventHandler(object sender, EventArgs e);

        public event HotKeyPressedEventHandler HotKeyPressed;

        public const int WmHotKey = 786;

        private IntPtr _hookId = IntPtr.Zero;

        private delegate IntPtr LowLevelKeyboardProc(int nCode, IntPtr wParam, IntPtr lParam);
        private LowLevelKeyboardProc _proc;

        private const int WH_KEYBOARD_LL = 13;

        private const int WM_KEYDOWN = 0x100;
        private const int WM_KEYUP = 0x101;
        private const int WM_SYSKEYDOWN = 0x104;
        private const int WM_SYSKEYUP = 0x105;

        private const byte VK_SHIFT = 0x10;
        private const byte VK_CAPITAL = 0x14;

        public event System.Windows.Forms.KeyEventHandler KeyDown;
        public event System.Windows.Forms.KeyPressEventHandler KeyPress;
        public event System.Windows.Forms.KeyEventHandler KeyUp;

        [StructLayout(LayoutKind.Sequential)]
        private sealed class KeyboardHookStruct
        {
            /// <summary>
            /// Specifies a virtual-key code. The code must be a value in the range 1 to 254. 
            /// </summary>
            public int vkCode;
            /// <summary>
            /// Specifies a hardware scan code for the key. 
            /// </summary>
            public int scanCode;
            /// <summary>
            /// Specifies the extended-key flag, event-injected flag, context code, and transition-state flag.
            /// </summary>
            public int flags;
            /// <summary>
            /// Specifies the time stamp for this message.
            /// </summary>
            public int time;
            /// <summary>
            /// Specifies extra information associated with the message. 
            /// </summary>
            public int dwExtraInfo;
        }

        public void SendToLeft()
        {

        }

        private void SendToLeft(object sender, EventArgs eventArgs) => SendToLeft();

        private byte MyGetKeyState(Keys key)
        {
            var virtualKeyCode = (int)key;
            if (virtualKeyCode < 0 || virtualKeyCode > 255)
            {
                throw new ArgumentOutOfRangeException(nameof(key), key, "The value must be between 0 and 255.");
            }
            return _keyboardStateNative[virtualKeyCode];
        }

        private static bool GetHighBit(byte value)
        {
            return (value >> 7) != 0;
        }

        private static bool GetLowBit(byte value)
        {
            return (value & 1) != 0;
        }

        public bool IsDown(Keys key)
        {
            var keyState = MyGetKeyState(key);
            var isDown = GetHighBit(keyState);
            return isDown;
        }

        private void ThreadPreprocessMessageMethod(ref MSG msg, ref bool handled)
        {
            if (handled || msg.message != WmHotKey || (int)msg.wParam != _id)
                return;

            // hot key pressed

            // List pressed keys
            //var keys = new List<Keys>();
            //var keyboardStateNative = new byte[256];
            //GetKeyboardState(keyboardStateNative);
            //_keyboardStateNative = keyboardStateNative;

            //for (var i = 0; i < 256; i++)
            //{
            //    if (IsDown((Keys)i))
            //    {
            //        keys.Add((Keys)i);
            //    }
            //}

            /*

            if (!keys.Contains(e.KeyData))
            {
                keys.Add(e.KeyData);
            }

            // Find hotkey
            foreach (HotKey hotKey in _hotKeys)
            {
                if (hotKey.Equals(keys))
                {
                    if (hotKey.Action != null)
                    {
                        hotKey.Action(sender, EventArgs.Empty);
                        e.Handled = true;
                    }
                }
            }
            */

            int a = 1;

            //OnHotKeyPressed();
            //handled = true;
        }

        private IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam)
        {
            var handled = false;
            if (nCode >= 0)
            {
                var myKeyboardHookStruct = (KeyboardHookStruct)Marshal.PtrToStructure(lParam, typeof(KeyboardHookStruct));
                if ((wParam.ToInt32() == WM_KEYDOWN || wParam.ToInt32() == WM_SYSKEYDOWN))
                {
                    var keyData = (Keys)myKeyboardHookStruct.vkCode;
                    var e = new System.Windows.Forms.KeyEventArgs(keyData);

                    //ctrl+alt+上下调整水平线
                    if (e.Shift && e.Alt && (e.KeyValue == 38 || e.KeyValue == 40))
                    {
                        //lineY = e.KeyValue == 38 ? lineY - 2 : lineY + 2;
                        //this.line1.Top = lineY + 10;

                        int a = 0;
                    }

                    //KeyDown(this, e);
                    handled = handled || e.Handled;
                }

                if (wParam.ToInt32() == WM_KEYDOWN)
                {
                    var isDownShift = (GetKeyState(VK_SHIFT) & 0x80) == 0x80;
                    var isDownCapslock = GetKeyState(VK_CAPITAL) != 0;

                    var keyState = new byte[256];
                    GetKeyboardState(keyState);
                    var inBuffer = new byte[2];
                    if (ToAscii(myKeyboardHookStruct.vkCode, myKeyboardHookStruct.scanCode, keyState, inBuffer, myKeyboardHookStruct.flags) == 1)
                    {
                        var key = (char)inBuffer[0];
                        if ((isDownCapslock ^ isDownShift) && char.IsLetter(key)) key = char.ToUpperInvariant(key);
                        var e = new KeyPressEventArgs(key);
                        //KeyPress(this, e);
                        handled = handled || e.Handled;
                    }
                }

                if ((wParam.ToInt32() == WM_KEYUP || wParam.ToInt32() == WM_SYSKEYUP))
                {
                    var keyData = (Keys)myKeyboardHookStruct.vkCode;
                    var e = new System.Windows.Forms.KeyEventArgs(keyData);
                    //KeyUp(this, e);
                    handled = handled || e.Handled;
                }
            }

            // if event handled in application do not handoff to other listeners
            return new IntPtr(1);
        }

        void HookKeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
        {

        }

        public MainWindow()
        {
            InitializeComponent();

            ModifierKeys fsModifiers = ModifierKeys.Windows;
            Keys vk = Keys.NumPad7;
            _id = Interlocked.Increment(ref _lastHotKeyId);
            IntPtr hWnd = new WindowInteropHelper(System.Windows.Application.Current.MainWindow).Handle;

            ComponentDispatcher.ThreadPreprocessMessage += ThreadPreprocessMessageMethod;
            // ThreadPreprocessMessageMethod 
            // 内部维护一个 _id ，win32 函数 RegisterHotKey 注册热键时把这个 _id 传进去。只要有热键触发就会回调 ThreadPreprocessMessageMethod，参数 msg.wParam 如果等于 _id 就表明你注删的热键触发了


            IsRegistered = RegisterHotKey(hWnd, _id, fsModifiers, vk);

            //_proc = HookCallback;
            //var curProcess = Process.GetCurrentProcess();
            //ProcessModule curModule = curProcess.MainModule;
            //_hookId = SetWindowsHookEx(WH_KEYBOARD_LL, _proc, GetModuleHandle(curModule.ModuleName), 0);



            //KeyDown += new System.Windows.Forms.KeyEventHandler(HookKeyDown);

            //HotKeyPressed += SendToLeft;

            //ComponentDispatcher.ThreadPreprocessMessage += ThreadPreprocessMessageMethod;

            //IsRegistered = !UnregisterHotKey(hWnd, _id);

        }
    }
}




```





```C#
using System;
using System.Text;
using System.Runtime.InteropServices;
using System.Windows.Forms;

public class SystemHotKey
{
    /// <summary>
    /// 如果函数执行成功，返回值不为0。
    /// 如果函数执行失败，返回值为0。要得到扩展错误信息，调用GetLastError。
    /// </summary>
    /// <param name="hWnd">要定义热键的窗口的句柄</param>
    /// <param name="id">定义热键ID（不能与其它ID重复）</param>
    /// <param name="fsModifiers">标识热键是否在按Alt、Ctrl、Shift、Windows等键时才会生效</param>
    /// <param name="vk">定义热键的内容</param>
    /// <returns></returns>
    [DllImport("user32.dll", SetLastError = true)]
    public static extern bool RegisterHotKey(IntPtr hWnd, int id, KeyModifiers fsModifiers, Keys vk);

    /// <summary>
    /// 注销热键
    /// </summary>
    /// <param name="hWnd">要取消热键的窗口的句柄</param>
    /// <param name="id">要取消热键的ID</param>
    /// <returns></returns>
    [DllImport("user32.dll", SetLastError = true)]
    public static extern bool UnregisterHotKey(IntPtr hWnd, int id);

    /// <summary>
    /// 辅助键名称。
    /// Alt, Ctrl, Shift, WindowsKey
    /// </summary>
    [Flags()]
    public enum KeyModifiers { None = 0, Alt = 1, Ctrl = 2, Shift = 4, WindowsKey = 8 }

    /// <summary>
    /// 注册热键
    /// </summary>
    /// <param name="hwnd">窗口句柄</param>
    /// <param name="hotKey_id">热键ID</param>
    /// <param name="keyModifiers">组合键</param>
    /// <param name="key">热键</param>
    public static void RegHotKey(IntPtr hwnd, int hotKeyId, KeyModifiers keyModifiers, Keys key)
    {
        if (!RegisterHotKey(hwnd, hotKeyId, keyModifiers, key))
        {
            int errorCode = Marshal.GetLastWin32Error();
            if (errorCode == 1409)
            {
                MessageBox.Show("热键被占用 ！");
            }
            else
            {
                MessageBox.Show("注册热键失败！错误代码：" + errorCode);
            }
        }
    }

    /// <summary>
    /// 注销热键
    /// </summary>
    /// <param name="hwnd">窗口句柄</param>
    /// <param name="hotKey_id">热键ID</param>
    public static void UnRegHotKey(IntPtr hwnd, int hotKeyId)
    {
        //注销指定的热键
        UnregisterHotKey(hwnd, hotKeyId);
    }

}
```



#### C# 动态调试器

- https://bbs.pediy.com/thread-270368.htm

  

# Avalonia

- https://github.com/AvaloniaUI/Avalonia.MusicStore



# UGUI



- https://www.raywenderlich.com/6570-introduction-to-unity-ui-part-1



# VS Code



```
dotnet new console --framework net5.0

dotnet run
```



```
# https://github.com/agracio/edge-js

js C# interop

```



# 动态脚本

- https://github.com/dotnetcore/Natasha



# 发布压缩



- https://www.qiufengblog.com/articles/asp-net-blazor-publish.html





# SignalR

SignalR是一个提供实时双向通信能力的组件。所谓双向，就是客户端和服务端都可以向对方发送消息。很多人会有一个误解，认为SignalR就是对WebSockets进行了一下封装，其实不然。WebSockets是SignalR的首选通信方式，但根据应用场景和网络环境等的不同，SignalR也会选择性的自动切换到服务端发送事件（Server-Sent Events）或者长轮询（Long Polling）的方式上。

SignalR使用了**hub**这样一个东西来支持客户端和服务端之间的通信，可以认为它是一个消息集散中心。客户端和服务端通过互相调用对方的方法的方式来进行消息的传递。

SignalR可以利用ASP.NET Core身份验证来识别每一个连接（Connection）所对应的用户，继而可以对hub及其中的方法进行权限控制。



# 视频下载

- https://github.com/ytdl-org/youtube-dl

  

```
--write-sub                      Write subtitle file
--write-auto-sub                 Write automatic subtitle file (YouTube only)
--all-subs                       Download all the available subtitles of the video
--list-subs                      List all available subtitles for the video
--sub-format FORMAT              Subtitle format, accepts formats preference, for example: "srt" or "ass/srt/best"
--sub-lang LANGS                 Languages of the subtitles to download (optional) separated by commas, use IETF language tags like 'en,pt'

youtube-dl --list-subs https://www.youtube.com/watch?v=9BSjD3f_FkE&t=83s #王德峰：《资本论》

youtube-dl --write-sub --sub-lang zh --skip-download https://www.youtube.com/watch?v=9BSjD3f_FkE&t=83s 
```



- https://github.com/leiurayer/downkyi
  
- **哔哩下载姬** CSharp 缺GUI代码
  
- https://github.com/kengwang/BiliDuang

  - https://www.52pojie.cn/forum.php?mod=viewthread&tid=1342876&highlight=%CA%D3%C6%B5%CF%C2%D4%D8

  - **BiliDuang - 哔哩哔哩视频下载器** CSharp 有GUI

- https://www.52pojie.cn/forum.php?mod=viewthread&tid=1384315&highlight=%CA%D3%C6%B5%CF%C2%D4%D8

  - you-get 支持多

    

# 爬虫



## sign



python has same section

```
using System;
using OpenQA.Selenium;
using OpenQA.Selenium.IE;
using OpenQA.Selenium.Interactions;
using System.Threading;

namespace BaiduAutoLoginOut
{
    class Program
    {
        static void Main(string[] args)
        {
            IWebDriver iw = new InternetExplorerDriver();
            iw.Navigate().GoToUrl("http://www.baidu.com");
            IWebElement login = iw.FindElement(By.Id("s_username_top"));
            Actions action = new Actions(iw);
            action.MoveToElement(login).Build().Perform();
            WaitUntilPageLoaded(iw, "//a[text()=' 退出 ']");
            iw.FindElement(By.XPath("//a[text()=' 退出 ']")).Click();
        }
        private static void WaitUntilPageLoaded(IWebDriver iw, string v)
        {
            try
            {
                iw.FindElement(By.XPath(v));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
                Thread.Sleep(1000);
                WaitUntilPageLoaded(iw, v);
            }
        }
    }
}
```





