import Vue from "vue";
import VueMeta from "vue-meta";
import PortalVue from "portal-vue";
import { InertiaApp } from "@inertiajs/inertia-vue";

Vue.config.productionTip = false;
Vue.mixin({
  methods: {
    route(routeName, param = null) {
      let routeString = this.$page.routes[routeName];
      if (param) {
        const startIndex = routeString.indexOf("@");
        const endIndex = routeString.indexOf("/", startIndex);
        if (endIndex !== -1) {
          routeString =
            routeString.substr(0, startIndex) +
            param +
            routeString.substr(endIndex);
        } else {
          routeString = routeString.substr(0, startIndex) + param + "/";
        }
      }
      return routeString;
    },
  },
});
Vue.use(InertiaApp);
Vue.use(PortalVue);
Vue.use(VueMeta);

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
