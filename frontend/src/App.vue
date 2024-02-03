<template>
  <NavigationBar> </NavigationBar>
  <router-view></router-view>
</template>

<script>
import NavigationBar from "./components/NavigationBar.vue";

export default {
  name: "App",
  components: {
    NavigationBar,
  },
};
</script>

<style>
body {
  background-color: #f8f9fa;
}
</style>
