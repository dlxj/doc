[TOC]



# Swift Summary



> Option values  值有可能是nil 的变量，变量后面要加一个问号?
>
> > xx as? String ?? ” “  option强转String,  转不了就给个空串默认值
>



> $somevalue  传指针，期待被修改







## VStack 竖排


```swift
VStack {
	Text("Hello, World!")
  Text("Hello, World!")
}
```





## ZStack 垂直排 





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



