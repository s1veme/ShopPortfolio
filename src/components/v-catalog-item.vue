<template>
  <div class="v-catalog-item">
    <div class="container mx-auto py-10 flex justify-center">
      <div
        class="bg-white w-80 shadow-lg cursor-pointer rounded transform hover:scale-105 duration-300 ease-in-out"
      >
        <div class="">
          <img src="https://picsum.photos/400/300" alt="" class="rounded-t" />
        </div>
        <div class="p-4">
          <h2 class="text-2xl uppercase">{{ productData.name }}</h2>
          <p class="font-light text-gray-500 text-lg my-2">${{ productData.price_now }};</p>
          <p>
            {{ productData.short_description }}
          </p>
          <a
            href="#"
            class="block bg-gray-300 py-2 px-2 text-gray-600 text-center rounded shadow-lg uppercase font-light mt-6 hover:bg-gray-400 hover:text-white duration-300 ease-in-out"
            @click="addProductToBacket"
            v-if="isAuth"
            >Add to cart</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-catalog-item",
  props: {
    productData: {
      type: Object,
      default() {
        return {};
      },
    },
    isAuth: {
      type: Boolean,
      default() {
        return false
      }
    }
  },

  data() {
    return {}
  },

  methods: {
    addProductToBacket() {
      this.$emit("addProductToBacket", this.productData.id);
    }
  },
};
</script>

<style></style>
