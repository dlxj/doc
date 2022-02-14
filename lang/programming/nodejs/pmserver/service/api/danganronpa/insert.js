module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({}) {

        let obj = this

        let re = await this.dbs.defaultDB.drop.query({'dbname':'danganronpa'})
        re = await this.dbs.defaultDB.danganronpa.create.query({})

        //let re = await this.services.user.getuser( { userid:'0' } )

        // let re = await this.dbs.temp2.search.query({keywd})

        return 'hi from insert'

        // return 'hi from service.'

    }
}