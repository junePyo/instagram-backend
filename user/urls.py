from django.urls import path
from user import views

urlpatterns = [
    path('/<int:account_pk>', views.profile, name='user-profile'),
    path('/login', views.LoginView.as_view(), name='user-login'),
    path('/logout', views.logout, name='user-logout'),
    path('/register', views.RegisterView.as_view(), name='user-register'),
    path('/main', views.mainView, name='user-main'),
]
