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

        let re = await global.services.user.getuser( { userid:'' } )

        return 'hi from service.'

        // return 'hi from service.'

    }
}

/*



*/
