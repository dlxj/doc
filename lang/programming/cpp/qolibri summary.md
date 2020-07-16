





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



