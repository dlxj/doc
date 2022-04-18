
let insertPasswd = global.config.insertPasswd

module.exports = {
    name: 'opennmt',
    remark: '',
    params: {
    },
    async handler({}) {

        let re = await this.services.anime.opennmt({})

        return this.msg(200, 'ok.')

    }
}