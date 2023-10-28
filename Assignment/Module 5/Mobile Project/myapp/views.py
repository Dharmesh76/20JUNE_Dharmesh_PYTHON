from django.shortcuts import render,redirect
from .form import *
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def siteadmin(request):
    return render(request,'admin.html')

def sitemanager(request):
    data=""
    if request.method=='POST':
        search=request.POST['s']
        try:
            data=product_sub_category_details.objects.get(product_model=search)
        except:    
            messages.add_message(request, messages.INFO, "Product Not Available")
    if data:
        data=data
    else:
        data=("none")
    return render(request,'manager.html',{'data':data})

def adddata(request):
    data=Product_mst.objects.all()
    if request.method=='POST':
        user=adddataform(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            print("data Added")
        else:
            print(user.errors)

    return render(request,'adddata.html',{'data':data}) 


def viewdata(request):
    data=product_sub_category_details.objects.all()
    productdata=Product_mst.objects.all()
    return render(request,'viewdata.html',{'data':data})

def deleteview(request):
    data=product_sub_category_details.objects.all()
    return render(request,'deletedata.html',{'data':data})

def deletedata(request,id):
    data=product_sub_category_details.objects.get(id=id)
    product_sub_category_details.delete(data)
    return redirect('deleteview')