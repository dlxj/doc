

# XAML

see huggingface\ffmediaelement

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









[DMSkin](https://github.com/944095635/DMSkin)

[WPF 实现裁剪图像](https://v2ex.com/t/950084#)

[WPF UI](https://github.com/lepoco/wpfui)

[HandyControl](https://github.com/HandyOrg/HandyControl)







