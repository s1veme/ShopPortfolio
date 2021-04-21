<template>
  <div class="v-basket-payment flex-wrap flex justify-center m-10">
    <button
      @click="payment"
      class="py-2 px-4 bg-green-500 text-white font-semibold rounded-lg shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-400 focus:ring-opacity-75"
    >
      ОПЛАТИТЬ
    </button>
  </div>
</template>

<script>
export default {
  name: "v-basket-payment",

  data() {
    return {};
  },

  methods: {
    payment() {
      console.log("CLICK");
    },
  },
};
</script>
