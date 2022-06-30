import Vue from "vue";
import VueRouter from "vue-router";
import LoginPage from "../pages/LoginPage.vue";
import RegisterPage from "../pages/RegisterPage.vue";
import HomePage from "../pages/HomePage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
    meta: { title: "Newsfeed Portal" }
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
    meta: { title: "Login | Newsfeed Portal" }
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
    meta: { title: "Register | Newsfeed Portal" }
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem("tokenData");

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    next("/");
  }
  next();
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
