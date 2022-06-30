import apiClient from "../ApiClient";

const urlList = {
  rootUrl: "/api/v1/"
};

export default {
  getNewsList(page, perPage) {
    let url = urlList.rootUrl + `news/?page_size=${perPage}&page=${page}`;
    return apiClient.get(url);
  }
};
