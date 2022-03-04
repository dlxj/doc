

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

