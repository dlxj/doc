
/*

for ubuntu:

gcc -shared -static-libgcc -static-libstdc++ -o ./libs/libiplay.so \
	iplay.c -I/opt/host/usr/include -I/opt/host/usr/include/alsa -I/root/koreader/koreader-base/luajit-2.0/src/ \
  -L/opt/host/usr/lib -lasound -lpthread -lm -lrt -ldl


for k3:

arm-none-linux-gnueabi-gcc -shared -static-libgcc -static-libstdc++ -o ./libs/libiplay.so \
	iplay.c -I/usr/include -I/usr/include/alsa -I/root/koreader/koreader-base/luajit-2.0/src/ \
  -L/opt/host/usr/lib -lasound -lpthread -lm -lrt -ldl

*/

#include "sq.c"
#include <alsa/asoundlib.h>
#include "lua.h"
#include "lauxlib.h"


struct WavInfo {
    int numChannels;    // 声道数
    int sampleRate;     // 采样率，一秒多少个样本
    int bitsPerSample;  // 每个样本多少位
    int numSamples;     // 每个声道有多少个样本
    int totalSamples;   // 总共有多少个样本
    int subchunk2Size;  // = 整个文件大小 - 文件头大小  // 既是纯音频数据的大小 // = 所有样本的字节数
    int hacking;
};
typedef struct WavInfo WavInfo;

static char *dataPcm(char *fname, int *out_siz_buf) {
    return data(fname, out_siz_buf);
}

static char *readbuf(char *buf, int sizbuf, int nread, bool setnew, int newoffset) {  // readbuf 函数内部保存有一个读取偏移量，每次读一个新buf 的时侯记得重置为0
    static int offset = 0;
    static char tmp[512];
    memset(tmp, 0, sizeof(tmp));
    if (nread > 512) { ERR("Error in readbuf(). too many to read.");  };
    if ( (offset + nread) > sizbuf ) { ERR("Error in readbuf(). reading out of bounds."); };
    if (setnew) offset = newoffset;
    memcpy(tmp, buf+offset, nread);
    offset = offset + nread;
    return tmp;
}

static bool isWavBuf(char *buf, int siz) {
    int NumChannels, SampleRate, ByteRate, BlockAlign, BitsPerSample, Subchunk2Size, NumSamples, totalSamples;
    if (siz < 44) return false;
    char *riff = readbuf(buf, siz, 4, true, 0);  // readbuf 函数内部保存有一个读取偏移量，每次读一个新buf 的时侯记得重置为0
    if (strcmp(riff, "RIFF") != 0) return false;
    NumChannels = (*(short*)readbuf(buf, siz, 2, true, 22));     // 声道数
    SampleRate = (*(int*)readbuf(buf, siz, 4, false, -1));       // 采样率，一秒多少个样本
    ByteRate = (*(int*)readbuf(buf, siz, 4, false, -1));
    BlockAlign = (*(short*)readbuf(buf, siz, 2, false, -1));
    BitsPerSample = (*(short*)readbuf(buf, siz, 2, false, -1));  // 每个样本多少位
    Subchunk2Size = (*(int*)readbuf(buf, siz, 4, true, 40));     // NumSamples * NumChannels * BitsPerSample/8  -- 可以理解成后面的纯音频数据有多少字节  --
                                                                    // Subchunk2Size == 整个文件大小 - 文件头大小  -- 既是纯音频数据的大小

    if (BitsPerSample < 8) { LOG("Warning in isWavBuf(): BitsPerSample < 8"); }

    totalSamples = Subchunk2Size * 8 / BitsPerSample;               // 总共有多少个样本
    NumSamples = totalSamples / NumChannels;    // 每个声道有多少个样本
    if ( Subchunk2Size != (siz - 44 ) ) {
        if ( Subchunk2Size < (siz - 44 ) ) { LOG("Warning in isWavBuf(): size of WAV file not correct! may be have some additional stuff."); }
        if ( Subchunk2Size > (siz - 44 ) ) {
            LOG("Error format: size of WAV file not correct! may be audio data not complete.");
            return false;
        }
    }
    if ( (Subchunk2Size * 8) != (NumSamples * NumChannels * BitsPerSample) ) return false;
    return true;
}

