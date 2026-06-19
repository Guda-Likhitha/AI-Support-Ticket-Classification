from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'create/',
        views.create_ticket,
        name='create_ticket'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),
]