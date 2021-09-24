





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



### 出现次数

```
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



### 拼接



```c#
# {} 里面的是动态计算
string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
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







## 自动格式化



```
Ctrl + K ,  Ctrl + D.  自动整理代码
```





# 图像



# FFMPEG



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



```
当前目录

stringpath= Environment.CurrentDirectory;

上级目录

string path = new DirectoryInfo("../").FullName;

上上级目录

string path = new DirectoryInfo("../../").FullName;

```





## 文件读写



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



