from rest_framework import viewsets, status
from rest_framework.response import Response
from posts.models import Post

# Create your views here.
class PostViewSet(): 
    queryset = Post.objects.all()