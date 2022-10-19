from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('login/', views.user_login, name="user_login"),      
    path('logout/', views.user_logout, name="user_logout"),
    path('<int:pk>/', views.detail, name="detail"),
]
