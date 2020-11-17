<template>
  <v-container class="v-container-true" v-if="projetos.length > 0">
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

  <v-container class="v-container-false" v-else>
    Não há projetos cadastrados. Cadastre um para que seja listado aqui.
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
      axios.get("http://localhost:5000/listar_projetos").then(response => {
        console.log(response)
        this.projetos = response.data;
        })
      .catch((error) => {
        console.log(error)
      });
  }
}
</script>

<style>
   .v-container-true {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-auto-rows: minmax(80px, auto);
   }

   .v-container-false {
      position: fixed;
      top: 50%;
      left: 71%;
      transform: translate(-50%, -50%);
   }
</style>