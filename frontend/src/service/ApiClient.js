import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const apiClient = axios.create({
  baseURL: process.env.BASE_URL,
});

apiClient.interceptors.request.use(function(config) {
  // Do something before request is sent
  const tokenData = JSON.parse(localStorage.getItem("tokenData"));
  if (tokenData) {
    config.headers["Authorization"] = "Bearer " + tokenData.access;
  }
  return config;
});

export default apiClient;
