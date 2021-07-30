<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="test_connection" class="btn btn-primary">Test Koneksi</button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios';

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;

  mounted() {
    this.test_connection();
  }

  test_connection(): void {
    const base_url = 'localhost:80';
    const endpoint = '/api/hello';

    axios.get(`http://${base_url}${endpoint}`)
    .then((res) => {
      alert(res);
    }).catch((error) => {
      alert(error);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
