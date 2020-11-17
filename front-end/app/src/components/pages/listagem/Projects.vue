<template>
  <v-main>
    teste
  </v-main>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Projects',
  data: () => {
      return {
        projetos: null
      }
  },
  mounted() {
      axios.get("http://localhost:5000/listar_projetos").then(response => (this.projetos = response.data))
  }
}
</script>

<style>
  .home-text {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
   }  
</style>