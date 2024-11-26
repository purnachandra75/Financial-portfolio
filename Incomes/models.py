from django.db import models

# Create your models here.
from django.db import models
from usercradintials.models import Userdetails
class RegisterIncome(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    
class IncomeSource(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    source=models.CharField(max_length=40,blank=False)
    frea=[
        ('one_time','one_time'),
        ('monthly','monthly'),
        ('Quarterly','Quarterly'),
        ('Halfyealy','Halfyealy'),
        ('Yearly','Yearly')
    ]
    frequency=models.CharField(max_length=20,choices=frea)
    description=models.TextField()
    date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
