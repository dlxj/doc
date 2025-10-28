

## visual studio 2022

### 复制文件到 bin

```

see huggingface\WeChatOcr\src\WeChatOcr\WeChatOcr.csproj

	<ItemGroup>
		<Content Include="wco_data\**">
			<CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
			<PackageCopyToOutput>true</PackageCopyToOutput>
		</Content>
	</ItemGroup>



```





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



```
            DateTime lastCreate = DateTime.Parse("1971-01-01");

            lock (bookIndexCreateHisotry)
            {
                if (!bookIndexCreateHisotry.TryGetValue(appID, out lastCreate))
                {
                    bookIndexCreateHisotry.Add(appID, DateTime.Now);
                }
            }

            var ts = DateTime.Now - lastCreate;

            // 有效时间8小时
            if (ts.TotalHours >= 8760)
```







## Grammar



### ??

```
`??` 是 C# 语言中的空合并运算符（Null-coalescing operator）。它用于在一个表达式可能为空（null）时提供一个默认值。

see https://github.com/loongEgg/LoongKeys

        public DelegateCommand(Action<T> execute, Predicate<T> canExecute) {
            _Execute = execute ?? throw new ArgumentNullException("execute 不能为空");
            _CanExecute = canExecute;
        }
        	# 为空就抛异常
        

```





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



### Lazy Singleton

```

see nodejs summary.md -> WPF -> STranslate 对标Bob

STranslate.Util\SingletonUtil.cs

public class Singleton<T> where T : class, new()
{
    private static readonly Lazy<T> _instance = new(() => (T)Activator.CreateInstance(typeof(T), true)!, true);

    public static T Instance => _instance.Value;
}

`Singleton<T>` 是一个通用的单例（Singleton）泛型类，用于实现对某个类型（`T`）的惰性单例模式（Lazy Singleton）。以下是对它的功能和用途的详细说明：

### 功能解析

1. **`Singleton<T>` 类的定义**:  
   - 这是一种通用的、线程安全的单例模式实现。
   - 它可以用于任何满足以下条件的类型 `T`：
     - `T` 必须是引用类型（即 `class`）。
     - `T` 必须有一个无参的 `public` 或 `protected` 构造函数（因为泛型约束中指定了 `new()`）。

2. **线程安全的单例实现**:
   - 使用了 `Lazy<T>` 类型来确保实例的创建是延迟（Lazy）的，即只有在第一次访问 `Instance` 属性时才会创建实例。
   - `Lazy<T>` 默认具有线程安全性，因此可以安全地在多线程环境中使用，无需额外的锁机制。

3. **结构与关键点**:
   - `_instance` 是一个私有静态字段，存储了 `Lazy<T>` 类型的实例。  
   - `_instance` 的 `Value` 属性用于访问和初始化 `T` 类型的单例实例。
   - `Instance` 是一个公共的静态属性，用于全局访问 `T` 的单例对象。
   - `(T)Activator.CreateInstance(typeof(T), true)!`: 使用反射的方式，调用 `T` 的无参构造函数（包括 `protected` 和 `private` 构造函数）。

---

### 主要用途

1. **单实例管理**:  
   如果某个类中只需要一个实例（例如配置管理器、日志记录器、系统上下文等），可以使用该单例模式来管理实例。

2. **解决泛型单例问题**:  
   传统单例模式通常用于具体类型，而通过泛型类 `Singleton<T>`，可以对任何满足约束的类型 `T` 使用单例模式，而无需重复实现。

3. **线程安全**:  
   `Lazy<T>` 的线程安全机制能够确保单例实例的初始化仅发生一次。

---

### 使用方法

假设有以下一个类 `MyClass`：

​```csharp
public class MyClass
{
    private MyClass() 
    {
        Console.WriteLine("MyClass Constructor Called");
    }
    
    public void DoWork()
    {
        Console.WriteLine("Working...");
    }
}
​```

因为 `MyClass` 是一个带有私有构造函数的类，我们可以通过 `Singleton<T>` 作为其单例管理器：

​```csharp
var instance1 = Singleton<MyClass>.Instance;
var instance2 = Singleton<MyClass>.Instance;

instance1.DoWork();

// 检查是否是同一个实例
Console.WriteLine(ReferenceEquals(instance1, instance2)); // 输出为 True
​```

运行结果：
​```
MyClass Constructor Called
Working...
True
​```

这里通过 `Singleton<MyClass>.Instance` 获取了全局的单例实例。而由于 `MyClass` 的构造函数是私有的，传统写法无法直接创建实例，但 `Activator.CreateInstance` 可以突破这种限制。

---

### 代码改进建议

1. **传递自定义参数**:
   如果需要为单例类 `T` 的构造函数传递参数，可以扩展实现方法，例如通过其他方法注入构造参数。

2. **实例初始化回调**:
   如果需要对实例进行初始化操作，可以进一步扩展 `Singleton<T>` 来支持自定义的初始化逻辑。

---

### 总结

该类的主要用途是通用的惰性单例模式实现，可以用于管理引用类型的单例对象，尤其适合应用于需要确保全局唯一性的对象（如配置、日志、缓存上下文等）。




`Singleton<T>` 类通过 **`Lazy<T>`** 和静态字段实现了只创建一次实例（即确保只调用一次 `new`）。以下是具体的原理分析，重点说明它是如何保证只初始化一次的。

---

### 核心点：单例实现的关键在于 **`Lazy<T>`** 和 **静态字段**


```


#### 1. 静态字段的特性



    - **静态字段（`static` 字段）在类的生命周期中仅初始化一次并且由 CLR（Common Language Runtime）保证线程安全。**
        - 静态字段在类被第一次使用时会初始化；之后不会再重新初始化。
        - 初始化是由 CLR 自动保证的，多线程环境中静态字段（如 `_instance`）的初始化只会发生一次。
    - 在代码中：
        ```csharp
        private static readonly Lazy<T> _instance = new(() => (T)Activator.CreateInstance(typeof(T), true)!, true);
        
    - `_instance` 是类的一个静态字段，并且是只读字段。
    - 它被初始化为 `Lazy<T>` 实例（支持惰性初始化）。

#### 2. `Lazy<T>` 的线程安全机制
- **`Lazy<T>` 是 .NET 提供的一个专门用于实现延迟初始化的结构，允许你在真正需要的时候才初始化某个对象。**
- **线程安全性**:
    - 默认情况下，`Lazy<T>` 使用 `LazyThreadSafetyMode` 的 **`ExecutionAndPublication` 模式**，这意味着多线程环境中只会初始化一次：
        1. 多个线程并发访问 `Lazy.Value` 时，CLR 保证只会有一个线程真正执行初始化方法（`Activator.CreateInstance(...)`），其他线程会阻塞直到初始化完成。
        2. 初始化完成后，所有线程都能获取相同的实例。
    - 另一个参数 `true`（传递到 `Lazy<T>` 的构造器中）进一步明确了线程安全性。

    **初始化方式:**
    ```csharp
    new(() => (T)Activator.CreateInstance(typeof(T), true)!, true);
    ```
    表示：
    - 延迟执行匿名方法 `() => (T)Activator.CreateInstance(...)`，直到调用 `Lazy<T>.Value` 属性。
    - 第二个参数 `true` 明确开启线程安全。

#### 3. 懒加载的工作原理
- 整个单例机制的核心是 **`Lazy<T>` 的延迟初始化**：
    - 在代码中，当你第一次访问 `Singleton<T>.Instance` 时：
      ```csharp
      public static T Instance => _instance.Value;
      ```
      触发了 `_instance.Value` 的访问。
    - `Lazy<T>` 的 `Value` 属性会检查实例是否已经创建：
        - **如果实例还未创建：**  
          开始执行 `Lazy<T>` 的初始化委托 `() => (T)Activator.CreateInstance(...)`，创建一个新的实例。
        - **如果实例已经创建：**  
          直接返回已经创建的实例。
    - 由于 `Lazy<T>` 自身提供线程安全性，这整个过程是线程安全的，确保初始化方法只执行一次。

---

#### 4. 执行流程示例

以代码为例，分析其如何只 `new` 一次：

```csharp
var instance1 = Singleton<MyClass>.Instance;
var instance2 = Singleton<MyClass>.Instance;

Console.WriteLine(ReferenceEquals(instance1, instance2)); // 输出 True
​```

#### 执行顺序

1. **静态字段初始化**：
    - 类 `Singleton<MyClass>` 第一次被使用时，静态字段 `_instance` 会被初始化。
    - `_instance` 是一个 `Lazy<T>`，但初始化时并不会立即创建真实的 `T` 类型（即 `MyClass`）。
2. **懒加载（Lazy Initialization）**：
    - 第一次访问 `Singleton<MyClass>.Instance` 时：
        - 调用 `_instance.Value`。
        - 检测是否已初始化内部对象：
            - 未初始化：执行初始化方法 `() => (T)Activator.CreateInstance(...)`，并创建 `MyClass` 的实例。
            - 已初始化：直接返回已创建的 `MyClass` 实例。
3. **返回实例**：
    - `Singleton<MyClass>.Instance` 返回 `MyClass` 单例。
    - 后续每次访问 `Instance`，都会直接返回 `Lazy<T>` 内部存储的已创建实例。

---

### 实现只调用一次 `new`

- **`Lazy<T>` 的核心**：
    - `Lazy<T>` 内部包含了一个布尔标志，用于记录是否已经初始化实例。
    - 只有第一次访问 `Value` 时，才会尝试初始化，后续直接返回已经初始化的值。
    - 多线程环境下，`LazyThreadSafetyMode.ExecutionAndPublication` 能确保其他线程在实例创建的同时阻塞，直到初始化完成。

#### 核心机制简化为伪代码：
假设 `Lazy<T>` 的内部逻辑如下：
​```csharp
private bool isInitialized; // 标志变量，初始值为 false
private T value;

public T Value
{
    get
    {
        if (!isInitialized)
        {
            // 线程安全地初始化值
            lock (lockObject)
            {
                if (!isInitialized)
                {
                    value = initializationDelegate();
                    isInitialized = true; // 将标志置为 true
                }
            }
        }
        return value; // 返回已初始化的值
    }
}
​```

- 在第一次调用 `Lazy<T>.Value` 时，会通过 `initializationDelegate` 调用 `Activator.CreateInstance(...)` 来创建实例，同时将 `isInitialized` 标志置为 `true`。
- 后续调用时，不会再执行初始化，而是直接返回实例 `value`。

---

### 总结

**如何只调用一次 `new`：**
1. 依赖于静态字段的初始化特性：静态字段（`_instance`）整个程序运行期间只会初始化一次。
2. 使用 `Lazy<T>` 内部的延迟加载和线程安全机制：
    - 保证第一次访问时懒加载实例。
    - 多线程并发访问时，通过锁或者原子性操作确保只有一个线程完成初始化。

因此，无论多少次访问 `Singleton<T>.Instance`，内部的 `new T()` 都只执行一次。

```



### 线程安全集合

```
# see huggingface\yt-dlp-gui\yt-dlp-gui\ViewModels\Main.cs
public ConcurrentObservableCollection<Chapters> Chapters { get; set; } = new();


这段C#代码声明了一个公共属性 `Chapters`，其类型为 `ConcurrentObservableCollection<Chapters>`，并初始化为一个新的空集合。以下是对其作用的详细解释：

### **1. 核心功能**
• **线程安全集合**：  
  `ConcurrentObservableCollection` 是一个**并发安全的可观察集合**，结合了以下特性：
  • **线程安全**：允许多个线程同时添加、删除或修改元素，避免线程冲突（如锁竞争）。
  • **可观察性**：当集合内容变化时，自动触发事件（如 `INotifyCollectionChanged`），通知订阅者（如UI控件）更新。

• **数据绑定**：  
  适用于需要将集合数据绑定到UI的场景（如WPF、UWP、Android/Xamarin）。当章节数据变化时，UI会自动刷新。


```



### Theme

```

see huggingface\itrans\src\iTrans\Themes\DarkTheme.xaml

App.xaml
    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="Themes/DarkTheme.xaml"/>
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>
    
huggingface\itrans\src\iTrans\MainView.xaml
	Background="{StaticResource BackgroundColour}"
		# 使用样式
		
```





### 嵌入资源

```

# see huggingface\yt-dlp-gui\yt-dlp-gui\Views\Main.xaml

        Icon="pack://application:,,,/Resources/logo.ico">


在 WPF 应用程序中，`pack://application:,,,` 是特殊的 URI 语法，用于访问应用程序资源。具体来说：

这个 URI 的完整结构是 `pack://application:,,,/资源路径`，其中：

1. `pack://` 表示使用 WPF 的 pack URI 方案
2. `application:,,,` 表示资源位于当前应用程序的主程序集中
3. `/Resources/logo.ico` 是资源在程序集中的路径

这个语法常用于访问被标记为"资源"（Resource）类型的文件，这些文件会在编译时被嵌入到程序集中。其等价于更简短的写法：`/AssemblyName;component/Resources/logo.ico`，但这里使用了更明确的 pack URI 格式。

在您代码中的具体应用：
​```xml
Icon="pack://application:,,,/Resources/logo.ico"
​```
表示从当前应用程序的程序集中加载位于 Resources 文件夹下的 logo.ico 文件作为窗口图标。

三个逗号 `,,,` 是 URI 的合法语法，表示：
- 第一个逗号分隔 application: 和空的主机名
- 第二个逗号分隔空的主机名和空端口
- 第三个逗号作为路径分隔符

这是 WPF 定义的标准资源引用方式，适用于所有被编译为 Embedded Resource 的文件。


```





## Json

- https://www.cnblogs.com/xtxk110/archive/2019/10/11/11654486.html  转DataTable 有行和列
- https://blog.csdn.net/q__y__L/article/details/103566693  真 高级用法



### JObject 简化写法

```
see huggingface\WeChatOcr\src\WeChatOcr\Wchtcr.cs

arr.Add(new JObject{ { "x", Left }, { "y", Top } });  // 左上
arr.Add(new JObject{["x"] = Right, ["y"] = Top });    // 右上
	# 两种写法都可以


var obj = new JObject();
array.Add(obj);

var word = item.SingleStrUtf8;  // 一行的文本
obj.Add("word", word);

var Left = item.Left;
var Right = item.Right;
var Top = item.Top;
var Bottom = item.Bottom;
JArray arr = new JArray();
arr.Add(new JObject{["x"] = Left,  ["y"] = Top});     // 左上
arr.Add(new JObject{["x"] = Right, ["y"] = Top });    // 右上
arr.Add(new JObject{["x"] = Left,  ["y"] = Bottom }); // 左下
arr.Add(new JObject{["x"] = Right, ["y"] = Bottom }); // 右下
// 一行四个解的坐标
obj.Add("pos", arr);

res = root.ToString();
```



### 对象序列化

```

see huggingface\imradv3\src\WpfEditor\TextEditorControl.cs


[Serializable]
public class TextCharacter
{
    public System.Text.Rune Character { get; set; }
    public Brush Foreground { get; set; } = Brushes.Black;
    public bool IsComment { get; set; } = false;
    public bool IsKeyword { get; set; } = false;
    public bool IsString { get; set; } = false;
    public bool IsNumber { get; set; } = false;


