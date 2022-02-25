
let subtitleSteams = global.config.subtitleSteams

module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({}) {

        // drop and create db, then create table
        let re = await this.dbs.defaultDB.dropdatabase.query({'dbname': 'anime'})
        re = await this.dbs.defaultDB.createdatabase.query({'dbname':'anime'})
        re = await this.dbs.anime.createtable.query({'tablename': 'anime'})

        let mkvs = this.libs.files.allmkv(global.animes.root)

        let names = {}
        for (let vdpath of mkvs) {
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)
            if ( !( name in names ) ) {
                names[name] = name
                //re = await this.dbs.anime.createtable.query({'tablename':name}) // create table, this is separate table, cancel now
            }
        }

        for (let j = 0; j < mkvs.length; j++) {

            let vdpath = mkvs[j]
            let { name, seasion, seasionname, episode, videoname } = this.libs.vdinfo.episode(vdpath)

            if ( !(name in subtitleSteams) ) {
                throw `error: name '${name}' not in config.subtitleSteams!`
            }

            let subsjp = []
            let subszh = []

            let nths = subtitleSteams[name]
            for (let nth of nths) {
                let { srt, msg } = await this.libs.ffmpeg.extractSubtitle(vdpath, 'srt', nth)
                if (srt == null) {
                    console.log(`Warning: srt_jp is null\nmsg: ${msg}`)
                    continue
                }
                srt = this.libs.srt.clean(srt)
    
                let subtitles = this.libs.srt.parse(srt)  // jp ch all in one srt, and have the same time
    
    
                for (let i = 0; i < subtitles.length; i++) {
                    let item = subtitles[i]
                    let subtitle = item.subtitle
                    if (subtitle.trim() == '') {
                        continue
                    }
                    if (this.libs.mecab.isJP(subtitle)) {
                        subsjp.push(item)
                    } else {
                        subszh.push(item)
                    }
                }
            }


            let subtitles2 = this.libs.srt.merge(subsjp, subszh)

            console.log(`# begin insert...`)
            for (let i = 0; i < subtitles2.length; i++) {  // 

                let item = subtitles2[i]

                let begintime = item.begintime.replace(',', '.')  // for ffmpeg
                let endtime = item.endtime.replace(',', '.')
                let jp = item.jp.trim()
                let zh = item.zh.trim()

                let { hiras, msg } = await this.libs.mecab.hiras(jp)
                if (hiras == null) {
                    throw `Error: segment fail. ${msg}`
                }


                let jp_ruby = hiras.ruby
                let hiragana = hiras.hiragana

                let hiragana_ng = this.libs.srt.NG(hiragana)
                let jp_ng = this.libs.srt.NG(jp)
                let zh_ng = this.libs.srt.NG(zh)

                jp_ng = (jp_ng.concat(hiragana_ng)).join(' ')  // for fulltext search All in one
                zh_ng = zh_ng.join(' ')
                hiragana_ng = hiragana_ng.join(' ')

                let { au: audio } = await this.libs.ffmpeg.extractAudio(vdpath, 'mp3', begintime, endtime)
                if (audio == null) {
                    throw `au is null. ${vdpath} ${begintime}`
                }
            
                //fs.writeFileSync('./tmp.mp3', audio )
        
                let video = Buffer.from('')  // empty now

                let re = await this.dbs.anime.insert.query({tablename:'anime', name, seasion, jp, zh, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionname, endtime, audio, video})
            
                console.log(`${i + 1}/${subtitles2.length} subs | ${j + 1} / ${mkvs.length} mkvs ${name}`)   
                
                

            }

        }

        console.log('all taske done.')

        return 'all taske done.'

    }
}

/*


//let { hiras, msg }= await this.libs.mecab.haras('騙して勝つ')
// let { hiras, msg }= await this.libs.mecab.haras("お願いします! ピカピカ! ")  // crash

SELECT Max(ID) FROM danganronpa;
SELECT p."id", p.jp_ruby, p.zh, p.v_jp, p.v_zh, p.seasion, p."name" FROM danganronpa p WHERE ID IN (1, 3);

*/


/*

ffmpeg -i "E:\videos\anime\pokemon\S14\Best_Wishes\1.mkv" -y -map 0:s:0 -f srt pipe:1
ffmpeg -i "/mnt/videos/anime/pokemon/S14/Best_Wishes/1.mkv" -y -map 0:s:0 -f srt pipe:1

windows 

$ ffmpeg
ffmpeg version 4.4.1-essentials_build-www.gyan.dev Copyright (c) 2000-2021 the FFmpeg developers
  built with gcc 11.2.0 (Rev1, Built by MSYS2 project)
  configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-libass --enable-libfreetype --enable-libfribidi --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-ffnvcodec --enable-nvdec --enable-nvenc --enable-d3d11va --enable-dxva2 --enable-libmfx --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband
  libavutil      56. 70.100 / 56. 70.100
  libavcodec     58.134.100 / 58.134.100
  libavformat    58. 76.100 / 58. 76.100
  libavdevice    58. 13.100 / 58. 13.100
  libavfilter     7.110.100 /  7.110.100
  libswscale      5.  9.100 /  5.  9.100
  libswresample   3.  9.100 /  3.  9.100
  libpostproc    55.  9.100 / 55.  9.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...

Use -h to get full help or, even better, run 'man ffmpeg'



# ffmpeg
ffmpeg version 3.4.9 Copyright (c) 2000-2021 the FFmpeg developers
  built with gcc 4.8.5 (GCC) 20150623 (Red Hat 4.8.5-44)
  configuration: --prefix=/usr --bindir=/usr/bin --datadir=/usr/share/ffmpeg --docdir=/usr/share/doc/ffmpeg --incdir=/usr/include/ffmpeg --libdir=/usr/lib64 --mandir=/usr/share/man --arch=x86_64 --optflags='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic' --extra-ldflags='-Wl,-z,relro ' --extra-cflags=' ' --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3 --enable-bzlib --disable-crystalhd --enable-fontconfig --enable-gcrypt --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libcdio --enable-libdrm --enable-indev=jack --enable-libfreetype --enable-libfribidi --enable-libgsm --enable-libmp3lame --enable-nvenc --enable-openal --enable-opencl --enable-opengl --enable-libopenjpeg --enable-libopus --disable-encoder=libopus --enable-libpulse --enable-librsvg --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libvorbis --enable-libv4l2 --enable-libvidstab --enable-libvpx --enable-libx264 --enable-libx265 --enable-libxvid --enable-libzvbi --enable-avfilter --enable-avresample --enable-libmodplug --enable-postproc --enable-pthreads --disable-static --enable-shared --enable-gpl --disable-debug --disable-stripping --shlibdir=/usr/lib64 --enable-libmfx --enable-runtime-cpudetect
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...




*/