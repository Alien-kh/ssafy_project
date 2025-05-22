<!-- views/SignUpView.vue -->

<template>
  <div>
    <form @submit.prevent="onSignUp">
      <label for="username">username: </label>
      <input type="text" id="username" v-model="username">

      <label for="password1">password1: </label>
      <input type="password" id="password1" v-model="password1">

      <label for="password2">password2: </label>
      <input type="password" id="password2" v-model="password2">
      <label for="age">age: </label>
      <input type="number" id="age" v-model="age">

      <input type="submit" value="signup">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'
  
  const accountStore = useAccountStore()

  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')
  const age = ref(null)
  const onSignUp = function () {
    const userInfo = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      age: age.value
    }
    accountStore.signUp(userInfo)  
  }
  
</script>

<style>

</style>
