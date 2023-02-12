from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'), # pk stands for primary key, int stands for integer
    path('post/', AddPostView.as_view(), name='post')
]