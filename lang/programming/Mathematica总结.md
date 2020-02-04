$Version

- 显示版本号



sameQ :=(Length[#1 \[Intersection] #2]  == Length[ #1])&
sameQ[{1,2,3}, {1,3,2}]

用交集来判断集合是否相等？





