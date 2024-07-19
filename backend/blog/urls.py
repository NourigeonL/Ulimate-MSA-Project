from django.urls import path, include
from .views import PostCreate, PostList
urlpatterns = [
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/create/", PostCreate.as_view(), name="post-create"),
]