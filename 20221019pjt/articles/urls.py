from django.urls import path
from . import views

app_name="articles"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:article_pk>/', views.detail, name="detail"),
    path('<int:article_pk>/add_comment/', views.add_comment, name="add_comment"),
    path('<int:article_pk>/delete_comment/<int:comment_pk>/', views.delete_comment, name="delete_comment"),
]
