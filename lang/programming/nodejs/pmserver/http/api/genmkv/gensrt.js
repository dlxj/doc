
module.exports = {
    name: 'gensrt',
    remark: '',
    params: {
        keywd: {
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


        let mkvs = this.libs.files.allfiles(global.animes.root, type)

        let re = await this.services.search( { keywd, type } )

        return this.msg(200, re)
    }
}

/*



*/
