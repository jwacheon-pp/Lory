from rest_framework import viewsets
from posts.models import Post
from posts.serializers import CreatePostSerializer, ModifyPostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreatePostSerializer
        elif self.action in ['update', 'partial_update']:
            return ModifyPostSerializer
        return CreatePostSerializer