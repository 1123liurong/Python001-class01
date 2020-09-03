from django.db import models

# Create your models here.

class Type(models.Model):
  #id=models.AutoField(primary_key = True) ，Django会自动创建id并设置为主键
  typename = models.CharField(max_length=20)
# 短评对应星级  

class Shorts(models.Model):  
  starts = models.CharField(max_length=50)
  num = models.CharField(max_length=5)
  details = models.CharField(max_length=200)
  times = models.CharField(max_length=20)

