from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer