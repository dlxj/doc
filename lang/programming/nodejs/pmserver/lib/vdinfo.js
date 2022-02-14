
let path = require('path')

let regstrs = [
    String.raw`.+?Animation - (\d+) \[.+?`,  // 4 danggan
    String.raw`第(\d+(?:~\d+)*)话`          // 4 pokemon
]

module.exports = {

    episode: function(vdpath) {
        
        let videoname = path.basename(vdpath)
        let episode = ''

        let regstr = ''
        for (let str of regstrs) {
            if ( videoname.match(new RegExp(str)) != null ) {
                regstr = str
                break
            }
        }

        if (regstr == '') {
            throw `unkonw episode: ${videoname}`
        }

        let match = videoname.match(new RegExp(regstr)) // /第(\d+(?:~\d+)*)话/
        if (match != null) {
            episode = match[1]
        } else {
            match = videoname.match(/^(\d+)\.mkv/)
            if (match != null) {
                episode = match[1]
            }
            else {
                throw `unkonw episode: ${videoname}.`
            }
        }

        return { videoname, episode }
    }

}