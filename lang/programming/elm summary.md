

[elm-graphql](https://github.com/dillonkearns/elm-graphql)



### 从无到有地创造几个元素，把这些元素组合成一个集合



```elm
type Thing = Something | SomethingElse

```



## 利用已经存在的几个元素，把这些元素组合成一个集合



```elm
type alias Location = { lat:Int, long:Int }
```





I found the simplest way to count matches in both Dicts is this:

```elm
Dict.size ( Dict.intersect dict1 dict2 )
```







