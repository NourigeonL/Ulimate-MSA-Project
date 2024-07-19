from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
        
class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    queryset = Post.objects.all()