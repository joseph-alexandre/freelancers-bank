<template>
<v-app>
  <div id="app">
    <Navegacao />
    <router-view></router-view>
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