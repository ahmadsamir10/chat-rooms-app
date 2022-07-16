import re
from django.shortcuts import render
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import Message, Room


class Index(View):
    #login_url = ''
    def get(self, request):
        return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


class RoomView(DetailView):
    template_name = 'room.html'
    pk_url_kwarg = 'room_name'
    def get_object(self):
        room_name = self.kwargs.get(self.pk_url_kwarg)
        room_name = re.sub(r"\s|-", "_", room_name)         
        chat_room, created = Room.objects.get_or_create(name=room_name)
        return chat_room
