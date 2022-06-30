<template>
  <div class="container">
    <b-row>
      <b-col cols="4" class="text-center my-4 mx-auto">
        <h1>Newsfeed Portal</h1>
      </b-col>
    </b-row>

    <b-row>
      <b-col cols="4" class="text-center mx-auto">
        <form-login></form-login>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import FormLogin from "../components/account/FormLogin.vue";

export default {
  components: {
    FormLogin
  }
};
</script>
