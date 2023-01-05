
module.exports = {
    name: '智能计算试题标签',
    params: {
        AppID: {
            type: 'number',
            remark: '题库ID'
        },
        UserID: {
            type: 'number',
            remark: '操作用户ID'
        },
        testCptIDs: {
            type: 'array',
            default: [],
            remark: '章节ID'
        },
        refresh: {
            type: 'bool',
            remark: 'true 重新计算，false 不进行重新计算'
        }
    },
    remark: '',
    author: '',
    handler: async function (params) {  // conn, params, 

        let { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params

        let worker = require('../../../lib/worker.js')
        let simir_data1 = await worker.create('../m.js', params) // 相对路径是相对 worker.js 所在目录说的

        let a = 1

        // __ws__.send({msg:'ok'})

    }
}