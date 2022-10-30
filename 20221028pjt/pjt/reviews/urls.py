from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # 리뷰
    # 목록조회
    path("", views.index, name="index"),
    # 게시물 생성
    path("create/", views.create, name="create"),
    # 게시물 조회
    path("<int:review_pk>/", views.detail, name="detail"),
    # 게시물 수정
    path("<int:review_pk>/update/", views.update, name="update"),
    # 게시물 삭제
    path("<int:review_pk>/delete/", views.delete, name="delete"),
    # 게시물 좋아요
    path("<int:review_pk>/like/", views.like, name="like"),
    # 게시물 '제목'검색
    path('search/', views.search, name='search'),
    # 댓글
    # 댓글 작성
    path(
        "<int:review_pk>/comments/create/",
        views.comments_create,
        name="comments_create",
    ),
    # 댓글 삭제
    path(
        "<int:review_pk>/comments/<int:comment_pk>/delete/",
        views.comments_delete,
        name="comments_delete",
    ),
]
