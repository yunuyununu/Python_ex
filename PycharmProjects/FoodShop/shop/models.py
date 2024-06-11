from django.db import models

class Member(models.Model):
    userid = models.CharField(max_length=50, null=False, primary_key=True)
    passwd = models.CharField(max_length=500, null=False)
    name = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    tel = models.CharField(max_length=20, null=True)


class Chat(models.Model):  # 대화내용저장
    idx = models.AutoField(primary_key=True)  # 자동증가 일련번호
    userid = models.CharField(max_length=50, null=False)
    query = models.CharField(max_length=500, null=False)
    answer = models.CharField(max_length=1000, null=False)
    intent = models.CharField(max_length=50, null=False)
