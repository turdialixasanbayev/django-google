from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.index_view,
        name='home',
    ),
    path(
        'profile/',
        views.profile,
        name="profile",
    ),
    path("login/", views.login_page, name="login"),
]
