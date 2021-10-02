from django.shortcuts import render,redirect
from .models import student

# Create your views here.
def add(request):
    if request.method=='POST':
        un=request.POST['Username']
        firstname=request.POST['First_name']
        lastname=request.POST['Last_name']
        email=request.POST['Email_id']
        passwd=request.POST['Password']
        status=request.POST[' status']

        x=student(First_name=firstname,Last_name=lastname,Email_id= email,Password=passwd, status= status,Username=un)
        x.save()

    else:
        return render(request,'add.html')
