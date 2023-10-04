from django.urls import path

from . import views

urlpatterns = [
    path("", views.teknik_main, name="teknik"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("admin-ayarları/", views.settings, name="settings"),
    path("parola-güncelle/", views.parola, name="parola"),
]