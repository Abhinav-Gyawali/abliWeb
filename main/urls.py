from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('password-reset/verify', views.handle_password_reset, name='handle_password_reset'),
]