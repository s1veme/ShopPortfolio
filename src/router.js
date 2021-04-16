import { createRouter, createWebHistory } from 'vue-router'

import vBasket from './views/basket-product'
import vCatalog from './views/v-catalog'
import vLogin from './views/v-login'


const routes = [
    {
        path: '/',
        component: vCatalog
    },
    {
        path: '/basket',
        component: vBasket,
        name: 'basket',
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/login',
        component: vLogin,
        name: 'login'
    }
]

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

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
