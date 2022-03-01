
let insertPasswd = global.config.insertPasswd

module.exports = {
    name: 'insert',
    remark: '',
    params: {
        passwd: {
            type: 'string',
            remark: ''
        }
    },
    async handler({passwd}) {

        if (passwd != insertPasswd) {
            console.log('Warning: Passwd not correct!!! hit api http/anime/insert')
            return this.msg(200, 'hi,,,')
        }

        console.log('hit http/anime/insert')        

        let re = await this.services.anime.insert({})

        // let dbpaths = libfiles.allfiles(dbsDir, 'js')

        //let { default:libvdinfo } = await import('./videoinfo.mjs')

        //let re = await this.services.user.getuser( { userid:'0' } )

        // let re = await this.dbs.temp2.search.query({keywd})

        return this.msg(200, 'hi,,,')

        // return 'hi from service.'

    }
}