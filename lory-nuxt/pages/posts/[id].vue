<template>
  <div class="p-6">
    <div v-if="pending">로딩 중...</div>
    <div v-else-if="error">오류 발생: {{ error.message }}</div>
    <div v-else-if="post">
      <h1 class="text-3xl font-bold mb-4">{{ post.title }}</h1>
      <p class="text-gray-600 mb-2">작성자 ID: {{ post.creator_id }}</p>
      <p class="text-gray-500 mb-4">작성일: {{ new Date(post.created_at).toLocaleDateString() }}</p>
      <div class="text-gray-800">{{ post.content }}</div>
      <NuxtLink to="/posts" class="mt-4 inline-block text-blue-600 hover:underline">← 목록으로 돌아가기</NuxtLink>
    </div>
    <div v-else>게시글을 찾을 수 없습니다.</div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const route = useRoute()

const { id } = route.params

// 백엔드 API에서 데이터 가져오기
const {
  data: post,
  pending,
  error,
} = await useFetch(`${config.public.apiBase}/posts/${id}`)
</script>