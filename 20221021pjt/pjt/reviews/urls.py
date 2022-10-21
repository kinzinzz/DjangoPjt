from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
   path('create/', views.review_create, name="review_create"),
   # review
   path('index/', views.index, name="index"),
   path('<int:review_pk>/', views.review_detail, name="review_detail"),
   path('<int:review_pk>/upadte/', views.review_update, name="review_update"),
   path('<int:review_pk>/delete/', views.review_delete, name="review_delete"),
   # comment
   path('<int:review_pk>/comments/', views.comment_add, name="comment_add"),
   path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name="comment_delete"),
   path('<int:review_pk>/comments/<int:comment_pk>/update/', views.comment_update, name="comment_update"),
]
