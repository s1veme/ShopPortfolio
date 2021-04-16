<template>
  <div class="basket-products v-catalog flex-wrap flex justify-around" v-if="BASKET.length">
    <v-basket-item
      v-for="(product, index) in BASKET"
      :key="product.id"
      :productData="product"
      @removeProductToBasket="removeToBasket(index)"
    >
    </v-basket-item>
  </div>
    <div class="flex-wrap flex justify-center" v-else>
      <h1>Пожалуйста, добавьте что-нибудь в корзину!</h1>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import vBasketItem from "../components/v-basket-item";

export default {
  name: "basket-product",
  components: {
    vBasketItem,
  },

  data() {
    return {};
  },
  computed: {
    ...mapGetters(["BASKET"]),
  },

  methods: {
    ...mapActions([
      'REMOVE_PRODUCT_IN_BASKET'
    ]),
    removeToBasket(index) {
      console.log(index)
      this.REMOVE_PRODUCT_IN_BASKET(index)
    }
  }
};
</script>

<style></style>
