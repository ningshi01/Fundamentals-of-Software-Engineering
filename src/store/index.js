import { createStore } from "vuex";
const store = createStore({
    state: {
        token: null,
        isLogin:false
      },
    mutations: {
        setToken(state, token) {
            console.log(token)
            state.token = token;
            console.log(state.token)
          },
          setLogin(state,isLogin){
            state.isLogin=isLogin
          }
          
    },
    actions: {},

    getters: {},

    modules: {},
})
export default store;

