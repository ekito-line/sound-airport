from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('post/', views.post, name='post'),
    path('main/', views.main, name='main'),
    path('<int:user_id>/follow/', views.follow, name='follow'),
    path('<int:post_id>/like/', views.like, name='like'),
    path('mypage/', views.mypage, name='mypage'),
]
