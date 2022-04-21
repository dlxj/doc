<template>
  <div class="itemZh">

      <div v-for="item in todo" :key="item.id">
        <h1> {{ item.id }} </h1>
      </div>

  </div>
</template>

<script>

export default {
    data() {
        return {
            todo:[
                {id:1,ok:true},
                {id:2,ok:false},
                {id:3,ok:true},   
            ]  
        }
    }

}

</script>