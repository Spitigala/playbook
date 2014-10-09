# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def players(request):
    html = "<html><body><p>Hello World. You're at players.</p></body></html>"
    return HttpResponse(html)

def index(request):
    html = "<html><body><p>Hello World. You're at index.</p></body></html>"
    return HttpResponse(html)