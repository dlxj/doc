
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

        let services = this.services


        let re = await this.services.search( { keywd } )

        return this.msg(200, 'hi,,,')
    }
}

/*



*/
