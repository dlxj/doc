<template>
  <div class="hello">
    keywd
    <!-- <input type="text" v-for="(item,i) of items" v-model="items[i]" :key="i"> <button @click="search">search</button> -->
    <input v-model="keywdModel.keywd" placeholder="edit me" />  <button @click="search">search</button>
    <!-- <p>keywd is: {{ keywdModel.keywd }}</p> -->
    <p></p>

    <div v-html="resultModel.result"></div>

    <!-- v-if 是条件渲染，每次状态更新都会重新删除或者创建元素，但v-if有较高的切换性能消耗 -->
    <!-- Vue 官方中不推荐v-for 和v-if 在同一标签中共同使用。因此，给上述示例代码外面加上一层div，isListShow 为true 时创建，为false 时销毁 -->
    <!-- <div class="list_main" v-if="isListShow">
      <ul id="example-1">
        <li v-for="item in items" :key="item.message">
          {{ item.message }}
        </li>
      </ul>
    </div> -->

  </div>
</template>

<script>

// import config from '@/config.js'

const formurlencoded = require('form-urlencoded')
const bent = require('bent')

export default {
  name: 'HelloWorld',
  data () {
    return {
      keywdModel:  { keywd: '' },
      resultModel: { result: '' },
      items: []
    }
  },
  computed: {
    itemNum: function () {
      return this.items.length
    }
  },
  methods: {

    async search () {

      let keywd = this.keywdModel.keywd

      let host = 'localhost:80'
      let url = `http://${host}`
      let json = {
        keywd: 'ここ',
        type: 'anime'
      }
      let formurlencoded_json = formurlencoded(json)

      let post = bent(url, 'POST', 'json', 200)
      let response = await post('/search', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded' })

      if (response.status == 200) {
        // return [response.data, '']
      } else {
        // return [null, response.msg]
      }

      if (response.data.length > 0) {

        let { id, jp, name, seasion, time, zh } = response.data[0]; debugger
        let result = `${jp}<br>${zh}`

        this.$set(this.resultModel, 'result', result)  // 强制重绘
        // this.$set(this.keywdModel, 'keywd', 'aaaa')
        this.$nextTick(() => {
          // DOM 渲染完后回调
        })


      }


      console.log('hited.')
    }

  }
  // watch: {

  //   items (newVal) {
  //     isListShow = false
  //     this.$nextTick(() => {
  //       isListShow = true
  //     })
  //   }

  // }
}
</script>

<!--

<template>
  <div>
    <input type="text" v-for="(item,i) of items" v-model="items[i]" :key="i">
    <button @click="onAdd">添加</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: []
    }
  },
  methods: {
    onAdd() {
      this.items.push('')
    }
  }
}
</script>

// template
<input type="text" v-model="computeValue">

// js
data () {
    return {
        form: {
            computeValue: ''
        }
    }
}
computed: {
    computeValue: {
      get () {
        return this.form.computeValue
      },
      set (val) {
        this.form.computeValue = val.replace(/[9]/g, 'a')
      }
    }
}

      // 1. 异步渲染，$nextTick 待 DOM 渲染完再回调
      // 2. 页面渲染时会将 data 的修改做整合，多次 data 修改只会渲染一次
      this.$nextTick(() => {
        // 获取 DOM 元素
        // const ulElem = this.$refs.ul1
        // 如果没加$nextTick,点击第一次，li的节点是3个（为何不是6个），因为dom是异步渲染，data数据改变不会立刻渲染
        // console.log( ulElem.childNodes.length )
        items = [
          { message: 'Xoo' },
          { message: 'Yar' }
        ]
        console.log('hited.')
      })
-->

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!--
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
-->
