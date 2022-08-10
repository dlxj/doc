
(async()=>{

    // -hwaccel cuvid 

    let { execa } = await import('execa')

    let cmd = `ffmpeg -y -i "1.mp4" -i "1.mkv" -map 0:v -map 1:a:0 -map 0:a:0 -vf "subtitles='1.srt'" "out.mkv"`  // 生成硬字幕

    let childProcess = execa(cmd, { shell:true, 'encoding': 'utf8' })
    let { stdout:out1 } = await childProcess

    let a = 1

})()




