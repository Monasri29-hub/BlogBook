from django.urls import path
from . import views

urlpatterns = [
    #path('', views.test),
    path('login/', views.user_login),
    path('', views.signup),
    path('home/', views.home),
    path('newpost/', views.newpost),
    path('myposts/', views.myposts),
    path('signout/', views.signout),
]