



eb_set_hooks  搜这个

Ａ級



先删除缓存

/Users/vvw/Library/Caches/qolibri/ＮＨＫ　日本語発音アクセント辞典

>font	image	mpeg	wave



201297x1630.wav  # 先生成这个

12284x419.jpeg      # 再生成这个





实验代码写这里



```c++
// 图片能正常断下来，看看自已写的代码能否断下来？
void MainWindow::viewSearch()
	viewSearch(str, model->method);
		// 实验代码写这里
		
		QByteArray EbCore::hookBeginInColorJpeg(int, const unsigned int *argv)
			// 用自已的代码替换这个函数
		QByteArray EbCore::hookEndInColorGraphic(int, const unsigned int*)
      // 用自已的代码替换这个函数
      
```





搜索入口

```c++
void MainWindow::viewSearch()
	viewSearch(str, model->method);

// 断这里
QByteArray EbCore::hookBeginWave(int, const unsigned int *argv)

 
```





```c++
EbCore::EbCore(HookMode hmode) : QEb()
	setHooks(hooks);

ebhook.cpp
	HOOK_FUNC(BEGIN_WAVE, EbCore, hookBeginWave)
	HOOK_FUNC(END_WAVE, EbCore, hookEndWave)

```



```c++
// 一切的开始
qolibri.cpp
int main(int argc, char *argv[])
	QApplication app(argc, argv);
	int ret = app.exec();
```



```c++
// 初始化
EbCore::EbCore(HookMode hmode) : QEb()
    initializeBook();
    initializeAppendix();
    initializeHookset();
```



```c++
// 遍历词条的方法
QList <EB_Hit> hits;  // 存所有命中的位置
int count = 0;

EB_Position pos;
eb_text(&book, &pos);  // first word position

EB_Hit hit;
hit.heading = pos;
hit.text = pos;
hits << hit;  // 存进链表
count++;

eb_seek_text(&book, &pos);
eb_forward_text(&book, &appendix);



```





手动触发

```c++
// ebhook.cpp
EB_Error_Code iHookBEGIN_IN_COLOR_JPEG(EB_Book *book, EB_Appendix*,
    void *classp, EB_Hook_Code, int argc, const unsigned int* argv)
{
    EbCore *p = static_cast<EbCore*>(classp);
    QByteArray b =  p->hookBeginInColorJpeg(argc,argv);
    if (!b.isEmpty()) {
        return eb_write_text_string(book, b);
    } else {
        return EB_SUCCESS;
    }
}

EB_Hook hooks[] = {
  { EB_HOOK_BEGIN_IN_COLOR_JPEG, iHookBEGIN_IN_COLOR_JPEG },
  { EB_HOOK_NULL, NULL }
}

    EB_Book book;
    EB_Appendix appendix;
    EB_Hookset hookset;
    EB_BookList bookList;

    eb_initialize_book(&book);
    eb_initialize_appendix(&appendix);
    eb_initialize_hookset(&hookset);

		EB_Error_Code ecode;
		ecode = eb_set_hooks(&hookset, hooks);
		ecode = eb_bind(&book, 
            	QString("/Users/vvw/Documents/dic/NHK").toLocal8Bit());  
				// path.toUtf8();
		
		
		
		EB_Subbook_Code codes[EB_MAX_SUBBOOKS];
    int cnt;

    QList <EB_Subbook_Code> list;
    ecode = eb_subbook_list(&book, codes, &cnt);
		
		ecode = eb_set_subbook(&book, codes[0]);
		


```





## QT Creator 导入CMakelist.txt 既可生成项目文件

```
EB_Error_Code ecode = eb_set_hooks(&hookset, hooks);
```

