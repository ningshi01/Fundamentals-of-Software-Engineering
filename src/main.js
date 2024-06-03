import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import ElementPlus from 'element-plus'
import 'element-plus/theme-chalk/index.css'
import store from './store'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import mitt from 'mitt'
import './assets/global.css'
import './assets/icon/right/iconfont.css'

const app = createApp(App)

const debounce = (fn, delay) => {
    let timer = null;
    return function () {
      let context = this;
      let args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () {
        fn.apply(context, args);
      }, delay);
    }
  }
  
  const _ResizeObserver = window.ResizeObserver;
  window.ResizeObserver = class ResizeObserver extends _ResizeObserver{
    constructor(callback) {
      callback = debounce(callback, 16);
      super(callback);
    }
  }

app.use(router)
app.use(ElementPlus)
app.use(store)
const emitter = mitt()
app.config.globalProperties.emitter = emitter
app.provide('appContext', app)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.mount('#app')