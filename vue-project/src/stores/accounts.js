// store/accounts.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')
  const router = useRouter()

  const signUp = function ({username, password1, password2, age}) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/signup/`,
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        username,
        password1,
        password2,
        age: Number(age)
      }
    })
    .then(res => {
        console.log('회원가입 성공:', res)
        const password = password1
        logIn({username, password})
    })
    .catch(err => {
        console.log('Error details:', err.response?.data)
        console.log('Status code:', err.response?.status)
    })
  }

  const logIn = function({username, password}) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        // console.log(res)
        token.value = res.data.key
        router.push({ name: 'ArticleView' })
      })
      .catch(err => console.log(err))
  }

  const logOut = function() {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/logout/`,
    })
    .then((res) => {
      token.value = null
      router.push({ name: 'LogInView'})
    })
    .catch((err) => console.log(err))
  }

  return { 
    token,
    signUp, logIn, logOut
  }
}, { persist: true })
