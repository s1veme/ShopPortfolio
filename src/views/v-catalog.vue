<template>
    <div class="v-catalog flex-wrap flex justify-around">
        <v-catalog-item
            v-for="product in PRODUCTS"
            :key="product.id"
            :productData="product"
            :isAuth="isLoggedIn"
            @addProductToBacket="addToBacket"
        >
        </v-catalog-item>
    </div>
</template>

<script>

import vCatalogItem from '../components/v-catalog-item'
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'v-catalog',
    components: {
        vCatalogItem
    },

    data() {
        return {
        }
    },

    computed: {
        ...mapGetters([
            'PRODUCTS',
            'isLoggedIn'
        ])
    },

    methods: {
        ...mapActions([
            'GET_PRODUCTS_FROM_API',
            'ADD_PRODUCT_IN_BASKET'
        ]),
        addToBacket(data) {
            const product = this.PRODUCTS.find(x => x.id === data)
            this.ADD_PRODUCT_IN_BASKET(product)
        }
    },
    mounted() {
        this.GET_PRODUCTS_FROM_API()
    }
}
</script>

<style>

</style>