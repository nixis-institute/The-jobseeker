from django.db import models
from django.contrib.auth.models import auth
from datetime import datetime,date
from django.contrib.auth.models import User
# from django.db import models

class create(models.Model):
    name = models.CharField(max_length=50)
    addres = models.TextField(blank=True,null=True)
    contact = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    org_name = models.CharField(max_length=50,blank=True,null=True)
    jobs = models.TextField(blank=True,null=True)
    us = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    tm = models.DateField(default=date.today())
    exp = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.jobs


class JOBS(models.Model):
    jbs = models.TextField(blank=True,null=True)
    tm = models.DateTimeField(default=datetime.now())
    us = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.jbs

