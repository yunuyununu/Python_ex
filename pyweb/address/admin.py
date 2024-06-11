from django.contrib import admin
from address.models import Address
from guestbook.models import Guestbook

class AddressAdmin(admin.ModelAdmin):
    # 화면에 출력할 필드 목록을 튜플로 지정
    list_display = ('name','tel','email','address')
    # 듀플 수정 X 리스트 O
admin.site.register(Address,AddressAdmin)
# 관리자 화면에 등록
# Register your models here.
admin.site.register(Guestbook)
