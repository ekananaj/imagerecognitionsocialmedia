<template>
  <div>
    <input type="file" @change="handleFileUpload" />
    <button @click="uploadImage">Upload Image</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageFile: null
    };
  },
  methods: {
    handleFileUpload(event) {
      this.imageFile = event.target.files[0];
    },
    uploadImage() {
      const formData = new FormData();
      formData.append('file', this.imageFile);

      fetch('http://localhost:8000/api/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
    }
  }
};
</script>
