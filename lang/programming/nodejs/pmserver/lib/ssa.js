
let fs = require('fs')

module.exports = {

    extractSrt: function({str, sapath=null}) {
    
        let srt = ''
        let items = []

        let sa = str
        if (sapath != null) {
            sa = fs.readFileSync(sapath, { encoding:"utf-8"})
        } 
        sa = sa.replace(/\r\n/g, '\n')
        let matchs = sa.matchAll(String.raw`<p begin="(\d\d:\d\d:\d\d.\d\d\d)"\s+end="(\d\d:\d\d:\d\d.\d\d\d)".+?>(.+?)</p>`)
        let arr = Array.from(matchs)
        for (let match of arr) {

            let origin = match[0]
            let begin = match[1]
            let end = match[2]
            let text = match[3]
            text = text.replace(/<span.+?>/g, '').replace(/<\/span>/g, '').replace(/<br\s*\/>/g, '\n')

            items.push( { begin, end, text } )
        } 

        for (let i = 0; i < items.length; i++) {

            let { begin, end, text } = items[i]
            begin = begin.replace('.', ',')
            end = end.replace('.', ',')

            text = text.replace(/\n+/g, ' ')  // 去掉行间回车

            srt += `\n${i+1}\n${begin} --> ${end}\n${text}\n`
       }

       return srt

    } 
}



























/*

00:00:03,586 --> 00:00:06,923

*/



























// module.exports.extractSrt({str:`<p begin="00:02:14.802" end="00:02:17.304" style="s1"><span style="s2">（アナウンサー）<span style="s3">さあ イワーク</span><br /><span style="s3">巨体を生かして—</span></span></p>`})



/*

1
00:00:03,586 --> 00:00:06,923
♪～

2
00:01:23,666 --> 00:01:27,670
～♪

*/