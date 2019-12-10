from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    message="<h3>Hello welcome to Django Project</h3>"
    return HttpResponse(message)
    
