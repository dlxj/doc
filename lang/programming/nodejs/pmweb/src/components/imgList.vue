<template>
  <el-carousel
    ref="carousel"
    trigger="click"
    :initial-index="nowIndex"
    height="500px"
    :autoplay="false"
    arrow="never"
  >
    <el-carousel-item
      v-for="(item, index) in urlShow"
      :key="index"
      width="100%"
      height="100%"
    >
      <el-image
        :src="item.srcPath"
        v-if="item"
        width="100%"
        height="100%"
      ></el-image>
      <!-- <smlCanvas
        :coords="item.coors"
        :src="item.srcPath"
        v-if="item"
      ></smlCanvas> -->
    </el-carousel-item>
    <div @click="prevEvent" class="click-btn prev-btn">
      <i class="el-icon-caret-left"></i>
    </div>
    <div @click="nextEvent" class="click-btn next-btn">
      <i class="el-icon-caret-right"></i>
    </div>
  </el-carousel>
</template>

<script>

// import { Carousel } from 'vue-carousel'

export default {
  name: "imgList",
  data() {
    return {
      urlShow: [], //展示图片列表
      nowIndex: 0, //当前展示的幻灯片索引
      urlsLen: 0, //urls的长度
      showLen: 3, //此时页面中已加载多少张图片，初始值与initLen一致
      initLen: 3, //页面进入加载图片的张数
      prevNum: 0, //记录已点击上一张按钮多少次
      nextNum: 0, //记录已点击下一张按钮多少次
    };
  },
  methods: {
    showImg() {
      this.urlsLen = this.urls.length;
      if (this.urlsLen < 3) {
        //当数据少于3张的时候
        this.initLen = this.urlsLen;
        this.showLen = this.urlsLen;
      }
      this.urlShow = new Array(this.urlsLen); //根据url的长度来创建一个展示图片的List
      if (this.order === "asc") {
        //进入页面展示第一张
        this.nowIndex = 0;
        for (let i = 0; i < this.showLen; i++) {
          //赋值urlShow的前三个元素
          this.urlShow[i] = this.urls[i];
        }
      } else {
        //进入页面展示最后一张
        this.nowIndex = this.urlsLen - 1;
        for (let i = 0; i < this.showLen; i++) {
          //赋值urlShow的后三个元素
          let num = this.urlsLen - 1 - i;
          this.urlShow[num] = this.urls[num];
        }
      }
    },
    nextEvent() {
      //点击下一张按钮
      if (this.showLen < this.urlsLen) {
        if (this.order === "asc") {
          let diffNext = this.initLen + this.nextNum;
          if (!this.urlShow[diffNext]) {
            this.urlShow[diffNext] = this.urls[diffNext];
          }
        } else {
          let diffNext = this.nextNum;
          if (!this.urlShow[diffNext]) {
            this.urlShow[diffNext] = this.urls[diffNext];
          }
        }
        this.nextNum += 1;
        this.showLen += 1;
      }
      if (this.nowIndex === this.urlsLen - 1) {
        this.nowIndex = 0;
      } else {
        this.nowIndex = this.nowIndex + 1;
      }
      this.$refs.carousel.setActiveItem(this.nowIndex);
    },
    prevEvent() {
      //上一张按钮点击
      if (this.showLen < this.urlsLen) {
        //若图片还未加载完全
        // 依次加入图片
        if (this.order === "asce") {
          //初始图片从一张展示，所以此时从队尾依次往前加载
          let diff = this.urlsLen - this.prevNum - 1;
          if (!this.urlShow[diff]) {
            // 若数据不存在，赋值，存在就不需要了
            this.urlShow[diff] = this.urls[diff];
          }
        } else {
          // 初始图片从最后一张展示，所以从第（urlsLen-initLen）张依次往前加载
          let diff = this.urlsLen - this.initLen - this.prevNum - 1;
          if (!this.urlShow[diff]) {
            this.urlShow[diff] = this.urls[diff];
          }
        }
        this.prevNum += 1; //上一张点击次数+1
        this.showLen += 1; //已加载的数据+1
      }
      if (this.nowIndex === 0) {
        //若此时展示的是第一张，上一张就是最后一张
        this.nowIndex = this.urlsLen - 1;
      } else {
        //否则就是上一张
        this.nowIndex = this.nowIndex - 1;
      }
      this.$refs.carousel.setActiveItem(this.nowIndex);
    },
  },
  created() {
    this.showImg();
  },
//   components: { Carousel },  // componentItemZh step 2: register the component
  props: ["urls", "order"], // 定义形参，父组件调用的时侯要这样传实参:  <imgList :urls="urls" :order="order"></imgList>
}
</script>