static WavInfo wavInfo(char* buf, int siz) {
    WavInfo info;
    info.hacking = 0;
    if ( !isWavBuf(buf, siz) ) { ERR("Error in wavInfo(). not a wav buf");}
    info.numChannels = (*(short*)readbuf(buf, siz, 2, true, 22));
    info.sampleRate = (*(int*)readbuf(buf, siz, 4, false, -1));          // 采样率，一秒多少个样本
    int ByteRate = (*(int*)readbuf(buf, siz, 4, false, -1));
    int BlockAlign = (*(short*)readbuf(buf, siz, 2, false, -1));
    info.bitsPerSample = (*(short*)readbuf(buf, siz, 2, false, -1));     // 每个样本多少位
    info.subchunk2Size = (*(int*)readbuf(buf, siz, 4, true, 40));        // NumSamples * NumChannels * BitsPerSample/8  -- 可以理解成后面的纯音频数据有多少字节  --
                                                                         // Subchunk2Size == 整个文件大小 - 文件头大小  -- 既是纯音频数据的大小

    info.totalSamples = info.subchunk2Size * 8 / info.bitsPerSample;  // 总共有多少个样本
    info.numSamples   = info.totalSamples / info.numChannels;            // 每个声道有多少个样本

    if ( (info.subchunk2Size * 8) != (info.numSamples * info.numChannels * info.bitsPerSample) ) { ERR("ERR in wavInfo(). subchunk2Size not correct."); }
    if (info.subchunk2Size == 22) {
        // 不规范的文件头，这里先用hacking 的方法应付之
        // to do: fix this and remove hacking
        DBLOG("Warning: info.subchunk2Size = %d in function %s()", info.subchunk2Size, __func__);
        char * dataflag =  (char*)readbuf(buf, siz, 4, true, 0x42);
        DBLOG("#############%s###############",dataflag);
        if (strcmp(dataflag, "data") == 0 ) {
            int newsubchunk2Size = (*(int*)readbuf(buf, siz, 4, false, -1));
            DBLOG("#############new subchunk2Size = %d###############", newsubchunk2Size);
            LOG("Warning: now, use hacking set this size to new subchunk2Size");
            info.subchunk2Size = newsubchunk2Size;
            info.hacking = 0x4A;
        }
    }
    return info;
}

static char *dataWavFromBuf(char *buf, int siz, int *out_siz_buf, WavInfo *out_info) {
    char *tmpbuf;
    if (! isWavBuf(buf, siz) ) DBERR("not a wav buf. in %s", __func__);
    *out_info = wavInfo(buf, siz);
    tmpbuf = (char*) malloc(out_info->subchunk2Size);
    if (out_info->hacking == 0)
        memcpy(tmpbuf, buf+44, out_info->subchunk2Size);  // wav data size = 44 byte of header + pure audio data
    else
        memcpy(tmpbuf, buf+out_info->hacking, out_info->subchunk2Size);
    *out_siz_buf = out_info->subchunk2Size;
    return tmpbuf;
}

static char *dataWav(char *fname, int *out_siz_buf, WavInfo *out_info) {
    char *buf;
    int tmpsiz;
    char *tmpbuf = data(fname, &tmpsiz);
    buf = dataWavFromBuf(tmpbuf, tmpsiz, out_siz_buf, out_info);
    free(tmpbuf);
    return buf;
}

static bool isWavfile(char *name) {
    bool re;
    char *buf; int siz;
    buf = data(name, &siz);
    re = isWavBuf(buf, siz);
    free(buf);
    return re;
}

