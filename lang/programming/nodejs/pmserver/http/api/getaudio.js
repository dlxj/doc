
module.exports = {
    name: 'search',
    remark: '',
    params: {
        name: {
            type: 'string',
            remark: ''
        },
        type: {
            type: 'enum',
            range:["anime","drama"],
            remark: '',
            default:'anime'
        }
    },
    async handler({ keywd, type }) {

        // return File(memory, "audio/mpeg", $"{id}.mp3");
        // let audio_dir = path.join(global.animes.root_audio, name, seasion)
        // let audio_path = path.join(audio_dir, `${tableID}.mp3`)


        let re = await this.services.search( { keywd, type } )

        return this.msg(200, re)
    }
}

/*



*/
