

(async () => {

    const WebSocket = require('ws')

    //webSocket服务端地址
    let wsBaseURL = 'ws://127.0.0.1:321' // 我的电脑
    // let wsBaseURL = 'ws://192.168.1.124:7116'  // 124 tmux 独立进程
    //let wsBaseURL = 'ws://192.168.1.124:7115'  // 正式 题库内去重

    // let wsBaseURL = 'ws://172.16.4.184:10000'    // 本机负载均衡
    //let wsBaseURL = 'ws://172.16.4.184:10001'

    // let wsBaseURL = 'ws://192.168.1.124:10000'        // 正式负载均衡 它会转发
    //let wsBaseURL = 'ws://192.168.1.124:7115'        // 正式负载均衡 它会转发

    let wsClient = null


    wsClient = new WebSocket(wsBaseURL)

    wsClient.onopen = async () => {

        console.log(wsBaseURL + '连接成功')

        // app = { "AppID": 4221, "BookID": -1, "userID": "1", "refresh": 0 }
        //app = { "AppID": 5548, "BookID": -1, "userID": "1", "refresh": 0 }

        //app = { "AppID": 4286, "BookID": -1, "userID": "1", "refresh": 0 }
        // app = { "AppID": 4459, "BookID": -1, "userID": "1", "refresh": 0 }
        // app = { "AppID": 6927, "BookID": -1, "userID": "1", "refresh": 0 }
        // app = { "AppID": 6042, "BookID": -1, "userID": "1", "refresh": 0 }
        // app = { "AppID": 4285, "BookID": -1, "userID": "1", "refresh": 0 }
        // app = { "AppID": 17387, "BookID": -1, "userID": "1", "refresh": 0 }  // 很长
        app = { "AppID": 18744, "BookID": -1, "userID": "1", "refresh": 0 }    // 很短

        if (app.refresh == 1) {

            // 先清除所有以前的题库内去重结果
        }


        // 开始题库内去重
        start_diff: {

            try {
                wsClient.send(JSON.stringify({ "api": "/test/smartCalc", "params": app }))
            } catch (error) {
                console.log(error.msg)
            }

        }

    }

    wsClient.onmessage = (msg) => {
        let data = JSON.parse(msg.data)
        console.log(msg.data)

        let progress = Number(data.progress)
        if (progress > 99.999999999) {
            wsClient.close()
        }


    }

    wsClient.onclose = (event) => {
        let { code, reason, wasClean } = event  // code=1005, reason='', wasClean=true // 正常退出

        if (code == 1005 && reason == '') {
            console.log('The connection has been closed successfully.')
            process.exit()
        } else {
            console.log('ERROR: 连接被意外关闭!!')
        }

    }
})()





