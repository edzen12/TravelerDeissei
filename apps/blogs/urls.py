from django.urls import path
from .views import BlogDetailView, BlogListView, AddReview


urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='list_blog'),
    path('blogs/<str:slug>/', BlogDetailView.as_view(), name="blog_detail"),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]
