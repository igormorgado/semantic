<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <JobInput msg="This is job-input-script component"/>
  </div>
</template>

<script>
import JobInput from './components/job-input-script.vue'

export default {
  name: 'App',
  components: {
    JobInput
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
