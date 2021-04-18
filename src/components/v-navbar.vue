<template>
  <div class="v-navbar">
    <div
      class="w-screen flex flex-row items-center p-1 justify-between bg-white shadow-xs"
    >
      <router-link to="/" class="ml-8 text-lg text-gray-700 hidden md:flex"
        >Shop</router-link
      >
      <span
        class="w-screen md:w-1/3 h-10 bg-gray-200 cursor-pointer border border-gray-300 text-sm rounded-full flex"
      >
        <input
          type="search"
          name="serch"
          placeholder="Search"
          class="flex-grow px-4 rounded-l-full rounded-r-full text-sm focus:outline-none"
        />
        <i class="fas fa-search m-3 mr-5 text-lg text-gray-700 w-4 h-4"> </i>
      </span>
      <div class="flex flex-row-reverse mr-4 ml-4 md:hidden">
        <i class="fas fa-bars"></i>
      </div>
      <div class="flex flex-row-reverse mr-8 hidden md:flex">
        <router-link
          to="/basket"
          class="text-gray-700 text-center bg-gray-400 px-4 py-2 m-2"
          v-if="isLoggedIn"
          >Basket</router-link
        >
        <span v-if="isLoggedIn" class="text-gray-700 text-center bg-gray-400 px-4 py-2 m-2"> | <a @click="logout">Logout</a></span>
        <router-link
          to="/login"
          class="text-gray-700 text-center bg-gray-400 px-4 py-2 m-2"
          v-if="!isLoggedIn"
          >Login</router-link
        >
        <router-link
          to="/registration"
          v-if="!isLoggedIn"
          class="text-gray-700 text-center bg-gray-400 px-4 py-2 m-2"
        >
          Registration
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "v-navbar",
  data() {
    return {};
  },

  computed: {
    ...mapGetters(["isLoggedIn"]),
  },

  methods: {
    ...mapActions(["logout"]),

logout() {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      }
    }
};
</script>

<style></style>
