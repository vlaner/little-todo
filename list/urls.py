from django.urls import path
from .views import HomeView, RegisterView, CreatePostView, UpdatePostView, DeletePostView, CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('create/', CreatePostView.as_view(), name='createPost'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='updatePost'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='deletePost'),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
