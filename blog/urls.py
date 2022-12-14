from django.urls import path
from blog import views
from blog.views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/create", PostCreateView.as_view(), name="post-create"),
    path('user/<username>/', UserPostListView.as_view(), name='user-posts'),
    path("about/", views.about, name="blog-about"),
]
