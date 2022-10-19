from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('prfile_update/<int:pk>', views.profile_update, name='profile_update'),
]
