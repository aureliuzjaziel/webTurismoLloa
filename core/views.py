from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request): 
    return render(request,'core/index.html')

def users(request): 
    return render(request,'core/users.html')


