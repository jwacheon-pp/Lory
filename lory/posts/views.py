from rest_framework import viewsets
from posts.models import Post
from posts.serializers import CreatePostSerializer, ModifyPostSerializer, GetPostSerializer
from rest_framework import permissions
from rest_framework.permissions import AllowAny

# Create your views here.
class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreatePostSerializer
        elif self.action in ['update', 'partial_update']:
            return ModifyPostSerializer
        return GetPostSerializer

    def get_permissions(self):
        if self.action != 'create':
            return [permissions.AllowAny()]  # 👈 회원가입만 예외
        return [permissions.IsAuthenticated()]