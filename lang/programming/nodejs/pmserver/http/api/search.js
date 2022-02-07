
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

        let re = await this.service.search( { keywd } )

        return this.msg(200, 'hi,,,')
    }
}

/*



*/
