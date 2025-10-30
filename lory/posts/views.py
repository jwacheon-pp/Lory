from rest_framework import viewsets
from posts.models import Post
from posts.serializers import CreatePostSerializer, ModifyPostSerializer, GetPostSerializer
from posts.permissions import IsOwnerOrReadOnly
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
        if self.action in ['retrieve', 'list']:
            return [permissions.AllowAny()]
        # create는 로그인 필요, 수정/삭제는 작성자만 가능
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.IsAuthenticated()]