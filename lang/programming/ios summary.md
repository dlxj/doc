

# ish postresql

- https://github.com/ish-app/ish/issues/833

```
apk add postgresql
su - postgres
mkdir /var/lib/postgresql/data
chmod 0700 /var/lib/postgresql/data
initdb -D /var/lib/postgresql/data
```



```
I am running PostgreSQL in a FreeBSD jail. The standard way to solve this in that environment is to add:

allow.sysvipc = 1;
```







# iSH Shell (termux)

https://zhuanlan.zhihu.com/p/299824345

https://www.v2ex.com/t/718503





```
wget -qO- http://dl-cdn.alpinelinux.org/alpine/v3.9/main/x86/apk-tools-static-2.10.6-r0.apk  | tar -xz sbin/apk.static && ./sbin/apk.static add apk-tools && rm sbin/apk.static && rmdir sbin 2> /dev/null
```



```
apk update
apk add git

```



```
# copy file
You’re gonna wanna go to /private/var/mobile/Containers/Shared/AppGroup on filza, find the container that is iSH’s, should be easy from there

iSH is available in the stock Files app. If your iDevice is jailbroken, you can look for apps' files in /User/containers

iPhone手机照片相对比较容易，默认路径为：/private/var/mobie/Media/DCIM/


mount -t ios website /mnt

on my ipad I was only able to mount my local Downloads folder.

```



```
Mounting other file providers - ish-app/ish Wiki
To mount other file providers in iSH, you can simply run

mount -t ios <src> <dst>
where <src> will be ignored and <dst> is where to mount the file

Upon running the command like

mount -t ios . /mnt
a file picker will show up and you may select which folder to mount.

Additionally, if jailbroken or using the psychic paper exploit (not available through TestFlight nor will we help you do it), you can also mount using real, absolute paths. To do so run:

mount -t real <src> <dst>
where <src> is the absolute path from the root of iOS and <dst> is the location in iSH to mount the file.

To mount the whole iOS file system into iSH’s /mnt run:

mount -t real / /mnt
To unmount when finished you can run:

umount <dir>
where <dir> is the directory where files were previously mounted.
```





```
tty-share # webbrowser 访问shell
```



# 越狱

https://dkxuanye.cn/?p=9772  多巴胺2.0越狱自动挂载系统目录



# 个人开发者

- https://www.v2ex.com/t/835778

```
楼上 @riordanw 说得已经非常全面了，个人目前是完全可以做的，同作为一个独立开发者，感觉对一些规则和政策还是相对熟悉一些，我补充一些细节吧。
AppStore 是对个人开发者最友好的平台了，只要你遵守平台规则，不乱搞（刷量刷好评盗版等等），获得一定曝光和新增还是很有希望的。其实在 AppStore 上，有大量的个人开发者，他们贡献了非常多的 App ，无论国内外开发者，都有做得非常厉害的产品。

Android 平台，个人可以 Google Play （国内用户少），华为（个人可以加广告，但是收费只能是企业账号），酷安。其他 OPPO 、ViVO 、小米，都只能企业账号，而且需要软著。

软著的话，在阿里云或者淘宝都能办，时间久一些，一般 30 天，你也可以去 “中国版权服务” 公众号上面，自己预约办理，稍微麻烦一些，因为需要准备很多材料，官网自己办理，也是最多 30 天（我自己是 22 天就拿到的）。

国内的广告平台，优量汇、穿山甲，均不支持个人申请接入，必须企业，所以比较蛋疼，也可以尝试一些广告联盟，比如 口袋工厂（ https://www.13lm.com/）,个人能够接入进去。
国外的话 就是 Admob 了。

广告具体的收益问题，我没法回答，没有相关经验，期待其他大佬来分享一下。

-------------------------

欢迎一起尝试做独立开发者，确实是一条比较艰难的路，而且国内相关信息有限，但归根结底，还是要自己走一遍，才能亲自体会到其中的辛酸与乐趣。
```



# MACOS



## 镜像下载

- https://www.applex.net/pages/macos/

- https://github.com/balena-io/etcher/releases

  > 烧录工具





