from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('story/', views.story, name='story'),
    path('single-story/', views.single_story, name='single_story'),
    path('game/', views.game, name='game'),
    path('parent/', views.parent, name='parent'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('bk-admin', views.custom_admin, name='custom_admin'),
]

