module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({ }) {



        let obj = this

        let mkvs = this.libs.files.allmkv(global.animes.root, 'Danganronpa')
        for (let j = 0; j < mkvs.length; j++) {

            let vdpath = mkvs[j]
            let { videoname, episode } = this.libs.vdinfo.episode(vdpath)
            //let { srt: srt_jp, msg: msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream

            let { srt: srt_jp, msg: msg_jp } = await this.libs.ffmpeg.extractSubtitle(vdpath, 'srt', 0)
            if (srt_jp == null) {
                console.log(`Warning: srt_jp is null\nmsg: ${msg_jp}`)
                continue
            }
            srt_jp = this.libs.srt.clean(srt_jp)

            let jps = this.libs.srt.parse(srt_jp)

            /*
            
                fsrt = os.path.join(currDir, frtname)
    strs = "\n"+readstring(fsrt)+"\n"
    iters = re.finditer(r"\n\d+\n", strs, re.DOTALL)
    poss = [ i.span() for i in iters ]

            */

            let a = 1

            //let vinfo = libvdinfo.vdinfo(vdpath)
        }

        //dbpaths.forEach((dbPath) => {

        let re = await this.dbs.defaultDB.drop.query({ 'dbname': 'danganronpa' })  // drop db
        re = await this.dbs.defaultDB.danganronpa.create.query({})              // create db
        re = await this.dbs.danganronpa.createtable.query({})                   // create table 

        //let re = await this.services.user.getuser( { userid:'0' } )

        // let re = await this.dbs.temp2.search.query({keywd})

        return 'hi from insert'

        // return 'hi from service.'

    }
}