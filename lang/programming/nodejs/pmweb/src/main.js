
import Vue from 'vue'
import App from './App'
import router from './router'

import 'normalize.css/normalize.css' // a modern alternative to CSS resets
import './styles/element-variables.scss'

import Element from 'element-ui'
// import VueCarousel from 'vue-carousel'
import Carousel3d from 'vue-carousel-3d'

// import JSMpeg from '@/util/jsmpeg.js' // https://blog.csdn.net/focusmickey/article/details/111269204

import '@/util/jsmpeg.js' // 要点：修改 jsmpeg.js ,  将 JSMpeg 赋值给 window 对象   window.JSMpeg = JSMpeg;    // https://blog.csdn.net/m0_46627730/article/details/106132847   

//import JSMpeg from '@cycjimmy/jsmpeg-player' // https://github.com/cycjimmy/jsmpeg-player  // npm install @cycjimmy/jsmpeg-player --save

( async () => {

  // const config = require('./config')
  // console.log(config.server.encrypt)
  let formurlencoded = require('form-urlencoded')
  const bent = require('bent')
  const getBuffer = bent('buffer')
  // let buffer = await getBuffer('https://cn.vuejs.org/images/logo.svg')

  // npm run dev
  // let host = 'localhost:80'
  // let url = `http://${host}`
  // // let json = {
  // //   passwd: 'rn'
  // // }
  // // let formurlencoded_json = formurlencoded(json)

  // // let post = bent(url, 'POST', 'json', 200)
  // // let response = await post('/anime/insert', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded' })
  // let json = {
  //   keywd: 'ここ',
  //   type: 'anime'
  // }
  // let formurlencoded_json = formurlencoded(json)

  // let post = bent(url, 'POST', 'json', 200)
  // let response = await post('/search', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded' })

  // if (response.status == 200) {
  //   // return [response.data, '']
  // } else {
  //   // return [null, response.msg]
  // }

  // require('fs').writeFileSync('logo.svg', buffer)  // 浏览器不能写本地文件

  Vue.config.productionTip = false

  Vue.use(Element, {size: 'mini'})  // 所有拥有 size 属性的组件默认尺寸全部设为 small
  // Vue.use(VueCarousel, {size: 'mini'})
  Vue.use(Carousel3d)

  // Vue.use(JSMpeg)

  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })

})()


