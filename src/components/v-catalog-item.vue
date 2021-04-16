<template>
  <div class="v-catalog-item">
    <div class="py-6">
      <div class="flex max-w-md bg-white shadow-lg rounded-lg overflow-hidden">
        <div
          class="w-1/3 bg-cover"
          style="background-image: url('https://images.unsplash.com/photo-1494726161322-5360d4d0eeae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80')"
        ></div>
        <div class="w-2/3 p-4">
          <h1 class="text-gray-900 font-bold text-2xl">
            {{ productData.name }}
          </h1>
          <p class="mt-2 text-gray-600 text-sm">
            Lorem ipsum dolor sit amet consectetur adipisicing elit In odit
            exercitationem fuga id nam quia
          </p>
          <div class="flex item-center justify-between mt-3">
            <h1 class="text-gray-700 font-bold text-xl">
              ${{ productData.price_now }}
            </h1>
            <button
              class="px-3 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded"
              @click="addProductToBacket"
            >
              Add to Card
            </button>
          </div>
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
  },

  data() {
    return {}
  },

  methods: {
    addProductToBacket() {
      this.$emit("addProductToBacket", this.productData.id);
    },
  },
};
</script>

<style></style>
