
module.exports = {
    name: 'search',
    remark: '',
    params: {
        keywd: {
            type: 'string',
            remark: ''
        }
    },
    async handler({ keywd }) {

        let obj = this

        // let re = await this.dbs.defaultDB.drop.query({'dbname':'temp'})
        // re = await this.dbs.defaultDB.temp.create.query({})

        re = await this.services.search( { keywd } )

        return this.msg(200, 'hi,,,')
    }
}

/*



*/
