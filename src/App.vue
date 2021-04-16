<template>
  <header>
    <v-navbar></v-navbar>
  </header>
  <div class="container mx-auto">
    <router-view></router-view>
  </div>
</template>

<script>

import vNavbar from '@/components/v-navbar'

export default {
  name: 'App',

  components: {
    vNavbar
  },
  
  data() {
    return {
    }
  }
}
</script>

