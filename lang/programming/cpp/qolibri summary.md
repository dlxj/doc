

```cpp

qeb.cpp
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



