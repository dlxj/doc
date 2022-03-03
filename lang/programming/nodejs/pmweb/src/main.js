
import Vue from 'vue'
import App from './App'
import router from './router'

( async () => {

  // const config = require('./config')
  // console.log(config.server.encrypt)
  let formurlencoded = require('form-urlencoded')
  const bent = require('bent')
  const getBuffer = bent('buffer')
  let buffer = await getBuffer('https://cn.vuejs.org/images/logo.svg'); debugger

  let host = 'localhost:80'
  let url = `http://${host}`
  let json = {
    passwd: 'rn'
  }
  let formurlencoded_json = formurlencoded(json)

  let post = bent(url, 'POST', 'json', 200)
  let response = await post('/anime/insert', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded' })

  if (response.status == 200) {
    // return [response.data, '']
  } else {
    // return [null, response.msg]
  }

  // require('fs').writeFileSync('logo.svg', buffer)  // 浏览器不能写本地文件

  Vue.config.productionTip = false

  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })

})()


