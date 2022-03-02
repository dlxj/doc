<template>
  <div class="hello">
    keywd
    <input v-model="message" placeholder="edit me" />  <button @click="search">search</button>
    <p>Message is: {{ message }}</p>

    <!-- v-if 是条件渲染，每次状态更新都会重新删除或者创建元素，但v-if有较高的切换性能消耗 -->
    <!-- Vue 官方中不推荐v-for 和v-if 在同一标签中共同使用。因此，给上述示例代码外面加上一层div，isListShow 为true 时创建，为false 时销毁 -->
    <div class="list_main" v-if="isListShow">
      <ul id="example-1">
        <li v-for="item in items" :key="item.message">
          {{ item.message }}
        </li>
      </ul>
    </div>

  </div>
</template>

<script>

let isListShow = true

let items = [
  { message: 'Foo' },
  { message: 'Bar' }
]

export default {
  name: 'HelloWorld',
  data () {
    return {
      message: '',
      isListShow,
      items
    }
  },
  methods: {

    search () {

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
    }

  },
  watch: {



  }
}
</script>

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
