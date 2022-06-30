import ServiceAccount from "../../service/account/ServiceAccount";

export const namespaced = true;

export const state = {
  tokenData: null
};

export const mutations = {
  SET_TOKEN_DATA(state, tokenData) {
    localStorage.setItem("tokenData", JSON.stringify(tokenData));
    state.tokenData = tokenData;
  },

  LOGOUT() {
    localStorage.removeItem("tokenData");
    location.reload();
  }
};

export const actions = {
  loginUser({ commit }, userCredentials) {
    return ServiceAccount.loginUser(userCredentials)
      .then(response => {
        commit("SET_TOKEN_DATA", response.data);
        return response;
      })
      .catch(err => {
        if (err.response.status == 400) {
          let message = "";

          if (err.response.data.message) {
            message = err.response.data.message;
          } else if (err.response.data.username) {
            message = "Username: " + err.response.data.username;
          } else if (err.response.data.password) {
            message = "Password: " + err.response.data.password[0];
          }

          if (message) {
            Vue.toasted.show(message, {
              className: "bg-danger"
            });
          }
        } else {
          Vue.toasted.show("Oops! Something went wrong", {
            className: "bg-danger"
          });
        }

        return err.response;
      });
  },

  registerUser({ commit }, userData) {
    return ServiceAccount.registerUser(userData)
      .then(response => {
        commit("SET_TOKEN_DATA", response.data);
        Vue.toasted.show("Successfully registered", {
          className: "bg-success"
        });
        return response;
      })
      .catch(err => {
        if (err.response.status == 400) {
          let message = "";

          if (err.response.data.message) {
            message = err.response.data.message;
          } else if (err.response.data.username) {
            message = "Username: " + err.response.data.username;
          } else if (err.response.data.email) {
            message = "Email: " + err.response.data.email;
          } else if (err.response.data.password) {
            message = "Password: " + err.response.data.password[0];
          }

          if (message) {
            Vue.toasted.show(message, {
              className: "bg-danger"
            });
          }
        } else {
          Vue.toasted.show("Oops! Something went wrong", {
            className: "bg-danger"
          });
        }

        return err.response;
      });
  },

  refreshToken({ commit }) {
    return ServiceAccount.refreshToken()
      .then(response => {
        commit("SET_TOKEN_DATA", response.data);
        return response;
      })
      .catch(err => {
        console.log(err);
        return err.response;
      });
  },

  logoutUser({ commit }) {
    commit("LOGOUT");
  }
};

export const getters = {
  loggedIn(state) {
    return !!state.tokenData;
  }
};
