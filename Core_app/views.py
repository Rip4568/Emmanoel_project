from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
class TesteView(View):
    PATH_TEMPLATE = "Core_app/teste.html"
    def get(self, request, *args, **kwargs):
        send_mail(
            from_email='jhone.test14@gmail.com',
            recipient_list=['SocialSiteManel22@gmail.com'],
            message='foi',
            subject='subject de que ?',
            fail_silently=False,
        )
        return render(request, template_name=self.PATH_TEMPLATE, context={})

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        if password == 'teste' and username == 'teste':
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return 'error'
            login(request, user)
            return user
        return redirect(reverse('Core_app:teste'))


def index(request):
    TEMPLATE_PATH = 'Core_app/index.html'
    return render(request,TEMPLATE_PATH,context={})

def room(request, room_name):
    TEMPLATE_PATH = 'Core_app/chat.html'
    return render(request,TEMPLATE_PATH,context={"room_name":room_name})
