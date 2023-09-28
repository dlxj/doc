
# lambda



`&|x: i32| x < 3` 是 Rust 中的 lambda 函数语法，也被称为闭包（closure）。闭包是一种可以捕获外部变量并在需要时执行的匿名函数。

- `&` 表示这是一个引用（reference），表示闭包将借用（borrow）外部变量而不获取所有权。
- `|x: i32|` 指定了闭包的参数列表。在这里，闭包有一个参数 `x`，它的类型是 `i32`。
- `x < 3` 是闭包的主体部分，它表示比较 `x` 是否小于 3，并返回结果。



f: &dyn Fn(T) -> bool

`&dyn` 表示 f 是一个动态函数的引用, 在编译时未知，直到调用才确定



```rust
// cargo new mmsgrs

pub fn filter<T: Copy>(array: Vec<T>, f: &dyn Fn(T) -> bool) -> Vec<T> {
    let mut result: Vec<T> = Vec::new();

    for index in 0..array.len() {
        let value = array[index];
        if f(value) {
            result.push(value);
        }
    }

    return result;
}

fn main() {
    let _tmp = filter([1, 2, 3, 4,5].to_vec(), &|x| x < 3);
    println!("Hello, world!");
}
```














let mut l = n.as_ref().unwrap().borrow_mut().left.take(); 



以往的编程语言经验阻碍了你的学习。Rust是混合范式，所以你可以看到OOP和函数式语言的影子。从其他语言转过来的人，因为有过往语言的经验，所以容易造成思维惯性。一上来就强行把Rust语言的概念和以往的知识进行关联。一些典型的问题比如，trait是什么呀？是不是接口？Rust怎么没有继承？等等。我在这里提醒大家，Rust的混合范式并非简单的oop或函数式范式的堆砌，它其实是一种**更加抽象的融合：类型+行为。trait就是行为的抽象，所以它既可以作为接口，又可以作为类型限定，甚至可以作为抽象类型**（打个比方，有时候你的行为决定了你是哪一类人）。所以，需要先对Rust有全面了解，才能明白它的混合范式到底是什么。



```
pub fn is_leap_year(year: i64) -> bool {
match (year % 4, year % 100, year % 400) {
(0, 0, 0) => true,
(0, 0, _) => false,
(0, _, _) => true,
(_, _, _) => false,
}
}

Exercism 上一个印象很深的求闰年的写法
```



# string

r#"您好！"#：原始字符串常量（字节数组），保留所有的字符
b"您好！"：字节字符串常量，使用默认编码进行保存
"您好！"：字符串常量，使用UTF-8进行编码保存

需要注意的是，在Rust中，默认字符串常量的编码方式是UTF-8。如果需要使用其他编码方式保存字符串常量，可以使用相应的字节字符串常量或指定编码格式。



在 Rust 中，有 `str` 和 `String` 两种类型，主要是因为它们具有不同的特性和用途。

1. **`str`**：
   - `str` 是一种字符串切片类型（string slice），它是一个不可变的字符串引用。
   - `str` 类型通常用于表示字符串的视图，在编程中经常用来访问、查找和操作字符串数据，而不需要拥有独立所有权。
   - `str` 数据通常以字面值（literal）或者通过 `&str` 借用得到。
2. **`String`**：
   - `String` 是一种拥有所有权的动态字符串类型，它是可变的，可以修改和扩展。
   - `String` 类型通常用于创建、修改和拥有自己的字符串数据。
   - `String` 对象可以通过 `String::from` 方法从其他类型（如`&str` 或字面值）转换而来，也支持使用 `+` 和 `+=` 运算符进行字符串连接。

所以，当你需要处理字符串数据时，如果仅需要对其进行查看或者临时引用，可以使用 `str` 类型。而当你需要对字符串进行修改、扩展或拥有单独的所有权时，应该使用 `String` 类型。



```rust
let mut v = String::new();
assert!(v.is_empty());

v.push('a');
assert!(!v.is_empty());
```





## utf32  转 utf8

```
    let hello = widestring::utfstring::Utf32String::from(widestring::utf32str!("一世皆尚同"));
    let tmp = hello.to_string();
```





# json

```
[dependencies]
csv = "1.2.2"
regex = "1.9.5"
serde_json = "1.0.107"

    let data = r#"
    {
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ]
    }"#;
    let v: serde_json::Value = serde_json::from_str(data).unwrap();
    println!("Please call {} at the number {}", v["name"], v["phones"][0]);



    let john = json!({
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ]
    });
    println!("first phone number: {}", john["phones"][0]);
    println!("{}", john.to_string());

```





# vector

```
# see echodict\mmsgrs\src\main.rs
	let jp_sequence: Vec<(String, usize)> = get_jp_sequence(&str);
    let not_jp_sequence: Vec<(String, usize)> = get_not_jp_sequence(&str);

    for (string, number) in &not_jp_sequence {
        println!("String: {}, Number: {}", string, number);
    }
    
    for v in &sequence {
        let seq = &v["seq"];
        let index = &v["index"];
        let typee = &v["type"];
        println!("{} {} {}", seq, index, typee);
    }
```





# TCP

- https://zhuanlan.zhihu.com/p/97200083
  - 使用Rust实现Tcp加速



