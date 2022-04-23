<template>
  <div class="app">
    <div class="header">
      Sentiments Analysis
    </div>
    <div class="search">
      <div style="margin-right: 20px">
        <div style="font-size: 18px;font-weight: bold;margin-bottom: 10px">
          Date
        </div>
        <div style="padding-left: 20px">
          <el-date-picker
            style="height: 25px;"
            v-model="date"
            type="daterange"
            range-separator="To"
            start-placeholder="Start date"
            end-placeholder="End date"
          />
        </div>
      </div>
      <div>
        <div style="font-size: 18px;font-weight: bold;margin-bottom: 10px ">
          Sentiments
        </div>
        <div style="display: flex;flex-wrap: wrap">
          <el-input clearable v-model="value" placeholder="请输入" style="width: 160px;height: 30px;margin-right: 20px"/>
          <div
            class="content"
            v-for="content in contents"
            :key="content">
            {{ content }}
          </div>
        </div>
      </div>
    </div>
    <div class="side-main">
      <div class="side">
        <div
          :class="{
            'active-side-item': active === menu.index,
            'inactive-side-item':active !== menu.index
          }"
          class="side-item"
          @click="go(menu)"
          :key="menu.route"
          v-for="menu in menus">
          {{ menu.name }}
        </div>
      </div>
      <div class="main">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {reactive, toRefs} from "vue";
import router from "@/router";

const state = reactive({
  active: 0,
  menus: [
    {
      name: 'word cloud',
      route: 'one',
      index: 0
    },
    {
      name: 'algorithm analysis',
      route: 'two',
      index: 1
    },
    {
      name: 'model analysis',
      route: 'three',
      index: 2
    }
  ],
  date: '',
  contents: [
    '（Blank）',
    'anticipation',
    'fear',
    'negative',
    'sadness',
    'trust',
    'anger',
    'disgust',
    'joy',
    'positive',
    'surprise'
  ],
  value: ''
})

const go = (menu: any) => {
  router.push({name: menu.route}).then(() => state.active = menu.index)
}

const {active, menus, date, contents, value} = toRefs(state)

</script>

<style>

.content {
  margin-right: 20px;
  width: 160px;
  height: 30px;
  background-color: #F2F0FD;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  color: #8D8C90;
  margin-bottom: 10px;
  border-radius: 5px;
}

.search {
  height: 80px;
  margin-top: 60px;
  box-sizing: border-box;
  padding-top: 15px;
  display: flex;
}

.active-side-item {
  color: #ffffff;
  background-color: #FA3F3A;
}

.inactive-side-item {
  background-color: #F2F0FD;
}

.side-item {
  height: 56px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  cursor: pointer;
  border-radius: 10px;
}

.side {
  width: 180px;
  height: 100%;
  position: fixed;
}

.main {
  flex: 1;
  box-sizing: border-box;
  padding: 0 20px;
  margin-left: 180px;
  height: 100%;
}

.side-main {
  display: flex;
  width: 100%;
  margin-top: 20px;
  flex: 1;
  padding: 20px 0;
  box-sizing: border-box;
}

.header {
  z-index: 9999;
  height: 60px;
  width: 100%;
  background-color: #FA3F3A;
  color: #ffffff;
  font-size: 18px;
  display: flex;
  align-items: center;
  padding-left: 100px;
  position: fixed;
}

.app {
  display: flex;
  flex-direction: column;
  height: 100%;
}

body, html {
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  color: #303133;
  background: #FEFEFE;
}
</style>
