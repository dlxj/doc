

## 传参

Product->Scheme->Edit Scheme，弹出一个对话框如下，在Run->Arguments



## xcode 编译QT 项目



1. 先用QT Creator 建一个空项目
2. 添加main.cpp 等源文件并保证通过编译，正常运行
3. qmake 生成makefile
4. qmake 生成xcode 工程

```
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -o makefile eblib2.pro
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -spec macx-clang
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake && make -j4
/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake -spec macx-xcode
```







[macOS - Compile QT5 Project in Xcode 7+(2019)](https://gist.github.com/xul76/1a13f9743b4a5ce4c2246b8bdc6f2029)

https://gist.github.com/xul76/1a13f9743b4a5ce4c2246b8bdc6f2029



```
/ * 
     *  macOS - Compile QT5 Project in Xcode [7+] (2019)
   / *
   
   
   This method of building (compiling) a QT 5.x project in Xcode [7+] on macOS requires:
   
   
      o QT 5.x (recommended: 5.9.7)
      o Xcode 7.2+ (other versions might work as well)
   
   
   The result of this is that you will create a .xcodeproj file in the same folder as your <project>.pro file. This file
   allows you to edit- and build QT C++ projects in Xcode.
   
   
   Note: Replace "<username>" in the following commands with your macOS username.
         If you have installed QT in a different folder: replace paths accordingly.
   
   
   1. Open a Terminal
   
   2. # cd <qt project folder>
   
   3. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake -o makefile <project>.pro
   
   4. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake -spec macx-clang
   
   5. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake && make -j4
        ... ! DO NOT CLEAN AFTER BUILDING !
   
   6. # /Users/<username>/Qt5.9.7/5.9.7/clang_64/bin/qmake -spec macx-xcode
   
   7. Open .xcodeproj file in Xcode
   
   8. You will see a warning asking you if you want to update this project file with new values.
      Press "Update"
      
   9. Click on your Project (top of File Explorer in Xcode)
   
  10. Click on "Build Settings"
  
  11. Under "Build Locations", correct paths that have double slashes
   
  12. ???
  
  13. PROFIT
  
  +xuL
```

