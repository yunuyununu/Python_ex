from django.shortcuts import render
from django.http import JsonResponse
from ajax.models import Keyword
from mymember.models import Member
import hashlib

def home(request):
    return render(request,'ajax/index.html')

def gugu(request):
    if request.method =="GET":
        return render(request,'ajax/gugu.html')
    elif request.method =="POST":
        num = int(request.POST['num'])
        result = ''
        for i in range(1,10):
            result += f'{num} x {i} = {num * i}<br>'
        return render(request, 'ajax/gugu_result.html',{'result':result})

def gugu_ajax(request):
    num = int(request.GET['num'])
    result = ''
    for i in range(1,10):
        result += f'{num} x {i} = {num * i}<br>'
    return JsonResponse({'result': result}) #결과출력영역에 찍히게됨

def login(request):
    return render(request, 'ajax/login.html')

def login_check(request):
    try:
        userid = request.GET['userid']
        passwd = request.GET['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest() #평문=>암호(암호화) ,암호+>평문(복호화)
        row = Member.objects.filter(userid=userid,passwd=passwd)[0] #테이블 모든 검색 [0]-첫번째레코드
        if row is not None:
            result = row.name + '님 환영합니다.'
        return JsonResponse({'result':result})
    except:
        return JsonResponse({'result':'아이디 또는 비밀번호가 일치하지 않습니다.'})

def keyword(request):
    return render(request, 'ajax/keyword.html')

def keyword_list(request):
    keyword = request.GET['search']
    rows = Keyword.objects.filter(word__contains=keyword).all()
    #print(rows)
    #print(rows.values)
    rows = list(rows.values())
    #print(rows)
    items = []
    for row in rows:
        items.append(row['word'].replace(keyword,"<span style='color:red'>"+keyword+"</span>"))
    print(items)
    return JsonResponse(items,safe=False)