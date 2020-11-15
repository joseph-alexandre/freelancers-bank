<template>
<div>
  <v-card
    :loading="loading"
    class="d-flex flex-row mb-6"
    max-width="300"
    v-for="projeto of projetos" :key="projeto.id"
  >
    <v-img
      height="250"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>Cafe Badilico</v-card-title>

    <v-card-text>
        <v-card-subtitle>
          Criador: {{projeto.nome_criador}}
        </v-card-subtitle>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Descrição</v-card-title>

    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      />
       <p>{{ projeto.descricao }}</p>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Reserve
      </v-btn>
    </v-card-actions>
  </v-card>
  </div>
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
  v-card {
    background-color: black;
  }
</style>