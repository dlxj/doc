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

        //let re = await this.service.user.getuser( { userid:'' } )

        return 'hi from service.'

        // return 'hi from service.'

    }
}

/*



*/
