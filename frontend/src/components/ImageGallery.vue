<template>
  <div>
    <h2>Uploaded Images</h2>
    <ul>
      <li v-for="(image, index) in images" :key="index">
        <img :src="image.url" alt="Uploaded image" width="200" />
        <p>{{ image.filterResult }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [] // replace with fetched image data
    };
  },
  created() {
    // Fetch images from the backend
    fetch('http://localhost:8000/api/images')
      .then(response => response.json())
      .then(data => this.images = data)
      .catch(error => console.error('Error:', error));
  }
};
</script>
