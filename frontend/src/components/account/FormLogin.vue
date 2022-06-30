<template>
  <div>
    <b-form @submit.prevent="onSubmit">
      <b-form-group label="Username">
        <b-form-input
          v-model="form.username"
          type="text"
          placeholder="Enter username"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group label="Password">
        <b-form-input
          v-model="form.password"
          type="password"
          placeholder="Enter password"
          required
        ></b-form-input>
      </b-form-group>

      <div class="my-4">
        <b-button type="submit" variant="primary">Login</b-button>
      </div>
    </b-form>

    <router-link to="/register">
      Don't have an account? Register
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    onSubmit() {
      this.$store.dispatch("account/loginUser", this.form).then(response => {
        if (response.status == 200) {
          this.$router.push({ name: "HomePage" });
        }
      });
    }
  }
};
</script>
