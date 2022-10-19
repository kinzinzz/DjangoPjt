from django.urls import path
from . import views

app_name="articles"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/comments/', views.add_comment, name="add_comment"),    
    path('<int:article_pk>/comments/<int:comment_pk>delete_comments/', views.delete_comment, name="delete_comment"),    
]