    // 字符在图片上的坐标和宽高
    public int x { get; set; } = -1;
    public int y { get; set; } = -1;
    public int w { get; set; } = -1;
    public int h { get; set; } = -1;
    

    public string ImageMD5 { get; set; } = "";

    // 添加无参构造函数用于JSON反序列化
    public TextCharacter()
    {
    }

    public TextCharacter(System.Text.Rune c)
    {
        Character = c;
    }

    public TextCharacter(System.Text.Rune c, int x, int y, int w, int h, string imageMd5)
    {
        Character = c;
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        ImageMD5 = imageMd5;
    }

    // 添加一个接受char的构造函数，方便兼容现有代码
    public TextCharacter(char c)
    {
        Character = new System.Text.Rune(c);
    }
}


string json = Newtonsoft.Json.JsonConvert.SerializeObject(characters);



// 反序列化
string json = Clipboard.GetData("TextEditorCustomFormat") as string;
//List<TextCharacter> characters = (List<TextCharacter>)Newtonsoft.Json.JsonConvert.DeserializeObject<List<TextCharacter>>(json);

List<TextCharacter> characters = new List<TextCharacter>();

List<JObject> ls = Newtonsoft.Json.JsonConvert.DeserializeObject<List<JObject>>(json);
	// System.Text.Rune 字段不支持直接序列化，所以需要转换
	// 实际上是因为它没有一个空白的构造函数，所以 Newtonsoft.Json 拿它没办法

foreach (var item in ls)
{
    var Character = item["Character"].Value<JObject>();
    var Value = Character["Value"].Value<int>();
    System.Text.Rune rune = new System.Text.Rune(Value);

    // 反序列化每个字符
    var chr = new TextCharacter(
        rune, // 获取第一个字符
        item["x"].Value<int>(),
        item["y"].Value<int>(),
        item["w"].Value<int>(),
        item["h"].Value<int>(),
        item["ImageMD5"].Value<string>()
    );
    characters.Add(chr);
}


```



### 转字符串并格式化

```
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;

// 示例：JArray 格式化
JArray jArray = new JArray { "A", "B", "C" };
string formattedJson = jArray.ToString(Formatting.Indented);
```





### 扩展

```

https://stackoverflow.com/questions/14886800/convert-jobject-into-dictionarystring-object-is-it-possible

	using Newtonsoft.Json;
	using Newtonsoft.Json.Linq;
	
	public static class JObjectExtensions
	{
	    public static IDictionary<string, object> ToDictionary(this JObject @object)
	    {
	        var result = @object.ToObject<Dictionary<string, object>>();
	
	        var JObjectKeys = (from r in result
	                           let key = r.Key
	                           let value = r.Value
	                           where value.GetType() == typeof(JObject)
	                           select key).ToList();
	
	        var JArrayKeys = (from r in result
	                          let key = r.Key
	                          let value = r.Value
	                          where value.GetType() == typeof(JArray)
	                          select key).ToList();
	
	        JArrayKeys.ForEach(key => result[key] = ((JArray)result[key]).Values().Select(x => ((JValue)x).Value).ToArray());
	        JObjectKeys.ForEach(key => result[key] = ToDictionary(result[key] as JObject));
	
	        return result;
	    }
	}


​    
    string code = @"
                console.log(fs)  // fs 是事先 import 好的模块，这里可以直接用  所有可用参数都在这里展开了：  ...params
                console.log('hello, from vm')
                return callback({ msg:'hi,,,' }) // 约定最后以 callback 返回值
            ";
    
            string imports = @"
                [""fs""]
            ";
    
            try
            {
                var url = "http://127.0.0.1:8880/vm/vmrun";
                var client = new RestClient(url);
                var request = new RestRequest();
                request.Method = Method.Post;
                request.Timeout = 5000;
                request.AddHeader("content-type", "application/x-www-form-urlencoded;charset=UTF-8");
                request.AddParameter("application/x-www-form-urlencoded", $"code={WebUtility.UrlEncode(code)}&imports={WebUtility.UrlEncode(imports)}", ParameterType.RequestBody);
    
                var response = client.Execute(request);
                string jsonstr = response.Content;


                JObject obj = JObject.Parse(jsonstr);
                int status = obj.Value<int>("status");
                if (status != 200)
                {
                    throw new Exception($"接口请求失败: {url}");
                }
                
                var m = obj["data"]["msg"].ToString();
    
                var d = obj.ToDictionary();
    
                int a = 1;
            }
            catch (Exception ex)
            {
                int b = 1;
            }

```





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

var data1 = new
{
    prism_wordsInfo = new[] 
    {
        new { word = "第一单元" }
    }
};

var json1 = JsonConvert.SerializeObject(data1, Formatting.Indented);


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
            
        // 动态添加数组，数组里再加对象
        JArray itemsArray = new JArray();
        
        // 创建第一个对象并添加到数组
        JObject item1 = new JObject();
        item1.Add("itemId", "001");
        item1.Add("itemName", "商品1");
        item1.Add("price", 99.9);
        itemsArray.Add(item1);
        
        // 创建第二个对象并添加到数组
        JObject item2 = new JObject();
        item2.Add("itemId", "002");
        item2.Add("itemName", "商品2");
        item2.Add("price", 199.5);
        itemsArray.Add(item2);
        
        // 将数组添加到主对象中
        obj.Add("items", itemsArray);

        var res = obj.ToString();
        Console.WriteLine(res);
            
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


​                
​                


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



### 4 字节表示一个字符 Rune

```

string smiley = "\uD83D\uDE00"; // 😀 表情符号，U+1F600

这里， \uD83D 是高位代理字符， \uDE00 是低位代理字符，它们一起表示了U+1F600这个4字节的Unicode字符。

C#中的字符串( string )使用UTF-16编码来表示Unicode字符。 2 对于4字节的Unicode字符（即超出基本多语言平面BMP的字符，码点值大于U+FFFF的字符），C#使用 代理对 （Surrogate Pair）机制来表示。


see huggingface\imradv3\src\WpfEditor\TextEditorControl.cs

                        // 遍历 oneChar 中的每个字符
                        for (int i = 0; i < oneChar.Length;)
                        {
                            // 获取当前位置的 Rune
                            Rune rune = Rune.GetRuneAt(oneChar, i);  // 4 个字节表示单个字符

                            // 将 Rune 添加到字符列表中
                            textLine.Characters.Add(new TextCharacter(rune, x, y, w, h, md5));

                            // 移动到下一个 Rune 的位置
                            i += rune.Utf16SequenceLength;
                        }


```



### Rune 遍历 string 的每一个字符

```

see huggingface\imradv3\src\WpfEditor\TextEditorControl.cs

					// 遍历 oneChar 中的每个字符
                    for (int i = 0; i < oneChar.Length;)
                    {
                        Rune rune = Rune.GetRuneAt(oneChar, i);  // 4 个字节表示单个字符


                        // 移动到下一个 Rune 的位置
                        i += rune.Utf16SequenceLength;
                    }
```



```

string lineText = string.Concat(line.Characters.Select(tc => tc.Character.ToString()));


var sb = new StringBuilder();
foreach (var textcharacter in line.Characters)
{
    sb.Append(textcharacter.Character.ToString());
}
string lineText = sb.ToString();


```







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
//  {} 里面的是动态计算
string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
```



```
// 致少 4 位数字
string imageName = $"{pageNumber:D4}.jpg";

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





### iterate with index

```

# see huggingface\imradv3\src\WpfEditor\MainWindow.xaml.cs
	using System.Linq; // 需要引入 LINQ 命名空间

                // 先删除选框下的文字
                int idx = -1;
                foreach (var (line, index) in Editor._lines.Select((line, index) => (line, index) ))
                {
                    if (line.selected_rectange == null || !line.selected_rectange.HasValues)
                    {
                        continue;
                    }
                    int Id = line.selected_rectange["Id"].Value<int>();
                    if (rect.Id == Id)
                    {
                        idx = index;
                        break;
                    }
                }
```





### CopyTo

```
// 创建一个源List集合
List<int> sourceList = new List<int> { 10, 20, 30, 40, 50 };

// 创建一个目标数组，长度要足够容纳要复制的元素
int[] targetArray = new int[10]; // 长度为10的数组

// 使用CopyTo方法复制元素
// 从sourceList的索引1开始(值20)，复制3个元素到targetArray的索引2开始的位置
sourceList.CopyTo(1, targetArray, 2, 3);

// 输出目标数组内容
Console.WriteLine(string.Join(", ", targetArray));
// 输出结果: 0, 0, 20, 30, 40, 0, 0, 0, 0, 0
```



### GetRange

```
List<T> GetRange(int index, int count);
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



### 命名元组

```
            // 使用C# 7.0引入的命名元组返回结果
            return (ImagePath: pth_img, JsonPath: pth_json);
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

```
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



​```c#
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



# Path



## 可执行文件所在目录

```
// 可执行文件所在目录的路径

public static readonly string ExecutablePath = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
```





## 程序目录下的特定 exe

```
# see huggingface\yt-dlp-gui\yt-dlp-gui\Views\Main.xaml.cs
	var deps = Directory.EnumerateFiles(App.AppPath, "*.exe", SearchOption.AllDirectories).ToList();
                	# 所有 exe
                deps = deps.Where(x => Path.GetFileName(App.AppExe) != Path.GetFileName(x)).ToList();
                	# 排除自身
```



## 改扩展名

```
 string jp2Path = Path.ChangeExtension(imagePath, ".jp2");
 
```



## Combine GetFullPath

```

see huggingface\imradv3\src\WpfEditor\global.cs

		public static (string ImagePath, string JsonPath) get_img_json_pth(string m5)
        {
            // 这是工作目录
            string pth_img = Path.Combine(Constant.ExecutablePath, "data", "img", $"{m5}.txt"); // .parent_path().parent_path() 在C#中不需要
            string pth_json = Path.Combine(Constant.ExecutablePath, "data", "json", $"{m5}.json"); // .parent_path().parent_path() 在C#中不需要

            // C#中不需要lexically_normal()，Path.GetFullPath可以规范化路径
            pth_img = Path.GetFullPath(pth_img);
            pth_json = Path.GetFullPath(pth_json);

            // 使用C# 7.0引入的命名元组返回结果
            return (ImagePath: pth_img, JsonPath: pth_json);
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



### byte 转 Mat

```

see huggingface\itrans\src\iTrans\ViewModels\MainViewModel.cs

Mat im_orig = Cv2.ImDecode(imageBytes, ImreadModes.Color);

using Rect = OpenCvSharp.Rect;
Cv2.Rectangle(im_orig, new Rect(x, y, width, height), new OpenCvSharp.Scalar(0, 0, 255) );

```



### Mat 转 byte

```

see huggingface\itrans\src\iTrans\ViewModels\MainViewModel.cs

mt.ToBytes()
                                    Mat mt = new Mat("E:\\huggingface\\ColorTextEditorV2\\data\\0003.jpg", ImreadModes.Color);
                                    var wechat_ocr_result = await ExecuteAsyncWechatOCR(mt.ToBytes(), CancellationToken.None);
                                    ;
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





## 异步回调

```
using Fleck;
using OpenCvSharp;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.Remoting.Messaging;


namespace ocrClient
{

    public delegate void drawingLineDelegate();

    public partial class imgRotateForm : Form
    {
        // key : path  value: image bytes
        public static Dictionary<string, Image> g_dic_images = new Dictionary<string, Image>();

        public static string g_state = "ready";
        public static int g_total = 0;
        public static int g_curr = 0;

        public static List<string> g_img_paths = new List<string>();

        SynchronizationContext _syncContext = null;


        string imagePath = "";

        Mat img;

        float angle = 1.0f;

        bool rotated = false; 

        //水平线
        int lineY = 0;

        line line1 = new line();

        //websocket对象
        ws w;
        //websocket连接
        IWebSocketConnection conn;


        //声明委托
        private delegate Mat calcHandler(string img_path);

        //代理方法
        public Mat calc(string img_path)
        {

            var img_src = new Mat(img_path);

            try
            {
                var newImg = Sample.matRotate(img_src, angle);
                img_src.Dispose();
                img_src = newImg;
            }
            catch (Exception)
            {
                MessageBox.Show("已到最大旋转角度");
            }

            return img_src;

        }

        //异步调用
        public async void calc_all(List<string> img_paths)
        {

            if (img_paths.Count <= 0)
            {
                return;
            }

            calcHandler handler = new calcHandler(calc);

            imgBoardForm.g_total = img_paths.Count;
            imgBoardForm.g_curr = 0;

            string path = img_paths[imgBoardForm.g_curr];
            IAsyncResult result = handler.BeginInvoke(path, new AsyncCallback(CallBack), "one task done.");

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

            string msg = $"处理进度：{imgBoardForm.g_curr + 1} /{imgBoardForm.g_img_paths.Count}";

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

                IAsyncResult result2 = handler.BeginInvoke(path, new AsyncCallback(CallBack), "one task done.");

            }
            else
            {
                _syncContext.Post(SetButtonText, "一键处理全部图片");//子线程中通过UI线程上下文更新UI
                MessageBox.Show("全部图片处理完成.");
            }

        }

        public imgRotateForm(string _imagePath, ws _w, IWebSocketConnection _conn)
        {

            InitializeComponent();

            line1.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            line1.BackColor = Color.Red;
            line1.Width = pictureBox1.Width;
            line1.Height = 2;
            line1.Cursor = Cursors.SizeNS;
            line1.MouseDown += new MouseEventHandler(this.pictureBox1_MouseDown);
            line1.MouseMove += new MouseEventHandler(this.pictureBox1_MouseMove);
            line1.MouseUp += new MouseEventHandler(this.pictureBox1_MouseUp);

            this.pictureBox1.Controls.Add(line1);
            w = _w;
            conn = _conn;
            loadImage(_imagePath);

            //获取UI线程同步上下文   
            _syncContext = SynchronizationContext.Current;
        }

        private void SetButtonText(object text)
        {
            this.button4.Text = text.ToString();
            if (text.ToString() == "一键处理全部图片")
            {
                this.button4.Enabled = true;

            }
        }


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


        void showImage()
        {
            using (var memoryStream = img.ToMemoryStream())
            {

                var image = Image.FromStream(memoryStream);
                this.pictureBox1.Image = image;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            showImage();
        }

        //左转
        private void button1_Click(object sender, EventArgs e)
        {
            rotate(angle);

            rotated = true;
        }

        //右转
        private void button2_Click(object sender, EventArgs e)
        {
            rotate(angle * -1);

            rotated = true;

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (!float.TryParse(textBox1.Text, out angle))
            {
                MessageBox.Show("请输入正确角度数值");
            }
        }

        private void imgRotateForm_Load(object sender, EventArgs e)
        {
            if (imagePath != "")
            {
                loadImage(imagePath);
            }
            this.lineY = this.pictureBox1.Height / 2;
            this.line1.Top = lineY + 10;
        }

        /// <summary>
        /// 旋转图片
        /// </summary>
        /// <param name="angle">角度</param>
        void rotate(float angle)
        {
            button1.Enabled = false;
            button2.Enabled = false;
            try
            {
                var newImg = Sample.matRotate(this.img, angle);
                this.img.Dispose();
                this.img = newImg;
                this.showImage();
            }
            catch (Exception)
            {
                MessageBox.Show("已到最大旋转角度");
                this.img = new Mat(imagePath);
                this.showImage();
            }

            button1.Enabled = true;
            button2.Enabled = true;
        }


        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void imgRotateForm_Paint(object sender, PaintEventArgs e)
        {

        }

        private void textBox2_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();

            ofd.Filter = "图像文件(*.jpg;*.gif;*.png;*.bmp)|*.jpg;*.gif;*.png;*.bmp;*.jpeg";
            ofd.Multiselect = true;
            var r = ofd.ShowDialog();
            if (r != DialogResult.OK)
            {
                return;
            }

            string[] arr = ofd.FileNames;

            listView1.Items.Clear();
            listView1.BeginUpdate();
            foreach (string path in arr)
            {
                string name = Path.GetFileName(path);
                ListViewItem lvi = new ListViewItem();
                lvi.Text = name;
                lvi.Tag = path;
                listView1.Items.Add(lvi);
            }
            listView1.EndUpdate();
            textBox2.Text = string.Join(";", arr);
        }


        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count == 0)
            {
                return;
            }
            loadImage(listView1.SelectedItems[0].Tag.ToString());
        }


        int startY = 0;
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {

            if (e.Y >= lineY - 5 && e.Y <= lineY + 5)
            {
                pictureBox1.Cursor = Cursors.SizeNS;
            }
            else
            {
                pictureBox1.Cursor = Cursors.Default;
            }
            if (startY != 0)
            {
                if (e.Y - startY != 0)
                {

                }
                lineY = startY + (e.Y - startY);
                line1.Top = lineY;
                if (this.Top < 10)
                {
                    this.Top = 10;
                }
            }
            else
            {
                return;
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            startY = e.Y;
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            startY = 0;
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            if (this.img == null)
            {
                return;
            }

            string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
            //保存到临时目录
            this.img.SaveImage(dist);

            this.img.Dispose();
            this.pictureBox1.Image.Dispose();
            Thread.Sleep(100);
            File.Delete(this.imagePath);
            Thread.Sleep(100);
            File.Move(dist, this.imagePath);

            string md5 = util.getFileMd5(this.imagePath);

            if (w != null && conn != null)
            {
                w.send(conn, new
                {
                    retType = "imgRotate",
                    data = new
                    {
                        path = this.imagePath,
                        md5 = md5
                    }
                });
                this.Close();
                return;
            }
            MessageBox.Show("保存成功");
            loadImage(imagePath);
        }

        private void imgRotateForm_KeyDown(object sender, KeyEventArgs e)
        {
            //ctrl+alt+上下调整水平线
            if (e.Shift && e.Alt && (e.KeyValue == 38 || e.KeyValue == 40))
            {
                lineY = e.KeyValue == 38 ? lineY - 2 : lineY + 2;
                this.line1.Top = lineY + 10;
            }
            //ctrl+s保存
            else if (e.Control && e.KeyCode == Keys.S)
            {
                this.button3_Click_1(null, null);
            }
            //ctrl+左右切换上下页
            else if (e.Control && (e.KeyValue == 37 || e.KeyValue == 39))
            {
                int idx = listView1.SelectedItems[0].Index;
                //左键
                if (e.KeyValue == 37 && idx - 1 > 0)
                {
                    idx--;
                }
                else if (e.KeyValue == 39 && idx + 1 < listView1.Items.Count)
                {
                    idx++;
                }
                else
                {
                    return;
                }
                listView1.SelectedItems.Clear();
                listView1.Items[idx].Selected = true;
                listView1.Items[idx].Focused = true;
                listView1.Items[idx].EnsureVisible();
                e.Handled = true;
            }
            //alt+上下调整角度大小
            else if (e.Alt && (e.KeyValue == 38 || e.KeyValue == 40))
            {
                angle = e.KeyValue == 38 ? angle + 0.1f : angle - 0.1f;
                textBox1.Text = angle.ToString();
            }
            //alt+左右键旋转
            else if (e.Alt && (e.KeyValue == 37 || e.KeyValue == 39))
            {
                if (e.KeyValue == 37)
                {
                    this.button1_Click(sender, e);
                }
                else
                {
                    this.button2_Click(sender, e);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (!this.rotated)
            {
                MessageBox.Show("请先旋转一张图片，之后其他所有图片都按同样的角度调整并保存");
                return;
            }

            if (listView1.Items.Count == 0)
            {
                return;
            }

            List<string> img_paths = new List<string>();
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                string path = listView1.Items[i].Tag.ToString();
                img_paths.Add(path);
            }

            imgBoardForm.g_img_paths = img_paths;

            this.button4.Enabled = false;

            calc_all(img_paths);   // 异步方法
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (this.img == null)
            {
                return;
            }

            string dist = $"{Directory.GetCurrentDirectory()}/rotate{DateTime.Now.ToString("yyyyMMddHHmmssfffff")}{Path.GetExtension(imagePath)}";
            //保存到临时目录
            this.img.SaveImage(dist);

            this.img.Dispose();
            this.pictureBox1.Image.Dispose();
            Thread.Sleep(100);
            File.Delete(this.imagePath);
            Thread.Sleep(100);
            File.Move(dist, this.imagePath);

            string md5 = util.getFileMd5(this.imagePath);

            if (w != null && conn != null)
            {
                w.send(conn, new
                {
                    retType = "imgRotate",
                    data = new
                    {
                        path = this.imagePath,
                        md5 = md5
                    }
                });
                this.Close();
                return;
            }
            MessageBox.Show("保存成功");
            loadImage(imagePath);
        }
    }
}

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





