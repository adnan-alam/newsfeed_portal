import apiClient from "../ApiClient";

const urlList = {
  rootUrl: "/api/v1/"
};

export default {
  getNewsList(page, perPage) {
    let url = urlList.rootUrl + `news/?page_size=${perPage}&page=${page}`;
    return apiClient.get(url);
  },

  getNewsSourceListWithoutPagination() {
    let url = urlList.rootUrl + `news-sources/`;
    return apiClient.get(url);
  },

  getUserNewsSettings() {
    let url = urlList.rootUrl + `news-settings/`;
    return apiClient.get(url);
  },

  updateNewsSettings(settingsId, data) {
    let url = urlList.rootUrl + `news-settings/${settingsId}/`;
    return apiClient.patch(url, data);
  }
};
