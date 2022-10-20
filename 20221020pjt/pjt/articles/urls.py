from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
   path('', views.index, name="index"),
   path('create/', views.create, name="create"),
   path('<int:article_pk>/delete/', views.delete_article, name="delete_article"),
   path('<int:article_pk>/update/', views.update, name="update"),
   path('<int:article_pk>/', views.article_detail, name="article_detail"),
   path('<int:article_pk>/commnents/create/', views.add_comment, name="add_comment"),
   path('<int:article_pk>/commnents/<int:comment_pk>/delete/', views.delete_comment, name="delete_comment"),
]