## 打开chrome

- https://blog.csdn.net/liuhuanping/article/details/118518795



# 单步调试 c++/cli dll 的方法



```

see E:\huggingface\WeChatOcr\sample\call_clr\call_clr.cpp

// 单步调试 c++/cli dll 的方法：
    // 前提：所有 dll 必须是 net481 往下（含）
	// 1. 把它设为启动项目 
	// 2. 项目属性中 -> 调试  命令填 E:\huggingface\WeChatOcr\x64\Debug\call_clr.exe 工作目录填 E:\huggingface\WeChatOcr\x64\Debug
    // call_clr.exe 是能正常调用这个 c++/cli dll 的程序

// 调用关系

// E:\huggingface\WeChatOcr\x64\Debug\call_clr.exe  -> 
    // E:\huggingface\WeChatOcr\x64\Debug\clr_wapper_net481.dll ->
        // E:\huggingface\WeChatOcr\src\WeChatOcr\bin\Debug\net481\WeChatOcr.dll ->
            // E:\lib\Google.Protobuf.dll
			// E:\lib\Newtonsoft.Json.dll

// 普通 C# 项目是这样 net8.0-windows;net7.0-windows;net6.0-windows;net481;net472




```



# 纯 C++ 调用 C# dll 成功案例

```
// huggingface\WeChatOcr\sample\call_clr\call_clr.cpp

/*


WeChatOcr -> 调试 -> 打开调试启动配置文件UI -> 创建新的配置 -> 可执行文件 E:\huggingface\WeChatOcr\x64\Debug\call_clr.exe -> 工作目录 E:\huggingface\WeChatOcr\x64\Debug

   -> WeChatOcr 设为启动项目 -> F5

   这样，c++/cli 和 C# dll 设置断点后都能断下来

*/

// 注意：此项目必须设置：调试 -> 工作目录为  E:\huggingface\WeChatOcr\x64\Debug ，这样才能正常调用 ocr dll ，并输出识别结果


// 重要：WeChatOcr 目标框架只有 net481 这一个时，将本项目也设为 net481，此时这个项目可以辅助 clr_wapper_net481 调试代码。但是识别是不成功的，
// WeChatOcr 设为 net8.0-windows ，ConsoleApp1 为 .net 8.0 ，能正常识别。

// see csharp summary.md -> C++/cli

// 单步调试 c++/cli dll 的方法：
    // 前提：所有 dll 必须是 net481 往下（含）
	// 1. 把它设为启动项目 
	// 2. 项目属性中 -> 调试  命令填 E:\huggingface\WeChatOcr\x64\Debug\call_clr.exe 工作目录填 E:\huggingface\WeChatOcr\x64\Debug
    // call_clr.exe 是能正常调用这个 c++/cli dll 的程序

// 调用关系

// E:\huggingface\WeChatOcr\x64\Debug\call_clr.exe  -> 
    // E:\huggingface\WeChatOcr\x64\Debug\clr_wapper_net481.dll ->
        // E:\huggingface\WeChatOcr\src\WeChatOcr\bin\Debug\net481\WeChatOcr.dll ->
            // E:\lib\Google.Protobuf.dll
			// E:\lib\Newtonsoft.Json.dll

// 普通 C# 项目是这样 net8.0-windows;net7.0-windows;net6.0-windows;net481;net472


#include <iostream>
#include <Windows.h>

// 声明函数指针类型
typedef const char* (*FunNativeFunc)(const char*);

int main()
{
    // 加载 DLL
    HMODULE hModule = LoadLibrary(L"E:\\huggingface\\WeChatOcr\\x64\\Debug\\clr_wapper_net80.dll");
    // HMODULE hModule = LoadLibrary(L"E:\\huggingface\\WeChatOcr\\x64\\Debug\\clr_wapper_net481.dll");  // 仅用于单步调试 c++/cli dll, clr_wapper_net481.dll，它需要用这个 exe 启动
    if (!hModule) {
        std::cerr << "无法加载 DLL，错误码: " << GetLastError() << std::endl;
        return 1;
    }

    // 获取函数地址
    FunNativeFunc funNative = (FunNativeFunc)GetProcAddress(hModule, "fun_native");
    if (!funNative) {
        std::cerr << "无法找到函数，错误码: " << GetLastError() << std::endl;
        FreeLibrary(hModule);
        return 1;
    }

    // 调用函数
    const char* result = funNative("E:\\huggingface\\WeChatOcr\\t2.jpg");
    if (result) {
        std::cout << "函数返回值: " << result << std::endl;
    } else {
        std::cout << "函数返回了空指针" << std::endl;
    }

    // 释放 DLL
    FreeLibrary(hModule);
    return 0;
}

```



```

// huggingface\WeChatOcr\src\clr_wapper_net80\clr_wapper_net80_2.cpp

#include "pch.h"

using namespace System;
using namespace WeChatOcr;

using namespace System::Reflection;
using namespace System::Collections::Generic;
using namespace System::Threading;
using namespace System::Threading::Tasks;
using namespace System::Reflection;
using namespace System::IO;
using namespace System::Runtime::CompilerServices;

#include <msclr/gcroot.h>


// 添加导出声明
extern "C" __declspec(dllexport) const char* fun_native(const char* args)
{
    // 将原生字符串转换为托管字符串
    String^ managedArgs = gcnew String(args);

    // 创建托管字符串数组
    array<String^>^ argsArray = gcnew array<String^>(1);
    argsArray[0] = managedArgs;

    // 设置DLL路径
    String^ dllPath = "E:\\huggingface\\WeChatOcr\\src\\WeChatOcr\\bin\\Debug\\net8.0\\WeChatOcr.dll"; // "E:\\huggingface\\WeChatOcr\\src\\WeChatOcr\\bin\\Debug\\net8.0-windows\\WeChatOcr.dll";
    String^ protobufPath = "E:\\lib\\Google.Protobuf.dll";
    String^ newtonsoftPath = "E:\\lib\\Newtonsoft.Json.dll";

    // 加载依赖DLL
    Assembly::LoadFrom(protobufPath);
    Assembly::LoadFrom(newtonsoftPath);

    // 加载主DLL
    Assembly^ assembly = Assembly::LoadFrom(dllPath);
    Type^ imageOcrType = assembly->GetType("WeChatOcr.ImageOcr");
    Type^ WchtrType = assembly->GetType("WeChatOcr.Wchtcr");

    // 获取 WeChatOcrResult 类型
    Type^ weChatOcrResultType = assembly->GetType("WeChatOcr.WeChatOcrResult");

    // 创建正确的 Action 泛型类型
    array<Type^>^ typeArgs = gcnew array<Type^>(2);
    typeArgs[0] = String::typeid;
    typeArgs[1] = weChatOcrResultType;
    Type^ actionGenericType = Type::GetType("System.Action`2")->MakeGenericType(typeArgs);

    // 获取 DisposeAsync 方法
    MethodInfo^ disposeAsyncMethod = imageOcrType->GetMethod("DisposeAsync");

    // 使用正确的参数类型获取方法
    array<Type^>^ paramTypes = gcnew array<Type^>(2);
    paramTypes[0] = String::typeid;
    paramTypes[1] = actionGenericType;
    MethodInfo^ runMethod = imageOcrType->GetMethod("Run", paramTypes);


    array<Type^>^ paramTypes2 = gcnew array<Type^>(1);
    paramTypes2[0] = String::typeid;
    MethodInfo^ recMethod = WchtrType->GetMethod("rec", paramTypes2);


    // 创建 ImageOcr 实例
    array<Object^>^ constructorArgs = gcnew array<Object^>(0);
    Object^ ocrInstance = Activator::CreateInstance(WchtrType, constructorArgs);

    //var ret = recMethod.Invoke(ocrInstance, new object[]{ "E:\\huggingface\\WeChatOcr\\t2.jpg" });


    // 调用 rec 方法
    array<Object^>^ recParams = gcnew array<Object^>(1);
    recParams[0] = managedArgs; // "E:\\huggingface\\WeChatOcr\\t2.jpg";
    String^ ret = safe_cast<String^>( recMethod->Invoke(ocrInstance, recParams) );


    // 将托管字符串转换为非托管字符串并返回
    // 注意：这里分配的内存需要在调用方负责释放，或者使用静态缓冲区
    // 使用静态变量保存转换后的字符串，防止函数返回后内存被释放
    static IntPtr ptrToNativeString;
    // 释放之前可能分配的内存
    if (ptrToNativeString != IntPtr::Zero) {
        System::Runtime::InteropServices::Marshal::FreeHGlobal(ptrToNativeString);
    }
    ptrToNativeString = System::Runtime::InteropServices::Marshal::StringToHGlobalAnsi(ret);
    return static_cast<const char*>(ptrToNativeString.ToPointer());

    //return 555;
}

```



```

// huggingface\WeChatOcr\src\WeChatOcr\Wchtcr.cs

using System.Threading.Tasks;

namespace WeChatOcr;

public class Wchtcr: IDisposable
{
    private TaskCompletionSource<string?>? _tcs;  // List<WeChatOcr.SingleResult>?

    public Wchtcr()
    {
        _tcs = new TaskCompletionSource<string?>();  // List<WeChatOcr.SingleResult>?
    }

    public void Dispose()
    {
        
    }

