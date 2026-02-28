

# 添加资源

```
.Net 6.0 WPF

修改项目文件 .csproj 
  <ItemGroup>
    <Page Update="App.Icons.xaml">
      <Generator>MSBuild:Compile</Generator>
    </Page>
    <Page Update="App.Styles.xaml">
      <Generator>MSBuild:Compile</Generator>
    </Page>
  </ItemGroup>
  
  
修改 App.xaml
     <Application.Resources>
        <ResourceDictionary>
 			<ResourceDictionary.MergedDictionaries>
 			    <ResourceDictionary Source="App.Icons.xaml" />
                <ResourceDictionary Source="App.Styles.xaml" />
 			</ResourceDictionary.MergedDictionaries>
         </ResourceDictionary>
    </Application.Resources>
    

添加用户控件, 既可看到效果
<UserControl x:Class="WpfApp1.UserControl1"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
             xmlns:local="clr-namespace:WpfApp1"
             mc:Ignorable="d">
    <Grid Name="Controls" Visibility="Visible" Height="250" Background="{x:Null}">

        <Grid VerticalAlignment="Bottom">
            <Grid.RowDefinitions>
                <RowDefinition Height="30"></RowDefinition>
                <RowDefinition Height="40"></RowDefinition>
                <RowDefinition Height="70"></RowDefinition>
            </Grid.RowDefinitions>

            <DockPanel Name="ProgressPanel" Grid.Row="1" LastChildFill="True" Margin="20,0">
                <Grid Width="500">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="100" />
                        <ColumnDefinition />
                        <ColumnDefinition />
                        <ColumnDefinition Width="100" />
                    </Grid.ColumnDefinitions>
                </Grid>
            </DockPanel>

            <Grid Name="ControlsPanel" Grid.Row="2" Margin="20,0">
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*" />
                    <ColumnDefinition Width="1*" />
                    <ColumnDefinition Width="1*" />
                </Grid.ColumnDefinitions>
                <DockPanel Name="LeftControls" HorizontalAlignment="Left" Grid.Column="0">
                    <ToggleButton Style="{DynamicResource ModernToggleButtonStyle}" >
                        <Path Stretch="Uniform" Data="{Binding Source={StaticResource VerticalSyncIcon}, Path=Data}" Fill="{Binding Path=Foreground, RelativeSource={RelativeSource AncestorType={x:Type ToggleButton}}}" ></Path>
                    </ToggleButton>
                </DockPanel>
            </Grid>
        </Grid>

    </Grid>
</UserControl>

    
```







# XAML

see huggingface\ffmediaelement

see GitHub\echodict\WPF\WpfApp1 仿制品

see GitHub\gdscript\godot-subtitles-4.1_clone

## d:DesignHeight

```
mc:Ignorable="d" d:DesignHeight="700"
```

这段代码是XAML (eXtensible Application Markup Language) 属性的一部分，用来定义设计时的属性。让我为你解释每个部分的作用：

- `mc:Ignorable="d"`：这里的 `mc` 是XML命名空间的前缀，通常在XAML文件的顶部被定义，如 `xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"`。`Ignorable` 指示XAML处理器在运行时忽略特定前缀的所有属性。在这个例子中，"d" 前缀下的所有属性在运行时都将被忽略，只有在设计时才会被设计器工具（比如 Visual Studio 或 Blend）使用。

- `d:DesignHeight="700"`：再次见到 "d" 前缀，这表示 `DesignHeight` 是一个设计时属性，用于指示设计器在渲染控件时使用的假设高度。在本例中，设计时的高度被设置为700单位。这对于开发者在不运行应用程序的情况下，仅通过XAML编辑器查看和设计用户界面非常有用。

这些属性对实际运行的应用程序没有任何影响，因为它们在编译时会被忽略。它们只为提升设计时的体验而存在。



## Grid

```
        <Grid VerticalAlignment="Bottom">
            <Grid.RowDefinitions>
                <RowDefinition Height="30"></RowDefinition>
                <RowDefinition Height="40"></RowDefinition>
                <RowDefinition Height="70"></RowDefinition>
        </Grid.RowDefinitions>
        
        
                <Grid Width="500">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="100" />
                        <ColumnDefinition />
                        <ColumnDefinition />
                        <ColumnDefinition Width="100" />
                    </Grid.ColumnDefinitions>
                   		# 列定义, 两边各100，中间平分
        
```

- `Grid`: 这是使用的网格布局控件。
- `VerticalAlignment="Bottom"`: 这个属性设置了整个`Grid`垂直对齐方式，使得`Grid`会在其父容器内对齐到底部。



