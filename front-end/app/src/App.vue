<template>
<v-app>
  <div id="app">
    <Navegacao />
    <v-main>
      <router-view></router-view>
    </v-main>
  </div>
</v-app>
</template>
<script>

import Navegacao from './components/pages/navegacao/Navegacao.vue'
export default {
  name: 'App',
  components: {
    Navegacao
  }
}
</script>

<style>
    .link {
      text-decoration: none;
    }
</style>