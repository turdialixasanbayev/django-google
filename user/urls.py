from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('profile/', views.profile_page, name="profile"),
    path("login/", views.login_page, name="login"),
]
