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
  }
};
