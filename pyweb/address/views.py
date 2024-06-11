from django.shortcuts import redirect,render
from address.models import Address

def home(request):
    items = Address.objects.order_by("name")
    return render(request,'address/list.html',{'items':items,'address_count':len(items)})

def write(request):
    return render(request,"address/write.html")

def insert(request):
    addr = Address(name=request.POST['name'],tel=request.POST['tel'],email=request.POST['email'],address=request.POST['address'])
    addr.save()
    return redirect("/address/")

def detail(request):
    addr = Address.objects.get(idx=request.GET['idx'])
    return render(request,'address/detail.html',{'addr':addr})

def update(request):
    addr = Address(idx=request.POST['idx'], name=request.POST['name'], tel=request.POST['tel'], email=request.POST['email'], address=request.POST['address'])
    addr.save()
    return redirect("/address/")

def delete(request):
    Address.objects.get(idx=request.POST['idx']).delete()
    return redirect("/address/")