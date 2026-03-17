from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    # return HttpResponse(u'Привет, Мир!') 

    return render(request, 'static_handler.html')