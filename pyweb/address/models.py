from django.db import models
#이름,전화,이메일,주소
class Address(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    tel = models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)

# Create your models here.
