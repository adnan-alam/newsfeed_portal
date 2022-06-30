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

      <b-form-group label="Email">
        <b-form-input
          v-model="form.email"
          type="email"
          placeholder="Enter email"
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

      <b-form-group label="Confirm Password">
        <b-form-input
          v-model="form.confirm_password"
          type="password"
          placeholder="Confirm password"
          required
        ></b-form-input>
      </b-form-group>

      <div class="my-4">
        <b-button type="submit" variant="primary">Register</b-button>
      </div>
    </b-form>

    <router-link to="/login">
      Already have an account? Login
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        email: "",
        password: "",
        confirm_password: ""
      }
    };
  },
  methods: {
    onSubmit() {
      this.$store.dispatch("account/registerUser", this.form).then(response => {
        if (response.status == 201) {
          this.$router.push({ name: "HomePage" }).catch(() => {});
        }
      });
    }
  }
};
</script>
