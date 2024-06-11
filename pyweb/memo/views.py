from django.shortcuts import render,redirect
from memo.models import Memo

def home(request):
    memoList = Memo.objects.order_by("-idx") #내림차순 ("idx")=>오름차순
    #       클래스 모든      정렬
    return render(request, 'memo/list.html',{'memoList':memoList, 'memoCount':len(memoList)})
    #화면전환 (render=>html완성시켜라)                                   변수명  데이터

def insert_memo(request): #폼데이터
    memo=Memo(writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect("/memo") #http:/localhost/memo로 이동

def detail_memo(request):
    row = Memo.objects.get(idx=request.GET['idx'])
    return render(request, 'memo/detail.html',{'row':row})

def update_memo(request):
    memo = Memo(idx=request.POST['idx'], writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect("/memo")

def delete_memo(request):
    Memo.objects.get(idx=request.POST['idx']).delete()
    return redirect("/memo")