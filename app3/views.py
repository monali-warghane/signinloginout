from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        passwd=request.POST['password']
        x=User.objects.create_user(username=username,password= passwd)
        x.save()
        return redirect('signup')


    else:
        return render(request,'signup.html')