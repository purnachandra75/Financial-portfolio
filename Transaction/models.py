from django.db import models
from usercradintials.models import Userdetails


# Create your models here.

class Transactions(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    
    transaction_type=models.CharField(max_length=20)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=40)
    date=models.DateField()
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

 