<!-- App.vue -->

<template>
  <header>
    <nav>
      <RouterLink :to="{ name:'ArticleView' }">Articles</RouterLink> | 
      <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> | 
      <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink>
      <form @submit.prevent="logOut">
        <input type="submit" value="LogOut">
      </form>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
  import { useAccountStore } from './stores/accounts';

  const accountStore = useAccountStore();

  const logOut = function () {
    accountStore.logOut()
  }
</script>

<style scoped>
</style>
