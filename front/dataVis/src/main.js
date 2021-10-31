// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueCookies from 'vue-cookies'
// Vue.use(VueCookies)
Vue.use(ElementUI)
Vue.use(VueAxios, axios);
Vue.prototype.$cookies = VueCookies

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})
router.beforeEach(
    (to, from, next) => {

        if (this.$cookies.isKey('username')) {
            this.$cookies.get('username')
            next(to)
        } else {
            this.$router.push('/user/login')
        }
    }
)