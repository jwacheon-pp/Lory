<template>
  <div class="p-6 max-w-md mx-auto">
    <h1 class="text-2xl font-bold mb-4">로그인</h1>

    <input
      v-model="email"
      type="email"
      placeholder="Email"
      class="border p-2 mb-2 w-full"
    />
    <input
      v-model="password"
      type="password"
      placeholder="Password"
      class="border p-2 mb-4 w-full"
    />

    <button
      @click="login"
      :disabled="pending"
      class="bg-blue-600 text-white px-4 py-2 w-full"
    >
      {{ pending ? '로그인 중...' : '로그인' }}
    </button>

    <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useUserStore } from '~/stores/user'

const config = useRuntimeConfig()
const router = useRouter()
const userStore = useUserStore()

let email = ref('')
let password = ref('')
let pending = ref(false)
let error = ref<string | null>(null)

const login = async () => {
  pending.value = true
  error.value = null

  try {
    const res = await axios.post(`${config.public.apiBase}/login/`, {
      email: email.value,
      password: password.value
    })

    const token = res.data.access
    // Pinia store에 JWT와 user_id 저장
    userStore.setToken(token)

    // localStorage에 토큰 저장 (선택 사항)
    localStorage.setItem('access_token', token)

    // 로그인 성공 시 게시글 목록 페이지로 이동
    router.push('/posts')
  } catch (err: any) {
    // 오류 메시지 처리
    error.value = err.response?.data?.detail || '로그인 실패'
  } finally {
    pending.value = false
  }
}
</script>