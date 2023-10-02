from django.db import models

# Create your models here.
class studentModel(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()