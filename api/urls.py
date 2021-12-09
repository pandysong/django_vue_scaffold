from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.handle_upload, name='api-upload'),
    path('csrf', views.get_csrf, name='api-csrf'),
]
