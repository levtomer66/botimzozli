<template>
  <div  class="content countdown-timer">
    <lingallery :iid.sync="currentId" :width="width" :height="height" :items="items"/>
  </div>
</template>

<style scoped>
.content {
  max-width: 500px;
  margin: auto;
  text-align: right;
}
</style>

<script>
  import Lingallery from 'lingallery';
  export default {
    data() {
    return {
        currentId: null,
        width: 900,
        height: 800,
        items: [ {src: '', caption: ''}]
    }
  },
  created() {
    this.$axios.get('/api')
      .then(response => {
        this.items = response.data.resources.map(function(a) { return { 'src': a.url, 'thumbnail': a.url, 'caption': a.filename } })
      }).catch(err => console.log(err))
  }

  }
</script>
