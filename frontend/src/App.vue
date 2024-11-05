<template>
  <div id="app">
    <h1>Image Recognition & Filtering App</h1>
    <ImageUpload />
    <ImageGallery />
  </div>
</template>

<script>
import ImageUpload from './components/ImageUpload.vue';
import ImageGallery from './components/ImageGallery.vue';

export default {
  components: {
    ImageUpload,
    ImageGallery
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
</style>
