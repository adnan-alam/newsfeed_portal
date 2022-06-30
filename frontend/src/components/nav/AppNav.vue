<template>
  <div id="nav">
    <router-link to="/">
      News
    </router-link>
    <router-link v-if="loggedIn" to="/settings">
      Settings
    </router-link>
    <b-button v-if="loggedIn" variant="white" @click="logout">
      Logout
    </b-button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("account", ["loggedIn"])
  },

  methods: {
    logout() {
      this.$store.dispatch("account/logoutUser");
    }
  }
};
</script>

<style scoped>
#nav {
  display: flex;
  align-items: center;
  min-height: 50px;
  padding: 0.2em 1em;
  background: linear-gradient(to right, #16c0b0, #84cf6a);
}
.nav-welcome {
  margin-left: auto;
  margin-right: 1rem;
  color: white;
}
a {
  font-weight: bold;
  color: #2c3e50;
  margin: auto 0.8em auto 0.4em;
  text-decoration: none;
  border-top: 2px solid transparent;
  border-bottom: 2px solid transparent;
}
.router-link-exact-active {
  color: white;
  border-bottom: 2px solid #fff;
}
button,
.button {
  margin-left: auto;
  background: white;
  text-decoration: none;
  color: #2c3e50;
  padding: 5px;
  border-radius: 5px;
}
button.router-link-active,
.button.router-link-active {
  color: #2c3e50;
}
.logoutButton {
  cursor: pointer;
}
.nav-welcome + button {
  margin-left: 0;
}
</style>