    public async Task<string?> rec_async(string pth_img)
    {
        try
        {
            byte[] bytes = null;

            using (FileStream stream = new FileStream(pth_img, FileMode.Open, FileAccess.Read))
            using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
            {
                bytes = reader.ReadBytes(Convert.ToInt32(stream.Length));
            }

            using var ocr = new WeChatOcr.ImageOcr();
            ocr.Run(bytes, (path, result) =>
            {
                //try
                //{
                //    if (System.IO.File.Exists(path))
                //        System.IO.File.Delete(path);
                //}
                //catch
                //{
                //    // ignore
                //}

                try
                {
                    if (result == null) return;
                    var list = result?.OcrResult?.SingleResult;
                    if (list == null)
                    {
                        _tcs.SetResult(null);
                        return;
                    }

                    var sb = new System.Text.StringBuilder();
                    for (var i = 0; i < list?.Count; i++)
                    {
                        if (list[i] is not { } item || string.IsNullOrEmpty(item.SingleStrUtf8))
                            continue;

                        sb.AppendLine(item.SingleStrUtf8);
                    }

                    _tcs.SetResult(sb.ToString());
                }
                catch (Exception ex)
                {
                    System.Diagnostics.Debug.WriteLine(ex.Message);
                    _tcs.SetResult(null);
                }
            });

            var timeoutTask = Task.Delay(3000);
            var completedTask = await Task.WhenAny(_tcs.Task, timeoutTask);

            if (completedTask == timeoutTask)
            {
                _tcs.SetCanceled();
                //throw new TimeoutException("WeChatOCR operation timed out.");
            }
            // 提取content的值
            var finalResult = await _tcs.Task;

            //ResultTb.Text = finalResult.Result;

            await ocr.DisposeAsync();

            return finalResult;

        }
        catch (Exception ex)
        {
            //ResultTb.Text = ex.Message;
            return null; //  ex.Message; 
        }
    }

    public string? rec(string pth_img)
    {
        // 重置TaskCompletionSource以确保每次调用都使用新的实例
        _tcs = new TaskCompletionSource<string?>();
        
        // 检查文件是否存在
        if (!System.IO.File.Exists(pth_img))
        {
            return $"文件不存在: {pth_img}";
        }
        
        try
        {
            var ret = Task.Run(async () => await rec_async(pth_img)).Result;
            return ret;
        }
        catch (Exception ex)
        {
            return $"错误: {ex.Message}";
        }
    }
}

```







# Call dll

```

# see huggingface\WeChatOcr\sample\ConsoleApp1\main_call_dll.cs

// Todo: 尝试直接调用 dll ，而不是引用项目
// E:\huggingface\WeChatOcr\src\WeChatOcr\bin\Debug\net8.0-windows\WeChatOcr.dll
// C:\Users\i\.nuget\packages\google.protobuf\3.29.3
// C:\Users\i\.nuget\packages\newtonsoft.json\13.0.3


using System.Runtime.InteropServices;
using System.Reflection;

var dllPath = @"E:\huggingface\WeChatOcr\src\WeChatOcr\bin\Debug\net8.0-windows\WeChatOcr.dll";
var protobufPath = @"E:\lib\Google.Protobuf.dll";
var newtonsoftPath = @"E:\lib\Newtonsoft.Json.dll";

// 加载依赖 DLL
Assembly.LoadFrom(protobufPath);
Assembly.LoadFrom(newtonsoftPath);

// 加载主 DLL
var assembly = Assembly.LoadFrom(dllPath);
var imageOcrType = assembly.GetType("WeChatOcr.ImageOcr");
var singleResultType = assembly.GetType("WeChatOcr.SingleResult");

async Task<List<object>?> wcht4_ocr(string pth)
{
    byte[] bytes = null;

    using (FileStream stream = new FileStream(pth, FileMode.Open, FileAccess.Read))
    using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
    {
        bytes = reader.ReadBytes(Convert.ToInt32(stream.Length));
    }

    var tcs = new TaskCompletionSource<List<object>?>();

    try
    {   
        // 创建 ImageOcr 实例，传入 null 作为默认路径
        var ocrInstance = Activator.CreateInstance(imageOcrType, new object?[] { null });
        //var runMethod = imageOcrType.GetMethod("Run");

        // 明确指定要使用的 Run 方法重载
        //var runMethod = imageOcrType.GetMethod("Run", new Type[] { typeof(byte[]), typeof(Action<string, object>) });


        // 获取 WeChatOcrResult 类型
        var weChatOcrResultType = assembly.GetType("WeChatOcr.WeChatOcrResult");

        // 创建正确的 Action 泛型类型
        var actionType = typeof(Action<,>).MakeGenericType(typeof(string), weChatOcrResultType);

        // 获取 DisposeAsync 方法
        var disposeAsyncMethod = imageOcrType.GetMethod("DisposeAsync");
        // 使用正确的参数类型获取方法
        var runMethod = imageOcrType.GetMethod("Run", new Type[] { typeof(string), actionType });

        // 创建回调委托
        var callback = new Action<string, Object>((path, result) =>
        {
            //try
            //{
            //    if (System.IO.File.Exists(path))
            //        System.IO.File.Delete(path);
            //}
            //catch
            //{
            //    // ignore
            //}

            try
            {
                if (result == null) return;
                
                // 通过反射获取 OcrResult 和 SingleResult
                var ocrResultProp = result.GetType().GetProperty("OcrResult");
                var ocrResult = ocrResultProp?.GetValue(result);

                if (ocrResult == null)
                {
                    tcs.SetResult(null);
                    return;
                }

                var resultList = new List<object> { ocrResult };

                tcs.SetResult(resultList);

            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine(ex.Message);
            }
        });

        // 调用 Run 方法
        runMethod.Invoke(ocrInstance, new object[] { pth, callback });

        var timeoutTask = Task.Delay(9000);
        var completedTask = await Task.WhenAny(tcs.Task, timeoutTask);

        if (completedTask == timeoutTask)
        {
            tcs.SetCanceled();
        }

        var finalResult = await tcs.Task;

        // 调用 DisposeAsync 方法
        await (Task)disposeAsyncMethod.Invoke(ocrInstance, null);

        return finalResult;
    }
    catch (Exception ex)
    {
        System.Diagnostics.Debug.WriteLine(ex.Message);
        return null;
    }
}

var ret = await wcht4_ocr("E:\\huggingface\\WeChatOcr\\t2.jpg");
if (ret != null && ret.Count > 0)
{
    // 将 ret[0] 转换为 OcrResult 类型
    var ocrResult = ret[0];
    // 通过反射获取 SingleResult 属性
    var singleResultProp = ocrResult.GetType().GetProperty("SingleResult");
    var singleResults = singleResultProp?.GetValue(ocrResult) as IEnumerable<object>;
    
    if (singleResults != null)
    {
        string t = "";
        foreach (var item in singleResults)
        {
            // 获取 SingleStrUtf8 和 OneResult 属性值
            var line = item.GetType().GetProperty("SingleStrUtf8")?.GetValue(item) as string;
            var Left = item.GetType().GetProperty("Left")?.GetValue(item);
            var Right = item.GetType().GetProperty("Right")?.GetValue(item);
            var Bottom = item.GetType().GetProperty("Bottom")?.GetValue(item);
            var Top = item.GetType().GetProperty("Top")?.GetValue(item);

            t += $"[{Left} {Top} {Right} {Bottom}] {line}\n";
            
            var oneResult = item.GetType().GetProperty("OneResult")?.GetValue(item) as IEnumerable<object>;
            if (oneResult != null)
            {
                foreach (var itm in oneResult)
                {
                    var word = itm.GetType().GetProperty("SingleStrUtf8")?.GetValue(item) as string;
                    var Lft = itm.GetType().GetProperty("Left")?.GetValue(itm);
                    var Rght = itm.GetType().GetProperty("Right")?.GetValue(itm);
                    var Bttom = itm.GetType().GetProperty("Bottom")?.GetValue(itm);
                    var Tp = itm.GetType().GetProperty("Top")?.GetValue(itm);

                }
            }
            
        }

        Console.WriteLine(t);
    }
}

Console.WriteLine("Hello, World!");

```



```

// 以上代码 C++/cli 对等翻译
// see E:\huggingface\WeChatOcr\src\clr_wapper_net481\clr_wapper_net481.cpp

using namespace System;
using namespace WeChatOcr;

using namespace System::Reflection;
using namespace System::Collections::Generic;
using namespace System::Threading;
using namespace System::Threading::Tasks;
using namespace System::Reflection;
using namespace System::IO;
using namespace System::Runtime::CompilerServices;

#include <msclr/gcroot.h>

namespace iocr {

    // 异步方法辅助函数
    ref class TaskAwaiter
    {
    private:
        Task^ task;

    public:
        TaskAwaiter(Task^ t) : task(t) {}

        void GetResult() {
            task->Wait();
        }
    };

    // 创建回调函数对象类
    ref class OcrCallback
    {
    private:
        TaskCompletionSource<List<Object^>^>^ tcs;

    public:
        OcrCallback(TaskCompletionSource<List<Object^>^>^ taskSource) : tcs(taskSource) {}

        void HandleCallback(String^ path, Object^ result)
        {
            try
            {
                if (result == nullptr) return;

                // 通过反射获取 OcrResult 和 SingleResult
                PropertyInfo^ ocrResultProp = result->GetType()->GetProperty("OcrResult");
                Object^ ocrResult = ocrResultProp != nullptr ? ocrResultProp->GetValue(result) : nullptr;

                if (ocrResult == nullptr)
                {
                    tcs->SetResult(nullptr);
                    return;
                }

                List<Object^>^ resultList = gcnew List<Object^>();
                resultList->Add(ocrResult);

                tcs->SetResult(resultList);
            }
            catch (Exception^ ex)
            {
                System::Diagnostics::Debug::WriteLine(ex->Message);
            }
        }
    };

    int fun(array<System::String^>^ args)
    {
        // 创建TaskCompletionSource
        auto tcs = gcnew TaskCompletionSource<List<Object^>^>();

        // 设置DLL路径
        String^ dllPath = "E:\\huggingface\\WeChatOcr\\src\\WeChatOcr\\bin\\Debug\\net481\\WeChatOcr.dll"; // "E:\\huggingface\\WeChatOcr\\src\\WeChatOcr\\bin\\Debug\\net8.0-windows\\WeChatOcr.dll";
        String^ protobufPath = "E:\\lib\\Google.Protobuf.dll";
        String^ newtonsoftPath = "E:\\lib\\Newtonsoft.Json.dll";

        // 加载依赖DLL
        Assembly::LoadFrom(protobufPath);
        Assembly::LoadFrom(newtonsoftPath);

        // 加载主DLL
        Assembly^ assembly = Assembly::LoadFrom(dllPath);
        Type^ imageOcrType = assembly->GetType("WeChatOcr.ImageOcr");
        Type^ singleResultType = assembly->GetType("WeChatOcr.SingleResult");

        // 创建 ImageOcr 实例，传入 null 作为默认路径
        array<Object^>^ constructorArgs = gcnew array<Object^>(1);
        constructorArgs[0] = nullptr; // 相当于C#中的null
        Object^ ocrInstance = Activator::CreateInstance(imageOcrType, constructorArgs);

        // 获取 WeChatOcrResult 类型
        Type^ weChatOcrResultType = assembly->GetType("WeChatOcr.WeChatOcrResult");

        // 创建正确的 Action 泛型类型
        array<Type^>^ typeArgs = gcnew array<Type^>(2);
        typeArgs[0] = String::typeid;
        typeArgs[1] = weChatOcrResultType;
        Type^ actionGenericType = Type::GetType("System.Action`2")->MakeGenericType(typeArgs);

        // 获取 DisposeAsync 方法
        MethodInfo^ disposeAsyncMethod = imageOcrType->GetMethod("DisposeAsync");

        // 使用正确的参数类型获取方法
        array<Type^>^ paramTypes = gcnew array<Type^>(2);
        paramTypes[0] = String::typeid;
        paramTypes[1] = actionGenericType;
        MethodInfo^ runMethod = imageOcrType->GetMethod("Run", paramTypes);


        // 在lambda中使用gcroot包装托管对象
        msclr::gcroot<TaskCompletionSource<List<Object^>^>^> tcsRoot = tcs;


        // 创建回调对象和委托
        OcrCallback^ callbackObj = gcnew OcrCallback(tcs);
        Action<String^, Object^>^ callback = gcnew Action<String^, Object^>(callbackObj, &OcrCallback::HandleCallback);


        // 调用 Run 方法
        array<Object^>^ runParams = gcnew array<Object^>(2);
        runParams[0] = "E:\\huggingface\\WeChatOcr\\t2.jpg";
        runParams[1] = callback;
        runMethod->Invoke(ocrInstance, runParams);

        // 创建超时任务
        Task^ timeoutTask = Task::Delay(9000);

        // 等待任务完成或超时
        array<Task^>^ tasks = gcnew array<Task^>(2);
        tasks[0] = tcs->Task;
        tasks[1] = timeoutTask;
        Task^ completedTask = Task::WhenAny(tasks)->Result;

        if (completedTask == timeoutTask)
        {
            tcs->SetCanceled();
        }

        // 获取最终结果
        List<Object^>^ finalResult = dynamic_cast<Task<List<Object^>^>^>(tcs->Task)->Result;

        // 调用 DisposeAsync 方法
        Task^ disposeTask = dynamic_cast<Task^>(disposeAsyncMethod->Invoke(ocrInstance, nullptr));
        disposeTask->Wait();

        return 0;
    }

    // 添加导出声明
    extern "C" __declspec(dllexport) int fun_native(const char* args)
    {
        // 将原生字符串转换为托管字符串
        String^ managedArgs = gcnew String(args);

        // 创建托管字符串数组
        array<String^>^ argsArray = gcnew array<String^>(1);
        argsArray[0] = managedArgs;

        // 调用托管函数
        return fun(argsArray);
    }
}
```





```


// 需要先引用项目

//using SingleResult = WeChatOcr.SingleResult;


//async Task<List<SingleResult>?> wcht4_ocr(string pth)
//{
//    byte[] bytes = null;

//    using (FileStream stream = new FileStream(pth, FileMode.Open, FileAccess.Read))
//    using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
//    {
//        bytes = reader.ReadBytes(Convert.ToInt32(stream.Length));
//    }

//    TaskCompletionSource<List<SingleResult>?>? _tcs;

//    _tcs = new TaskCompletionSource<List<SingleResult>?>();

//    try
//    {
//        //var bytes = ImageUtilities.ConvertBitmap2Bytes(bitmap, ImageFormat.Png);
//        using var ocr = new WeChatOcr.ImageOcr();
//        ocr.Run(bytes, (path, result) =>
//        {
//            try
//            {
//                if (System.IO.File.Exists(path))
//                    System.IO.File.Delete(path);
//            }
//            catch
//            {
//                // ignore
//            }

//            try
//            {
//                if (result == null) return;
//                var list = result?.OcrResult?.SingleResult;
//                if (list == null)
//                {
//                    //避免重复set
//                    //_tcs.SetResult("WeChatOCR get result is null");
//                    _tcs.SetResult(null);
//                    return;
//                }

//                _tcs.SetResult(list);


//                var sb = new System.Text.StringBuilder();
//                for (var i = 0; i < list?.Count; i++)
//                {
//                    if (list[i] is not { } item || string.IsNullOrEmpty(item.SingleStrUtf8))
//                        continue;

//                    sb.AppendLine(item.SingleStrUtf8);
//                }



//                //_tcs.SetResult(sb.ToString());
//            }
//            catch (Exception ex)
//            {
//                System.Diagnostics.Debug.WriteLine(ex.Message);
//            }
//        });

//        var timeoutTask = Task.Delay(3000);
//        var completedTask = await Task.WhenAny(_tcs.Task, timeoutTask);

//        if (completedTask == timeoutTask)
//        {
//            _tcs.SetCanceled();
//            //throw new TimeoutException("WeChatOCR operation timed out.");
//        }
//        // 提取content的值
//        var finalResult = await _tcs.Task;

