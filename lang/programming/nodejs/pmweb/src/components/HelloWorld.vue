<template>
  <div class="hello">
    keywd
    <input v-model="message" placeholder="edit me" />  <button @click="search">search</button>
    <p>Message is: {{ message }}</p>

    <ul id="example-1">
      <li v-for="item in items" :key="item.message">
        {{ item.message }}
      </li>
    </ul>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      message: '',
      items: [
        { message: 'Foo' },
        { message: 'Bar' }
      ]
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
        console.log('hited.')
      })
    }

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
