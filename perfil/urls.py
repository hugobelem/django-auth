from django.urls import path

from . import views

app_name = 'perfil'
urlpatterns = [
    path('', views.update_user, name='perfil'),
]
