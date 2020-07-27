

https://wiki.qt.io/Building_Qt_5_from_Git



qt 5.15 dependency

https://doc.qt.io/qt-5/linux-requirements.html



https://doc.qt.io/qt-5/linux-building.html

https://download.qt.io/archive/qt/5.15/5.15.0/single/



sudo apt-cache search libgl | grep dev



./configure -no-opengl



```
sudo apt-get build-dep qt5-default
sudo apt-get install libxcb-xinerama0-dev 
```



windows-10-enable-ntfs-long-paths-policy-option-missing



```
Qt WebEngine Build Tools:
  Use System Ninja ....................... no
  Use System Gn .......................... no
  Jumbo Build Merge Limit ................ 8
  Developer build ........................ no
  QtWebEngine required system libraries:
    fontconfig ........................... no
    dbus ................................. no
    nss .................................. no
    khr .................................. no
    glibc ................................ yes

```



libfontconfig1-dev



## String



```cpp

char buffer[ EB_MAX_PATH_LENGTH + 1 ];

QTextCodec * codec_ISO, * codec_GB, * codec_Euc;
codec_ISO = QTextCodec::codecForName( "ISO8859-1" );
codec_GB = QTextCodec::codecForName( "GB2312" );
codec_Euc = QTextCodec::codecForName("EUC-JP");

QString title = codec_Euc->toUnicode( buf ); // QString

QByteArray array = string.toLocal8Bit();
char* buffer = array.data();

QString subbook_dir = QString::fromLocal8Bit( buffer );

QByteArray 可以直接传给QString 的构造函数

```



## Version change



```
fix: Qt::SkipEmptyParts is avalible since Qt5.14
refactor: replace qrand() with QRandomGenerator
refactor: replace QMap with QMultiMap
refactor: replace QTextStream& QTextStreamFunctions::endl(QTextStream&) with Qt::endl
refactor: replace QString::SkipEmptyParts with Qt::SkipEmptyParts
refactor: replace QProcess::execute(const QString&) with QProcess::execute(const QString &program, const QStringList &arguments)
refactor: replace QList::swap() with QList::swapItemsAt()
```



You have the latest version of `qt5-default` package available from Ubuntu repositories [qt5-default (5.9.5+dfsg-0ubuntu1)](https://packages.ubuntu.com/bionic/qt5-default). To install the `5.10.x` version you should follow the instructions described on the official website : [Install Qt 5 on Ubuntu](https://wiki.qt.io/Install_Qt_5_on_Ubuntu)

The installation file can be downloaded from [here](http://download.qt.io/official_releases/qt/5.10/).

The `5.10.0` version:

```
wget http://download.qt.io/official_releases/qt/5.10/5.10.0/qt-opensource-linux-x64-5.10.0.run
```

The `5.10.1` version:

```
wget http://download.qt.io/official_releases/qt/5.10/5.10.1/qt-opensource-linux-x64-5.10.1.run
```

to set qt 5.10 as default edit:

```
sudo nano /usr/lib/x86_64-linux-gnu/qtchooser/default.conf
```

with the following line (replace $USER with your username):

```
/home/$USER/Qt5.10.0/5.10.0/gcc_64/bin
/home/$USER/Qt5.10.0/5.10.0/gcc_64/lib
```

then run:

```
qtchooser -print-env
qmake -v
```