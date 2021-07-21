from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

# Create your models here.

class Consumer(models.Model):
	username = models.CharField(max_length=30)#ForeignKey(User, on_delete=models.CASCADE)
	residence = models.CharField(max_length=50, default=None)
	gasValue = models.CharField(max_length=5, default=0)
	leakagecase = models.CharField(max_length=3, default=0)
	date = models.DateTimeField(default=timezone.now)
