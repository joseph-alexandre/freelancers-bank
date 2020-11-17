import Projects from "./components/pages/listagem/Projects.vue";
import Home from "./components/pages/home/Home.vue";
import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/projetos",
    name: "projetos",
    component: Projects,
  },
  {
    path: "/",
    name: "home",
    component: Home,
  },
];
const router = new VueRouter({ mode: "history", base: __dirname, routes });

export default router;
