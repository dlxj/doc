[TOC]



# Swift Summary



> Option values  值有可能是nil 的变量，变量后面要加一个问号?
>
> > xx as? String ?? ” “  option强转String,  转不了就给个空串默认值
>
> 





## VStack 竖排


```swift
VStack {
	Text("Hello, World!")
  Text("Hello, World!")
}
```



## Text

### padding, background, foregroundColor



## Button

### cornerRadius, shadow

```swift
            Button(action:{
                
            }){
                Text("屠龙宝刀点击就送！")
                .padding() // 文本外围胖一圈
                    .background(Color.blue)
                    .foregroundColor(.white)
            }
            .cornerRadius(10) // 按钮加圆角效果
            .shadow(radius: 10) // 按钮加外围阴影
```



##  Class



### Restore data from startup

- 继承 NSObject, NSCoding



