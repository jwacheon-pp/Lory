from django.test import TestCase
from posts.models import Post

class PostModelTest(TestCase):

    def test_create_post(self):
        """Post 모델이 정상적으로 생성되는지 테스트"""
        post = Post.objects.create(
            title="테스트 제목",
            content="테스트 내용",
            creator_id=1
        )
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(str(post), "테스트 제목 by 1")
        self.assertTrue(post.is_active)
        self.assertIsNotNone(post.created_at)

    def test_ordering(self):
        """Post의 ordering 설정이 -created_at인지 확인"""
        post1 = Post.objects.create(title="첫 번째", content="A", creator_id=1)
        post2 = Post.objects.create(title="두 번째", content="B", creator_id=1)
        posts = list(Post.objects.all())
        
        self.assertEqual(posts[0], post2)


