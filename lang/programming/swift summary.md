[TOC]



# Swift Summary

[Demo Todolist](https://github.com/theniceboy/Todolist-SwiftUI/issues/1)



> Option values  值有可能是nil 的变量，变量后面要加一个问号?
>
> > xx as? String ?? ” “  option强转String,  转不了就给个空串默认值
>



> $somevalue  传指针，期待被修改
>
> > DatePicker 的第二参日期变量



UInt64(0xffff_ffff_ffff_ffff) 



Code written at global scope is used as the entry point for the program, so you **don’t need a main() function**.

don’t need to import a separate library for functionality like input/output or string handling



```swift
let fruitSummary = "I have \(apples + oranges) pieces of fruit."
let quotation = """
I said "I have \(apples) apples."
And then I said "I have \(apples + oranges) pieces of fruit."
"""
```

“let s = 1.description”



## @state



对于 SwiftUI 视图来说，传统的**异步分发是不安全**的 —— 不要引火烧身



State属于SwiftUI架构，ObservableObject属于Combine架构

ObservableObject



### views are functions of their state



> 视图是state 的函数，也就是说视图是函数的结果，state 是函数的参数
> 想要修改视图不是直接对结果动手，而是要修改参数，既修改state





## $



指针，披着传值外套的指针就是引用



## 匿名函数



> 函数就是闭包

```
let mappedNumbers = numbers.map({ number in 3 * number })  // in 分隔了形参和函数体
print(mappedNumbers)

let sortedNumbers = numbers.sorted { $0 > $1 } // 第一参、第二参
print(sortedNumbers)
{1}()  // call and re 1
```



no return, three are legal

```
func say1(_ s:String) -> Void { print(s) }
func say2(_ s:String) -> () { print(s) }
func say3(_ s:String) { print(s) }
```





## List and Dictionary



```
let emptyArray = [String]()
let emptyDictionary = [String: Float]()
shoppingList = []
occupations = [:]
```



## Optional value



? 表示值可以为nil，?? 为nil 时提供默认值

```swift
if let name = optionalName {
    greeting = "Hello, \(name)"
}
let informalGreeting = "Hi \(nickName ?? fullName)"
```



## Function



### 参数由标签后接变量签名组成

```swift
func greet(_ person: String, on day: String) -> String {  // 
    return "Hello \(person), today is \(day)."
}
greet("John", on: "Wednesday")
```



## Protocol



### 继承协议确定类型

```swift
protocol Entertainment  {      
  associatedtype MediaType  
}
class Foo : Entertainment  {
  typealias MediaType = String //可以指定任意类型
}
```



继承只继承协议，传统继承的语义通过组合来实现。既**一个view 套在另一个view 里面**



## String



### multi-line strings

```
"""
a
b
"""

"""
a \
b \
"""
// 一个有换行，一个无换行
```



### interpolation

```
"a is \(v)"
```





## View 



### minimal protocol

```swift
import SwiftUI

struct iHome: View {
    var body: some View {
        ZStack {
            Spacer()
        }
    }
}

#if DEBUG
struct iHome_Previews: PreviewProvider {
    static var previews: some View {
        iHome()
    }
}
#endif
```



### the *safe area*

an area where they can’t be covered up by system UI or device rounded corners





### 是看得见摸得着的对象（Touchable）

A view may come from a nib, or you can create it in code. 



启动时窗口被创建并显示，否则就是黑屏一片。view 是windows 的下一级。

Windows 组成了可视部分的整个背景，是所有view 的superview

IOS 13 起，ipad 可以有多窗口，iphone 只能有一个窗口





- view



## VStack 竖排


```swift
VStack {
	Text("Hello, World!")
  Text("Hello, World!")
}
```

### Form

Forms are regular containers just like VStack, so you can switch between the two freely depending on your purpose.



## ZStack 垂直排





## Space



```swift
Spacer().frame(height:20)  // 加点小空档
```





## Text



### padding, background, foregroundColor

###  font(.title)

### text binding

```
TextField 
init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit: () -> Void)
```





## Enum



![image-20200531164947473](swift summary.assets/image-20200531164947473.png)

```swift
enum Planet: Int {
    case mercury  // 默认从零开始，也可以显示给第一项赋值 xx = 1
    case venus
    case earth
    case mars
}
let earth = Planet(rawValue: 2)
```





### 文本过长用省略号代替

```text
lineLimit(nil)
```



### 文本过长自动缩小并显示

```text
minimumScaleFactor(0.3)
```



### 多行文本对齐

```text
.multilineTextAlignment(.leading)
```





## Navigation



### Hide navigation

```swift
.navigationBarHidden(true)
.navigationBarTitle(Text("Home"))
.edgesIgnoringSafeArea([.top, .bottom])
```







## Button

### cornerRadius, shadow

```swift
        VStack {
            Text("Hello, World!")
            Button(action:{
                
            }){
                Text("屠龙宝刀点击就送！")
                .padding() // 文本外围胖一圈
                    .background(Color.blue)
                    .foregroundColor(.white)
            }
            .cornerRadius(10) // 按钮加圆角效果
            .shadow(radius: 10) // 按钮加外围阴影
        }
```



### forbidden click

```swift
disabled(true)
```









##  Class



### restore data on startup

- 继承 NSObject, NSCoding, Identifiable



```swift
class Todo:NSObject, NSCoding, Identifiable
```





## System



### hide keyboard

```swift
UIApplication.shared.keyWindow?.endEditing(true)
```



nibs, outlets, and actions, and the mechanics of nib loading

