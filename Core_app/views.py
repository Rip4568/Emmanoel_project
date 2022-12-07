from django.shortcuts import render

def index(request):
    TEMPLATE_PATH = 'Core_app/index.html'
    return render(request,TEMPLATE_PATH,context={})

def room(request, room_name):
    TEMPLATE_PATH = 'Core_app/chat.html'
    return render(request,TEMPLATE_PATH,context={"room_name":room_name})