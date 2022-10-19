from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("index/", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("password_change/", views.password_change, name="password_change"),
    path("delete/", views.delete, name="delete"),
    path("search/", views.search, name="search"),
]
