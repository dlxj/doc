//var nodejieba = require("nodejieba")

module.exports = {
    spaced: async function (str) {
        //let arr = nodejieba.cut(str)
        let arr = 'null'
        return { spaced:arr.join(' ').replace(/\s+/g, ' ') }
    }
}
