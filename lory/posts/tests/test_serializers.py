from django.test import TestCase
from posts.models import Post
from posts.serializers import CreatePostSerializer, ModifyPostSerializer, GetPostSerializer

class PostSerializerTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content.',
            creator_id=1,
        )
        self.post_data = {
            'title': 'New Post',
            'content': 'New content.',
            'creator_id': 2,
        }

    def test_create_post_serializer_valid(self):
        # CreatePostSerializer가 유효한 데이터를 올바르게 직렬화하고 저장하는지 확인하는 테스트
        serializer = CreatePostSerializer(data=self.post_data)
        self.assertTrue(serializer.is_valid())
        post = serializer.save()
        self.assertEqual(post.title, self.post_data['title'])
        self.assertEqual(post.creator_id, self.post_data['creator_id'])

    def test_create_post_serializer_invalid(self):
        # CreatePostSerializer가 유효하지 않은 데이터를 올바르게 거부하는지 확인하는 테스트
        invalid_data = {
            'title': '',  # Empty title
            'content': 'Content',
            'creator_id': 1,
        }
        serializer = CreatePostSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_modify_post_serializer_valid(self):
        # ModifyPostSerializer가 기존 Post 인스턴스를 유효한 데이터로 업데이트하는지 확인하는 테스트
        update_data = {
            'title': 'Updated Title',
            'content': 'Updated content.',
        }
        serializer = ModifyPostSerializer(self.post, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, update_data['title'])

    def test_get_post_serializer(self):
        # GetPostSerializer가 Post 인스턴스를 올바르게 직렬화하여 데이터를 반환하는지 확인하는 테스트
        serializer = GetPostSerializer(self.post)
        data = serializer.data
        self.assertEqual(data['title'], self.post.title)
        self.assertEqual(data['content'], self.post.content)
        self.assertEqual(data['creator_id'], self.post.creator_id)
        self.assertIn('id', data)