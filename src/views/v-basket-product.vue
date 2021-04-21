<template>
  <div class="basket-products v-catalog items-center" v-if="BASKET.length">
    <div class="flex-wrap flex justify-around">
      <v-basket-item
        v-for="(product, index) in BASKET"
        :key="product.id"
        :productData="product"
        @removeProductToBasket="removeToBasket(index)"
      >
      </v-basket-item>
    </div>
    <v-basket-payment></v-basket-payment>
  </div>
  
  <div class="flex-wrap flex justify-center" v-else>
    <h1>Пожалуйста, добавьте что-нибудь в корзину!</h1>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import vBasketItem from "../components/basket/v-basket-item";
import vBasketPayment from "../components/basket/v-basket-payment";

export default {
  name: "basket-product",
  components: {
    vBasketItem,
    vBasketPayment,
  },

  data() {
    return {};
  },
  computed: {
    ...mapGetters(["BASKET"]),
  },

  methods: {
    ...mapActions(["REMOVE_PRODUCT_IN_BASKET"]),
    removeToBasket(index) {
      this.REMOVE_PRODUCT_IN_BASKET(index);
    },
  },
};
</script>

<style></style>
