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

        //let re = await this.services.user.getuser( { userid:'0' } )

        let re = await this.dbs.anime.search.query({tablename:'anime', keywd})

        return 'hi from service.'

        // return 'hi from service.'

    }
}

/*



*/
