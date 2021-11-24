from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_crypto, name='all_crypto'),
]
