
let fs = require('fs')
let chardet = require('chardet')

module.exports = {

    extractSrt: function({str, sapath=null}) {

        // Dialogue: Marked=0,0:01:48.80,0:01:51.70,Default,,0000,0000,0000,,尼多力诺使出如此强大的攻击

        
    
        let srt = ''
        let items = []

        let sa = str
        if (sapath != null) {
            let encode = chardet.detect(Buffer.from( require('fs').readFileSync(sapath) ))
            sa = fs.readFileSync(sapath, { encoding:encode})  // encode
        }
        
        sa = sa.replace(/\r\n/g, '\n')
        let matchs = sa.matchAll(String.raw`\nDialogue:.+?(\d:\d\d:\d\d\.\d\d),(\d:\d\d:\d\d\.\d\d),Default,,.+?,,(.+)`)
        let arr = Array.from(matchs)
        for (let match of arr) {

            let origin = match[0]
            let begin = '0' + match[1]
            let end = '0' + match[2]
            let text = match[3]

            if (text.indexOf('WWW.C2CLUB.NET') != -1) {
                continue
            }

            text = text.replace(/\{.+\}/g, '').replace(/<\/span>/g, '').replace(/<br\s*\/>/g, '\n')

            items.push( { begin, end, text } )
        } 

        for (let i = 0; i < items.length; i++) {

            let { begin, end, text } = items[i]
            begin = begin.replace('.', ',')
            end = end.replace('.', ',')

            text = text.replace(/\n+/g, ' ')  // 去掉行间回车

            srt += `\n${i+1}\n${begin} --> ${end}\n${text}\n`
        }

        if (srt == '') {
            let a = 1
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