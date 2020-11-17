<template>
  <v-container class="v-container">
    <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="370"
    v-for="projeto of projetos" :key="projeto.id"
  >
    <v-img
      height="250"
      v-bind:src="projeto.caminho_imagem"
    ></v-img>

    <v-card-title>{{projeto.nome}}</v-card-title>

    <v-card-text>
      <div class="my-4 subtitle-1">
        Desenvolvido por {{projeto.nome_criador}}
      </div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Descrição</v-card-title>

    <v-card-text>
      <p>
       {{projeto.descricao}}
      </p>
    </v-card-text>

    <v-card-actions>
      
      <a v-bind:href="projeto.url_repositorio" class="link" target="_blank">
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Repositório
      </v-btn>
      </a>
    </v-card-actions>
  </v-card>
  </v-container>
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

   .v-container {
     display: grid;
     grid-template-columns: repeat(2, 1fr);
     grid-auto-rows: minmax(50px, auto);
   }
</style>