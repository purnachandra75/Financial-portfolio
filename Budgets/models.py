from django.db import models
from usercradintials.models import Userdetails
# Create your models here.
class Budgets(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    category=models.CharField(max_length=20,blank=False)
    limit=models.DecimalField(max_digits=10,decimal_places=2)
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class RegisterBudget(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)