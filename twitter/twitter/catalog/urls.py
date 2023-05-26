from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('developer/', views.developer, name='developer'),
    path('login/', views.login, name='login'),
    #path('profile/', views.profile, name='profile'),
    path('profile/', views.PostView.as_view(), name='profile'),
    #path('profile/', views.full_slug, name='full_slug'),
    path('profile/home/', views.PostViewHome.as_view(), name='home'),
    #path('success/',views.success,name='success'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", views.registration, name="signup"),
    #path('profile/home/', views.home, name='home'),
    path('profile/photogallery/', views.photo, name='photo'),
    path('profile/messager/', views.messager, name='messager'),
    path('profile/edit/', views.edit_profile, name='edit'),
    path('profile/newtweet/', views.new_post, name='newtweet'),
    #path('profile/<int:pk>/', views.post_getail, name='comment'),
    path('profile/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    #path('profile/comment/<int:pk>', views.PostDetail.as_view(), name='comment'),
    path('profile/review/<int:pk>', views.AddComments.as_view(), name='add_comment'),
    #path('profile/<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('profile/<int:pk>/add_likes', views.hit_like_button, name='add_likes'),
    path('profile/<int:pk>/add_like', views.home_like_button, name='add_like'),
    path('profile/<int:pk>/del_post', views.PostDelete.as_view(), name='del_post'),

]


