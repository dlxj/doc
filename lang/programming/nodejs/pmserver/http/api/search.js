
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


        let r = await pg.defaultDB.query('select $1::text as name', ['brianc'])

        let services = this.services


        let re = await this.services.search( { keywd } )

        return this.msg(200, 'hi,,,')
    }
}

/*



*/
