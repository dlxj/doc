

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



