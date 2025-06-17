from django.urls import path

from . import views

app_name = 'powerups'
urlpatterns = [
    path('', views.index, name='index'),
    path('all/<str:order>/', views.AllPowerupsView.as_view(), name='all'),
    path('sort', views.sort, name='sort'),
    path('users/', views.AllUsersView.as_view(), name='users'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('<int:pk>/', views.PowerUpDetailView.as_view(), name='powerup_detail'),
    path('add_powerup', views.addPowerup, name='add_powerup'),
    path('create', views.create, name='create')
]