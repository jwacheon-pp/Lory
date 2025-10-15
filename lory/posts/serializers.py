from rest_framework import serializers
from posts.models import Post

class GetPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post 
        fields = [
            'id',
            'title',
            'content',
            'creator_id',
            'created_at',
        ]
        extra_kwargs = {
            'url': {'view_name': 'posts-detail', 'lookup_field': 'pk'},
        }

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'creator_id',
        ]

class ModifyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]