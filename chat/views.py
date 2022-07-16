import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import Room
from django.contrib.auth.forms import UserCreationForm


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form':form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'registration/register.html', {'form':form})

class Index(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


class RoomView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    template_name = 'room.html'
    pk_url_kwarg = 'room_name'
    def get_object(self):
        room_name = self.kwargs.get(self.pk_url_kwarg)
        room_name = re.sub(r"\s|-", "_", room_name)         
        chat_room, created = Room.objects.get_or_create(name=room_name)
        return chat_room
