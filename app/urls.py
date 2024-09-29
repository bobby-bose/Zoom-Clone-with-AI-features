from django.urls import path

from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('', views.LoginUserView.as_view(), name='login'),
    path('meeting/', views.meeting, name='meeting'),
    path('conference/', views.conference, name='conference'),
]