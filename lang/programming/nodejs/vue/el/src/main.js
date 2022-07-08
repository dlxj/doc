// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

Vue.use(ElementUI)

/**
 * 安装自定义插件
 */
const plugs = require.context('@/plugs/', false, /.js$/i).keys();
const plugDict = {};
for (let p of plugs) {
  const name = p.replace(/\.\/([\S]+?)\.js/g, '$1');
  let plug = require(`@/plugs/${name}.js`).default;
  if (typeof (plug) === 'function') {
    plug = new plug();
  }
  plugDict[`$${name}`] = plug;
  //安装
  Vue.use({
    install(v) {
      v.prototype[`$${name}`] = new Proxy(plug, {
        get(target, key) {
          if (plug[key] !== undefined) {
            return plug[key];
          } else {
            console.log(key);
            return v.prototype[key];
          }
        }
      });
    }
  });
}
for (const key in plugDict) {
  const plug = plugDict[key];
  Object.assign(plug, plugDict);
}
for (const key in plugDict) {
  const plug = plugDict[key];
  if (plug !== null && plug !== undefined && typeof (plug.init) === 'function') {
    plug.init();
    delete plug['init'];
  }
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
