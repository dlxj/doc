.因为新版的 `CocoaPods` 不允许用`pod repo add`直接添加`master`库



```ruby
$ cd ~/.cocoapods/repos
$ pod repo remove master
$ git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git master
```

2.在`podFile`第一行加上



```bash
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
```

3.最后记得`remove trunk` ，执行下面的命令



```csharp
pod repo remove trunk
```

4.更新依赖库



```undefined
pod install
```







sudo mount -uw /
>重启按 cmd+R  
>csrutil disable 
>sudo gem update --system

sudo gem install cocoapods
pod setup

cd $project$
pod install

rm -rf ~/.cocoapods
pod setup

cd ~/.cocoapods/repos/master/Specs
ls | grep PLMedia*，若为空，则需重新 update CocoaPods
pod repo 命令看下你是否更换过源
https://www.jianshu.com/p/cd057b2055c0

pod --version
gem source -l
gem sources --remove https://rubygems.org/
gem sources -a https://gems.ruby-china.com/
sudo gem install cocoapods
pod --version

https://www.jianshu.com/p/cd057b2055c0