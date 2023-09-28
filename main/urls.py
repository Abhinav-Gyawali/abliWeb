from django.urls import path
from . import views

urlpatterns = [
    path('/',view.home,name="home"),
    path('reset-password/<str:oob_code>/', views.handle_password_reset, name='handle_password_reset'),
]