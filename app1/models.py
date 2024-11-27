from django.db import models

# Create your models here.
class users(models.Model):
    uname=models.CharField(max_length=20,primary_key=True)
    email=models.EmailField()
    pass1=models.CharField(max_length=20)
    pass2=models.CharField(max_length=20)
 