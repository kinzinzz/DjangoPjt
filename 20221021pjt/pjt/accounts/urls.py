from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('<int:user_pk>/detail/', views.user_detail, name="user_detail"),
    path('<int:user_pk>/update/', views.user_update, name="user_update"),
    path('<int:user_pk>/password_change/', views.password_change, name="password_change"),
    path('<int:user_pk>/delete/', views.delete, name="delete"),
]
