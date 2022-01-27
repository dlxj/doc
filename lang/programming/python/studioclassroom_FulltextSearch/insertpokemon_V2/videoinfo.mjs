
import path from 'path'

export default {

    vdinfo(vdpath) {
        
        let videoname = path.basename(vdpath)
        let episode = ''

        let match = videoname.match(/第(\d+(?:~\d+)*)话/)
        if (match != null) {
            episode = match[1]
        } else {
            match = videoname.match(/^(\d+)\.mkv/)
            if (match != null) {
                episode = match[1]
            }
            else {
                throw `unkonw episode: ${videoname}`
            }
        }

        return {  videoname, episode }
        
    }
}

