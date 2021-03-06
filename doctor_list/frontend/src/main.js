import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import BootstrapVue from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(BootstrapVue)
Vue.http.options.root = 'http://localhost:8000'
new Vue({
  render: h => h(App)
}).$mount('#app')
