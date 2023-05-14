from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #social media
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('settings', views.settings, name='settings'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('pwdlist', views.pwdlist, name="pwdlist"),
    path('aboutus', views.aboutus, name='aboutus'),

    #lessons
    path('ps', views.ps, name='ps'),
    path('pc', views.pc, name='pc'),
    path('pl', views.pl, name='pl'),
    path('pp', views.pp, name='pp'),
]