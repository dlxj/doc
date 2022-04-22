<template>
  <div class="itemZh">

      <div v-for="item in rawresultsModel" :key="item.elm_id">

        <div v-html="`${item.jp}`"></div> <img :id="`img_${item.elm_id}`" :src="`${item.img_play}`" @onclick="`play('${item.elm_id}')`"><audio :id="`audio_${item.elm_id}`" :src="`${item.au_url}`" type="audio/mpeg" preload="auto"></audio><br>{{item.zh}}

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
    props: ['rawresultsModel']
}

</script>