//        //ResultTb.Text = finalResult.Result;

//        await ocr.DisposeAsync();

//        return finalResult;

//    }
//    catch (Exception ex)
//    {
//        //ResultTb.Text = ex.Message;
//        return null; //  ex.Message; 
//    }
//}


//var ret = await wcht4_ocr("E:\\t\\wchtcr\\t2.jpg");

//Console.WriteLine("Hello, World!");

```



## C++/cli



- 不支持编译为可执行文件 ：C++/CLI项目在.NET Core/.NET 5+环境下只能编译为DLL，不能编译为可执行文件（EXE）。
- 仅支持Windows平台 ：C++/CLI对.NET的支持仅限于Windows系统。
- 不支持SDK风格的项目文件 ：C++/CLI项目不使用新的SDK风格项目文件格式，而是继续使用.vcxproj格式。



```

公共语言运行时 .NET 运行时支持(/clr:netcore)

目标框架 .NET 8.0
	# 普通 C# 项目是这样 net8.0-windows;net7.0-windows;net6.0-windows;net481;net472


#include "pch.h"

using namespace System;

int main(array<System::String ^> ^args)
{
    return 0;
}


```



### 调用 C# dll

```
using namespace System;
using namespace System::Reflection;

namespace iocr {

    int fun(array<System::String^>^ args)
    {
        // 设置DLL路径
        String^ dllPath = "E:\\huggingface\\WeChatOcr\\src\\WeChatOcr\\bin\\Debug\\net8.0-windows\\WeChatOcr.dll";
        String^ protobufPath = "E:\\lib\\Google.Protobuf.dll";
        String^ newtonsoftPath = "E:\\lib\\Newtonsoft.Json.dll";
        
        // 加载依赖DLL
        Assembly::LoadFrom(protobufPath);
        Assembly::LoadFrom(newtonsoftPath);
        
        // 加载主DLL
        Assembly^ assembly = Assembly::LoadFrom(dllPath);
        Type^ imageOcrType = assembly->GetType("WeChatOcr.ImageOcr");
        Type^ singleResultType = assembly->GetType("WeChatOcr.SingleResult");
        
        return 0;
    }

    // 添加导出声明
    extern "C" __declspec(dllexport) int fun_native(const char* args)
    {
        // 将原生字符串转换为托管字符串
        String^ managedArgs = gcnew String(args);
        
        // 创建托管字符串数组
        array<String^>^ argsArray = gcnew array<String^>(1);
        argsArray[0] = managedArgs;
        
        // 调用托管函数
        return fun(argsArray);
    }
}
```



```

普通 cpp 调用 c++/cli 的 dll

#include <iostream>
#include <Windows.h>

using namespace iocr;

// 声明函数指针类型
//typedef int (*FunNativeFunc)(const char*);

int main()
{
	//iocr::fun_native("");

    //// 加载 DLL
    //HMODULE hModule = LoadLibrary(L"E:\\t\\Project2\\x64\\Debug\\clr_dll.dll");
    //if (!hModule) {
    //    std::cerr << "无法加载 DLL，错误码: " << GetLastError() << std::endl;
    //    return 1;
    //}

    //// 获取函数地址
    //FunNativeFunc funNative = (FunNativeFunc)GetProcAddress(hModule, "fun_native");
    //if (!funNative) {
    //    std::cerr << "无法找到函数，错误码: " << GetLastError() << std::endl;
    //    FreeLibrary(hModule);
    //    return 1;
    //}

    //// 调用函数
    //int result = funNative("测试参数");
    //std::cout << "函数返回值: " << result << std::endl;

    //// 释放 DLL
    //FreeLibrary(hModule);
    return 0;
}
```







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

  - https://github.com/nodejs/node/blob/v18.12.1/test/embedding/embedtest.cc  

    > 编译18.12.1 应该就可以运行下面的代码了

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



## python



### C# 调用 python dll

- https://blog.51cto.com/u_15221047/2807071





# 网络请求



## Downloader

- https://github.com/bezzad/Downloader

```
                void OnDownloadStarted(object sender, DownloadStartedEventArgs e)
                {
                    var fname = $"Downloading {Path.GetFileName(e.FileName)}";
                }

                void OnDownloadFileCompleted(object sender, AsyncCompletedEventArgs e)
                {
                    if (e.Cancelled)
                    {
                    }
                    else if (e.Error != null)
                    {

                    }
                    else
                    {
                        // 下载完成
                    }

                }


                //
                // 开始下载文件
                //
                var downloadOpt = new DownloadConfiguration()
                {
                    ChunkCount = 1, // file parts to download, default value is 1
                    OnTheFlyDownload = false, // caching in-memory or not? default values is true
                    ParallelDownload = false // download parts of file as parallel or not. Default value is false
                };
                var downloader = new DownloadService(downloadOpt);
                downloader.DownloadStarted += OnDownloadStarted;
                downloader.DownloadFileCompleted += OnDownloadFileCompleted;
                
                
                
                    await downloader.DownloadFileTaskAsync(fileURL, dst); 
                    
                    // await downloader.DownloadFileTaskAsync("https://xxx.oss-cn-hangzhou.aliyuncs.com/tk_ppt/487937/73234/123.pptx", @"G:\123.pptx");

```





## RestSharp

```
using RestSharp;

            string code = @"
                console.log(fs)  // fs 是事先 import 好的模块，这里可以直接用  所有可用参数都在这里展开了：  ...params
                console.log('hello, from vm')
                return callback({ msg:'hi,,,' }) // 约定最后以 callback 返回值
            ";

            string imports = @"
                [""fs""]
            ";

            try
            {
                var client = new RestClient("http://127.0.0.1:8880/vm/vmrun");
                var request = new RestRequest();
                request.Method = Method.Post;
                request.Timeout = 5000;
                request.AddHeader("content-type", "application/x-www-form-urlencoded;charset=UTF-8");
                request.AddParameter("application/x-www-form-urlencoded", $"code={WebUtility.UrlEncode(code)}&imports={WebUtility.UrlEncode(imports)}", ParameterType.RequestBody);

                var response = client.Execute(request);
                string data = response.Content;
                int a = 1;
            }
            catch (Exception ex)
            {
                int b = 1;
            }

```



```
/// <summary>
        /// Post提交
        /// </summary>
        /// <param name="url">提交地址</param>
        /// <param name="content">提交的Post信息</param>
        /// <param name="contentType">提交信息格式类型</param>
        /// <returns></returns>
        public static string HttpPost(string url, string content, string contentType)
        {
            try
            {
                var client = new RestClient(url);
                var request = new RestRequest();
                request.Method = Method.Post;
                request.Timeout = 5000;
                request.AddParameter(contentType, content, ParameterType.RequestBody);
                var response = client.Execute(request);
                return response.Content;
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }
        }
        
        
         /// <summary>
        /// Get提交
        /// </summary>
        /// <param name="url">提交地址</param>
        /// <returns></returns>
        public static string HttpGet(string url)
        {
            try
            {
                var client = new RestClient(url);
                var request = new RestRequest();
                request.Method = Method.Get;
                request.Timeout = 5000;
                request.AddHeader("content-type", "text/html; charset=utf-8");
                request.AddHeader("content-encoding", "gzip");
                var response = client.Execute(request);
                return response.Content;
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }
        }
```





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



## RichTextBox

https://github.com/cuikp/AvRichTextBox 替代方案



- ### **RichTextBox控件的常用事件** [u](https://www.cnblogs.com/yeshenmeng/p/9435398.html)

  1. SelectionChange事件——控件中选中的文本发生改变时，触发该事件。 
  2. TextChanged事件——控件中的文本内容发生改变时，触发该事件。

- ##### winform中单个RichTextBox实现鼠标右键(剪切，复制，粘贴)功能  [u](https://blog.csdn.net/Pei_hua100/article/details/123402342)



```
private static void InitRichTextBoxContextMenu(RichTextBox textBox)
        {
            //创建剪切子菜单
 
            var cutMenuItem = new System.Windows.Forms.MenuItem("剪切");
 
            cutMenuItem.Click += (sender, eventArgs) => textBox.Cut();
 
            //创建复制子菜单
 
            var copyMenuItem = new System.Windows.Forms.MenuItem("复制");
 
            copyMenuItem.Click += (sender, eventArgs) => textBox.Copy();
 
            //创建粘贴子菜单
 
            var pasteMenuItem = new System.Windows.Forms.MenuItem("粘贴");
 
            pasteMenuItem.Click += (sender, eventArgs) => textBox.Paste();
 
            //创建右键菜单并将子菜单加入到右键菜单中
 
            var contextMenu = new ContextMenu();
 
            contextMenu.MenuItems.Add(cutMenuItem);
 
            contextMenu.MenuItems.Add(copyMenuItem);
 
            contextMenu.MenuItems.Add(pasteMenuItem);
 
            textBox.ContextMenu = contextMenu;
 
        }

```





```
// SelectionChange 事件没找到，用这个替代方法也能达到目的

        private string selectText = "";

        public Form1()
        {
            InitializeComponent();

            this.richTextBox1.HideSelection = false; // Keep the selection highlighted, even after textbox loses focus.
        }

        private void richTextBox1_MouseUp(object sender, MouseEventArgs e)
        {
            
            if (e.Button == MouseButtons.Right)
            {
                if (this.selectText != this.richTextBox1.SelectedText)
                {
                    this.selectText = this.richTextBox1.SelectedText;
                }
            }

        }

```



```
private void richTextBox1_SelectionChanged(object sender, EventArgs e)
{
  textBox1.Text = richTextBox1.SelectedText;
}
```



```
// 右键菜单
	public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            richTextBox1.Text = "清音俗世留 纷争几时休\n" + "若能破名利 太虚任遨游";
        }

        private void copy_Click(object sender, EventArgs e)//复制
        {
            richTextBox1.Copy();
        }

        private void undo_Click(object sender, EventArgs e)//取消
        {
            if (richTextBox1.CanUndo)
            {
                richTextBox1.Undo();
            }
        }

        private void selectall_Click(object sender, EventArgs e)//全选
        {
            richTextBox1.SelectAll();
        }

        private void delete_Click(object sender, EventArgs e)//清除
        {
            richTextBox1.Clear();
        }

        private void paste_Click(object sender, EventArgs e)//粘贴
        {       
           if ( (richTextBox1.SelectionLength>0)&&(MessageBox.Show("是否覆盖选中的文本?", "覆盖", MessageBoxButtons.YesNo) == DialogResult.No))
                richTextBox1.SelectionStart = richTextBox1.SelectionStart + richTextBox1.SelectionLength;
            richTextBox1.Paste();
        }

        private void clip_Click(object sender, EventArgs e)//剪切
        {
            richTextBox1.Cut();
        }

        private void redo_Click(object sender, EventArgs e)//重做
        {
            if (richTextBox1.CanRedo)
                richTextBox1.Redo();
        }

        private void richTextBox1_MouseUp(object sender, MouseEventArgs e)//控制右键菜单的显示
        {
            if (e.Button == MouseButtons.Right)
            {
                if (richTextBox1.CanRedo)//redo
                    redo.Enabled = true;
                else
                    redo.Enabled = false;
                if (richTextBox1.CanUndo)//undo
                    undo.Enabled = true;
                else
                    undo.Enabled = false;
                if (richTextBox1.SelectionLength > 0)
                {
                    copy.Enabled = true;
                    clip.Enabled = true;
                }
                else
                {
                    copy.Enabled = false;
                    clip.Enabled = false;
                }
                if (Clipboard.GetDataObject().GetDataPresent(DataFormats.Text))
                    paste.Enabled = true;
                else
                    paste.Enabled = false;
                contextMenuStrip1.Show(richTextBox1, new Point(e.X, e.Y));
            }
        }
    }
```





# WPF

- https://github.com/dotnet/wpf/blob/main/src/Microsoft.DotNet.Wpf/src/PresentationFramework/ref/PresentationFramework.cs  

  - // C:\Program Files\dotnet\packs\Microsoft.WindowsDesktop.App.Ref\6.0.36\ref\net6.0\PresentationFramework.dll  是不是这个的源码

  - ```
    namespace System.Windows.Controls
        public class RichTextBox
        	# RichTextBox 在这个命名空间里面
    ```

  - https://www.cnblogs.com/wuty/p/18607430 wpf 源码编译

    - https://blog.lindexi.com/post/%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA-WPF-%E5%AE%98%E6%96%B9%E5%BC%80%E6%BA%90%E6%A1%86%E6%9E%B6%E6%BA%90%E4%BB%A3%E7%A0%81.html  wpf 源码编译

- https://github.com/dnSpyEx/dnSpy  .net 反编译



## WPF 源码编译

https://github.com/dotnet/wpf/blob/main/Documentation/developer-guide.md  **必看** 编译指南

```

win11 + visual studio 2025 preview

C:\Users\Administrator\wpf\.dotnet\sdk\9.0.100-alpha.1.23615.4 复制到
  C:\Users\Administrator\wpf\.dotnet\sdk
	# 这样复制

C:\Users\Administrator\wpf\packaging\Directory.Build.props
  <PropertyGroup>
    
    <!-- 添加以下属性以支持调试符号 -->
    <DebugType>portable</DebugType>
    <DebugSymbols>true</DebugSymbols>
    <EmbedAllSources>true</EmbedAllSources>
    <IncludeSymbols>true</IncludeSymbols>

  </PropertyGroup>
  	 # 让生成的 nuget 包带调试符号 
  

dotnet --list-sdks
9.0.200 [C:\Program Files\dotnet\sdk]
	# wpf\src\Microsoft.DotNet.Wpf\src\System.Xaml
	# 单独编译这个项目时，把 wpf\global.json 里的 sdk 改成 9.0.200

	https://builds.dotnet.microsoft.com/dotnet/Sdk/9.0.200/dotnet-sdk-9.0.200-win-x64.zip
		# 这里下载
		# C:\Users\Administrator\wpf\.dotnet\sdk\9.0.100-alpha.1.23615.4
			# 原始依赖它是放这里


C:\Users\Administrator\wpf\.editorconfig
[*.cs]
dotnet_diagnostic.CA2022.severity = none
dotnet_diagnostic.CA2265.severity = none
dotnet_diagnostic.CA2668.severity = none
	# 改成 9.0.200 后，这里加一行

依赖树：
wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Controls\RichTextBox.cs # RichTextBox 代码在这
	
wpf\src\Microsoft.DotNet.Wpf\src\System.Xaml
	wpf\src\Microsoft.DotNet.Wpf\src\System.Xaml\ref


C:\Users\Administrator\wpf
	# 源码本来是放在这里编译的，如果移动路径可能会编译失败

git clone https://github.com/dotnet/wpf
切到 v6.0.36 分支, RichTextBox 控件 dll 显示使用的是这个版本

LINK : fatal error LNK1104: 无法打开文件“MSVCURTD_netcore.LIB”
	# 安装 c++ cli 
		对v143 生成工具(最新)的 C++/CLI 支持
			对v141 生成工具(14.16)的 C++/CLI 支持
            14.40-17.10
            14.42-17.12
                # 实测这三个不需要安装

用他的 wpf fork 看看能不能成功
	# https://github.com/Dotnet9527/wpf
		# 这个 fork

C:\Users\Administrator\.netcoreeng\native\temp
	# 看看总共下载了几个压缩包


