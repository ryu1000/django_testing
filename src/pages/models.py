from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(User, on_delete=models.CASCADE)