<template>
  <div class="container">
    <b-row>
      <b-col cols="4" class="text-center my-4 mx-auto">
        <h1>Newsfeed Portal Settings</h1>
      </b-col>
    </b-row>

    <b-row>
      <b-col cols="4" class="text-center my-4 mx-auto">
        <form-news-settings></form-news-settings>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import FormNewsSettings from "../components/settings/FormNewsSettings.vue";

export default {
  components: { FormNewsSettings }
};
</script>
