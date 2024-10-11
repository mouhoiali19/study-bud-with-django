from django.urls import path
from base import views

urlpatterns = [
    path('login/' , views.loginPage, name="login"),
    path('logout/' , views.logoutuser, name="logout"),
    path('register/' , views.registerpage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/' , views.createRoom,name="create-room"),
    path('update-room/<str:pk>' , views.UpdateRoom,name="update-room"),
    path('delete-room/<str:pk>' , views.deleteRoom,name="delete-room"),
   
]
