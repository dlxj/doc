



eb_set_hooks  搜这个

Ａ級



先删除缓存

/Users/vvw/Library/Caches/qolibri/ＮＨＫ　日本語発音アクセント辞典

>font	image	mpeg	wave



搜索入口

```
void MainWindow::viewSearch()
	viewSearch(str, model->method);
```





```c++
EbCore::EbCore(HookMode hmode) : QEb()
	setHooks(hooks);

ebhook.cpp
	HOOK_FUNC(BEGIN_WAVE, EbCore, hookBeginWave)
	HOOK_FUNC(END_WAVE, EbCore, hookEndWave)

```





## QT Creator 导入CMakelist.txt 既可生成项目文件



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



