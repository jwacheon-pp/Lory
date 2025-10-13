from django.test import TestCase
from django.utils import timezone
from posts.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'creator_id': 1,
        }

    def test_create_post(self):
        # Post 모델 인스턴스를 생성하고 필드 값들이 올바르게 설정되는지 확인하는 테스트
        post = Post.objects.create(**self.post_data)
        self.assertEqual(post.title, self.post_data['title'])
        self.assertEqual(post.content, self.post_data['content'])
        self.assertEqual(post.creator_id, self.post_data['creator_id'])
        self.assertTrue(post.is_active)
        self.assertIsInstance(post.created_at, timezone.now().__class__)

    def test_post_str_method(self):
        # Post 모델의 __str__ 메소드가 올바른 문자열을 반환하는지 확인하는 테스트
        post = Post.objects.create(**self.post_data)
        self.assertEqual(str(post), f"{post.title} by {post.creator_id}")

    def test_post_manager_create_post(self):
        # PostManager의 create_post 메소드를 사용하여 Post를 생성하고 반환되는 객체가 올바른지 확인하는 테스트
        post = Post.objects.create_post(**self.post_data)
        self.assertEqual(post.title, self.post_data['title'])
        self.assertEqual(post.content, self.post_data['content'])
        self.assertEqual(post.creator_id, self.post_data['creator_id'])