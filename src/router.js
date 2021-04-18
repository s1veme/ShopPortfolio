import { createRouter, createWebHistory } from 'vue-router'
import store from './vuex/store'


const routes = [
    {
        path: '/',
        component: () => import('./views/v-catalog'),
    },
    {
        path: '/basket',
        component: () => import('./views/basket-product'),
        name: 'basket',
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/login',
        component: () => import('./views/v-login'),
        name: 'login'
    },
    {
        path: '/registration',
        component: () => import('./views/v-registration'),
        name: 'registration'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.getters.isLoggedIn) {
            next()
            return
        }
        next('/login')
    } else {
        next()
    }
})

export default router
