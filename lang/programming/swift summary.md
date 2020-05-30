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



## 匿名函数



> 函数就是闭包

```
let mappedNumbers = numbers.map({ number in 3 * number })  // in 分隔了形参和函数体
print(mappedNumbers)

let sortedNumbers = numbers.sorted { $0 > $1 } // 第一参、第二参
print(sortedNumbers)
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





## VStack 竖排


```swift
VStack {
	Text("Hello, World!")
  Text("Hello, World!")
}
```





## ZStack 垂直排 





## Space



```swift
Spacer().frame(height:20)  // 加点小空档
```





## Text



### padding, background, foregroundColor



### text binding

```
TextField 
init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit: () -> Void)
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



