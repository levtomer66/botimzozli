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
    this.$axios.post(`https://${process.env.API_KEY}:${process.env.API_SECRET}@api.cloudinary.com/v1_1/${process.env.CLOUDNAME}/resources/search`, {"expression": "folder=bots/botimzozli"} ,{ headers: {'Access-Control-Allow-Origin' : '*'}})
      .then(response => {
        this.items = response.data.resources.map(function(a) { return { 'src': a.url, 'thumbnail': a.url, 'caption': a.filename } })
        console.log(this.items)
      }).catch(err => console.log(err))
  }

  }
</script>
