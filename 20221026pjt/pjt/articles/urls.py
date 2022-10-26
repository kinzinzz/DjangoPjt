from django.urls import path
from . import views

app_name="articles"

urlpatterns = [
    # 게시글 작성 페이지
    path('create/', views.create, name="create"),
    # 코멘트 작성 페이지
    path('<int:article_pk>/comment_create/', views.comment_create, name="comment_create")
]   
