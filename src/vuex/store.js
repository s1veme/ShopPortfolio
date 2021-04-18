import axios from 'axios'
import { createStore } from 'vuex'

let store = createStore({
    state: {
        products: [],
        basket: [],
        isAuth: false,
        token: localStorage.getItem('token') || '',
        user: {}
    },
    mutations: {
        SET_PRODUCTS_TO_STATE: (state, products) => {
            state.products = products
        },
        ADD_PRODUCT_TO_STATE: (state, product) => {
            if (!(state.basket.some(e => e.id == product.id)))  {
                state.basket.push(product)
            } 
        },
        REMOVE_PRODUCT_TO_STATE: (state, index) => {
            state.basket.splice(index, 1)
        },
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token, user){
            state.status = 'success'
            state.token = token
            state.user = user
        },
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = ''
            state.token = ''
        },
    },
    actions: {
        GET_PRODUCTS_FROM_API({commit}) {
            return axios('http://127.0.0.1:8000/api/v1/shops/all/product', {
                method: "GET"
            })
            .then((products) => {
                commit('SET_PRODUCTS_TO_STATE', products.data.results)
                return products
            })
            .catch((error) => {
                console.log(error)
                return error
            })
        },
        ADD_PRODUCT_IN_BASKET({commit}, product) {
            return commit('ADD_PRODUCT_TO_STATE', product)
        },
        REMOVE_PRODUCT_IN_BASKET({commit}, index) {
            return commit('REMOVE_PRODUCT_TO_STATE', index)
        },

        login({commit}, user){
            return new Promise((resolve, reject) => {
              commit('auth_request')
              const username = user.username
              axios({url: 'http://localhost:8000/auth/jwt/create/', data: user, method: 'POST' })
              .then(resp => {
                const token = resp.data.access
                const user = username
                console.log(token)
                localStorage.setItem('token', token)
                axios.defaults.headers.common['Authorization'] = token
                commit('auth_success', token, user)
                resolve(resp)
              })
              .catch(err => {
                commit('auth_error')
                localStorage.removeItem('token')
                reject(err)
              })
            })
        },
    },
    getters: {
        PRODUCTS(state) {
            return state.products
        },
        BASKET(state) {
            return state.basket
        },
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    }
})

export default store;