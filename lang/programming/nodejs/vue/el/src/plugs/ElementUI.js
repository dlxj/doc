// 常用提示
import {
  Loading,
  Message,
  MessageBox,
  Notification
} from 'element-ui'
var errorList = []
export default {
  init() {

  },
  success(message, duration) {
    this.$message({
      showClose: true,
      message: message,
      type: 'success',
      offset: 400,
      duration: (duration == null || duration == undefined) ? 1500 : duration * 1000
    });
  },
  error(message, duration) {
    this.$message({
      showClose: true,
      message: message,
      type: 'error',
      offset: 300,
      duration: (duration == null || duration == undefined) ? 3000 : duration * 1000
    });
  },
  warning(message, duration) {
    this.$message({
      showClose: true,
      message: message,
      type: 'warning',
      offset: 400,
      duration: (duration == null || duration == undefined) ? 3000 : duration * 1000
    });
  },
  errorList(key, message, duration) {
    if (errorList.indexOf(key) == -1) {
      errorList.push(key);
      this.$message({
        showClose: true,
        message: message,
        type: 'error',
        offset: 400,
        duration: (duration == null || duration == undefined) ? 1500 : duration * 1000
      });
      setTimeout(() => {
        let index = errorList.indexOf(key)
        errorList.splice(index, 1)
      }, 1500);
    }

  },
  $MessageBox(o) {
    return MessageBox(o)
  },
  $confirm(message, title, opting) {
    return MessageBox.confirm(message, title, opting)
  },
  confirm_1(message) {
    return new Promise((ok, err) => {
      this.$confirm(message, "提示", {
        confirmButtonText: '重新登入',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        ok()
      })
    })
  },
  //https://element.eleme.cn/#/zh-CN/component/message-box
  $alert(message, title, opting) {
    this.$MessageBox({
      title: title,
      message: message,
      ...opting,
    })
  },
  alert_1(msg, text) {
    return new Promise((ok, err) => {
      this.$alert(msg, '提示', {
        confirmButtonText: text || '我知道了',
        dangerouslyUseHTMLString: true,
        closeOnClickModal:false,
        callback: action => {
          ok(action)
        }
      })
    })
  },
  alert_2(title, content, cancelButtonText = "取消", confirmButtonText = "确定") {
    return new Promise((ok, err) => {
      this.$alert(content || "", title, {
        cancelButtonText: cancelButtonText,
        confirmButtonText: confirmButtonText,
        dangerouslyUseHTMLString: true,
        showCancelButton: true,
        closeOnClickModal:false,
        callback: (action) => {
          if (action == "confirm") { //confirmButtonText
            ok(action)
          }
          if (action == "cancel") { //cancelButtonText
            err(action)
          }
        }
      })
    })
  },
  //https://element.eleme.cn/#/zh-CN/component/loading
  $loading(o) {
    var d = Object.assign({
      lock: true,
      text: 'Loading',
      spinner: 'el-icon-loading',
      background: 'transparent'
    }, o)
    return Loading.service(d)
  },
  loading_1() {
    return this.$loading()
  },
  loading_2(text) {
    return this.$loading({
      // lock: true,
      text: text || 'Loading',
      spinner: 'el-icon-loading',
      background: 'transparent'
    });
  },
  loading_3(text) {
    return this.$loading({
      lock: true,
      text: text || 'Loading',
      spinner: 'el-icon-loading',
      background: 'rgba(0, 0, 0, 0.4)'
    });
  },
  // https://element.eleme.cn/#/zh-CN/component/message
  $message(o) {
    return Message(o)
  },
  message_err(msg, o = {}) {
    this.$message({
      showClose: true,
      message: msg,
      type: "error",
      ...o
    });
  },
  message_success(msg, o = {}) {
    this.$message({
      showClose: true,
      message: msg,
      type: "success",
      ...o
    });
  },

  // https://element.eleme.cn/#/zh-CN/component/notification
  $Notification(o) {
    return Notification(o)
  },
  Notification_ok(message) {
    this.$Notification({
      title: '成功',
      message: message,
      type: 'success',
      duration: 10 * 1000,
    })
  },

  $prompt(message,title,o){
    var d = Object.assign(o,{
      title:title,
      message:message,
    })
    return MessageBox(d)
  },
  // prompt_1(){
  //   return new Promise((ok,err)=>{
  //     this.$prompt('内容', '提示', {
  //       confirmButtonText: '确定',
  //       cancelButtonText: '取消',
  //       inputPattern: /.+/,
  //       inputErrorMessage: '正则错误提示',

  //       showInput:"",  //	是否显示输入框	boolean	—	false（以 prompt 方式调用时为 true）
  //       inputPlaceholder:"", //	输入框的占位符	string	—	—
  //       inputType:"",  //	输入框的类型	string	—	text
  //       inputValur:"", //	输入框的初始文本	string	—	—
  //       inputPattern:"", //	输入框的校验表达式	regexp	—	—
  //     }).then(({ value }) => {
  //       ok(value)
  //     }).catch(() => {
  //       err()
  //     });
  //   })
  // }
}