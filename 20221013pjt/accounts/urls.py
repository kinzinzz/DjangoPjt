from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('',views.user_list, name='user_list'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('<int:pk>/update/', views.update, name='update'),
    #비밀번호 변경
    path('password/', views.change_password, name='change_password'),
    #탈퇴
    path('delete/', views.delete, name="delete"),
    #회원 검색
    path('search/', views.search, name='search'),
]
