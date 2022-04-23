<template>
  <div class="images">
    <div class="image-items">
      <div class="image-item">
        <div class="title">
          title
        </div>
        <img :src="first" alt="" class="image">
      </div>
      <div class="image-item">
        <div class="title">
          title
        </div>
        <img :src="second" alt="" class="image">
      </div>
    </div>
    <div class="image-items">
      <div class="image-item">
        <div class="title">
          title
        </div>
        <img :src="third" alt="" class="image">
      </div>
      <div class="image-item">
        <div class="title">
          title
        </div>
        <img :src="four" alt="" class="image">
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "One"
})
</script>

<script lang="ts" setup>
const first = require('@/assets/1.png')
const second = require('@/assets/2.png')
const third = require('@/assets/3.png')
const four = require('@/assets/4.png')
</script>

<style scoped>
.images {
  height: 100%;
}

.image-items {
  height: 49%;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  margin-bottom: 5px;
}

.image-item {
  width: 49%;
  height: 100%;
  margin-right: 10px;
  border: 3px solid #FA3F3A;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  padding: 10px;
}

.image {
  flex: 1;
}

.title{
  height: 5%;
  color: #FA3F3A;
  background-color: #F2F0FD;
  margin-bottom: 5px;
  padding: 5px 20px;
  font-size: 16px;
  border-radius: 15px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
}
</style>


