from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload/', views.upload_view, name='upload'),
    path('result/<int:pk>/', views.result_view, name='result'),
    path('list/', views.list_view, name='list'),
]