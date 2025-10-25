<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">📜 게시글 목록</h1>

    <div v-if="pending">로딩 중...</div>
    <div v-else-if="error">오류 발생: {{ error.message }}</div>
    <div v-else>
      <div
        v-for="post in posts"
        :key="post.id"
        class="border rounded p-4 mb-3 shadow-sm"
      >
        <NuxtLink :to="`/posts/${post.id}`" class="font-semibold text-lg text-blue-600 hover:underline">{{ post.title }}</NuxtLink>
        <p class="text-gray-700">{{ post.content }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()

// 백엔드 API에서 데이터 가져오기
const {
  data: posts,
  pending,
  error,
} = await useFetch(`${config.public.apiBase}/posts/`)
</script>