```cpp
unning /usr/local/Cellar/cmake/3.18.0/bin/cmake /Users/vvw/Documents/qolibri '-GCodeBlocks - Unix Makefiles' -DCMAKE_BUILD_TYPE:STRING=Debug -DCMAKE_CXX_COMPILER:STRING=/usr/bin/clang++ -DCMAKE_C_COMPILER:STRING=/usr/bin/clang -DCMAKE_PREFIX_PATH:STRING=/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64 -DQT_QMAKE_EXECUTABLE:STRING=/Users/vvw/usr/local/Qt5.14.2/5.14.2/clang_64/bin/qmake in /private/var/folders/62/j3_wjvp97n30cs5sd9pxs3zc0000gn/T/QtCreator-LxOSNf/qtc-cmake-xgVaEUaB.
-- The C compiler identification is AppleClang 11.0.3.11030032
-- The CXX compiler identification is AppleClang 11.0.3.11030032
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    QT_QMAKE_EXECUTABLE


-- Build files have been written to: /private/var/folders/62/j3_wjvp97n30cs5sd9pxs3zc0000gn/T/QtCreator-LxOSNf/qtc-cmake-xgVaEUaB
```







```cpp

eb_search_keyword(&book, wlist);

qeb.cpp
  ecode = eb_menu(&book, &pos);
  QString t;
  candidate(pos, &t)
    candidate(const EB_Position &pos, QString *txt)
      *txt = text(pos)
      	 eb_seek_text(&book, &pos)
           

QString QEb::readText(void *para, bool hook_flag)
{
    char buff[1024+1];
    ssize_t len;
    QByteArray b;
    for(;;) {
        EB_Error_Code ecode;
        if (hook_flag)
            ecode = eb_read_text(&book, &appendix, &hookset, para,
                                 1024, buff, &len);
        else
            ecode = eb_read_text(&book, &appendix, NULL, para,
                                 1024, buff, &len);
        if (ecode != EB_SUCCESS) {
            dispError("eb_read_text", ecode);
            break;
        }
        if (len > 0)
            b += QByteArray(buff, (int)len);
        if (isTextStopped())
            break;
        //if (len < 1024)
        //    break;
    }
    return b;

}

EB_Position QEb::startText()
{
    EB_Position pos;
    EB_Error_Code ecode = eb_text(&book, &pos);  # 获得pos
    if (ecode != EB_SUCCESS) {
        dispError("eb_text", ecode);
        return invalidPosition();
    }
    return pos;
}    

QEb::seekText(const EB_Position &pos)  # 根据pos 获得文本


EB_Error_Code QEb::setBinaryWave(const EB_Position &start, EB_Position &end)
{
    EB_Error_Code ecode = eb_set_binary_wave(&book, &start, &end);
    if (ecode != EB_SUCCESS)
        dispError("eb_set_binary_wave", ecode);
    return ecode;
}
QByteArray QEb::readBinary()
{
    char buff[1024];
    ssize_t len;
    QByteArray b;
    for(;;) {
        EB_Error_Code ecode = eb_read_binary(&book, 1024, buff, &len);
        if (ecode != EB_SUCCESS) {
            dispError("eb_read_binary", ecode);
            return b;
        }
        if (len > 0 )
            b += QByteArray(buff, (int)len);
        if (len < 1024)
            break;
    }
    return b;
}
```





```cpp

ebcore.cpp
QByteArray EbCore::hookBeginWave(int, const unsigned int *argv)
{
    // argv[2] : start page
    // qrgv[3] : start offset
    // qrgv[4] : end page
    // argv[5] : end offset
    QByteArray fname = binaryFname("wav", argv[2], argv[3]);
    QByteArray out = "<a class=snd href=\"sound?" +
                     ebCache.waveCachePath.toUtf8() + "/" + fname + "\">";
    if (ebCache.waveCacheList.contains(fname))
        return out;

    EB_Position spos;
    spos.page = argv[2];
    spos.offset = argv[3];
    EB_Position epos;
    epos.page = argv[4];
    epos.offset = argv[5];
    if (setBinaryWave(spos,epos) != EB_SUCCESS)
        return errorBStr("Image(wave) Error") + "<a>";

    QByteArray image = readBinary();
    if (image.isEmpty())
        return errorBStr("Image(wave) Error") + "<a>";

    if(!makeBinaryFile(ebCache.waveCachePath + '/' + fname, image))
        return errorBStr("Image(wave) Write Error") + "<a>";

    ebCache.waveCacheList << fname;

    return out;
}
```



