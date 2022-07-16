from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='chat-index'),
    path('<str:room_name>/', views.RoomView.as_view(), name='chat-room'),
]