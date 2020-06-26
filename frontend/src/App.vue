<template>
    <div id="app">
        <NavbarComponent />
        <router-view />
    </div>
</template>

<script>
import NavbarComponent from "./components/Navbar"
export default {
  name: "App",
  components: {
    NavbarComponent
  }
};
</script>
<style>

* {
            font-family: 'Playfair Display', serif;
        }

</style>
