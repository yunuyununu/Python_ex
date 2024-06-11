from django.contrib import admin
from survey.models import Survey, Answer

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("question","ans1","ans2","ans3","ans4","status")
    #관리자화면 필드목록

admin.site.register(Survey, SurveyAdmin) #(테이블,화면)
admin.site.register(Answer)