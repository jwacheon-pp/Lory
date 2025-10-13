from django.test import TestCase
from posts.serializers import CreatePostSerializer, ModifyPostSerializer

class PostSerializerTest(TestCase):

    def test_create_post_serializer_valid(self):
        data = {
            "title": "새 글",
            "content": "내용",
            "creator_id": 1
        }
        serializer = CreatePostSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "새 글")

    def test_create_post_serializer_invalid(self):
        """title이 누락된 경우 검증 실패해야 함"""
        data = {"content": "내용만 있음", "creator_id": 1}
        serializer = CreatePostSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_modify_post_serializer_fields(self):
        """ModifyPostSerializer가 올바른 필드만 포함하는지 확인"""
        data = {"title": "수정된 제목", "content": "수정된 내용"}
        serializer = ModifyPostSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(set(serializer.fields.keys()), {"title", "content"})