### 一定要加 Canvas

```
Grid 下面一定要加 Canvas, 否则会变小透明
<Canvas IsHitTestVisible="False" Background="{DynamicResource ShadedBackgroundBrush}" />
```





### 基础模板

```
# 新建用户控件 UserControl

    <Grid Name="Controls" Visibility="Visible" Height="250" Background="{x:Null}">

        <Grid VerticalAlignment="Bottom">
            <Grid.RowDefinitions>
                <RowDefinition Height="30"></RowDefinition>
                <RowDefinition Height="40"></RowDefinition>
                <RowDefinition Height="70"></RowDefinition>
            </Grid.RowDefinitions>

            <DockPanel Name="ProgressPanel" Grid.Row="1" LastChildFill="True" Margin="20,0">
                <Grid Width="500">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="100" />
                        <ColumnDefinition />
                        <ColumnDefinition />
                        <ColumnDefinition Width="100" />
                    </Grid.ColumnDefinitions>
                </Grid>
            </DockPanel>

        </Grid>

    </Grid>
```



### 列平分

```
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*" />
                    <ColumnDefinition Width="1*" />
                    <ColumnDefinition Width="1*" />
                </Grid.ColumnDefinitions>
```





## Window

```
WindowStartupLocation="Manual" MinHeight="720" Height="0" MinWidth="1280" Width="0"
Background="Black"
Title="MainWindow"
```



### 获取主窗口实例

```
# see echodict\WPF\WpfApp1\WpfApp1\UserControl1.xaml.cs
		private void Play_Button_Click(object sender, RoutedEventArgs e)
        {
            paly();
        }

        async void paly()
        {
            MainWindow main = (MainWindow)Application.Current.MainWindow;
            var target = new Uri(@"E:\videos\netflix\anime\japanese\Touch\Episode 1\Touch_S01E01_Episode 1.mp4");
            await main.Media.Open(target);
        }
```



#### 遍历窗口

```
using System.Linq;
using System.Windows;

public static Window GetFirstNonMainWindow()
{
    var mainWin = Application.Current.MainWindow;
    return Application.Current.Windows
        .OfType<Window>()
        .FirstOrDefault(win => win != mainWin);
}

```









## 全屏问题

