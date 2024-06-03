module.exports = {
  lintOnSave: false,
  devServer: {
    open: true,
    //这里的ip和端口是前端项目的;下面为需要跨域访问后端项目
    proxy: {
      '/api': {
        target: 'http://101.43.215.188:8000/api/',//这里填入你要请求的接口的前缀
        ws:true,//代理websocked
        changeOrigin:true,//虚拟的站点需要更管origin
        secure: true,                   //是否https接口
        pathRewrite:{
          '^/api':''//重写路径
        },

      }
    }
  },
  transpileDependencies: true
}

