from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('primary-data', views.fetch_primary_data, name='primary-data')
]
