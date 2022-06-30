<template>
  <div class="container">
    <b-row>
      <b-col cols="4" class="text-center my-4 mx-auto">
        <h1>Newsfeed Portal</h1>
      </b-col>
    </b-row>

    <b-row v-if="!loggedIn">
      <b-col cols="4" class="text-center mx-auto">
        <form-login></form-login>
      </b-col>
    </b-row>

    <news-list v-else></news-list>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import FormLogin from "../components/account/FormLogin.vue";
import NewsList from "../components/news/NewsList.vue";

export default {
  components: { FormLogin, NewsList },

  computed: {
    ...mapGetters("account", ["loggedIn"])
  }
};
</script>
