from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.Index.as_view(), name='chat-index'),
    path('<str:room_name>/', views.RoomView.as_view(), name='chat-room'),
]