File 'C:\Users\echod\.netcoreeng\native\temp\strawberry-perl-5.38.0.1-win64-x64.zip' already exists, skipping download
E:\t\wpf_fork\wpf\.tools\bin\net-framework-48-ref-assemblies
	# 下载的东西藏在这里，存起来


https://github.com/dotnet/wpf/issues/8343

.\build.cmd -clean
	# 失败以后先 clean
.\build.cmd -pack -ci -configuration Debug -prepareMachine /p:Platform=x86
	.\build.cmd -pack -ci -configuration Debug -prepareMachine /p:Platform=x64 /p:EnableNuGetAudit=false

工程属性页中“Alt+F7”－>“配置属性”－>“C/C++”－>“常规”－>“调试信息格式”，选择“用于“编辑并继续”的程序数据库(/ZI)”。另外，在“配置属性”－>“链接器”－>“调试”－>“生成调试信息”中，选择“是”。

工具->选项->调试->常规，将”要求源文件与原始版本完全匹配”

clear the .tools\native\bin subfolder of the git repo (alternatively try a fresh clone)
C:\Users\<user>\.netcoreeng\native\temp contains download caches (remove individual files if the zip file is partially downloaded or otherwise broken)
C:\Users\<user>\.netcoreeng\native\bin contains unpacked downloads (remove if you suspect unpacking was interrupted/failed)
	# 下载缓存也可以清一下


wpf\src\Microsoft.DotNet.Wpf\src\System.Printing\CPP\src\PrintSystemPathResolver.cpp(308,50): er
ror C5307: 'int System::String::IndexOf(wchar_t,int)': argument (1) converted from 'char' to 'wchar_t'. Missing 'L' enc
oding-prefix for character literal?
	# 装完 cli 以后只有一个错误
	# 14.39 14.40 14.41 14.42 14.44 Latest 这几个全装了，有效的应该是前面几个？
	# 后面先不装，一个个试
		# 308 417 473 行 加一个 L 后成功编译

命令行编译成功
C:\Users\Administrator\wpf\artifacts\packages\Debug\NonShipping
Microsoft.DotNet.Arcade.Wpf.Sdk.Debug.9.0.0-ci.nupkg
Microsoft.DotNet.Wpf.GitHub.Debug.9.0.0-ci.nupkg
Microsoft.DotNet.Wpf.ProjectTemplates.Debug.9.0.0-ci.nupkg
Microsoft.NET.Sdk.WindowsDesktop.Debug.9.0.0-ci.nupkg
runtime.win-x86.Microsoft.DotNet.Wpf.GitHub.Debug.9.0.0-ci.nupkg
	# 生成这五个包
	
C:\Users\Administrator\wpf\.packages
	# 它的依赖包在这里，自定义 RichTextBox 时可以引用它
	

新建一个控制台程序 选 .net9.0 ，选 x86 编译 
  <ItemGroup>
    <PackageReference Include="Microsoft.DotNet.Wpf.GitHub.Debug" Version="9.0.0-ci" />
    <PackageReference Include="Microsoft.DotNet.Wpf.ProjectTemplates.Debug" Version="9.0.0-ci" />
    <PackageReference Include="runtime.win-x86.Microsoft.DotNet.Wpf.GitHub.Debug" Version="9.0.0-ci" />
  </ItemGroup>
  	# 引用这些自已编译的 wpf 包
  	# NUGet 要先添加本地文件夹的源


wpf\src\Microsoft.DotNet.Wpf\src\DirectWriteForwarder\DirectWriteForwarder.vcxproj : error  : The SDK 'Microsoft.DotNet.Arcade.Sdk' specified could not be found. 
	# 直接打开解决方案报错


https://github.com/dotnet/wpf/blob/main/Documentation/wpf.vsconfig

{
  "version": "1.0",
  "components": [
    "Microsoft.Component.CodeAnalysis.SDK",
    "Microsoft.Component.MSBuild",
    "Microsoft.Component.VC.Runtime.UCRTSDK",
    "Microsoft.Net.Component.4.6.2.SDK",
    "Microsoft.Net.Component.4.7.2.TargetingPack",
    "Microsoft.NetCore.Component.DevelopmentTools",
    "Microsoft.NetCore.Component.SDK",
    "Microsoft.VisualStudio.Component.Git",
    "Microsoft.VisualStudio.Component.NuGet",
    "Microsoft.VisualStudio.Component.Roslyn.Compiler",
    "Microsoft.VisualStudio.Component.Roslyn.LanguageServices",
    "Microsoft.VisualStudio.Component.TextTemplating",
    "Microsoft.VisualStudio.Component.VC.ATL",
    "Microsoft.VisualStudio.Component.VC.ATLMFC",
    "Microsoft.VisualStudio.Component.VC.CLI.Support",
    "Microsoft.VisualStudio.Component.VC.CoreIde",
    "Microsoft.VisualStudio.Component.VC.Modules.x86.x64",
    "Microsoft.VisualStudio.Component.VC.Redist.14.Latest",
    "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
    "Microsoft.VisualStudio.Component.VSSDK",
    "Microsoft.VisualStudio.Component.Windows10SDK.19041"
  ]
}
	# 可能要装完这些东西


wpf\src\Microsoft.DotNet.Wpf\src\WpfGfx\core\dll\WpfGfx.sln  这个项目的C++的代码用到的是
 版本，装它

.\build.cmd -pack -ci -configuration Debug -prepareMachine /p:Platform=x86




```



### 编译后包的使用



```

C:\Users\Administrator\wpf\.dotnet\sdk\9.0.100-alpha.1.23615.4 复制到
  C:\Users\Administrator\wpf\.dotnet\sdk
	# 这样复制

C:\Users\Administrator\wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework
	# 项目改成控制台类型
	
# main.cs 新增文件 
using System;
namespace PresentationFramework
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("######### Test Modify code. this comiple from wpf souce code!!!");
        }
    }
}
	# 成功运行并进入断点
	
	
```





```
wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Application.cs

        static Application()
        {
            ApplicationInit();
            Console.log("######### Test Modify code. this comiple from wpf souce code!!!");
        }
			# 这里加调试输出，证明是我们自已编译的


E:\localNuget
	# 生成的五个包放这里
	
创建一个控制台程序，注意：编译出来的是基于.Net9.0的，所以依赖的版本是基于net9.0，TargetFramework 需要选择windows，才能用到wpf。由于本地编译的wpf框架是基于x86的，所以 Platforms 选择 x86

C:\Users\Administrator\wpf\packaging\Directory.Build.props
  <PropertyGroup>
    
    <!-- 添加以下属性以支持调试符号 -->
    <DebugType>portable</DebugType>
    <DebugSymbols>true</DebugSymbols>
    <EmbedAllSources>true</EmbedAllSources>
    <IncludeSymbols>true</IncludeSymbols>

  </PropertyGroup>
  	 # 让生成的 nuget 包带调试符号 

vs2025 preview Nuget包源，添加 E:\localNuget，名称 localNuget


引用本地编译的 wpf nuget包 

<Project Sdk="Microsoft.NET.Sdk">
	<PropertyGroup>
		<OutputType>WinExe</OutputType>
		<TargetFramework>net9.0-windows</TargetFramework>
		<ImplicitUsings>enable</ImplicitUsings>
		<Nullable>enable</Nullable>
		<UseWPF>true</UseWPF>
		<Platforms>x86</Platforms>
	</PropertyGroup>
	<PropertyGroup>
		<WpfRepoRoot>C:\Users\Administrator\wpf</WpfRepoRoot>
	</PropertyGroup>
	<Import Project="$(WpfRepoRoot)\eng\wpf-debug.targets" />
</Project>
	# 这样也可以，比较简单
	# F11 其实是能进入源码的，但是必须从外面下断再单步进去，wpf 源码里直接下断点是行不通的
		# 工具 -> 选项 -> 调试 -> 符号 加入这两个
			$(WpfRepoRoot)\artifacts\obj\**\Debug
			$(WpfRepoRoot)\artifacts\obj\**\net9.0
				# 这样就能成功加载符号
					# 调试 -> 窗口 -> 模块 能看到 dll 的符号是否成功加载
	
	    C:\Users\Administrator\wpf\eng\wpf-debug.targets 的
		WpfRepoRoot 改成这个：C:\Users\Administrator\wpf

<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
      <UseWPF>true</UseWPF>
    <Platforms>x86</Platforms>
	<DebugType>full</DebugType>
	<DebugSymbols>true</DebugSymbols>
    <EmbedAllSources>true</EmbedAllSources>
	<IncludeSymbols>true</IncludeSymbols>
	  <!-- Change this value based on where your local repo is located -->
	  <WpfRepoRoot>C:\Users\Administrator\wpf</WpfRepoRoot>
	  <!-- Change based on which assemblies you build (Release/Debug) -->
	  <WpfConfig>Debug</WpfConfig>
	  <WpfOuputFolder>Microsoft.DotNet.Wpf.GitHub.Debug</WpfOuputFolder>
	  <!-- Publishing a self-contained app ensures our binaries are used. -->
	  <SelfContained>true</SelfContained>
	  <!-- The runtime identifier needs to match the architecture you built WPF assemblies for. -->
	  <RuntimeIdentifier>win-x86</RuntimeIdentifier>
  </PropertyGroup>

	<ItemGroup>
		<Reference Include="$(WpfRepoRoot)\artifacts\packaging\$(WpfConfig)\$(WpfOuputFolder)\lib\net9.0\*.dll" />
		<ReferenceCopyLocalPaths Include="$(WpfRepoRoot)\artifacts\packaging\$(WpfConfig)\$(WpfOuputFolder)\lib\$(RuntimeIdentifier)\*.dll" />
		<ReferenceCopyLocalPaths Include="$(WpfRepoRoot)\artifacts\packaging\$(WpfConfig)\$(WpfOuputFolder)\runtimes\$(RuntimeIdentifier)\native\*.dll" />
	</ItemGroup>
</Project>
	# 这样配置后，F12 能导航到源码
		# 但是断点无效，断不下来！！！



<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
      <UseWPF>true</UseWPF>
    <Platforms>x86</Platforms>
	<DebugType>full</DebugType>
	<DebugSymbols>true</DebugSymbols>
  </PropertyGroup>
	<ItemGroup>
		<PackageReference Include="Microsoft.DotNet.Wpf.GitHub.Debug" Version="9.0.0-ci">
			<IncludeSymbols>true</IncludeSymbols>
		</PackageReference>
		<PackageReference Include="Microsoft.DotNet.Wpf.ProjectTemplates.Debug" Version="9.0.0-ci">
			<IncludeSymbols>true</IncludeSymbols>
		</PackageReference>
		<PackageReference Include="runtime.win-x86.Microsoft.DotNet.Wpf.GitHub.Debug" Version="9.0.0-ci">
			<IncludeSymbols>true</IncludeSymbols>
		</PackageReference>
	</ItemGroup>
</Project>
	# 引入带调试符号的包
	#  <PackageReference Include="Microsoft.DotNet.Wpf.ProjectTemplates.Debug" Version="9.0.0-ci">
		# 一定要加这一句后才会输出：######### Test Modify code. this comiple from wpf souce code!!!


nuget.config
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="LocalSymbols" value="E:\localNuget" />
  </packageSources>
</configuration>
	# 项目根目录新增
	

visual studio 2025 -> 工具 -> 选项 -> 调试 -> 符号 -> 新位置 -> E:\localNuget

程序运行以后 -> 调试 -> 窗口 -> 模块 能看到已加载 dll


using System.Windows;

class Program
{

    [STAThread]
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");

        Application app = new Application();

        var window = new Window();
        window.Title = "Test";

        app.Run(window);
        Console.ReadKey();
    }
}
	# 成功打印了调试信息
		# 关键点：AnyCpu 那里新建 x86 配置，新建就可以不需要复制其他配置，然后选 x86
		######### Test Modify code. this comiple from wpf souce code!!!


C:\Users\Administrator\wpf\artifacts\packaging\Debug\Microsoft.DotNet.Wpf.GitHub.Debug\lib\net9.0
	# 直接导入所有 dll 作为依赖就可以正常运行！！！
	# 下一步在把 PresentationFramework 的源码加进来编译

```



### 路径变量 插入源码

```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net9.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>

    <RepoRoot>C:\Users\Administrator\wpf\</RepoRoot>
    <SourceDir>$(RepoRoot)src\Microsoft.DotNet.Wpf\src\</SourceDir>
    <SharedDir>$(SourceDir)Shared\</SharedDir>

  </PropertyGroup>

  <Target Name="DebugVars" BeforeTargets="Build">
    <Message Text="SharedDir: $(SharedDir)" Importance="high" />
    <Message Text="Full Path: $(SharedDir)RefAssemblyAttrs.cs" Importance="high" />
  </Target>

  <!--
    PowerShell 测试路径是否存在
    Test-Path "C:\Users\Administrator\wpf\src\Microsoft.DotNet.Wpf\src\Shared\RefAssemblyAttrs.cs"
   -->

  <ItemGroup>
    <Compile Include="$(SharedDir)\RefAssemblyAttrs.cs" />
  </ItemGroup>


</Project>
```





##　语法

### 设计时属性

```
`mc:Ignorable="d"` 是 XAML 中的一个特殊属性，主要用于设计时的兼容性。让我来解释一下：

1. `mc:Ignorable` 告诉 XAML 解析器哪些命名空间前缀可以被安全地忽略。

2. 这里的 `"d"` 指的是设计时命名空间（Design-time namespace），也就是在你的 XAML 代码中声明的：
​```xml
xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
​```

3. 主要作用：
   - 允许在 XAML 中使用仅供设计时使用的属性和标记（比如在 Visual Studio 设计器或 Blend 中）
   - 这些设计时属性在运行时会被完全忽略
   - 不会影响应用程序的实际运行

4. 常见用例：
   - `d:DesignWidth` 和 `d:DesignHeight`：设置设计时的窗口尺寸
   - `d:DataContext`：设置设计时的数据上下文
   - `d:DesignSource`：指定设计时的数据源

如果移除 `mc:Ignorable="d"`，那么运行时可能会对设计时属性产生警告或错误，因为运行时环境不知道如何处理这些仅用于设计时的属性。
```



### 扩展方法

```
see huggingface\itrans\src\ScreenGrab\Extensions\WpfExtensions.cs

让我来解释一下 C# 扩展方法（Extension Methods）的原理和使用：

### 1. 扩展方法的原理

扩展方法是 C# 3.0 引入的一个特性，允许你向现有类型"添加"方法，而无需修改或继承原始类型。在这个例子中：

​```csharp
public static Point GetAbsolutePosition(this Window w)
​```

- `this Window w` 中的 `this` 关键字表明这是一个扩展方法
- 它会将 `GetAbsolutePosition` 方法"附加"到 `Window` 类型上
- 实际上这是一个静态方法，但可以像实例方法一样调用

### 2. 使用要求

1. 扩展方法必须定义在静态类中（如这里的 `WpfExtensions`）
2. 扩展方法本身必须是静态的（static）
3. 第一个参数必须使用 `this` 关键字，表示要扩展的类型

### 3. 如何使用

假设你有一个 Window 对象，可以这样使用这个扩展方法：

