import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const chart = () => import("../views/chart/chart")


export default new Router({
  routes: [
    {
      path: '/',
      redirect: 'chart'
    },
    {
      path: '/chart',
      component: chart
    }
  ]
})
