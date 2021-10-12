





## .net core



```
        // /home/data/users/xxx/soft/dotnet ainlp.dll
        // /home/data/users/xxx/project/smartsearch

        // curl -d "" "http://localhost:63164/api/smarsearch/search"
        // 要禁止强制跳转，只需要在项目的 Startup.cs 程序的 Configure 方法中注释掉 “app.UseHttpsRedirection();” 这一行代码即可。
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



## Json



Newtonsoft.Json



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



## String



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





## blazor



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



# 进程、异步、流



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



# OS 兼容



```c#
# https://github.com/madelson/MedallionShell/blob/master/SampleCommand/PlatformCompatibilityTests.cs

public static readonly string DotNetPath = RuntimeInformation.IsOSPlatform(OSPlatform.Windows)
            ? @"C:\Program Files\dotnet\dotnet.exe"
            : "/usr/bin/dotnet";
            
```



# anime_Danganronpa_version1.cs



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



# Postgresql



HeidiSQL 、Navicat Premium



```
# https://www.connectionstrings.com/npgsql/
	# 连接串
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

```





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
			byte[] bts = null;

            using (FileStream stream = new FileStream("tmp.mp3", FileMode.Open, FileAccess.Read))
            using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
            {
                bts = reader.ReadBytes(Convert.ToInt32(stream.Length));
            }

            return bts;
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



