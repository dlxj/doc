





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



