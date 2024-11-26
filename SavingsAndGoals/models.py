from django.db import models
from usercradintials.models import Userdetails

# Create your models here.


class SavingandGoals(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    goal_name=models.CharField(max_length=20,blank=False)
    target_amount=models.DecimalField(max_digits=20,decimal_places=2)
    current_amount=models.DecimalField(max_digits=20,decimal_places=2)
    deadline=models.DateField()
    crated_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class RegisterSavingsandGoals(models.Model):
    user=models.ForeignKey(Userdetails,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    
    

