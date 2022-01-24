

String.prototype.replaceAll = function (search, replacement) {
    var target = this
    return target.replace(new RegExp(search, 'g'), replacement)
}

export default {

    clean: function (str) {
        str = str.replaceAll(/<font.+?>/g, '').replaceAll(/<\/.+?>/g, '').replaceAll(/<b>/g, '').replaceAll(/\r\n/g, '\n')
        return str
    },
    parse: function (str) {

        let subs = []

        let regstr = String.raw`\d+\n(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)\n`  // `00:00:00.000`
        let reg = new RegExp(regstr, 'g')
        let matchs = str.matchAll(reg)
        let arr = Array.from(matchs)

        if (arr.length > 0) {

            for (let i = 0; i < arr.length; i++) {
                let match = arr[i]
                let begin = match.index
                let end = begin + match[0].length

                let begintime = match[1]
                let endtime = match[2]

                let subtitle = ''
                if (i != arr.length - 1) {

                    let match2 = arr[i + 1]
                    let begin2 = match2.index

                    subtitle = str.substring(end, begin2)

                } else {

                    subtitle = str.substring(end)
                }

                subtitle = subtitle.replaceAll(String.raw`\s+`, ' ')


                subs.push({ begintime, endtime, subtitle })

            }

        }

        return subs

    },
    merge: function (subsjp, subszh) {

        let subs = []

        for (let i = 0; i < subsjp.length; i++) {

            let begintime_jp = subsjp[i].begintime
            let endtime_jp = subsjp[i].endtime
            let subtitle_jp = subsjp[i].subtitle

            let begin_seconds_jp = parse_srt_time(begintime_jp)
            let end_seconds_jp = parse_srt_time(endtime_jp)

            let duration_jp = end_seconds_jp - begin_seconds_jp

            let matchQ = false
            for (let j = 0; j < subszh.length; j++) {

                let begintime_zh = subszh[j].begintime
                let endtime_zh = subszh[j].endtime
                let subtitle_zh = subszh[j].subtitle

                let begin_seconds_zh = parse_srt_time(begintime_zh)
                let end_seconds_zh = parse_srt_time(endtime_zh)

                let duration_zh = end_seconds_zh - begin_seconds_zh

                let deviation = Math.abs(duration_zh - duration_jp)
                let de_begin = Math.abs(begin_seconds_zh - begin_seconds_jp)
                let de_end = Math.abs(end_seconds_zh - end_seconds_jp)

                if (deviation <= 1.5) {  // duration less than 1 second

                    if (de_begin <= 1.5) {

                        if (de_end <= 1.5) {

                            subs.push({ begintime: begintime_jp, endtime: endtime_jp, jp: subtitle_jp, zh: subtitle_zh })
                            matchQ = true
                            break

                        }

                    }
                }


                if ((j - i > 15)) {
                    break
                }

            }

            if (!matchQ) {
                //subs.push( {begintime:begintime_jp, endtime:endtime_jp, jp:subtitle_jp, zh:'' } )
            }
        }

        return subs
    },
    // NGram
    NG: function (strs) {

        strs = strs.replaceAll(String.raw`\s`, '')

        function ng(s, n) {

            var grs = []

            for (let i = 0; i < s.length; i++) {

                if (i + n > s.length) {
                    break
                }

                var gr = s.substring(i, i + n)

                grs.push(gr)


            }

            return grs

        }

        var gss = []
        for (let i = 2; i <= 10; i++) {

            let gs = ng(strs, i)

            if (gs.length > 0) {

                gss = gss.concat(gs)

            } else {

                break

            }

        }

        return gss

    }
}

function parse_srt_time(strtime) {

    let reg = new RegExp(String.raw`(\d\d):(\d\d):(\d\d),(\d\d\d)`)
    let match = strtime.match(reg)
    if (match !== null) {

        let hh = parseInt(match[1])   // 时
        let mm = parseInt(match[2])   // 分
        let ss = parseInt(match[3])   // 秒
        let ms = parseInt(match[4])   // 毫秒

        let sss = hh * 3600 + mm * 60 + ss + (ms / 1000)  // total seconds

        return sss
    }

    return null
}