​```csharp
// 首先引入命名空间
using ScreenGrab.Extensions;

// 然后可以直接在 Window 对象上调用这个方法
Window window = new Window();
Point position = window.GetAbsolutePosition();

// 等价于静态调用（但一般不这么用）
Point position = WpfExtensions.GetAbsolutePosition(window);
​```

### 4. 扩展方法的优势

1. **代码组织**：可以将相关功能组织在一起，而不是散布在原始类中
2. **不修改原代码**：可以为第三方库或框架类添加功能，而无需修改或继承原始代码
3. **智能提示支持**：在 IDE 中可以像普通实例方法一样获得智能提示
4. **链式调用**：可以支持方法链式调用，提高代码可读性

### 5. 实际应用场景

在这个例子中，`GetAbsolutePosition` 扩展了 WPF 的 `Window` 类，添加了获取窗口绝对位置的功能：

​```csharp
// 在需要获取窗口位置的地方
public void SomeMethod()
{
    Window mainWindow = Application.Current.MainWindow;
    Point windowPosition = mainWindow.GetAbsolutePosition();
    // 使用 windowPosition.X 和 windowPosition.Y
}
​```

### 6. 注意事项

1. 扩展方法不能覆盖原有类型的方法
2. 如果原有类型添加了同名方法，原有方法优先级更高
3. 扩展方法不能访问被扩展类型的私有成员
4. 建议只为确实需要扩展的类型添加有意义的扩展方法

扩展方法是一个强大的功能，但应该谨慎使用，主要用于：
- 为现有类型添加实用的辅助方法
- 提供更好的 API 设计和代码可读性
- 实现特定的领域功能扩展

```





### 为什么点击事件不触发

```

1. 不在视觉树里的元素无戏可唱（不响应 UI 交互事件）
2. 透明的元素没戏
3. 后面定义控件覆盖前面控件，子覆盖父控件
3. 覆盖不管大小，小一样盖住大。覆盖住事件就被它截走了，不会下层控件不会再响应事件
4. Background="Transparent"   Background="NavajoWhite" 灵活切换来定义要响应的事件的控件

<Window
    x:Class="ScreenGrab.ScreenGrabView"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:local="clr-namespace:ScreenGrab"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    Title="ScreenGrab"
    Width="800"
    Height="450"
    AllowsTransparency="True"
    Background="Transparent"
    Closed="Window_Closed"
    Loaded="Window_Loaded"
    ResizeMode="NoResize"
    ShowInTaskbar="False"
    Topmost="True"
    Unloaded="Window_Unloaded"
    WindowStyle="None"
    mc:Ignorable="d">

    <Grid d:Background="Transparent">
        <Viewbox>
            <Image x:Name="BackgroundImage" Stretch="UniformToFill" />
        </Viewbox>
        <Canvas
            Background="NavajoWhite"
            x:Name="RegionClickCanvas"
            Cursor="Cross"
            MouseDown="RegionClickCanvas_MouseDown"
        >
        </Canvas>

    </Grid>
</Window>
```





### Stretch 拉伸模式

```
`Stretch="UniformToFill"` 是 WPF 中图像拉伸模式的一个选项，它的作用是：

1. 保持图像的原始宽高比（不会变形）
2. 填充整个可用空间，确保没有空白区域
3. 如果需要，会裁剪图像的部分内容以适应容器

WPF 中的 Stretch 属性有以下几种模式：

- `None`: 不进行任何拉伸，保持原始大小
- `Fill`: 完全填充，可能会导致图像变形
- `Uniform`: 等比例缩放，可能会有空白区域
- `UniformToFill`: 等比例缩放并填充满，可能会裁剪部分内容

在你的代码中：
​```xml:e:\huggingface\iScreenGrab\src\ScreenGrab\ScreenGrabView.xaml
<Viewbox>
    <Image x:Name="BackgroundImage" Stretch="UniformToFill" />
</Viewbox>
​```

这个设置确保了背景图片会：
1. 完全填充 Viewbox 控件的空间
2. 保持图片的原始宽高比
3. 如果图片的宽高比与 Viewbox 不完全匹配，会裁剪掉超出的部分，而不是出现空白区域或者使图片变形

这种设置在需要填满整个区域但又不希望图片变形的场景下非常有用，比如全屏背景图片的显示。
```



### 宏

```
        # see huggingface\iScreenGrab\src\ScreenGrab\ScreenGrabView.xaml.cs
        private double Clamp(double value, double min, double max)
        {
            #if NETFRAMEWORK
            		# .net framework
                    if (value < min) return min;
                    if (value > max) return max;
                    return value;
            #else
                return Math.Clamp(value, min, max);
            #endif
        }
```



### 裁剪区域 镂空效果

```

# see huggingface\itrans\src\ScreenGrab\ScreenGrabView.xaml

            <Canvas.Clip>
                <CombinedGeometry GeometryCombineMode="Exclude">
                    <CombinedGeometry.Geometry1>
                        <RectangleGeometry x:Name="FullWindow" />
                    </CombinedGeometry.Geometry1>
                    <CombinedGeometry.Geometry2>
                        <RectangleGeometry x:Name="ClippingGeometry" />
                    </CombinedGeometry.Geometry2>
                </CombinedGeometry>
            </Canvas.Clip>
            
            
 这段代码是用于实现截图时的遮罩效果。让我解释一下它的工作原理：

​```xml:e:\huggingface\itrans\src\ScreenGrab\ScreenGrabView.xaml
<Canvas.Clip>
    <CombinedGeometry GeometryCombineMode="Exclude">
        <CombinedGeometry.Geometry1>
            <RectangleGeometry x:Name="FullWindow" />  <!-- 整个窗口区域 -->
        </CombinedGeometry.Geometry1>
        <CombinedGeometry.Geometry2>
            <RectangleGeometry x:Name="ClippingGeometry" />  <!-- 选中的截图区域 -->
        </CombinedGeometry.Geometry2>
    </CombinedGeometry>
</Canvas.Clip>
​```

具体来说：

1. `Canvas.Clip` 定义了一个裁剪区域，只有在这个区域内的内容才会显示
2. `CombinedGeometry` 用于组合两个几何图形：
   - `GeometryCombineMode="Exclude"` 表示使用排除模式，即从第一个几何图形中排除第二个几何图形的区域
   - `Geometry1` (`FullWindow`) 代表整个窗口的区域
   - `Geometry2` (`ClippingGeometry`) 代表用户选择的截图区域

这样的组合效果是：
- 当用户进行截图选择时，选中的区域（`ClippingGeometry`）会从整个窗口区域（`FullWindow`）中被"挖空"
- 剩余的区域会显示半透明的遮罩效果（通过 `BackgroundBrush` 实现）
- 这就形成了常见的截图工具的效果：选中区域清晰可见，而其他区域显示半透明遮罩

这是一个很常见的截图工具的实现方式，可以让用户清楚地看到自己选择的区域范围。

```



### Border 带边框特效的面板

```

# see huggingface\itrans\src\ScreenGrab\ScreenGrabView.xaml

        <Border
            x:Name="PromptMsg"
            Margin="15"
            HorizontalAlignment="Left"
            VerticalAlignment="Bottom"
            Background="#424242"
            BorderBrush="WhiteSmoke"
            BorderThickness=".6"
            Opacity="0.9"
            Visibility="Collapsed">
            <local:AutoGrid
                ChildMargin="3"
                ChildVerticalAlignment="Center"
                Columns="*, *"
                RowCount="2"
                RowHeight="30">
                <Grid.Resources>
                    <Style TargetType="StackPanel">
                        <Setter Property="Orientation" Value="Horizontal" />
                        <Setter Property="HorizontalAlignment" Value="Right" />
                    </Style>
                    <Style TargetType="TextBlock">
                        <Setter Property="Foreground" Value="White" />
                        <Setter Property="FontSize" Value="16" />
                        <Setter Property="HorizontalAlignment" Value="Left" />

                    </Style>
                </Grid.Resources>
                <StackPanel>
                    <local:UcCharacter DisplayChar="Shift" />
                    <local:UcCharacter DisplayChar="🖱" />
                </StackPanel>
                <TextBlock Text="移动选区" />
                <StackPanel>
                    <local:UcCharacter DisplayChar="F" />
                </StackPanel>
                <TextBlock x:Name="FreezeTb" Text="取消冻结窗口" />
            </local:AutoGrid>
        </Border>

这段代码中使用 Border 是为了创建一个提示信息面板，主要有以下几个原因：

1. **视觉边界和样式**
   - Border 提供了一个清晰的视觉边界，通过 `BorderBrush` 和 `BorderThickness` 属性设置了浅色边框
   - 通过 `Background="#424242"` 设置了深色背景，配合 `Opacity="0.9"` 实现半透明效果
   - 这些样式让提示信息在截图界面上更加醒目且美观

2. **布局控制**
   - Border 作为容器控件，可以通过 `Margin="15"` 控制与父容器的间距
   - 使用 `HorizontalAlignment="Left"` 和 `VerticalAlignment="Bottom"` 将提示信息固定在左下角
   - 通过 `Visibility="Collapsed"` 控制整个提示面板的显示和隐藏

3. **内容组织**
   - Border 内部包含了一个 `local:AutoGrid`，用于组织快捷键提示信息
   - 这种嵌套结构使得提示信息的布局更加清晰和模块化

4. **用户体验**
   - 通过 Border 的视觉效果，让用户能够清楚地区分提示信息和截图区域
   - 半透明效果确保提示信息不会完全遮挡底部内容

总的来说，Border 在这里起到了一个视觉容器的作用，它不仅提供了样式和边界，还帮助组织和布局内部的提示信息内容，使整个提示面板看起来更加专业和美观。

```



### 跟随鼠标的交叉线

```
# see huggingface\itrans\src\ScreenGrab\ScreenGrabView.xaml

            <!--  Horizontal Line  -->
            <Line
                x:Name="HorizontalLine"
                Stroke="#92caf4"
                StrokeThickness="1"
                Visibility="Collapsed" />
            <!--  Vertical Line  -->
            <Line
                x:Name="VerticalLine"
                Stroke="#92caf4"
                StrokeThickness="1"
                Visibility="Collapsed" />
                
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            (HorizontalLine.X1, VerticalLine.Y1, (HorizontalLine.X2, VerticalLine.Y2)) = (0, 0, this.GetWidthHeight());
        }
        
        private void RegionClickCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            var movingPoint = e.GetPosition(this);

            // Update the horizontal line to match the mouse Y position
            HorizontalLine.Y1 = HorizontalLine.Y2 = movingPoint.Y;

            // Update the vertical line to match the mouse X position
            VerticalLine.X1 = VerticalLine.X2 = movingPoint.X;
        }
        
        private void SetAuxiliaryVisibility(bool isVisible)
        {
            var setVisibility = isVisible ? Visibility.Visible : Visibility.Collapsed;
            if (HorizontalLine.Visibility == setVisibility && VerticalLine.Visibility == setVisibility)
                return;
            HorizontalLine.Visibility = setVisibility;
            VerticalLine.Visibility = setVisibility;
        }

```



### 引用类库里的自定义控件

```
xmlns:sg="clr-namespace:ScreenGrab;assembly=ScreenGrab"
        xmlns:local="clr-namespace:iTrans"
        xmlns:vm ="clr-namespace:iTrans.ViewModels"
        	# 对比原生写法，少了定义程序集 assembly=xxx
    
    <Grid>
        <sg:AutoGrid
                ChildMargin="3"
                ChildVerticalAlignment="Center"
                Columns="*, *"
                RowCount="2"
                RowHeight="30">
        </sg:AutoGrid>
        <Viewbox>
            <Image x:Name="ClipImage" Stretch="UniformToFill" />
        </Viewbox>
    </Grid>
    
    
另外，请确保：
	1. ScreenGrab 项目已经被正确引用到 iTrans 项目中
	2. ScreenGrab 项目已经被成功编译

```



### RichTextBox 原生命令

https://www.cnblogs.com/zhouyinhui/archive/2010/06/22/1762633.html

```
# see huggingface\RichTextBoxEditor\RichTextBoxEditor\MainWindow.xaml

	<Button ToolTip="项目编号" Command="EditingCommands.ToggleBullets" CommandTarget="{Binding ElementName=richTextBox}">
                <Path Data="{StaticResource icon_bullets}" Stretch="Fill" Fill="DimGray"></Path>
            </Button>
            	# 触发以后自动更新 UI，这命令不用自已定义
            	
            	
EditingCommands.ToggleBullets.Execute(null, richTextBox);
	# 代码直接触发
	
	
        private static void OnFormattingPropertyChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            RichTextBox richTextBox = (RichTextBox)d;

            if (richTextBox._implicitDocument)
            {
                richTextBox.TransferFormattingProperty(e.Property, e.NewValue);
            }
        }
        	
        	# wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Controls\RichTextBox.cs
        	# 文本格式化应该调用的是这里
        	
        HookupInheritablePropertyListeners();
        	# 构造函数就调用这个
	

```



```
wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Controls\RichTextBox.cs
	# RichTextBox 代码在这

如果你确实需要使用 Microsoft 内部的 API，你需要添加对相应程序集的引用。但我再次强调，这是不推荐的做法。

要使用 MS.Internal 命名空间，你需要：

1. 首先在项目中添加对 WindowsBase.dll 的引用（通常 WPF 项目默认已经包含）
2. 在代码文件顶部添加以下特性来取消对内部 API 的访问限制：

using System.Security;
[assembly: SecurityTransparent]
[assembly: AllowPartiallyTrustedCallers]
[assembly: SecurityRules(SecurityRuleSet.Level1)]

using MS.Internal;
using MS.Internal.Documents;


```





```
FlowDocument 支持多种文档块元素：

1. Section - 用于分组段落和其他块元素
2. Paragraph - 段落文本
3. List - 列表（有序或无序）
4. Table - 表格
5. BlockUIContainer - 用于包含 UI 元素
6. Figure - 用于包含图像和说明文字
7. Floater - 浮动内容块
这些元素可以根据需要组合使用，以创建更复杂的文档结构。每个 Section 可以有自己的格式设置，比如边距、对齐方式等。
```



```

# ai 写的代码，构造函数有错误

huggingface\RichTextBoxEditor\RichTextBoxEditor\CustomTextElement.cs

using System;
using System.Windows;
using System.Windows.Documents;

namespace RichTextBoxEditor
{
    public class CustomTextElement : TextElement, ICloneable
    {
        public CustomTextElement(TextPointer position) : base(position)
        {
        }

        public CustomTextElement(TextPointer start, TextPointer end) : base(start, end)
        {
        }

        // 自定义属性，可以根据需要添加更多
        public string CustomData
        {
            get { return (string)GetValue(CustomDataProperty); }
            set { SetValue(CustomDataProperty, value); }
        }

        public static readonly DependencyProperty CustomDataProperty =
            DependencyProperty.Register("CustomData", typeof(string), typeof(CustomTextElement),
                new FrameworkPropertyMetadata(string.Empty, FrameworkPropertyMetadataOptions.Inherits));

        public object Clone()
        {
            // 使用当前元素的开始和结束位置创建新实例
            CustomTextElement clone = new CustomTextElement(this.ContentStart, this.ContentEnd);
            clone.CustomData = this.CustomData;
            // 复制基类属性
            clone.FontFamily = this.FontFamily;
            clone.FontSize = this.FontSize;
            clone.FontStyle = this.FontStyle;
            clone.FontWeight = this.FontWeight;
            clone.Foreground = this.Foreground;
            clone.Background = this.Background;
            return clone;
        }
    }
}

