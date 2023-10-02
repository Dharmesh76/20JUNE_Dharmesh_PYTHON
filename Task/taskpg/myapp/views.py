from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def signup(request):
    if request.method=='POST':
        user=signUPform(request.POST)
        if user.is_valid():
            user.save()
            print("data submitted")
        else:
            print(user.errors)    
    return render(request,'signup.html')

def showdata(request):
    data=studentModel.objects.all()
    return render (request,'showdata.html',{'data':data})

def deletedata(request,id):
    udata=studentModel.objects.get(id=id)
    studentModel.delete(udata)
    return redirect('showdata')

def updatedata(request,uid):
    udata=studentModel.objects.get(id=uid)
    if request.method=='POST':
        user=updateForm(request.POST,instance=udata)
        if user.is_valid():
            user.save()
        else:
            print(user.errors)
    return render(request,'updatedata.html',{'udata':udata})            

