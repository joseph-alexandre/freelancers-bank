<template>
  <div id="teste">
    <p>{{ this.count }}</p>
    <button v-on:click="incrementValue">Button</button>
  </div>
</template>

<script>
var data = { count: 0 }
export default {
  name: 'Increment',
  data: () => {
      return data;
  },
  methods: {
      incrementValue :  () => {
          data.count += 1;
      }
  }
}
</script>
