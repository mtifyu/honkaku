from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.login, name='registration'),
    path('profile/', views.login, name='profile'),
    path('logout/', views.login, name='logout'),
]
