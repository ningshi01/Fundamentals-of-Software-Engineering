<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="body">
      <div class="main">
        <div class="switch-component">
          <div class="switch" id="switch-cnt">
            <div class="switch__circle"></div>
            <div class="switch__circle switch__circle--t"></div>
            <div class="switch__container" id="switch-c1">
              <h2 class="switch__title title">Welcome Back !</h2>
              <p class="switch__description description">To keep connected with us please login with your personal info</p>
              <button class="switch__button button switch-btn" @click="change">SIGN IN</button>
            </div>
            <div class="switch__container is-hidden" id="switch-c2">
              <h2 class="switch__title title">Hello Friend !</h2>
              <p class="switch__description description">Enter your personal details and start journey with us</p>
              <button class="switch__button button switch-btn" @click="change">SIGN UP</button>
            </div>
          </div>
        </div>
        <div class="sign__container is-hidden" id="SignIn" ><sign-in class="sign_Page"></sign-in></div>
        <div class="sign__container" id="SignUp" ><sign-up class="sign_Page"></sign-up> </div>
      <!-- <sign-in class="sign__container" id="SignIn" v-if="isSignIn"></sign-in>
      <sign-up class="sign__container is-hidden" id="SignUp" v-else></sign-up> -->
      </div>
  </div>
</template>

<script>
import SignIn from './login/sign_in.vue'
import SignUp from './login/sign_up.vue'


export default {
methods: {

  change() {
    const switchC1 = document.querySelector("#switch-c1");
    const switchC2 = document.querySelector("#switch-c2");

    const signIn=document.querySelector("#SignIn");
    const signUp=document.querySelector("#SignUp");


    signIn.classList.toggle("is-hidden");
    signUp.classList.toggle("is-hidden");
    switchC1.classList.toggle("is-hidden");
    switchC2.classList.toggle("is-hidden");
   // this.isSignIn = !this.isSignIn;
  }
},
  
  components: {
    SignIn,
    SignUp,
  },
  data() {
    return {
      isSignIn: true
    }
  }
}
</script>
<style scoped >
.switch__title {
  text-align: center;
}
.switch__button {
  text-align: center;}
.switch__container {
    text-align: center;
  }
@import '../assets/login.css';
*, *::after, *::before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  user-select: none;
}

.body {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Montserrat", sans-serif;
  font-size: 12px;
  background-color: #ecf0f3;
  color: #a0a5a8;
}
.switch-component {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 400px;
}
.main {
  position: relative;
  width: 1000px;
  min-width: 1000px;
  min-height: 600px;
  height: 600px;
  padding: 25px;
  background-color: #ecf0f3;
  box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
  border-radius: 20px;
  overflow: hidden;
}
@media (max-width: 1200px) {
  .main {
    transform: scale(0.7);
  }
}
@media (max-width: 1000px) {
  .main {
    transform: scale(0.6);
  }
}
@media (max-width: 800px) {
  .main {
    transform: scale(0.5);
  }
}
@media (max-width: 600px) {
  .main {
    transform: scale(0.4);
  }
}
</style>
