<template>
  <v-main>
    <p class="home-text">
      Bem-vindo ao aplicativo. Abra o menu de navegação e escolha alguma opção.
    </p>
  </v-main>
</template>

<script>

export default {
  name: 'Home',
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