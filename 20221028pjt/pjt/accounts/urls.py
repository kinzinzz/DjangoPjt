from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # 회원가입
    path("signup/", views.signup, name="signup"),
    # 로그인
    path("login/", views.user_login, name="user_login"),
    # 로그아웃
    path("logout/", views.user_logout, name="user_logout"),
    # 회원정보 조회
    path("<int:user_pk>/", views.user_detail, name="user_detail"),
    # 회원정보 변경
    path("<int:user_pk>/profile_change/", views.profile_change, name="profile_change"),
    # 비밀번호 변경
    path(
        "<int:user_pk>/password_change/", views.password_change, name="password_change"
    ),
    # 회원 탈퇴
    path("<int:user_pk>/user_delete/", views.user_delete, name="user_delete"),
    # 팔로우
    path("<int:user_pk>/follow/", views.follow, name="follow"),
]
