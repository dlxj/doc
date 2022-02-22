module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({}) {

        let obj = this

        

        let re = await this.services.anime.insert({})

        // let dbpaths = libfiles.allfiles(dbsDir, 'js')

        //let { default:libvdinfo } = await import('./videoinfo.mjs')

        //let re = await this.services.user.getuser( { userid:'0' } )

        // let re = await this.dbs.temp2.search.query({keywd})

        return this.msg(200, 'hi,,,')

        // return 'hi from service.'

    }
}