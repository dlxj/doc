
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
        },
        lang_type: {
            type: 'enum',
            range:["jp","zh"],
            remark: '',
            default:'jp'
        },
    },
    async handler({ keywd, type, lang_type }) {

        // let re = await this.dbs.defaultDB.drop.query({'dbname':'temp'})
        // re = await this.dbs.defaultDB.temp.create.query({})

        let re = await this.services.search( { keywd, type, lang_type } )

        return this.msg(200, re)
    }
}

/*



*/
