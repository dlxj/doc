<template>
  <div class="hello">
    <!-- <img src="../assets/play.gif"> -->
    keywd
    <!-- <input type="text" v-for="(item,i) of items" v-model="items[i]" :key="i"> <button @click="search">search</button> -->
    <input v-model="keywdModel.keywd" placeholder="edit me" />
    <button @click="search">search</button>
    <p></p>
    <select v-model="keywdModel.lang_type">
      <option>jp</option>
      <option>zh</option>
    </select>

    <el-select
      v-model="value1"
      multiple
      collapse-tags
      style="margin-left: 20px"
      placeholder="animes"
    >
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      >
      </el-option>
    </el-select>

    <!-- <p>keywd is: {{ keywdModel.keywd }}</p> -->

    <p></p>

    <div class="result_main" v-if="isResultShow">
      <!-- <div v-html="resultModel.result"></div> -->

      <div v-for="item in resultsModel" :key="item.result">
        <div v-html="item.result"></div>
        <br />
      </div>
    </div>

    <div class="result_image">
      <el-collapse v-model="activeName" accordion>
        <el-collapse-item title="一致性 Consistency" name="1">
          <div>
            与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；
          </div>
          <div>
            在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。
          </div>
        </el-collapse-item>
        <el-collapse-item title="反馈 Feedback" name="2">
          <div>
            控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；
          </div>
          <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
        </el-collapse-item>
        <el-collapse-item title="效率 Efficiency" name="3">
          <div>简化流程：设计简洁直观的操作流程；</div>
          <div>
            清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；
          </div>
          <div>
            帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。
          </div>
        </el-collapse-item>
        <el-collapse-item title="可控 Controllability" name="4">
          <div>
            用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；
          </div>
          <div>
            结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>

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
import config from "@/config.js";
let host = config.server.host;

import img_play from "../assets/play.gif";
import img_play2 from "../assets/play2.gif";

const formurlencoded = require("form-urlencoded");
const bent = require("bent");

export default {
  name: "index",
  data() {
    return {
      keywdModel: { keywd: "", lang_type: "jp" },
      resultModel: { result: "" },
      resultsModel: [],
      isResultShow: false,
      items: [],
      options: [
        {
          value: "dangan",
          label: "dangan",
        },
        {
          value: "poke",
          label: "poke",
        },
      ],
      value1: [],
      activeName: "1",
    };
  },
  computed: {
    itemNum: function () {
      return this.items.length;
    },
  },
  methods: {
    async search() {
      let keywd = this.keywdModel.keywd;
      let lang_type = this.keywdModel.lang_type;

      if (keywd == "") {
        return;
      }

      //let host = 'localhost:81'
      let url = `http://${host}`;
      let json = {
        keywd,
        type: "anime",
        lang_type,
      };
      let formurlencoded_json = formurlencoded(json);

      let post = bent(url, "POST", "json", 200); //debugger
      let response = await post("/search", formurlencoded_json, {
        "Content-Type": "application/x-www-form-urlencoded",
      });

      if (response.status == 200 && response.data.length > 0) {
        //let { id, jp, name, seasion, time, zh } = response.data[0]
        //let result = `${jp}<br>${zh}`

        const data = [];
        for (let { id, jp, type, name, seasion, time, zh } of response.data) {
          //let bs = process.env.BASE_URL; debugger
          let elm_id = `${type}_${name}_${seasion}_${id}`;
          let au_url = `${url}/getaudio?type=${type}&name=${name}&seasion=${seasion}&id=${id}`;

          //
          let result = `${jp}<img id="img_${elm_id}" src="${img_play}" onclick="play('${elm_id}')"><audio id="audio_${elm_id}" src="${au_url}" type="audio/mpeg" preload="auto"></audio><br>${zh}`; //debugger
          //let result = `${jp}<div @click="play"><img id="img_${elm_id}" src="${img_play}"></div><audio id="audio_${elm_id}" src="${au_url}" type="audio/mpeg" preload="auto"></audio><br>${zh}`; //debugger
          data.push({ result });
        }
        data.push({ result: `<br><button onclick="next()">next</button>` });

        // let audio_dir = path.join(global.animes.root_audio, type, name, seasion)
        // let audio_path = path.join(audio_dir, `${id}.mp3`)
        // http://127.0.0.1:80/getaudio?type=anime&name=danganronpa&seasion=S01&id=1

        // <audio id="@($"audio{row.id}")" src="@($"{url}")" type="audio/mpeg" preload="auto"></audio>
        // onclick="openImg()"

        this.resultsModel = data;

        //this.$set(this.resultModel, 'result', result)  // 强制重绘
        // this.$set(this.keywdModel, 'keywd', 'aaaa')

        //this.resultModel.result = result
        this.isResultShow = true;
        this.$nextTick(() => {
          // DOM 渲染完后回调
          //debugger
        });
      } else {
        console.log(`Waring: POST fail. ${url}/search`);
      }

      console.log("hited.");
    },
  },
  mounted() {
    window.play = function (elm_id) {
      let auid = `audio_${elm_id}`;
      var igid = `img_${elm_id}`;

      let au = document.getElementById(auid);
      let ig = document.getElementById(igid);
      if (au.paused) {
        au.play();
        ig.src = img_play2;
        // this.$nextTick(() => {
        //   // DOM 渲染完后回调
        //   //debugger
        // })

        au.addEventListener("pause", function () {
          ig.src = img_play;
        });
      }
      // var au = <HTMLAudioElement>document.getElementById(auid);
      // //var ig = <HTMLImageElement>document.getElementById("img"+id);

      // console.log(`openImg clicked. ${elm_id}`); debugger
    };
    let search = this.search;
    window.next = async function () {
      await search();
    };
  },
  // watch: {

  //   items (newVal) {
  //     isListShow = false
  //     this.$nextTick(() => {
  //       isListShow = true
  //     })
  //   }

  // }
};
</script>

<!--

type:anime
name:danganronpa
seasion:S01
id:1
            @((MarkupString)@row.jp) <img id="@($"img{row.id}")" src="images/play.gif" alt="play" @onclick="@(() => HandlePlayAudio($"{row.id}"))" style=" cursor: pointer">



<img v-bind:src="./assets/logo.png">


<img :src="static/images/play.gif">


<img :src="'/static/imgs/' + source + '.png'"



  // <audio id="@($"audio{row.id}")" src="@($"{url}")" type="audio/mpeg" preload="auto"></audio>

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


interface Window {
    Music: any;
}

function Play(element, flag) {
    var dom = document.querySelector(element);
    if (flag) {
        dom.play();
    }
    else {
        dom.pause();
    }
}

function GetMusicTime(element) {
    var dom = document.querySelector(element);
    let obj = {
        currentTime: dom.currentTime,
        duration: dom.duration
    }
    let json = JSON.stringify(obj);

    return json
}

function SetMusicTime(element, time) {
    var dom = document.querySelector(element);
    dom.currentTime = time;
}

window.Music = {
    //print: Print,
    play: Play,
    getMusicTime: GetMusicTime,
    setMusicTime: SetMusicTime
}

function playaudio(id) {
    var au = <HTMLAudioElement>document.getElementById("audio"+id);
    var ig = <HTMLImageElement>document.getElementById("img"+id);

    if (au.paused) {
        au.play();
        ig.src = "images/play2.gif";
        au.addEventListener("pause", function () {
            ig.src = "images/play.gif";
        });
    }

    /*
     
     document.getElementById('img').setAttribute('src', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==');
     
     */
}


ここ
-->
