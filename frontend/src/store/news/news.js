import ServiceNews from "../../service/news/ServiceNews";

export const namespaced = true;

export const state = {
  newsList: [],
  newsCount: null
};

export const mutations = {
  SET_NEWS_LIST(state, data) {
    state.newsList = data;
  },

  SET_NEWS_COUNT(state, count) {
    state.newsCount = count;
  }
};

export const actions = {
  getNewsList({ commit }, { page, perPage }) {
    return ServiceNews.getNewsList(page, perPage)
      .then(response => {
        commit("SET_NEWS_LIST", response.data.results);
        commit("SET_NEWS_COUNT", response.data.count);
        return response;
      })
      .catch(err => {
        console.log(err);
        return err.response;
      });
  },

  getNewsSourceListWithoutPagination({}) {
    return ServiceNews.getNewsSourceListWithoutPagination()
      .then(response => {
        return response;
      })
      .catch(err => {
        console.log(err);
        return err.response;
      });
  },

  getUserNewsSettings({}) {
    return ServiceNews.getUserNewsSettings()
      .then(response => {
        return response;
      })
      .catch(err => {
        console.log(err);
        return err.response;
      });
  },

  updateNewsSettings({}, { settingsId, data }) {
    return ServiceNews.updateNewsSettings(settingsId, data)
      .then(response => {
        Vue.toasted.show("Settings updated successfully", {
          className: "bg-success"
        });
        return response;
      })
      .catch(err => {
        if (err.response.status == 400) {
          let message = "";

          if (err.response.data.message) {
            message = err.response.data.message;
          } else if (err.response.data.country) {
            message = "Country of news: " + err.response.data.country;
          } else if (err.response.data.source) {
            message = "Source of news: " + err.response.data.source;
          } else if (err.response.data.keywords) {
            message = "Keywords: " + err.response.data.keywords;
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
  }
};
