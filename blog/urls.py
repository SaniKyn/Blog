from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    AddCommentView,
    HomePageView,
    PostsByAuthorView
)

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('', HomePageView.as_view(), name='home'),
    path('post/author/<int:author_id>', PostsByAuthorView.as_view(), name='posts_by_author'),
]
