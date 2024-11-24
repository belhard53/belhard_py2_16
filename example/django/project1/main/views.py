from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello DJANGO")
    return render(request, 't1.html', context={'name':'name1'})


def hello1(request, count):
    return render(request, 't1.html', 
                  context={'name':'name1', 'count':'_'*count})