static void setParams(snd_pcm_t *handle,
               unsigned int nchannel, unsigned int nbit_per_simple, unsigned int samplerate,
               int *out_nframe_per_play, snd_pcm_format_t *out_format)
{
    snd_pcm_hw_params_t *hwparams;
    snd_pcm_format_t format;
    unsigned int exact_rate, exact_rate_orig;
    unsigned int buffer_time, period_time;
    snd_pcm_uframes_t chunk_size;
    snd_pcm_uframes_t buffer_size;
    unsigned int bits_per_sample;  unsigned int bits_per_frame;

    switch (nbit_per_simple) {
        case 4:
            ERR("ERR in playPcm(). bitsPerSample is 4 bit, not support yet!");
            break;
        case 8:
            format = SND_PCM_FORMAT_U8;
            break;
        case 16:
			format = SND_PCM_FORMAT_S16;
			break;
		case 24:
			format = SND_PCM_FORMAT_S24;
			break;
		case 32:
			format = SND_PCM_FORMAT_S32;
			break;
    }

    if (snd_pcm_format_physical_width(format) != nbit_per_simple) ERR("Err in SNDWAV_SetParams() snd_pcm_format_physical_width(format) != nbit_per_simple");
    *out_format = format;

    //sndpcm->channels = nchannel;
    exact_rate = samplerate; exact_rate_orig = exact_rate;

    /* Allocate the snd_pcm_hw_params_t structure on the stack. */
    snd_pcm_hw_params_alloca(&hwparams);

    /* Init hwparams with full configuration space */
    if (snd_pcm_hw_params_any(handle, hwparams) < 0) ERR("Error snd_pcm_hw_params_any/n");

    if (snd_pcm_hw_params_set_access(handle, hwparams, SND_PCM_ACCESS_RW_INTERLEAVED) < 0) ERR("Error snd_pcm_hw_params_set_access/n");

    if (snd_pcm_hw_params_set_format(handle, hwparams, format) < 0) ERR("Error snd_pcm_hw_params_set_format/n");

    /* Set number of channels */
    if (snd_pcm_hw_params_set_channels(handle, hwparams,  nchannel) < 0) ERR("Error snd_pcm_hw_params_set_channels/n");

    /* Set sample rate. If the exact rate is not supported */
    /* by the hardware, use nearest possible rate.         */
    if (snd_pcm_hw_params_set_rate_near(handle, hwparams, &exact_rate, 0) < 0) ERR("Error snd_pcm_hw_params_set_rate_near/n");
    if (exact_rate != exact_rate_orig) DBERR("The rate %d Hz is not supported by your hardware./n ==> Using %d Hz instead./n",exact_rate_orig, exact_rate);

    if (snd_pcm_hw_params_get_buffer_time_max(hwparams, &buffer_time, 0) < 0) ERR("Error snd_pcm_hw_params_get_buffer_time_max/n");
    if (buffer_time > 500000) buffer_time = 500000;
    period_time = buffer_time / 4;

    if (snd_pcm_hw_params_set_buffer_time_near(handle, hwparams, &buffer_time, 0) < 0) ERR("Error snd_pcm_hw_params_set_buffer_time_near/n");
    if (snd_pcm_hw_params_set_period_time_near(handle, hwparams, &period_time, 0) < 0) ERR("Error snd_pcm_hw_params_set_period_time_near/n");
    if (snd_pcm_hw_params(handle, hwparams) < 0) ERR("Error snd_pcm_hw_params(handle, params)/n");

    snd_pcm_hw_params_get_period_size(hwparams, &chunk_size, 0);
    snd_pcm_hw_params_get_buffer_size(hwparams, &buffer_size);
    *out_nframe_per_play = chunk_size;
    if (chunk_size == buffer_size) DBERR("Can't use period equal to buffer size (%lu == %lu)/n", chunk_size, buffer_size);
}

static void play_pcm(snd_pcm_t *handle, char *buf, int siz, int nframe_per_play, int nbyte_per_frame) {

    int written = 0;
    int nbyte_per_play = nframe_per_play * nbyte_per_frame;

    DBLOG("pcm data siz = %d bytes", siz);

    while (written < siz) {
        int nframe; int res;
        res = siz - written;
        if (res < nbyte_per_play) {
            //LOG("res < nbyte_per_play");
            break;
        } else {
            nframe = snd_pcm_writei(handle, buf+written, nbyte_per_play);
        }

        if (nframe > 0) {
            written = written + (nframe * nbyte_per_frame);
        }

        if (nframe == -EAGAIN || (nframe >= 0 && nframe < nframe_per_play)) {
            snd_pcm_wait(handle, 1000);
        } else if (nframe == -EPIPE) {
            snd_pcm_prepare(handle);
            LOG("############ Buffer Underrun ############");
        } else if (nframe == -ESTRPIPE) {
            LOG("############ Need suspend ############");
        } else if (nframe < 0) {
            DBERR("Error snd_pcm_writei: '%s'", snd_strerror(nframe));
        }
    }
}

