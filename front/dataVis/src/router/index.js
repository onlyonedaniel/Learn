import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const chart = () => import("../views/chart/chart")

const register = () => import("../views/user/register")

const login = () => import("../views/user/login")

const user = () => import("../views/user/user")
const router = new Router({
    routes: [
        {
            path: '/',
            redirect: 'user'
        },
        {
            path: '/chart',
            component: chart
        },
        {
            path: '/user',
            component: user,
            children: [
                {
                    path: 'register',
                    component: register
                },
                {
                    path: 'login',
                    component: login
                },
            ]
        }
    ]
})

export default router