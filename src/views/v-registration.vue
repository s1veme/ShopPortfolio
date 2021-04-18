<template>
  <div class="v-registration">
    <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md">
      <div class="bg-white shadow w-full rounded-lg divide-y divide-gray-200">
        <form class="px-5 py-7" @submit.prevent="registration">
          <label class="font-semibold text-sm text-gray-600 pb-1 block"
            >login</label
          >
          <small
            v-if="errors.username"
            class="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1"
            >{{ errors.username }}</small
          >
          <input
            type="text"
            class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
            v-model.trim="username"
          />
          <label class="font-semibold text-sm text-gray-600 pb-1 block">
            email
          </label>
          <small
            v-if="errors.email"
            class="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1"
            >{{ errors.email }}</small
          >
          <input
            type="text"
            class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
            v-model.trim="email"
          />
          <label class="font-semibold text-sm text-gray-600 pb-1 block">
            password
          </label>
          <small
            v-if="errors.password"
            class="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1"
            >{{ errors.password }}</small
          >
          <input
            type="text"
            class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
            v-model.trim="password"
          />
          <button
            type="submit"
            class="transition duration-200 bg-blue-500 hover:bg-blue-600 focus:bg-blue-700 focus:shadow-sm focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50 text-white w-full py-2.5 rounded-lg text-sm shadow-sm hover:shadow-md font-semibold text-center inline-block"
          >
            <span class="inline-block mr-2">Login</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              class="w-4 h-4 inline-block"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M17 8l4 4m0 0l-4 4m4-4H3"
              />
            </svg>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-registration",

  data() {
    return {
      username: "",
      email: "",
      password: "",
      errors: {
        username: null,
        email: null,
        password: null,
      },
    };
  },

  methods: {
    formIsValid() {
      let isValid = true;

      if (this.username.length === 0) {
        this.errors.username = "Имя не может быть пустым";
        isValid = false;
      } else {
        this.errors.username = null;
      }

      if (this.password.length === 0) {
        this.errors.password = "Пароль не может быть пустым";
        isValid = false;
      } else {
        this.errors.password = null;
      }

      if (this.email.length === 0) {
        this.errors.password = "Почта не может быть пустой";
        isValid = false;
      } else {
        this.errors.email = null;
      }

      return isValid;
    },

    registration() {
        let data = {
          username: this.username,
          email: this.email,
          password: this.password,
        }
        this.$store.dispatch('register', data)
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
    }
  },
};
</script>

<style></style>
