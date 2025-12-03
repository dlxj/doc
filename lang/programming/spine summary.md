

https://zh.esotericsoftware.com/spine-examples-mix-and-match  spine 换装动画



https://zh.esotericsoftware.com/spine-twitch  教程直播 PNGTuber



```

动态皮肤混合（推荐用于复杂换装）
这是实现自由搭配最常用的方法。其思路是创建一个新的空白皮肤，然后像“拼积木”一样，将各个部位的皮肤（如基础皮肤、发型、上衣、下装）按顺序添加进去。



// 获取骨架数据
var skeletonData = skeleton.Skeleton.Data;
// 创建一个新的空皮肤，用于混合
Spine.Skin mixedSkin = new Spine.Skin("custom-character");
// 将各个部位的皮肤添加到混合皮肤中（顺序可能影响显示层级）
mixedSkin.AddSkin(skeletonData.FindSkin("skin-base")); // 基础身体
mixedSkin.AddSkin(skeletonData.FindSkin("hair/blue")); // 发型
mixedSkin.AddSkin(skeletonData.FindSkin("clothes/dress-green")); // 上衣
// 将混合好的皮肤设置给角色
skeleton.Skeleton.SetSkin(mixedSkin);
skeleton.Skeleton.SetSlotsToSetupPose();

```