static void init_device(snd_pcm_t **out_handle, char *devicename, int nchannel, int nbit_per_simple,
                    int samplerate, int *out_nframe_per_play, int *out_nbyte_per_frame, snd_pcm_format_t *out_format) {
    if (snd_pcm_open(out_handle, devicename, SND_PCM_STREAM_PLAYBACK, 0) < 0) DBERR("Error snd_pcm_open [ %s]/n", devicename);
    setParams(*out_handle, nchannel, nbit_per_simple, samplerate, out_nframe_per_play, out_format);
    int bits_per_frame = nbit_per_simple * nchannel;
    *out_nbyte_per_frame = bits_per_frame / 8;
}

static void close_device(snd_pcm_t *handle) {
    snd_pcm_drain(handle);
    snd_pcm_close(handle);
}

static void playPcm_(char *buf, int siz,
              int nchannel, int nbit_per_simple, int samplerate) {
    snd_pcm_t *handle;
    int nframe_per_play, nbyte_per_frame;
    snd_pcm_format_t format;

    init_device(&handle, "default",
                nchannel, nbit_per_simple, samplerate,
                &nframe_per_play, &nbyte_per_frame, &format);
    int i;
    play_pcm(handle, buf, siz, nframe_per_play, nbyte_per_frame);

    close_device(handle);
}

static void playPcm(char *fname, int nchannel, int nbit_per_simple, int samplerate) {
    char *buf; int siz;
    buf = dataPcm(fname, &siz);
    playPcm_(buf, siz, nchannel, nbit_per_simple, samplerate);
    free(buf);
}

static void playWav(char *fname) {
    snd_pcm_t *handle;
    int nframe_per_play, nbyte_per_frame;

    int nchannel, nbit_per_simple, samplerate;
    char *buf; int siz;
    WavInfo info;
    buf = dataWav(fname, &siz, &info);
    nchannel = info.numChannels; nbit_per_simple = info.bitsPerSample; samplerate = info.sampleRate;
    playPcm_(buf, siz, nchannel, nbit_per_simple, samplerate);
    free(buf);
}

void checkstring(char *buf) {
    //if (buf == NULL ||)
}

void speak(char *word) {
    char *fname = DBWORDWAV;
    sqlite3 *db = sqOpen(fname);
    char *tmpbuf; int siz;
    tmpbuf = sqGet(db, word, &siz);
    if (tmpbuf == NULL) {
        DBLOG("try lowercase again");
        tmpbuf = sqGet(db, lowercase(word), &siz);
    }
    char *oriwd = NULL;
    if (tmpbuf == NULL) {
        DBLOG("may be a inflection form, translate to it's orignal form");
        char *dbname = DBINFLECTION;
        char *infwd = word;
        char *oriwd = sqGetOrigWord(dbname, infwd);
        if (oriwd != NULL) {
            DBLOG("inflection word = '%s', orignal word = '%s'", infwd, oriwd);
            tmpbuf = sqGet(db, oriwd, &siz);
            if (tmpbuf == NULL) {
                // oriwd may be a upercase form, translate to lowercase form
                char *lower = lowercase(oriwd);
                DBLOG("lowercase word = '%s'", lower);
                tmpbuf = sqGet(db, lower, &siz);
            }
            free(oriwd);
        }
    }
    if (tmpbuf != NULL) {
        if (! isWavBuf(tmpbuf, siz) ) DBERR("not a wav file.");
        char *pcmbuf; int pcmbufsiz;
        WavInfo info;
        pcmbuf = dataWavFromBuf(tmpbuf, siz, &pcmbufsiz, &info);
        free(tmpbuf);
        playPcm_(pcmbuf, pcmbufsiz, info.numChannels, info.bitsPerSample, info.sampleRate);
        free(pcmbuf);
    } else {
        DBLOG("the word [%s] not has correspoding pronunciation audio data. in function %s()", word, __func__);
    }
    if (db != NULL) sqlite3_close(db);
}

static int l_genSpeakData (lua_State *L) {
  sqGenSpeakDB();
  return 0;
}

static int l_speak (lua_State *L) {
    size_t len;
    char *word = luaL_checklstring(L, 1, &len);
    if (word == NULL) DBERR("Error: you pass a NULL for arguemnt 'word'. in %s", __func__);
    if (len != strlen(word)) DBERR("Error: bad argument. in %s", __func__);
    if ( !(strlen(word) > 0) ) DBERR("Error: argument 'word' has no charater. in %s", __func__);
    DBLOG("word = '%s'", word);
    speak(word);
}

