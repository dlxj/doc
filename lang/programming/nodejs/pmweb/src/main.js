
import Vue from 'vue'
import App from './App'
import router from './router'

(async () => {


  const config = require('./config')
  console.log(config.server.encrypt)
  const bent = require('bent')
  const getBuffer = bent('buffer')
  let buffer = await getBuffer('https://cn.vuejs.org/images/logo.svg'); debugger

  // require('fs').writeFileSync('logo.svg', buffer)  // 浏览器不能写本地文件

  // console.log(getBuffer)

  Vue.config.productionTip = false

  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })

})()
