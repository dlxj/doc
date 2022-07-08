// 常用提示
import {
  Loading,
  Message,
  MessageBox,
  Notification
} from 'element-ui'
var errorList = []
export default {
  init () {

  },
  success (message, duration) {
    this.$message({
      showClose: true,
      message: message,
      type: 'success',
      offset: 400,
      duration: (duration == null || duration === undefined) ? 1500 : duration * 1000
    })
  },
  error (message, duration) {
    this.$message({
      showClose: true,
      message: message,
      type: 'error',
      offset: 300,
      duration: (duration == null || duration === undefined) ? 3000 : duration * 1000
    })
  },
  warning (message, duration) {
    this.$message({
      showClose: true,
      message: message,
      type: 'warning',
      offset: 400,
      duration: (duration == null || duration === undefined) ? 3000 : duration * 1000
    })
  },
  errorList (key, message, duration) {
    if (errorList.indexOf(key) === -1) {
      errorList.push(key)
      this.$message({
        showClose: true,
        message: message,
        type: 'error',
        offset: 400,
        duration: (duration == null || duration === undefined) ? 1500 : duration * 1000
      })
      setTimeout(() => {
        let index = errorList.indexOf(key)
        errorList.splice(index, 1)
      }, 1500)
    }
  },
  $MessageBox (o) {
    return MessageBox(o)
  },
  $confirm (message, title, opting) {
    return MessageBox.confirm(message, title, opting)
  },
  confirm_1 (message) {
    return new Promise((resolve, reject) => {
      this.$confirm(message, '提示', {
        confirmButtonText: '重新登入',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        resolve()
      })
    })
  },
  // https://element.eleme.cn/#/zh-CN/component/message-box
  $alert (message, title, opting) {
    this.$MessageBox({
      title: title,
      message: message,
      ...opting
    })
  },
  alert_1 (msg, text) {
    return new Promise((resolve, reject) => {
      this.$alert(msg, '提示', {
        confirmButtonText: text || '我知道了',
        dangerouslyUseHTMLString: true,
        closeOnClickModal: false,
        callback: action => {
          resolve(action)
        }
      })
    })
  },
  alert_2 (title, content, cancelButtonText = '取消', confirmButtonText = '确定') {
    return new Promise((resolve, reject) => {
      this.$alert(content || '', title, {
        cancelButtonText: cancelButtonText,
        confirmButtonText: confirmButtonText,
        dangerouslyUseHTMLString: true,
        showCancelButton: true,
        closeOnClickModal: false,
        callback: (action) => {
          if (action === 'confirm') { // confirmButtonText
            resolve(action)
          }
          if (action === 'cancel') { // cancelButtonText
            reject(action)
          }
        }
      })
    })
  },
  // https://element.eleme.cn/#/zh-CN/component/loading
  $loading (o) {
    var d = Object.assign({
      lock: true,
      text: 'Loading',
      spinner: 'el-icon-loading',
      background: 'transparent'
    }, o)
    return Loading.service(d)
  },
  loading_1 () {
    return this.$loading()
  },
  loading_2 (text) {
    return this.$loading({
      // lock: true,
      text: text || 'Loading',
      spinner: 'el-icon-loading',
      background: 'transparent'
    })
  },
  loading_3 (text) {
    return this.$loading({
      lock: true,
      text: text || 'Loading',
      spinner: 'el-icon-loading',
      background: 'rgba(0, 0, 0, 0.4)'
    })
  },
  // https://element.eleme.cn/#/zh-CN/component/message
  $message (o) {
    return Message(o)
  },
  message_err (msg, o = {}) {
    this.$message({
      showClose: true,
      message: msg,
      type: 'error',
      ...o
    })
  },
  message_success (msg, o = {}) {
    this.$message({
      showClose: true,
      message: msg,
      type: 'success',
      ...o
    })
  },

  // https://element.eleme.cn/#/zh-CN/component/notification
  $Notification (o) {
    return Notification(o)
  },
  Notification_ok (message) {
    this.$Notification({
      title: '成功',
      message: message,
      type: 'success',
      duration: 10 * 1000
    })
  },

  $prompt (message, title, o) {
    var d = Object.assign(o, {
      title: title,
      message: message
    })
    return MessageBox(d)
  }
}
