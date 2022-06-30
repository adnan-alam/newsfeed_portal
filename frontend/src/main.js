import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import Toasted from "vue-toasted";

// Import Bootstrap an BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import apiClient from "./service/ApiClient";

window.Vue = Vue;

Vue.config.productionTip = false;

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

Vue.use(Toasted, {
  class: "rouded",
  position: "bottom-right",
  fitToScreen: true,
  theme: "toasted-primary",
  duration: 3000,
});


new Vue({
  router,
  store,
  render: (h) => h(App),
  created() {
    const tokenDataString = localStorage.getItem("tokenData");
    if (tokenDataString) {
      const tokenData = JSON.parse(tokenDataString);
      this.$store.commit("account/SET_TOKEN_DATA", tokenData);
    }

    apiClient.interceptors.response.use(
      (response) => response,
      (error) => {
        console.log(error.response);
        if (error.response.status === 401) {
          this.$store.dispatch("account/refreshToken");
          // this.$router.push("/");
          // this.$store.commit("LOGOUT");
        }
        return Promise.reject(error);
      }
    );
  },
}).$mount("#app");
