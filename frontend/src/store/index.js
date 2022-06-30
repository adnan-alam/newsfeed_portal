import Vue from "vue";
import Vuex from "vuex";

import * as account from "./account/account.js";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: { account },
});
