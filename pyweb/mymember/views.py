from django.shortcuts import render, redirect
from mymember.models import Member
import hashlib

def home(request):
    if 'userid' not in request.session.keys():
        return render(request, 'mymember/login.html')
    else:
        return render(request, 'mymember/main.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
#csrf 토큰 검사 면제
def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest()

        row = Member.objects.filter(userid=userid, passwd=passwd) #레코드검색
        if len(row) > 0:
            row = Member.objects.filter(userid=userid, passwd=passwd)[0]
            request.session['userid'] = userid
            request.session['name'] = row.name  #세션변수 저장
            return render(request, 'mymember/main.html')
        else:
            return render(request,'mymember/login.html',
                          {'msg':'아이디 또는 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request,'mymember/login.html')

def join(request):
    if request.method == 'POST':  #양식을 채우고 제출
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest() #비밀번호 암호화
        name = request.POST['name']
        address = request.POST['address']
        tel = request.POST['tel']
        Member(userid=userid, passwd=passwd, name=name, address=address, tel=tel).save()  #레코드에 저장
        request.session['userid'] = userid
        request.session['name'] = name
        return render(request, 'mymember/main.html')
    else:
        return render(request, 'mymember/join.html')

def logout(request):
    request.session.clear()  #세션변수 삭제
    return redirect('/mymember')  #다시홈으로


