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
            remark: ''
        }
    },
    async handler({ keywd, type }) {


        let re = await this.dbs.anime.search.query({tablename:'anime', keywd})

        return re.rows


    }
}

/*



*/
