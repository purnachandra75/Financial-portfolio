from django.shortcuts import redirect, render
from django.views import View
from .forms import SavingsandgoalsDetails,RegisteSandGform
from .models import SavingandGoals,RegisterSavingsandGoals
def getSaveandGolepage(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    somedata=SavingandGoals.objects.filter(user_id=uid)
    return render(request,'savingsandgoals.html',{'user':user,'somedata':somedata})
def deleteSavingsandgoals(request,id):
    somedata=SavingandGoals.objects.filter(id=id)
    somedata.delete()
    return redirect('SavingeandGoal')

class CreateSavingsandGoals(View):
    def get(self,request):
        user=request.session.get('user')
        uid=request.session.get('uid')
        
        
        return render(request,'createSaveingsAndGoals.html',{'form':SavingsandgoalsDetails(request=request),'user':user})
    def post(self,request):
        uid=request.session.get('uid')
        user=request.session.get('user')
        somedata=SavingsandgoalsDetails(request.POST,request=request)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('SavingeandGoal')
        
class Updatesavingsandgoals(View):
    def get(self,request,id):
        user=request.session.get('user')
       
        somedat=SavingandGoals.objects.get(id=id)
        return render(request,'createSaveingsAndGoals.html',{'form':SavingsandgoalsDetails(request=request,instance=somedat),'user':user})
    
    def post(self,request,id):
        somedat=SavingandGoals.objects.get(id=id)
        newdata=SavingsandgoalsDetails(request.POST,instance=somedat,request=request)
        if newdata.is_valid():
            newdata.save()
            return redirect('SavingeandGoal')
        
def registerSaveingsandGoals(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    somedata=RegisterSavingsandGoals.objects.filter(user_id=uid)
    return render(request,'registerSaveings&goals.html',{'user':user,'somedata':somedata})
class CreategoalsRegister(View):
    def get(self,request):
        user=request.session.get('user')
        return render(request,'createSaveingsAndGoals.html',{'user':user,'form':RegisteSandGform()})
    def post(self,request):
        uid=request.session.get('uid')
        somedata=RegisteSandGform(request.POST)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('regiSavingsAndGoals')
        
class UpdateSandGRegister(View):
    def get(self,request,id):
        user=request.session.get('user')
        somedata=RegisterSavingsandGoals.objects.get(id=id)
        return render(request,'createSaveingsAndGoals.html',{'user':user,'form':RegisteSandGform(instance=somedata)})
    def post(self,request,id):
        somedata=RegisterSavingsandGoals.objects.get(id=id)
        somedata=RegisteSandGform(request.POST,instance=somedata)
        if somedata.is_valid():
            somedata.save()
            return redirect('regiSavingsAndGoals')
        
def deleteSandGRegi(request,id):
    somedata=RegisterSavingsandGoals.objects.get(id=id)
    somedata.delete()
    return redirect('regiSavingsAndGoals')
