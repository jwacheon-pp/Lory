from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from posts.models import Post

class PostViewSetTest(APITestCase):
    def setUp(self):
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'creator_id': 1,
        }
        self.post = Post.objects.create(**self.post_data)
        self.list_url = reverse('posts-list')
        self.detail_url = reverse('posts-detail', kwargs={'pk': self.post.pk})

    def test_list_posts(self):
        # Post 목록을 가져오는 API 엔드포인트가 정상적으로 작동하는지 확인하는 테스트
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_post(self):
        # 새로운 Post를 생성하는 API 엔드포인트가 정상적으로 작동하는지 확인하는 테스트
        new_post_data = {
            'title': 'New Post',
            'content': 'New content.',
            'creator_id': 2,
        }
        response = self.client.post(self.list_url, new_post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], new_post_data['title'])

    def test_retrieve_post(self):
        # 특정 Post를 조회하는 API 엔드포인트가 정상적으로 작동하는지 확인하는 테스트
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        # 기존 Post를 수정하는 API 엔드포인트가 정상적으로 작동하는지 확인하는 테스트
        update_data = {
            'title': 'Updated Title',
            'content': 'Updated content.',
        }
        response = self.client.put(self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, update_data['title'])

    def test_delete_post(self):
        # Post를 삭제하는 API 엔드포인트가 정상적으로 작동하는지 확인하는 테스트
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())