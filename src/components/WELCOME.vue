<template>
    <div class="hcontainer">
      <span class="demonstration"></span>
      <el-carousel height="650px" class="optimized-carousel">
      <el-carousel-item v-for="item in imgwrap" :key="item.url">
          <el-image :src="item.url" close-on-press-escape="false">img1</el-image>
      </el-carousel-item>
      </el-carousel>
    </div>
</template>
  
  
  <script setup>
  const imgwrap = [
    { url: require('../assets/imgs/xz1.jpg') },
    { url: require('../assets/imgs/TheGreatWall1.jpg') },
    { url: require('../assets/imgs/xz3.jpg') },
    { url: require('../assets/imgs/xz4.jpg') },
    { url: require('../assets/imgs/HongKong1.jpg') },
  ];
  </script>
  
  <style scoped>
  .hcontainer {
    width: 100%;
    height: 100vh;
    overflow: hidden;
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
  
  .demonstration {
    color: var(--el-text-color-secondary);
  }
  
  .el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
    text-align: center;
  }
  
   .optimized-carousel {
    width: 1100px; /* 设置走马灯的宽度为100% */
    height: 650px; /* 设置走马灯的高度为100% */
    transform: scale(1); /* 缩小至90% */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 边缘模糊化加重影处理 */
    perspective: 1000px; /* 加强立体效果 */
    border-radius: 40px;
    margin-left: 5%;
  }
  
  
  .el-image {
    width: 100%; /* 设置图片的宽度为100% */
    height: 100%; /* 设置图片的高度为100% */
  }
  .table1{
      padding: 0 18.5rem 0 19.75rem;
      text-align: center;
      
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