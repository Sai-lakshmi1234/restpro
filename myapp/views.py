from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def menu(request):
    return render(request,'menu.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')