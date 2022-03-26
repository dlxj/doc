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
        },
        lang_type: {
            type: 'enum',
            range:["jp","zh"],
            remark: '',
            default:'jp'
        },
    },
    async handler({ keywd, type, lang_type }) {

        let search_field = 'v_jp'
        if (lang_type == 'zh') {
            search_field = 'v_zh'
        }

        let re = await this.dbs.anime.search.query({tablename:'anime', keywd, search_field})

        return re.rows


    }
}

/*



*/
