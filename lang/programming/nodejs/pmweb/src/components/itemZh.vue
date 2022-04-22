<template>
  <div class="itemZh">

      <div v-for="item in todo" :key="item.id">
        <h1> {{ item.id }} </h1>
      </div>

  </div>
</template>

<script>

export default {
    name: 'itemZh',
    data() {
        return {
        }
    },
    props: ['todo']
}

</script>