<template>
  <div>
    <h1>{{ msg }}</h1>
    <button @click="showMsg">showMsg</button>
    <!-- this.$ElementUI.message_success('ok') -->
  </div>
</template>

<script>
export default {
  name: 'welcome!',
  data () {
    return {
      msg: 'hi,,,'
    }
  },
  methods: {
    showMsg () {
      this.$ElementUI.message_success('ok')
      console.log('hited.')
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
