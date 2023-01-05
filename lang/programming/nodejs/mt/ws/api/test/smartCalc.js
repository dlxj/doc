
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
    author: 'gd',
    handler: async function (params) {  // conn, params, 

        let { AppID, UserID, refresh, testCptIDs, __ip__, __ws__ } = params

        __ws__.send('ok')

    }
}