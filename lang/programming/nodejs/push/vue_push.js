
const WebSocket = require('ws')

// WebSocket.client()

server = new WebSocket.Server({ port: 5000 })
server.connectionCount = 0
server.on('connection', (socket, req) => {
    const url = req.socket.remoteAddress + upgradeReq.url
    console.log('new connection req url [%s]', url)
    socket.on('close', () => {
        server.connectionCount--
        console.log(`%s disconnected ! `, url)
        // close no use
        // 
    });

    this.server.connectionCount++;
    let streamUrl = getURLParameters(req.url).url

    if (!streamUrl) { return; }

    //   let dataCache = this.URL_STREAM.get(streamUrl);
    //   dataCache || (dataCache = new DataCache());
    //   dataCache.clients.push(socket);

    //   dataCache.mpeg = this.initMpeg1Muxe(streamUrl);
    //   this.URL_STREAM.set(streamUrl, dataCache);

    console.log('webSocket产生新的连接:%s ', url)

})

let a = 1


async function client() {

    const ws = new WebSocket('ws://127.0.0.1:5000/path')
    ws.on('open', function open() {
      ws.send('something')
    })
    ws.on('message', function message(data) {
      console.log('received: %s', data)
    })


}


function getURLParameters(url) {
    const params = url.match(/([^?=&]+)(=([^&]*))/g)
    return params ? params.reduce(
        (a, v) => (a[v.slice(0, v.indexOf('='))] = v.slice(
            v.indexOf('=') + 1), a), {},
    ) : [];
}



// utils/websocket.js

const audioUrl = require('@/assets/remind-music/remind.mp3')
export default {
  install: function (Vue){
    let Socket = ''
    let setIntervalWesocketPush = null
    let socketUrl = ''
    let myAudio = ''
    // 控制长连接是否尝试从新请求
    let againSocket = true
    let SocketFocm = Vue.extend({
      beforeCreate() {
        try {
          myAudio = new Audio()
          myAudio.src = audioUrl
          myAudio.preload
        } catch (error) {
          Vue.prototype.$message({message: '您的浏览器不支持语言提醒功能', type: 'error'})
        }
      },
      methods: {
        sokitEvent(){
          let str = [{"bizId":"1111111111","dflag":0,"gmtCreated":"2020-12-24T08:25:28Z","gmtModified":"2020-12-24T08:25:28Z","id":"1UQjqKwpHNm","message":"您有新的订单，请注意查收！","pk":"shop_console","pushScene":0,"sessionId":"1UMFGC473km","status":0,"type":0},{"bizId":"2222222","dflag":0,"gmtCreated":"2020-12-24T08:25:34Z","gmtModified":"2020-12-24T08:25:34Z","id":"1UQjqQwDPed","message":"您有新的订单，请注意查收！","pk":"shop_console","pushScene":0,"sessionId":"1UMFGC473km","status":0,"type":0},{"bizId":"333333333","dflag":0,"gmtCreated":"2020-12-24T08:25:39Z","gmtModified":"2020-12-24T08:25:39Z","id":"1UQjqWHLT3Y","message":"您有新的订单，请注意查收！","pk":"shop_console","pushScene":0,"sessionId":"1UMFGC473km","status":0,"type":0}]
          this.onmessageWS({data: JSON.stringify({result: str, code:200})})
        },
        myAudio(){
          // false true
          // false false
          // true true
          // 经播放完毕 结束
          if(myAudio.paused){
            try {
              myAudio.play()
            } catch (error) {

            }
          }
        },
        createSocket(url = socketUrl){
          Socket && Socket.close()
          if (!Socket) {
            (url)&&(socketUrl = url)
            console.log('建立websocket连接', url)
            Socket = new WebSocket(url)
            Socket.onopen = this.onopenWS
            Socket.onmessage = this.onmessageWS
            Socket.onerror = this.onerrorWS
            Socket.onclose = this.oncloseWS
            // setTimeout(() => {
              // this.sokitEvent()
              // console.log('发消息')
              // this.onmessageWS({data: 121212})
            // })
          } else {
            console.log('websocket已连接')
          }
        },
        /**打开WS之后发送心跳 */
        onopenWS() {
          this.sendPing()
        },
         /**WS数据接收统一处理 */
        /**
         * 
         * {
         *  业务ID
            bizId: "201224145021255003"
            // 消息文本
            message: "您有新的订单，请注意查收！"
            // pk
            pk: "shop_console"
            // 消息类型 0-订单
            pushScene: 0
            // 店铺id
            sessionId: "1UMFGC473km"
            // 消息提醒类型 0-文本 1-语言
            type: 0
          }
        */
        onmessageWS (e) {
          // 收到消息之后，直接播放语音提醒
          let data = JSON.parse(e.data||'{}')
          if(data.code === 200){
            this.myAudio()
            this.$eventBus.$emit('onmessageWS', {data: data.result})
          }
          if(data.code === 401){
            againSocket = false
          }
        },
        /**连接失败重连 */
        onerrorWS () {
          Socket.close()
          clearInterval(setIntervalWesocketPush)
          if(!againSocket){
            console.log('长连接关闭不再尝试重连')
            return false
          }
          console.log('连接失败重连中')
          if (Socket.readyState !== 3) {
            Socket = null
            setTimeout(() => {
              this.createSocket()
            },10000)
          }
        },
        /**断开重连 */
        oncloseWS () {
          clearInterval(setIntervalWesocketPush)
          console.log('websocket已断开....正在尝试重连')
          if(!againSocket){
            console.log('长连接关闭不再尝试重连')
            return false
          }
          if (Socket.readyState !== 2) {
            Socket = null
            setTimeout(() => {
              this.createSocket()
            },10000)
          }
        },
        /**发送心跳
         * @param {number} time 心跳间隔毫秒 默认5000
         * @param {string} ping 心跳名称 默认字符串ping
         */
        sendPing(time = 5000, ping = 'ping') {
          clearInterval(setIntervalWesocketPush)
          Socket.send(ping)
          setIntervalWesocketPush = setInterval(() => {
            Socket.send(ping)
          }, time)
        },
        // 关闭长连接
        closeSocket(){
          console.log('关闭长连接')
          clearInterval(setIntervalWesocketPush)
          againSocket = false
          socketUrl = ''
          Socket.close()
          Socket = null
        }
      }
    })
    const socketFocm = new SocketFocm()

    /**
     * 发送数据但连接未建立时进行处理等待重发
     * @param {any} message 需要发送的数据
     */
    const connecting = message => {
      setTimeout(() => {
        if (Socket.readyState === 0) {
          connecting(message)
        } else {
          Socket.send(JSON.stringify(message))
        }
      }, 10000)
    }
    /**
     * 发送数据
     * @param {any} message 需要发送的数据
     */
    const sendWSPush = message => {
      if (Socket !== null && Socket.readyState === 3) {
        Socket.close()
        createSocket()
      } else if (Socket.readyState === 1) {
        Socket.send(JSON.stringify(message))
      } else if (Socket.readyState === 0) {
        connecting(message)
      }
    }
    Vue.prototype.$Socket = {
      sendWSPush: sendWSPush,
      connecting: connecting,
      closeSocket: socketFocm.closeSocket,
      createSocket: socketFocm.createSocket
    }
  }
}

// main.js中加入以下代码
import createSocket from './utils/websocket'
Vue.use(createSocket)


// permission.js文件中加入以下代码
vue.$Socket.createSocket(`ws://api.test.zjddwl.net/message/webSocket/shop_console/${getToken()}`)
