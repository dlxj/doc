## datatime

```c#
            int unixTimestamp = ((int)DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1)).TotalSeconds);
            DateTime ConvertedUnixTime = DateTimeOffset.FromUnixTimeSeconds(unixTimestamp).DateTime;
            string batch = ConvertedUnixTime.ToString("yyyy-MM-dd HH:mm:ss");
```



## Json



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



## 正则



```c#
                Regex r = new Regex(@"[^0-9,]*");
                srcList = r.Replace(srcList, "");
```