```





#### 加粗

```

参照它实现自已的自定义属性

wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Documents\TextEditorCharacters.cs 
	line 179

// 加粗
OnToggleBold(object target, ExecutedRoutedEventArgs args)


// 字号增大
OnIncreaseFontSize(object target, ExecutedRoutedEventArgs args)
	# 模仿这个属性可能比较好，因为是数值的

TextEditorCharacters._OnApplyProperty(This, TextElement.FontSizeProperty, fontSize);
	# line 327



```





#### 切换项目符号

https://www.cnblogs.com/tianqing/p/13197382.html

```
_ToggleBullets

FlowDocument
    ├── Block (段落级元素)
    │   ├── Paragraph
    │   ├── Section
    │   ├── List
    │   └── Table
    └── Inline (行内元素)
        ├── Run (纯文本)
        ├── Span
        ├── Hyperlink
        └── InlineUIContainer
     
wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Documents\TextEditorLists.cs

        internal static void _RegisterClassHandlers(Type controlType, bool registerEventListeners)
            CommandHelpers.RegisterCommandHandler(controlType, EditingCommands.ToggleBullets       , new ExecutedRoutedEventHandler(OnListCommand) , new CanExecuteRoutedEventHandler(OnQueryStatusNYI), KeyGesture.CreateFromResourceStrings(KeyToggleBullets, nameof(SR.KeyToggleBulletsDisplayString)));
	# 切换项目符号应该在 OnListCommand 里处理？

private static void OnListCommand(object target, ExecutedRoutedEventArgs args)
	ToggleBullets(thisSelection, parentListItem, immediateListItem, list);

dotnet tool install --global dotnet-debugger-extensions
	# 安装 dotnet 调试插件

    # choco install winget
        # C:\ProgramData\chocolatey\lib\winget
            # 装到这里了
            # 它只是一个包，根本用不了
            
    # winget install Microsoft.WinDbg
        # Administrator 账户才能找到 winget 命令
		# 也用不了
		
https://aka.ms/windbg/download
	# 下载后成功运行了 
	# 这样安装应该是 64 位的，编程 wpf 也要 64 位才可以！！！

g
	# 继续运行

dotnet tool install --global dotnet-sos
dotnet-sos install
.load C:\Users\i\.dotnet\sos\sos.dll
	# huggingface\RichTextBoxEditor\RichTextBoxEditor\bin\x64\Debug\net9.0-windows\win-x64\RichTextBoxEditor.exe
	# 一定是要 64 位的程序才成功

!sos.help
	# 打印帮助

.chain
	-->  C:\Users\i\.dotnet\sos\sos.dll

.symfix
!sym noisy
.reload

!bpmd PresentationFramework.dll System.Windows.Documents.TextEditorLists.ToggleBullets
	# 成功下断点
	# 注意下断点后它可能不会马上显示出来，而是实际触发后窗口的断点才可见
	# wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Documents\TextEditorLists.cs
	# 源码在 177 行

光标放在某个段落 -> 点“项目符号” 
	# 成功触发刚才下的断点
	

x user32!*
	# 显示 dll 的所有符号
	# 先加载符号，view -> Modules 可以看到符号加载没有 没有右键强制加载它
	x PresentationFramework!*
		# 成功打印符号
		.logopen E:\symbols.txt
		x PresentationFramework!*
		.logclose
		# ToggleBullets(TextSelection thisSelection, ListItem parentListItem, ListItem immediateListItem, List list)
x PresentationFramework.dll!ToggleBullets
		
		wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Documents\TextEditorLists.cs  line 177
ToggleBullets(TextSelection thisSelection, ListItem parentListItem, ListItem immediateListItem, List list)		
这个函数用于切换文本的项目符号（bullet points）状态。它根据当前选择的文本位置和状态来决定执行什么操作。让我们分析每个条件分支：

1. 第一个条件分支 ( immediateListItem != null && HasBulletMarker(list) )：
   
   - 当前位置已经是一个带项目符号的列表项
   - 两种处理情况：
     - 如果列表是嵌套的（ list.Parent is ListItem ）：
       - 取消缩进并转换为普通段落
     - 如果是普通列表：
       - 仅取消缩进
2. 第二个条件分支 ( immediateListItem != null )：
   
   - 当前位置是一个列表项，但不是项目符号样式
   - 操作：
     - 将列表标记样式改为圆点样式（ TextMarkerStyle.Disc ）
3. 第三个条件分支 ( parentListItem != null )：
   
   - 当前位置在一个列表项内，但不是直接的列表项
   - 操作：
     - 将段落转换为项目符号列表项
     - 增加缩进级别
4. 最后的情况（else）：
   
   - 当前位置不在任何列表中
   - 操作：
     - 直接将段落转换为项目符号列表项
简单来说，这个函数实现了以下功能：

- 如果文本已经是项目符号列表，则移除项目符号
- 如果文本是其他类型的列表，则转换为项目符号列表
- 如果文本是普通段落，则添加项目符号
这样的设计让用户可以通过重复调用同一个命令来切换文本的项目符号状态，类似于我们在 Word 等文字处理软件中使用项目符号按钮的行为。

参数含义：

- thisSelection: TextSelection

- 表示当前文本编辑器中的选择区域
- 包含了选择的起始位置和结束位置
- 用于确定要应用项目符号的文本范围
- parentListItem: ListItem

- 表示当前选择位置的父级列表项
- 如果当前选择位置在嵌套列表中，这个参数代表外层的列表项
- 用于处理嵌套列表的情况
- immediateListItem: ListItem

- 表示当前选择位置的直接列表项
- 如果当前选择位置就在一个列表项中，这个参数就代表那个列表项
- 用于确定是否需要切换当前列表项的样式
- list: List

- 表示当前列表项所属的列表对象
- 包含了列表的样式信息（如项目符号类型）
- 用于修改或获取列表的标记样式（MarkerStyle）



list.MarkerStyle 属性改变后会触发哪个函数调用（改成圆点样式）

List.MarkerStyle 是一个 DependencyProperty，当它的值改变时会触发属性变更通知机制。让我解释一下这个过程：

1. MarkerStyle 是在 System.Windows.Documents.List 类中定义的依赖属性：

当 MarkerStyle 属性值改变时，会触发以下过程：

    1. 首先触发 OnMarkerStyleChanged 回调函数
    2. 由于设置了 FrameworkPropertyMetadataOptions.AffectsMeasure ，会触发元素的重新测量
    3. 由于设置了 FrameworkPropertyMetadataOptions.AffectsRender ，会触发元素的重新渲染
    4. 如果有任何绑定到这个属性的 UI 元素，它们也会收到通知并更新
    这样就能确保列表标记样式的改变能立即反映在用户界面上。


wpf\src\Microsoft.DotNet.Wpf\src\PresentationFramework\System\Windows\Documents\List.cs
	line 267
	新建 ListItem 元素


在 WPF 中，单个字符的属性是在 System.Windows.Documents.TextElement 类中定义的基本属性，主要包括：

    public class TextElement : FrameworkContentElement
        public static readonly DependencyProperty FontFamilyProperty;

public abstract class Inline : TextElement

具体的文本运行时属性在 System.Windows.Documents.Run 类中：
    public class Run : Inline
        // 实际文本内容
			//text node in Flow content (text run)


```



##### 每一个字符增加自定义属性

```

从你提供的代码可以看出， `Run.cs` 类是 WPF 文本处理的基本单元。它继承自 Inline 类，可以应用各种文本格式化属性，包括 FontWeight 来实现文本加粗。

当你在 RichTextBox 中设置文本为粗体时，实际上是在修改 Run 对象的 FontWeight 依赖属性。这个属性的变化会触发 WPF 的属性系统，从而更新 UI 显示。

如果你需要在代码中动态处理文本加粗，建议使用 TextRange 的方式，因为它可以方便地处理选中的文本范围，而不需要手动创建和管理 Run 对象。

// 方式1：直接设置 Run 的 FontWeight
Run boldRun = new Run("这是加粗文本");
boldRun.FontWeight = FontWeights.Bold;

// 方式2：使用 TextRange 设置选中文本的格式
TextRange textRange = new TextRange(richTextBox.Selection.Start, richTextBox.Selection.End);
textRange.ApplyPropertyValue(TextElement.FontWeightProperty, FontWeights.Bold);




新建 System\Windows\Documents\TextCharacterProperty.cs
	# ai 生成的代码，可能需要修改
using System.Windows;

namespace System.Windows.Documents
{
    // 定义一个自定义附加属性
    public static class TextCharacterProperty
    {
        public static readonly DependencyProperty CustomProperty = 
            DependencyProperty.RegisterAttached(
                "Custom",
                typeof(object),
                typeof(TextCharacterProperty),
                new FrameworkPropertyMetadata(null));

        public static void SetCustom(DependencyObject element, object value)
        {
            element.SetValue(CustomProperty, value);
        }

        public static object GetCustom(DependencyObject element)
        {
            return element.GetValue(CustomProperty);
        }
    }

    // 在处理文本时，需要将文本拆分成单个字符的 Run
    private static void ApplyCustomPropertyToCharacters(TextRange range, object customValue)
{
    TextPointer current = range.Start;
    while (current.CompareTo(range.End) < 0)
    {
        TextPointer nextPosition = current.GetNextInsertionPosition(LogicalDirection.Forward);
        if (nextPosition == null) break;
        
        string text = current.GetTextInRun(LogicalDirection.Forward);
        if (!string.IsNullOrEmpty(text))
        {
            // 删除原始文本
            current.DeleteTextInRun(text.Length);
            
            // 为每个字符创建新的 Run
            foreach (char c in text)
            {
                Run run = new Run(c.ToString());
                TextCharacterProperty.SetCustom(run, customValue);
                current.InsertInline(run);
            }
        }
        current = nextPosition;
    }
}

// 为选中文本的每个字符添加自定义属性
TextSelection selection = richTextBox.Selection;
using (selection.DeclareChangeBlock())
{
    ApplyCustomPropertyToCharacters(selection, yourCustomValue);
}

}


严重性	代码	说明	项目	文件	行	禁止显示状态	详细信息
错误(活动)		TypesMustExist : Type 'System.Windows.Documents.TextCharacterProperty' does not exist in the implementation but it does exist in the contract.	PresentationFramework	C:\Users\Administrator\wpf\eng\WpfArcadeSdk\tools\ApiCompat.targets	226		
	# 出错了


```







##### WPF 自定义文本框输入法 IME 跟随光标

https://blog.lindexi.com/post/WPF-%E8%87%AA%E5%AE%9A%E4%B9%89%E6%96%87%E6%9C%AC%E6%A1%86%E8%BE%93%E5%85%A5%E6%B3%95-IME-%E8%B7%9F%E9%9A%8F%E5%85%89%E6%A0%87.html

WPF 自定义文本框输入法 IME 跟随光标

- https://github.com/lindexi/lindexi_gd/tree/b3a1fffece8284d0b84407aa13d949de6a2f1536/





## WPF编程宝典



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



```
右键项目 -> 编缉项目文件

新增：
	<PropertyGroup>
		<LangVersion>latest</LangVersion>
	</PropertyGroup>
	
https://github.com/RomaSharper/YoutubeWatcher
	# 正常运行
```





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



### STranslate

https://www.cnblogs.com/aierong/p/17305990.html Mvvm 写法

```

see nodejs summary.md -> WPF -> [STranslate 对标Bob](https://github.com/ZGGSONG/STranslate)  **完成度很高的** wpf

目录结构技巧：新建 wpf 解决方案 -> 删掉项目 -> 新建解决方案文件夹(虚拟的) -> 新建 src 文件夹（物理的）
  -> 右击 src 新建项目选 wpf 桌面 windows

see STranslate\ViewModels\MainViewModel.cs

Loaded(Window view)
	# 开始注册热键

CommunityToolkit.Mvvm 8.3.2
	# 安装
Microsoft.Xaml.Behaviors.Wpf 1.1.135
	# 安装
ScreenGrab 1.0.6
	# 安装 用于屏幕截图，不安装它，而是集成它的源码看看
	# Dapplo.Windows.User32 1.0.28
	


新建项目
WpfApp1\App.xaml
	StartupUri="MainWindow.xaml"  
		# 删除这一行，手动启动窗体

WpfApp1\MainView.xaml
		x:Class="WpfApp1.MainView"
        xmlns:i="http://schemas.microsoft.com/xaml/behaviors"
        xmlns:vm="clr-namespace:WpfApp1.model"
        x:Name="MainWindow" # 注意 x:Name 和 x:class 必须不同
        mc:Ignorable="d"
        d:DataContext="{d:DesignInstance Type=vm:MainViewModel}"
		# 加命名空间，并让 MainViewModel 类可见
	    <i:Interaction.Triggers>
        <i:EventTrigger EventName="Loaded">
            <i:InvokeCommandAction Command="{Binding LoadedCommand}" CommandParameter="{Binding ElementName=MainWindow}" />
        </i:EventTrigger>
    </i:Interaction.Triggers>
		# 加事件绑定

		
WpfApp1\App.xaml.cs		
        protected override void OnStartup(StartupEventArgs e) {
            base.OnStartup(e);
            new MainWindow().Show();
        }
        	# 加入


model/MainWindowModel.cs
namespace WpfApp1.model
	public partial class MainViewModel : ObservableObject {
        [RelayCommand]
        private void Loaded(Window view){} // 自动生成 LoadedCommand
    }
		# 新建源文件


# 要成功触发绑定事件，必须设置 DataContext 
WpfApp1\MainView.xaml.cs
    public class Singleton<T> where T : class, new()
    {
        private static readonly Lazy<T> _instance = new(() => (T)Activator.CreateInstance(typeof(T), true)!, true);

        public static T Instance => _instance.Value;
    }

    public partial class MainView : Window
    {
        private readonly MainViewModel _vm = Singleton<MainViewModel>.Instance;

        public MainView()
        {
            DataContext = _vm;

            InitializeComponent();
        }
    }


```



#### 截图窗口显示不出来

```
see huggingface\itrans\src\iTrans\ViewModels\MainViewModel.cs

        // 执行实际截图
        internal void ScreenShotHandler(CancellationToken? token = null)
        {
            if (ScreenGrabber.IsCapturing) return;
                // https://github.com/wuqinchao/ScreenCapturer // 替代品
            
            ScreenGrabber.OnCaptured = async bitmap => await ScreenshotCallbackAsync(bitmap, token);
            // 确保在 UI 线程上调用 Capture 方法
            Application.Current.Dispatcher.Invoke(() => ScreenGrabber.Capture(true));
                // ScreenGrabber.Capture(true);
                    // 直接调用这个截图窗口显示不出来

1.	UI 线程问题：确保 Capture 方法在 UI 线程上调用。可以使用 Dispatcher 来确保在 UI 线程上执行。
2.	窗口状态：确保窗口的 WindowState 和 Visibility 属性正确设置。
3.	窗口显示顺序：确保窗口在调用 Show 方法后立即调用 Activate 方法。


```





#### WPF 嵌入 winform 

https://www.zggsong.com/posts/coding/winform-wpf-res-dict/



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

    

# 登录

- https://github.com/openiddict/openiddict-core



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





