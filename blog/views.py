from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'blog/index.html')
def page1(request):
    return render(request,'blog/page1.html')
def page2(request):
    return render(request,'blog/page2.html')