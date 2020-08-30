

I found the simplest way to count matches in both Dicts is this:

```elm
Dict.size ( Dict.intersect dict1 dict2 )
```







