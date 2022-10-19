from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("<int:review_pk>/", views.detail, name="detail"),
    path("<int:review_pk>/update/", views.update, name="update"),
    path("<int:review_pk>/delete/", views.delete, name="delete"),
    path("search/", views.search, name="search"),
    # 댓글
    path("<int:pk>/add_comment/", views.add_comment, name="add_comment"),
    path("<int:pk>/comment_remove/", views.comment_remove, name="comment_remove"),
    path("<int:pk>/comment_modify/", views.comment_modify, name="comment_modify"),
]
