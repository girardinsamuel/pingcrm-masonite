import Vue from "vue";
import VueMeta from "vue-meta";
import PortalVue from "portal-vue";
import { InertiaApp } from "@inertiajs/inertia-vue";
import { InertiaProgress } from "@inertiajs/progress/src";
import route from "ziggy-js";
import { Ziggy } from "./routes";

Vue.config.productionTip = false;

Vue.mixin({
  methods: {
    route: (name, params, absolute) => route(name, params, absolute, Ziggy),
  },
});

Vue.use(InertiaApp);
Vue.use(PortalVue);
Vue.use(VueMeta);

InertiaProgress.init();

let app = document.getElementById("app");

new Vue({
  metaInfo: {
    titleTemplate: (title) => (title ? `${title} - Ping CRM` : "Ping CRM"),
  },
  render: (h) =>
    h(InertiaApp, {
      props: {
        initialPage: JSON.parse(app.dataset.page),
        resolveComponent: (name) => require(`./Pages/${name}`).default,
        //   resolveComponent: (name) =>
        //     import(`@/Pages/${name}`).then((module) => module.default),
      },
    }),
}).$mount(app);
