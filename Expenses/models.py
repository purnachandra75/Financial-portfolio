from django.db import models
from usercradintials.models import Userdetails
# Create your models here.

class ExpensesInfo(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=20,blank=False)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)
    is_recurring=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class ExpensesRegister(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    frea=[
        ('one_time','one_time'),
        ('monthly','monthly'),
        ('Quarterly','Quarterly'),
        ('Halfyealy','Halfyealy'),
        ('Yearly','Yearly')
    ]
    type=models.CharField(max_length=100,choices=frea)