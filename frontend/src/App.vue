<template>
  <div id="app">
    <div class="mb-4">
      <app-nav />
    </div>

    <router-view />
  </div>
</template>

<script>
import AppNav from "./components/nav/AppNav.vue";

export default {
  components: {
    AppNav,
  },
};
</script>

<style>
</style>
