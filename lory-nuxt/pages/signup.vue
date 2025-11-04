<template>
  <div class="p-6 max-w-md mx-auto">
    <h1 class="text-2xl font-bold mb-4">회원가입</h1>

    <input
      v-model="email"
      type="email"
      placeholder="Email"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="nickname"
      type="text"
      placeholder="Nickname"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="first_name"
      type="text"
      placeholder="First Name"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="last_name"
      type="text"
      placeholder="Last Name"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="bio"
      type="text"
      placeholder="Bio"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="phone_number"
      type="text"
      placeholder="Phone Number"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="password"
      type="password"
      placeholder="Password"
      class="border p-2 mb-4 w-full"
    />

    <button
      @click="signup"
      :disabled="pending"
      class="bg-blue-600 text-white px-4 py-2 w-full"
    >
      {{ pending ? '가입 중...' : '회원가입' }}
    </button>

    <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    <div v-if="success" class="text-green-600 mt-2">{{ success }}</div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const config = useRuntimeConfig()
const router = useRouter()

// 입력값
const email = ref('')
const nickname = ref('')
const first_name = ref('')
const last_name = ref('')
const bio = ref('')
const phone_number = ref('')
const password = ref('')

const pending = ref(false)
const error = ref<string | null>(null)
const success = ref<string | null>(null)

const signup = async () => {
  pending.value = true
  error.value = null
  success.value = null

  try {
    await axios.post(`${config.public.apiBase}/users/signup/`, {
      email: email.value,
      nickname: nickname.value,
      first_name: first_name.value,
      last_name: last_name.value,
      bio: bio.value,
      phone_number: phone_number.value,
      password: password.value,
    })

    success.value = '회원가입이 완료되었습니다. 로그인 화면으로 이동합니다.'
    setTimeout(() => router.push('/login'), 1500)
  } catch (err: any) {
    error.value =
      err.response?.data?.detail ||
      err.response?.data?.email?.[0] ||
      '회원가입 실패'
  } finally {
    pending.value = false
  }
}
</script>
