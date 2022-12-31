from django.urls import path
from passwordless import views


urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'done/', views.done, name='done'),
    path(r'login-form/', views.login_form, name='login_form'),
    path(r'validation-sent/', views.validation_sent,
        name='validation_sent'),
    path(r'token-login/<slug:token>/', views.token_login,
        name='token_login'),
    path(r'logout/', views.logout, name='logout')
]
