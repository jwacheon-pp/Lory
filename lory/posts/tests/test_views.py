# posts/tests/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from posts.models import Post

class PostViewSetTest(APITestCase):

    def setUp(self):
        self.list_url = reverse('posts-list')

    def test_create_post(self):
        data = {
            "title": "테스트 포스트",
            "content": "내용입니다.",
            "creator_id": 1
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, "테스트 포스트")

    def test_list_posts(self):
        Post.objects.create(title="A", content="B", creator_id=1)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_post(self):
        post = Post.objects.create(title="A", content="B", creator_id=1)
        url = reverse('posts-detail', args=[post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "A")
