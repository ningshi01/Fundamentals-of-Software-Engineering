<template>
  <div class="mycon">
    <div class="blur-background"></div>
    <fornav msg1=车次调控 msg2=主页 msg3=个人信息 msg4=列车信息 msg5=设置
    href1=#/trainAdjust1 href2=#/trainAdjust2 href3=#/trainAdjust3 href4=#/trainAdjust4 href5=#/></fornav>
    <div class="hcon">
      <img src="../../assets/cat.png" alt="" class="flg">
      <img src="../../assets/logo.png" alt="" class="lg">
      <br><h1 id="welcome">MewTrain欢迎您,尊敬的铁路系统员！</h1><br>
    </div>
    <div class="table1">
      <div class="block text-center">
          <span class="demonstration"></span>
          <el-carousel height="650px" class="optimized-carousel">
          <el-carousel-item v-for="item in imgwrap" :key="item.url">
              <el-image :src="item.url" close-on-press-escape="false">img1</el-image>
          </el-carousel-item>
          </el-carousel>
      </div>
    </div>
  </div>
</template>

<script>
import fornav from './fornav.vue';
export default {
    name: "My_trainAdjust_home",
    data(){
        return{
            imgwrap:[
    { url: require('../../assets/imgs/xz1.jpg') },
    { url: require('../../assets/imgs/TheGreatWall1.jpg') },
    { url: require('../../assets/imgs/xz3.jpg') },
    { url: require('../../assets/imgs/xz4.jpg') },
    { url: require('../../assets/imgs/HongKong1.jpg') },
            ]
        }
    },
    components: {
        fornav,
    },
    methods: {
    },
}
</script>

<style scoped>

.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  height: 100%;
  margin: 0;
  text-align: center;
}
.table1{
    padding: 0 18.5rem 0 19.75rem;
    text-align: center;
}

.optimized-carousel {
  width: 1250px; /* 设置走马灯的宽度为100% */
  height: 600px; /* 设置走马灯的高度为100% */
  transform: scale(1); /* 缩小至90% */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 边缘模糊化加重影处理 */
  perspective: 1000px; /* 加强立体效果 */
  border-radius: 40px;
  margin-left: -20%;
}
.el-image {
  width: 100%; /* 设置图片的宽度为100% */
  height: 100%; /* 设置图片的高度为100% */
}
.demo-image .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  vertical-align: top;
}
.demo-image .block:last-child {
  border-right: none;
}
.demo-image .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
</style>