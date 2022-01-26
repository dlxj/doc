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
        return this.msg(200, 'hi,,,')
    }
}

/*



*/
