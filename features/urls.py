from django.urls import path
from features import views

urlpatterns = [
    path('/comments', views.getComments, name='features-comments'),
    path('/comments/write/<int:account_pk>', views.postComments,
         name='features-comments_post'),
]
