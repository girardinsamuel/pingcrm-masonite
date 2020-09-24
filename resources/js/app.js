import Vue from "vue";
import VueMeta from "vue-meta";
import PortalVue from "portal-vue";
import { InertiaApp } from "@inertiajs/inertia-vue";

Vue.config.productionTip = false;
// Vue.mixin({
//   methods: {
//     // TODO: implements a package as Ziggy to use with Masonite maybe !!
//     route(routeName, param = null) {
//       let routeString = this.$page.routes[routeName];
//       if (param) {
//         if (typeof param == "object") {
//           const queryString = Object.keys(param)
//             .map((key) => {
//               return (
//                 encodeURIComponent(key) + "=" + encodeURIComponent(param[key])
//               );
//             })
//             .join("&");
//           routeString += "/?" + queryString;
//         } else {
//           const startIndex = routeString.indexOf("@");
//           const endIndex = routeString.indexOf("/", startIndex);
//           if (endIndex !== -1) {
//             routeString =
//               routeString.substr(0, startIndex) +
//               param +
//               routeString.substr(endIndex);
//           } else {
//             routeString = routeString.substr(0, startIndex) + param + "/";
//           }
//         }
//       }
//       return routeString;
//     },
//   },
// });
import route from "ziggy"
Vue.mixin({
    methods: {
        route: (name, params, absolute) => route(name, params, absolute, window.Ziggy),
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
