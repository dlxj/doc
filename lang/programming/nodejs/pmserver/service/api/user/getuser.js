module.exports = {
    name: 'getuser',
    remark: '',
    params: {
        userid: {
            type: 'string',
            remark: ''
        }
    },
    async handler({ userid }) {
        
        return 'hi from service.user.getuser'

    }
}

/*



*/