static void print_lua_type(int t) {
    switch(t) {
        case LUA_TNIL           : { printf("LUA_TNIL"); break; }
        case LUA_TNUMBER        : { printf("LUA_TNUMBER"); break; }
        case LUA_TSTRING        : { printf("LUA_TSTRING"); break; }
        case LUA_TBOOLEAN       : { printf("LUA_TBOOLEAN"); break; }
        case LUA_TTABLE         : { printf("LUA_TTABLE"); break; }
        case LUA_TFUNCTION      : { printf("LUA_TFUNCTION"); break; }
        case LUA_TUSERDATA      : { printf("LUA_TUSERDATA"); break; }
        case LUA_TTHREAD        : { printf("LUA_TTHREAD"); break; }
        case LUA_TLIGHTUSERDATA : { printf("LUA_TLIGHTUSERDATA"); break; }
        default:
            printf("UNKNOW");break;
        print("\n");
    }
}

const struct luaL_Reg libiplay [] = {
	//{"sqGenSpeakDB", l_genSpeakData},
	//{"speak", l_speak},
	{NULL, NULL}
};

int luaopen_libiplay (lua_State *L) {
  //luaL_newlib(L, libiplay);
  luaL_register (L,
                    "libiplay",
                    libiplay);
  return 1;
}

int main() {
//int mainiplay() {

    // test lua
    lua_State *L = luaL_newstate ();
    if (L == NULL) DBERR("Error luaL_newstate in %s", __func__);
    //LUA_REGISTRYINDEX
    if (luaL_newmetatable(L, "LuaBook.dir") == 0) ERR("全局表registry 已有值");
        //将registry["LuaBook.dir"]压栈,registry已有值则返回0，否则新建表并存入registry["LuaBook.dir"]，并返回1
        // registry 是一个全局表，用于在不同的模块中共享数据

    lua_getfield(L, LUA_REGISTRYINDEX, "LuaBook.dir");
        // 取值registry["LuaBook.dir"]，并入栈。
        // LUA_REGISTRYINDEX 是伪索引，它不索此栈而是索引全局表registry

    //if (lua_compare(L, -1, -2, LUA_OPEQ) == 1) {
        //LOG("tow table equal");
    //} else {
    //    ERR("tow table not equal");
    //}

    int t = lua_type(L, lua_gettop(L));
    //print_lua_type(t);

    //printf("fname is: '%s'\n", wordFormWavPath("/root/iplay/kokia2.wav"));
    //printf("fname is: '%s'\n", wordFormWavPath("./kokia2.wav"));
    //printf("fname is: '%s'\n", wordFormWavPath("kokia2.wav"));
    //printf("fname is: '%s'\n", wordFormWavPath("kokia2.WAV"));


    // test alsa
    sqGenSpeakDB();
    char *word = "aberrance";
    speak("a");
    speak("aberrance");
    speak("bump");
    speak("aboard");
    speak("knot");
    speak("fist");
    speak("ability");
    speak("A's");
    //  test split() function
    const char *buf = "A's,a's,c's,d's";
    int siz = strlen(buf) + 1;
    unsigned int *pointerArray = NULL; int szofpointerArray = 0; int nPointer = 0;
    pointerArray = split(buf, siz, ',', &szofpointerArray);
    nPointer = szofpointerArray / (sizeof (char*));
    int i;
    for (i = 0; i < nPointer; i++) {
        DBLOG("%s", (char*)(*(pointerArray+i)));
    }

    // test inflection db
    char *dbname = DBINFLECTION;
    char *inflectionword = "apples";
    char *orinalword     = "apple";


    if ( ! sqIsDbExsit(dbname) ) {
        sqGenDBInflectionWords(dbname, inflectionword, strlen(inflectionword)+1, orinalword, strlen(orinalword)+1, false);
        sqGenDBInflectionWords(dbname, NULL, -1, NULL, -1, true);  // close db
    }

    char *infwd = "apples";
    char *oriwd = sqGetOrigWord(dbname, infwd);
    if (oriwd != NULL) {
        DBLOG("inflection word = '%s', orignal word = '%s'", infwd, oriwd);
        free(oriwd);
    } else {
        DBLOG("inflection word '%s' not have correspoding orignal word", infwd);
    }
    if (PFLOG != NULL) fclose(PFLOG);
    return 0;
}



