
module.exports = {
    name: 'search',
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

        // let re = await this.dbs.defaultDB.drop.query({'dbname':'temp'})
        // re = await this.dbs.defaultDB.temp.create.query({})

        let re = await this.services.search( { keywd, type } )

        return this.msg(200, re)
    }
}

/*



*/