[全屏问题](https://www.cnblogs.com/Naylor/p/17118993.html)







# 异步锁

[AsyncEx](https://github.com/StephenCleary/AsyncEx)



```
        private void Play_Button_Click(object sender, RoutedEventArgs e)
        {
            Action play = async () =>
            {
                var target = new Uri(@"E:\videos\netflix\anime\japanese\Touch\Episode 1\Touch_S01E01_Episode 1.mp4");
                await main.Media.Open(target);
            };
            play();
        }
```











[DMSkin](https://github.com/944095635/DMSkin)

[WPF 实现裁剪图像](https://v2ex.com/t/950084#)

[WPF UI](https://github.com/lepoco/wpfui)

[HandyControl](https://github.com/HandyOrg/HandyControl)





# CefSharp 读本地文件

```

see E:\huggingface_echodict\IPTV-Web-Player

see E:\huggingface_echodict\CefSharpPlayer\CefSharpPlayer\CefSharpPlayer.csproj

see E:\huggingface_echodict\Echodict\src\WpfEditor


	<ItemGroup>
		<PackageReference Include="CefSharp.Wpf.NETCore" Version="141.0.110" />
	</ItemGroup>

CefSharp.Wpf.NETCore 是一个将 Chromium 浏览器引擎嵌入到 .NET (WPF) 应用程序中的控件。如果你将这个网页打包成一个使用 CefSharp 的桌面客户端， 是可以实现直接读取本地文件而无需用户确认的 ，但需要进行特定的配置。

以下是详细分析：


1. 为什么 CefSharp 可以做到？
CefSharp 运行在你的桌面应用程序进程中，拥有与你的应用程序相同的本地文件系统访问权限。与运行在沙箱环境中的普通浏览器（如 Chrome/Edge）不同，CefSharp 允许开发者通过配置来 禁用 Web 安全限制 或 注册自定义协议 ，从而赋予网页代码访问本地文件的能力。


2. 如何实现（原理分析）
要实现“不弹窗直接读取文件”，通常有以下几种 CefSharp 配置方案：

- 方案 A：禁用 Web 安全策略（最简单但不推荐用于生产） 通过设置 CefSettings 或 BrowserSettings ：
  
  - WebSecurity = CefState.Disabled ：禁用同源策略。
  - FileAccessFromFileUrls = CefState.Enabled ：允许 file:// 协议访问其他 file:// 资源。
  - UniversalAccessFromFileUrls = CefState.Enabled ：允许 file:// 协议访问任何来源的资源。 效果 ：你的网页里的 JS 可以直接通过 file:///E:/Videos/movie.ts 这样的路径去加载文件，或者通过 XHR/Fetch 请求本地路径。
- 方案 B：注册自定义 Scheme（推荐） 你可以注册一个自定义协议（例如 local:// 或 myscheme:// ），并编写一个 C# 的 ISchemeHandlerFactory 。
  
  - 原理 ：当网页请求 local://videos/playlist.m3u8 时，CefSharp 会拦截这个请求，调用你的 C# 代码。你的 C# 代码可以直接从硬盘读取对应的文件流并返回给网页。
  - 优点 ：安全、可控。网页不需要知道绝对路径，只需要请求虚拟路径。
- 方案 C：对象绑定 (C# <-> JS Binding) 你可以将一个 C# 对象注入到 JavaScript 的 window 对象中。
  
  - 原理 ：JS 调用 window.myFileHelper.getFileContent('E:/video.ts') ，C# 端接收到调用后读取文件并返回数据（字符串或 Base64）。
  - 优点 ：可以实现极其灵活的逻辑。

```





# CefShap H.264

https://zhuanlan.zhihu.com/p/694014974 编译带H.264的cef(windows)



````

          
针对 CefSharp 不支持 H.264/AAC 的情况，最佳的转换方案是将视频转换为 **WebM 格式**（使用 **VP9** 或 **VP8** 视频编码，**Opus** 或 **Vorbis** 音频编码）。


推荐方案：转换为 WebM (VP9 + Opus)

这是目前兼容性最好的开源方案，CefSharp（基于 Chromium）原生支持这种格式，无需任何额外插件或授权。

鉴于目前的 `playlist.m3u8` 是分段视频，而 HLS 协议 (`.m3u8`) 通常绑定 MPEG-TS/fMP4 容器且对非 H.264 编码支持较差（且你的前端播放器使用了 `hls.js` 和 `mux.js`，它们主要针对 H.264/AAC 设计），最稳妥的方法是将整个播放列表**合并并转换为一个单一的 WebM 文件**。


1. 使用 FFmpeg 转换
请确保已安装 FFmpeg，然后在终端运行以下命令（将路径替换为你的实际路径）：

```powershell
ffmpeg -i "e:\huggingface_echodict\CefSharpPlayer\IPTV\TempVideo2\playlist.m3u8" -c:v libvpx-vp9 -c:a libopus "e:\huggingface_echodict\CefSharpPlayer\IPTV\TempVideo2\output.webm"
```

*   `-c:v libvpx-vp9`: 使用 VP9 视频编码（质量好，体积小，CefSharp 支持）。
*   `-c:a libopus`: 使用 Opus 音频编码（CefSharp 支持）。
*   此命令会自动读取 m3u8 中的所有 ts 分段并合并为一个文件。


2. 修改播放器逻辑 (core.js)
转换后，你将得到一个 `output.webm` 文件。由于原本的播放器逻辑（在 `core.js` 中）针对 `.ts` 文件使用了 `mux.js` 进行转码（transmux），这**不适用于 WebM 文件**。

你需要修改前端代码，在加载 `.webm` 文件时**直接播放**，跳过 `mux.js` 的处理：

*   **不要**将 `.webm` 文件重命名为 `.ts` 欺骗播放器，因为 `mux.js` 解析 WebM 数据时会报错。
*   在 `core.js` 中，直接将 WebM 文件的 URL 赋给 `video.src` 即可：
    ```javascript
    // 伪代码示例
    if (file.name.endsWith('.webm')) {
        video.src = URL.createObjectURL(file);
        video.play();
    }
    ```


为什么不推荐其他方案？
1.  **保持 .ts 后缀但改编码 (VP9 in TS)**: MPEG-TS 标准主要支持 H.264/MPEG2。虽然 FFmpeg 可以强制把 VP9 放入 TS，但浏览器和 `hls.js` / `mux.js` 极大概率无法解析这种非标组合。
2.  **HLS + WebM (DASH)**: 如果必须保留流式播放（切片），应该使用 **DASH** (`.mpd` + `.webm` 切片)，但这需要重新生成 manifest 文件并使用 `dash.js` 播放器，比单文件方案复杂得多。

**总结**：为了最快解决 CefSharp 播放问题，建议直接**转为单文件 WebM** 并直接播放**。


````



