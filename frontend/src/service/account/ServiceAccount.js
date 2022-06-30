import apiClient from "../ApiClient";

const urlList = {
  urlAccount: "/api/v1/",
  urlToken: "/api/v1/token/",
  urlTokenRefresh: "/api/v1/token/refresh/",
};

export default {
  loginUser(userCredentials) {
    return apiClient.post(urlList.urlToken, userCredentials);
  },

  registerUser(userData) {
    let url = `${urlList.urlAccount}users/`;
    return apiClient.post(url, userData);
  },

  refreshToken() {
    let url = urlList.urlTokenRefresh;
    const tokenData = JSON.parse(localStorage.getItem("tokenData"));
    return apiClient.post(url, tokenData.refresh);
  },
};
