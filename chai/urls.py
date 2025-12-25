from django.urls import path

from .import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('order/', views.order_chai, name='order_chai')
]