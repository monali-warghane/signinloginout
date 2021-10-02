from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        passwd=request.POST['password']
        user=auth.authenticate(username=username,password=passwd)
        if user is not None:
            return redirect('/')
        else:
            return redirect('login')

    else:
        return render(request,'login.html')
