import { createStore } from "vuex";
const store = createStore({
    state: {
        token: null,
        isLogin:false,
        nowUserID:0
      },
    mutations: {
        setToken(state, token) {
            console.log(token)
            state.token = token;
            console.log(state.token)
          },
          setLogin(state,isLogin){
            state.isLogin=isLogin
          },
          setUserID(state,nowUserID){
            state.nowUserID=nowUserID
          }
          
    },
    actions: {},

    getters: {},

    modules: {},
})
export default store;

