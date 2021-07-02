import Vue from 'vue'
import App from './App.vue'
import TextHighlight from 'vue-text-highlight'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue' 

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.component('text-highlight', TextHighlight)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
